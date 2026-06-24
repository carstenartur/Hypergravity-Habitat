# Annotated Literature Review: Sustained Moderate Hypergravity

**Project:** Hypergravity Habitat  
**Document type:** annotated literature review and evidence matrix  
**Status:** Version 0.1 — annotated, not yet systematic  
**Scope:** altered gravity research, artificial gravity, centrifugation, analogues, space biology, plant science, biological payloads, and Coriolis/human-performance constraints  
**Last updated:** 2026-06-24

---

## 1. Purpose

This document converts the earlier literature-review scaffold into an annotated review. It identifies peer-reviewed and institutional sources that are directly relevant to the Hypergravity Habitat concept and uses them to test the central project premise:

> Does the existing altered-gravity research landscape leave a meaningful gap for sustained moderate hypergravity as a controlled terrestrial research environment?

This is not yet a complete systematic review. It is an annotated working review designed to support expert feedback, proposal preparation, and future systematic literature work.

---

## 2. Preliminary Review Conclusion

The literature and institutional sources support a cautious position:

1. **Human spaceflight deconditioning and countermeasure research are well-established.** NASA HRP and DLR :envihab provide strong institutional context for ground-based, analogue, and countermeasure research.
2. **Artificial gravity is a serious research topic, not a fringe idea.** Peer-reviewed reviews describe it as a possible integrated countermeasure, but emphasize unresolved questions about exposure duration, rotation rate, gravity gradients, Coriolis effects, and human tolerance.
3. **Bed-rest and short-arm centrifuge studies are important comparators.** They provide methodology and partial evidence, but they do not fully answer sustained habitat-scale moderate hypergravity questions.
4. **Biological hypergravity and simulated microgravity literature is substantial.** It shows that gravity and simulated gravity environments can affect cells, plants, microorganisms, and model systems, while also warning that fluid shear, vibration, and handling can confound results.
5. **The project’s research gap remains plausible but unproven.** The strongest near-term path is not human habitation, but a rigorously instrumented physical or biological payload demonstrator.
6. **Coriolis effects should be treated as an explicit design constraint.** Projectile sports, ball skills, throwing, kicking, and moving-object accuracy may require much larger radii than simple strength training.

---

## 3. Review Questions

### Primary Review Question

Does existing research infrastructure already cover sustained moderate hypergravity sufficiently, or is there a defensible research gap?

### Secondary Questions

1. Which existing platforms cover microgravity, bed rest, intermittent artificial gravity, and biological hypergravity?
2. What exposure durations, gravity levels, and measurement conditions are reported in the literature?
3. Which domains are strongest candidates for early non-human demonstrators?
4. Which human-centred claims are premature?
5. Which engineering variables are likely to confound biological or physiological interpretation?
6. How do Coriolis and rotating-frame effects affect possible sports-science or coordination uses?

---

## 4. Search Strategy

### 4.1 Databases and Source Types

The following sources should be used for the full systematic version:

- PubMed / MEDLINE
- NASA Technical Reports Server
- NASA Task Book
- NASA Open Science Data Repository
- ESA publications and facility documentation
- DLR publications and :envihab documentation
- Google Scholar
- Web of Science or Scopus where available
- IEEE Xplore for control, sensor, and maglev topics
- TRID / transportation databases for rail vibration and ride-quality literature

### 4.2 Search Strings

Human artificial gravity and centrifugation:

```text
("artificial gravity" OR centrifugation OR "short-arm centrifuge") AND (human OR astronaut OR "bed rest") AND (countermeasure OR physiology OR vestibular OR cardiovascular OR musculoskeletal)
```

Bed-rest analogues:

```text
("head-down tilt" OR "bed rest") AND (spaceflight OR microgravity) AND (countermeasure OR artificial gravity OR centrifuge)
```

Biological hypergravity:

```text
(hypergravity OR centrifuge OR "altered gravity") AND (cell OR microbial OR microorganism OR tissue OR mechanotransduction)
```

Plant science:

```text
(hypergravity OR "altered gravity" OR microgravity OR partial gravity) AND (plant OR Arabidopsis OR gravitropism OR root OR shoot)
```

Ground-based simulators and confounders:

```text
("random positioning machine" OR clinostat OR "simulated microgravity") AND (fluid OR shear OR artifact OR confounder OR mammalian cell)
```

Coriolis and human performance:

```text
(Coriolis OR "rotating environment" OR "rotating frame") AND (human OR vestibular OR projectile OR throwing OR sport OR locomotion OR artificial gravity)
```

Engineering and ride quality:

```text
(vibration OR "ride quality" OR "human comfort") AND (railway OR maglev OR "moving platform" OR laboratory)
```

---

## 5. Inclusion Criteria

Include sources that satisfy at least one of the following:

1. Peer-reviewed review or experimental paper on artificial gravity, centrifugation, bed rest, hypergravity, plant gravity response, or biological response to altered gravity.
2. Official institutional source describing relevant research infrastructure, programme goals, or data repositories.
3. Technical source relevant to vibration, rotating-frame dynamics, ride quality, or payload interpretation.
4. Source that explicitly reports gravity level, acceleration, exposure duration, experimental system, or control strategy.
5. Source that identifies confounders such as vibration, fluid shear, sample handling, confinement, or Coriolis effects.

---

## 6. Exclusion Criteria

Exclude or treat separately:

1. Popular articles unless they help identify primary sources.
2. Speculative architecture claims without equations, experiments, or source traceability.
3. Studies without clear exposure conditions.
4. Microgravity-only studies unless they directly support contrast, countermeasure logic, or research-gap framing.
5. High-g aviation studies unless relevant to moderate sustained exposure or human tolerance.
6. Biological studies where gravity cannot plausibly be separated from unmeasured vibration, shear, temperature, or handling artefacts.
7. Clinical or performance claims without controlled evidence.

---

## 7. Evidence Matrix

| ID | Source | Type | Domain | Key contribution | Relevance to Hypergravity Habitat | Limitations |
|---|---|---|---|---|---|---|
| I-01 | NASA Human Research Program | institutional | human spaceflight | HRP uses ground facilities, ISS, and analogues to protect astronaut health and performance | frames the project as possible analogue/pre-feasibility research | not evidence for the proposed infrastructure |
| I-02 | DLR :envihab | institutional facility | aerospace medicine | integrated terrestrial facility with short-arm centrifuge, living/simulation, medical and biology modules | key benchmark and comparator | does not by itself establish the project gap |
| I-03 | NASA Biological & Physical Sciences | institutional | space biology / physical sciences | NASA studies how gravity affects living organisms and how systems respond to spaceflight environments | supports biological-payload path and open-data orientation | programme-level source, not specific hypergravity evidence |
| A-01 | Clément, Bukley & Paloski (2015) | peer-reviewed review | artificial gravity | argues artificial gravity could provide broad-spectrum countermeasure but requires more study | central artificial-gravity review and Coriolis/radius context | focused on spaceflight countermeasures, not terrestrial hypergravity habitat |
| A-02 | Pavy-Le Traon et al. (2007) | peer-reviewed review | bed rest | reviews 20 years of bed-rest physiology research | establishes bed rest as strong analogue methodology | bed rest models unloading, not elevated effective gravity |
| A-03 | Hargens & Vico (2016) | peer-reviewed review | bed rest / analogue | describes long-duration bed rest as microgravity analogue | supports human-research methodology and control design | does not answer sustained hypergravity adaptation |
| A-04 | Yang et al. (2007) | peer-reviewed experiment | hypergravity exercise | discusses artificial gravity/hypergravity resistance exercise as microgravity countermeasure | supports exercise-under-centrifugation as relevant comparator | short/intervention focus; not habitat-scale continuous exposure |
| A-05 | Caiozzo & Haddad et al. (2009) | peer-reviewed pilot study | artificial gravity / muscle | pilot study on artificial gravity as countermeasure for knee extensor and plantar flexor muscle groups | relevant to muscle-loading hypothesis | pilot scale; not long-duration habitation |
| B-01 | Wuest et al. (2017) | peer-reviewed experiment/model | simulated microgravity confounders | shows RPM fluid motion and shear stresses can be important | directly supports confounder-control requirement | RPM context, not hypergravity habitat directly |
| B-02 | Wuest et al. (2015) | peer-reviewed review | mammalian cell culture | critical review of RPM use for mammalian cell culture | supports caution in interpreting ground-based altered-gravity biology | simulated microgravity, not sustained hypergravity |
| B-03 | Herranz et al. (2013) | peer-reviewed review | ground-based simulators | organism-specific recommendations for simulated microgravity facilities | helps define platform-selection and control standards | mainly simulated microgravity |
| B-04 | van Loon (2007) | peer-reviewed review/history | RPM / gravity research | history and use of the RPM in gravity-related research | background for simulator taxonomy | not a hypergravity habitat source |
| P-01 | Kiss (2000) | peer-reviewed review | plant gravitropism | reviews early phases of plant gravitropism | supports plant science as gravity-sensitive early domain | not specific to moderate sustained hypergravity |
| P-02 | Vandenbrink & Kiss (2016) | peer-reviewed review | plant space biology | critical review of plant experiments in microgravity | supports plant relevance and space-biology framing | reduced gravity focus |
| P-03 | Manzano et al. (2018) | peer-reviewed experiment | partial gravity / plants | tests Moon/Mars partial-gravity simulation paradigms in plant development | relevant to partial-gravity and plant-response methodology | not elevated gravity habitat scale |
| P-04 | Moulia & Fournier (2009) | peer-reviewed review | plant biomechanics | biomechanics and systems view of gravitropic movements | supports physical modelling of plant responses | not an infrastructure source |
| C-01 | Clément et al. (2015), Coriolis sections | peer-reviewed review | rotating environments | explicitly discusses Coriolis, cross-coupled accelerations, radius/rotation trade-offs | direct basis for radius constraints and sports/projectile concerns | mostly human movement/spacecraft context |
| C-02 | Nathan et al. (2008) | peer-reviewed sports physics | ball flight | quantifies spin/Magnus effects in baseball flight | useful reminder that projectile sports require full trajectory models | not about rotating habitats |

