# Ethics and Governance Framework

**Project:** Hypergravity Habitat  
**Document type:** ethics and governance framework  
**Status:** working document for pre-feasibility review  
**Scope:** human-subject research, biological payloads, animal research, data governance, medical oversight, and institutional review

---

## 1. Purpose

This document defines the ethical and governance principles for the Hypergravity Habitat project. It is intended to prevent premature claims or unsafe development pathways, especially where human participants, animals, biological samples, or personal data could be involved.

The core governance question is:

> What review, oversight, consent, safety, welfare, and data-protection structures are required before each class of research can proceed?

This document is not an ethics approval. It is a framework for determining what approvals and safeguards would be required in future stages.

---

## 2. Governance Principle

The project should follow this order:

1. literature review,
2. modelling,
3. instrumented non-living payloads,
4. low-risk biological payloads,
5. expert review,
6. formal pre-feasibility study,
7. only then possible human-subject or animal research if justified.

No document in this repository should imply that human habitation, clinical use, animal studies, or athlete training interventions are ready for implementation.

---

## 3. Research Classes and Governance Burden

| Research class | Example | Governance burden |
|---|---|---|
| Non-living physical payload | sensors, dummy masses, materials samples | technical safety review |
| Contained biological payload | microbes, cells, plants | biosafety and containment review |
| Human data only | modelling, surveys, public datasets | data ethics and privacy review if identifiable |
| Short human exposure | tolerance or motion study | ethics approval, medical review, safety case |
| Repeated human exposure | training or adaptation study | higher ethics and medical oversight |
| Long-duration human study | habitation or residency | full institutional governance and independent monitoring |
| Animal study | model organism or vertebrate study | formal animal ethics approval and 3R justification |

---

## 4. Human-Subject Research

Human studies require:

- independent ethics approval,
- medical governance,
- informed consent,
- participant screening,
- risk-benefit assessment,
- adverse-event reporting,
- data-protection plan,
- right to withdraw,
- emergency procedures,
- stop criteria,
- independent review for higher-risk protocols.

### 4.1 Human-Subject Caution

Human-subject studies are not justified simply because the project is interesting. They require:

1. a precise scientific question,
2. evidence that non-human alternatives are insufficient,
3. a mature technical safety case,
4. medically acceptable exposure limits,
5. defined monitoring and emergency response,
6. review by competent institutional bodies.

### 4.2 Participant Groups

Different participant groups have different ethical issues.

| Group | Ethical concern |
|---|---|
| healthy volunteers | avoid unnecessary risk and undue inducement |
| athletes | career impact, injury risk, performance disruption |
| clinical populations | therapeutic misconception and vulnerability |
| older adults | higher physiological risk |
| employees or students | possible coercion |
| military or occupational participants | institutional pressure and dual-use concerns |

Elite athletes require particular caution because injury, technique disruption, or performance loss may have professional consequences.

---

## 5. Informed Consent

Consent materials should state clearly:

- study purpose,
- procedures,
- exposure conditions,
- expected duration,
- known and unknown risks,
- right to withdraw,
- medical monitoring,
- data collected,
- data storage and sharing,
- compensation if any,
- adverse-event handling,
- limits of confidentiality,
- contact information for investigators and ethics body.

Consent must not overstate possible benefits. For early stages, participants should be told that sustained moderate hypergravity effects are uncertain.

---

## 6. Medical Governance

Human studies require medical oversight appropriate to exposure level.

Possible requirements:

- pre-participation medical screening,
- cardiovascular risk assessment,
- musculoskeletal assessment,
- vestibular susceptibility assessment,
- medication review,
- emergency medical plan,
- monitoring during exposure,
- recovery follow-up,
- adverse-event reporting,
- medical stop criteria.

Medical governance should be independent of project enthusiasm.

---

## 7. Sports-Science Governance

Sports-science use cases require additional caution.

Potential concerns:

