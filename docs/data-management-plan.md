# Data Management Plan

**Project:** Hypergravity Habitat  
**Document type:** preliminary data-management plan  
**Status:** working document for pre-feasibility and demonstrator planning  
**Scope:** engineering, environmental, biological, human-subject, metadata, code, and open-science data governance

---

## 1. Purpose

This document defines how data should be generated, documented, stored, shared, and protected in the Hypergravity Habitat project.

The core data-management question is:

> How can the project make calculations, demonstrator data, environmental measurements, and experimental results reproducible while protecting sensitive data and avoiding unsupported claims?

This plan should be updated before any real experiment begins.

---

## 2. Data Philosophy

The project should follow four principles.

1. **Reproducibility:** calculations and analysis should be repeatable.
2. **Metadata completeness:** acceleration, vibration, environment, and operational events must be recorded.
3. **Appropriate openness:** non-sensitive data should be shareable where possible.
4. **Protection of sensitive data:** human health, performance, and identifiable data require strict governance.

---

## 3. Data Types

| Data type | Examples | Sensitivity | Likely sharing status |
|---|---|---:|---|
| calculation data | radius, speed, acceleration tables | low | open |
| simulation data | parameter sweeps, model outputs | low-medium | open where possible |
| sensor data | acceleration, vibration, temperature, humidity | low-medium | open where possible |
| biological data | growth curves, images, assay outputs | medium | share with metadata if safe |
| human physiological data | ECG, blood pressure, sleep, performance | high | restricted or anonymized |
| video/image data | participant or payload recordings | variable | restricted if identifiable |
| operational logs | transfer events, stops, maintenance | medium | project-controlled |
| safety data | incident reports, hazard logs | medium-high | controlled |
| code | calculation and analysis scripts | low | open by default |

---

## 4. Metadata Requirements

Every experiment or demonstrator run should record:

- experiment ID,
- date and time,
- operator,
- platform version,
- payload version,
- target gravity,
- measured acceleration vector,
- angular rate,
- vibration spectrum,
- temperature,
- humidity,
- CO2 where relevant,
- light level and spectrum where relevant,
- power interruptions,
- transfer or stop events,
- protocol deviations,
- calibration status,
- analysis software version.

Without metadata, experimental results may not be interpretable.

---

## 5. File and Dataset Naming

Suggested convention:

```text
YYYYMMDD_project_stage_payload_run_datatype_version.ext
```

Example:

```text
20260715_stage2_seedling_run03_acceleration_v01.csv
20260715_stage2_seedling_run03_images_v01.zip
20260715_stage2_seedling_run03_protocol_v01.md
```

---

## 6. Version Control

Use Git for:

- documentation,
- calculation scripts,
- analysis scripts,
- metadata templates,
- small tabular datasets,
- protocol files.

Do not store large binary datasets directly in Git unless explicitly planned. Use a separate data repository or large-file system for large imaging, sensor, or video datasets.

---

## 7. Data Storage

A future implementation should define:

- primary storage location,
- backup location,
- access permissions,
- retention period,
- encryption requirements,
- data owner,
- data steward,
- recovery procedure.

For human-subject data, storage must comply with applicable data-protection law and institutional rules.

---

## 8. FAIR Principles

Where possible, data should be:

- **Findable:** use identifiers and structured metadata.
- **Accessible:** define access conditions.
- **Interoperable:** use common formats such as CSV, JSON, HDF5, TIFF, Markdown, or open metadata standards.
- **Reusable:** include methods, units, calibration, and license information.

Not all data can be open. Sensitive human data may require restricted access.

---

## 9. Human Data Governance

Human-subject data may include:

- medical data,
- physiological monitoring,
- movement data,
- sleep data,
- performance data,
- video,
- psychological questionnaires,
- personal information.

Requirements:

- ethics approval,
- informed consent,
- data minimization,
- pseudonymization,
- access control,
- secure storage,
- defined retention period,
- withdrawal procedure,
- publication rules,
- re-identification risk assessment.

Human data should not be treated as open by default.

---

## 10. Biological Data Governance

Biological datasets should include:

- organism or cell type,
- strain or cultivar,
- growth medium,
- environmental conditions,
- exposure duration,
- gravity level,
- vibration and acceleration logs,
- imaging settings,
- assay method,
- control condition,
- contamination status,
- sample handling events.

For genetically modified organisms, pathogens, or controlled materials, additional governance applies.

---

## 11. Engineering Data Governance

Engineering data should include:

- sensor model,
- calibration date,
- sampling rate,
- sensor location,
- coordinate system,
- raw signal,
- filtered signal if used,
- processing script,
- uncertainty estimate,
- event log.

Acceleration and vibration data are core project data. They should be preserved even when biological or human results are inconclusive.

---

## 12. Analysis Reproducibility

Every analysis should include:

- raw input data reference,
- cleaning steps,
- analysis code,
- software version,
- output files,
- plots,
- assumptions,
- excluded data and reason,
- uncertainty statement.

The project should prefer scripts or notebooks over manual spreadsheet calculations for key outputs.

---

## 13. Licensing

Suggested defaults:

- documentation: CC BY 4.0 unless otherwise stated,
- code: permissive open-source license to be selected,
- non-sensitive datasets: open license where appropriate,
- human data: restricted access or anonymized subset only,
- third-party data: follow original license.

The repository should not assume that all future data can be public.

---

## 14. Data Publication Packages

A publication-quality dataset should include:

- protocol,
- raw data,
- processed data,
- metadata,
- calibration files,
- analysis code,
- README,
- license,
- limitations,
- contact or maintainer information.

---

## 15. Data Risks

| Risk | Mitigation |
|---|---|
| missing metadata | mandatory metadata template |
| uncalibrated sensors | calibration log |
| undocumented processing | version-controlled scripts |
| privacy breach | access control and pseudonymization |
| large binary file loss | backup and external data storage |
| unsupported claims | link conclusions to data and uncertainty |
| confounders not logged | minimum environmental logging standard |

---

## 16. Immediate Actions

1. Create metadata templates for payload runs.
2. Define CSV schema for acceleration and vibration data.
3. Define experiment ID convention.
4. Add code license decision.
5. Add data storage plan before any real experiment.
6. Add human-data privacy protocol before any human research.

---

## 17. Preliminary Conclusion

The Hypergravity Habitat project depends on data quality. Without complete metadata, acceleration logs, vibration data, environmental measurements, and reproducible analysis, biological or human findings would be difficult to interpret.

Data management is therefore not administrative overhead; it is central to scientific validity.