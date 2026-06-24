# Figure Register

**Project:** Hypergravity Habitat  
**Purpose:** track figure sources, assumptions, and verification status  
**Rule:** no figure without source

---

## 1. Figure Source Policy

Every figure must have:

- a figure ID,
- a source file,
- a source document or calculation script,
- assumptions,
- units,
- limitation note,
- status.

Rendered graphics should be reproducible from the source files.

---

## 2. Register

| Figure ID | Title | Source file | Source basis | Status |
|---|---|---|---|---|
| FIG-001 | Resultant Effective Gravity Vector | `resultant-effective-gravity.mmd` | `docs/physics-reference.md`; `calculations/hypergravity_sizing.py` | source ready |
| FIG-002 | Demonstrator Ladder | `demonstrator-ladder.mmd` | `docs/roadmap.md`; `docs/minimum-useful-demonstrator.md`; `docs/experimental-programme.md` | source ready |
| FIG-003 | Architecture Options | `architecture-options.mmd` | `docs/architecture-trade-study.md`; `docs/facility-comparison.md`; `docs/engineering/full-ring-vehicle-concept.md` | source ready |
| FIG-004 | Safety Case Structure | `safety-case-structure.mmd` | `docs/safety-case-outline.md`; `docs/risk-register.md`; `docs/requirements-traceability-matrix.md` | source ready |
| FIG-005 | Confounder-Control Chain | `confounder-control-chain.mmd` | `docs/vibration-and-confounders.md`; `docs/data-management-plan.md` | source ready |
| FIG-006 | Physics Plots | `generate_physics_plots.py` | `docs/physics-reference.md`; `calculations/hypergravity_sizing.py`; `calculations/coriolis_projectile_deflection.py` | generator ready |

---

## 3. Assumption Summary

### FIG-001

Assumes a terrestrial circular platform where Earth gravity and centripetal acceleration are perpendicular components. Uses:

```text
g_eff = √(g² + a_c²)
θ = arctan(a_c / g)
```

### FIG-002

Uses staged development logic from roadmap, minimum demonstrator, and experimental programme documents. It is a programme-flow diagram, not an engineering proof.

### FIG-003

Uses architecture categories and recommendations from the architecture trade study. Scores are intentionally not shown until a formal weighted trade study exists.

### FIG-004

Shows safety-case argument structure. It does not assert that any system is safe.

### FIG-005

Shows how unmeasured platform effects can invalidate biological, human, or sports-science interpretations.

### FIG-006

Numerical plots are generated from equations in `docs/physics-reference.md`. Values are first-order concept-screening outputs, not final engineering values.

---

## 4. Rendering Rule

When a figure is rendered to SVG/PNG/PDF, add a metadata comment or caption:

```text
Figure ID: FIG-XXX
Generated from: <source file>
Source basis: <document/script list>
Generated on: YYYY-MM-DD
Limitations: first-order / conceptual / not to scale / etc.
```

---

## 5. Status

The register is now active. Future diagrams should be added here before being used in proposal material.

---

<!-- project-footer -->
**Project:** [Hypergravity Habitat](../README.md) · **Status:** exploratory research documentation · **License:** see repository license and file-level notes
