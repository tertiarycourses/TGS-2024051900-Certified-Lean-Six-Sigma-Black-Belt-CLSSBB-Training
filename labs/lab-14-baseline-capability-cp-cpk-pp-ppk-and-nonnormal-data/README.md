# Lab 14 — Baseline Capability — Cp, Cpk, Pp, Ppk and Non-Normal Data

**DMAIC phase:** MEASURE  |  **Lab type:** Core  |  **Course:** Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900)

## Objective

Establish baseline capability for your capstone, handling non-normal data correctly (A4, K2).

## Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## What you will build

A baseline capability study for your capstone Y with a documented normality decision.

**Tools and techniques:** Cp, Cpk, Pp, Ppk, within vs overall variation, normality testing, Box-Cox transformation, non-normal capability

## Data files in this folder

- **`lab-14-baseline-capability.xlsx`** — *Dataset.* 250 baseline burst-pressure readings in 50 subgroups of 5 (normal), plus 200 right-skewed leak-test cycle times for the non-normal capability exercise.

Open the workbook from THIS lab's folder. Every workbook has a **`Data Dictionary`** sheet that defines each column, its unit and its specification limits — read it before you analyse anything.

> The data describes the same Meridian Medical Devices seal-weld process used by every other lab, so the figures you compute here agree with the ones you computed earlier. Use your OWN workplace data instead wherever you can obtain it — the workbook is the fallback.

## Steps

### Step 1

Recap capability in full: Cp = (USL - LSL) / 6 sigma measures spread only; Cpk also accounts for centring and is always <= Cp.

### Step 2

Recap the acceptance benchmarks: Cpk >= 1.33 capable, >= 1.67 for critical characteristics, and the relationship between Cpk and sigma level.

### Step 3

Learn the distinction most practitioners get wrong: Cp/Cpk use WITHIN-subgroup (short-term) variation; Pp/Ppk use TOTAL (long-term) variation.

### Step 4

Understand the consequence: reporting Cpk on an unstable process flatters it, because between-subgroup drift is excluded from the estimate.

### Step 5

Establish the rule — the process must be STABLE before capability means anything. Check stability with a control chart first.

### Step 6

Test your capstone Y for normality using Anderson-Darling or Shapiro-Wilk. Read the p-value: p < 0.05 rejects normality.

### Step 7

Recognise that cycle time, waiting time and defect counts are routinely non-normal and usually right-skewed — this is expected, not an error.

### Step 8

For non-normal data, choose your route: apply a Box-Cox or Johnson transformation, or fit the correct distribution (Weibull, lognormal, exponential) directly.

### Step 9

Apply the transformation, re-test normality, then compute capability on the transformed scale — and report results in the ORIGINAL units.

### Step 10

Calculate both Cpk and Ppk for your capstone Y and explain the gap between them. A large gap means the process drifts between subgroups.

### Step 11

Record the baseline capability in your capstone pack alongside the Lab 3 sigma level.

## Check your work

You have confirmed stability before computing capability, tested and documented normality with a p-value, handled non-normality by transformation or distribution fitting, and reported both Cpk and Ppk with an explanation of the gap.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
