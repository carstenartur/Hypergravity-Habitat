# Requirements Traceability Matrix

**Project:** Hypergravity Habitat  
**Document type:** requirements traceability matrix  
**Status:** initial framework  
**Scope:** links scientific, engineering, safety, ethics, and demonstrator requirements to verification methods and current documents

---

## 1. Purpose

This document provides a traceability structure for the Hypergravity Habitat project. It connects requirements to their source, design response, verification method, and current status.

The purpose is to make the project reviewable:

> A reviewer should be able to see where each requirement comes from, which document addresses it, and how it could be verified.

---

## 2. Status Definitions

| Status | Meaning |
|---|---|
| open | requirement identified but not yet addressed |
| drafted | addressed in documentation but not verified |
| modelled | supported by calculation or simulation |
| testable | demonstrator or verification method defined |
| verified | evidence exists |
| deferred | later-stage requirement |
| rejected | no longer part of current scope |

---

## 3. Requirement Categories

| Prefix | Category |
|---|---|
| SCI | scientific requirement |
| PHY | physics/model requirement |
| BIO | biological payload requirement |
| HUM | human-subject requirement |
| ENG | engineering requirement |
| SAF | safety requirement |
| ETH | ethics/governance requirement |
| DAT | data-management requirement |
| ECO | economic/programme requirement |
| DEM | demonstrator requirement |

---

## 4. Traceability Matrix

| ID | Requirement | Source document | Design response | Verification method | Status |
|---|---|---|---|---|---|
| SCI-001 | Define the research gap before architecture selection | `research-gap.md`, `facility-comparison.md` | annotated review and facility comparison | expert review | drafted |
| SCI-002 | Distinguish acute response from adaptation | `scientific-questions.md` | exposure-duration taxonomy | protocol design | drafted |
| SCI-003 | Use low-risk early payloads before human studies | `minimum-useful-demonstrator.md` | payload-first strategy | demonstrator plan | drafted |
| PHY-001 | Use vector-corrected resultant gravity model | `preliminary-sizing.md`, `physics-reference.md` | equations and sizing script | code review, calculation check | modelled |
| PHY-002 | Calculate radius, speed, angular rate, and bank angle | `preliminary-sizing.md` | `hypergravity_sizing.py` | script output | modelled |
| PHY-003 | Model Coriolis effects for projectile tasks | `literature-review.md`, `sports-science.md` | `coriolis_projectile_deflection.py` | script output and later 3D model | modelled |
| BIO-001 | Include matched 1 g biological controls | `biology.md`, `plant-science.md` | payload protocol requirement | demonstrator protocol | drafted |
| BIO-002 | Log environmental variables for biological payloads | `data-management-plan.md`, `vibration-and-confounders.md` | metadata and sensor requirements | data package review | drafted |
| BIO-003 | Prevent contamination and define sample handling | `ethics-and-governance.md` | biosafety and handling plan | biosafety review | open |
| HUM-001 | Defer human studies until safety and ethics exist | `ethics-and-governance.md`, `roadmap.md` | staged roadmap | governance checkpoint | drafted |
| HUM-002 | Define medical stop criteria before exposure | `human-physiology.md`, `safety-case-outline.md` | medical governance requirement | ethics/medical review | open |
| HUM-003 | Treat sports training claims as hypotheses | `sports-science.md` | evidence-level language | document review | drafted |
| ENG-001 | Measure acceleration and vibration continuously | `design-requirements.md`, `vibration-and-confounders.md` | instrumentation requirement | sensor calibration and test run | drafted |
| ENG-002 | Define safe state for each demonstrator | `safety-case-outline.md` | safe-state requirement | integrated test | open |
| ENG-003 | Compare architecture options before selection | `architecture-trade-study.md` | trade-study matrix | expert review | drafted |
| SAF-001 | Maintain a risk register | `risk-register.md` | risk categories and mitigation | periodic review | drafted |
| SAF-002 | Define emergency stop/shutdown concept | `safety-case-outline.md` | safety requirement | demonstrator test | open |
| SAF-003 | Define fire and power-loss response | `safety-case-outline.md` | hazard sections | safety review | open |
| ETH-001 | Require ethics approval for human studies | `ethics-and-governance.md` | governance checkpoint | institutional approval | drafted |
| ETH-002 | Apply 3R principles for animal research | `ethics-and-governance.md` | animal research governance | animal ethics review | drafted |
| DAT-001 | Use reproducible calculation scripts | `data-management-plan.md`, `calculations/README.md` | Python scripts in repository | code review | drafted |
| DAT-002 | Define metadata for demonstrator runs | `data-management-plan.md` | metadata requirements | template and dataset audit | drafted |
| DAT-003 | Protect sensitive human data | `data-management-plan.md`, `ethics-and-governance.md` | privacy requirements | data protection review | open |
| ECO-001 | Use staged cost model, not full facility estimate | `cost-model.md` | staged cost framework | funding review | drafted |
| DEM-001 | Define minimum useful demonstrator | `minimum-useful-demonstrator.md` | payload-first recommendation | expert review | drafted |
| DEM-002 | Include stop/go criteria | `roadmap.md`, `minimum-useful-demonstrator.md` | decision tables | milestone review | drafted |

---

## 5. Verification Methods

Possible verification methods:

- literature review,
- expert review,
- equation check,
- script output,
- simulation,
- sensor calibration,
- bench test,
- integrated demonstrator test,
- biosafety review,
- ethics approval,
- safety case review,
- data audit,
- cost sensitivity analysis.

---

## 6. Missing Verification Artifacts

The following artifacts are still needed:

1. metadata template,
2. acceleration and vibration CSV schema,
3. biological payload protocol template,
4. safety test checklist,
5. expert-review questionnaire,
6. architecture scoring sheet,
7. cost sensitivity spreadsheet or script,
8. diagram set for physics and roadmap.

---

## 7. Maintenance Rules

- Add every new major requirement to this file.
- Do not leave a requirement without a source document.
- Do not claim verification until evidence exists.
- Use `deferred` for later-stage requirements rather than deleting them.
- Update status after each major documentation or demonstrator phase.

---

## 8. Preliminary Conclusion

The requirements traceability matrix turns the repository from a set of documents into a reviewable system. It should become the central checklist for future development, especially if the project is prepared for academic feedback or funding review.