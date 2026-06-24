# Preliminary Sizing Study

**Project:** Hypergravity Habitat  
**Document type:** preliminary engineering sizing and parameter study  
**Status:** working document for pre-feasibility review  
**Scope:** relationship between target effective gravity, lateral acceleration, radius, speed, angular rate, infrastructure size, and first-order cost drivers

---

## 1. Purpose

This document provides first-order sizing relationships for candidate Hypergravity Habitat configurations. It is not a construction proposal and should not be read as a final engineering design.

Its purpose is to make the dominant physical relationships explicit before architecture selection. In particular, it corrects a common simplification: for a terrestrial circular platform, target effective gravity is the vector result of Earth gravity and generated lateral acceleration, not simply Earth gravity plus an additional vertical component.

The document supports comparison of:

- small rotating or guided demonstrators,
- circular railway concepts,
- magnetic levitation concepts,
- larger habitat-scale systems.

---

## 2. Core Physical Model

For a body moving in a circle:

\[
a_c = \frac{v^2}{r} = \omega^2 r
\]

where:

- \(a_c\) = centripetal acceleration in m/s²,
- \(v\) = tangential speed in m/s,
- \(r\) = radius in m,
- \(\omega\) = angular velocity in rad/s.

On Earth, a circular platform combines vertical gravity with horizontal centripetal acceleration:

\[
g_{eff} = \sqrt{g^2 + a_c^2}
\]

Solving for the required lateral acceleration:

\[
a_c = g \sqrt{g_{rel}^2 - 1}
\]

where \(g_{rel}\) is the desired resultant effective gravity in multiples of 1 g.

The bank angle or cabin-tilt angle needed to align the floor with the resultant load vector is:

\[
\theta = \arctan\left(\frac{a_c}{g}\right)
\]

---

## 3. Important Correction

A target of **1.10 g resultant effective gravity** does **not** require only 0.10 g lateral acceleration. It requires approximately 0.458 g lateral acceleration because the lateral and vertical components combine vectorially.

| Target resultant effective gravity | Required lateral acceleration | Required lateral acceleration | Approximate resultant-vector angle |
|---:|---:|---:|---:|
| 1.05 g | 3.14 m/s² | 0.320 g | 17.8° |
| 1.10 g | 4.49 m/s² | 0.458 g | 24.6° |
| 1.20 g | 6.50 m/s² | 0.663 g | 33.6° |
| 1.25 g | 7.35 m/s² | 0.750 g | 36.9° |
| 1.50 g | 10.96 m/s² | 1.118 g | 48.2° |

This correction has major implications for operating speed, track design, comfort, land use, and feasibility.

---

## 4. Candidate Ring Sizes

| Radius | Circumference | Diameter | Approximate enclosed area |
|---:|---:|---:|---:|
| 100 m | 0.63 km | 200 m | 3.1 ha |
| 200 m | 1.26 km | 400 m | 12.6 ha |
| 400 m | 2.51 km | 800 m | 50.3 ha |
| 500 m | 3.14 km | 1.0 km | 78.5 ha |
| 1,000 m | 6.28 km | 2.0 km | 314 ha |
| 2,000 m | 12.57 km | 4.0 km | 1,257 ha |

Larger radii reduce angular rate but increase land use, guideway length, civil infrastructure, and likely cost.

---

## 5. Required Operating Speed

Using the vector-corrected model above:

| Radius | Speed for 1.10 g resultant | Speed for 1.25 g resultant |
|---:|---:|---:|
| 100 m | 76 km/h | 98 km/h |
| 200 m | 108 km/h | 138 km/h |
| 400 m | 153 km/h | 195 km/h |
| 500 m | 171 km/h | 218 km/h |
| 1,000 m | 241 km/h | 309 km/h |
| 2,000 m | 341 km/h | 437 km/h |

These values show why modest resultant gravity increases can still imply demanding operating speeds at large radius.

---

## 6. Approximate Lap Time and Angular Rate

| Radius | Lap time at 1.10 g | Angular rate at 1.10 g | Lap time at 1.25 g | Angular rate at 1.25 g |
|---:|---:|---:|---:|---:|
| 100 m | 30 s | 2.02 rpm | 23 s | 2.59 rpm |
| 200 m | 42 s | 1.43 rpm | 33 s | 1.83 rpm |
| 400 m | 59 s | 1.01 rpm | 46 s | 1.29 rpm |
| 500 m | 66 s | 0.91 rpm | 52 s | 1.16 rpm |
| 1,000 m | 94 s | 0.64 rpm | 73 s | 0.82 rpm |
| 2,000 m | 133 s | 0.45 rpm | 104 s | 0.58 rpm |

