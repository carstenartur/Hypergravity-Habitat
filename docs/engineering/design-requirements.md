# Design Requirements

**Project:** Hypergravity Habitat  
**Document type:** technology-neutral system requirements  
**Status:** working document for pre-feasibility review  
**Scope:** scientific, engineering, safety, operational, medical, biological, and programme requirements for candidate hypergravity research infrastructure

---

## 1. Purpose

This document defines technology-neutral requirements for evaluating Hypergravity Habitat concepts. It is intended to prevent premature architecture selection and to provide a common basis for comparing railway, maglev, rotating, hybrid, and payload-only demonstrator concepts.

The requirements are not final specifications. They are a pre-feasibility framework that should be refined through literature review, modelling, expert consultation, and demonstrator testing.

The central rule is:

> A design concept is only credible if it can be traced back to a scientific requirement and evaluated against safety, controllability, reproducibility, and operational feasibility.

---

## 2. Requirement Levels

Requirements should be classified by maturity.

| Level | Meaning |
|---|---|
| Mandatory requirement | Required for safety, scientific validity, or governance |
| Target requirement | Desired performance for a useful system |
| Trade requirement | Can be optimized against cost, complexity, or scope |
| Unknown requirement | Requires research before a value can be set |
| Stage-specific requirement | Applies only to a demonstrator, payload platform, or human-rated system |

This classification is important because early demonstrators should not be burdened with full habitat requirements.

---

## 3. Development Stages

The project should define requirements separately for each stage.

| Stage | Description | Requirement emphasis |
|---|---|---|
| Stage 0 | literature review and modelling | equations, evidence map, requirements definition |
| Stage 1 | instrumented physics demonstrator | acceleration, vibration, control, data quality |
| Stage 2 | biological payload demonstrator | environmental control, sample handling, reproducibility |
| Stage 3 | short human tolerance study | medical governance, safety, monitoring |
| Stage 4 | repeated or medium-duration exposure | habitability, recovery, operations |
| Stage 5 | long-duration habitat-scale research | full safety case, logistics, emergency systems |

Human-habitation requirements should not be applied to Stage 1 or Stage 2 unless they are explicitly needed.

---

## 4. Scientific Requirements

### SR-001 — Defined Effective Gravity

The system shall define and measure the effective gravity environment experienced by the payload or participant.

Required documentation:

- target resultant effective gravity,
- lateral and vertical acceleration components,
- gravity vector orientation,
- variation across payload area or body height,
- transient accelerations,
- measurement uncertainty.

### SR-002 — Reproducibility

Experiments shall be repeatable under comparable conditions.

Minimum requirements:

- controlled operating parameters,
- environmental logging,
- documented transfer events,
- baseline and recovery conditions,
- matched 1 g controls where appropriate.

### SR-003 — Exposure Duration

The system shall support exposure durations appropriate to the research question.

Examples:

- seconds to minutes for sensor and tolerance tests,
- hours to days for early response,
- days to weeks for adaptation studies,
- weeks to months only after sufficient evidence and governance.

### SR-004 — Adjustable or Selectable Gravity

The project should allow comparison between at least two effective-gravity conditions over time. This may be achieved by speed variation, radius variation, payload position, different demonstrators, or staged infrastructure.

### SR-005 — Measurement Quality

The system shall monitor variables that could confound scientific interpretation.

Minimum variables:

- acceleration,
- vibration,
- temperature,
- humidity,
- acoustic noise where relevant,
- light where relevant,
- air quality where relevant,
- power interruptions,
- operational events.

---

## 5. Physics and Engineering Requirements

### ER-001 — Transparent Parameter Model

Each concept shall provide equations and assumptions for:

- centripetal acceleration,
- resultant effective gravity,
- angular velocity,
- bank or floor angle,
- gravity gradients,
- speed,
- radius,
- energy and power where applicable.

### ER-002 — Acceleration Stability

The platform shall maintain acceleration within defined tolerances for the intended experiment class. Tolerances remain open until payload requirements are defined.

### ER-003 — Vibration Control

Mechanical vibration shall be measured continuously and reduced to levels compatible with the experiment class.

This is mandatory because vibration can be a biological, physiological, and instrument confounder.

### ER-004 — Environmental Control

The platform shall control or measure environmental variables relevant to the experiment.

Examples:

- temperature,
- humidity,
- CO2,
- oxygen where relevant,
- airflow,
- light level and spectrum,
- noise,
- contamination,
- electromagnetic environment where relevant.

### ER-005 — Reliability and Maintainability

The system should support operation long enough for the intended protocol. Maintenance needs shall be documented as part of the experiment plan.

### ER-006 — Safe State

Every concept shall define a safe state after power loss, control failure, guideway fault, fire, medical emergency, or environmental-control failure.

