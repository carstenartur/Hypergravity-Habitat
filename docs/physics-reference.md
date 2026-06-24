# Physics Reference

**Project:** Hypergravity Habitat  
**Document type:** physics and notation reference  
**Status:** working reference  
**Scope:** effective gravity, circular motion, bank angle, angular rate, Coriolis effects, projectile deflection, gravity gradients, and scaling relationships

---

## 1. Purpose

This document collects the core physics used throughout the Hypergravity Habitat repository. It is intended to make assumptions transparent and prevent inconsistent calculations across documents.

The reference is first-order. It is suitable for concept screening and requirements discussion, not for detailed engineering, safety certification, or human-subject protocol approval.

---

## 2. Readability Rule

Reader-facing documents should avoid raw equation markup. Formulas should be written in readable plain text or Unicode notation and explained immediately.

Example:

```text
g_eff = √(g² + a_c²)
```

Meaning: the resultant effective gravity is the vector combination of Earth gravity and generated centripetal acceleration.

---

## 3. Notation

| Symbol | Meaning | Unit |
|---|---|---|
| g | Earth-normal gravitational acceleration | m/s² |
| g_eff | resultant effective gravity | m/s² |
| g_rel | resultant effective gravity relative to 1 g | dimensionless |
| a_c | centripetal acceleration | m/s² |
| v | tangential speed | m/s |
| r | radius | m |
| ω or Ω | angular velocity | rad/s |
| T | time or flight time, depending on context | s |
| L | distance or circumference, depending on context | m |
| θ | bank angle or resultant-vector angle | degrees or radians |
| y | lateral projectile deflection | m |

Use `ω` for platform angular velocity in general calculations and `Ω` when emphasizing rotating-frame effects such as Coriolis acceleration.

---

## 4. Circular Motion

Centripetal acceleration:

```text
a_c = v² / r = ω² r
```

Tangential speed:

```text
v = √(a_c r)
```

Angular velocity:

```text
ω = v / r = √(a_c / r)
```

Rotations per minute:

```text
rpm = (ω / 2π) × 60
```

Circumference:

```text
L = 2πr
```

Lap time:

```text
T_lap = 2πr / v
```

---

## 5. Resultant Effective Gravity on Earth

For a terrestrial circular platform, Earth gravity acts vertically and centripetal acceleration acts horizontally. The resultant effective gravity magnitude is:

```text
g_eff = √(g² + a_c²)
```

If the target resultant gravity is expressed as a multiple of Earth gravity:

```text
g_eff = g_rel × g
```

then the required lateral acceleration is:

```text
a_c = g × √(g_rel² − 1)
```

This equation is central. A target of 1.10 g resultant effective gravity does **not** require only 0.10 g lateral acceleration. It requires approximately 0.458 g lateral acceleration.

---

## 6. Bank Angle or Floor Alignment

The resultant load vector is tilted relative to vertical by:

```text
θ = arctan(a_c / g)
```

If a platform floor is aligned with the resultant vector, this is the approximate required floor or vehicle bank angle.

| Target resultant gravity | Lateral acceleration | Bank angle |
|---:|---:|---:|
| 1.05 g | 0.320 g | 17.8° |
| 1.10 g | 0.458 g | 24.6° |
| 1.20 g | 0.663 g | 33.6° |
| 1.25 g | 0.750 g | 36.9° |
| 1.50 g | 1.118 g | 48.2° |

---

## 7. Radius, Speed, and Angular-Rate Trade-Off

For fixed target resultant gravity, `a_c` is fixed. Therefore:

```text
v is proportional to √r
ω is proportional to 1 / √r
```

Increasing radius reduces angular rate and Coriolis effects, but increases circumference, land use, guideway length, and likely cost. It also increases required speed for the same lateral acceleration.

---

## 8. Gravity Gradients

In rotating systems, effective acceleration can vary with radius:

```text
a_c(r) = ω²r
```

For small radial height or payload dimension `Δr`:

```text
Δa_c ≈ ω² × Δr
```

Gravity gradients matter for:

- human body height,
- plant growth chambers,
- cell-culture racks,
- fluid systems,
- large payloads,
- rotating platforms with small radius.

Large radii reduce relative gradients across a given payload size.

---

## 9. Coriolis Acceleration

In a rotating frame, a moving object experiences Coriolis acceleration.

Vector form:

```text
a_cor_vector = −2 Ω × v_rel
```

Magnitude:

```text
a_cor = 2 Ω v_rel sin(φ)
```

where `φ` is the angle between the rotation vector and the relative velocity vector.

For worst-case screening:

```text
a_cor ≈ 2 Ω v_rel
```

Coriolis effects are relevant for:

- head movements,
- walking and turning,
- throwing and kicking,
- free projectiles,
- fluid systems,
- moving samples or equipment.

---

## 10. Projectile Deflection Screening

For a projectile moving over distance `L` with speed `v`, approximate flight time is:

```text
T ≈ L / v
```

First-order lateral deflection:

```text
y ≈ Ω v T²
```

or:

```text
y ≈ Ω × L² / v
```

This is a simplified screening model. It does not include drag, spin, Magnus effect, launch angle, target height, release height, curved cabin geometry, direction relative to platform rotation, or athlete compensation.

Use `calculations/coriolis_projectile_deflection.py` for first-order estimates.

---

## 11. Stopping Distance

For a platform moving at speed `v` and decelerating at `a_b`:

```text
s = v² / (2a_b)
t = v / a_b
```

This matters for emergency stop, safe evacuation, passenger comfort, payload integrity, braking heat, and energy recovery.

---

## 12. Kinetic Energy

Vehicle or rotating-platform kinetic energy:

```text
E_k = 0.5 × m × v²
```

Large moving systems store substantial kinetic energy. This affects emergency braking, containment, collision risk, power recovery, and safety-case requirements.

---

## 13. Power and Energy Placeholders

First-order propulsion power depends on losses such as rolling resistance, aerodynamic drag, bearing losses, guideway losses, levitation or control power, HVAC, and laboratory loads.

Aerodynamic drag force:

```text
F_d = 0.5 × ρ × C_d × A × v²
```

Drag power:

```text
P_d = F_d × v = 0.5 × ρ × C_d × A × v³
```

This shows why high speeds can strongly affect operating cost.

---

## 14. Calculation Tools

Current scripts:

- `calculations/hypergravity_sizing.py`
- `calculations/coriolis_projectile_deflection.py`
- `calculations/railway_g_envelope.py`

These scripts should be treated as concept tools.

---

## 15. Common Calculation Errors to Avoid

1. Treating 1.10 g as 1 g plus 0.10 g lateral acceleration.
2. Ignoring bank angle.
3. Ignoring angular rate when discussing human comfort.
4. Ignoring Coriolis effects for projectiles and moving humans.
5. Ignoring vibration as a biological confounder.
6. Using speed tables without stating target resultant gravity.
7. Comparing rail, maglev, and rotating systems without common assumptions.

---

## 16. Preliminary Conclusion

The basic physics of a hypergravity platform are simple, but their design consequences are severe. Small increases in resultant effective gravity can imply substantial lateral acceleration, banking, speed, angular-rate, and safety constraints.

All future documents should link back to this reference or to reproducible calculation scripts when presenting numerical claims.

---

<!-- project-footer -->
**Project:** [Hypergravity Habitat](../README.md) · **Status:** exploratory research documentation · **License:** see repository license and file-level notes
