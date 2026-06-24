# Diagrams

This directory is intended for figures, schematics, and visual explanation material for the Hypergravity Habitat project.

The project needs diagrams because many review-relevant ideas are geometric or systems-based: resultant effective gravity, radius/speed trade-offs, Coriolis effects, demonstrator staging, architecture comparison, and safety logic.

---

## Priority Figures

### 1. Resultant Effective Gravity Vector

Purpose:

- show Earth gravity and lateral centripetal acceleration as perpendicular components,
- show the resultant effective gravity vector,
- show the required bank or floor angle.

Related documents:

- `docs/physics-reference.md`
- `docs/engineering/preliminary-sizing.md`

---

### 2. Radius-Speed-Gravity Trade-Off

Purpose:

- show how required speed changes with radius,
- compare target resultant gravity levels,
- make large-radius implications visible.

Related files:

- `calculations/hypergravity_sizing.py`

---

### 3. Coriolis Projectile Deflection

Purpose:

- show how thrown or kicked projectiles deviate in a rotating frame,
- compare handball and football examples,
- explain why sport-specific skill maintenance can require larger radii than strength training.

Related files:

- `calculations/coriolis_projectile_deflection.py`
- `docs/science/coriolis-projectile-accuracy.md`

---

### 4. Demonstrator Ladder

Purpose:

- show progression from calculation to instrumentation, biological payloads, engineering demonstrators, and only later possible human studies.

Related documents:

- `docs/roadmap.md`
- `docs/minimum-useful-demonstrator.md`
- `docs/experimental-programme.md`

---

### 5. Architecture Trade Study Diagram

Purpose:

- compare no-build, existing facilities, payload demonstrator, rotating platform, rail, maglev, and hybrid concepts.

Related document:

- `docs/architecture-trade-study.md`

---

### 6. Safety Case Structure

Purpose:

- show how hazards, requirements, mitigations, evidence, and residual risk connect.

Related documents:

- `docs/safety-case-outline.md`
- `docs/risk-register.md`
- `docs/requirements-traceability-matrix.md`

---

## Style Guidelines

Figures should be:

- simple,
- source-controlled,
- editable,
- labelled with SI units,
- referenced from the relevant document,
- cautious in wording,
- suitable for academic or proposal use.

Preferred source formats:

- SVG,
- Mermaid diagrams in Markdown,
- Python-generated plots,
- draw.io source files if exported to SVG or PNG.

---

## Status

No final figure set exists yet. This directory currently defines the required figure plan.