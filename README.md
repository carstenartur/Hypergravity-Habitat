# Hypergravity Habitat

**A proposal-oriented research documentation project for sustained moderate hypergravity as a terrestrial experimental environment.**

---

## Executive Summary

Hypergravity Habitat is an early-stage research and feasibility documentation project. It explores whether a terrestrial platform could support controlled experiments at sustained effective gravity levels above Earth-normal gravity.

The project addresses a possible gap between existing altered-gravity research regimes: orbital microgravity, parabolic flight, bed-rest analogues, high-g exposure, short-duration centrifugation, and conventional laboratory studies. These platforms are scientifically valuable, but they do not fully answer what could be learned from sustained, moderate, experimentally controlled hypergravity exposure over durations long enough to observe adaptation rather than only acute response.

The central research question is:

> How do biological, technical, and human-centred systems respond to sustained effective gravity above 1 g over scientifically meaningful durations?

This repository does **not** propose immediate construction or operation of a facility. Its purpose is to develop a rigorous basis for literature review, modelling, demonstrator definition, expert discussion, feasibility assessment, and future collaboration.

---

## Research Vision

The long-term vision is to evaluate whether sustained moderate hypergravity deserves to be developed as a distinct research-infrastructure class.

Potential research domains include:

- artificial-gravity research,
- space medicine and countermeasure research,
- human physiology,
- biomechanics and human performance,
- plant science,
- cell and microbial biology,
- controlled-environment agriculture,
- railway and maglev engineering,
- rotating-platform and guideway demonstrators,
- research infrastructure planning.

The project remains architecture-neutral. Circular railway systems, magnetic levitation systems, rotating structures, payload-only rigs, and hybrid demonstrators are treated as candidates to be compared against common scientific and engineering requirements.

---

## Research Gap

| Research regime | Typical platform | Typical duration | Gravity environment | Limitation for this project |
|---|---|---:|---:|---|
| Orbital microgravity | Space station | Days to months | Near 0 g | Not elevated gravity |
| Parabolic flight | Aircraft | Seconds | Alternating low-g and high-g | Too short for adaptation |
| Bed-rest analogue | Clinical facility | Days to months | 1 g with unloading analogue | Does not create elevated effective gravity |
| Human centrifuge | Ground centrifuge | Minutes to hours in many protocols | Elevated acceleration | Usually not a continuous habitat or laboratory |
| Biological centrifuge | Laboratory centrifuge | Variable | Elevated acceleration | Often small-scale and payload-specific |
| Hypergravity Habitat concept | Terrestrial circular, rotating, or guided platform | To be studied | Moderately above 1 g | Requires feasibility validation |

The research gap is the lack of a clearly defined, controlled, long-duration research environment for studying moderate hypergravity as its own scientific regime.

---

## Evidence Levels

All documents should distinguish between evidence levels.

| Evidence level | Meaning |
|---|---|
| Established knowledge | Supported by accepted physics, engineering practice, or peer-reviewed literature |
| Engineering principle | Direct consequence of transparent equations and assumptions |
| Engineering estimate | Approximation based on stated assumptions and uncertainty |
| Working hypothesis | Plausible idea requiring validation |
| Open research question | Topic requiring further review, modelling, or experiment |

This distinction is essential because the project combines established mechanics with early-stage infrastructure concepts.

---

## Repository Structure

```text
README.md

docs/
  concept-note.md
  proposal-brief.md
  research-gap.md
  literature-review.md
  scientific-questions.md
  glossary.md
  roadmap.md
  work-packages.md
  risk-register.md
  safety-case-outline.md
  ethics-and-governance.md
  data-management-plan.md
  requirements-traceability-matrix.md
  facility-comparison.md
  architecture-trade-study.md
  minimum-useful-demonstrator.md
  experimental-programme.md
  physics-reference.md
  vibration-and-confounders.md
  habitability.md

  science/
    human-physiology.md
    biology.md
    plant-science.md
    sports-science.md
    coriolis-projectile-accuracy.md

  engineering/
    design-requirements.md
    preliminary-sizing.md
    railway-platform.md
    tilting-train-and-cant-limits.md
    railway-g-envelope.md
    full-ring-vehicle-concept.md
    maglev-platform.md
    transfer-system-concept.md

  economics/
    cost-model.md

calculations/
  README.md
  hypergravity_sizing.py
  coriolis_projectile_deflection.py
  railway_g_envelope.py

diagrams/
  README.md

simulations/
  Numerical models and parameter studies

references/
  Literature notes and source material

papers/
  Draft papers, whitepapers, and proposal-oriented documents
```

