# Qiao et al. (2022) — Maritime Emergency Response (FRAM-BN)

## Experiment Summary

| Property | Value |
|----------|-------|
| **Article** | Qiao, W. et al. (2022) — FRAM-BN coupled resilience assessment for maritime emergency response |
| **Domain** | Maritime Emergency Response |
| **Functions** | 25 |
| **Edges** | 50 |
| **Scenarios** | 10 (Baseline + 9 degradation) |
| **Iterations** | 1,000 per stochastic scenario |
| **Method** | Monte Carlo simulation |

## Scenarios

| # | Name | Description |
|---|------|-------------|
| S0 | Baseline | Normal operations — all functions at nominal variability |
| S1 | Communication Degraded | VHF/radio communication functions degraded |
| S2 | Coordination Degraded | Inter-agency coordination impaired |
| S3 | Resource Degraded | Limited SAR resources availability |
| S4 | Detection Degraded | Detection/monitoring functions impaired |
| S5 | Command Degraded | Command & control functions degraded |
| S6 | Environmental Stress | Weather/sea state amplified variability |
| S7 | Training Degraded | Crew competency reduced |
| S8 | Combined (S1+S5) | Communication + Command degraded together |
| S9 | Combined (S3+S4+S6) | Resource + Detection + Environmental triple stress |

## Key Validation Targets

### 1. Degradation Ordering
All degradation scenarios (S1–S9) should produce REI ≥ Baseline REI.

### 2. Combined vs Individual Stress
- S8 (S1+S5 combined) REI should be ≥ max(S1 REI, S5 REI)
- S9 (S3+S4+S6 triple) REI should be ≥ max(S3, S4, S6)

### 3. Barrier Function Identification
Functions acting as barriers should show low CV and stabilizing influence on downstream functions.

### 4. Resonance Chains
Propagation paths from epicenter functions through the model should be traceable via correlation analysis.

## Reproduction Steps

1. **Place exports**: Copy FlowFRAM JSON exports to `data/`
2. **Install deps**: `pip install -r ../requirements.txt`
3. **Run**: `python validate.py`
4. **Outputs**:
   - `spreadsheets/` — XLSX files with live Excel formulas
   - `results/validation-report.md` — Validation report

## Data Format

Each scenario exports 3 JSON files from FlowFRAM:
- `*-complexity-metrics-results-*.json` — REI, factors, resonance, chains, entropy
- `*-statistics-results-*.json` — Per-function simulation statistics
- `*-message-flow-results-*.json` — Raw message flow data (optional for validation)
