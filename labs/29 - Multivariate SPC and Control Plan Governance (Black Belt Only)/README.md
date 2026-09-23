<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Lab 29 — Multivariate SPC and Control Plan Governance (Black Belt Only)

**CONTROL** · Monitor correlated characteristics with Hotelling's T-squared and govern control plans (A5, K1).

| Field | Detail |
|---|---|
| Case study | Meridian Medical Devices — seal weld burst pressure |
| DMAIC phase | CONTROL |
| Lab type | Core |
| Deliverable | A Hotelling T-squared chart plus a governed control plan for your capstone. |
| Tools | Multivariate SPC, Hotelling T-squared, correlation structure, false alarm inflation, control plan, response plan, audit cadence |
| Data file | `lab-29-multivariate-spc-control-plan.xlsx` |

---

## The Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## The Evidence

**`lab-29-multivariate-spc-control-plan.xlsx`** — *Dataset.* 50 paired clamp/dwell readings where the two variables are normally correlated — plus the project's draft control plan to govern.

| Sheet | What it contains | Rows |
|---|---|---|
| MultivariateData | Two correlated process variables, 50 observations. | 50 |
| ControlPlan | The draft control plan — audit it and fill the gaps. | 5 |

Open the workbook from this folder. Every workbook opens on a **Data Dictionary** sheet defining each column, its unit and the specification limits — read it before you analyse anything.

> Use your OWN workplace data wherever you can obtain it. The workbook is the fallback, and it describes the same Meridian process as every other lab, so your figures reconcile across labs.

## Step-by-Step

1. Understand the false alarm problem: 5 separate charts each at alpha = 0.0027 gives a combined false alarm rate over 1.3 percent — five times intended.
2. Understand the more serious failure: two characteristics can each sit within their own limits while their COMBINATION is impossible, and separate charts will never see it.
3. Identify a set of correlated characteristics in your capstone — dimensions on one part, or related cycle times across linked steps.
4. Compute the correlation matrix and confirm the characteristics are genuinely correlated. If they are independent, separate charts are fine.
5. Learn Hotelling's T-squared: it collapses several correlated characteristics into one statistic accounting for the covariance structure.
6. Build the T-squared chart with its upper control limit from the F-distribution, and note there is no lower limit — T-squared is always positive.
7. Understand the interpretation difficulty: a T-squared signal tells you something is wrong but not which variable. Use decomposition or individual charts as a follow-up diagnostic.
8. Now build your capstone control plan in full: for each critical X and the Y — the metric, target, specification, measurement method, sample size, frequency, chart type, owner and reaction plan.
9. Write the reaction plan for each metric as a specific instruction: containment action, escalation path, named owner and time limit. 'Investigate' is not a reaction plan.
10. Add the control plan to the process documentation and update the SOP, training material and visual management boards.
11. Step up to portfolio governance: as Black Belt you audit control plans across multiple projects. Define your audit cadence and criteria.
12. Define what a control plan audit checks: is the chart still being maintained, are signals being actioned, is the owner still in post, and has the process drifted since handover?
13. Identify the most common decay mode — charts maintained but signals never actioned — and write your countermeasure for it.

## The GenAI Prompt

Copy the prompt in [prompt.txt](prompt.txt) into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details, then CHECK the answer against your own working — the tool is right, the AI is not always.

## Self-Check — Is Your Output Finished?

Your correlated characteristics are confirmed by a correlation matrix before applying T-squared, every control plan metric has a specific named reaction plan, and you have defined an audit cadence with explicit criteria.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Files in this folder: [scenario.md](scenario.md) · [worksheet.md](worksheet.md) (and worksheet.pdf) · `lab-29-multivariate-spc-control-plan.xlsx` · [debrief.md](debrief.md) (TRAINER) · [prompt.txt](prompt.txt)*

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
