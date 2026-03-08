# Rees & Slater (2024) — Boil Water Advisory

## Experiment Summary

| Property | Value |
|----------|-------|
| **Article** | Rees, L.P. & Slater, P. (2024) |
| **Domain** | Water safety / boil water advisory process |
| **Functions** | 10 |
| **Edges** | 9 |
| **Scenarios** | 9 (6 deterministic + 3 stochastic) |
| **Iterations** | 1000 (stochastic), 1 (deterministic) |

## Scenarios

| # | Scenario | Type | Description |
|---|----------|------|-------------|
| S1 | Baseline | Deterministic | All functions at nominal values |
| S2 | Double Water | Deterministic | Water volume doubled |
| S3 | Extended Stewing Time | Deterministic | Longer tea steeping |
| S4 | Linear Temperature Increment | Stochastic | Linear temp variation |
| S5 | Normal Distribution Temperature | Stochastic | Gaussian temp variation |
| S6 | Random Uniform Temperature | Stochastic | Uniform temp variation |
| S7-S9 | Additional scenarios | Deterministic | Various parameter changes |

## How to Reproduce

1. Place FlowFRAM JSON exports in `data/`
2. Run validation:
   ```bash
   cd rees-slater-2024
   python3 validate.py
   ```
3. Check results in `spreadsheets/` and `results/`

## Google Sheets

*(Link will be added after import)*

## Key Claims Validated

- Deterministic scenarios produce zero variability (CV = 0)
- Stochastic scenarios exhibit measurable output variability
- Temperature variation scenarios show highest CV values
- REI increases with stochastic variability
