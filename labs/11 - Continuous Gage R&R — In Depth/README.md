<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Lab 11 — Continuous Gage R&R — In Depth

**MEASURE** · Validate a continuous measurement system for your capstone using Gage R&R (A4).

| Field | Detail |
|---|---|
| Case study | Meridian Medical Devices — seal weld burst pressure |
| DMAIC phase | MEASURE |
| Lab type | Core |
| Deliverable | A completed crossed Gage R&R study with %study variation and ndc for your capstone metric. |
| Tools | Accuracy, bias, linearity, stability, repeatability, reproducibility, %study variation, ndc, %tolerance |
| Data file | `lab-11-gage-rr-continuous.xlsx` |

---

## The Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## The Evidence

**`lab-11-gage-rr-continuous.xlsx`** — *Dataset.* Crossed Gage R&R: 10 parts x 3 operators x 3 trials on the burst-pressure rig. The study is built to FAIL — find out why before you trust any other data.

| Sheet | What it contains | Rows |
|---|---|---|
| GageRR | Crossed design, 90 measurements. Parts span the production range. | 90 |

Open the workbook from this folder. Every workbook opens on a **Data Dictionary** sheet defining each column, its unit and the specification limits — read it before you analyse anything.

> Use your OWN workplace data wherever you can obtain it. The workbook is the fallback, and it describes the same Meridian process as every other lab, so your figures reconcile across labs.

## Step-by-Step

1. Recap the components of measurement variation in full: observed variation = actual process variation + measurement system variation.
2. Recap the five MSA properties: accuracy (bias), linearity, stability, repeatability (equipment) and reproducibility (operator).
3. Distinguish repeatability from reproducibility precisely — same operator repeating, versus different operators on the same part.
4. Design a crossed Gage R&R for your capstone metric: 10 parts spanning the full process range, 3 operators, 3 repeat measurements each.
5. Select parts that span the real range of production. Parts clustered near the mean will flatter the gauge and hide its weakness.
6. Randomise the measurement order and blind the operators to previous readings, or you will measure memory rather than the gauge.
7. Run the study and record all 90 measurements in the standard crossed layout.
8. Calculate %study variation for repeatability, reproducibility and total Gage R&R. Apply the acceptance rule: under 10% acceptable, 10-30% marginal, over 30% unacceptable.
9. Calculate the number of distinct categories (ndc). ndc must be 5 or more for the gauge to distinguish parts usefully.
10. If the gauge fails, decide the fix: recalibrate, retrain operators, tighten the operational definition or replace the instrument. Then re-run.

## The GenAI Prompt

Copy the prompt in [prompt.txt](prompt.txt) into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details, then CHECK the answer against your own working — the tool is right, the AI is not always.

## Self-Check — Is Your Output Finished?

Your study uses parts spanning the full process range with randomised blinded order, and you have computed %study variation and ndc with a stated accept/reject decision.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Files in this folder: [scenario.md](scenario.md) · [worksheet.md](worksheet.md) (and worksheet.pdf) · `lab-11-gage-rr-continuous.xlsx` · [debrief.md](debrief.md) (TRAINER) · [prompt.txt](prompt.txt)*

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
