# Diagrams

This directory contains **source-backed diagram material** for the Hypergravity Habitat project.

No diagram in this repository should be treated as valid unless it has a documented source: an equation, a calculation script, a data table, a Mermaid source file, or a cited project document.

---

## Source Rule

Every figure must have:

1. a figure ID,
2. a source file,
3. a source document or calculation script,
4. stated assumptions,
5. units where numerical values are shown,
6. a limitation note.

Generated images without a source file should not be committed.

---

## Current Diagram Sources

| Figure ID | Topic | Source file | Source basis |
|---|---|---|---|
| FIG-001 | Resultant effective gravity vector | `resultant-effective-gravity.mmd` | `docs/physics-reference.md`, `calculations/hypergravity_sizing.py` |
| FIG-002 | Demonstrator ladder | `demonstrator-ladder.mmd` | `docs/roadmap.md`, `docs/minimum-useful-demonstrator.md`, `docs/experimental-programme.md` |
| FIG-003 | Architecture options | `architecture-options.mmd` | `docs/architecture-trade-study.md` |
| FIG-004 | Safety case structure | `safety-case-structure.mmd` | `docs/safety-case-outline.md`, `docs/risk-register.md`, `docs/requirements-traceability-matrix.md` |
| FIG-005 | Confounder-control chain | `confounder-control-chain.mmd` | `docs/vibration-and-confounders.md`, `docs/data-management-plan.md` |
| FIG-006 | Physics plots | `generate_physics_plots.py` | `calculations/hypergravity_sizing.py`, `calculations/coriolis_projectile_deflection.py`, `docs/physics-reference.md` |

---

## Planned Rendered Outputs

Rendered SVG/PNG files are intentionally not required at this stage. The authoritative sources are the Mermaid and Python files.

If rendered graphics are later added, they should be generated from the source files and accompanied by a note such as:

```text
Generated from: diagrams/resultant-effective-gravity.mmd
Source documents: docs/physics-reference.md, calculations/hypergravity_sizing.py
Generated on: YYYY-MM-DD
```

---

## Priority Figures

### FIG-001: Resultant Effective Gravity Vector

Purpose:

- show Earth gravity and lateral centripetal acceleration as perpendicular components,
- show the resultant effective gravity vector,
- show the required bank or floor angle.

Source basis:

- `docs/physics-reference.md`
- `docs/engineering/preliminary-sizing.md`
- `calculations/hypergravity_sizing.py`

---

### FIG-002: Demonstrator Ladder

Purpose:

- show progression from calculation to instrumentation, biological payloads, engineering demonstrators, and only later possible human studies.

Source basis:

- `docs/roadmap.md`
- `docs/minimum-useful-demonstrator.md`
- `docs/experimental-programme.md`

---

### FIG-003: Architecture Trade Study Diagram

Purpose:

- compare no-build, existing facilities, payload demonstrator, rotating platform, rail, maglev, and hybrid concepts.

Source basis:

- `docs/architecture-trade-study.md`
- `docs/facility-comparison.md`

---

### FIG-004: Safety Case Structure

Purpose:

- show how hazards, requirements, mitigations, evidence, and residual risk connect.

Source basis:

- `docs/safety-case-outline.md`
- `docs/risk-register.md`
- `docs/requirements-traceability-matrix.md`

---

### FIG-005: Confounder-Control Chain

Purpose:

- show how platform effects can confound biological or human results and how measurement/logging controls interpretation.

Source basis:

- `docs/vibration-and-confounders.md`
- `docs/data-management-plan.md`

---

### FIG-006: Radius-Speed and Coriolis Plots

Purpose:

- generate numerical plots from reproducible equations rather than hand-drawn illustration.

Source basis:

- `diagrams/generate_physics_plots.py`
- `calculations/hypergravity_sizing.py`
- `calculations/coriolis_projectile_deflection.py`

---

## Style Guidelines

Figures should be:

- source-controlled,
- editable,
- reproducible,
- labelled with SI units,
- referenced from relevant documents,
- cautious in wording,
- suitable for academic or proposal use.

Preferred source formats:

- Mermaid `.mmd`,
- Python generators,
- CSV data files,
- SVG generated from source.

---

## Status

This directory now contains source-backed diagram definitions and a generator script. The next step is rendering selected figures to SVG after deciding the exact output style.