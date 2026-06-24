# Calculations

This directory contains reproducible calculation tools for the Hypergravity Habitat project.

The goal is to make numerical assumptions inspectable, repeatable, and easy to challenge. Calculations in this directory should be treated as pre-feasibility tools, not final engineering designs.

---

## Available Tools

### `hypergravity_sizing.py`

First-order sizing model for terrestrial circular hypergravity concepts.

It calculates:

- required lateral centripetal acceleration,
- operating speed,
- angular rate,
- lap time,
- circumference,
- bank angle / resultant-vector angle.

The model uses the vector-corrected relationship:

```text
g_eff = √(g² + a_c²)
```

This is important because a terrestrial circular platform combines vertical Earth gravity and horizontal centripetal acceleration.

Usage:

```bash
python calculations/hypergravity_sizing.py
python calculations/hypergravity_sizing.py --format csv
python calculations/hypergravity_sizing.py --g-levels 1.05 1.10 1.20 --radii 100 250 500
```

---

### `coriolis_projectile_deflection.py`

First-order estimator for Coriolis deflection of thrown or kicked projectiles inside a rotating or circular platform.

It estimates:

- platform angular rate from target resultant gravity and radius,
- approximate projectile flight time,
- first-order lateral deflection,
- approximate radius required for an allowed deflection threshold.

The screening model is:

```text
y ≈ Ω × L² / v
```

where:

- `y` is lateral deflection,
- `Ω` is platform angular rate,
- `L` is projectile range,
- `v` is projectile speed.

This model is intentionally simple. It does not include drag, spin, Magnus effect, launch angle, bounce, target height, or exact 3D geometry.

Usage:

```bash
python calculations/coriolis_projectile_deflection.py
python calculations/coriolis_projectile_deflection.py --target-g 1.10 --range 20 --speed 20
python calculations/coriolis_projectile_deflection.py --target-g 1.10 --range 30 --speed 25 --allowed-deflection 0.5
```

---

### `railway_g_envelope.py`

First-order railway g-envelope screening model.

It estimates:

- track-equivalent lateral acceleration from cant and cant deficiency,
- track-equivalent resultant effective g,
- resultant-vector angle,
- cabin alignment angle when carbody tilt or internal floor tilt is added,
- equivalent cant-plus-deficiency required for target g values.

The screening relationship is:

```text
a_c / g ≈ (h_cant + h_def) / G_track
```

where:

- `h_cant` is track cant,
- `h_def` is cant deficiency,
- `G_track` is track gauge.

Usage:

```bash
python calculations/railway_g_envelope.py
python calculations/railway_g_envelope.py --targets 1.02 1.05 1.10 1.20
```

Important limitation: carbody tilt can help align the cabin floor, but it does not remove the wheel-rail force limits. This tool is not a certification model.

---

## Documentation Links

Related documents:

- `docs/physics-reference.md`
- `docs/engineering/preliminary-sizing.md`
- `docs/engineering/design-requirements.md`
- `docs/engineering/railway-platform.md`
- `docs/engineering/tilting-train-and-cant-limits.md`
- `docs/engineering/railway-g-envelope.md`
- `docs/engineering/maglev-platform.md`
- `docs/literature-review.md`
- `docs/science/sports-science.md`

---

## Calculation Standard

All future calculation files should:

1. state equations in readable notation,
2. define units,
3. expose assumptions,
4. avoid hidden constants,
5. support reproducible outputs,
6. distinguish first-order estimates from validated engineering models,
7. identify limitations and uncertainty.

---

## Status

The current calculation tools are suitable for concept screening and documentation consistency. They are not sufficient for detailed engineering, safety certification, sports-science protocol design, railway approval, or construction planning.

---

<!-- project-footer -->
**Project:** [Hypergravity Habitat](../README.md) · **Status:** exploratory research documentation · **License:** see repository license and file-level notes
