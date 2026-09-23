<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Lab 3 — DMAIC at Depth — Recap, Y = f(X) and Baseline Sigma for Your Project

**FOUNDATIONS** · Re-derive the DMAIC roadmap and express your capstone as Y = f(X) with a baseline sigma level (K1, A4).

| Field | Detail |
|---|---|
| Case study | Meridian Medical Devices — seal weld burst pressure |
| DMAIC phase | FOUNDATIONS |
| Lab type | Core |
| Deliverable | A DMAIC tollgate map, a Y = f(X) model and a baseline DPMO / sigma level for your capstone. |
| Tools | DMAIC roadmap, tollgate deliverables, Y = f(X), DPU, DPO, DPMO, sigma level, sigma shift |
| Data file | `lab-03-baseline-sigma-calculator.xlsx` |

---

## The Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## The Evidence

**`lab-03-baseline-sigma-calculator.xlsx`** — *Template.* Twelve months of production and defect counts — compute DPU, DPO, DPMO, yield, RTY and the baseline sigma level for your project Y.

| Sheet | What it contains | Rows |
|---|---|---|
| MonthlyCounts | Actual production and defect counts. 4 defect opportunities per unit. | 12 |
| RTY | First-pass yield at each of the six process steps. | 6 |
| YfX | Decompose your project Y into candidate Xs. | 8 |

Open the workbook from this folder. Every workbook opens on a **Data Dictionary** sheet defining each column, its unit and the specification limits — read it before you analyse anything.

## Step-by-Step

1. Recap each DMAIC phase in full: its purpose, its core tools, its tollgate deliverable and the most common way teams fail in it.
2. For each phase, write the one question that phase answers — Define: what problem? Measure: how big? Analyze: why? Improve: what fix? Control: how do we hold it?
3. Write your capstone project Y — the single output metric your customer actually feels. It must be measurable and it must already have data.
4. Brainstorm at least twelve candidate Xs that could drive that Y. Classify each as controllable, noise or SOP-governed.
5. Write the relationship formally as Y = f(X1, X2, ... Xn), and mark which Xs you can experiment on later in the DOE labs.
6. Collect or estimate your baseline: units processed, defects observed and opportunities per unit over a defined recent period.
7. Calculate DPU, DPO and DPMO. Show the formulas: DPU = defects/units; DPO = defects/(units x opportunities); DPMO = DPO x 1,000,000.
8. Convert DPMO to a baseline sigma level using the conversion table, and state whether the 1.5-sigma long-term shift is included.
9. Record this baseline in your capstone pack — every improvement claim on Day 5 is measured against this number.

## The GenAI Prompt

Copy the prompt in [prompt.txt](prompt.txt) into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details, then CHECK the answer against your own working — the tool is right, the AI is not always.

## Self-Check — Is Your Output Finished?

You can explain all five DMAIC tollgates without notes, your Y is a measurable customer-facing output with at least twelve classified Xs, and your baseline DPMO and sigma level are calculated from real counts.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Files in this folder: [scenario.md](scenario.md) · [worksheet.md](worksheet.md) (and worksheet.pdf) · `lab-03-baseline-sigma-calculator.xlsx` · [debrief.md](debrief.md) (TRAINER) · [prompt.txt](prompt.txt)*

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
