<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Lab 23 — Full Factorial Design of Experiments (Black Belt Only)

**IMPROVE** · Design, run and analyse a full factorial experiment on your capstone process (A3, A5, K2).

| Field | Detail |
|---|---|
| Case study | Meridian Medical Devices — seal weld burst pressure |
| DMAIC phase | IMPROVE |
| Lab type | Core |
| Deliverable | A designed 2^k full factorial experiment with main effects and interaction analysis. |
| Tools | OFAT vs DOE, 2^k factorial, factors & levels, randomisation, replication, blocking, main effects, interaction plots, effect significance |
| Data file | `lab-23-full-factorial-doe.xlsx` |

---

## The Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## The Evidence

**`lab-23-full-factorial-doe.xlsx`** — *Dataset.* A replicated 2^3 full factorial (16 runs) on clamp pressure, dwell time and ambient temperature — run order already randomised.

| Sheet | What it contains | Rows |
|---|---|---|
| FullFactorial | 2^3 x 2 replicates. Coded and uncoded levels both given. | 16 |

Open the workbook from this folder. Every workbook opens on a **Data Dictionary** sheet defining each column, its unit and the specification limits — read it before you analyse anything.

> Use your OWN workplace data wherever you can obtain it. The workbook is the fallback, and it describes the same Meridian process as every other lab, so your figures reconcile across labs.

## Step-by-Step

1. Understand why OFAT fails: it cannot detect interactions at all, and it requires more runs for less information than a factorial design.
2. Recap the DOE vocabulary in full: factor, level, response, run, effect, interaction, replication, randomisation, blocking and experimental error.
3. Select 3 factors from your capstone that you can actually control and vary — temperature, speed, pressure, batch size, staffing level or method variant.
4. Set two levels for each factor — low (-1) and high (+1). Set them wide enough to produce a detectable effect but within safe operating limits.
5. Build the 2^3 design matrix: 8 runs covering every combination of the three factors, in standard order.
6. Decide replication. Replicates give an estimate of pure experimental error and let you test effect significance — 2 replicates gives 16 runs.
7. RANDOMISE the run order. Randomisation protects against unknown time-varying nuisance factors and is not optional.
8. Use blocking if runs must span shifts, days or material lots — block on the nuisance factor so it does not contaminate the effects.
9. Execute the experiment, holding all non-experimental factors constant and recording anything unexpected during each run.
10. Calculate main effects: the average response at the high level minus the average at the low level, for each factor.
11. Calculate interaction effects for AB, AC, BC and the three-way ABC.
12. Plot main effects (steeper slope means larger effect) and interaction plots (non-parallel lines mean interaction present).
13. Test effect significance using a Pareto of effects or a normal probability plot of effects — points off the line are real effects.
14. Build the prediction equation from the significant effects and identify the factor settings that optimise your Y.
15. Run confirmation trials at the predicted optimum. If the confirmation fails, the model is missing something — do not roll out.

## The GenAI Prompt

Copy the prompt in [prompt.txt](prompt.txt) into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details, then CHECK the answer against your own working — the tool is right, the AI is not always.

## Self-Check — Is Your Output Finished?

Your design is fully randomised with replication, you have computed and plotted both main effects and interactions, effect significance is assessed statistically, and confirmation runs validate the predicted optimum.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Files in this folder: [scenario.md](scenario.md) · [worksheet.md](worksheet.md) (and worksheet.pdf) · `lab-23-full-factorial-doe.xlsx` · [debrief.md](debrief.md) (TRAINER) · [prompt.txt](prompt.txt)*

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
