# Lab 19 — ANOVA, Interactions and Non-Parametric Tests (Black Belt Only)

**DMAIC phase:** ANALYZE  |  **Lab type:** Core  |  **Course:** Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900)

## Objective

Compare multiple groups using ANOVA and apply non-parametric alternatives (A3, K2).

## Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## What you will build

One-way and two-way ANOVA on your capstone data plus a non-parametric confirmation.

**Tools and techniques:** One-way ANOVA, F-statistic, post-hoc Tukey, two-way ANOVA, interaction effects, Mann-Whitney, Kruskal-Wallis, Mood's median

## Data files in this folder

- **`lab-19-anova-interactions-nonparametric.xlsx`** — *Dataset.* One-way ANOVA across four seal-ring suppliers, a two-way ANOVA (plant x shift) containing a genuine interaction, and skewed data for Kruskal-Wallis.

Open the workbook from THIS lab's folder. Every workbook has a **`Data Dictionary`** sheet that defines each column, its unit and its specification limits — read it before you analyse anything.

> The data describes the same Meridian Medical Devices seal-weld process used by every other lab, so the figures you compute here agree with the ones you computed earlier. Use your OWN workplace data instead wherever you can obtain it — the workbook is the fallback.

## Steps

### Step 1

Understand alpha inflation: comparing 4 groups pairwise needs 6 t-tests, and at alpha = 0.05 the family-wise false-positive risk rises to about 26 percent.

### Step 2

Recap one-way ANOVA: it partitions total variation into between-group and within-group components, and the F-statistic is their ratio.

### Step 3

State the ANOVA hypotheses: H0 is that all group means are equal; Ha is that at least one differs — ANOVA does not tell you which.

### Step 4

Check the ANOVA assumptions: normality of residuals, independence, and equal variances (test with Levene's or Bartlett's).

### Step 5

Run one-way ANOVA on a capstone factor with 3+ levels — plant, line, shift, product family or supplier.

### Step 6

If ANOVA is significant, run a post-hoc Tukey HSD to identify WHICH pairs differ, with the family-wise error rate controlled.

### Step 7

Extend to two-way ANOVA with two factors at once — for example plant AND shift on your capstone Y.

### Step 8

Read the interaction term. A significant interaction means the effect of one factor DEPENDS on the level of the other — for instance night shift hurts Suzhou but not Singapore.

### Step 9

Plot the interaction. Non-parallel lines indicate interaction; crossing lines indicate a strong one that invalidates any single-factor conclusion.

### Step 10

Understand why this matters for Improve: with a significant interaction, a fix that works at one plant may fail or backfire at another.

### Step 11

Now the non-parametric branch. When normality fails and transformation does not fix it, switch tests rather than ignoring the violation.

### Step 12

Map each test to its non-parametric equivalent: 2-sample t -> Mann-Whitney; one-way ANOVA -> Kruskal-Wallis; paired t -> Wilcoxon signed-rank; and Mood's median for heavy outliers.

### Step 13

Re-run one of your significant findings using its non-parametric equivalent. Agreement across both strengthens your Day 5 defence considerably.

## Check your work

Your ANOVA assumptions are tested and documented, significant results carry a post-hoc analysis, you have interpreted an interaction plot, and at least one finding is confirmed non-parametrically.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
