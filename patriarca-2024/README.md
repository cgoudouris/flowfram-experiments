# Patriarca et al. (2024) — Healthcare FRAM (Functional Random Walker)

## Experiment Summary

| Property | Value |
|----------|-------|
| **Article** | Patriarca, R. et al. (2024) — Functional Random Walker for healthcare resilience |
| **Domain** | Healthcare system — Emergency triage and treatment |
| **Functions** | 14 (F01–F14) |
| **Edges** | 19 |
| **Scenarios** | 2 |
| **Iterations** | 1000 (stochastic Monte Carlo) |

## Scenarios

| # | Scenario | Description |
|---|----------|-------------|
| S0 | Nominal Baseline | All α₀=1.0, δ=δ₀ — Normal operating conditions |
| S1 | Hemorrhagic Event | F04 missing Control (Article §4.3) — Degraded precision |

## Key Validation Targets

### PRECISION_OUT Cascade
The article's core mechanism: precision degradation propagates through the function coupling chain.

| Function | Expected Mean | Chain Position |
|----------|--------------|----------------|
| F04 | ≈ 0.90 | Source (epicenter) |
| F10 | ≈ 0.90 | Direct downstream |
| F08 | ≈ 0.81 | Two hops (0.9 × 0.9) |
| F11 | ≈ 0.81 | Two hops |

### F04 Epicenter Analysis
- Mean output ≈ 0.9006
- CV ≈ 15.04%
- Highest variability among all functions

## How to Reproduce

```bash
cd patriarca-2024
python3 validate.py
```

## Google Sheets

*(Link will be added after import)*
