#!/usr/bin/env python3
"""
First-order Coriolis projectile deflection estimator.

This script estimates the order-of-magnitude lateral deflection of a thrown or
kicked projectile inside a rotating or circular Hypergravity Habitat concept.

It is intended for concept screening only. It does not model drag, spin,
Magnus effect, launch angle, bounce, target height, or exact 3D geometry.

The first-order worst-case estimate is:

    y ~= Omega * L^2 / v

where:
    y      lateral deflection relative to the rotating frame [m]
    Omega  platform angular rate [rad/s]
    L      projectile range [m]
    v      projectile speed [m/s]

For a terrestrial circular platform, Omega can be derived from a target
resultant effective gravity and radius:

    a_c = g * sqrt(g_rel^2 - 1)
    Omega = sqrt(a_c / r)

Use this script to compare rough radius requirements for sports-like tasks.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import Iterable, List

STANDARD_GRAVITY = 9.80665


@dataclass(frozen=True)
class CoriolisScenario:
    target_g: float
    radius_m: float
    range_m: float
    projectile_speed_mps: float
    lateral_acceleration_g: float
    angular_rate_rad_s: float
    rpm: float
    estimated_deflection_m: float
    flight_time_s: float


def lateral_acceleration_for_resultant_g(target_g: float, g0: float = STANDARD_GRAVITY) -> float:
    if target_g < 1.0:
        raise ValueError("target_g must be >= 1.0")
    return g0 * math.sqrt(target_g * target_g - 1.0)


def angular_rate_for_radius(target_g: float, radius_m: float) -> float:
    if radius_m <= 0:
        raise ValueError("radius_m must be positive")
    a_c = lateral_acceleration_for_resultant_g(target_g)
    return math.sqrt(a_c / radius_m)


def estimate_deflection(omega: float, range_m: float, projectile_speed_mps: float) -> float:
    if range_m < 0:
        raise ValueError("range_m must be non-negative")
    if projectile_speed_mps <= 0:
        raise ValueError("projectile_speed_mps must be positive")
    return omega * range_m * range_m / projectile_speed_mps


def required_radius_for_deflection(
    target_g: float,
    range_m: float,
    projectile_speed_mps: float,
    allowed_deflection_m: float,
) -> float:
    """Return radius needed to keep first-order deflection below a threshold."""
    if allowed_deflection_m <= 0:
        raise ValueError("allowed_deflection_m must be positive")
    omega_max = allowed_deflection_m * projectile_speed_mps / (range_m * range_m)
    a_c = lateral_acceleration_for_resultant_g(target_g)
    return a_c / (omega_max * omega_max)


def scenario(target_g: float, radius_m: float, range_m: float, speed_mps: float) -> CoriolisScenario:
    a_c = lateral_acceleration_for_resultant_g(target_g)
    omega = angular_rate_for_radius(target_g, radius_m)
    rpm = omega * 60.0 / (2.0 * math.pi)
    flight_time = range_m / speed_mps
    y = estimate_deflection(omega, range_m, speed_mps)
    return CoriolisScenario(
        target_g=target_g,
        radius_m=radius_m,
        range_m=range_m,
        projectile_speed_mps=speed_mps,
        lateral_acceleration_g=a_c / STANDARD_GRAVITY,
        angular_rate_rad_s=omega,
        rpm=rpm,
        estimated_deflection_m=y,
        flight_time_s=flight_time,
    )


def format_markdown(rows: List[CoriolisScenario]) -> str:
    lines = [
        "| target g | radius m | range m | speed m/s | rpm | flight time s | estimated deflection m |",
        "|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| "
            f"{row.target_g:.2f} | "
            f"{row.radius_m:.0f} | "
            f"{row.range_m:.1f} | "
            f"{row.projectile_speed_mps:.1f} | "
            f"{row.rpm:.3f} | "
            f"{row.flight_time_s:.2f} | "
            f"{row.estimated_deflection_m:.2f} |"
        )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Estimate first-order Coriolis deflection for projectile tasks")
    parser.add_argument("--target-g", type=float, default=1.10, help="Target resultant effective gravity in g")
    parser.add_argument(
        "--radii",
        type=float,
        nargs="+",
        default=[100, 200, 500, 1000, 2000, 5000, 10000],
        help="Candidate radii in metres",
    )
    parser.add_argument("--range", dest="range_m", type=float, default=20.0, help="Projectile range in metres")
    parser.add_argument("--speed", dest="speed_mps", type=float, default=20.0, help="Projectile speed in m/s")
    parser.add_argument(
        "--allowed-deflection",
        type=float,
        default=None,
        help="Optional allowed deflection in metres; prints required radius",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    rows = [scenario(args.target_g, radius, args.range_m, args.speed_mps) for radius in args.radii]

    print("# Coriolis projectile deflection estimate")
    print()
    print("Model: first-order worst-case y ~= Omega * L^2 / v")
    print()
    print(format_markdown(rows))

    if args.allowed_deflection is not None:
        radius_required = required_radius_for_deflection(
            target_g=args.target_g,
            range_m=args.range_m,
            projectile_speed_mps=args.speed_mps,
            allowed_deflection_m=args.allowed_deflection,
        )
        omega_max = args.allowed_deflection * args.speed_mps / (args.range_m * args.range_m)
        rpm_max = omega_max * 60.0 / (2.0 * math.pi)
        print()
        print("## Radius requirement")
        print()
        print(
            f"To keep deflection <= {args.allowed_deflection:.3g} m "
            f"over {args.range_m:.1f} m at {args.speed_mps:.1f} m/s "
            f"for target {args.target_g:.2f} g, first-order radius requirement is "
            f"approximately {radius_required:.0f} m ({radius_required / 1000.0:.2f} km)."
        )
        print(f"Corresponding maximum angular rate: {rpm_max:.3f} rpm.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
