#!/usr/bin/env python3
"""
Railway g-envelope screening model for Hypergravity Habitat concepts.

This script estimates a first-order corridor for achievable resultant effective
gravity in a rail-based circular platform using track cant, cant deficiency,
optional carbody tilt, and optional internal floor tilt.

It is not a railway certification tool. It is a concept-screening tool that
helps identify when a target g-level is far outside conventional rail practice.

Source basis:
- docs/physics-reference.md
- docs/engineering/tilting-train-and-cant-limits.md
- 49 CFR 213.329 for example regulatory limits and safety criteria

Definitions
-----------
q = a_c / g  (lateral acceleration ratio)
G = sqrt(1 + q^2)  (resultant effective gravity in multiples of g)
theta = atan(q)  (resultant-vector angle from vertical)

For standard-gauge track, a simple rail-equivalent lateral ratio can be
screened as:

q_track ~= (cant + cant_deficiency) / gauge

where cant and cant deficiency are expressed as height differences.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import List

STANDARD_GAUGE_M = 1.435


@dataclass(frozen=True)
class EnvelopeCase:
    name: str
    cant_mm: float
    cant_deficiency_mm: float
    carbody_tilt_deg: float
    internal_floor_tilt_deg: float
    track_lateral_g: float
    track_resultant_g: float
    track_resultant_angle_deg: float
    cabin_alignment_angle_deg: float
    cabin_alignment_resultant_g: float
    equivalent_total_cant_mm: float


def resultant_g_from_lateral_ratio(q: float) -> float:
    return math.sqrt(1.0 + q * q)


def angle_deg_from_lateral_ratio(q: float) -> float:
    return math.degrees(math.atan(q))


def lateral_ratio_from_angle_deg(angle_deg: float) -> float:
    return math.tan(math.radians(angle_deg))


def target_equivalent_cant_mm(target_resultant_g: float, gauge_m: float = STANDARD_GAUGE_M) -> float:
    if target_resultant_g < 1.0:
        raise ValueError("target_resultant_g must be >= 1.0")
    q = math.sqrt(target_resultant_g * target_resultant_g - 1.0)
    return q * gauge_m * 1000.0


def make_case(
    name: str,
    cant_mm: float,
    cant_deficiency_mm: float,
    carbody_tilt_deg: float = 0.0,
    internal_floor_tilt_deg: float = 0.0,
    gauge_m: float = STANDARD_GAUGE_M,
) -> EnvelopeCase:
    q_track = (cant_mm + cant_deficiency_mm) / 1000.0 / gauge_m
    track_g = resultant_g_from_lateral_ratio(q_track)
    track_angle = angle_deg_from_lateral_ratio(q_track)
    # Track cant and cant deficiency govern rail-equivalent acceleration.
    # Carbody/internal tilt can help align the floor, but it does not remove
    # the wheel-rail force limits. We therefore report it separately.
    track_cant_angle = math.degrees(math.atan((cant_mm / 1000.0) / gauge_m))
    cabin_alignment_angle = track_cant_angle + carbody_tilt_deg + internal_floor_tilt_deg
    q_cabin_alignment = lateral_ratio_from_angle_deg(cabin_alignment_angle)
    cabin_alignment_g = resultant_g_from_lateral_ratio(q_cabin_alignment)
    return EnvelopeCase(
        name=name,
        cant_mm=cant_mm,
        cant_deficiency_mm=cant_deficiency_mm,
        carbody_tilt_deg=carbody_tilt_deg,
        internal_floor_tilt_deg=internal_floor_tilt_deg,
        track_lateral_g=q_track,
        track_resultant_g=track_g,
        track_resultant_angle_deg=track_angle,
        cabin_alignment_angle_deg=cabin_alignment_angle,
        cabin_alignment_resultant_g=cabin_alignment_g,
        equivalent_total_cant_mm=(cant_mm + cant_deficiency_mm),
    )


def default_cases() -> List[EnvelopeCase]:
    return [
        make_case("FRA example: 7 in cant + 3 in deficiency", 177.8, 76.2, 0.0),
        make_case("FRA higher example: 7 in cant + 5 in deficiency", 177.8, 127.0, 0.0),
        make_case("EU-style screening: 180 mm cant + 150 mm deficiency", 180.0, 150.0, 0.0),
        make_case("Aggressive screening: 180 mm cant + 200 mm deficiency", 180.0, 200.0, 0.0),
        make_case("FRA 7 in cant + 8 deg carbody tilt", 177.8, 76.2, 8.0),
        make_case("180 mm cant + 8 deg carbody tilt", 180.0, 150.0, 8.0),
        make_case("Custom 300 mm cant + 200 mm deficiency", 300.0, 200.0, 0.0),
    ]


def print_case_table(cases: List[EnvelopeCase]) -> None:
    print("| case | cant mm | cant deficiency mm | carbody tilt deg | track-equivalent lateral g | track-equivalent resultant g | track angle deg | cabin alignment angle deg | cabin-alignment resultant g |")
    print("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    for c in cases:
        print(
            f"| {c.name} | {c.cant_mm:.1f} | {c.cant_deficiency_mm:.1f} | {c.carbody_tilt_deg:.1f} | "
            f"{c.track_lateral_g:.3f} | {c.track_resultant_g:.3f} | {c.track_resultant_angle_deg:.1f} | "
            f"{c.cabin_alignment_angle_deg:.1f} | {c.cabin_alignment_resultant_g:.3f} |"
        )


def print_target_table(targets: List[float]) -> None:
    print("| target resultant g | required lateral g | required resultant angle deg | equivalent cant+deficiency mm on standard gauge |")
    print("|---:|---:|---:|---:|")
    for target in targets:
        q = math.sqrt(target * target - 1.0)
        angle = angle_deg_from_lateral_ratio(q)
        eq_cant = target_equivalent_cant_mm(target)
        print(f"| {target:.3f} | {q:.3f} | {angle:.1f} | {eq_cant:.0f} |")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Railway g-envelope screening model")
    parser.add_argument("--targets", type=float, nargs="+", default=[1.02, 1.035, 1.05, 1.10, 1.20, 1.25])
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    print("# Railway g-envelope screening tables")
    print()
    print("Model note: track-equivalent values screen wheel-rail/cant logic; carbody tilt helps cabin alignment but does not remove track-force limits.")
    print()
    print("## Example envelope cases")
    print()
    print_case_table(default_cases())
    print()
    print("## Target g requirements")
    print()
    print_target_table(args.targets)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
