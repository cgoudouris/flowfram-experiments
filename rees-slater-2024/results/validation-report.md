# Validation Report: Rees & Slater (2024) — Boil Water Advisory
## Scenario: base-configuration

**Total checks: 30 | Passed: 28 | Failed: 2**

| Metric | FlowFRAM | Recomputed | Abs Error | Rel Error % | Status |
|--------|----------|------------|-----------|-------------|--------|
| REI | 0.606811 | 0.606811 | 0.000000 | 0.0000% | ✅ PASS |
| REI_static+dynamic_sum | 0.606811 | 0.606811 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Coupling Network Entropy_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Temporal Consistency_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_System Activity Entropy_value | 0.129315 | 0.129315 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Aspect Entropy_value | 0.127497 | 0.127497 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Functional Resonance_value | 0.050000 | 0.050000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Entropy Synchronization_value | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Output Variability_value | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the heating time | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to boil water | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to set the target temperature | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the time it is allowed to stew | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to pour onto tea leaves | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to fill with a quantity of water | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to supply kettle | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Resonance_score_to boil water->to pour onto tea leaves | -0.500000 | -0.500000 | 0.000000 | 0.0000% | ✅ PASS |
| TE_net_to boil water->to pour onto tea leaves | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| TE_causal_confirmed_count | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| VPI | 1 | 0.500000 | 0.500000 | 50.0000% | ❌ FAIL |
| H_aspect_recomputed | 2.251629 | 2.251629 | 0.000000 | 0.0000% | ✅ PASS |
| ChainStrength_0_to boil water → to pour onto t | 1 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Damping_to pour onto tea leaves | 10 | 1.000000 | 9.000000 | 90.0000% | ❌ FAIL |
| System_ITD_recomputed | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CRI_top1_score | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| ES_amplification_factor | 1 | 1 | 0.000000 | 0.0000% | ✅ PASS |
| REI_nonlinear | 0.606811 | 0.606811 | 0.000000 | 0.0000% | ✅ PASS |
| REI_interaction_percent | 0.000000 | 0.000000 | 0.000000 | 0.0036% | ✅ PASS |
| EntropyRate_system | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMPERATURE | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |

*Generated: Python script independent recomputation*

---

# Validation Report: Rees & Slater (2024) — Boil Water Advisory
## Scenario: convergence-N100-normal-distribution-temperature

**Total checks: 34 | Passed: 33 | Failed: 1**

| Metric | FlowFRAM | Recomputed | Abs Error | Rel Error % | Status |
|--------|----------|------------|-----------|-------------|--------|
| REI | 0.643297 | 0.640834 | 0.002463 | 0.3829% | ✅ PASS |
| REI_static+dynamic_sum | 0.643297 | 0.640834 | 0.002463 | 0.3829% | ✅ PASS |
| Factor_Coupling Network Entropy_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Temporal Consistency_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_System Activity Entropy_value | 0.131341 | 0.131341 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Aspect Entropy_value | 0.102185 | 0.102185 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Functional Resonance_value | 0.100000 | 0.100000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Entropy Synchronization_value | 0.004681 | 0.004681 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Output Variability_value | 0.002627 | 0.002627 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the heating time | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to boil water | 0.453841 | 0.453841 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to set the target temperature | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the time it is allowed to stew | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to pour onto tea leaves | 11.913726 | 11.913726 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to fill with a quantity of water | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to supply kettle | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Resonance_score_to boil water->to pour onto tea leaves | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| TE_net_to boil water->to pour onto tea leaves | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| TE_causal_confirmed_count | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| VPI | 1 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| H_aspect_recomputed | 1.842371 | 1.842371 | 0.000000 | 0.0000% | ✅ PASS |
| ChainStrength_0_to boil water → to pour onto t | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Damping_to pour onto tea leaves | 10.000000 | 1.000000 | 9.000000 | 90.0000% | ❌ FAIL |
| System_ITD_recomputed | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CRI_top1_score | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| ES_amplification_factor | 1.009285 | 1.009285 | 0.000000 | 0.0000% | ✅ PASS |
| ES_convergence_iterations | 7.000000 | 7.000000 | 0.000000 | 0.0000% | ✅ PASS |
| REI_nonlinear | 0.643297 | 0.640834 | 0.002463 | 0.3829% | ✅ PASS |
| REI_interaction_percent | 0.384385 | 0.000000 | 0.384385 | 100.0000% | ✅ PASS |
| EntropyRate_system | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_QUANTITY_g | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_Capacity_J_gC | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMP_START_C | 129.194431 | 129.194431 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMPERATURE | 129.194431 | 129.194431 | 0.000000 | 0.0000% | ✅ PASS |

