<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Lab 10 — Sampling Strategy, Sample Size and Rational Subgrouping

**MEASURE** · Determine defensible sample sizes and design rational subgroups for your capstone (A4).

| Field | Detail |
|---|---|
| Case study | Meridian Medical Devices — seal weld burst pressure |
| DMAIC phase | MEASURE |
| Lab type | Core |
| Deliverable | Calculated sample sizes for your capstone metrics and a rational subgrouping scheme. |
| Tools | Random/stratified/systematic/cluster sampling, sample size for continuous & discrete data, rational subgrouping, sampling bias |
| Data file | `lab-10-sampling-frame.xlsx` |

---

## The Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## The Evidence

**`lab-10-sampling-frame.xlsx`** — *Dataset.* A 600-unit population frame for one month — draw random, stratified, systematic and cluster samples from it and compare what each one tells you.

| Sheet | What it contains | Rows |
|---|---|---|
| PopulationFrame | Every unit produced in April 2026 — the frame you sample FROM. | 600 |

Open the workbook from this folder. Every workbook opens on a **Data Dictionary** sheet defining each column, its unit and the specification limits — read it before you analyse anything.

> Use your OWN workplace data wherever you can obtain it. The workbook is the fallback, and it describes the same Meridian process as every other lab, so your figures reconcile across labs.

## Step-by-Step

1. Recap the four sampling schemes in full: simple random, stratified, systematic and cluster — with the failure mode of each.
2. Identify the sampling bias risks in your capstone: convenience sampling, day-shift-only sampling, and sampling only when the process is running well.
3. Recap the continuous-data sample size formula n = (1.96 s / d)^2, where s is the estimated standard deviation and d is the precision you require.
4. Apply it to your project Y. Estimate s from historical data or a pilot sample, choose your required precision d, and calculate n.
5. Recap the discrete-data formula n = (1.96/d)^2 x p(1-p), where p is the estimated proportion defective.
6. Apply it to your attribute metrics. Note how much larger n becomes — this is the cost of measuring in pass/fail.
7. Now design rational subgroups. A subgroup must contain only common-cause variation, so that between-subgroup variation shows up as a signal.
8. Decide what varies WITHIN your subgroup and what varies BETWEEN subgroups. Getting this backwards makes control limits so wide that nothing ever signals.
9. Set subgroup size and sampling frequency for your capstone Y, and state what shift size you would be able to detect.
10. Document the sampling plan and check it against the data collection plan from Lab 9 for consistency.

## The GenAI Prompt

Copy the prompt in [prompt.txt](prompt.txt) into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details, then CHECK the answer against your own working — the tool is right, the AI is not always.

## Self-Check — Is Your Output Finished?

Your sample sizes are calculated from a real estimate of s or p, your subgrouping scheme places common-cause variation within subgroups, and you can state the shift size your plan can detect.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Files in this folder: [scenario.md](scenario.md) · [worksheet.md](worksheet.md) (and worksheet.pdf) · `lab-10-sampling-frame.xlsx` · [debrief.md](debrief.md) (TRAINER) · [prompt.txt](prompt.txt)*

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
