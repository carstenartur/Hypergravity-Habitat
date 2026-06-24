#!/usr/bin/env python3
"""
Hypergravity Habitat sizing model.

This script calculates first-order parameter tables for terrestrial circular
hypergravity concepts. It uses a vector-corrected model: Earth gravity and
centripetal acceleration are treated as perpendicular components.

The script is intentionally dependency-free so it can run in any standard
Python 3 environment.

Examples
--------
Print default markdown tables:

    python calculations/hypergravity_sizing.py

Use custom target resultant-g values and radii:

    python calculations/hypergravity_sizing.py --g-levels 1.05 1.10 1.20 --radii 100 250 500

Export CSV:

    python calculations/hypergravity_sizing.py --format csv
"""

from __future__ import annotations

import argparse
import csv
import math
import sys
from dataclasses import dataclass
from typing import Iterable, List

STANDARD_GRAVITY = 9.80665  # m/s^2


@dataclass(frozen=True)
class SizingResult:
    """One sizing result for a target resultant-g level and radius."""

    target_g: float
    radius_m: float
    lateral_acceleration_mps2: float
    lateral_acceleration_g: float
    speed_mps: float
    speed_kmh: float
    angular_velocity_rad_s: float
    rpm: float
    lap_time_s: float
    circumference_m: float
    bank_angle_deg: float


def lateral_acceleration_for_resultant_g(target_g: float, g0: float = STANDARD_GRAVITY) -> float:
    """
    Return lateral centripetal acceleration needed for a target resultant g.

    For a terrestrial circular platform:

        g_eff = sqrt(g0^2 + a_c^2)

    If target_g is expressed as multiples of g0, then:

        a_c = g0 * sqrt(target_g^2 - 1)

    Parameters
    ----------
    target_g:
        Desired resultant effective gravity in multiples of Earth gravity.
        Must be >= 1.0.
    g0:
        Reference gravitational acceleration in m/s^2.
    """
    if target_g < 1.0:
        raise ValueError("target_g must be >= 1.0 for a terrestrial hypergravity concept")
    return g0 * math.sqrt(target_g * target_g - 1.0)


def calculate_result(target_g: float, radius_m: float, g0: float = STANDARD_GRAVITY) -> SizingResult:
    """Calculate sizing parameters for one target resultant-g and radius."""
    if radius_m <= 0:
        raise ValueError("radius_m must be positive")

    a_c = lateral_acceleration_for_resultant_g(target_g, g0=g0)
    speed_mps = math.sqrt(a_c * radius_m) if a_c > 0 else 0.0
    circumference_m = 2.0 * math.pi * radius_m
    omega = speed_mps / radius_m if radius_m > 0 else 0.0
    rpm = omega * 60.0 / (2.0 * math.pi)
    lap_time_s = circumference_m / speed_mps if speed_mps > 0 else math.inf
    bank_angle_deg = math.degrees(math.atan2(a_c, g0))

    return SizingResult(
        target_g=target_g,
        radius_m=radius_m,
        lateral_acceleration_mps2=a_c,
        lateral_acceleration_g=a_c / g0,
        speed_mps=speed_mps,
        speed_kmh=speed_mps * 3.6,
        angular_velocity_rad_s=omega,
        rpm=rpm,
        lap_time_s=lap_time_s,
        circumference_m=circumference_m,
        bank_angle_deg=bank_angle_deg,
    )


def generate_results(g_levels: Iterable[float], radii: Iterable[float]) -> List[SizingResult]:
    """Generate results for all combinations of target g levels and radii."""
    results: List[SizingResult] = []
    for target_g in g_levels:
        for radius_m in radii:
            results.append(calculate_result(target_g=target_g, radius_m=radius_m))
    return results


def format_markdown(results: List[SizingResult]) -> str:
    """Return results as a Markdown table."""
    lines = [
        "| target resultant g | radius m | circumference km | lateral g | speed km/h | rpm | lap time s | bank angle deg |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in results:
        lines.append(
            "| "
            f"{r.target_g:.2f} | "
            f"{r.radius_m:.0f} | "
            f"{r.circumference_m / 1000.0:.2f} | "
            f"{r.lateral_acceleration_g:.3f} | "
            f"{r.speed_kmh:.1f} | "
            f"{r.rpm:.3f} | "
            f"{r.lap_time_s:.1f} | "
            f"{r.bank_angle_deg:.1f} |"
        )
    return "\n".join(lines)


def write_csv(results: List[SizingResult]) -> None:
    """Write results as CSV to stdout."""
    writer = csv.writer(sys.stdout)
    writer.writerow(
        [
            "target_resultant_g",
            "radius_m",
            "circumference_m",
            "lateral_acceleration_mps2",
            "lateral_acceleration_g",
            "speed_mps",
            "speed_kmh",
            "angular_velocity_rad_s",
            "rpm",
            "lap_time_s",
            "bank_angle_deg",
        ]
    )
    for r in results:
        writer.writerow(
            [
                f"{r.target_g:.6g}",
                f"{r.radius_m:.6g}",
                f"{r.circumference_m:.6g}",
                f"{r.lateral_acceleration_mps2:.6g}",
                f"{r.lateral_acceleration_g:.6g}",
                f"{r.speed_mps:.6g}",
                f"{r.speed_kmh:.6g}",
                f"{r.angular_velocity_rad_s:.6g}",
                f"{r.rpm:.6g}",
                f"{r.lap_time_s:.6g}",
                f"{r.bank_angle_deg:.6g}",
            ]
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Hypergravity Habitat first-order sizing model")
    parser.add_argument(
        "--g-levels",
        type=float,
        nargs="+",
        default=[1.05, 1.10, 1.20, 1.25, 1.50],
        help="Target resultant effective gravity levels in multiples of Earth gravity",
    )
    parser.add_argument(
        "--radii",
        type=float,
        nargs="+",
        default=[100, 200, 400, 500, 1000, 2000],
        help="Candidate radii in metres",
    )
    parser.add_argument(
        "--format",
        choices=["markdown", "csv"],
        default="markdown",
        help="Output format",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        results = generate_results(g_levels=args.g_levels, radii=args.radii)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.format == "csv":
        write_csv(results)
    else:
        print("# Hypergravity Habitat sizing table")
        print()
        print("Model: terrestrial circular platform with vector-combined Earth gravity and centripetal acceleration.")
        print()
        print(format_markdown(results))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
