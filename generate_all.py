#!/usr/bin/env python3
"""
generate_all.py — Master script to run all 4 experiment validations.

Usage:
  python generate_all.py           # Run all experiments
  python generate_all.py --only patriarca-2024  # Run specific experiment

Each experiment:
  1. Reads FlowFRAM JSON exports from <experiment>/data/
  2. Recomputes metrics independently (Python, no FlowFRAM dependency)
  3. Generates XLSX spreadsheets with live Excel formulas
  4. Produces a validation report (Markdown)
"""

import argparse
import importlib
import os
import sys
import time

EXPERIMENTS = [
    "rees-slater-2024",
    "patriarca-2024",
    "qiao-2022",
    "slim-nadeau-2019",
]


def run_experiment(experiment_name: str) -> bool:
    """Run a single experiment's validation script."""
    exp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), experiment_name)
    validate_script = os.path.join(exp_dir, "validate.py")

    if not os.path.exists(validate_script):
        print(f"  ⚠ No validate.py found in {experiment_name}/")
        return False

    data_dir = os.path.join(exp_dir, "data")
    if not os.path.exists(data_dir) or not any(
        f.endswith(".json") for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f))
    ):
        print(f"  ⚠ No JSON exports in {experiment_name}/data/ — skipping")
        return False

    # Import and run the experiment's main()
    sys.path.insert(0, exp_dir)
    try:
        spec = importlib.util.spec_from_file_location(
            f"{experiment_name}.validate", validate_script
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.main()
        return True
    except Exception as e:
        print(f"  ✗ Error in {experiment_name}: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        if exp_dir in sys.path:
            sys.path.remove(exp_dir)


def main():
    parser = argparse.ArgumentParser(
        description="Generate validation spreadsheets and reports for all FlowFRAM experiments."
    )
    parser.add_argument(
        "--only",
        type=str,
        choices=EXPERIMENTS,
        help="Run only a specific experiment",
    )
    args = parser.parse_args()

    target_experiments = [args.only] if args.only else EXPERIMENTS

    print("=" * 70)
    print("  FlowFRAM Experiment Reproducibility — Validation & Spreadsheet Generator")
    print(f"  Experiments: {len(target_experiments)}")
    print("=" * 70)
    print()

    results = {}
    t0 = time.time()

    for exp in target_experiments:
        print(f"\n{'─'*70}")
        print(f"  Experiment: {exp}")
        print(f"{'─'*70}\n")
        success = run_experiment(exp)
        results[exp] = success

    elapsed = time.time() - t0

    # Summary
    print(f"\n{'='*70}")
    print("  Summary")
    print(f"{'='*70}")
    for exp, success in results.items():
        status = "✅ Done" if success else "⚠ Skipped / Error"
        print(f"  {exp}: {status}")
    print(f"\n  Total time: {elapsed:.1f}s")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
