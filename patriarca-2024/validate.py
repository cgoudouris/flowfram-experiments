#!/usr/bin/env python3
"""
validate.py — Patriarca et al. (2024) Healthcare FRAM experiment.

Model: 14 functions (F01–F14), 19 edges, 2 scenarios
  - S0: Nominal Baseline (all α₀=1.0, δ=δ₀)
  - S1: Hemorrhagic Event (F04 missing Control — Article §4.3)

Key validation targets:
  - PRECISION_OUT cascade: F04=0.9 → F10=0.9 → F08=0.81 → F11=0.81
  - F04 epicenter: mean≈0.9, CV≈15%
  - REI change S0→S1

Article: Patriarca, R. et al. (2024) — Functional Random Walker Healthcare
"""
from __future__ import annotations

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common.export_reader import discover_scenarios, load_scenario
from common.metrics import (
    validate_scenario, format_validation_report,
    compute_cv, validate_metric,
)
from common.xlsx_generator import generate_scenario_xlsx, generate_comparison_xlsx


EXPERIMENT_NAME = "Patriarca et al. (2024) — Healthcare FRAM (FRW)"
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
SPREADSHEETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "spreadsheets")
RESULTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")


def validate_precision_cascade(cm, results_list):
    """
    Article-specific validation: PRECISION_OUT propagation chain.
    F04 → F10 → F08 → F11
    Expected: 0.9 → 0.9 → 0.81 → 0.81
    """
    precision_targets = {
        "F04": 0.9,
        "F10": 0.9,
        "F08": 0.81,
        "F11": 0.81,
    }

    for fv in cm.function_variabilities:
        for func_id, expected_mean in precision_targets.items():
            if func_id in fv.function_id:
                results_list.append(validate_metric(
                    f"PRECISION_cascade_{func_id}_mean",
                    fv.mean,
                    expected_mean,
                    tolerance=0.05,  # 5% tolerance for stochastic
                ))


def main():
    os.makedirs(SPREADSHEETS_DIR, exist_ok=True)
    os.makedirs(RESULTS_DIR, exist_ok=True)

    scenarios = discover_scenarios(DATA_DIR)
    if not scenarios:
        print(f"No scenario files found in {DATA_DIR}/")
        print("Place FlowFRAM JSON exports in data/")
        return

    print(f"{'='*60}")
    print(f"  {EXPERIMENT_NAME}")
    print(f"  Found {len(scenarios)} scenario(s)")
    print(f"{'='*60}\n")

    all_reports = []
    comparison_data = []

    for sf in scenarios:
        print(f"Processing: {sf.scenario_name}")
        cm, stats, mf = load_scenario(sf)

        if not cm:
            print(f"  ⚠ No complexity-metrics export found, skipping.")
            continue

        # 1. Generate XLSX
        xlsx_path = os.path.join(SPREADSHEETS_DIR, f"{sf.scenario_name}-analysis.xlsx")
        generate_scenario_xlsx(EXPERIMENT_NAME, sf.scenario_name, cm, stats, xlsx_path)
        print(f"  ✓ Spreadsheet: {xlsx_path}")

        # 2. Standard validation
        results = validate_scenario(cm, stats)

        # 3. Article-specific: PRECISION_OUT cascade
        validate_precision_cascade(cm, results)

        report = format_validation_report(EXPERIMENT_NAME, sf.scenario_name, results)
        all_reports.append(report)

        passed = sum(1 for r in results if r.passed)
        total = len(results)
        print(f"  ✓ Validation: {passed}/{total} checks passed")

        comparison_data.append((sf.scenario_name, cm))

    # Cross-scenario comparison
    if len(comparison_data) > 1:
        comp_path = os.path.join(SPREADSHEETS_DIR, "scenario-comparison.xlsx")
        generate_comparison_xlsx(EXPERIMENT_NAME, comparison_data, comp_path)
        print(f"\n✓ Comparison spreadsheet: {comp_path}")

    # Write report
    report_path = os.path.join(RESULTS_DIR, "validation-report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n\n---\n\n".join(all_reports))
    print(f"✓ Validation report: {report_path}")

    print(f"\n{'='*60}")
    print(f"  Done. {len(scenarios)} scenario(s) processed.")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