Angular rate is important for vestibular and Coriolis effects. A large radius can reduce angular-rate concerns but may require high speed and very large land area.

---

## 7. Interpretation for Railway and Maglev Concepts

A circular railway or maglev system must be evaluated against multiple coupled variables:

- resultant gravity target,
- lateral acceleration,
- banking or cabin tilt,
- radius,
- speed,
- angular rate,
- track or guideway length,
- ride quality,
- maintenance,
- emergency stopping distance,
- land use,
- cost.

No single radius is optimal without weighting these variables against scientific requirements.

---

## 8. Demonstrator Implications

The corrected sizing suggests that early demonstrators should not aim immediately for large human-habitat systems.

More credible early steps include:

1. small payload centrifuge or rotating platform,
2. instrumented circular payload cart,
3. low-speed guideway rig for acceleration and vibration measurement,
4. biological payload demonstrator at modest resultant gravity,
5. parameter study comparing rail, maglev, and rotating systems.

A human-rated railway or maglev habitat would require a much more demanding safety and operations case.

---

## 9. First-Order Cost Drivers

At this stage, cost should be treated parametrically rather than as a single headline number.

Main capital-cost drivers:

- guideway or track length,
- earthworks and site preparation,
- vehicle or payload module design,
- power supply,
- control and safety systems,
- laboratories and support buildings,
- environmental-control systems,
- emergency infrastructure,
- permitting and certification,
- commissioning and test programme.

Main operating-cost drivers:

- continuous operating hours,
- energy demand,
- maintenance and inspection,
- staffing,
- payload operations,
- medical or biological support,
- safety and emergency readiness,
- component replacement,
- data and facility management.

---

## 10. Preliminary Track-Length Cost Placeholder

The following placeholder uses a notional high-quality circular guideway or railway construction cost of 25 M€/km. This number is not a validated estimate and must be replaced with project-specific cost data.

| Radius | Circumference | Placeholder guideway cost |
|---:|---:|---:|
| 100 m | 0.63 km | 15.7 M€ |
| 200 m | 1.26 km | 31.4 M€ |
| 400 m | 2.51 km | 62.8 M€ |
| 500 m | 3.14 km | 78.5 M€ |
| 1,000 m | 6.28 km | 157.1 M€ |
| 2,000 m | 12.57 km | 314.2 M€ |

This table includes only guideway length. It excludes land, vehicles, buildings, laboratories, power, control, safety systems, contingency, and operations.

---

## 11. Architecture Trade-Offs

### Smaller Radius

Potential advantages:

- lower land use,
- shorter guideway,
- lower civil cost,
- easier demonstrator construction.

Potential disadvantages:

- higher angular rate,
- stronger vestibular effects,
- tighter curvature,
- higher wear for rail systems,
- stronger gravity gradients across payloads or humans.

### Larger Radius

Potential advantages:

- lower angular rate,
- reduced curvature effects,
- potentially better comfort,
- more plausible habitat-scale layout.

Potential disadvantages:

- much higher land use,
- longer guideway,
- higher required speed for the same lateral acceleration,
- higher capital cost,
- more difficult emergency and operations concept.

---

## 12. Required Next Calculations

This document should be followed by reproducible calculations for:

- emergency stopping distance,
- propulsion power,
- aerodynamic drag,
- rolling resistance or maglev power demand,
- vibration assumptions,
- ride-quality limits,
- banking geometry,
- gravity gradients,
- payload-environment variability,
- land-use constraints,
- energy and operational cost.

All future calculations should state equations, units, assumptions, and uncertainty.

---

## 13. Open Questions

1. What target resultant gravity is scientifically meaningful?
2. What lateral acceleration is tolerable for each experiment class?
3. What angular rate is acceptable for biological payloads, plants, animals, and humans?
4. What radius minimizes total scientific, safety, and cost risk?
5. Can a small-radius demonstrator answer enough questions before larger infrastructure is considered?
6. What vibration and acceleration noise levels are acceptable?
7. How should banking or cabin orientation be implemented?
8. At what point does maglev become preferable to conventional rail?

---

## 14. Preliminary Conclusion

The corrected vector model shows that even modest resultant hypergravity levels may require substantial lateral acceleration. This strengthens the case for staged demonstrators, careful modelling, and architecture-neutral trade studies before any large facility is proposed.

The most immediate engineering output should be a reproducible parameter model that allows reviewers to vary target gravity, radius, speed, angular rate, bank angle, land use, and cost assumptions.