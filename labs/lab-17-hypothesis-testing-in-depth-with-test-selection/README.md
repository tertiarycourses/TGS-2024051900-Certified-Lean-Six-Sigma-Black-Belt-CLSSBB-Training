# Lab 17 — Hypothesis Testing — In Depth, With Test Selection

**DMAIC phase:** ANALYZE  |  **Lab type:** Core  |  **Course:** Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900)

## Objective

Test your capstone's candidate causes with correctly selected hypothesis tests (A3, K2).

## Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## What you will build

Completed hypothesis tests on your capstone's candidate causes with documented conclusions.

**Tools and techniques:** H0/Ha, alpha, beta, power, p-values, t-tests, paired t, F-test, proportion tests, test selection logic

## Data files in this folder

- **`lab-17-hypothesis-testing.xlsx`** — *Dataset.* Three tests on one sheet each: a 2-sample t (old vs new fixture), a paired t (before/after operator re-training) and a 2-proportion test (defect rates by plant).

Open the workbook from THIS lab's folder. Every workbook has a **`Data Dictionary`** sheet that defines each column, its unit and its specification limits — read it before you analyse anything.

> The data describes the same Meridian Medical Devices seal-weld process used by every other lab, so the figures you compute here agree with the ones you computed earlier. Use your OWN workplace data instead wherever you can obtain it — the workbook is the fallback.

## Steps

### Step 1

Recap the logic of hypothesis testing in full: assume H0 (no difference), then ask how likely the observed data would be if H0 were true.

### Step 2

Recap H0 and Ha formulation. H0 always contains the equality; Ha carries the claim you are trying to establish.

### Step 3

Recap alpha, beta and power. Alpha is producer's risk (Type I, false alarm); beta is consumer's risk (Type II, missed signal); power = 1 - beta.

### Step 4

Understand the practical consequence: an underpowered test that fails to reject H0 has proven nothing. Check power before concluding 'no difference'.

### Step 5

Learn the test selection logic in full. Continuous Y: 1 sample vs target = 1-sample t; 2 independent groups = 2-sample t; paired = paired t; 3+ groups = ANOVA; variances = F-test or Levene.

### Step 6

Learn the discrete-Y branch: 1 proportion = 1-proportion test; 2 proportions = 2-proportion test; categorical association = chi-square.

### Step 7

Check the assumptions before every test: normality, independence and equal variance. A violated assumption invalidates the p-value entirely.

### Step 8

Take your five candidate causes from Lab 16 and select the correct test for each. Write down the justification for each selection.

### Step 9

State H0 and Ha for each test, set alpha (normally 0.05), and confirm you have adequate sample size and power.

### Step 10

Run each test and record the p-value. Apply the decision rule: p < alpha rejects H0.

### Step 11

Distinguish statistical from PRACTICAL significance. A p-value of 0.001 on a 0.2 percent improvement is real but worthless — always report effect size alongside p.

### Step 12

Build your rejected-causes log so nobody re-litigates cleared causes in Improve, and record confirmed causes in your capstone pack.

## Check your work

Every test has a documented selection justification and assumption check, results report effect size alongside the p-value, and you maintain both a confirmed-cause and a rejected-cause log.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
