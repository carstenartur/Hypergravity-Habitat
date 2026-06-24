# Physics Reference

**Project:** Hypergravity Habitat  
**Document type:** physics and notation reference  
**Status:** working reference  
**Scope:** effective gravity, circular motion, bank angle, angular rate, Coriolis effects, projectile deflection, gravity gradients, and scaling relationships

---

## 1. Purpose

This document collects the core physics used throughout the Hypergravity Habitat repository. It is intended to make assumptions transparent and prevent inconsistent calculations across documents.

The reference is first-order. It is suitable for concept screening and requirements discussion, not for detailed engineering or safety certification.

---

## 2. Notation

| Symbol | Meaning | Unit |
|---|---|---|
| \(g\) | Earth-normal gravitational acceleration | m/s² |
| \(g_{eff}\) | resultant effective gravity | m/s² |
| \(g_{rel}\) | resultant effective gravity relative to 1 g | dimensionless |
| \(a_c\) | centripetal acceleration | m/s² |
| \(v\) | tangential speed | m/s |
| \(r\) | radius | m |
| \(\omega\), \(\Omega\) | angular velocity | rad/s |
| \(T\) | time or flight time depending on context | s |
| \(L\) | distance or circumference depending on context | m |
| \(\theta\) | bank angle / resultant-vector angle | degrees or radians |
| \(y\) | lateral projectile deflection | m |

Use \(\omega\) for platform angular velocity in general calculations and \(\Omega\) when emphasizing rotating-frame effects such as Coriolis acceleration.

---

## 3. Circular Motion

Centripetal acceleration is:

\[
a_c = \frac{v^2}{r} = \omega^2 r
\]

Tangential speed is:

\[
v = \sqrt{a_c r}
\]

Angular velocity is:

\[
\omega = \frac{v}{r} = \sqrt{\frac{a_c}{r}}
\]

Rotations per minute:

\[
rpm = \frac{\omega}{2\pi} \cdot 60
\]

Circumference:

\[
L = 2\pi r
\]

Lap time:

\[
T_{lap} = \frac{2\pi r}{v}
\]

---

## 4. Resultant Effective Gravity on Earth

For a terrestrial circular platform, Earth gravity acts vertically and centripetal acceleration acts horizontally. The resultant effective gravity magnitude is:

\[
g_{eff} = \sqrt{g^2 + a_c^2}
\]

If the target resultant gravity is expressed as a multiple of Earth gravity:

\[
g_{eff} = g_{rel}g
\]

then the required lateral acceleration is:

\[
a_c = g\sqrt{g_{rel}^2 - 1}
\]

This equation is central. A target of 1.10 g resultant effective gravity does **not** require only 0.10 g lateral acceleration. It requires approximately 0.458 g lateral acceleration.

---

## 5. Bank Angle or Floor Alignment

The resultant load vector is tilted relative to vertical by:

\[
\theta = \arctan\left(\frac{a_c}{g}\right)
\]

If a platform floor is aligned with the resultant vector, this is the approximate required floor or vehicle bank angle.

Examples:

| Target resultant gravity | Lateral acceleration | Bank angle |
|---:|---:|---:|
| 1.05 g | 0.320 g | 17.8° |
| 1.10 g | 0.458 g | 24.6° |
| 1.20 g | 0.663 g | 33.6° |
| 1.25 g | 0.750 g | 36.9° |
| 1.50 g | 1.118 g | 48.2° |

---

## 6. Radius, Speed, and Angular Rate Trade-Off

For fixed target resultant gravity, \(a_c\) is fixed. Therefore:

\[
v \propto \sqrt{r}
\]

and:

\[
\omega \propto \frac{1}{\sqrt{r}}
\]

Increasing radius reduces angular rate and Coriolis effects, but increases circumference, land use, guideway length, and likely cost. It also increases required speed for the same lateral acceleration.

---

## 7. Gravity Gradients

In rotating systems, effective acceleration can vary with radius:

\[
a_c(r) = \omega^2 r
\]

