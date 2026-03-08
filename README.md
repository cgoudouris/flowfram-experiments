# FlowFRAM Experiment Reproducibility Package

**Transparent, independently verifiable reproduction of all FlowFRAM thesis experiments.**

This repository contains the complete data, analysis scripts, and **formula-based spreadsheets** needed to reproduce and verify the quantitative results presented in the FlowFRAM PhD thesis. All computations can be validated without access to the FlowFRAM source code.

---

## 📋 Experiments

| # | Experiment | Article | Functions | Edges | Scenarios | Method |
|---|-----------|---------|-----------|-------|-----------|--------|
| 1 | [Rees & Slater (2024)](rees-slater-2024/) | Boil Water Advisory | 10 | 9 | 9 | Stochastic + Deterministic |
| 2 | [Patriarca et al. (2024)](patriarca-2024/) | Healthcare FRAM | 14 | 19 | 2 | Stochastic (Monte Carlo) |
| 3 | [Qiao et al. (2022)](qiao-2022/) | Maritime Emergency | 25 | 50 | 10 | Stochastic (Monte Carlo) |
| 4 | [Slim & Nadeau (2019)](slim-nadeau-2019/) | Aircraft Deicing | 17 | 35 | 6 | Deterministic (Fuzzy Logic) |

**Total: 66 functions, 113 edges, 27 scenarios**

---

## 🔬 Reproducibility Approach

Each experiment provides **two independent verification instruments**:

### 1. Python Validation Scripts
- Parse FlowFRAM JSON exports
- **Recompute all metrics** from raw data using standard formulas
- Compare recomputed values against FlowFRAM's results
- Generate validation reports with pass/fail status

### 2. Excel Spreadsheets (XLSX) with Live Formulas
- All cells contain **actual Excel/Google Sheets formulas** (not static values)
- Formulas implement the same mathematical expressions used by FlowFRAM
- Anyone can inspect and modify the calculations directly
- Available as XLSX files and as Google Sheets (links in each experiment folder)

Both instruments produce **identical results**, proving computational transparency.

---

## 📁 Repository Structure

```
flowfram-experiments/
├── README.md                     # This file
├── requirements.txt              # Python dependencies
├── generate_all.py               # Master script: generates all spreadsheets + reports
├── common/                       # Shared Python library
│   ├── __init__.py
│   ├── export_reader.py          # Reads FlowFRAM JSON exports
│   ├── xlsx_generator.py         # Generates XLSX with formulas
│   └── metrics.py                # Independent metric recomputation
├── rees-slater-2024/
│   ├── README.md                 # Experiment-specific documentation
│   ├── validate.py               # Validation script
│   ├── data/                     # FlowFRAM JSON exports (3 files per scenario)
│   ├── spreadsheets/             # Generated XLSX files
│   └── results/                  # Validation reports
├── patriarca-2024/
│   ├── ...                       # Same structure
├── qiao-2022/
│   ├── ...
└── slim-nadeau-2019/
    ├── ...
```

### Data Files (per scenario)

Each scenario produces 3 JSON exports from FlowFRAM:

| File | Content | Used for |
|------|---------|----------|
| `*-statistics-results-*.json` | Per-variable mean, std, percentiles, histograms | CV, distribution analysis |
| `*-complexity-metrics-results-*.json` | REI, factors, resonance, chains, barriers | All complexity metrics |
| `*-message-flow-results-*.json` | Raw message trace | Message count, flow analysis |

---

## 🚀 Quick Start

### Prerequisites

```bash
python3 --version   # Python 3.9+
pip install -r requirements.txt
```

### Run All Validations

```bash
# Generate spreadsheets + validation reports for all experiments
python3 generate_all.py

# Or run a single experiment
cd patriarca-2024
python3 validate.py
```

### Output

After running, each experiment folder will contain:
- `spreadsheets/*.xlsx` — One spreadsheet per scenario with live formulas
- `results/validation-report.md` — Comparison of recomputed vs. FlowFRAM values

---

## 📊 Metrics Verified

All 22 FlowFRAM metric types are independently recomputed and verified by this package. Metrics are organized by category:

### Core Metrics

| # | Metric | Formula | XLSX Sheet | Description |
|---|--------|---------|------------|-------------|
| 1 | **REI** | $REI = \sum_{k=1}^{n} w_k \cdot F_k$ | REI Calculation | Resonance Entropy Index — weighted sum of complexity factors |
| 2 | **REI Static/Dynamic** | $REI_s = \sum_{static} w_k F_k$ | REI Calculation | Breakdown into static vs dynamic factor contributions |
| 3 | **Factor Contributions** | $\%_k = \frac{w_k F_k}{REI}$ | REI Calculation | Per-factor percentage of total REI |
| 4 | **REI Convergence** | $\Delta REI_t = REI_t - REI_{t-1}$ | *(history in Metadata)* | Iteration-over-iteration stability of REI |

### Variability Metrics

| # | Metric | Formula | XLSX Sheet | Description |
|---|--------|---------|------------|-------------|
| 5 | **CV** | $CV = \frac{\sigma}{\mu}$ | Function Statistics | Coefficient of Variation per function |
| 6 | **CV%** | $CV\% = CV \times 100$ | Function Statistics | Percentage form with cross-validation |
| 7 | **CRI** | $CRI_i = \frac{CV_i}{\sum CV}$ | CRI Ranking | Criticality Ranking Index — normalized CV contribution |
| 8 | **Precision Phenotype** | Threshold-based classification | Function Statistics | Function variability classification (low/medium/high) |

