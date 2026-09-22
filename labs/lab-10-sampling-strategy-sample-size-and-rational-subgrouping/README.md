# Lab 10 — Sampling Strategy, Sample Size and Rational Subgrouping

**DMAIC phase:** MEASURE  |  **Lab type:** Core  |  **Course:** Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900)

## Objective

Determine defensible sample sizes and design rational subgroups for your capstone (A4).

## Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## What you will build

Calculated sample sizes for your capstone metrics and a rational subgrouping scheme.

**Tools and techniques:** Random/stratified/systematic/cluster sampling, sample size for continuous & discrete data, rational subgrouping, sampling bias

## Data files in this folder

- **`lab-10-sampling-frame.xlsx`** — *Dataset.* A 600-unit population frame for one month — draw random, stratified, systematic and cluster samples from it and compare what each one tells you.

Open the workbook from THIS lab's folder. Every workbook has a **`Data Dictionary`** sheet that defines each column, its unit and its specification limits — read it before you analyse anything.

> The data describes the same Meridian Medical Devices seal-weld process used by every other lab, so the figures you compute here agree with the ones you computed earlier. Use your OWN workplace data instead wherever you can obtain it — the workbook is the fallback.

## Steps

### Step 1

Recap the four sampling schemes in full: simple random, stratified, systematic and cluster — with the failure mode of each.

### Step 2

Identify the sampling bias risks in your capstone: convenience sampling, day-shift-only sampling, and sampling only when the process is running well.

### Step 3

Recap the continuous-data sample size formula n = (1.96 s / d)^2, where s is the estimated standard deviation and d is the precision you require.

### Step 4

Apply it to your project Y. Estimate s from historical data or a pilot sample, choose your required precision d, and calculate n.

### Step 5

Recap the discrete-data formula n = (1.96/d)^2 x p(1-p), where p is the estimated proportion defective.

### Step 6

Apply it to your attribute metrics. Note how much larger n becomes — this is the cost of measuring in pass/fail.

### Step 7

Now design rational subgroups. A subgroup must contain only common-cause variation, so that between-subgroup variation shows up as a signal.

### Step 8

Decide what varies WITHIN your subgroup and what varies BETWEEN subgroups. Getting this backwards makes control limits so wide that nothing ever signals.

### Step 9

Set subgroup size and sampling frequency for your capstone Y, and state what shift size you would be able to detect.

### Step 10

Document the sampling plan and check it against the data collection plan from Lab 9 for consistency.

## Check your work

Your sample sizes are calculated from a real estimate of s or p, your subgrouping scheme places common-cause variation within subgroups, and you can state the shift size your plan can detect.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
