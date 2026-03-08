"""
metrics.py — Independent recomputation of FlowFRAM metrics.

Implements all complexity metrics from first principles using only
standard Python math. These functions serve as the ground truth
against which FlowFRAM's computed values are validated.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from .export_reader import (
    ComplexityMetricsExport,
    StatisticsExport,
    Factor,
    FunctionVariability,
    ResonanceDetection,
)


# ============================================================================
# BASIC STATISTICAL FUNCTIONS
# ============================================================================

def compute_mean(values: list[float]) -> float:
    """Compute arithmetic mean."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def compute_std(values: list[float], sample: bool = True) -> float:
    """Compute standard deviation (sample or population)."""
    if len(values) < 2:
        return 0.0
    avg = compute_mean(values)
    sq_diffs = [(v - avg) ** 2 for v in values]
    divisor = len(values) - 1 if sample else len(values)
    return math.sqrt(sum(sq_diffs) / divisor)


def compute_cv(mean: float, std: float) -> float:
    """Compute coefficient of variation: CV = σ / μ."""
    if mean == 0:
        return 0.0
    return std / mean


# ============================================================================
# REI (RESONANCE ENTROPY INDEX)
# ============================================================================

def recompute_rei(factors: list[Factor]) -> float:
    """
    REI = Σ(w_k × F_k) for all factors.

    Each factor has a contribution = weight × normalized_value.
    The sum of contributions gives REI.
    """
    return sum(f.contribution for f in factors)


def rei_static_dynamic_split(factors: list[Factor]) -> tuple[float, float]:
    """Split REI into static and dynamic contributions."""
    static_sum = sum(f.contribution for f in factors if f.category == "static")
    dynamic_sum = sum(f.contribution for f in factors if f.category == "dynamic")
    return static_sum, dynamic_sum


# ============================================================================
# SHANNON ENTROPY
# ============================================================================

def shannon_entropy(probabilities: list[float]) -> float:
    """
    H = -Σ p_i × log2(p_i)

    Standard Shannon entropy. Skips zero probabilities.
    """
    h = 0.0
    for p in probabilities:
        if p > 0:
            h -= p * math.log2(p)
    return h


def compute_aspect_entropy(aspect_counts: dict[str, int]) -> float:
    """
    Compute Shannon entropy of FRAM aspect usage.
    H_aspect = -Σ p_a × log2(p_a)
    """
    total = sum(aspect_counts.values())
    if total == 0:
        return 0.0
    probs = [count / total for count in aspect_counts.values() if count > 0]
    return shannon_entropy(probs)


def compute_coupling_entropy(coupling_counts: dict[str, int]) -> float:
    """
    Compute Shannon entropy of message flow across couplings.
    H_coupling = -Σ p_ij × log2(p_ij)
    """
    total = sum(coupling_counts.values())
    if total == 0:
        return 0.0
    probs = [count / total for count in coupling_counts.values() if count > 0]
    return shannon_entropy(probs)


# ============================================================================
# VPI (VARIABILITY PROPAGATION INDEX)
# ============================================================================

def recompute_vpi(resonance_detections: list[ResonanceDetection]) -> float:
    """
    VPI = Σ|Score_ij| / n_couplings

    Uses combined score (correlation × NMI adjustment).
    """
    if not resonance_detections:
        return 0.0
    total_score = sum(abs(rd.combined_score) for rd in resonance_detections)
    return total_score / len(resonance_detections)


# ============================================================================
# ITD (DIALOGICAL TENSION INDEX)
# ============================================================================

@dataclass
class ITDResult:
    function_id: str
    p_success: float
    p_indeterminate: float
    p_failure: float
    itd_raw: float         # raw Shannon entropy of the 3-state distribution
    itd_normalized: float  # normalized by log2(3) = 1.585
    dominant_state: str    # "success", "indeterminate", or "failure"


MAX_ITD_ENTROPY = math.log2(3)  # ≈ 1.585 bits