*Generated: Python script independent recomputation*

---

# Validation Report: Rees & Slater (2024) — Boil Water Advisory
## Scenario: convergence-N500-normal-distribution-temperature

**Total checks: 34 | Passed: 33 | Failed: 1**

| Metric | FlowFRAM | Recomputed | Abs Error | Rel Error % | Status |
|--------|----------|------------|-----------|-------------|--------|
| REI | 0.642498 | 0.640238 | 0.002260 | 0.3518% | ✅ PASS |
| REI_static+dynamic_sum | 0.642498 | 0.640238 | 0.002260 | 0.3518% | ✅ PASS |
| Factor_Coupling Network Entropy_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Temporal Consistency_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_System Activity Entropy_value | 0.131341 | 0.131341 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Aspect Entropy_value | 0.102185 | 0.102185 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Functional Resonance_value | 0.100000 | 0.100000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Entropy Synchronization_value | 0.004297 | 0.004297 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Output Variability_value | 0.002415 | 0.002415 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the heating time | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to boil water | 0.417276 | 0.417276 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to set the target temperature | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the time it is allowed to stew | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to pour onto tea leaves | 10.944940 | 10.944940 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to fill with a quantity of water | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to supply kettle | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Resonance_score_to boil water->to pour onto tea leaves | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| TE_net_to boil water->to pour onto tea leaves | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| TE_causal_confirmed_count | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| VPI | 1 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| H_aspect_recomputed | 1.842371 | 1.842371 | 0.000000 | 0.0000% | ✅ PASS |
| ChainStrength_0_to boil water → to pour onto t | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Damping_to pour onto tea leaves | 10.000000 | 1.000000 | 9.000000 | 90.0000% | ❌ FAIL |
| System_ITD_recomputed | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CRI_top1_score | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| ES_amplification_factor | 1.008496 | 1.008496 | 0.000000 | 0.0000% | ✅ PASS |
| ES_convergence_iterations | 7.000000 | 7.000000 | 0.000000 | 0.0000% | ✅ PASS |
| REI_nonlinear | 0.642498 | 0.640238 | 0.002260 | 0.3518% | ✅ PASS |
| REI_interaction_percent | 0.353063 | 0.000000 | 0.353063 | 100.0000% | ✅ PASS |
| EntropyRate_system | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_QUANTITY_g | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_Capacity_J_gC | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMP_START_C | 108.346344 | 108.346344 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMPERATURE | 108.346344 | 108.346344 | 0.000000 | 0.0000% | ✅ PASS |

*Generated: Python script independent recomputation*

---

# Validation Report: Rees & Slater (2024) — Boil Water Advisory
## Scenario: convergence-N5000-normal-distribution-temperature

**Total checks: 34 | Passed: 33 | Failed: 1**

| Metric | FlowFRAM | Recomputed | Abs Error | Rel Error % | Status |
|--------|----------|------------|-----------|-------------|--------|
| REI | 0.642136 | 0.639967 | 0.002168 | 0.3377% | ✅ PASS |
| REI_static+dynamic_sum | 0.642136 | 0.639967 | 0.002168 | 0.3377% | ✅ PASS |
| Factor_Coupling Network Entropy_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Temporal Consistency_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_System Activity Entropy_value | 0.131341 | 0.131341 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Aspect Entropy_value | 0.102185 | 0.102185 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Functional Resonance_value | 0.100000 | 0.100000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Entropy Synchronization_value | 0.004123 | 0.004123 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Output Variability_value | 0.002319 | 0.002319 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the heating time | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to boil water | 0.398652 | 0.398652 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to set the target temperature | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the time it is allowed to stew | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to pour onto tea leaves | 10.506922 | 10.506922 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to fill with a quantity of water | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to supply kettle | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Resonance_score_to boil water->to pour onto tea leaves | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| TE_net_to boil water->to pour onto tea leaves | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| TE_causal_confirmed_count | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| VPI | 1 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| H_aspect_recomputed | 1.842371 | 1.842371 | 0.000000 | 0.0000% | ✅ PASS |
| ChainStrength_0_to boil water → to pour onto t | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Damping_to pour onto tea leaves | 10.000000 | 1.000000 | 9.000000 | 90.0000% | ❌ FAIL |
| System_ITD_recomputed | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CRI_top1_score | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| ES_amplification_factor | 1.008100 | 1.008100 | 0.000000 | 0.0000% | ✅ PASS |
| ES_convergence_iterations | 7.000000 | 7.000000 | 0.000000 | 0.0000% | ✅ PASS |
| REI_nonlinear | 0.642136 | 0.639967 | 0.002168 | 0.3377% | ✅ PASS |
| REI_interaction_percent | 0.338832 | 0.000000 | 0.338832 | 100.0000% | ✅ PASS |
| EntropyRate_system | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_QUANTITY_g | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_Capacity_J_gC | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMP_START_C | 98.674999 | 98.674999 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMPERATURE | 98.674999 | 98.674999 | 0.000000 | 0.0000% | ✅ PASS |

