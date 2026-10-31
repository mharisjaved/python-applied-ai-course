# AI Capstone Plan

Copy this file into your capstone folder as `PLAN.md`, fill every section (short answers are fine), and get it
approved on Day 56. Keep it to about one page.

**Name:** … · **Option:** A / B / C / D · **Project title:** …

## 1. Problem and user

- **Problem** (1–2 sentences): what is hard or slow today, and for whom?
- **Target user:** who uses it, in what situation?
- **Why AI?** Which **one** part needs ML or an LLM, and why can plain Python not do that part well?

## 2. Example run

Write what the user types and what the app prints (5–10 lines, invented but realistic):

```
…
```

## 3. Data

- **Source:** (file name / dataset / sample texts you write) · number of rows or texts: …
- **Checked today:** I opened it and it has the columns or text I need: yes / no
- **Problems found** (missing values, odd categories, too little data…) and what I will do about them: …

## 4. Data & privacy check

- **Is any of the data personal** (names, contact details, IDs, health, money of a real person)? …
- **What is sent to the API**, exactly (or "nothing: local model")? …
- **What I deliberately do not send / store:** …
- **What users must not type**, and how the app tells them: …

## 5. Success criteria (at least 3, each with a number and how it is measured)

| # | Criterion | How I measure it | Target |
|---|-----------|------------------|--------|
| 1 | ≥ 5 pytest tests pass offline | `uv run pytest -q` without a key | 5+ passed |
| 2 | … | … | … |
| 3 | … | … | … |

## 6. Design: where the AI sits

- **Core functions** (no AI), one line each: …
- **The ONE AI function:** name, input, return value (the exact dict/shape): …
- **Offline mode:** what the mock returns (LLM) or which model is trained at start-up (option A): …
- **Fallback** when the AI reply is unusable or refused: …

## 7. Risks (top 3)

| Risk | Likelihood 1–3 | Impact 1–3 | Plan / fallback |
|------|----------------|------------|-----------------|
| No network or key during the demo | | | offline mode, rehearsed with `COURSE_OFFLINE=1` |
| … | | | |
| … | | | |

## 8. Scope and schedule

| Must (≤ 5, about 80 % of the time) | Should | Could |
|------------------------------------|--------|-------|
| … | … | … |

| Day | What I will have working by the end |
|-----|-------------------------------------|
| 57 | core + ≥ 3 tests + AI stub, app runs end to end |
| 58 | AI behind one function, mock first, fake-model tests |
| 59 | failure cases fixed, one hallucination/sanity check, README, demo script |
| 60 | presentation |

---

**Approval** (instructor): ☐ approved ☐ approved with changes: … ☐ not yet: … · date: …