---

## 8. Annotated Sources

### I-01 — NASA Human Research Program

**Reference:** NASA Human Research Program. https://www.nasa.gov/hrp/

**Type:** Official institutional source.

**Summary:** NASA describes HRP as using research to protect astronaut health and performance, including ground facilities, the ISS, and analog environments.

**Relevance:** This source frames the project as belonging to a recognized domain: human health and performance research for exploration. It supports the use of analogue and ground facilities as legitimate research tools.

**Limitations:** It does not support any claim that a Hypergravity Habitat is needed or feasible. It is context, not project-specific evidence.

**Use in project:** Institutional anchor for human research, countermeasures, analogues, and risk framing.

---

### I-02 — DLR :envihab

**Reference:** DLR Institute of Aerospace Medicine. :envihab aerospace medicine research facility. https://www.dlr.de/en/envihab

**Type:** Official facility source.

**Summary:** DLR describes :envihab as a medical research facility for studying environmental effects on humans and countermeasures. It includes a Short-Arm Centrifuge, living and simulation facility, PET-MRI, psychology laboratory, and biology laboratory.

**Relevance:** This is one of the most important comparator facilities for the Hypergravity Habitat concept. It shows that advanced terrestrial aerospace medicine infrastructure already exists and that any new concept must define what it adds.

**Limitations:** The official facility description is not a peer-reviewed experimental paper. It does not prove that sustained moderate hypergravity is missing.

**Use in project:** Benchmark for facility comparison, requirements, and funding credibility.

---

### I-03 — NASA Biological & Physical Sciences

**Reference:** NASA Biological & Physical Sciences. https://science.nasa.gov/biological-physical/

**Type:** Official institutional source.

**Summary:** NASA BPS describes research using space stressors such as radiation and microgravity and states that the Space Biology Program studies how gravity affects living organisms and how biological systems accommodate to spaceflight environments.

**Relevance:** This supports the biological-payload route for the Hypergravity Habitat project. It also supports open-science data practices and the importance of metadata.

**Limitations:** This is programme-level context rather than evidence for sustained moderate hypergravity.

**Use in project:** Anchor for biology, plant science, microbial systems, and open data.

---

### A-01 — Clément, Bukley & Paloski (2015)

**Reference:** Clément, G. R., Bukley, A. P., & Paloski, W. H. (2015). *Artificial gravity as a countermeasure for mitigating physiological deconditioning during long-duration space missions*. Frontiers in Systems Neuroscience, 9, 92. https://doi.org/10.3389/fnsys.2015.00092

**Type:** Peer-reviewed review.

**Summary:** The review argues that artificial gravity could be a broad-spectrum countermeasure for weightlessness-related deconditioning, while emphasizing unresolved questions about sensorimotor effects, rotation rate, gravity gradients, exposure duration, and Coriolis/cross-coupled accelerations.

