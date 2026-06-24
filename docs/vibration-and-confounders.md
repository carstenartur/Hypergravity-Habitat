# Vibration and Confounders

**Project:** Hypergravity Habitat  
**Document type:** confounder-control framework  
**Status:** working document for demonstrator and experimental design  
**Scope:** vibration, acceleration transients, environmental variables, fluid motion, handling, noise, electromagnetic effects, and experimental validity

---

## 1. Purpose

This document defines the major confounders that must be controlled or measured in Hypergravity Habitat experiments. It is especially important for biological payloads and later human studies.

The central question is:

> If an experiment shows a biological, physiological, or performance change, how do we know that the cause is effective gravity rather than vibration, temperature, fluid shear, handling, noise, stress, or another platform artefact?

Confounder control is central to scientific credibility.

---

## 2. Principle

The project should assume that every moving or rotating platform introduces confounders until proven otherwise.

A result should not be interpreted as a gravity effect unless major confounders are:

1. controlled,
2. measured,
3. matched in a control condition,
4. or explicitly discussed as limitations.

---

## 3. Main Confounder Categories

| Confounder | Affects | Why it matters |
|---|---|---|
| vibration | biology, instruments, humans | can alter cells, plants, comfort, measurements |
| acceleration transients | all payloads | start/stop events may dominate exposure |
| temperature | biology, humans, sensors | affects metabolism, comfort, sensor drift |
| humidity | plants, humans, equipment | affects growth, sleep, static, comfort |
| CO2 / air quality | plants, humans, animals | affects physiology and growth |
| light | plants, circadian rhythm | can dominate biological outcomes |
| fluid shear | cells, microbes | can mimic or obscure gravity effects |
| sedimentation | cells, microbes, particles | affects exposure and nutrient gradients |
| noise | humans, animals | stress and sleep confounder |
| electromagnetic fields | sensors, biology | especially relevant to maglev concepts |
| handling | biological samples | can create artefacts |
| confinement | humans, animals | stress and behaviour confounder |
| expectation/placebo | humans | performance and subjective outcomes |

---

## 4. Vibration

### Why Vibration Matters

Vibration can affect:

- cell morphology,
- plant growth,
- microbial growth,
- microscopy,
- sensor readings,
- human comfort,
- sleep,
- motion sickness,
- performance tests.

A railway, maglev, rotating rig, or guided cart may all generate vibration, but with different spectra and amplitudes.

### Required Measurements

At minimum:

- acceleration time series,
- frequency spectrum,
- sensor location,
- sampling rate,
- calibration record,
- platform operating state,
- payload mounting condition.

### Reporting

Report vibration alongside biological or human outcomes. Do not present results as gravity-only effects if vibration is unmeasured.

---

## 5. Acceleration Transients

Start, stop, braking, docking, transfer, and speed changes can introduce acceleration transients.

Required logging:

- event type,
- time,
- duration,
- peak acceleration,
- jerk,
- payload state,
- environmental state.

Transients may be especially important in intermittent exposure or scheduled-stop protocols.

---

## 6. Temperature and Humidity

Temperature and humidity can dominate biological and human outcomes.

Minimum requirements:

- continuous logging,
- sensor calibration,
- payload-level measurement where possible,
- matched control condition,
- alarm thresholds for real experiments.

Plant, cell, microbial, and animal studies require tighter environmental documentation than simple engineering tests.

---

## 7. Light and Photoperiod

For plant experiments and human circadian studies, light must be specified.

Record:

- light intensity,
- spectrum,
- photoperiod,
- spatial variation,
- heat from lighting,
- exposure interruptions,
- imaging light exposure.

Light gradients can produce effects stronger than moderate gravity changes.

---

## 8. Fluid Motion and Shear

Fluid systems are highly sensitive to motion.

Potential confounders:

- fluid shear,
- mixing,
- sedimentation,
- gas exchange,
- nutrient gradients,
- meniscus behaviour,
- vessel geometry,
- vibration-induced flow.

