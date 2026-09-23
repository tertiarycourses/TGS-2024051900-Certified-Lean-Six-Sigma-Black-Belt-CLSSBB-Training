<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Lab 19 — ANOVA, Interactions and Non-Parametric Tests (Black Belt Only)

**ANALYZE** · Compare multiple groups using ANOVA and apply non-parametric alternatives (A3, K2).

| Field | Detail |
|---|---|
| Case study | Meridian Medical Devices — seal weld burst pressure |
| DMAIC phase | ANALYZE |
| Lab type | Core |
| Deliverable | One-way and two-way ANOVA on your capstone data plus a non-parametric confirmation. |
| Tools | One-way ANOVA, F-statistic, post-hoc Tukey, two-way ANOVA, interaction effects, Mann-Whitney, Kruskal-Wallis, Mood's median |
| Data file | `lab-19-anova-interactions-nonparametric.xlsx` |

---

## The Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## The Evidence

**`lab-19-anova-interactions-nonparametric.xlsx`** — *Dataset.* One-way ANOVA across four seal-ring suppliers, a two-way ANOVA (plant x shift) containing a genuine interaction, and skewed data for Kruskal-Wallis.

| Sheet | What it contains | Rows |
|---|---|---|
| OneWay | Burst pressure by seal-ring supplier, 20 units each. | 80 |
| TwoWay | Balanced 3x3 design, 10 units per cell. | 90 |
| NonParametric | Rework cycle time by line — heavily skewed. | 75 |

Open the workbook from this folder. Every workbook opens on a **Data Dictionary** sheet defining each column, its unit and the specification limits — read it before you analyse anything.

> Use your OWN workplace data wherever you can obtain it. The workbook is the fallback, and it describes the same Meridian process as every other lab, so your figures reconcile across labs.

## Step-by-Step

1. Understand alpha inflation: comparing 4 groups pairwise needs 6 t-tests, and at alpha = 0.05 the family-wise false-positive risk rises to about 26 percent.
2. Recap one-way ANOVA: it partitions total variation into between-group and within-group components, and the F-statistic is their ratio.
3. State the ANOVA hypotheses: H0 is that all group means are equal; Ha is that at least one differs — ANOVA does not tell you which.
4. Check the ANOVA assumptions: normality of residuals, independence, and equal variances (test with Levene's or Bartlett's).
5. Run one-way ANOVA on a capstone factor with 3+ levels — plant, line, shift, product family or supplier.
6. If ANOVA is significant, run a post-hoc Tukey HSD to identify WHICH pairs differ, with the family-wise error rate controlled.
7. Extend to two-way ANOVA with two factors at once — for example plant AND shift on your capstone Y.
8. Read the interaction term. A significant interaction means the effect of one factor DEPENDS on the level of the other — for instance night shift hurts Suzhou but not Singapore.
9. Plot the interaction. Non-parallel lines indicate interaction; crossing lines indicate a strong one that invalidates any single-factor conclusion.
10. Understand why this matters for Improve: with a significant interaction, a fix that works at one plant may fail or backfire at another.
11. Now the non-parametric branch. When normality fails and transformation does not fix it, switch tests rather than ignoring the violation.
12. Map each test to its non-parametric equivalent: 2-sample t -> Mann-Whitney; one-way ANOVA -> Kruskal-Wallis; paired t -> Wilcoxon signed-rank; and Mood's median for heavy outliers.
13. Re-run one of your significant findings using its non-parametric equivalent. Agreement across both strengthens your Day 5 defence considerably.

## The GenAI Prompt

Copy the prompt in [prompt.txt](prompt.txt) into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details, then CHECK the answer against your own working — the tool is right, the AI is not always.

## Self-Check — Is Your Output Finished?

Your ANOVA assumptions are tested and documented, significant results carry a post-hoc analysis, you have interpreted an interaction plot, and at least one finding is confirmed non-parametrically.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Files in this folder: [scenario.md](scenario.md) · [worksheet.md](worksheet.md) (and worksheet.pdf) · `lab-19-anova-interactions-nonparametric.xlsx` · [debrief.md](debrief.md) (TRAINER) · [prompt.txt](prompt.txt)*

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