*Generated: Python script independent recomputation*

---

# Validation Report: Rees & Slater (2024) — Boil Water Advisory
## Scenario: double-water-volume

**Total checks: 30 | Passed: 28 | Failed: 2**

| Metric | FlowFRAM | Recomputed | Abs Error | Rel Error % | Status |
|--------|----------|------------|-----------|-------------|--------|
| REI | 0.606811 | 0.606811 | 0.000000 | 0.0000% | ✅ PASS |
| REI_static+dynamic_sum | 0.606811 | 0.606811 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Coupling Network Entropy_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Temporal Consistency_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_System Activity Entropy_value | 0.129315 | 0.129315 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Aspect Entropy_value | 0.127497 | 0.127497 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Functional Resonance_value | 0.050000 | 0.050000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Entropy Synchronization_value | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Output Variability_value | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the heating time | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to boil water | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to set the target temperature | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the time it is allowed to stew | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to pour onto tea leaves | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to fill with a quantity of water | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to supply kettle | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Resonance_score_to boil water->to pour onto tea leaves | -0.500000 | -0.500000 | 0.000000 | 0.0000% | ✅ PASS |
| TE_net_to boil water->to pour onto tea leaves | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| TE_causal_confirmed_count | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| VPI | 1 | 0.500000 | 0.500000 | 50.0000% | ❌ FAIL |
| H_aspect_recomputed | 2.251629 | 2.251629 | 0.000000 | 0.0000% | ✅ PASS |
| ChainStrength_0_to boil water → to pour onto t | 1 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Damping_to pour onto tea leaves | 10 | 1.000000 | 9.000000 | 90.0000% | ❌ FAIL |
| System_ITD_recomputed | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CRI_top1_score | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| ES_amplification_factor | 1 | 1 | 0.000000 | 0.0000% | ✅ PASS |
| REI_nonlinear | 0.606811 | 0.606811 | 0.000000 | 0.0000% | ✅ PASS |
| REI_interaction_percent | 0.000000 | 0.000000 | 0.000000 | 0.0025% | ✅ PASS |
| EntropyRate_system | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMPERATURE | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |

*Generated: Python script independent recomputation*

---

# Validation Report: Rees & Slater (2024) — Boil Water Advisory
## Scenario: extended-stewing-time

**Total checks: 30 | Passed: 28 | Failed: 2**