---

## Main Documents

### Concept and Proposal Framing

- [`docs/concept-note.md`](docs/concept-note.md) — proposal-grade concept framing.
- [`docs/proposal-brief.md`](docs/proposal-brief.md) — short brief suitable for academic or institutional feedback.
- [`docs/research-gap.md`](docs/research-gap.md) — structured research-gap analysis.
- [`docs/literature-review.md`](docs/literature-review.md) — annotated literature review, search strategy, inclusion/exclusion criteria, and evidence matrix.
- [`docs/scientific-questions.md`](docs/scientific-questions.md) — research-question catalogue.
- [`docs/glossary.md`](docs/glossary.md) — controlled terminology and notation.

### Programme, Governance, and Reviewability

- [`docs/roadmap.md`](docs/roadmap.md) — staged research and development roadmap.
- [`docs/work-packages.md`](docs/work-packages.md) — proposal-style work packages, deliverables, and milestones.
- [`docs/risk-register.md`](docs/risk-register.md) — preliminary risk register.
- [`docs/safety-case-outline.md`](docs/safety-case-outline.md) — preliminary safety-case framework.
- [`docs/ethics-and-governance.md`](docs/ethics-and-governance.md) — human, animal, biological, sports-science, and data governance framework.
- [`docs/data-management-plan.md`](docs/data-management-plan.md) — FAIR/open-science and sensitive-data handling framework.
- [`docs/requirements-traceability-matrix.md`](docs/requirements-traceability-matrix.md) — requirement-to-evidence traceability.

### Demonstrator and Architecture Logic

- [`docs/facility-comparison.md`](docs/facility-comparison.md) — comparison with existing research infrastructure.
- [`docs/architecture-trade-study.md`](docs/architecture-trade-study.md) — comparison of no-build, existing facilities, payload demonstrator, rotating, rail, maglev, and hybrid options.
- [`docs/minimum-useful-demonstrator.md`](docs/minimum-useful-demonstrator.md) — payload-first demonstrator strategy.
- [`docs/experimental-programme.md`](docs/experimental-programme.md) — staged experimental programme.
- [`docs/physics-reference.md`](docs/physics-reference.md) — physics and notation reference.
- [`docs/vibration-and-confounders.md`](docs/vibration-and-confounders.md) — confounder-control framework.
- [`docs/habitability.md`](docs/habitability.md) — human-factors and habitability framework.

### Science

- [`docs/science/human-physiology.md`](docs/science/human-physiology.md) — human physiology and adaptation questions.
- [`docs/science/biology.md`](docs/science/biology.md) — cell, microbial, organismal, and model-system biology.
- [`docs/science/plant-science.md`](docs/science/plant-science.md) — plant growth, gravitropism, controlled-environment agriculture.
- [`docs/science/sports-science.md`](docs/science/sports-science.md) — human performance and sports-science questions, treated cautiously as a later-stage domain.
- [`docs/science/coriolis-projectile-accuracy.md`](docs/science/coriolis-projectile-accuracy.md) — Coriolis limits on sport-specific projectile accuracy and skill maintenance during hypergravity residency.

### Engineering and Feasibility

- [`docs/engineering/design-requirements.md`](docs/engineering/design-requirements.md) — technology-neutral requirements framework.
- [`docs/engineering/preliminary-sizing.md`](docs/engineering/preliminary-sizing.md) — vector-corrected radius, speed, acceleration, and sizing model.
- [`docs/engineering/railway-platform.md`](docs/engineering/railway-platform.md) — circular railway concept assessment.
- [`docs/engineering/tilting-train-and-cant-limits.md`](docs/engineering/tilting-train-and-cant-limits.md) — tilting trains, track cant, cant deficiency, floor alignment, wheel unloading, and maximum-g constraints for railway concepts.
- [`docs/engineering/railway-g-envelope.md`](docs/engineering/railway-g-envelope.md) — first-order achievable-g corridor for railway concepts under cant, cant deficiency, tilt, and safety constraints.
- [`docs/engineering/full-ring-vehicle-concept.md`](docs/engineering/full-ring-vehicle-concept.md) — mechanically connected full-ring vehicle concept between conventional railway and rotating annular habitat.
- [`docs/engineering/maglev-platform.md`](docs/engineering/maglev-platform.md) — magnetic-levitation concept assessment.
- [`docs/engineering/transfer-system-concept.md`](docs/engineering/transfer-system-concept.md) — staged access, logistics, and emergency-transfer concepts.

