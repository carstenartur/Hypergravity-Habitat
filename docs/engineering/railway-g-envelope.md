# Railway g-Envelope

**Project:** Hypergravity Habitat  
**Document type:** engineering screening envelope  
**Status:** working document for railway feasibility  
**Scope:** achievable resultant effective-g corridor under track cant, cant deficiency, carbody tilt, and internal floor alignment constraints

---

## 1. Purpose

This document defines a first-order **railway g-envelope** for rail-based Hypergravity Habitat concepts. It answers the question:

> Is there a technical corridor of achievable g-values once railway limits such as track cant, cant deficiency, carbody tilt, wheel unloading, floor angle, and low-speed/stopped conditions are considered?

The answer is yes: there is an envelope. But for conventional railway practice it is likely a **narrow low-g envelope**, unless the system departs strongly from standard railway assumptions.

This document is a screening tool, not a certification analysis.

---

## 2. Basic Idea

For a terrestrial circular platform:

\[
g_{eff} = \sqrt{g^2 + a_c^2}
\]

and:

\[
\theta = \arctan(a_c/g)
\]

where:

- \(g_{eff}\) is resultant effective gravity,
- \(g\) is Earth gravity,
- \(a_c\) is lateral centripetal acceleration,
- \(\theta\) is the resultant-vector angle relative to vertical.

For railway concepts, this target angle must be compared with what the track and vehicle can safely provide.

---

## 3. Railway-Equivalent Cant Model

A simple screening approximation for standard-gauge railway is:

\[
\frac{a_c}{g} \approx \frac{h_{cant} + h_{def}}{G_{track}}
\]

where:

- \(h_{cant}\) is track cant,
- \(h_{def}\) is cant deficiency,
- \(G_{track}\) is track gauge, approximately 1.435 m for standard gauge.

This approximation is useful because it shows how much lateral acceleration a conventional rail geometry can balance or tolerate.

---

## 4. Why Carbody Tilt Is Not Enough

Carbody tilt helps align the cabin with the perceived load vector, but it does not remove the wheel-rail force problem.

Therefore, two envelopes must be separated:

1. **Track-force envelope** — governed by track cant, cant deficiency, wheel unloading, derailment risk, and standards.
2. **Cabin-alignment envelope** — governed by track cant, carbody tilt, possible internal floor tilt, clearance, doors, utilities, and passenger/payload usability.

A tilting train can improve cabin comfort while the bogies and rails still experience the underlying lateral-force condition.

---

## 5. Example Envelope Values

Using a 1.435 m standard gauge and simple cant-equivalent screening:

| Case | Cant | Cant deficiency | Track-equivalent lateral g | Track-equivalent resultant g | Track angle |
|---|---:|---:|---:|---:|---:|
| 7 in cant + 3 in deficiency | 178 mm | 76 mm | 0.177 g | 1.016 g | 10.0° |
| 7 in cant + 5 in deficiency | 178 mm | 127 mm | 0.213 g | 1.022 g | 12.0° |
| 180 mm cant + 150 mm deficiency | 180 mm | 150 mm | 0.230 g | 1.026 g | 13.0° |
| 180 mm cant + 200 mm deficiency | 180 mm | 200 mm | 0.265 g | 1.034 g | 14.8° |
| 300 mm cant + 200 mm deficiency | 300 mm | 200 mm | 0.348 g | 1.059 g | 19.2° |

These are not recommended design values. They are order-of-magnitude screening cases.

---

## 6. Target-g Requirements

The required equivalent cant-plus-deficiency for target resultant effective gravity is:

\[
(h_{cant}+h_{def}) \approx G_{track}\sqrt{g_{rel}^2 - 1}
\]

For standard gauge:

| Target resultant effective gravity | Required lateral g | Required angle | Equivalent cant + deficiency |
|---:|---:|---:|---:|
| 1.020 g | 0.201 g | 11.4° | 288 mm |
| 1.035 g | 0.267 g | 14.9° | 383 mm |
| 1.050 g | 0.320 g | 17.8° | 459 mm |
| 1.100 g | 0.458 g | 24.6° | 658 mm |
| 1.200 g | 0.663 g | 33.6° | 952 mm |
| 1.250 g | 0.750 g | 36.9° | 1076 mm |

