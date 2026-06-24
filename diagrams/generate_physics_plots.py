#!/usr/bin/env python3
"""
Generate source-backed physics plots for the Hypergravity Habitat project.

Figure source policy
--------------------
This file is a source file, not a rendered figure. Rendered SVG/PNG outputs
should be generated from this script and documented in diagrams/figure-register.md.

Source basis:
- docs/physics-reference.md
- docs/engineering/preliminary-sizing.md
- calculations/hypergravity_sizing.py
- calculations/coriolis_projectile_deflection.py

The calculations are first-order concept-screening models. They are not final
engineering, safety, or sports-science protocol models.

Generated outputs, if matplotlib is available:
- diagrams/generated/radius_speed_tradeoff.svg
- diagrams/generated/angular_rate_tradeoff.svg
- diagrams/generated/coriolis_deflection_radius.svg
- diagrams/generated/physics_plot_data.csv
"""

from __future__ import annotations

import csv
import math
from pathlib import Path
from typing import Iterable, List

STANDARD_GRAVITY = 9.80665

OUTPUT_DIR = Path(__file__).resolve().parent / "generated"


def lateral_acceleration_for_resultant_g(target_g: float) -> float:
    if target_g < 1.0:
        raise ValueError("target_g must be >= 1.0")
    return STANDARD_GRAVITY * math.sqrt(target_g * target_g - 1.0)


def speed_kmh(target_g: float, radius_m: float) -> float:
    a_c = lateral_acceleration_for_resultant_g(target_g)
    return math.sqrt(a_c * radius_m) * 3.6


def angular_rate_rpm(target_g: float, radius_m: float) -> float:
    a_c = lateral_acceleration_for_resultant_g(target_g)
    omega = math.sqrt(a_c / radius_m)
    return omega * 60.0 / (2.0 * math.pi)


def coriolis_deflection_m(target_g: float, radius_m: float, range_m: float, projectile_speed_mps: float) -> float:
    a_c = lateral_acceleration_for_resultant_g(target_g)
    omega = math.sqrt(a_c / radius_m)
    return omega * range_m * range_m / projectile_speed_mps


def radii_series() -> List[float]:
    return [100, 150, 200, 300, 400, 500, 750, 1000, 1500, 2000, 3000, 5000, 7500, 10000]


def write_csv_data() -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output = OUTPUT_DIR / "physics_plot_data.csv"
    g_levels = [1.05, 1.10, 1.20, 1.25]
    radii = radii_series()

    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "source_basis",
                "target_resultant_g",
                "radius_m",
                "speed_kmh",
                "angular_rate_rpm",
                "coriolis_deflection_20m_20mps_m",
                "coriolis_deflection_30m_25mps_m",
            ]
        )
        for target_g in g_levels:
            for radius_m in radii:
                writer.writerow(
                    [
                        "docs/physics-reference.md; calculations scripts",
                        target_g,
                        radius_m,
                        speed_kmh(target_g, radius_m),
                        angular_rate_rpm(target_g, radius_m),
                        coriolis_deflection_m(target_g, radius_m, 20.0, 20.0),
                        coriolis_deflection_m(target_g, radius_m, 30.0, 25.0),
                    ]
                )
    return output


def maybe_generate_plots() -> None:
    try:
        import matplotlib.pyplot as plt  # type: ignore
    except Exception:
        print("matplotlib not available; CSV data generated only")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    radii = radii_series()
    g_levels = [1.05, 1.10, 1.20, 1.25]

    # Plot 1: radius-speed trade-off
    plt.figure()
    for g_level in g_levels:
        plt.plot(radii, [speed_kmh(g_level, r) for r in radii], label=f"{g_level:.2f} g resultant")
    plt.xlabel("Radius [m]")
    plt.ylabel("Required speed [km/h]")
    plt.title("Radius-speed trade-off for terrestrial circular hypergravity")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "radius_speed_tradeoff.svg")
    plt.close()

    # Plot 2: angular rate trade-off
    plt.figure()
    for g_level in g_levels:
        plt.plot(radii, [angular_rate_rpm(g_level, r) for r in radii], label=f"{g_level:.2f} g resultant")
    plt.xlabel("Radius [m]")
    plt.ylabel("Angular rate [rpm]")
    plt.title("Angular-rate trade-off for terrestrial circular hypergravity")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "angular_rate_tradeoff.svg")
    plt.close()

    # Plot 3: Coriolis deflection for projectile examples at 1.10 g
    plt.figure()
    target_g = 1.10
    plt.plot(radii, [coriolis_deflection_m(target_g, r, 20.0, 20.0) for r in radii], label="20 m throw at 20 m/s")
    plt.plot(radii, [coriolis_deflection_m(target_g, r, 30.0, 25.0) for r in radii], label="30 m kick/pass at 25 m/s")
    plt.xlabel("Radius [m]")
    plt.ylabel("First-order deflection [m]")
    plt.title("Coriolis projectile deflection estimate at 1.10 g resultant")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "coriolis_deflection_radius.svg")
    plt.close()


def main() -> int:
    csv_path = write_csv_data()
    print(f"Wrote {csv_path}")
    maybe_generate_plots()
    print("Done. Rendered plot files are generated only if matplotlib is installed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