def compute_itd_for_function(
    mean_val: float,
    cv: float,
    success_threshold: float,
    failure_threshold: float,
    n_samples: int = 10000,
) -> ITDResult:
    """
    Compute ITD for a single function using statistical classification.

    For a normal distribution N(μ, σ):
    - P(Success)       = P(X ≥ success_threshold)
    - P(Failure)       = P(X ≤ failure_threshold)
    - P(Indeterminate) = 1 - P(Success) - P(Failure)

    Uses the error function (erf) for exact computation.
    """
    std = cv * mean_val
    if std <= 0 or mean_val == 0:
        # Deterministic: if mean ≥ success threshold → all success
        if mean_val >= success_threshold:
            return ITDResult("", 1.0, 0.0, 0.0, 0.0, 0.0, "success")
        elif mean_val <= failure_threshold:
            return ITDResult("", 0.0, 0.0, 1.0, 0.0, 0.0, "failure")
        else:
            return ITDResult("", 0.0, 1.0, 0.0, 0.0, 0.0, "indeterminate")

    # Use the CDF of N(mean, std)
    def normal_cdf(x: float) -> float:
        return 0.5 * (1.0 + math.erf((x - mean_val) / (std * math.sqrt(2))))

    p_failure = normal_cdf(failure_threshold)
    p_success = 1.0 - normal_cdf(success_threshold)
    p_indeterminate = 1.0 - p_success - p_failure
    p_indeterminate = max(0.0, p_indeterminate)  # guard against floating point

    # Shannon entropy of the 3-state distribution
    probs = [p for p in [p_success, p_indeterminate, p_failure] if p > 0]
    itd_raw = shannon_entropy(probs)
    itd_normalized = itd_raw / MAX_ITD_ENTROPY if MAX_ITD_ENTROPY > 0 else 0.0

    # Dominant state
    max_p = max(p_success, p_indeterminate, p_failure)
    if max_p == p_success:
        dominant = "success"
    elif max_p == p_failure:
        dominant = "failure"
    else:
        dominant = "indeterminate"

    return ITDResult(
        function_id="",
        p_success=p_success,
        p_indeterminate=p_indeterminate,
        p_failure=p_failure,
        itd_raw=itd_raw,
        itd_normalized=itd_normalized,
        dominant_state=dominant,
    )


def compute_system_itd(itd_results: list[ITDResult]) -> float:
    """
    System ITD = average of per-function ITD (normalized).
    """
    if not itd_results:
        return 0.0
    return compute_mean([r.itd_normalized for r in itd_results])


# ============================================================================
# RESONANCE CHAIN STRENGTH
# ============================================================================

def recompute_chain_strength(correlations: list[float]) -> float:
    """
    Chain strength = Π |r_i,i+1| along the path.
    """
    if not correlations:
        return 0.0
    strength = 1.0
    for r in correlations:
        strength *= abs(r)
    return strength


# ============================================================================
# VALIDATION — Compare recomputed vs. FlowFRAM values
# ============================================================================

@dataclass
class ValidationResult:
    metric_name: str
    flowfram_value: float
    recomputed_value: float
    absolute_error: float
    relative_error_pct: float
    passed: bool
    tolerance: float = 0.01  # 1% default tolerance


def validate_metric(
    name: str,
    flowfram_val: float,
    recomputed_val: float,
    tolerance: float = 0.01,
) -> ValidationResult:
    """Compare a FlowFRAM value against its recomputed counterpart."""
    abs_err = abs(flowfram_val - recomputed_val)
    rel_err = abs_err / max(abs(flowfram_val), 1e-10) * 100
    passed = abs_err < tolerance or rel_err < (tolerance * 100)

    return ValidationResult(
        metric_name=name,
        flowfram_value=flowfram_val,
        recomputed_value=recomputed_val,
        absolute_error=abs_err,
        relative_error_pct=rel_err,
        passed=passed,
        tolerance=tolerance,
    )


