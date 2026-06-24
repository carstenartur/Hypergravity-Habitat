# Minimum Useful Demonstrator

**Project:** Hypergravity Habitat  
**Document type:** demonstrator strategy and decision framework  
**Status:** working document for pre-feasibility planning  
**Scope:** definition of the smallest experiment or platform that produces useful evidence for the next project stage

---

## 1. Purpose

This document defines the concept of a **minimum useful demonstrator** for the Hypergravity Habitat project. It is intended to prevent premature large-infrastructure thinking and to identify the smallest credible step that can retire important scientific and engineering risks.

The central question is:

> What is the smallest demonstrator that can produce decision-quality evidence about sustained moderate hypergravity, measurement quality, confounders, and future feasibility?

The answer should be driven by research value, not by architectural preference.

---

## 2. Definition

A minimum useful demonstrator is:

> A limited, testable system that produces measurable data capable of confirming, narrowing, or rejecting a key assumption of the Hypergravity Habitat concept.

It does not need to resemble a full habitat. It does need to produce evidence that justifies, redirects, or stops the next stage.

---

## 3. Demonstrator Success Criteria

A useful demonstrator should satisfy at least five criteria.

1. **Defined gravity condition:** the effective gravity environment is calculated and measured.
2. **Known exposure duration:** the experiment has a clear time structure.
3. **Measured confounders:** vibration, temperature, humidity, acceleration transients, and operational events are logged.
4. **Matched control:** a 1 g or otherwise appropriate control condition exists.
5. **Reproducible output:** the experiment can be repeated with comparable results.
6. **Risk retirement:** the outcome reduces uncertainty about the next stage.
7. **Limited scope:** the demonstrator avoids unnecessary human or infrastructure complexity.

---

## 4. Why a Full Habitat Is Not the First Demonstrator

A full habitat would require:

- human safety case,
- ethics approval,
- medical governance,
- emergency access,
- continuous operation,
- high reliability,
- environmental control,
- transfer logistics,
- large capital cost,
- long planning horizon.

These requirements are inappropriate before the project has validated the basic measurement and research premise.

Therefore, the first useful demonstrator should be **payload-first**, not human-first.

---

## 5. Demonstrator Classes

### Class A — Calculation and Simulation Demonstrator

Purpose:

- validate equations,
- explore radius/speed/gravity trade-offs,
- estimate Coriolis and vibration sensitivity,
- produce reviewable parameter studies.

Outputs:

- reproducible scripts,
- tables,
- plots,
- sensitivity analysis,
- assumptions log.

Current status:

- initial sizing script exists in `calculations/hypergravity_sizing.py`,
- Coriolis projectile script exists in `calculations/coriolis_projectile_deflection.py`.

### Class B — Instrumentation Demonstrator

Purpose:

- verify sensor package,
- measure acceleration and vibration,
- test data logging,
- validate calibration procedures.

Possible platform:

- small rotating rig,
- circular cart,
- laboratory centrifuge,
- rail or guideway prototype.

Outputs:

- acceleration time series,
- vibration spectrum,
- environmental logs,
- repeatability data.

### Class C — Biological Payload Demonstrator

Purpose:

- test whether sustained moderate hypergravity produces interpretable biological data,
- test environmental control and confounder measurement.

Candidate payloads:

- microbial growth curves,
- plant seedling root-angle study,
- algae growth,
- cell morphology assay,
- sealed environmental payload.

Outputs:

- biological measurements,
- matched 1 g controls,
- environmental logs,
- confounder analysis.

### Class D — Guided Motion Demonstrator

Purpose:

- test rail, maglev, or circular guideway dynamics,
- measure ride quality,
- evaluate maintenance and control assumptions.

Outputs:

- acceleration stability,
- vibration data,
- power data,
- operational event log,
- preliminary safety findings.

### Class E — Short Human Tolerance Demonstrator

Purpose:

- later-stage tolerance and measurement feasibility.

Status:

- not appropriate as the first demonstrator.

Requirements:

- ethics approval,
- medical screening,
- safety case,
- emergency plan,
- conservative exposure protocol.

---

## 6. Candidate First Demonstrator Recommendation

The most credible first demonstrator is a combined **instrumented biological payload demonstrator**.

Recommended concept:

> A sealed, instrumented rotating or guided payload platform supporting a simple plant seedling or microbial experiment under a small set of effective-gravity conditions, with matched 1 g controls and continuous acceleration, vibration, temperature, and humidity logging.

Why this is strong:

- avoids human-subject risk,
- produces scientific data,
- tests engineering data quality,
- reveals confounders early,
- can be repeated,
- provides fundable outputs,
- can be reviewed by biology and engineering experts.

