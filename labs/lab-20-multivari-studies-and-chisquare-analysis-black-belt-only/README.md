# Lab 20 — Multi-Vari Studies and Chi-Square Analysis (Black Belt Only)

**DMAIC phase:** ANALYZE  |  **Lab type:** Core  |  **Course:** Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900)

## Objective

Decompose variation by family using a multi-vari study and test categorical association (A3, K2).

## Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## What you will build

A multi-vari chart decomposing your capstone variation plus a chi-square association test.

**Tools and techniques:** Multi-vari studies, positional/cyclical/temporal families, variation decomposition, chi-square, contingency tables, expected frequencies

## Data files in this folder

- **`lab-20-multivari-chisquare.xlsx`** — *Dataset.* A multi-vari study sampling positional, cyclical and temporal families, plus a plant x defect-mode contingency table for chi-square.

Open the workbook from THIS lab's folder. Every workbook has a **`Data Dictionary`** sheet that defines each column, its unit and its specification limits — read it before you analyse anything.

> The data describes the same Meridian Medical Devices seal-weld process used by every other lab, so the figures you compute here agree with the ones you computed earlier. Use your OWN workplace data instead wherever you can obtain it — the workbook is the fallback.

## Steps

### Step 1

Understand the three variation families. POSITIONAL: within a single unit or across positions in a machine. CYCLICAL: unit to unit, batch to batch. TEMPORAL: shift to shift, day to day.

### Step 2

Understand the payoff: if 70 percent of variation is positional, then investigating shift patterns is wasted effort no matter how thorough the investigation.

### Step 3

Design a multi-vari sampling plan for your capstone: sample multiple positions within units, consecutive units, and repeat across time periods.

### Step 4

Ensure the sampling captures all three families simultaneously — this is a nested sampling design, not three separate studies.

### Step 5

Collect the data and plot the multi-vari chart, with positional variation innermost and temporal outermost.

### Step 6

Read the chart: the family showing the largest vertical spread dominates. That is where your root cause investigation should concentrate.

### Step 7

Quantify the contribution of each family as a percentage of total variation using variance components.

### Step 8

Re-prioritise your candidate cause list from Lab 16 against the dominant variation family, and drop causes that belong to a family contributing little.

### Step 9

Now chi-square. Build a contingency table of two categorical variables from your capstone — defect type against shift, supplier or line.

### Step 10

Calculate expected frequencies under independence: expected = (row total x column total) / grand total.

### Step 11

Check the validity condition: all expected frequencies should be 5 or more, or the chi-square approximation breaks down and categories must be combined.

### Step 12

Compute the chi-square statistic and its p-value, and conclude whether defect type is associated with your categorical factor.

### Step 13

Translate a significant association into a testable process hypothesis — association is not causation, but it does tell you where to look.

## Check your work

Your multi-vari chart captures all three families with quantified variance contributions, your cause list is re-prioritised against the dominant family, and your chi-square satisfies the expected-frequency condition.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
