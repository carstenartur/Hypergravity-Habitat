# Coriolis Effects, Projectile Accuracy, and Sport-Skill Maintenance

**Project:** Hypergravity Habitat  
**Document type:** theoretical modelling note  
**Status:** first-order concept note  
**Scope:** handball throws, football passes/shots, target accuracy, skill maintenance, human factors, and radius requirements in rotating/circular hypergravity environments

---

## 1. Purpose

This note evaluates how Coriolis effects could limit **sport-specific accuracy training** inside a circular or rotating Hypergravity Habitat.

The purpose is not to propose Coriolis force as a training stimulus. The relevant scenario is different:

> An athlete may use the station primarily for muscle-building or load-adaptation training, but still need to maintain sport-specific precision skills during the same training block.

For sports such as handball, football, basketball, tennis, volleyball, baseball, hockey, or racket sports, skill maintenance often requires repeated target-directed movements. If the platform radius is too small, projectile trajectories may deviate enough that normal accuracy practice becomes non-Earth-like.

This makes Coriolis not a desired training effect, but a **compatibility constraint**.

---

## 2. Core Scenario

A practical example:

- A handball player enters a hypergravity training programme to increase leg and trunk loading.
- The programme lasts several weeks.
- During that period the athlete cannot simply stop throwing practice, because throwing accuracy, timing, perception-action coupling, and tactical routines may deteriorate.
- If throws inside the habitat curve strongly relative to Earth-normal expectations, the athlete may either train the wrong skill or need special compensation.

The equivalent football scenario is:

- A player may tolerate hypergravity strength and conditioning work.
- But long passes, shots, crosses, and target kicks require predictable ball flight.
- Strong Coriolis deviation could make normal technical training impossible unless the radius is large enough or the training is redesigned.

---

## 3. First-Order Physics

For a projectile moving relative to a rotating frame, the Coriolis acceleration magnitude is approximately:

```text
a_cor = 2 Ω v
```

where:

- `a_cor` is Coriolis acceleration,
- `Ω` is the platform angular rate,
- `v` is projectile speed relative to the platform.

For a simple horizontal projectile over range `L`, with approximate flight time:

```text
T ≈ L / v
```

The first-order lateral deflection is:

```text
y ≈ Ω v T²
```

or:

```text
y ≈ Ω × L² / v
```

This is a screening model. It estimates order of magnitude only.

---

## 4. Relationship to Platform Radius

For a terrestrial circular platform, the required centripetal acceleration for a target resultant gravity is:

```text
a_c = g × √(g_rel² − 1)
```

The angular rate is:

```text
Ω = √(a_c / r)
```

Therefore, for a fixed target resultant gravity, larger radius lowers angular rate and reduces Coriolis deflection.

This is why projectile accuracy can impose a stronger radius requirement than muscle-building exercises.

---

## 5. Example: 1.10 g Resultant Effective Gravity

For a 1.10 g resultant effective-gravity target on Earth, the required lateral acceleration is approximately:

```text
a_c ≈ 0.458 g
```

At radius `r = 500 m`:

```text
Ω ≈ 0.095 rad/s ≈ 0.91 rpm
```

### 20 m handball-style throw

Assume a range of 20 m and projectile speed of 20 m/s:

```text
y ≈ 0.095 × 20² / 20 ≈ 1.9 m
```

### 30 m football-style pass or shot

Assume a range of 30 m and projectile speed of 25 m/s:

```text
y ≈ 0.095 × 30² / 25 ≈ 3.4 m
```

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

This table shows that Earth-like projectile accuracy can become a much stricter design driver than muscle loading.

---

## 7. Interpretation for Muscle-Building Programmes

A facility used for hypertrophy, resistance training, cycling, treadmill work, or controlled load adaptation may be technically useful at radii that are too small for normal ball-sport accuracy.

That creates a programme-design problem:

> The station may be adequate for muscle-building, but inadequate for maintaining sport-specific precision skills during the same residency.

This distinction matters for athletes. A training intervention that improves strength but disrupts timing, throwing accuracy, kicking accuracy, or decision-action coupling may be unattractive for elite sport.

| Training component | Coriolis sensitivity | Facility implication |
|---|---:|---|
| Squats, resistance machines | low | smaller radii may be acceptable |
| Cycling / treadmill | low-medium | angular rate and vestibular comfort matter |
| Jumping and landing | medium | movement control and vestibular effects matter |
| Short technical drills | medium | possible with reduced distances and instrumentation |
| Handball throwing accuracy | high | radius or special compensation becomes important |
| Football passing/shooting accuracy | high | radius or separate skill-maintenance solution required |
| Elite precision maintenance | very high | Earth-like practice may require very low angular rate |

---

## 8. Possible Design Responses

If athletes must maintain precision training during a hypergravity residency, possible responses include larger radius, short-distance technical drills, orientation-specific training zones, instrumented targets, adaptive visual feedback, separate non-rotating 1 g skill-training areas, scheduled return-to-1 g skill sessions, virtual or augmented-reality skill maintenance, or classification of ball drills as sensorimotor adaptation research.

Each option has consequences for the scientific protocol and facility design.

---

## 9. Skill Maintenance versus Sensorimotor Adaptation

The project should distinguish two different purposes.

### Skill maintenance

The athlete wants to preserve Earth-normal sport skill during a hypergravity block. Trajectories should remain close enough to Earth-normal conditions that the athlete does not learn maladaptive compensations.

### Sensorimotor adaptation research

The researcher intentionally studies how athletes adapt to altered projectile trajectories. Trajectories may differ from Earth-normal conditions, but the difference must be measured and controlled.

These are different use cases. A facility can be useful for one while failing the other.

---

## 10. Research Use Cases

Projectile tasks could be useful for estimating functional Coriolis thresholds, defining radius requirements for sport-skill compatibility, measuring motor adaptation in rotating environments, comparing short-radius and large-radius concepts, determining whether sport-specific skill maintenance is possible during hypertrophy-focused residency, and evaluating transfer after return to 1 g.

---

## 11. Limitations of the Simple Model

The first-order model does not include aerodynamic drag, ball spin, Magnus effect, launch angle, release height, target height, curved cabin geometry, floor banking, player motion before release, orientation of the throw relative to the rotation axis, air motion inside the cabin, athlete learning, tactical perception, or decision timing.

A full model should simulate 3D projectile motion in the rotating frame and include ball-specific aerodynamics.

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

Coriolis force should be treated as a **skill-maintenance constraint** for sport-specific training during hypergravity residency.

For muscle-building and controlled exercise, smaller radii may be acceptable. For athletes who must continue handball, football, or other precision projectile practice during the same training block, much larger radii or separate skill-maintenance solutions may be required.

This makes projectile accuracy an important part of the sports-science, human-factors, and engineering requirements roadmap.

---

<!-- project-footer -->
**Project:** [Hypergravity Habitat](../../README.md) · **Status:** exploratory research documentation · **License:** see repository license and file-level notes