**Relevance:** This is one of the central sources for the project. It validates artificial gravity as a serious research field and explains why rotating environments introduce human-factors constraints.

**Limitations:** The article is focused on spaceflight artificial gravity as a countermeasure, not on terrestrial sustained moderate hypergravity. It also does not establish that a large habitat-style terrestrial platform is necessary.

**Use in project:** Core source for artificial gravity, radius/rotation trade-offs, human tolerance, Coriolis constraints, and why sustained exposure remains an open question.

---

### A-02 — Pavy-Le Traon et al. (2007)

**Reference:** Pavy-Le Traon, A., Heer, M., Narici, M. V., Rittweger, J., & Vernikos, J. (2007). *From space to Earth: advances in human physiology from 20 years of bed rest studies (1986–2006)*. European Journal of Applied Physiology. DOI to verify: https://doi.org/10.1007/s00421-007-0474-z

**Type:** Peer-reviewed review.

**Summary:** Reviews decades of bed-rest studies as an analogue for selected microgravity effects.

**Relevance:** Important for methodology: participant monitoring, controlled protocols, baseline/recovery design, and countermeasure evaluation.

**Limitations:** Bed rest is an unloading analogue. It does not create elevated effective gravity and therefore cannot answer sustained hypergravity questions directly.

**Use in project:** Methodological comparator for any future human protocol.

---

### A-03 — Hargens & Vico (2016)

**Reference:** Hargens, A. R., & Vico, L. (2016). *Long-duration bed rest as an analog to microgravity*. Journal of Applied Physiology. DOI to verify.

**Type:** Peer-reviewed review.

**Summary:** Discusses bed rest as a terrestrial analogue for microgravity-related physiological changes.

**Relevance:** Supports the argument that terrestrial analogues are valuable but domain-specific. It strengthens the need to define exactly what a hypergravity analogue would add.

**Limitations:** Again, bed rest is not sustained hypergravity.

**Use in project:** Analogue-research methodology and human-protocol design.

---

### A-04 — Yang et al. (2007)

**Reference:** Yang, Y., Baker, M., Graf, S., Larson, J., & Caiozzo, V. J. (2007). *Hypergravity resistance exercise: the use of artificial gravity as potential countermeasure to microgravity*. Journal of Applied Physiology. DOI to verify.

**Type:** Peer-reviewed experiment / applied physiology study.

**Summary:** Investigates hypergravity resistance exercise in the context of artificial gravity as a possible microgravity countermeasure.

**Relevance:** Directly relevant to the project’s muscle-loading and training questions. It suggests that exercise under increased effective load is already a legitimate research topic.

**Limitations:** The source does not support claims about long-duration habitat exposure or sports-training benefit. It should be used as a comparator, not as proof of the Hypergravity Habitat concept.

**Use in project:** Exercise and sports-science background; countermeasure comparison.

---

### A-05 — Caiozzo & Haddad et al. (2009)

**Reference:** Caiozzo, V. J., Haddad, F., and colleagues. (2009). *Artificial gravity as a countermeasure to microgravity: a pilot study examining the effects on knee extensor and plantar flexor muscle groups*. Journal of Applied Physiology. DOI to verify.

**Type:** Peer-reviewed pilot study.

**Summary:** Pilot evidence on artificial gravity as a countermeasure for selected muscle groups.

**Relevance:** Supports the inclusion of muscle-specific loading hypotheses and provides a bridge between centrifugation and exercise physiology.

**Limitations:** Pilot scale; not sufficient for claims about sustained habitation, sports performance, or clinical benefit.

**Use in project:** Human physiology and muscle-loading evidence map.

---

### B-01 — Wuest et al. (2017)

**Reference:** Wuest, S. L., Stern, P., Casartelli, E., & Egli, M. (2017). *Fluid Dynamics Appearing during Simulated Microgravity Using Random Positioning Machines*. PLOS ONE, 12(1), e0170826. https://doi.org/10.1371/journal.pone.0170826

**Type:** Peer-reviewed research article / numerical modelling.

**Summary:** The paper shows that random positioning machines, although widely used for simulated microgravity, can introduce fluid motion and shear stresses in cell-culture flasks. The authors conclude that such fluid dynamics cannot always be neglected.

