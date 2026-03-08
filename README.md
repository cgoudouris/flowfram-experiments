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

## 📊 Key Metrics Verified

| Metric | Formula | Description |
|--------|---------|-------------|
| **REI** | $REI = \sum_{k=1}^{n} w_k \cdot F_k$ | Resonance Entropy Index |
| **CV** | $CV = \frac{\sigma}{\mu}$ | Coefficient of Variation |
| **SEI** | $H = -\sum p_i \log_2 p_i$ | Shannon Entropy Index |
| **VPI** | $VPI = \frac{\sum \|r_{ij}\| \cdot w_{ij}}{n}$ | Variability Propagation Index |
| **ITD** | $ITD = \frac{-\sum p_s \log_2 p_s}{\log_2 \|S\|}$ | Dialogical Tension Index |
| **Resonance** | $Score_{ij} = r_{ij} \times (0.5 + 0.5 \times NMI_{ij})$ | Combined resonance score |

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
