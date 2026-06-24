# Work Packages

**Project:** Hypergravity Habitat  
**Document type:** work-package structure for pre-feasibility programme  
**Status:** working draft  
**Scope:** staged research tasks, deliverables, milestones, dependencies, and success criteria

---

## 1. Purpose

This document defines a structured set of work packages for the Hypergravity Habitat pre-feasibility programme. It is intended to make the project understandable to academic reviewers and early-stage research funders.

The work packages are designed to answer one question:

> What evidence must be produced before the project can responsibly move from concept to demonstrator?

---

## 2. Programme Logic

The work packages follow this sequence:

1. verify the research gap,
2. make calculations reproducible,
3. define requirements and risks,
4. identify a minimum useful demonstrator,
5. design first payload experiments,
6. compare architectures,
7. prepare external review and funding material.

---

## 3. WP1 — Literature and Facility Review

### Objective

Determine whether sustained moderate hypergravity is a real and relevant research gap.

### Tasks

- Review artificial-gravity literature.
- Review bed-rest and analogue studies.
- Review human centrifuge studies.
- Review biological hypergravity studies.
- Review plant gravity-response literature.
- Compare existing facilities.
- Identify which questions existing facilities already answer.

### Deliverables

- annotated literature review,
- facility comparison,
- source matrix,
- research-gap validation memo.

### Milestone

M1: Research gap either confirmed, narrowed, or rejected.

### Success Criteria

- at least one defensible unanswered research area is identified,
- claims are supported by source categories,
- gaps are stated cautiously.

---

## 4. WP2 — Physics and Parameter Modelling

### Objective

Develop reproducible calculations for candidate hypergravity concepts.

### Tasks

- Model resultant effective gravity.
- Model centripetal acceleration.
- Calculate radius, speed, angular rate, and bank angle.
- Estimate Coriolis projectile deflection.
- Identify parameter ranges for candidate demonstrators.
- Produce open calculation scripts.

### Deliverables

- `calculations/hypergravity_sizing.py`,
- `calculations/coriolis_projectile_deflection.py`,
- parameter tables,
- physics-reference document,
- plots or diagrams in later phase.

### Milestone

M2: Reviewable parameter model exists.

### Success Criteria

- calculations are reproducible,
- assumptions are explicit,
- equations are documented,
- reviewers can change input values.

---

## 5. WP3 — Requirements, Safety, Ethics, and Risk

### Objective

Define the governance and safety framework before architecture selection.

### Tasks

- Define technology-neutral requirements.
- Create risk register.
- Create safety-case outline.
- Create ethics and governance framework.
- Define data management requirements.
- Create requirements traceability matrix.

### Deliverables

- `docs/engineering/design-requirements.md`,
- `docs/risk-register.md`,
- `docs/safety-case-outline.md`,
- `docs/ethics-and-governance.md`,
- `docs/data-management-plan.md`,
- `docs/requirements-traceability-matrix.md`.

### Milestone

M3: Minimum governance framework exists for a non-human demonstrator.

### Success Criteria

- hazards are identified,
- ethical boundaries are explicit,
- human and animal studies are not treated as early defaults,
- requirements can be traced to documents.

---

## 6. WP4 — Minimum Useful Demonstrator

### Objective

Define the smallest demonstrator that can produce decision-quality evidence.

### Tasks

- Compare candidate demonstrator types.
- Define minimum data package.
- Select candidate payload class.
- Define stop/go criteria.
- Estimate cost and risk.

### Deliverables

- `docs/minimum-useful-demonstrator.md`,
- demonstrator concept table,
- candidate payload requirements,
- stop/go decision logic.

### Milestone

M4: First demonstrator candidate selected for expert review.

### Success Criteria

- demonstrator is not human-first,
- outputs are measurable,
- confounders are logged,
- failure outcomes are defined.

---

## 7. WP5 — Biological and Instrumentation Pilot Design

### Objective

Design a first pilot payload that tests both scientific and engineering assumptions.

### Tasks

- Define plant seedling payload option.
- Define microbial payload option.
- Define instrumentation-only payload.
- Define environmental enclosure requirements.
- Define matched 1 g control strategy.
- Define analysis and metadata requirements.

### Deliverables

- pilot payload concept,
- environmental monitoring plan,
- control plan,
- measurement protocol,
- data-management template.

### Milestone

M5: Pilot payload design ready for technical and scientific review.

### Success Criteria

- payload can be built within a realistic first funding stage,
- ethical burden is low,
- data will be interpretable,
- platform performance data are produced alongside scientific data.

---

## 8. WP6 — Architecture Trade Study

### Objective

Compare candidate architecture paths against requirements.

### Tasks

- Compare no-build, existing facilities, rotating payload demonstrator, laboratory centrifuge, guided cart, railway, maglev, rotating habitat, and hybrid options.
- Apply criteria for scientific value, safety, cost, measurement quality, and scalability.
- Identify architecture-specific risks.
- Recommend next-stage architecture path.

### Deliverables

- `docs/architecture-trade-study.md`,
- weighted trade-study table,
- architecture risk map,
- next-stage recommendation.

### Milestone

M6: Architecture path recommended for demonstrator stage.

### Success Criteria

- no architecture selected prematurely,
- no-build option considered,
- recommendation is linked to requirements.

---

## 9. WP7 — Expert Review and Proposal Preparation

### Objective

Prepare a package suitable for academic and institutional feedback.

### Tasks

- Prepare proposal brief.
- Prepare executive summary.
- Identify potential partners.
- Prepare figures and diagrams.
- Create review questions for experts.
- Incorporate feedback into roadmap.

### Deliverables

- `docs/proposal-brief.md`,
- partner map,
- review package,
- updated roadmap,
- pre-feasibility proposal outline.

### Milestone

M7: External review package ready.

### Success Criteria

- project can be sent to experts without appearing speculative,
- first fundable milestone is clear,
- risks and limitations are visible.

---

## 10. Dependencies

| Work package | Depends on |
|---|---|
| WP1 | none |
| WP2 | none, but informed by WP1 |
| WP3 | WP1, WP2 |
| WP4 | WP1, WP2, WP3 |
| WP5 | WP4 |
| WP6 | WP1–WP4 |
| WP7 | WP1–WP6 |

---

## 11. Suggested Timeline Logic

This document does not assign calendar dates. A calendar should be added only after resources and partners are known.

Relative order:

1. WP1 and WP2 in parallel,
2. WP3 after initial equations and gap review,
3. WP4 after requirements and risks,
4. WP5 after demonstrator selection,
5. WP6 after demonstrator requirements,
6. WP7 after enough content exists for serious critique.

---

## 12. Review Questions for Funders or Professors

1. Is the research gap plausible?
2. Are the first-stage work packages too broad?
3. Is a biological payload demonstrator the right first experiment?
4. Which existing facility should be consulted first?
5. Which safety or ethics issue is underestimated?
6. What evidence would make the project worth funding?
7. What evidence would justify stopping the project?

---

## 13. Preliminary Conclusion

The Hypergravity Habitat project should be presented as a pre-feasibility programme with clear work packages. The strongest funding logic is a sequence of literature review, reproducible modelling, requirements and risk definition, payload-first demonstrator design, and expert review.

This structure gives reviewers the opportunity to support, redirect, or reject the project before significant infrastructure commitments are made.