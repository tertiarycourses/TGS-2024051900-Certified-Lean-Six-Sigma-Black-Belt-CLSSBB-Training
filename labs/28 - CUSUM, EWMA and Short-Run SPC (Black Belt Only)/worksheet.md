<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Team Worksheet — Lab 28

## CUSUM, EWMA and Short-Run SPC (Black Belt Only)

**Team members:** ____________________________________________  
**Date:** ____________________

---

### 1. Our understanding of the problem

____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________

### 2. Our working

*Use the data in `lab-28-cusum-ewma-shortrun.xlsx`.*

____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________

____________________________________________________________________________________

### 3. What we produced

*Deliverable: CUSUM and EWMA charts on your capstone data plus a short-run standardised chart.*

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

**Step 1.** Understand Average Run Length (ARL): the expected number of subgroups before a chart signals. For a 1-sigma shift, a Shewhart Xbar chart has an ARL around 44 — far too slow.

____________________________________________________________________________________

**Step 2.** Understand the structural reason: a Shewhart chart considers only the CURRENT point and has no memory of the recent past.

____________________________________________________________________________________

**Step 3.** Learn CUSUM: it accumulates deviations from target, so a small persistent bias adds up into a detectable signal rather than being repeatedly dismissed as noise.

____________________________________________________________________________________

**Step 4.** Set up the CUSUM parameters: the reference value k (typically half the shift you want to detect) and the decision interval h (typically 4 or 5 sigma).

____________________________________________________________________________________

**Step 5.** Build upper and lower CUSUM statistics for your capstone data and plot them against the decision interval.

____________________________________________________________________________________

**Step 6.** Compare the CUSUM detection point against the Shewhart chart from Lab 27 on the same data — CUSUM typically detects a sustained small shift several subgroups sooner.

____________________________________________________________________________________

**Step 7.** Learn EWMA: each point is a weighted average of all history, with weights decaying geometrically. Lambda controls the memory.

____________________________________________________________________________________

**Step 8.** Choose lambda deliberately: small lambda (0.1-0.2) gives long memory and strong small-shift detection; large lambda (0.4+) approaches Shewhart behaviour.

____________________________________________________________________________________

**Step 9.** Build the EWMA chart with its widening initial control limits, and note that EWMA also handles autocorrelated data far better than Shewhart.

____________________________________________________________________________________

**Step 10.** Test your capstone data for autocorrelation. Chemical, batch and continuous-flow processes are frequently autocorrelated, which makes Shewhart limits far too narrow and generates constant false alarms.

____________________________________________________________________________________

**Step 11.** Now short-run SPC. Understand the problem: high-mix low-volume processes never accumulate 25 subgroups of any single part number.

____________________________________________________________________________________

**Step 12.** Learn the deviation-from-nominal (DNOM) approach: plot (measurement - part nominal) so different part numbers share one chart.

____________________________________________________________________________________

**Step 13.** Learn the standardised approach for parts with differing variances: plot (measurement - nominal) / sigma_part, putting all parts on a common scale.

____________________________________________________________________________________

**Step 14.** Build a short-run chart for a multi-product step in your capstone, or for Meridian's shared assembly line across pump variants.

____________________________________________________________________________________

**Step 15.** Decide which chart type belongs in your capstone control plan and justify the choice against shift size, autocorrelation and product mix.

____________________________________________________________________________________

### 7. Self-check

You have built CUSUM and EWMA charts and compared their detection speed against Shewhart on the same data, tested for autocorrelation, and justified your final chart selection for the control plan.

Complete?  ☐ Yes   ☐ Not yet

---

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