**Relevance:** Extremely important for Hypergravity Habitat biology. It demonstrates that altered-gravity experiments can be confounded by the platform itself. Any biological hypergravity payload must measure and control vibration, shear, fluid motion, temperature, handling, and geometry.

**Limitations:** The paper focuses on RPM simulated microgravity, not sustained hypergravity. Its value lies in confounder awareness and experimental design.

**Use in project:** Biological payload requirements, confounder-control strategy, evidence standard.

---

### B-02 — Wuest et al. (2015)

**Reference:** Wuest, S. L., Richard, S., Kopp, S., Grimm, D., & Egli, M. (2015). *Simulated Microgravity: Critical Review on the Use of Random Positioning Machines for Mammalian Cell Culture*. BioMed Research International. DOI to verify: https://doi.org/10.1155/2015/971474

**Type:** Peer-reviewed review.

**Summary:** Critical review of random positioning machines for mammalian cell culture.

**Relevance:** Supports the project’s requirement that biological altered-gravity experiments need careful platform-specific interpretation.

**Limitations:** Simulated microgravity rather than sustained hypergravity.

**Use in project:** Cell-biology experimental design and confounder identification.

---

### B-03 — Herranz et al. (2013)

**Reference:** Herranz, R., Anken, R., Boonstra, J., Braun, M., Christianen, P. C. M., de Geest, M., et al. (2013). *Ground-Based Facilities for Simulation of Microgravity: Organism-Specific Recommendations for Their Use, and Recommended Terminology*. Astrobiology. DOI to verify: https://doi.org/10.1089/ast.2012.0876

**Type:** Peer-reviewed review / recommendations.

**Summary:** Provides recommendations and terminology for ground-based microgravity simulation facilities across organism types.

**Relevance:** Helps the project define terminology, controls, and organism-specific platform selection.

**Limitations:** Focused on simulated microgravity, not hypergravity.

**Use in project:** Terminology, experimental standards, organism-specific design.

---

### B-04 — van Loon (2007)

**Reference:** van Loon, J. J. W. A. (2007). *Some history and use of the random positioning machine, RPM, in gravity related research*. Advances in Space Research. DOI to verify.

**Type:** Peer-reviewed review/history.

**Summary:** Historical and technical overview of the RPM in gravity-related research.

**Relevance:** Useful for understanding the evolution of ground-based altered-gravity simulators.

**Limitations:** Not specific to sustained hypergravity.

**Use in project:** Background taxonomy for simulator technologies.

---

### P-01 — Kiss (2000)

**Reference:** Kiss, J. Z. (2000). *Mechanisms of the Early Phases of Plant Gravitropism*. Critical Reviews in Plant Sciences. DOI to verify.

**Type:** Peer-reviewed review.

**Summary:** Reviews early mechanisms of plant gravitropism.

**Relevance:** Provides foundational plant-science context for why plants are a strong early experimental system.

**Limitations:** Not focused on moderate hypergravity or habitat-scale experiments.

**Use in project:** Plant payload selection and endpoint definition.

---

### P-02 — Vandenbrink & Kiss (2016)

**Reference:** Vandenbrink, J. P., & Kiss, J. Z. (2016). *Space, the final frontier: A critical review of recent experiments performed in microgravity*. Plant Science. DOI to verify.

**Type:** Peer-reviewed review.

**Summary:** Reviews plant experiments performed in microgravity.

**Relevance:** Provides a space-biology comparator for plant payloads and highlights the importance of controlled environmental conditions.

**Limitations:** Reduced/microgravity focus; does not answer elevated-gravity adaptation.

**Use in project:** Plant science background and research-gap contrast.

---

### P-03 — Manzano et al. (2018)

**Reference:** Manzano, A., Herranz, R., den Toom, L. A., te Slaa, S., Borst, G., et al. (2018). *Novel, Moon and Mars, partial gravity simulation paradigms and their effects on the balance between cell growth and cell proliferation during early plant development*. npj Microgravity. DOI to verify: https://doi.org/10.1038/s41526-018-0044-6

**Type:** Peer-reviewed research article.

**Summary:** Studies partial-gravity simulation paradigms and early plant development.

**Relevance:** Important for partial-gravity methodology and plant development under altered gravity.

**Limitations:** It does not directly address sustained moderate hypergravity above 1 g.

**Use in project:** Plant experiment design and partial-gravity comparison.