| Metric | FlowFRAM | Recomputed | Abs Error | Rel Error % | Status |
|--------|----------|------------|-----------|-------------|--------|
| REI | 0.606811 | 0.606811 | 0.000000 | 0.0000% | ✅ PASS |
| REI_static+dynamic_sum | 0.606811 | 0.606811 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Coupling Network Entropy_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Temporal Consistency_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_System Activity Entropy_value | 0.129315 | 0.129315 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Aspect Entropy_value | 0.127497 | 0.127497 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Functional Resonance_value | 0.050000 | 0.050000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Entropy Synchronization_value | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Output Variability_value | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the heating time | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to boil water | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to set the target temperature | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the time it is allowed to stew | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to pour onto tea leaves | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to fill with a quantity of water | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to supply kettle | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Resonance_score_to boil water->to pour onto tea leaves | -0.500000 | -0.500000 | 0.000000 | 0.0000% | ✅ PASS |
| TE_net_to boil water->to pour onto tea leaves | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| TE_causal_confirmed_count | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| VPI | 1 | 0.500000 | 0.500000 | 50.0000% | ❌ FAIL |
| H_aspect_recomputed | 2.251629 | 2.251629 | 0.000000 | 0.0000% | ✅ PASS |
| ChainStrength_0_to boil water → to pour onto t | 1 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Damping_to pour onto tea leaves | 10 | 1.000000 | 9.000000 | 90.0000% | ❌ FAIL |
| System_ITD_recomputed | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CRI_top1_score | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| ES_amplification_factor | 1 | 1 | 0.000000 | 0.0000% | ✅ PASS |
| REI_nonlinear | 0.606811 | 0.606811 | 0.000000 | 0.0000% | ✅ PASS |
| REI_interaction_percent | 0.000000 | 0.000000 | 0.000000 | 0.0038% | ✅ PASS |
| EntropyRate_system | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMPERATURE | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |

*Generated: Python script independent recomputation*

---

# Validation Report: Rees & Slater (2024) — Boil Water Advisory
## Scenario: linear-temperature-increment

**Total checks: 34 | Passed: 33 | Failed: 1**

| Metric | FlowFRAM | Recomputed | Abs Error | Rel Error % | Status |
|--------|----------|------------|-----------|-------------|--------|
| REI | 0.652824 | 0.647920 | 0.004904 | 0.7511% | ✅ PASS |
| REI_static+dynamic_sum | 0.652824 | 0.647920 | 0.004904 | 0.7511% | ✅ PASS |
| Factor_Coupling Network Entropy_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Temporal Consistency_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_System Activity Entropy_value | 0.131341 | 0.131341 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Aspect Entropy_value | 0.102185 | 0.102185 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Functional Resonance_value | 0.100000 | 0.100000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Entropy Synchronization_value | 0.009297 | 0.009297 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Output Variability_value | 0.005097 | 0.005097 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the heating time | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to boil water | 1.144479 | 1.144479 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to set the target temperature | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the time it is allowed to stew | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to pour onto tea leaves | 23.055650 | 23.055650 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to fill with a quantity of water | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to supply kettle | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Resonance_score_to boil water->to pour onto tea leaves | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| TE_net_to boil water->to pour onto tea leaves | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| TE_causal_confirmed_count | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| VPI | 1 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| H_aspect_recomputed | 1.842371 | 1.842371 | 0.000000 | 0.0000% | ✅ PASS |
| ChainStrength_0_to boil water → to pour onto t | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Damping_to pour onto tea leaves | 10.000000 | 1.000000 | 9.000000 | 90.0000% | ❌ FAIL |
| System_ITD_recomputed | 0.000004 | 0.000004 | 0.000000 | 0.0000% | ✅ PASS |
| CRI_top1_score | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| ES_amplification_factor | 1.024508 | 1.024508 | 0.000000 | 0.0000% | ✅ PASS |
| ES_convergence_iterations | 9.000000 | 9.000000 | 0.000000 | 0.0000% | ✅ PASS |
| REI_nonlinear | 0.652824 | 0.647920 | 0.004904 | 0.7511% | ✅ PASS |
| REI_interaction_percent | 0.756807 | 0.000000 | 0.756807 | 100.0000% | ✅ PASS |
| EntropyRate_system | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_QUANTITY_g | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_Capacity_J_gC | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMP_START_C | 841.666667 | 841.666667 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMPERATURE | 841.666667 | 841.666667 | 0.000000 | 0.0000% | ✅ PASS |

*Generated: Python script independent recomputation*

---

# Validation Report: Rees & Slater (2024) — Boil Water Advisory
## Scenario: normal-distribution-temperature

**Total checks: 34 | Passed: 33 | Failed: 1**

