<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Lab 13 — Nested and Destructive Gauge Studies (Black Belt Only)

**MEASURE** · Design a valid MSA when parts cannot be measured repeatedly (A4, K2).

| Field | Detail |
|---|---|
| Case study | Meridian Medical Devices — seal weld burst pressure |
| DMAIC phase | MEASURE |
| Lab type | Core |
| Deliverable | A nested gauge study design and analysis for a destructive or single-measurement test. |
| Tools | Nested vs crossed designs, destructive testing MSA, homogeneous batches, part-to-part confounding, variance components |
| Data file | `lab-13-nested-destructive-gauge.xlsx` |

---

## The Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## The Evidence

**`lab-13-nested-destructive-gauge.xlsx`** — *Dataset.* Nested (hierarchical) MSA for a DESTRUCTIVE burst test — each specimen can only be measured once, so operators measure different specimens from the same batch.

| Sheet | What it contains | Rows |
|---|---|---|
| NestedMSA | Operators are nested within batch — specimens are NOT shared. | 60 |

Open the workbook from this folder. Every workbook opens on a **Data Dictionary** sheet defining each column, its unit and the specification limits — read it before you analyse anything.

> Use your OWN workplace data wherever you can obtain it. The workbook is the fallback, and it describes the same Meridian process as every other lab, so your figures reconcile across labs.

## Step-by-Step

1. State precisely why a crossed design is invalid for destructive tests: the part no longer exists to be measured a second time.
2. Identify a destructive or non-repeatable measurement in your capstone — or use the Meridian seal-strength test on infusion pump tubing.
3. Understand the nested design: each operator measures DIFFERENT parts, and parts are nested within batch rather than crossed with operator.
4. Establish homogeneous batches. The design assumes parts within a batch are effectively identical — if they are not, part variation contaminates repeatability.
5. Justify batch homogeneity: same lot, same machine, same setup, consecutive production, minimal elapsed time.
6. Design the study: 3 operators, 10 batches, 3 parts per operator per batch, all parts within a batch treated as replicates.
7. Run the study and record results in the nested layout — operator within batch, not operator crossed with part.
8. Compute variance components for repeatability and reproducibility using the nested model. Note that repeatability is now confounded with within-batch part variation.
9. State that confounding explicitly in your report. A nested study OVERSTATES repeatability variation, so it is a conservative test.
10. Decide accept/reject, and record the design choice and its rationale for the Day 5 presentation — expect this to be challenged.

## The GenAI Prompt

Copy the prompt in [prompt.txt](prompt.txt) into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details, then CHECK the answer against your own working — the tool is right, the AI is not always.

## Self-Check — Is Your Output Finished?

You can explain why a crossed study is invalid for your measurement, your batches are justified as homogeneous, and your report states the repeatability/part-variation confounding explicitly.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Files in this folder: [scenario.md](scenario.md) · [worksheet.md](worksheet.md) (and worksheet.pdf) · `lab-13-nested-destructive-gauge.xlsx` · [debrief.md](debrief.md) (TRAINER) · [prompt.txt](prompt.txt)*

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
