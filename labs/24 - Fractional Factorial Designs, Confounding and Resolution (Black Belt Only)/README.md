<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Lab 24 — Fractional Factorial Designs, Confounding and Resolution (Black Belt Only)

**IMPROVE** · Screen many factors efficiently and interpret confounded effects correctly (A3, K2).

| Field | Detail |
|---|---|
| Case study | Meridian Medical Devices — seal weld burst pressure |
| DMAIC phase | IMPROVE |
| Lab type | Core |
| Deliverable | A fractional factorial screening design with a documented confounding structure. |
| Tools | 2^(k-p) designs, generators, defining relation, alias structure, confounding, Resolution III/IV/V, screening, fold-over designs |
| Data file | `lab-24-fractional-factorial-doe.xlsx` |

---

## The Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## The Evidence

**`lab-24-fractional-factorial-doe.xlsx`** — *Dataset.* A 2^(5-1) resolution V fractional factorial — 16 runs instead of 32, five factors, generator E = ABCD.

| Sheet | What it contains | Rows |
|---|---|---|
| FractionalFactorial | 16 runs, 5 factors, randomised order. | 16 |

Open the workbook from this folder. Every workbook opens on a **Data Dictionary** sheet defining each column, its unit and the specification limits — read it before you analyse anything.

> Use your OWN workplace data wherever you can obtain it. The workbook is the fallback, and it describes the same Meridian process as every other lab, so your figures reconcile across labs.

## Step-by-Step

1. Understand the economics: 2^7 full factorial = 128 runs; a 2^(7-4) fractional = 16 runs. The saving is real but it is paid for in resolving power.
2. Understand confounding (aliasing): in a fractional design, some effects are mathematically indistinguishable from others.
3. Learn the generator and defining relation — the algebra that determines exactly which effects are aliased with which.
4. Learn the resolution scale precisely. RESOLUTION III: main effects aliased with two-factor interactions. RESOLUTION IV: main effects clear of two-factor interactions, but two-factor interactions aliased with each other. RESOLUTION V: main effects and two-factor interactions all clear.
5. Understand the selection rule: use Resolution III only for early screening of many factors; use IV or V when you intend to interpret interactions.
6. Select 5 or more candidate factors from your capstone for a screening experiment.
7. Choose your fraction based on your run budget, and write down the resulting resolution BEFORE running anything.
8. Generate the design matrix and write out the complete alias structure. You must be able to state what each estimated effect is confounded with.
9. Apply effect sparsity and hierarchy: usually few factors dominate, and low-order effects are more likely to be real than high-order ones.
10. Randomise and execute the screening experiment.
11. Analyse the effects and identify the vital few factors. Where an important effect is confounded, state the ambiguity explicitly rather than assuming the main effect is the real one.
12. Resolve critical ambiguity with a fold-over design — a second fraction that de-aliases the effects you care about.
13. Take the screened vital few factors forward to a full factorial or RSM study in Lab 25.

## The GenAI Prompt

Copy the prompt in [prompt.txt](prompt.txt) into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details, then CHECK the answer against your own working — the tool is right, the AI is not always.

## Self-Check — Is Your Output Finished?

You stated the design resolution before running, wrote out the complete alias structure, and any ambiguous conclusion is either declared explicitly or resolved by a fold-over.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Files in this folder: [scenario.md](scenario.md) · [worksheet.md](worksheet.md) (and worksheet.pdf) · `lab-24-fractional-factorial-doe.xlsx` · [debrief.md](debrief.md) (TRAINER) · [prompt.txt](prompt.txt)*

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