### Economics

- [`docs/economics/cost-model.md`](docs/economics/cost-model.md) — staged cost framework for CAPEX, OPEX, renewal, and funding logic.

### Calculations and Figures

- [`calculations/README.md`](calculations/README.md) — calculation standards and usage notes.
- [`calculations/hypergravity_sizing.py`](calculations/hypergravity_sizing.py) — dependency-free sizing calculator for circular terrestrial hypergravity concepts.
- [`calculations/coriolis_projectile_deflection.py`](calculations/coriolis_projectile_deflection.py) — first-order Coriolis deflection estimator for thrown or kicked projectiles.
- [`calculations/railway_g_envelope.py`](calculations/railway_g_envelope.py) — first-order railway g-envelope screening calculator.
- [`diagrams/README.md`](diagrams/README.md) — planned figure set for proposal and review material.

---

## Candidate Concepts

### Circular Railway Platform

A circular railway platform could use a large-radius track and continuous motion to generate centripetal acceleration. This approach may benefit from mature rail engineering, but it raises questions about vibration, wear, access, maintenance, banking geometry, tilting-vehicle feasibility, land use, emergency stopping, and cost.

### Full-Ring Vehicle

A mechanically connected full-ring vehicle could reduce the intuitive problem of a short train tipping or sliding on a steeply canted curve by distributing loads around a closed annular structure. However, it becomes a specialized guided ring system with new constraints: structural load paths, guideway capture, thermal expansion, vibration modes, stopped-state behaviour, maintenance, and emergency access.

### Magnetic Levitation Platform

A maglev platform could reduce mechanical contact and may offer improved ride quality. It also introduces system complexity, power electronics, electromagnetic-compatibility questions, specialized maintenance, safety-case uncertainty, and cost risk.

### Rotating or Hybrid Platform

A rotating or hybrid demonstrator could provide a direct artificial-gravity test environment. Smaller demonstrators may be useful for instrumentation, biological payloads, and parameter validation. Larger rotating systems require deeper structural, human-factors, and safety analysis.

### Payload-Only Demonstrator

A small payload demonstrator may be the most credible first experimental step. It could test acceleration stability, vibration, environmental control, data logging, and simple biological payloads before any human-centred work is considered.

---

## Current Development Logic

The repository is organized around staged feasibility, not immediate implementation.

1. Define the research gap.
2. Establish cautious scientific questions.
3. Build reproducible physics and sizing models.
4. Compare candidate concepts against common requirements.
5. Identify the smallest useful demonstrator.
6. Test measurement quality and confounders.
7. Use low-risk biological payloads before human studies.
8. Create a safety, ethics, and risk framework.
9. Seek external expert review.
10. Prepare a formal pre-feasibility proposal only if earlier stages justify it.

---

## Documentation Standards

Contributions should:

- separate facts from hypotheses,
- state assumptions explicitly,
- use SI units consistently,
- show equations before derived numbers,
- cite sources wherever possible,
- document uncertainty and limitations,
- avoid promotional language,
- identify safety and ethics constraints,
- make calculations reproducible,
- include stop/go decision points where appropriate.

---

## Collaboration

The project welcomes critical feedback from researchers and practitioners in aerospace medicine, artificial gravity, physiology, biomechanics, plant science, cell biology, microbiology, sports science, railway engineering, maglev systems, rotating structures, safety engineering, research ethics, simulation, and research infrastructure planning.

The most valuable contributions at this stage are not advocacy but critique: identifying weak assumptions, missing literature, hidden risks, better experimental pathways, or more credible demonstrator concepts.

---

## Disclaimer

This repository is an exploratory research and documentation project. It does not propose immediate construction, human exposure, clinical application, or operation of any facility. Any real-world implementation would require scientific review, engineering validation, safety assessment, ethical review, medical governance, regulatory compliance, and institutional oversight.

---

## License

Documentation is intended to be published under Creative Commons Attribution 4.0 International (CC BY 4.0) unless otherwise stated.

Software, simulations, datasets, diagrams, or generated artifacts may use different licenses where appropriate.