### Entropy Metrics

| # | Metric | Formula | XLSX Sheet | Description |
|---|--------|---------|------------|-------------|
| 9 | **SEI (H_aspect)** | $H = -\sum p_i \log_2 p_i$ | Entropy Analysis | Shannon Entropy Index over aspect distribution |
| 10 | **H_norm** | $H_{norm} = \frac{H}{H_{max}}$ | Entropy Analysis | Normalized entropy (0 = uniform, 1 = max disorder) |
| 11 | **ES 2.0** | Bellman-Picard convergence | ES 2.0 | Entropy Synchronization — network amplification factor |
| 12 | **Entropy Rate** | $\dot{H}_i = CV_t - CV_{t-1}$ | Entropy Rate | Per-function convergence trend |

### Resonance Metrics

| # | Metric | Formula | XLSX Sheet | Description |
|---|--------|---------|------------|-------------|
| 13 | **Combined Score** | $S_{ij} = r_{ij} \times (0.5 + 0.5 \times NMI_{ij})$ | Resonance Analysis | Pearson × NMI resonance detection |
| 14 | **VPI** | $VPI = \frac{\sum \|S_{ij}\|}{n}$ | Resonance Analysis | Variability Propagation Index |
| 15 | **Chain Strength** | $\Pi \|r_i\|$ | Chains & Barriers | Product of absolute correlations along chain |
| 16 | **Barrier Damping** | $D = 1 - \frac{\|r_{out}\|}{\|r_{in}\|}$ | Chains & Barriers | Barrier effectiveness ratio |

### Causal Metrics

| # | Metric | Formula | XLSX Sheet | Description |
|---|--------|---------|------------|-------------|
| 17 | **Transfer Entropy** | $TE_{X \to Y}$ per coupling | Transfer Entropy | Causal information flow per coupling |
| 18 | **Net TE** | $TE_{net} = TE_{fwd} - TE_{rev}$ | Transfer Entropy | Net causal direction |
| 19 | **TE Summary** | Confirmed / Reversed / Symmetric counts | Transfer Entropy | System-level causal classification |

### Epistemological Metrics

| # | Metric | Formula | XLSX Sheet | Description |
|---|--------|---------|------------|-------------|
| 20 | **REI Non-Linear** | $REI_{NL} = REI_{lin} + \sum F_i \times F_j$ | REI Non-Linear | Non-linear REI with interaction terms (FOV×FRC, FOV×ES, FRC×ES) |
| 21 | **ITD** | $ITD = \frac{-\sum p_s \log_2 p_s}{\log_2 \|S\|}$ | ITD Analysis | Dialogical Tension Index (Morin dialogic principle) |
| 22 | **Descriptive Stats** | mean, std, min, max, percentiles | Variable Statistics | Full distribution statistics per variable |

### XLSX Sheets Summary

Each scenario spreadsheet contains up to **13 sheets**:

| Sheet | Content | Formulas |
|-------|---------|----------|
| Metadata | Experiment info, REI status | — |
| Function Statistics | Per-function μ, σ, CV, phenotype | CV = σ/μ |
| REI Calculation | Factor decomposition, static/dynamic split | REI = ΣwF, cross-check |
| Resonance Analysis | All detections with r, NMI | CombinedScore, VPI |
| Entropy Analysis | Aspect distribution, Shannon entropy | H = -Σp·log₂p |
| Chains & Barriers | Resonance chains, barrier functions | Strength = Π\|r\|, Damping |
| ITD Analysis | Per-function ITD with NORM.DIST | ITD_norm formula |
| CRI Ranking | Functions ranked by CV contribution | NormScore, cumulative |
| ES 2.0 | Bellman-Picard convergence data | Amplification analysis |
| REI Non-Linear | Factor interactions (FOV×FRC, etc.) | NL-REI = linear + interactions |
| Entropy Rate | Per-function CV convergence trends | Rate, trend classification |
| Transfer Entropy | Per-coupling causal TE analysis | Net TE, direction formulas |
| Variable Statistics | Full descriptive stats per variable | CV, Range formulas |

---

## 📎 Google Sheets Links

*(Links will be added after Google Workspace import)*

| Experiment | Spreadsheet |
|-----------|-------------|
| Rees & Slater (2024) | [Google Sheets link] |
| Patriarca et al. (2024) | [Google Sheets link] |
| Qiao et al. (2022) | [Google Sheets link] |
| Slim & Nadeau (2019) | [Google Sheets link] |

---

## 📚 References

1. Rees, L. P., & Slater, P. (2024). *FRAM analysis of boil water advisory processes*.
2. Patriarca, R., et al. (2024). *Functional Random Walker for healthcare system resilience*.
3. Qiao, W., et al. (2022). *FRAM-BN coupled approach for maritime emergency response*.
4. Slim, H., & Nadeau, S. (2019). *Fuzzy-FRAM approach for aircraft ground deicing*.

---

## License

This reproducibility package is released under the MIT License.
The FlowFRAM platform source code is proprietary and not included in this repository.
