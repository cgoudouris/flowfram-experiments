#!/usr/bin/env python3
"""
validate.py — Qiao et al. (2022) Maritime Emergency Response experiment.

Model: 25 functions, 50 edges, 10 scenarios
  - S0: Baseline (normal operations)
  - S1–S9: Degradation scenarios (individual and combined stress)

Key validation targets:
  - REI sensitivity across degradation levels
  - Barrier function identification
  - Resonance chain propagation paths
  - S5 vs S8 comparison (individual vs combined stress)

Article: Qiao, W. et al. (2022) — FRAM-BN coupled resilience assessment
"""
from __future__ import annotations

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common.export_reader import discover_scenarios, load_scenario
from common.metrics import validate_scenario, format_validation_report
from common.xlsx_generator import generate_scenario_xlsx, generate_comparison_xlsx


EXPERIMENT_NAME = "Qiao et al. (2022) — Maritime Emergency Response (FRAM-BN)"
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
SPREADSHEETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "spreadsheets")
RESULTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")


def validate_degradation_ordering(comparison_data, all_reports):
    """
    Article-specific: Verify that degradation scenarios produce
    higher REI than baseline.
    """
    if len(comparison_data) < 2:
        return

    baseline_rei = comparison_data[0][1].rei
    lines = [
        "## Degradation Ordering Validation",
        "",
        f"Baseline REI: {baseline_rei:.4f}",
        "",
        "| Scenario | REI | ΔREI | Higher than baseline? |",
        "|----------|-----|------|----------------------|",
    ]

    for name, cm in comparison_data:
        delta = cm.rei - baseline_rei
        higher = "✅ Yes" if cm.rei > baseline_rei else ("➖ Equal" if abs(delta) < 0.001 else "❌ No")
        lines.append(f"| {name} | {cm.rei:.4f} | {delta:+.4f} | {higher} |")

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

        # 2. Validate
        results = validate_scenario(cm, stats)
        report = format_validation_report(EXPERIMENT_NAME, sf.scenario_name, results)
        all_reports.append(report)

        passed = sum(1 for r in results if r.passed)
        total = len(results)
        print(f"  ✓ Validation: {passed}/{total} checks passed")

        comparison_data.append((sf.scenario_name, cm))

    # 3. Degradation ordering check
    validate_degradation_ordering(comparison_data, all_reports)

    # 4. Cross-scenario comparison
    if len(comparison_data) > 1:
        comp_path = os.path.join(SPREADSHEETS_DIR, "scenario-comparison.xlsx")
        generate_comparison_xlsx(EXPERIMENT_NAME, comparison_data, comp_path)
        print(f"\n✓ Comparison spreadsheet: {comp_path}")

    # 5. Write report
    report_path = os.path.join(RESULTS_DIR, "validation-report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n\n---\n\n".join(all_reports))
    print(f"✓ Validation report: {report_path}")

    print(f"\n{'='*60}")
    print(f"  Done. {len(scenarios)} scenario(s) processed.")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