| Metric | FlowFRAM | Recomputed | Abs Error | Rel Error % | Status |
|--------|----------|------------|-----------|-------------|--------|
| REI | 0.642276 | 0.640072 | 0.002204 | 0.3432% | ✅ PASS |
| REI_static+dynamic_sum | 0.642276 | 0.640072 | 0.002204 | 0.3432% | ✅ PASS |
| Factor_Coupling Network Entropy_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Temporal Consistency_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_System Activity Entropy_value | 0.131341 | 0.131341 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Aspect Entropy_value | 0.102185 | 0.102185 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Functional Resonance_value | 0.100000 | 0.100000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Entropy Synchronization_value | 0.004190 | 0.004190 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Output Variability_value | 0.002356 | 0.002356 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the heating time | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to boil water | 0.405347 | 0.405347 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to set the target temperature | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the time it is allowed to stew | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to pour onto tea leaves | 10.677172 | 10.677172 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to fill with a quantity of water | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to supply kettle | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Resonance_score_to boil water->to pour onto tea leaves | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| TE_net_to boil water->to pour onto tea leaves | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| TE_causal_confirmed_count | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| VPI | 1 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| H_aspect_recomputed | 1.842371 | 1.842371 | 0.000000 | 0.0000% | ✅ PASS |
| ChainStrength_0_to boil water → to pour onto t | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Damping_to pour onto tea leaves | 10.000000 | 1.000000 | 9.000000 | 90.0000% | ❌ FAIL |
| System_ITD_recomputed | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CRI_top1_score | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| ES_amplification_factor | 1.008243 | 1.008243 | 0.000000 | 0.0000% | ✅ PASS |
| ES_convergence_iterations | 7.000000 | 7.000000 | 0.000000 | 0.0000% | ✅ PASS |
| REI_nonlinear | 0.642276 | 0.640072 | 0.002204 | 0.3432% | ✅ PASS |
| REI_interaction_percent | 0.344344 | 0.000000 | 0.344344 | 100.0000% | ✅ PASS |
| EntropyRate_system | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_QUANTITY_g | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_Capacity_J_gC | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMP_START_C | 102.011847 | 102.011847 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMPERATURE | 102.011847 | 102.011847 | 0.000000 | 0.0000% | ✅ PASS |

*Generated: Python script independent recomputation*

---

# Validation Report: Rees & Slater (2024) — Boil Water Advisory
## Scenario: r3-normal-distribution-temperature

**Total checks: 34 | Passed: 33 | Failed: 1**

| Metric | FlowFRAM | Recomputed | Abs Error | Rel Error % | Status |
|--------|----------|------------|-----------|-------------|--------|
| REI | 0.642171 | 0.639994 | 0.002177 | 0.3391% | ✅ PASS |
| REI_static+dynamic_sum | 0.642171 | 0.639994 | 0.002177 | 0.3391% | ✅ PASS |
| Factor_Coupling Network Entropy_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Temporal Consistency_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_System Activity Entropy_value | 0.131341 | 0.131341 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Aspect Entropy_value | 0.102185 | 0.102185 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Functional Resonance_value | 0.100000 | 0.100000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Entropy Synchronization_value | 0.004140 | 0.004140 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Output Variability_value | 0.002328 | 0.002328 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the heating time | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to boil water | 0.401210 | 0.401210 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to set the target temperature | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the time it is allowed to stew | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to pour onto tea leaves | 10.549031 | 10.549031 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to fill with a quantity of water | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to supply kettle | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Resonance_score_to boil water->to pour onto tea leaves | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| TE_net_to boil water->to pour onto tea leaves | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| TE_causal_confirmed_count | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| VPI | 1 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| H_aspect_recomputed | 1.842371 | 1.842371 | 0.000000 | 0.0000% | ✅ PASS |
| ChainStrength_0_to boil water → to pour onto t | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Damping_to pour onto tea leaves | 10.000000 | 1.000000 | 9.000000 | 90.0000% | ❌ FAIL |
| System_ITD_recomputed | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CRI_top1_score | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| ES_amplification_factor | 1.008153 | 1.008153 | 0.000000 | 0.0000% | ✅ PASS |
| ES_convergence_iterations | 7.000000 | 7.000000 | 0.000000 | 0.0000% | ✅ PASS |
| REI_nonlinear | 0.642171 | 0.639994 | 0.002177 | 0.3391% | ✅ PASS |
| REI_interaction_percent | 0.340227 | 0.000000 | 0.340227 | 100.0000% | ✅ PASS |
| EntropyRate_system | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_QUANTITY_g | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_Capacity_J_gC | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMP_START_C | 99.954731 | 99.954731 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMPERATURE | 99.954731 | 99.954731 | 0.000000 | 0.0000% | ✅ PASS |

*Generated: Python script independent recomputation*

---

