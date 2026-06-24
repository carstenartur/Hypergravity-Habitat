# Contributing

Thank you for considering a contribution to Hypergravity Habitat.

This project is an exploratory research documentation effort. The most useful contributions at this stage are critical, corrective, and evidence-building. The goal is not to advocate for a facility before the evidence exists. The goal is to determine whether the research question deserves further work.

## Useful Contributions

The project especially welcomes contributions that:

- identify weak assumptions,
- add missing literature,
- correct equations or units,
- improve reproducibility of calculations,
- identify confounders,
- strengthen safety and ethics language,
- compare existing facilities,
- narrow the scope,
- define stop/go criteria,
- explain why a proposed path should be rejected or delayed.

A negative or narrowing contribution can be more valuable than a supportive one.

## Evidence Standard

Please distinguish clearly between:

- established knowledge,
- engineering principle,
- engineering estimate,
- working hypothesis,
- open research question,
- later-stage possibility.

Do not present human benefit, clinical benefit, athletic benefit, safety, feasibility, or economic justification as established unless the cited evidence directly supports that claim.

## Formula and Notation Style

Reader-facing Markdown should avoid raw LaTeX delimiters. Prefer readable notation such as:

```text
g_eff = √(g² + a_c²)
```

Always define symbols immediately after a formula.

Detailed rules are in [`docs/documentation-style-guide.md`](docs/documentation-style-guide.md).

## Human, Animal, and Biological Research

Do not propose human exposure, animal experiments, biological payloads, clinical applications, athlete interventions, or facility operation as ready-to-run activities. Such work would require formal institutional review, safety engineering, ethics approval, medical or veterinary governance, and appropriate data protection.

## Pull Request Checklist

Before opening a pull request, check that:

- [ ] claims are cautious and evidence-labelled,
- [ ] assumptions and limitations are explicit,
- [ ] formula notation is readable,
- [ ] sources are cited where needed,
- [ ] no unsupported benefit or safety claims are introduced,
- [ ] relevant documents are cross-linked,
- [ ] public-readiness lint checks pass where applicable.

Run:

```bash
python scripts/public_readiness_lint.py .
```

## Tone

Use precise, non-promotional language. This repository should be credible to sceptical reviewers.

Recommended framing:

> We are seeking critical review of the research gap, assumptions, safety logic, and staged demonstrator pathway.

---

<!-- project-footer -->
**Project:** [Hypergravity Habitat](README.md) · **Status:** exploratory research documentation · **License:** see repository license and file-level notes
