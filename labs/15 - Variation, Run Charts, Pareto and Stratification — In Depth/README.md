<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Lab 15 — Variation, Run Charts, Pareto and Stratification — In Depth

**ANALYZE** · Separate common from special cause variation and stratify your capstone data (A3).

| Field | Detail |
|---|---|
| Case study | Meridian Medical Devices — seal weld burst pressure |
| DMAIC phase | ANALYZE |
| Lab type | Core |
| Deliverable | A run chart with pattern analysis, a Pareto chart and a stratified defect analysis. |
| Tools | Common vs special cause, run chart patterns, tampering, Pareto principle, stratification, boxplots |
| Data file | `lab-15-run-chart-pareto-stratification.xlsx` |

---

## The Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## The Evidence

**`lab-15-run-chart-pareto-stratification.xlsx`** — *Dataset.* Three sheets: 60 daily Y averages for run-chart pattern analysis, a defect-mode Pareto count, and a plant/line/shift stratification table.

| Sheet | What it contains | Rows |
|---|---|---|
| RunChart | Daily mean burst pressure, 60 consecutive production days. | 60 |
| ParetoDefects | Warranty + in-process defect counts, last 12 months. | 8 |
| Stratification | Defect counts by plant x line x shift. | 54 |

Open the workbook from this folder. Every workbook opens on a **Data Dictionary** sheet defining each column, its unit and the specification limits — read it before you analyse anything.

> Use your OWN workplace data wherever you can obtain it. The workbook is the fallback, and it describes the same Meridian process as every other lab, so your figures reconcile across labs.

## Step-by-Step

1. Recap common versus special cause variation in full, with the management response each demands — process change versus local investigation.
2. Understand tampering (Deming's funnel): adjusting a stable process in response to common-cause noise increases variation. Demonstrate it with the bead or funnel experiment.
3. Plot your capstone Y as a run chart over time, with the median as the centre line.
4. Recap and apply the six run chart patterns in full: trend, shift, cluster, mixture, oscillation and bias — with the run rules that detect each.
5. Mark any special-cause signals and investigate what changed at that point in time. Special causes must be explained, not averaged away.
6. Recap the Pareto principle and build a Pareto chart of defect categories for your capstone, with the cumulative percentage line.
7. Identify the vital few categories accounting for roughly 80 percent of the impact. Weight by cost, not count, where defect costs differ materially.
8. Now stratify. Re-draw the Pareto separately by plant, line, shift, operator, product family and supplier.
9. Look for a stratification factor where the Pareto shape changes dramatically — that factor is a strong candidate X and tells you where to focus.
10. Build boxplots of your Y across each stratification factor to compare medians, spread and outliers visually before testing statistically.
11. Record your top three candidate Xs from stratification — these feed directly into the hypothesis tests in Lab 17.

## The GenAI Prompt

Copy the prompt in [prompt.txt](prompt.txt) into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details, then CHECK the answer against your own working — the tool is right, the AI is not always.

## Self-Check — Is Your Output Finished?

Your run chart is assessed against all six patterns, your Pareto is weighted appropriately, and stratification has produced at least three named candidate Xs for statistical testing.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Files in this folder: [scenario.md](scenario.md) · [worksheet.md](worksheet.md) (and worksheet.pdf) · `lab-15-run-chart-pareto-stratification.xlsx` · [debrief.md](debrief.md) (TRAINER) · [prompt.txt](prompt.txt)*

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