# Validation Report: Rees & Slater (2024) — Boil Water Advisory
## Scenario: random-uniform-temperature

**Total checks: 34 | Passed: 33 | Failed: 1**

| Metric | FlowFRAM | Recomputed | Abs Error | Rel Error % | Status |
|--------|----------|------------|-----------|-------------|--------|
| REI | 0.638981 | 0.637611 | 0.001370 | 0.2144% | ✅ PASS |
| REI_static+dynamic_sum | 0.638981 | 0.637611 | 0.001370 | 0.2144% | ✅ PASS |
| Factor_Coupling Network Entropy_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Temporal Consistency_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_System Activity Entropy_value | 0.131341 | 0.131341 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Aspect Entropy_value | 0.102185 | 0.102185 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Functional Resonance_value | 0.100000 | 0.100000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Entropy Synchronization_value | 0.002609 | 0.002609 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Output Variability_value | 0.001476 | 0.001476 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the heating time | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to boil water | 0.254623 | 0.254623 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to set the target temperature | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the time it is allowed to stew | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to pour onto tea leaves | 6.667408 | 6.667408 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to fill with a quantity of water | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to supply kettle | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Resonance_score_to boil water->to pour onto tea leaves | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| TE_net_to boil water->to pour onto tea leaves | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| TE_causal_confirmed_count | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| VPI | 1 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| H_aspect_recomputed | 1.842371 | 1.842371 | 0.000000 | 0.0000% | ✅ PASS |
| ChainStrength_0_to boil water → to pour onto t | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Damping_to pour onto tea leaves | 10.000000 | 1.000000 | 9.000000 | 90.0000% | ❌ FAIL |
| System_ITD_recomputed | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CRI_top1_score | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| ES_amplification_factor | 1.005070 | 1.005070 | 0.000000 | 0.0000% | ✅ PASS |
| ES_convergence_iterations | 6.000000 | 6.000000 | 0.000000 | 0.0000% | ✅ PASS |
| REI_nonlinear | 0.638981 | 0.637611 | 0.001370 | 0.2144% | ✅ PASS |
| REI_interaction_percent | 0.214895 | 0.000000 | 0.214895 | 100.0000% | ✅ PASS |
| EntropyRate_system | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_QUANTITY_g | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_Capacity_J_gC | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMP_START_C | 40.271265 | 40.271265 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMPERATURE | 40.271265 | 40.271265 | 0.000000 | 0.0000% | ✅ PASS |

*Generated: Python script independent recomputation*

---

# Validation Report: Rees & Slater (2024) — Boil Water Advisory
## Scenario: rep1-normal-distribution-temperature

**Total checks: 34 | Passed: 33 | Failed: 1**

| Metric | FlowFRAM | Recomputed | Abs Error | Rel Error % | Status |
|--------|----------|------------|-----------|-------------|--------|
| REI | 0.642087 | 0.639931 | 0.002156 | 0.3358% | ✅ PASS |
| REI_static+dynamic_sum | 0.642087 | 0.639931 | 0.002156 | 0.3358% | ✅ PASS |
| Factor_Coupling Network Entropy_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Temporal Consistency_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_System Activity Entropy_value | 0.131341 | 0.131341 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Aspect Entropy_value | 0.102185 | 0.102185 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Functional Resonance_value | 0.100000 | 0.100000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Entropy Synchronization_value | 0.004099 | 0.004099 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Output Variability_value | 0.002306 | 0.002306 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the heating time | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to boil water | 0.397471 | 0.397471 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to set the target temperature | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the time it is allowed to stew | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to pour onto tea leaves | 10.446294 | 10.446294 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to fill with a quantity of water | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to supply kettle | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Resonance_score_to boil water->to pour onto tea leaves | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| TE_net_to boil water->to pour onto tea leaves | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| TE_causal_confirmed_count | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| VPI | 1 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| H_aspect_recomputed | 1.842371 | 1.842371 | 0.000000 | 0.0000% | ✅ PASS |
| ChainStrength_0_to boil water → to pour onto t | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Damping_to pour onto tea leaves | 10.000000 | 1.000000 | 9.000000 | 90.0000% | ❌ FAIL |
| System_ITD_recomputed | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CRI_top1_score | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| ES_amplification_factor | 1.008073 | 1.008073 | 0.000000 | 0.0000% | ✅ PASS |
| ES_convergence_iterations | 7.000000 | 7.000000 | 0.000000 | 0.0000% | ✅ PASS |
| REI_nonlinear | 0.642087 | 0.639931 | 0.002156 | 0.3358% | ✅ PASS |
| REI_interaction_percent | 0.336912 | 0.000000 | 0.336912 | 100.0000% | ✅ PASS |
| EntropyRate_system | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_QUANTITY_g | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_Capacity_J_gC | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMP_START_C | 98.103571 | 98.103571 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMPERATURE | 98.103571 | 98.103571 | 0.000000 | 0.0000% | ✅ PASS |