---

### P-04 — Moulia & Fournier (2009)

**Reference:** Moulia, B., & Fournier, M. (2009). *The power and control of gravitropic movements in plants: a biomechanical and systems biology view*. Journal of Experimental Botany. DOI to verify.

**Type:** Peer-reviewed review.

**Summary:** Presents gravitropic movement as a biomechanical and systems-biology problem.

**Relevance:** Useful for designing plant experiments that combine morphology, mechanics, imaging, and environmental control.

**Limitations:** Not a hypergravity infrastructure source.

**Use in project:** Plant biomechanics and endpoint selection.

---

### C-01 — Coriolis and Rotating-Environment Constraints in Clément et al. (2015)

**Reference:** Clément, G. R., Bukley, A. P., & Paloski, W. H. (2015). *Artificial gravity as a countermeasure for mitigating physiological deconditioning during long-duration space missions*. Frontiers in Systems Neuroscience, 9, 92. https://doi.org/10.3389/fnsys.2015.00092

**Type:** Peer-reviewed review.

**Summary:** The paper explicitly discusses Coriolis forces, cross-coupled angular accelerations, rotation-rate limits, radius trade-offs, and human adaptation in rotating environments.

**Relevance:** This is the best initial source for including Coriolis as a design constraint. It supports the argument that radius and angular rate are not only engineering choices; they affect human movement, vestibular comfort, and potentially projectile accuracy.

**Limitations:** The paper focuses primarily on spacecraft artificial gravity, not sports use inside terrestrial hypergravity facilities.

**Use in project:** Coriolis constraints, human factors, ballistics and coordination research question.

---

### C-02 — Ball Flight and Sports Physics

**Reference:** Nathan, A. M., Hopkins, J., Chong, L., & Kaczmarski, H. (2008). *The effect of spin on the flight of a baseball*. American Journal of Physics. DOI to verify.

**Type:** Peer-reviewed sports physics.

**Summary:** Studies ball flight and the aerodynamic consequences of spin.

**Relevance:** Not a Coriolis source by itself, but important for any serious sports-ball analysis because ball flight is also affected by drag, spin, and Magnus forces.

**Limitations:** Baseball-specific and Earth-normal environment; does not address rotating habitats.

**Use in project:** Reminder that sports-projectile modelling must combine Coriolis, drag, spin, launch angle, ball type, and target geometry.

---

## 9. Coriolis, Ball Sports, and Radius Requirements

### 9.1 Why This Belongs in the Literature Review

Throwing, kicking, catching, and target accuracy are not merely recreational topics. They provide a sensitive test case for rotating-frame effects. A person doing squats or cycling may tolerate angular rates that would make long throws or football shots behave very differently from Earth-normal sport.

Therefore, projectile accuracy can be used as a **human-factors and design-requirement probe**.

### 9.2 First-Order Model

For a projectile moving inside a rotating reference frame, the Coriolis acceleration magnitude is approximately:

\[
a_{cor} = 2 \Omega v
\]

where:

- \(\Omega\) is the angular rate of the platform,
- \(v\) is projectile speed relative to the rotating frame.

For a simple worst-case horizontal throw over distance \(L\), with flight time \(T \approx L/v\), a first-order lateral deflection estimate is:

\[
y \approx \Omega v T^2 \approx \Omega \frac{L^2}{v}
\]

This is only a screening equation. A full model must include launch angle, vertical motion, drag, spin, Magnus effect, ball type, release height, target height, and direction relative to the rotation axis.

### 9.3 Example Implication

For a 1.10 g resultant effective-gravity target on a terrestrial circular platform, the required lateral acceleration is approximately 0.458 g. The platform angular rate is:

\[
\Omega = \sqrt{a_c/r}
\]

At a radius of 500 m, this is roughly 0.095 rad/s, or about 0.91 rpm. A 20 m handball-style throw at 20 m/s gives the order-of-magnitude deflection:

\[
y \approx 0.095 \cdot \frac{20^2}{20} \approx 1.9\,m
\]

A 30 m football-style pass or shot at 25 m/s gives:

\[
y \approx 0.095 \cdot \frac{30^2}{25} \approx 3.4\,m
\]

This indicates that ball sports may require much larger radii than basic muscle-loading exercises if Earth-like accuracy is desired.

### 9.4 Design Interpretation

This does **not** mean that sports use is impossible. It means it must be classified carefully:

