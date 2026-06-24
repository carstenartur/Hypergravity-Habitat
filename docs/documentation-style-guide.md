# Documentation Style Guide

**Project:** Hypergravity Habitat  
**Document type:** documentation style and review standard  
**Status:** recommended public-repository standard  
**Scope:** Markdown documents, equations, evidence levels, links, claims, footers, and public readability

---

## 1. Purpose

This guide defines how Hypergravity Habitat documents should be written before and after the repository becomes public.

The project combines physics, engineering, biology, human factors, safety, ethics, and programme planning. The writing must therefore be readable to interdisciplinary reviewers, not only to specialists.

---

## 2. Audience

Write for:

- scientists from adjacent fields,
- engineers outside the immediate subsystem,
- ethics and safety reviewers,
- potential collaborators,
- funders and research-infrastructure reviewers,
- technically interested readers.

Do not assume that all readers know LaTeX, railway engineering, centrifuge terminology, or space-medicine shorthand.

---

## 3. Formula and Notation Rules

### 3.1 No raw markup in reader-facing text

Do not leave reader-facing formulas in unfinished markup form. Avoid display-math delimiters or inline-math delimiters that only work in certain renderers.

### 3.2 Preferred formula style

Use readable plain text or Unicode notation:

```text
g_eff = √(g² + a_c²)
```

Then explain it immediately:

> The effective gravity is the vector combination of Earth gravity and the generated centripetal acceleration.

### 3.3 Always define symbols

After any formula, define every symbol used.

Example:

```text
a_c = v² / r
```

Where:

- `a_c` is centripetal acceleration,
- `v` is tangential speed,
- `r` is radius.

### 3.4 Keep formulas proportional to need

Use formulas only where they improve understanding. In proposal, governance, ethics, roadmap, and outreach documents, prefer plain language unless a formula is essential.

---

## 4. Evidence-Level Language

Every major claim should fall into one of these categories:

| Evidence level | Use when |
|---|---|
| Established knowledge | supported by accepted physics, engineering practice, peer-reviewed literature, or official institutional sources |
| Engineering principle | follows directly from stated equations and assumptions |
| Engineering estimate | approximate and dependent on assumptions |
| Working hypothesis | plausible but not demonstrated for this project |
| Open research question | requires literature review, modelling, experiment, or expert feedback |
| Later-stage possibility | relevant only after prior safety, ethics, and feasibility gates |

Avoid converting hypotheses into claims by tone.

---

## 5. Claims to Avoid Without Evidence

Do not claim that sustained moderate hypergravity:

- is safe for humans,
- improves health,
- improves athletic performance,
- treats or prevents disease,
- is economically justified,
- requires a full-scale habitat,
- is better than existing centrifuge or laboratory approaches,
- should proceed directly to human exposure.

Use cautious language:

- “may be relevant”,
- “candidate research question”,
- “requires validation”,
- “working hypothesis”,
- “not yet established”,
- “requires expert review”.

---

## 6. Citation and Source Rules

Use citations for:

- biological or physiological claims,
- facility capabilities,
- safety or ethics standards,
- human tolerance statements,
- cost estimates,
- engineering standards,
- data-management claims,
- specific literature findings.

A citation should support the exact statement being made. Unverified reference metadata should be marked clearly until checked; before outreach to domain experts, verify the most central sources.

---

## 7. Internal Links

Use relative links so the repository works when cloned or browsed locally.

Examples:

```markdown
[Physics Reference](physics-reference.md)
[Design Requirements](engineering/design-requirements.md)
[README](../README.md)
```

Run a link check before public release.

---

## 8. Document Header Standard

Each major document should begin with:

```markdown
# Document Title

**Project:** Hypergravity Habitat  
**Document type:** short description  
**Status:** working / draft / review-ready / deprecated  
**Scope:** what the document covers
```

Optional fields:

```markdown
**Audience:** target readers  
**Last updated:** YYYY-MM-DD
```

---

## 9. Footer Standard

Each Markdown document should end with a short footer.

For files in `docs/`:

```markdown
---

<!-- project-footer -->
**Project:** [Hypergravity Habitat](../README.md) · **Status:** exploratory research documentation · **License:** see repository license and file-level notes
```

For files in `docs/science/`, `docs/engineering/`, or `docs/economics/` use `../../README.md` as the target. For files in the repository root use `README.md`.

The footer does not replace the license file.

---

## 10. Public Outreach Tone

When contacting potential reviewers or collaborators:

- ask for critique, not endorsement;
- state what is uncertain;
- state what has not been claimed;
- ask targeted questions;
- avoid hype;
- include one short entry document and one detailed repository link.

Recommended phrase:

> We are not seeking endorsement at this stage. We are seeking critical review of the research gap, assumptions, safety logic, and staged demonstrator pathway.

---

## 11. Review Checklist for Each Document

Before a document is considered public-ready, check:

- [ ] no unfinished formula markup remains,
- [ ] formulas are readable and explained,
- [ ] claims are marked by evidence level,
- [ ] assumptions are explicit,
- [ ] limitations are visible,
- [ ] internal links work,
- [ ] source-dependent claims have citations or are marked as needing sources,
- [ ] human, medical, sports, and safety claims are cautious,
- [ ] the document links to related documents,
- [ ] the project footer is present.

---

<!-- project-footer -->
**Project:** [Hypergravity Habitat](../README.md) · **Status:** exploratory research documentation · **License:** see repository license and file-level notes