*Generated: Python script independent recomputation*

---

# Validation Report: Rees & Slater (2024) — Boil Water Advisory
## Scenario: rep2-normal-distribution-temperature

**Total checks: 34 | Passed: 33 | Failed: 1**

| Metric | FlowFRAM | Recomputed | Abs Error | Rel Error % | Status |
|--------|----------|------------|-----------|-------------|--------|
| REI | 0.642200 | 0.640015 | 0.002185 | 0.3402% | ✅ PASS |
| REI_static+dynamic_sum | 0.642200 | 0.640015 | 0.002185 | 0.3402% | ✅ PASS |
| Factor_Coupling Network Entropy_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Temporal Consistency_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_System Activity Entropy_value | 0.131341 | 0.131341 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Aspect Entropy_value | 0.102185 | 0.102185 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Functional Resonance_value | 0.100000 | 0.100000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Entropy Synchronization_value | 0.004154 | 0.004154 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Output Variability_value | 0.002336 | 0.002336 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the heating time | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to boil water | 0.402236 | 0.402236 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to set the target temperature | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the time it is allowed to stew | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to pour onto tea leaves | 10.584459 | 10.584459 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to fill with a quantity of water | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to supply kettle | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Resonance_score_to boil water->to pour onto tea leaves | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| TE_net_to boil water->to pour onto tea leaves | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| TE_causal_confirmed_count | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| VPI | 1 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| H_aspect_recomputed | 1.842371 | 1.842371 | 0.000000 | 0.0000% | ✅ PASS |
| ChainStrength_0_to boil water → to pour onto t | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Damping_to pour onto tea leaves | 10.000000 | 1.000000 | 9.000000 | 90.0000% | ❌ FAIL |
| System_ITD_recomputed | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CRI_top1_score | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| ES_amplification_factor | 1.008176 | 1.008176 | 0.000000 | 0.0000% | ✅ PASS |
| ES_convergence_iterations | 7.000000 | 7.000000 | 0.000000 | 0.0000% | ✅ PASS |
| REI_nonlinear | 0.642200 | 0.640015 | 0.002185 | 0.3402% | ✅ PASS |
| REI_interaction_percent | 0.341361 | 0.000000 | 0.341361 | 100.0000% | ✅ PASS |
| EntropyRate_system | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_QUANTITY_g | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_Capacity_J_gC | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMP_START_C | 100.460320 | 100.460320 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMPERATURE | 100.460320 | 100.460320 | 0.000000 | 0.0000% | ✅ PASS |

*Generated: Python script independent recomputation*

---

# Validation Report: Rees & Slater (2024) — Boil Water Advisory
## Scenario: sensitivity-sigma08-normal-distribution-temperature

**Total checks: 34 | Passed: 33 | Failed: 1**