| Use case | Radius requirement implication |
|---|---|
| Stationary strength training | radius mainly driven by comfort, safety, and platform feasibility |
| Cycling / treadmill / resistance training | Coriolis is relevant but less severe than for projectiles |
| Short-distance coordination drills | feasible at smaller radii if distances are short |
| Ball throwing/kicking with Earth-like accuracy | likely requires much larger radii or very low angular rate |
| Ball sports as adaptation research | possible even if trajectories differ, but not Earth-equivalent |
| Elite sports training claim | premature and should not be made without evidence |

### 9.5 Research Question Added

> Can projectile-skill tasks such as handball throws, football passes, or target kicks be used as sensitive functional tests for Coriolis effects, motor adaptation, and radius requirements in hypergravity training environments?

This is a legitimate theoretical research question. It should be included as a later-stage sports-science and human-factors topic, not as a primary justification for building the facility.

---

## 10. Gap Assessment by Domain

| Domain | Existing evidence strength | Gap relevance | Near-term action |
|---|---:|---:|---|
| human spaceflight physiology | high | medium | use as motivation and comparator |
| bed-rest analogues | high | medium | use methodology, not as direct substitute |
| artificial gravity centrifugation | medium-high | high | review exposure duration and tolerance literature |
| biological hypergravity | medium | high | identify low-risk payloads |
| plant altered-gravity science | medium-high | high | define plant demonstrator |
| sports performance | low-medium | exploratory | model Coriolis and movement tasks |
| railway/maglev ride quality | to be reviewed | high | add engineering standards |
| cost and infrastructure | low | high | add cost references and sensitivity analysis |

---

## 11. Claims Supported by Current Sources

The current sources support the following cautious claims:

1. Human spaceflight health and performance research already uses ground facilities, ISS research, and analogue environments.
2. DLR :envihab is a strong terrestrial aerospace medicine comparator and includes a short-arm centrifuge and living/simulation research infrastructure.
3. Artificial gravity has been seriously reviewed as a possible integrated countermeasure, but important questions remain unresolved.
4. Bed-rest studies are a mature analogue method for selected unloading effects.
5. Biological altered-gravity experiments require careful control of non-gravity confounders such as fluid shear and platform motion.
6. Plant biology is a strong early candidate domain because gravity sensing is central to plant development.
7. Coriolis and rotation-rate effects should be explicit design constraints for human movement and projectile tasks.

---

## 12. Claims Not Yet Supported

The current sources do **not** yet support these claims:

1. Sustained moderate hypergravity is beneficial for humans.
2. Hypergravity habitation is safe for long durations.
3. A railway or maglev platform is preferable to a rotating demonstrator.
4. Sports performance would improve after hypergravity exposure.
5. Ball-sport training would transfer positively back to 1 g.
6. A large habitat is justified before payload and modelling stages.
7. Existing facilities cannot answer any of the project questions.

These claims must remain hypotheses or open questions.

---

## 13. Priority Literature Gaps

The next review iteration should add:

1. more peer-reviewed short-arm centrifuge and bed-rest artificial-gravity trials,
2. DLR :envihab and short-arm centrifuge peer-reviewed studies,
3. ESA Large Diameter Centrifuge documentation and publications,
4. plant hypergravity papers with reported gravity levels and durations,
5. cell and microbial hypergravity studies with controlled vibration/shear conditions,
6. human movement studies in rotating rooms or centrifuges,
7. sports projectile modelling literature, including drag and Magnus effects,
8. rail/maglev vibration and ride-quality standards,
9. ethics literature for analogue human studies,
10. research-infrastructure cost benchmarks.

---

## 14. How This Review Changes the Project

The review supports three immediate project changes:

1. **Payload-first strategy:** biological and physical payload demonstrators should precede human-centred claims.
2. **Confounder-first measurement:** acceleration, vibration, shear, temperature, humidity, and operational events must be logged from the beginning.
3. **Coriolis as a requirement variable:** any sports, coordination, or projectile use case must be modelled separately from simple muscle-loading use cases.

---

## 15. Status and Next Step

This is now an annotated literature review rather than a scaffold, but it is not yet a systematic review. The next step is to verify all DOI metadata, add more peer-reviewed sources per domain, and convert the evidence matrix into a source-by-source spreadsheet or BibTeX-backed bibliography.