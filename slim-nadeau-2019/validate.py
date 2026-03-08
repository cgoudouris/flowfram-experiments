#!/usr/bin/env python3
"""
validate.py — Slim & Nadeau (2019) Aircraft Deicing experiment.

Model: 17 functions, 35 edges, 6 deterministic scenarios
  - S0: Baseline (Article Table — nominal conditions)
  - S1–S5: Variability degradation scenarios

Key validation targets:
  - Deterministic outputs (1 iteration each, NO stochastic analysis)
  - Fuzzy logic variability classification (NV / V / HV)
  - REI sensitivity to variability level changes
  - Perfect determinism: StdDev = 0, CV = 0 for all functions

Article: Slim, H. & Nadeau, S. (2019) — FRAM analysis of deicing operations
"""
from __future__ import annotations

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common.export_reader import discover_scenarios, load_scenario
from common.metrics import validate_scenario, format_validation_report
from common.xlsx_generator import generate_scenario_xlsx, generate_comparison_xlsx


EXPERIMENT_NAME = "Slim & Nadeau (2019) — Aircraft Deicing (Deterministic)"
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
SPREADSHEETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "spreadsheets")
RESULTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")


def validate_determinism(stats, all_reports):
    """
    Article-specific: Verify all scenarios are perfectly deterministic.
    In deterministic mode (1 iteration), all StdDevs must be 0
    and all CVs must be 0.
    """
    if not stats:
        return

    lines = [
        "## Determinism Validation",
        "",
        "All functions must have StdDev = 0 and CV = 0 (deterministic, 1 iteration).",
        "",
        "| Function | Mean | StdDev | CV | Deterministic? |",
        "|----------|------|--------|----|----------------|",
    ]

    all_deterministic = True
    for func_id, func_stats in sorted(stats.function_stats.items()):
        mean = func_stats.get("mean", 0)
        std = func_stats.get("std", 0)
        cv = func_stats.get("cv", 0)
        is_det = abs(std) < 1e-10 and abs(cv) < 1e-10
        if not is_det:
            all_deterministic = False
        status = "✅" if is_det else "❌"
        lines.append(f"| {func_id} | {mean:.4f} | {std:.6f} | {cv:.6f} | {status} |")

    lines.append("")
    if all_deterministic:
        lines.append("**✅ All functions are perfectly deterministic.**")
    else:
        lines.append("**❌ Some functions show non-zero variance — investigate.**")

    all_reports.append("\n".join(lines))


def validate_variability_classification(cm_data, all_reports):
    """
    Article-specific: The Slim & Nadeau article classifies function variability as:
      - NV (No Variability): fixed/constant output
      - V (Variable): moderate variability
      - HV (Highly Variable): high variability

    We verify that the REI factors reflect these classifications.
    """
    if not cm_data or not cm_data.factors:
        return

    lines = [
        "## Variability Classification",
        "",
        "Article uses NV/V/HV classification for function variability.",
        "We verify that factor magnitudes align with classification levels.",
        "",
        "| Factor | Value | Classification |",
        "|--------|-------|---------------|",
    ]

    for factor in cm_data.factors:
        val = factor.get("value", 0)
        name = factor.get("name", "")
        if val < 0.1:
            cls = "NV (No Variability)"
        elif val < 0.3:
            cls = "V (Variable)"
        else:
            cls = "HV (Highly Variable)"
        lines.append(f"| {name} | {val:.4f} | {cls} |")

    all_reports.append("\n".join(lines))


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
        report = format_validation_report(EXPERIMENT_NAME, sf.scenario_name, results)
        all_reports.append(report)

        passed = sum(1 for r in results if r.passed)
        total = len(results)
        print(f"  ✓ Validation: {passed}/{total} checks passed")

        # 3. Article-specific: determinism check
        validate_determinism(stats, all_reports)

        # 4. Article-specific: variability classification
        validate_variability_classification(cm, all_reports)

        comparison_data.append((sf.scenario_name, cm))

    # 5. Cross-scenario comparison
    if len(comparison_data) > 1:
        comp_path = os.path.join(SPREADSHEETS_DIR, "scenario-comparison.xlsx")
        generate_comparison_xlsx(EXPERIMENT_NAME, comparison_data, comp_path)
        print(f"\n✓ Comparison spreadsheet: {comp_path}")

    # 6. Write report
    report_path = os.path.join(RESULTS_DIR, "validation-report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n\n---\n\n".join(all_reports))
    print(f"✓ Validation report: {report_path}")

    print(f"\n{'='*60}")
    print(f"  Done. {len(scenarios)} scenario(s) processed.")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
