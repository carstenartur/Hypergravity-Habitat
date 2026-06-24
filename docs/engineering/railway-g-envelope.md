# Railway g-Envelope

**Project:** Hypergravity Habitat  
**Document type:** engineering screening envelope  
**Status:** working document for railway feasibility  
**Scope:** achievable resultant effective-g corridor under track cant, cant deficiency, carbody tilt, and internal floor alignment constraints

---

## 1. Purpose

This document defines a first-order **railway g-envelope** for rail-based Hypergravity Habitat concepts. It asks whether there is a technical corridor of achievable g-values once track cant, cant deficiency, carbody tilt, wheel unloading, floor angle, and low-speed or stopped conditions are considered.

The answer is yes: there is an envelope. But for conventional railway practice it is likely a **narrow low-g envelope**, unless the system departs strongly from standard railway assumptions.

This document is a screening tool, not a certification analysis.

---

## 2. Basic Idea

For a terrestrial circular platform:

```text
g_eff = √(g² + a_c²)
θ = arctan(a_c / g)
```

where:

- `g_eff` is resultant effective gravity,
- `g` is Earth gravity,
- `a_c` is lateral centripetal acceleration,
- `θ` is the resultant-vector angle relative to vertical.

For railway concepts, this target angle must be compared with what the track and vehicle can safely provide.

---

## 3. Railway-Equivalent Cant Model

A simple screening approximation for standard-gauge railway is:

```text
a_c / g ≈ (h_cant + h_def) / G_track
```

where:

- `h_cant` is track cant,
- `h_def` is cant deficiency,
- `G_track` is track gauge, approximately 1.435 m for standard gauge.

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

The required equivalent cant-plus-deficiency for target resultant effective gravity is approximately:

```text
h_cant + h_def ≈ G_track × √(g_rel² − 1)
```

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

A conservative conventional rail corridor appears to sit close to approximately 1.01–1.03 g resultant under standard-like cant and cant-deficiency assumptions. Higher values may be possible only with aggressive assumptions, special approval, or a system that becomes less like conventional rail and more like a custom guided, banked, or internally gimballed research system.

Possible approaches include extreme dedicated cant, special low-speed/stopped support concepts, internal tilting or gimballed cabins, nonstandard bogies and suspension, guideway capture, maglev, or payload-only operation.

---

## 8. Low-Speed and Stopped Condition

A high-cant circular railway has a major low-speed problem. If the train slows down or stops on a strongly banked track, the lateral centripetal acceleration disappears but the track remains tilted.

This creates inward/downhill load shift, cant excess, boarding and evacuation problems, maintenance difficulty, possible payload orientation problems, and emergency-response complications.

Therefore, a high-g railway concept needs a credible low-speed and stopped-state concept before it can be considered serious.

---

## 9. Practical Design Corridor

| Corridor | Approximate g-range | Interpretation |
|---|---:|---|
| conventional rail comfort/safety corridor | about 1.00–1.03 g | plausible for early rail discussion, still needs expert review |
| aggressive rail / special approval corridor | about 1.03–1.06 g | may require nonstandard cant, higher cant deficiency, and strong safety case |
| high hypergravity railway corridor | above 1.06 g | likely not conventional rail; requires custom guideway, internal tilt, or alternative architecture |
| 1.10 g and above | 1.10 g+ | far outside ordinary railway cant/tilt logic; probably pushes toward maglev, rotating, or specialized guided system |

These ranges are not final limits. They are a first-order feasibility map.

---

## 10. Screening Takeaway: Standard Rail, Special Rail, and Non-Standard Systems

A railway-based Hypergravity Habitat should be understood as a candidate for **very mild resultant hypergravity** unless the system departs substantially from conventional railway assumptions.

As a first-order screening interpretation:

| Concept class | Approximate resultant effective-g range | Interpretation |
|---|---:|---|
| Conventional railway logic | about 1.01–1.03 g | plausible order of magnitude under standard-like cant and cant-deficiency assumptions; still requires expert review |
| Special railway assumptions / tilting vehicle / aggressive approval envelope | about 1.03–1.04 g, possibly approaching 1.05 g in optimistic special cases | no longer a simple standard-train claim; requires explicit analysis of cant, cant deficiency, wheel unloading, comfort, clearance, stopped-state behaviour, and safety |
| Dedicated guided or internally tilted system | above about 1.05–1.06 g | likely leaves ordinary railway practice and becomes a specialized guideway, captured vehicle, gimballed cabin, maglev, or rotating-system problem |
| Clear hypergravity target | 1.10 g and above | should be treated as outside normal railway cant/tilt logic unless a new system architecture is proposed |

This table is not a certified railway limit. It is a screening guide for early feasibility discussion.

The key point is that small lateral accelerations produce only small increases in **resultant** effective gravity. For example, 0.20 g lateral acceleration gives:

```text
g_eff = √(1² + 0.20²) ≈ 1.020 g
```

That is only about a 2% increase in resultant effective gravity.

Tilting technology may help align the cabin with the perceived load vector, but it does not remove the underlying wheel-rail or guideway force limits. Track forces, wheel unloading, derailment safety, stopped and low-speed conditions, emergency braking, clearance, maintenance, and certification remain limiting factors.

Therefore, conventional railway concepts are useful as a benchmark and may be relevant for very mild hypergravity or payload demonstrators. However, many of the scientifically interesting questions — especially higher-g exposure, large controlled payload environments, human habitability, transfer systems, and sport/projectile compatibility — may require leaving the space of standard railway solutions.

---

## 11. Required Next Analysis

Before a rail concept claims any target g value, it needs cant and cant-deficiency calculation, wheel-unloading estimate, derailment-risk and vehicle dynamics model, carbody tilt and internal floor alignment model, stopped and low-speed analysis, emergency braking analysis, clearance analysis, ride-quality and vibration analysis, and expert review by railway dynamics specialists.

---

## 12. Calculation Tool

A first-order screening calculator has been added:

```bash
python calculations/railway_g_envelope.py
```

It prints example envelope cases and target-g requirements. The tool is intentionally simple and is designed to expose orders of magnitude.

---

## 13. Preliminary Conclusion

Yes, a g-envelope exists. It is the intersection of physics, railway geometry, track cant, cant deficiency, vehicle tilt, wheel unloading, speed, low-speed operation, and safety constraints.

The preliminary conclusion is that conventional railway technology may be relevant for **very mild hypergravity** or for payload/engineering demonstrators, but target values like **1.10 g resultant effective gravity** are probably outside ordinary railway practice unless the system becomes a highly specialized guideway or internally tilted research platform.

---

## 14. Source Anchors

- 49 CFR 213.329 — Curves; elevation and speed limitations. Used as an example of regulatory structure for maximum outside rail elevation, cant deficiency qualification, wheel unloading, carbody roll, and lateral acceleration criteria.
- `docs/physics-reference.md` — equations for resultant effective gravity and floor angle.
- `docs/engineering/tilting-train-and-cant-limits.md` — qualitative engineering discussion of tilting trains and cant limits.
- `calculations/railway_g_envelope.py` — reproducible screening calculations.

---

<!-- project-footer -->
**Project:** [Hypergravity Habitat](../../README.md) · **Status:** exploratory research documentation · **License:** see repository license and file-level notes