---

## 7. Candidate Experiment 1: Plant Seedling Payload

### Research Question

Do seedlings show measurable root or shoot development differences under sustained moderate hypergravity compared with matched 1 g controls?

### Candidate Measurements

- germination time,
- primary root length,
- root angle,
- shoot length,
- curvature dynamics,
- survival,
- time-lapse images,
- temperature and humidity,
- acceleration and vibration.

### Strengths

- low ethical burden,
- visually measurable,
- compatible with automation,
- short experimental duration,
- relevant to plant gravitropism.

### Risks

- irrigation and humidity confounders,
- vibration effects,
- light gradients,
- small effect size,
- species selection.

---

## 8. Candidate Experiment 2: Microbial Payload

### Research Question

Does sustained moderate hypergravity alter microbial growth curves or biofilm formation under controlled conditions?

### Candidate Measurements

- optical density,
- colony counts,
- imaging,
- growth rate,
- temperature,
- acceleration,
- vibration,
- contamination status.

### Strengths

- fast generation time,
- compact payload,
- repeatable,
- useful for platform validation.

### Risks

- fluid shear,
- sedimentation,
- oxygen gradients,
- temperature sensitivity,
- biosafety requirements.

---

## 9. Candidate Experiment 3: Instrumentation-Only Payload

### Research Question

Can the platform provide a stable, measured, reproducible hypergravity environment before biological interpretation is attempted?

### Candidate Measurements

- acceleration vector,
- angular rate,
- vibration spectrum,
- jerk,
- temperature,
- humidity,
- power stability,
- event logs.

### Strengths

- lowest biological risk,
- directly supports engineering feasibility,
- essential calibration step.

### Risks

- scientifically less attractive alone,
- may not demonstrate biological value.

---

## 10. Demonstrator Evaluation Matrix

| Candidate | Scientific value | Safety complexity | Cost | Confounder control | Funding value | Recommendation |
|---|---:|---:|---:|---:|---:|---|
| calculation model | medium | low | low | n/a | medium | already underway |
| instrumentation-only rig | medium | low-medium | low-medium | high | high | recommended first technical step |
| plant seedling payload | high | low-medium | low-medium | medium-high | high | recommended first science step |
| microbial payload | medium-high | medium | low-medium | medium | medium-high | strong alternative |
| cell-culture payload | high | medium-high | medium | medium | medium | later after environmental validation |
| guided rail/maglev rig | medium-high | medium-high | medium-high | medium | high | later engineering step |
| short human tolerance | high | high | high | medium | high but sensitive | not first |

---

## 11. Minimum Data Package

Every demonstrator should produce a minimum data package:

- protocol,
- target gravity,
- measured acceleration,
- vibration spectrum,
- temperature and humidity log,
- power and operational event log,
- control condition data,
- raw data files,
- analysis script,
- uncertainty statement,
- lessons learned,
- recommendation for next stage.

---

## 12. Stop/Go Criteria

A demonstrator should lead to a clear decision.

| Outcome | Decision |
|---|---|
| stable acceleration and low confounders | proceed to biological payload or larger test |
| high vibration but measurable | redesign platform or use vibration-matched controls |
| uncontrolled environment | improve payload enclosure before science claims |
| no measurable biological effect | adjust organism, gravity level, duration, or stop biological route |
| strong confounding | do not proceed to larger claims |
| unsafe operation | stop and redesign |

---

## 13. Recommended Near-Term Demonstrator Package

A credible first funding package could include:

1. reproducible physics and Coriolis models,
2. sensor and data-logging package,
3. small rotating or guided payload rig,
4. environmental enclosure,
5. plant seedling pilot experiment,
6. matched 1 g control,
7. vibration and acceleration analysis,
8. independent expert review.

This is likely more fundable than a large infrastructure request because it is narrow, testable, and risk-reducing.

---

## 14. Relationship to Other Documents

This document connects to:

- `docs/roadmap.md`,
- `docs/risk-register.md`,
- `docs/safety-case-outline.md`,
- `docs/vibration-and-confounders.md`,
- `docs/science/plant-science.md`,
- `docs/science/biology.md`,
- `docs/engineering/design-requirements.md`.

---

## 15. Preliminary Conclusion

The minimum useful demonstrator should not be a human habitat. It should be a small, instrumented, reproducible platform that tests both physics and experimental validity.

The strongest first candidate is an instrumented plant or microbial payload demonstrator with matched 1 g controls. This path produces evidence, avoids premature human risk, and gives reviewers a concrete next milestone.