This is critical for:

- cell culture,
- microbial growth,
- biofilms,
- hydroponics,
- algae,
- plant irrigation.

A biological payload should include fluid-behaviour assessment before interpreting results.

---

## 9. Noise

Noise is mainly a human and animal confounder, but it can also affect equipment.

Record:

- sound level,
- frequency characteristics if relevant,
- time pattern,
- relation to platform operation,
- sleep period exposure.

For human studies, noise can affect sleep, stress, performance, and mood.

---

## 10. Electromagnetic Effects

Maglev and high-power systems may introduce electromagnetic fields.

Potential effects:

- sensor interference,
- data corruption,
- heating,
- instrumentation noise,
- possible biological confounding in sensitive experiments.

A maglev concept should include electromagnetic compatibility measurements.

---

## 11. Handling and Transfer Effects

Sample handling can create artefacts.

Examples:

- temperature excursion during transfer,
- light exposure,
- mechanical shock,
- contamination,
- delayed fixation,
- inconsistent timing,
- operator differences.

Every handling event should be logged.

---

## 12. Human Confounders

Human studies introduce additional confounders:

- sleep schedule,
- diet,
- exercise volume,
- hydration,
- psychological stress,
- novelty effects,
- participant expectation,
- social dynamics,
- motivation,
- learning effects,
- caffeine, medication, or supplements.

These variables must be controlled or measured in any human protocol.

---

## 13. Control Strategies

Possible strategies:

1. matched 1 g controls,
2. vibration-matched controls,
3. sham exposure,
4. environmental control chambers,
5. baseline and recovery periods,
6. blinded analysis where possible,
7. repeated trials,
8. sensor redundancy,
9. standardized handling,
10. event logging.

---

## 14. Minimum Confounder Log

For every demonstrator run:

| Variable | Required? | Notes |
|---|---:|---|
| acceleration vector | yes | core exposure variable |
| angular rate | yes | rotating/circular systems |
| vibration | yes | frequency spectrum preferred |
| temperature | yes | payload-level if possible |
| humidity | yes | especially biology/plants/humans |
| light | if relevant | mandatory for plants/circadian studies |
| CO2 | if relevant | plants/humans/animals |
| operational events | yes | start, stop, transfer, fault |
| power interruptions | yes | affects payloads and sensors |
| handling events | if relevant | mandatory for samples |
| noise | if humans/animals | sleep and stress confounder |
| electromagnetic field | if maglev/high power | EMC and biological context |

---

## 15. Confounder Interpretation Matrix

| Observation | Possible gravity explanation | Alternative explanation to test |
|---|---|---|
| altered cell morphology | mechanotransduction | shear, temperature, handling, substrate |
| changed microbial growth | gravity effect | oxygen gradients, mixing, temperature |
| changed root angle | gravitropism | light gradient, moisture gradient, vibration |
| altered sleep | gravity load | noise, vibration, light, confinement |
| reduced performance | hypergravity fatigue | motivation, sleep, motion sickness, learning |
| ball-trajectory error | Coriolis | spin, drag, launch angle, player adaptation |

---

## 16. Relationship to Literature Review

The literature review already includes sources showing that ground-based altered-gravity simulators can introduce artefacts. This document turns that warning into project requirements.

The key methodological lesson is:

> The platform is part of the experiment.

---

## 17. Immediate Actions

1. Define acceleration/vibration sensor package.
2. Define metadata schema for environmental logging.
3. Add confounder-control section to every experiment protocol.
4. Define matched 1 g control conditions.
5. Add vibration and environmental data to all demonstrator outputs.
6. Avoid biological or human claims without confounder data.

---

## 18. Preliminary Conclusion

Vibration and confounders are likely to determine whether the Hypergravity Habitat project is scientifically credible. A small demonstrator with excellent confounder measurement is more valuable than a large demonstrator with ambiguous data.

The first real experiment should be designed around measurement quality, not around impressive scale.