- injury risk during elevated-load exercise,
- disruption of sport-specific skill,
- unproven performance benefit,
- pressure from teams, coaches, or sponsors,
- conflicts of interest,
- unequal access to experimental methods,
- anti-doping or regulatory interpretation if performance claims emerge.

The project should frame sports science as research into load adaptation and human performance, not as a proven training method.

---

## 8. Animal Research

Animal research should not be an early default.

Before animal studies are considered, the project should show:

1. a strong scientific rationale,
2. lack of adequate replacement methods,
3. clear welfare monitoring,
4. formal animal ethics approval,
5. trained personnel,
6. safe housing and environmental control,
7. humane endpoints,
8. statistically justified sample sizes.

The project should apply the 3R principles:

- **Replacement:** use non-animal methods where possible,
- **Reduction:** use the fewest animals consistent with valid science,
- **Refinement:** minimize distress and improve welfare.

---

## 9. Biological Payload Governance

Biological payloads require governance even without animals or humans.

Requirements may include:

- biosafety classification,
- containment plan,
- contamination prevention,
- sample-handling protocol,
- waste-handling protocol,
- decontamination plan,
- transport procedure,
- environmental logging,
- incident reporting.

For genetically modified organisms, pathogens, or higher-risk materials, additional legal and institutional controls would apply.

---

## 10. Data Governance

The project may generate:

- sensor data,
- biological data,
- environmental data,
- video or imaging data,
- medical data,
- performance data,
- behavioural data,
- personal or identifiable data.

Data governance should address:

- data minimization,
- lawful basis for collection,
- consent,
- anonymization or pseudonymization,
- storage security,
- access control,
- retention period,
- sharing policy,
- publication policy,
- withdrawal and deletion rights where applicable.

Human health and performance data must be treated as sensitive data.

---

## 11. FAIR and Open Science

Where possible, non-sensitive research data should follow FAIR principles:

- findable,
- accessible,
- interoperable,
- reusable.

For human data, openness must be balanced with privacy, consent, and re-identification risk.

Recommended practice:

- publish code and calculation models,
- publish metadata schemas,
- publish anonymized environmental and engineering datasets where possible,
- restrict identifiable human data,
- document data provenance.

---

## 12. Conflict of Interest

Potential conflicts:

- commercial training claims,
- technology supplier bias,
- sports performance marketing,
- pressure to justify infrastructure,
- selective reporting of positive results,
- funding-driven architecture selection.

Mitigation:

- disclose conflicts,
- use independent review,
- separate scientific evaluation from promotional material,
- publish negative and inconclusive findings where appropriate,
- maintain evidence-level labels.

---

## 13. Claims Governance

The repository should not claim that hypergravity:

- improves performance,
- treats disease,
- prevents bone loss,
- builds muscle better than established training,
- is safe for long-duration exposure,
- is economically justified,
- is ready for human habitation.

Permitted language at the current stage:

- “hypothesis”,
- “research question”,
- “candidate use case”,
- “requires validation”,
- “requires expert review”,
- “pre-feasibility concept”.

---

## 14. Governance Checkpoints

| Checkpoint | Required before |
|---|---|
| technical safety review | any moving or rotating demonstrator |
| biosafety review | biological payloads |
| data protection review | identifiable human data |
| ethics approval | human-subject research |
| medical governance | human exposure |
| animal ethics approval | animal studies |
| independent expert review | pre-feasibility funding proposal |
| full safety case | occupied long-duration platform |

---

## 15. Relationship to Other Documents

This document should be read with:

- `docs/safety-case-outline.md`,
- `docs/risk-register.md`,
- `docs/data-management-plan.md`,
- `docs/science/human-physiology.md`,
- `docs/science/sports-science.md`,
- `docs/minimum-useful-demonstrator.md`.

---

## 16. Preliminary Conclusion

Ethics and governance are not barriers to the project; they are what make the project credible. The safest and most fundable path is to begin with models and non-human payloads, document uncertainty honestly, and defer human or animal studies until evidence and formal review justify them.