| Metric | FlowFRAM | Recomputed | Abs Error | Rel Error % | Status |
|--------|----------|------------|-----------|-------------|--------|
| REI | 0.640413 | 0.638681 | 0.001732 | 0.2704% | ✅ PASS |
| REI_static+dynamic_sum | 0.640413 | 0.638681 | 0.001732 | 0.2704% | ✅ PASS |
| Factor_Coupling Network Entropy_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Temporal Consistency_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_System Activity Entropy_value | 0.131341 | 0.131341 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Aspect Entropy_value | 0.102185 | 0.102185 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Functional Resonance_value | 0.100000 | 0.100000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Entropy Synchronization_value | 0.003295 | 0.003295 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Output Variability_value | 0.001860 | 0.001860 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the heating time | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to boil water | 0.318900 | 0.318900 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to set the target temperature | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the time it is allowed to stew | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to pour onto tea leaves | 8.413060 | 8.413060 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to fill with a quantity of water | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to supply kettle | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Resonance_score_to boil water->to pour onto tea leaves | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| TE_net_to boil water->to pour onto tea leaves | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| TE_causal_confirmed_count | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| VPI | 1 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| H_aspect_recomputed | 1.842371 | 1.842371 | 0.000000 | 0.0000% | ✅ PASS |
| ChainStrength_0_to boil water → to pour onto t | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Damping_to pour onto tea leaves | 10.000000 | 1.000000 | 9.000000 | 90.0000% | ❌ FAIL |
| System_ITD_recomputed | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CRI_top1_score | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| ES_amplification_factor | 1.006408 | 1.006408 | 0.000000 | 0.0000% | ✅ PASS |
| ES_convergence_iterations | 6.000000 | 6.000000 | 0.000000 | 0.0000% | ✅ PASS |
| REI_nonlinear | 0.640413 | 0.638681 | 0.001732 | 0.2704% | ✅ PASS |
| REI_interaction_percent | 0.271175 | 0.000000 | 0.271175 | 100.0000% | ✅ PASS |
| EntropyRate_system | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_QUANTITY_g | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_Capacity_J_gC | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMP_START_C | 63.189313 | 63.189313 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMPERATURE | 63.189313 | 63.189313 | 0.000000 | 0.0000% | ✅ PASS |

*Generated: Python script independent recomputation*

---

# Validation Report: Rees & Slater (2024) — Boil Water Advisory
## Scenario: sensitivity-sigma12-normal-distribution-temperature

**Total checks: 34 | Passed: 33 | Failed: 1**

| Metric | FlowFRAM | Recomputed | Abs Error | Rel Error % | Status |
|--------|----------|------------|-----------|-------------|--------|
| REI | 0.644387 | 0.641647 | 0.002741 | 0.4253% | ✅ PASS |
| REI_static+dynamic_sum | 0.644387 | 0.641647 | 0.002741 | 0.4253% | ✅ PASS |
| Factor_Coupling Network Entropy_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Temporal Consistency_value | 0.150000 | 0.150000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_System Activity Entropy_value | 0.131341 | 0.131341 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Aspect Entropy_value | 0.102185 | 0.102185 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Functional Resonance_value | 0.100000 | 0.100000 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Entropy Synchronization_value | 0.005205 | 0.005205 | 0.000000 | 0.0000% | ✅ PASS |
| Factor_Output Variability_value | 0.002915 | 0.002915 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the heating time | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to boil water | 0.500671 | 0.500671 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to set the target temperature | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to control the time it is allowed to stew | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to pour onto tea leaves | 13.238888 | 13.238888 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to fill with a quantity of water | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CV%_to supply kettle | 0 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Resonance_score_to boil water->to pour onto tea leaves | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| TE_net_to boil water->to pour onto tea leaves | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| TE_causal_confirmed_count | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| VPI | 1 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| H_aspect_recomputed | 1.842371 | 1.842371 | 0.000000 | 0.0000% | ✅ PASS |
| ChainStrength_0_to boil water → to pour onto t | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| Damping_to pour onto tea leaves | 10.000000 | 1.000000 | 9.000000 | 90.0000% | ❌ FAIL |
| System_ITD_recomputed | 0.000000 | 0.000000 | 0.000000 | 0.0000% | ✅ PASS |
| CRI_top1_score | 1.000000 | 1.000000 | 0.000000 | 0.0000% | ✅ PASS |
| ES_amplification_factor | 1.010313 | 1.010313 | 0.000000 | 0.0000% | ✅ PASS |
| ES_convergence_iterations | 7.000000 | 7.000000 | 0.000000 | 0.0000% | ✅ PASS |
| REI_nonlinear | 0.644387 | 0.641647 | 0.002741 | 0.4253% | ✅ PASS |
| REI_interaction_percent | 0.427137 | 0.000000 | 0.427137 | 100.0000% | ✅ PASS |
| EntropyRate_system | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_QUANTITY_g | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_Capacity_J_gC | 0 | 0 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMP_START_C | 155.726081 | 155.726081 | 0.000000 | 0.0000% | ✅ PASS |
| Variance_TEMPERATURE | 155.726081 | 155.726081 | 0.000000 | 0.0000% | ✅ PASS |

*Generated: Python script independent recomputation*