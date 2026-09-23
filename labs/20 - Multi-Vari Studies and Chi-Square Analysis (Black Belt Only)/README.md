<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Lab 20 — Multi-Vari Studies and Chi-Square Analysis (Black Belt Only)

**ANALYZE** · Decompose variation by family using a multi-vari study and test categorical association (A3, K2).

| Field | Detail |
|---|---|
| Case study | Meridian Medical Devices — seal weld burst pressure |
| DMAIC phase | ANALYZE |
| Lab type | Core |
| Deliverable | A multi-vari chart decomposing your capstone variation plus a chi-square association test. |
| Tools | Multi-vari studies, positional/cyclical/temporal families, variation decomposition, chi-square, contingency tables, expected frequencies |
| Data file | `lab-20-multivari-chisquare.xlsx` |

---

## The Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## The Evidence

**`lab-20-multivari-chisquare.xlsx`** — *Dataset.* A multi-vari study sampling positional, cyclical and temporal families, plus a plant x defect-mode contingency table for chi-square.

| Sheet | What it contains | Rows |
|---|---|---|
| MultiVari | 3 lines x 4 cavities x 5 time points x 2 replicates = 120 readings. | 120 |
| ChiSquare | Defect counts by plant and mode — a 3x4 contingency table. | 3 |

Open the workbook from this folder. Every workbook opens on a **Data Dictionary** sheet defining each column, its unit and the specification limits — read it before you analyse anything.

> Use your OWN workplace data wherever you can obtain it. The workbook is the fallback, and it describes the same Meridian process as every other lab, so your figures reconcile across labs.

## Step-by-Step

1. Understand the three variation families. POSITIONAL: within a single unit or across positions in a machine. CYCLICAL: unit to unit, batch to batch. TEMPORAL: shift to shift, day to day.
2. Understand the payoff: if 70 percent of variation is positional, then investigating shift patterns is wasted effort no matter how thorough the investigation.
3. Design a multi-vari sampling plan for your capstone: sample multiple positions within units, consecutive units, and repeat across time periods.
4. Ensure the sampling captures all three families simultaneously — this is a nested sampling design, not three separate studies.
5. Collect the data and plot the multi-vari chart, with positional variation innermost and temporal outermost.
6. Read the chart: the family showing the largest vertical spread dominates. That is where your root cause investigation should concentrate.
7. Quantify the contribution of each family as a percentage of total variation using variance components.
8. Re-prioritise your candidate cause list from Lab 16 against the dominant variation family, and drop causes that belong to a family contributing little.
9. Now chi-square. Build a contingency table of two categorical variables from your capstone — defect type against shift, supplier or line.
10. Calculate expected frequencies under independence: expected = (row total x column total) / grand total.
11. Check the validity condition: all expected frequencies should be 5 or more, or the chi-square approximation breaks down and categories must be combined.
12. Compute the chi-square statistic and its p-value, and conclude whether defect type is associated with your categorical factor.
13. Translate a significant association into a testable process hypothesis — association is not causation, but it does tell you where to look.

## The GenAI Prompt

Copy the prompt in [prompt.txt](prompt.txt) into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details, then CHECK the answer against your own working — the tool is right, the AI is not always.

## Self-Check — Is Your Output Finished?

Your multi-vari chart captures all three families with quantified variance contributions, your cause list is re-prioritised against the dominant family, and your chi-square satisfies the expected-frequency condition.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Files in this folder: [scenario.md](scenario.md) · [worksheet.md](worksheet.md) (and worksheet.pdf) · `lab-20-multivari-chisquare.xlsx` · [debrief.md](debrief.md) (TRAINER) · [prompt.txt](prompt.txt)*

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
