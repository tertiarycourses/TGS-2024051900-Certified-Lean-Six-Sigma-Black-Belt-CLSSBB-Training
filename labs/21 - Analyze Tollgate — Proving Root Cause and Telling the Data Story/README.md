<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Lab 21 — Analyze Tollgate — Proving Root Cause and Telling the Data Story

**ANALYZE** · Consolidate your analysis into a defensible root cause conclusion (A3, K1).

| Field | Detail |
|---|---|
| Case study | Meridian Medical Devices — seal weld burst pressure |
| DMAIC phase | ANALYZE |
| Lab type | Core |
| Deliverable | An Analyze tollgate pack with proven root causes, evidence and a business-language summary. |
| Tools | Evidence consolidation, root cause validation, statistical-to-business translation, tollgate review, challenge preparation |
| Data file | `lab-21-analyze-tollgate-evidence.xlsx` |

---

## The Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## The Evidence

**`lab-21-analyze-tollgate-evidence.xlsx`** — *Template.* The evidence register for the Analyze tollgate — every claimed root cause, the statistical test that proves it, and the p-value.

| Sheet | What it contains | Rows |
|---|---|---|
| EvidenceRegister | A root cause with no test result beside it is an opinion. Fill this from Labs 15-20. | 9 |
| TollgateChecklist | The sponsor will ask these. Have the answer. | 7 |

Open the workbook from this folder. Every workbook opens on a **Data Dictionary** sheet defining each column, its unit and the specification limits — read it before you analyse anything.

## Step-by-Step

1. Assemble every analytical result from Labs 15-20: stratification, hypothesis tests, regression model, ANOVA, multi-vari and chi-square.
2. For each candidate cause, record the verdict — PROVEN (statistically supported), REJECTED (tested and cleared) or UNTESTED (no data available).
3. Apply the triangulation rule: a root cause is strongest when supported by more than one independent method — for instance stratification plus a hypothesis test plus a regression coefficient.
4. Check each proven cause for practical significance. Quantify how much of the Y gap each explains, in percent and in dollars.
5. Rank your proven causes by the size of their contribution to the Y gap.
6. Confirm your causes are ACTIONABLE — a proven cause you cannot influence belongs in the risk register, not the improvement plan.
7. Translate each finding into one business sentence: 'Night shift at Suzhou runs 2.3 percentage points lower first-pass yield, costing about $180k annually.'
8. Build the tollgate pack: baseline, analysis method, proven causes, rejected causes, quantified impact and the recommendation to proceed.
9. Rehearse the challenges you should expect: was the sample adequate, were assumptions checked, could a confounding variable explain this, is the measurement system valid?
10. Prepare your evidence for each challenge — this is exactly what the Day 5 steering committee will probe.
11. Present the tollgate to a peer group and capture their challenges, then strengthen any weak points before Day 4.

## The GenAI Prompt

Copy the prompt in [prompt.txt](prompt.txt) into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details, then CHECK the answer against your own working — the tool is right, the AI is not always.

## Self-Check — Is Your Output Finished?

Every candidate cause carries a verdict, proven causes are triangulated across multiple methods and quantified in dollars, and you have rehearsed a prepared response to each expected challenge.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Files in this folder: [scenario.md](scenario.md) · [worksheet.md](worksheet.md) (and worksheet.pdf) · `lab-21-analyze-tollgate-evidence.xlsx` · [debrief.md](debrief.md) (TRAINER) · [prompt.txt](prompt.txt)*

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
