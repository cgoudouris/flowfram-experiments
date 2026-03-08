#!/usr/bin/env python3
"""
validate.py — Rees & Slater (2024) Boil Water Advisory experiment.

Reads FlowFRAM exports from data/, recomputes all metrics independently,
generates XLSX spreadsheets with live formulas, and produces a validation report.

Model: 10 functions, 9 edges, 9 scenarios
  - 6 deterministic (no stochastic sampling)
  - 3 stochastic (1000 iterations each)

Article: Rees, L.P. & Slater, P. (2024)
"""
from __future__ import annotations

import sys
import os

# Add parent directory to path for common imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common.export_reader import discover_scenarios, load_scenario
from common.metrics import validate_scenario, format_validation_report
from common.xlsx_generator import generate_scenario_xlsx, generate_comparison_xlsx


EXPERIMENT_NAME = "Rees & Slater (2024) — Boil Water Advisory"
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
SPREADSHEETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "spreadsheets")
RESULTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")

# Expected scenarios (9 usable, scenario 10 is bibliography)
EXPECTED_SCENARIOS = [
    "baseline",
    "double-water",
    "ext-stewing-time",
    "linear-temp-increment",
    "normal-dist-temp",
    "random-uniform-temp",
    # Additional deterministic scenarios as named in the model
]


def main():
    os.makedirs(SPREADSHEETS_DIR, exist_ok=True)
    os.makedirs(RESULTS_DIR, exist_ok=True)

    # Discover scenarios
    scenarios = discover_scenarios(DATA_DIR)
    if not scenarios:
        print(f"No scenario files found in {DATA_DIR}/")
        print("Place FlowFRAM JSON exports (3 files per scenario) in the data/ folder.")
        print("Expected naming: {scenario}-complexity-metrics-results-*.json")
        print("                 {scenario}-statistics-results-*.json")
        print("                 {scenario}-message-flow-results-*.json")
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

        # 1. Generate XLSX with formulas
        xlsx_path = os.path.join(
            SPREADSHEETS_DIR,
            f"{sf.scenario_name}-analysis.xlsx"
        )
        generate_scenario_xlsx(
            experiment_name=EXPERIMENT_NAME,
            scenario_name=sf.scenario_name,
            cm=cm,
            stats=stats,
            output_path=xlsx_path,
        )
        print(f"  ✓ Spreadsheet: {xlsx_path}")

        # 2. Validate metrics
        results = validate_scenario(cm, stats)
        report = format_validation_report(EXPERIMENT_NAME, sf.scenario_name, results)
        all_reports.append(report)

        passed = sum(1 for r in results if r.passed)
        total = len(results)
        print(f"  ✓ Validation: {passed}/{total} checks passed")

        # Collect for comparison
        comparison_data.append((sf.scenario_name, cm))

    # 3. Generate cross-scenario comparison spreadsheet
    if len(comparison_data) > 1:
        comparison_path = os.path.join(SPREADSHEETS_DIR, "scenario-comparison.xlsx")
        generate_comparison_xlsx(EXPERIMENT_NAME, comparison_data, comparison_path)
        print(f"\n✓ Comparison spreadsheet: {comparison_path}")

    # 4. Write validation report
    report_path = os.path.join(RESULTS_DIR, "validation-report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n\n---\n\n".join(all_reports))
    print(f"✓ Validation report: {report_path}")

    print(f"\n{'='*60}")
    print(f"  Done. {len(scenarios)} scenario(s) processed.")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
