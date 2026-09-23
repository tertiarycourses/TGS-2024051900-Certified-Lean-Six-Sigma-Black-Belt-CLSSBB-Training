<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Lab 9 — Data Types, Operational Definitions and the Data Collection Plan

**MEASURE** · Build a rigorous data collection plan for your capstone (A4).

| Field | Detail |
|---|---|
| Case study | Meridian Medical Devices — seal weld burst pressure |
| DMAIC phase | MEASURE |
| Lab type | Core |
| Deliverable | A data collection plan with operational definitions for every metric in your capstone. |
| Tools | Continuous vs discrete, nominal/ordinal/interval/ratio, operational definitions, data collection plan, stratification factors |
| Data file | `lab-09-data-collection-raw-extract.xlsx` |

---

## The Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## The Evidence

**`lab-09-data-collection-raw-extract.xlsx`** — *Dataset.* Raw 240-row MES extract of seal weld burst-pressure tests — deliberately messy, so you can write operational definitions that fix it.

| Sheet | What it contains | Rows |
|---|---|---|
| RawExtract | Direct MES export, 240 tests, March 2026. Not cleaned. | 240 |

Open the workbook from this folder. Every workbook opens on a **Data Dictionary** sheet defining each column, its unit and the specification limits — read it before you analyse anything.

> Use your OWN workplace data wherever you can obtain it. The workbook is the fallback, and it describes the same Meridian process as every other lab, so your figures reconcile across labs.

## Step-by-Step

1. Recap the data hierarchy in full: nominal, ordinal, interval and ratio — and why the type determines which statistical test is legal.
2. Recap continuous versus discrete (attribute) data, and why continuous data needs far smaller samples to reach the same confidence.
3. List every metric your capstone requires: the project Y, each sub-Y from your flowdown, and each candidate X you intend to test.
4. Classify each metric by data type. Flag any metric currently collected as attribute that could be captured as continuous — convert it if you can.
5. Write a complete operational definition for each metric: what is measured, the instrument, the unit, the sampling point, the collector and the defect criterion.
6. Test each operational definition by having two people apply it independently to the same item. If they disagree, the definition is not yet operational.
7. Identify your stratification factors — plant, line, shift, operator, product family, supplier. You must capture these at collection time or you can never stratify later.
8. Build the data collection plan table: metric, definition, type, source, sample size, frequency, collector, stratification fields and start date.
9. Design the check sheet or data form. Make the easy path the correct path, or collectors will improvise.
10. Dry-run the plan on a small batch and fix whatever breaks before committing to full collection.

## The GenAI Prompt

Copy the prompt in [prompt.txt](prompt.txt) into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details, then CHECK the answer against your own working — the tool is right, the AI is not always.

## Self-Check — Is Your Output Finished?

Every capstone metric has a written operational definition that two people apply identically, stratification fields are captured at source, and the plan has survived a dry run.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Files in this folder: [scenario.md](scenario.md) · [worksheet.md](worksheet.md) (and worksheet.pdf) · `lab-09-data-collection-raw-extract.xlsx` · [debrief.md](debrief.md) (TRAINER) · [prompt.txt](prompt.txt)*

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
