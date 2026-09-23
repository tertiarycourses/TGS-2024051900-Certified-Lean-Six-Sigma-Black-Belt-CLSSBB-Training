<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Team Worksheet — Lab 19

## ANOVA, Interactions and Non-Parametric Tests (Black Belt Only)

**Team members:** ____________________________________________  
**Date:** ____________________

---

### 1. Our understanding of the problem

____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________

### 2. Our working

*Use the data in `lab-19-anova-interactions-nonparametric.xlsx`.*

____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________

### 3. What we produced

*Deliverable: One-way and two-way ANOVA on your capstone data plus a non-parametric confirmation.*

____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________

### 4. What the evidence does NOT tell us

____________________________________________________________________________________

____________________________________________________________________________________

### 5. Our conclusion

____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________

### 6. Step notes

**Step 1.** Understand alpha inflation: comparing 4 groups pairwise needs 6 t-tests, and at alpha = 0.05 the family-wise false-positive risk rises to about 26 percent.

____________________________________________________________________________________

**Step 2.** Recap one-way ANOVA: it partitions total variation into between-group and within-group components, and the F-statistic is their ratio.

____________________________________________________________________________________

**Step 3.** State the ANOVA hypotheses: H0 is that all group means are equal; Ha is that at least one differs — ANOVA does not tell you which.

____________________________________________________________________________________

**Step 4.** Check the ANOVA assumptions: normality of residuals, independence, and equal variances (test with Levene's or Bartlett's).

____________________________________________________________________________________

**Step 5.** Run one-way ANOVA on a capstone factor with 3+ levels — plant, line, shift, product family or supplier.

____________________________________________________________________________________

**Step 6.** If ANOVA is significant, run a post-hoc Tukey HSD to identify WHICH pairs differ, with the family-wise error rate controlled.

____________________________________________________________________________________

**Step 7.** Extend to two-way ANOVA with two factors at once — for example plant AND shift on your capstone Y.

____________________________________________________________________________________

**Step 8.** Read the interaction term. A significant interaction means the effect of one factor DEPENDS on the level of the other — for instance night shift hurts Suzhou but not Singapore.

____________________________________________________________________________________

**Step 9.** Plot the interaction. Non-parallel lines indicate interaction; crossing lines indicate a strong one that invalidates any single-factor conclusion.

____________________________________________________________________________________

**Step 10.** Understand why this matters for Improve: with a significant interaction, a fix that works at one plant may fail or backfire at another.

____________________________________________________________________________________

**Step 11.** Now the non-parametric branch. When normality fails and transformation does not fix it, switch tests rather than ignoring the violation.

____________________________________________________________________________________

**Step 12.** Map each test to its non-parametric equivalent: 2-sample t -> Mann-Whitney; one-way ANOVA -> Kruskal-Wallis; paired t -> Wilcoxon signed-rank; and Mood's median for heavy outliers.

____________________________________________________________________________________

**Step 13.** Re-run one of your significant findings using its non-parametric equivalent. Agreement across both strengthens your Day 5 defence considerably.

____________________________________________________________________________________

### 7. Self-check

Your ANOVA assumptions are tested and documented, significant results carry a post-hoc analysis, you have interpreted an interaction plot, and at least one finding is confirmed non-parametrically.

Complete?  ☐ Yes   ☐ Not yet

---

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
