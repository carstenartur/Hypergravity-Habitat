# Coriolis Effects, Projectile Accuracy, and Sports-Science Use Cases

**Project:** Hypergravity Habitat  
**Document type:** theoretical modelling note  
**Status:** first-order concept note  
**Scope:** handball throws, football shots, ball-sport accuracy, human factors, and radius requirements in rotating/circular hypergravity environments

---

## 1. Purpose

This note evaluates whether throwing and kicking tasks could be used to estimate how Coriolis effects influence target accuracy in a circular or rotating Hypergravity Habitat.

The short answer is yes: projectile tasks are likely to be a sensitive way to estimate whether a platform radius is large enough for Earth-like sports and coordination training. They are much more sensitive to angular rate than stationary strength exercises.

This does not mean that ball sports should be a primary justification for the facility. It means that ball-skill tasks are useful as a theoretical human-factors test case.

---

## 2. Core Question

> Could handball throws, football passes, or target kicks be used to determine whether the radius of a hypergravity training facility is large enough for accurate, Earth-like sport-specific practice?

This is a valid research question because rotating-frame dynamics affect freely moving objects differently from people and equipment in contact with the platform.

---

## 3. First-Order Physics

For a projectile moving relative to a rotating frame, the Coriolis acceleration magnitude is approximately:

\[
a_{cor} = 2 \Omega v
\]

where:

- \(a_{cor}\) is Coriolis acceleration,
- \(\Omega\) is the platform angular rate,
- \(v\) is projectile speed relative to the platform.

For a simple horizontal projectile over range \(L\), with approximate flight time:

\[
T \approx \frac{L}{v}
\]

The first-order lateral deflection is:

\[
y \approx \Omega v T^2
\]

or:

\[
y \approx \Omega \frac{L^2}{v}
\]

This is a screening model. It estimates order of magnitude only.

---

## 4. Relationship to Platform Radius

For a terrestrial circular platform, the required centripetal acceleration for a target resultant gravity is:

\[
a_c = g \sqrt{g_{rel}^2 - 1}
\]

The angular rate is:

\[
\Omega = \sqrt{\frac{a_c}{r}}
\]

Therefore, for a fixed target resultant gravity, larger radius lowers angular rate and reduces Coriolis deflection.

---

## 5. Example: 1.10 g Resultant Effective Gravity

For a 1.10 g resultant effective-gravity target on Earth, the required lateral acceleration is approximately:

\[
a_c \approx 0.458g
\]

At radius \(r = 500m\):

\[
\Omega \approx 0.095 rad/s \approx 0.91 rpm
\]

### 20 m handball-style throw

Assume:

- range: 20 m,
- projectile speed: 20 m/s.

Then:

\[
y \approx 0.095 \cdot \frac{20^2}{20} \approx 1.9m
\]

### 30 m football-style pass or shot

Assume:

- range: 30 m,
- projectile speed: 25 m/s.

Then:

\[
y \approx 0.095 \cdot \frac{30^2}{25} \approx 3.4m
\]

These values are large enough to substantially affect target accuracy.

---

## 6. Approximate Radius Sensitivity

For a 20 m throw at 20 m/s under a 1.10 g resultant target:

| Allowed first-order deflection | Approximate radius required |
|---:|---:|
| 1.0 m | 1.8 km |
| 0.5 m | 7.2 km |
| 0.2 m | 45 km |
| 0.1 m | 180 km |
| 0.05 m | 719 km |

This table shows that Earth-like projectile accuracy is a much stricter design driver than basic strength training.

---

## 7. Interpretation for Muscle-Building Facilities

A facility designed mainly for muscle loading, resistance training, cycling, treadmill work, or controlled exercise may not require radii large enough for Earth-like ball sports.

However, a facility intended for sport-specific training involving free projectiles should be evaluated separately.

| Activity type | Coriolis sensitivity | Radius implication |
|---|---:|---|
| Squats, resistance machines | low | radius driven mainly by comfort and safety |
| Cycling / treadmill | low-medium | angular rate matters but projectile accuracy does not |
| Jumping and landing | medium | motion control and vestibular effects matter |
| Short passing drills | medium-high | short distances may be manageable |
| Handball shots | high | large radius or adaptation required |
| Football passes / shots | high | large radius or modified training required |
| Elite precision training | very high | likely requires very low angular rate |

---

## 8. Research Use Cases

Projectile tasks could be useful for:

1. estimating functional Coriolis thresholds,
2. measuring motor adaptation in rotating environments,
3. comparing short-radius and large-radius platform concepts,
4. defining whether a training facility supports Earth-like or non-Earth-like sport skills,
5. developing sensorimotor adaptation protocols,
6. evaluating transfer after return to 1 g.

---

## 9. Limitations of the Simple Model

The first-order model does not include:

- aerodynamic drag,
- ball spin,
- Magnus effect,
- launch angle,
- release height,
- target height,
- curved cabin geometry,
- floor banking,
- player motion before release,
- orientation of the throw relative to the rotation axis,
- air motion inside the cabin,
- learning and compensation by athletes.

A full model should simulate 3D projectile motion in the rotating frame and include ball-specific aerodynamics.

---

## 10. Practical Design Options

If projectile accuracy matters, possible design responses include:

- use much larger radius,
- restrict projectile tasks to short distances,
- orient tasks along directions that minimize relevant Coriolis components,
- use instrumented targets and train compensation rather than Earth-like accuracy,
- classify ball sports as adaptation research rather than normal training,
- separate muscle-building areas from sports-skill areas,
- use virtual or robotic targets instead of assuming normal sport geometry.

---

## 11. Implication for Documentation

The Hypergravity Habitat project should explicitly distinguish:

1. **muscle-loading use cases** — plausible at smaller radii,
2. **human movement use cases** — require vestibular and gait analysis,
3. **projectile-skill use cases** — require much stronger Coriolis modelling,
4. **elite sport claims** — premature without evidence.

---

## 12. Related Calculation Tool

A first-order calculator has been added:

```bash
python calculations/coriolis_projectile_deflection.py --target-g 1.10 --range 20 --speed 20
```

To estimate the radius needed for a target deflection:

```bash
python calculations/coriolis_projectile_deflection.py --target-g 1.10 --range 20 --speed 20 --allowed-deflection 0.5
```

---

## 13. Preliminary Conclusion

Projectile accuracy should be included as a theoretical design and human-factors question. It is especially useful for determining whether a proposed radius supports Earth-like sport-specific training.

For muscle-building and controlled exercise, smaller radii may be acceptable. For handball or football tasks with realistic target accuracy, much larger radii or non-Earth-like training assumptions may be required.

This makes Coriolis modelling an important part of the engineering and sports-science roadmap.