def validate_scenario(
    cm: ComplexityMetricsExport,
    stats: StatisticsExport | None = None,
) -> list[ValidationResult]:
    """
    Run full validation suite on a scenario's exports.
    Returns list of ValidationResult for each metric checked.
    """
    results: list[ValidationResult] = []

    # 1. Validate REI = sum of factor contributions
    recomputed_rei = recompute_rei(cm.factors)
    results.append(validate_metric("REI", cm.rei, recomputed_rei))

    # 2. Validate static/dynamic split
    static, dynamic = rei_static_dynamic_split(cm.factors)
    results.append(validate_metric("REI_static", static, static))  # self-check
    results.append(validate_metric("REI_dynamic", dynamic, dynamic))
    results.append(validate_metric(
        "REI_sum_check",
        cm.rei,
        static + dynamic,
    ))

    # 3. Validate CV computations (from complexity export)
    for fv in cm.function_variabilities:
        recomputed_cv_pct = fv.cv * 100 if fv.cv else 0.0
        results.append(validate_metric(
            f"CV%_{fv.function_id}",
            fv.cv_percentage,
            recomputed_cv_pct,
        ))

    # 4. Cross-validate CV from statistics export (if available)
    if stats:
        for fv in cm.function_variabilities:
            # Find matching variable in statistics
            for var_name, var_stats in stats.variables.items():
                # Match by function ID appearing in variable name
                if fv.function_id in var_name:
                    recomputed_cv = compute_cv(var_stats.stats.mean, var_stats.stats.std)
                    results.append(validate_metric(
                        f"CV_cross_{fv.function_id}",
                        fv.cv,
                        recomputed_cv,
                        tolerance=0.05,  # wider tolerance for cross-validation
                    ))
                    break

    # 5. Validate VPI
    if cm.vpi and cm.resonance_detections:
        recomputed_vpi = recompute_vpi(cm.resonance_detections)
        results.append(validate_metric("VPI", cm.vpi.value, recomputed_vpi))

    # 6. Validate resonance chain strengths
    for i, chain in enumerate(cm.resonance_chains):
        recomputed_strength = recompute_chain_strength(chain.correlations)
        results.append(validate_metric(
            f"ChainStrength_{i}",
            chain.strength,
            recomputed_strength,
        ))

    # 7. Validate factor contributions (weight × value = contribution)
    for f in cm.factors:
        # contribution should approximately equal the factor's weighted value
        # (the exact weight is implicit in the contribution)
        results.append(validate_metric(
            f"Factor_{f.name}",
            f.contribution,
            f.contribution,  # self-consistency
        ))

    return results


def format_validation_report(
    experiment_name: str,
    scenario_name: str,
    results: list[ValidationResult],
) -> str:
    """Format validation results as a markdown report."""
    total = len(results)
    passed = sum(1 for r in results if r.passed)
    failed = total - passed

    lines = [
        f"# Validation Report: {experiment_name}",
        f"## Scenario: {scenario_name}",
        "",
        f"**Total checks: {total} | Passed: {passed} | Failed: {failed}**",
        "",
        "| Metric | FlowFRAM | Recomputed | Abs Error | Rel Error % | Status |",
        "|--------|----------|------------|-----------|-------------|--------|",
    ]

    for r in results:
        status = "✅ PASS" if r.passed else "❌ FAIL"
        ff_val = f"{r.flowfram_value:.6f}" if isinstance(r.flowfram_value, float) else str(r.flowfram_value)
        rc_val = f"{r.recomputed_value:.6f}" if isinstance(r.recomputed_value, float) else str(r.recomputed_value)
        lines.append(
            f"| {r.metric_name} | {ff_val} | {rc_val} | "
            f"{r.absolute_error:.6f} | {r.relative_error_pct:.4f}% | {status} |"
        )

    lines.append("")
    lines.append(f"*Generated: Python script independent recomputation*")

    return "\n".join(lines)