This table shows why railway-based hypergravity above approximately 1.03–1.05 g becomes difficult under conventional railway assumptions.

---

## 7. Interpretation

### Conventional railway corridor

A conservative conventional rail corridor appears to sit close to:

- approximately **1.01–1.03 g resultant** under standard-like cant and cant-deficiency assumptions,
- potentially somewhat higher only with aggressive assumptions and special approval,
- still far below 1.10 g unless track and vehicle design become highly nonstandard.

### Special railway or guided-system corridor

Higher values may be physically possible only if the system becomes less like a conventional railway and more like a custom guided, banked, or internally gimballed research system.

Possible approaches:

- extreme dedicated cant,
- special low-speed/stopped support concept,
- internal tilting or gimballed cabin,
- nonstandard bogies and suspension,
- guideway rather than conventional rail,
- maglev or roller-coaster-like support geometry,
- payload-only rather than human-rated operation.

---

## 8. Low-Speed and Stopped Condition

A high-cant circular railway has a major low-speed problem.

If the train slows down or stops on a strongly banked track, the lateral centripetal acceleration disappears but the track remains tilted. This creates:

- inward/downhill load shift,
- cant excess,
- boarding and evacuation problems,
- maintenance difficulty,
- possible payload orientation problems,
- emergency-response complications.

Therefore, a high-g railway concept needs a credible low-speed and stopped-state concept before it can be considered serious.

---

## 9. Practical Design Corridor

A useful screening corridor can be described as:

| Corridor | Approximate g-range | Interpretation |
|---|---:|---|
| conventional rail comfort/safety corridor | about 1.00–1.03 g | plausible for early rail discussion, still needs expert review |
| aggressive rail / special approval corridor | about 1.03–1.06 g | may require nonstandard cant, higher cant deficiency, and strong safety case |
| high hypergravity railway corridor | above 1.06 g | likely not conventional rail; requires custom guideway, internal tilt, or alternative architecture |
| 1.10 g and above | 1.10 g+ | far outside ordinary railway cant/tilt logic; probably pushes toward maglev, rotating, or specialized guided system |

These ranges are not final limits. They are a first-order feasibility map.

---

## 10. Required Next Analysis

Before a rail concept claims any target g value, it needs:

1. cant and cant-deficiency calculation,
2. wheel unloading estimate,
3. derailment-risk and vehicle dynamics model,
4. carbody tilt and internal floor alignment model,
5. stopped and low-speed analysis,
6. emergency braking analysis,
7. clearance and loading-gauge analysis,
8. ride-quality and vibration analysis,
9. expert review by railway dynamics specialists.

---

## 11. Calculation Tool

A first-order screening calculator has been added:

```bash
python calculations/railway_g_envelope.py
```

It prints example envelope cases and target-g requirements.

The tool is intentionally simple. It is designed to expose orders of magnitude and identify when target values are far outside conventional rail assumptions.

---

## 12. Preliminary Conclusion

Yes, a g-envelope exists. It is the intersection of physics, railway geometry, track cant, cant deficiency, vehicle tilt, wheel unloading, speed, low-speed operation, and safety constraints.

The preliminary conclusion is that conventional railway technology may be relevant for **very mild hypergravity** or for payload/engineering demonstrators, but target values like **1.10 g resultant effective gravity** are probably outside ordinary railway practice unless the system becomes a highly specialized guideway or internally tilted research platform.

This makes the railway concept still worth evaluating, but it also strengthens the case for comparing rail with maglev, rotating platforms, and payload-first demonstrators.

---

## 13. Source Anchors

- 49 CFR 213.329 — Curves; elevation and speed limitations. Used as an example of regulatory structure for maximum outside rail elevation, cant deficiency qualification, wheel unloading, carbody roll, and lateral acceleration criteria.
- `docs/physics-reference.md` — equations for resultant effective gravity and floor angle.
- `docs/engineering/tilting-train-and-cant-limits.md` — qualitative engineering discussion of tilting trains and cant limits.
- `calculations/railway_g_envelope.py` — reproducible screening calculations.