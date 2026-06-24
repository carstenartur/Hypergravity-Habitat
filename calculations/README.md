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

\[
g_{eff} = \sqrt{g^2 + a_c^2}
\]

This is important because a terrestrial circular platform combines vertical Earth gravity and horizontal centripetal acceleration.

---

## Usage

From the repository root:

```bash
python calculations/hypergravity_sizing.py
```

CSV output:

```bash
python calculations/hypergravity_sizing.py --format csv
```

Custom values:

```bash
python calculations/hypergravity_sizing.py --g-levels 1.05 1.10 1.20 --radii 100 250 500
```

---

## Documentation Links

Related documents:

- `docs/engineering/preliminary-sizing.md`
- `docs/engineering/design-requirements.md`
- `docs/engineering/railway-platform.md`
- `docs/engineering/maglev-platform.md`

---

## Calculation Standard

All future calculation files should:

1. state equations,
2. define units,
3. expose assumptions,
4. avoid hidden constants,
5. support reproducible outputs,
6. distinguish first-order estimates from validated engineering models,
7. identify limitations and uncertainty.

---

## Status

The current calculation model is suitable for concept screening and documentation consistency. It is not sufficient for detailed engineering, safety certification, or construction planning.