For small radial height or payload dimension \(\Delta r\):

\[
\Delta a_c \approx \omega^2 \Delta r
\]

Gravity gradients matter for:

- human body height,
- plant growth chambers,
- cell culture racks,
- fluid systems,
- large payloads,
- rotating platforms with small radius.

Large radii reduce relative gradients across a given payload size.

---

## 8. Coriolis Acceleration

In a rotating frame, a moving object experiences Coriolis acceleration:

\[
\vec{a}_{cor} = -2\vec{\Omega} \times \vec{v}_{rel}
\]

Magnitude:

\[
a_{cor} = 2\Omega v_{rel}\sin\phi
\]

where \(\phi\) is the angle between the rotation vector and the relative velocity vector.

For worst-case screening:

\[
a_{cor} \approx 2\Omega v_{rel}
\]

Coriolis effects are relevant for:

- head movements,
- walking and turning,
- throwing and kicking,
- free projectiles,
- fluid systems,
- moving samples or equipment.

---

## 9. Projectile Deflection Screening

For a projectile moving over distance \(L\) with speed \(v\), approximate flight time:

\[
T \approx \frac{L}{v}
\]

First-order lateral deflection:

\[
y \approx \Omega v T^2
\]

or:

\[
y \approx \Omega \frac{L^2}{v}
\]

This is a simplified screening model. It does not include:

- drag,
- spin,
- Magnus effect,
- launch angle,
- target height,
- release height,
- curved cabin geometry,
- direction relative to platform rotation,
- athlete compensation.

Use `calculations/coriolis_projectile_deflection.py` for first-order estimates.

---

## 10. Stopping Distance

For a platform moving at speed \(v\) and decelerating at \(a_b\):

\[
s = \frac{v^2}{2a_b}
\]

Stopping time:

\[
t = \frac{v}{a_b}
\]

This matters for:

- emergency stop,
- safe evacuation,
- transfer systems,
- passenger comfort,
- payload integrity,
- braking heat and energy.

A future safety document should include stopping-distance tables for candidate speeds and deceleration limits.

---

## 11. Kinetic Energy

Vehicle or rotating-platform kinetic energy:

\[
E_k = \frac{1}{2}mv^2
\]

Large moving systems store substantial kinetic energy. This affects:

- emergency braking,
- containment,
- collision risk,
- power recovery,
- safety-case requirements.

---

## 12. Power and Energy Placeholders

First-order propulsion power depends on losses such as:

- rolling resistance,
- aerodynamic drag,
- bearing losses,
- guideway losses,
- levitation or control power,
- HVAC and laboratory loads.

Aerodynamic drag force can be approximated as:

\[
F_d = \frac{1}{2}\rho C_d A v^2
\]

Drag power:

\[
P_d = F_d v = \frac{1}{2}\rho C_d A v^3
\]

This shows why high speeds can strongly affect operating cost.

---

## 13. Calculation Tools

Current scripts:

- `calculations/hypergravity_sizing.py`
- `calculations/coriolis_projectile_deflection.py`

These scripts should be treated as concept tools. Future versions should include:

- stopping distance,
- aerodynamic drag,
- rolling resistance,
- energy use,
- gravity gradients,
- parameter plots,
- uncertainty ranges.

---

## 14. Common Calculation Errors to Avoid

1. Treating 1.10 g as 1 g plus 0.10 g lateral acceleration.
2. Ignoring bank angle.
3. Ignoring angular rate when discussing human comfort.
4. Ignoring Coriolis effects for projectiles and moving humans.
5. Ignoring vibration as a biological confounder.
6. Using speed tables without stating target resultant gravity.
7. Comparing rail, maglev, and rotating systems without common assumptions.

---

## 15. Preliminary Conclusion

The basic physics of a hypergravity platform are simple, but their design consequences are severe. Small increases in resultant effective gravity can imply substantial lateral acceleration, banking, speed, angular-rate, and safety constraints.

All future documents should link back to this reference or to reproducible calculation scripts when presenting numerical claims.