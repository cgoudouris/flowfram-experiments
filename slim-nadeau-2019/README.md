# Slim & Nadeau (2019) — Aircraft Deicing (Deterministic)

## Experiment Summary

| Property | Value |
|----------|-------|
| **Article** | Slim, H. & Nadeau, S. (2019) — FRAM analysis of aircraft ground deicing operations |
| **Domain** | Aviation Safety — Ground Deicing |
| **Functions** | 17 |
| **Edges** | 35 |
| **Scenarios** | 6 (deterministic) |
| **Iterations** | 1 per scenario (deterministic) |
| **Method** | Deterministic propagation (fuzzy logic variability) |

## Scenarios

| # | Name | Description |
|---|------|-------------|
| S0 | Baseline | Article Table nominal conditions — all NV |
| S1 | Single HV | One function set to Highly Variable |
| S2 | Two HV | Two functions at HV |
| S3 | Moderate Spread | Several functions at V (Variable) |
| S4 | Mixed Degradation | Combination of V and HV |
| S5 | Maximum Degradation | Multiple HV functions |

## Key Validation Targets

### 1. Perfect Determinism
All scenarios run with 1 iteration. StdDev = 0 and CV = 0 for every function.

### 2. Variability Classification
The article uses NV / V / HV (No Variability / Variable / Highly Variable) classification:
- **NV**: Fixed output, no variation
- **V**: Moderate variability
- **HV**: High variability, potential for large deviations

### 3. REI Sensitivity
REI should increase monotonically from S0 (all NV) to S5 (maximum degradation):
```
REI(S0) ≤ REI(S1) ≤ REI(S2) ≤ ... ≤ REI(S5)
```

### 4. Output Determinism
Since each scenario runs exactly 1 iteration, all function outputs must be single deterministic values. No statistical variability should exist.

## Reproduction Steps

1. **Place exports**: Copy FlowFRAM JSON exports to `data/`
2. **Install deps**: `pip install -r ../requirements.txt`
3. **Run**: `python validate.py`
4. **Outputs**:
   - `spreadsheets/` — XLSX files with live Excel formulas
   - `results/validation-report.md` — Validation report with determinism checks

## Data Format

Each scenario exports 3 JSON files from FlowFRAM:
- `*-complexity-metrics-results-*.json` — REI, factors, resonance, chains, entropy
- `*-statistics-results-*.json` — Per-function statistics (all StdDev = 0 for deterministic)
- `*-message-flow-results-*.json` — Raw message flow data (optional)