---

## 6. Biological Payload Requirements

Biological payloads may be the most credible early science pathway.

Minimum requirements:

- controlled enclosure,
- matched 1 g control strategy,
- temperature and humidity logging,
- acceleration and vibration logging,
- contamination control,
- sample-access plan,
- power and data interface,
- recovery or fixation procedure,
- documentation of handling events.

Additional requirements may include:

- lighting control,
- CO2 monitoring,
- sterile work interface,
- microscopy,
- fluid handling,
- hydroponics or growth medium control,
- automated imaging.

---

## 7. Human-Subject Requirements

Human-subject requirements apply only to stages involving people.

Mandatory requirements:

- ethics approval,
- medical screening,
- informed consent,
- exposure stop criteria,
- emergency procedures,
- adverse-event reporting,
- privacy and data protection,
- participant withdrawal procedure,
- medical monitoring appropriate to exposure level,
- independent review for higher-risk protocols.

Human studies shall begin with conservative exposure durations and low-risk participant groups. Long-duration habitation shall not be considered an early-stage requirement.

---

## 8. Habitability Requirements

For any medium- or long-duration human study, the environment must support health, safety, and scientific validity.

Potential requirements:

- private rest area,
- sleep environment,
- hygiene facilities,
- nutrition management,
- exercise and movement space,
- communication,
- acoustic comfort,
- lighting and circadian support,
- psychological support,
- emergency communication,
- access to medical evaluation.

Quantitative values remain undefined and should be derived from analogue-habitat, clinical, occupational, and human-factors literature.

---

## 9. Operational Requirements

The system should define procedures for:

- experiment start and end,
- transfer events,
- routine logistics,
- sample handling,
- maintenance,
- emergency stop,
- emergency evacuation,
- power loss,
- data backup,
- participant monitoring where applicable,
- contamination events where applicable.

Each operational event should be logged because it may affect scientific interpretation.

---

## 10. Safety Requirements

Safety requirements apply to all stages, including payload-only tests.

Mandatory topics:

- hazard identification,
- risk register,
- safe shutdown,
- access control,
- fire protection,
- emergency communication,
- electrical safety,
- mechanical safety,
- containment where relevant,
- data and control-system reliability,
- inspection and maintenance plan,
- incident reporting.

For moving or rotating platforms, additional topics include:

- overspeed protection,
- braking behaviour,
- kinetic energy,
- structural monitoring,
- guideway integrity,
- emergency access,
- rescue procedures.

---

## 11. Economic and Programme Requirements

The project should be financially staged.

Requirements:

- define the smallest useful demonstrator,
- separate CAPEX from OPEX,
- include maintenance and renewal costs,
- include staffing assumptions,
- state uncertainty ranges,
- avoid unsupported headline cost claims,
- include stop/go decision points,
- compare cost to scientific output.

A full-scale facility should not be proposed before a pre-feasibility study and demonstrator evidence justify it.

---

## 12. Evaluation Matrix

| Criterion | Importance | Notes |
|---|---:|---|
| Scientific usefulness | high | primary justification |
| Safety | high | mandatory for all stages |
| Measurement quality | high | determines scientific validity |
| Reproducibility | high | required for reviewable science |
| Environmental control | high | especially for biology and humans |
| Technical feasibility | high | concept must be buildable at the stage proposed |
| Maintainability | medium-high | critical for long exposure |
| Cost realism | medium-high | required for funding credibility |
| Scalability | medium | useful but not required for first demonstrator |
| Habitability | stage-dependent | not required for payload-only phases |
| Upgrade potential | medium | should not override near-term validity |

---

## 13. Requirements Not Yet Quantified

The following values remain open:

- acceptable vibration limits for each payload class,
- acceptable angular rate for different human protocols,
- acceptable noise levels,
- minimum radius for human-centred studies,
- environmental tolerances for biological payloads,
- target gravity range,
- exposure duration thresholds,
- interruption frequency,
- emergency response time,
- minimum living volume,
- cost thresholds for demonstrator stages.

These should be converted into quantitative requirements only after literature review, modelling, and expert feedback.

---

## 14. Traceability Requirement

Every future design document should include a requirements traceability table:

| Requirement ID | Design response | Evidence or assumption | Verification method | Status |
|---|---|---|---|---|

This will make the repository more suitable for academic review and funding discussions.

---

## 15. Preliminary Conclusion

The Hypergravity Habitat project should remain requirements-led. The first objective is not to choose between railway, maglev, rotating, or hybrid concepts. The first objective is to define what scientific questions require, what safety allows, and what demonstrators can verify.

This document should be updated whenever the research gap, physics model, experimental plan, or safety analysis changes.