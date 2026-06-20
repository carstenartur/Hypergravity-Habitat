# Preliminary Sizing Study

**Project:** Hypergravity Habitat  
**Document:** Preliminary Engineering Sizing  
**Version:** 0.2 (Working Draft)

---

# Purpose

This document provides a first-order engineering comparison of several candidate Hypergravity Habitat configurations.

It is **not** a construction proposal.

Its purpose is to identify the principal relationships between

- ring radius,
- operating speed,
- infrastructure size,
- construction cost,
- operating cost,
- maintainability,
- scalability.

All calculations are preliminary and intended for feasibility discussions.

---

# Assumptions

## Target gravity levels

The project currently evaluates two operating points.

| Parameter | Value |
|-----------|------:|
| Earth gravity | 1.00 g |
| Scenario A | 1.10 g |
| Scenario B | 1.25 g |

The additional radial acceleration therefore becomes

| Scenario | Additional radial acceleration |
|----------|-------------------------------:|
|1.10 g|0.10 g = 0.981 m/s²|
|1.25 g|0.25 g = 2.452 m/s²|

---

# Equations

Required speed:

$begin:math:display$
v\=\\sqrt\{a \\cdot r\}
$end:math:display$

where

- v = velocity (m/s)
- a = additional radial acceleration
- r = ring radius

Track length:

$begin:math:display$
L\=2\\pi r
$end:math:display$

---

# Candidate Ring Sizes

| Radius | Track length |
|---------:|------------:|
|100 m|628 m|
|200 m|1,257 m|
|400 m|2,513 m|
|500 m|3,142 m|
|1000 m|6,283 m|
|2000 m|12,566 m|

---

# Required Operating Speed

| Radius | 1.10 g | 1.25 g |
|---------:|-------:|-------:|
|100 m|36 km/h|57 km/h|
|200 m|50 km/h|80 km/h|
|400 m|71 km/h|114 km/h|
|500 m|80 km/h|127 km/h|
|1000 m|113 km/h|180 km/h|
|2000 m|160 km/h|255 km/h|

> **Note:** These values are recalculated directly from the equations above and supersede earlier rough estimates discussed during the concept phase.

---

# Approximate Lap Time

| Radius | 1.10 g | 1.25 g |
|---------:|-------:|-------:|
|100 m|63 s|40 s|
|200 m|90 s|57 s|
|400 m|127 s|79 s|
|500 m|141 s|89 s|
|1000 m|200 s|126 s|
|2000 m|283 s|178 s|

---

# Reference Railway Cost Model

The following assumptions are used throughout the repository.

These values are placeholders and shall be replaced by literature values later.

| Parameter | Assumption |
|-----------|-----------:|
|High-quality railway construction|25 M€/km|
|Operations building|10 M€|
|Workshop|8 M€|
|Electrical infrastructure|5 M€|
|Contingency|20 %|

---

# Estimated Track Cost

| Radius | Track length | Track cost |
|---------:|------------:|-----------:|
|100 m|0.63 km|15.7 M€|
|200 m|1.26 km|31.4 M€|
|400 m|2.51 km|62.8 M€|
|500 m|3.14 km|78.5 M€|
|1000 m|6.28 km|157.1 M€|
|2000 m|12.57 km|314.2 M€|

---

# Demonstrator Rolling Stock

Reference configuration

- 1 locomotive
- 3 passenger coaches
- medical instrumentation
- basic laboratory equipment

The exact vehicle type remains open.

Using existing rolling stock is expected to minimise project cost.

---

# Capital Cost (Demonstrator)

| Component | Estimate |
|-----------|----------:|
|Track|see table above|
|Rolling stock|2–6 M€|
|Workshop & depot|18 M€|
|Utilities|5 M€|
|Contingency|20 %|

### Example (500 m radius)

| Component | Cost |
|-----------|----:|
|Track|78.5 M€|
|Rolling stock|4 M€|
|Buildings|23 M€|
|Contingency|21 M€|
|**Total**|**≈127 M€**|

---

# Operating Cost Model

Operating costs depend mainly on

- electricity
- personnel
- wheel wear
- rail wear
- scheduled maintenance

Instead of presenting unsupported values, future revisions shall derive annual operating costs from

- annual distance travelled,
- axle loads,
- maintenance intervals,
- electricity price,
- staffing model.

---

# Railway vs. Maglev

| Criterion | Railway | Maglev |
|-----------|:-------:|:------:|
|Technology readiness|★★★★★|★★★★☆|
|Initial investment|★★★★★|★★☆☆☆|
|Mechanical wear|★★☆☆☆|★★★★★|
|Ride quality|★★★☆☆|★★★★★|
|Maintenance complexity|★★★☆☆|★★★★☆|
|Upgrade potential|★★★★☆|★★★★★|

---

# Engineering Observations

A smaller radius

- reduces construction cost,
- reduces land use,
- increases curvature,
- increases wheel and rail wear.

A larger radius

- improves ride quality,
- reduces curvature,
- increases infrastructure cost,
- requires higher operating speed for the same effective gravity.

No optimum radius can currently be identified without considering maintenance cost, human comfort and scientific requirements simultaneously.

---

# Open Engineering Questions

- What minimum radius provides acceptable ride comfort?
- How does wheel wear scale with continuous operation?
- What is the optimal compromise between CAPEX and OPEX?
- At which radius does a maglev solution become economically competitive?
- Can the same infrastructure support multiple target gravity levels?

---

# Revision History

**Version 0.1**

- Initial sizing study.

**Version 0.2**

- Equations added.
- Assumptions documented.
- Cost model made traceable.
- Unsupported OPEX values removed.
- Tables reorganised around engineering decisions rather than descriptive text.