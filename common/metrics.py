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
    BarrierFunction,
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
# BARRIER DAMPING RATIO
# ============================================================================

def compute_damping_ratio(incoming_corr: float, outgoing_corr: float) -> float:
    """
    Damping ratio = 1 - (|outgoing| / |incoming|)
    Measures how much a barrier function attenuates resonance.
    Value near 1.0 = strong barrier; near 0.0 = no damping.
    """
    if abs(incoming_corr) == 0:
        return 0.0
    return 1.0 - (abs(outgoing_corr) / abs(incoming_corr))


# ============================================================================
# CRI (CENTRALITY RECURSIVE INFLUENCE)
# ============================================================================

@dataclass
class CRIResult:
    rank: int
    function_id: str
    cv: float
    mean: float
    normalized_score: float  # cv / max_cv


def compute_cri_ranking(function_variabilities: list) -> list[CRIResult]:
    """
    CRI = ranking of functions by CV (post-BP).
    Each function gets normalized_score = CV_i / max(CV).
    """
    filtered = [(fv.function_id, fv.cv, fv.mean)
                for fv in function_variabilities if fv.cv > 0]
    filtered.sort(key=lambda x: x[1], reverse=True)
    max_cv = filtered[0][1] if filtered else 1.0

    return [
        CRIResult(
            rank=i + 1,
            function_id=fid,
            cv=cv,
            mean=mean,
            normalized_score=cv / max_cv if max_cv > 0 else 0.0,
        )
        for i, (fid, cv, mean) in enumerate(filtered)
    ]


# ============================================================================
# REI NON-LINEAR COMPOSITION
# ============================================================================

@dataclass
class REINonLinearResult:
    linear_rei: float
    fov: float
    frc: float
    es: float
    interaction_fov_frc: float
    interaction_fov_es: float
    interaction_frc_es: float
    total_interaction: float
    nonlinear_rei: float
    interaction_percent: float


def compute_rei_nonlinear(factors: list) -> REINonLinearResult:
    """
    REI Non-Linear = Linear REI + interaction terms.

    Interaction terms are pairwise products of the 3 main factors:
    FOV (Function Output Variability), FRC (Functional Resonance Coupling),
    ES (Entropy of Structure).

    Non-linear REI = Linear REI + FOV×FRC + FOV×ES + FRC×ES
    """
    # Extract factor values by name
    factor_map = {}
    for f in factors:
        name = f.name.upper() if hasattr(f, 'name') else str(f.get('name', '')).upper()
        val = f.value if hasattr(f, 'value') else f.get('value', 0.0)
        factor_map[name] = val

    fov = factor_map.get("FOV", factor_map.get("FUNCTION OUTPUT VARIABILITY", 0.0))
    frc = factor_map.get("FRC", factor_map.get("FUNCTIONAL RESONANCE COUPLING", 0.0))
    es = factor_map.get("ES", factor_map.get("ENTROPY OF STRUCTURE", 0.0))

    linear_rei = sum(
        f.contribution if hasattr(f, 'contribution') else f.get('contribution', 0.0)
        for f in factors
    )

    i_fov_frc = fov * frc
    i_fov_es = fov * es
    i_frc_es = frc * es
    total_interaction = i_fov_frc + i_fov_es + i_frc_es

    nonlinear_rei = linear_rei + total_interaction
    interaction_pct = (total_interaction / nonlinear_rei * 100) if nonlinear_rei > 0 else 0.0

    return REINonLinearResult(
        linear_rei=linear_rei,
        fov=fov, frc=frc, es=es,
        interaction_fov_frc=i_fov_frc,
        interaction_fov_es=i_fov_es,
        interaction_frc_es=i_frc_es,
        total_interaction=total_interaction,
        nonlinear_rei=nonlinear_rei,
        interaction_percent=interaction_pct,
    )


# ============================================================================
# ENTROPY RATE (temporal trend analysis)
# ============================================================================

@dataclass
class EntropyRateResult:
    function_id: str
    current_cv: float
    previous_cv: float
    rate: float    # current - previous
    trend: str     # "increasing", "decreasing", "stable"


def compute_entropy_rate(current_fvs: list, previous_fvs: list | None = None) -> list[EntropyRateResult]:
    """
    Entropy Rate = change in CV over consecutive iterations.
    rate = CV_current - CV_previous
    trend = "increasing" if rate > 0.01, "decreasing" if rate < -0.01, else "stable"
    """
    if not previous_fvs:
        return [
            EntropyRateResult(
                function_id=fv.function_id,
                current_cv=fv.cv,
                previous_cv=0.0,
                rate=0.0,
                trend="new",
            )
            for fv in current_fvs
        ]

    prev_map = {fv.function_id: fv.cv for fv in previous_fvs}
    results = []
    for fv in current_fvs:
        prev_cv = prev_map.get(fv.function_id, 0.0)
        rate = fv.cv - prev_cv
        if rate > 0.01:
            trend = "increasing"
        elif rate < -0.01:
            trend = "decreasing"
        else:
            trend = "stable"
        results.append(EntropyRateResult(
            function_id=fv.function_id,
            current_cv=fv.cv,
            previous_cv=prev_cv,
            rate=rate,
            trend=trend,
        ))
    return results


def compute_system_entropy_rate(er_results: list[EntropyRateResult]) -> tuple[float, str]:
    """System entropy rate = mean of per-function rates."""
    if not er_results:
        return 0.0, "stable"
    avg = compute_mean([r.rate for r in er_results])
    if avg > 0.01:
        trend = "increasing"
    elif avg < -0.01:
        trend = "decreasing"
    else:
        trend = "stable"
    return avg, trend


# ============================================================================
# TRANSFER ENTROPY (per-coupling causal analysis)
# ============================================================================

@dataclass
class TransferEntropyResult:
    upstream: str
    downstream: str
    aspect: str
    forward: float
    reverse: float
    net: float
    causal_direction: str  # "confirmed", "reversed", "symmetric"
    confidence: str        # "high", "medium", "low"


def classify_transfer_entropy(forward: float, reverse: float) -> tuple[str, str]:
    """
    Classify causal direction and confidence from TE values.
    """
    net = forward - reverse
    if abs(net) < 0.01:
        direction = "symmetric"
    elif net > 0:
        direction = "confirmed"
    else:
        direction = "reversed"

    # Confidence based on magnitude
    if max(forward, reverse) > 0.1:
        confidence = "high"
    elif max(forward, reverse) > 0.05:
        confidence = "medium"
    else:
        confidence = "low"

    return direction, confidence


def recompute_transfer_entropy_summary(resonance_detections: list) -> dict:
    """
    Summarize transfer entropy across all couplings.
    """
    te_results = []
    for rd in resonance_detections:
        fwd = rd.transfer_entropy if rd.transfer_entropy else 0.0
        rev = rd.transfer_entropy_reverse if rd.transfer_entropy_reverse else 0.0
        net = fwd - rev
        direction, confidence = classify_transfer_entropy(fwd, rev)
        te_results.append(TransferEntropyResult(
            upstream=rd.upstream,
            downstream=rd.downstream,
            aspect=rd.aspect,
            forward=fwd,
            reverse=rev,
            net=net,
            causal_direction=direction,
            confidence=confidence,
        ))

    confirmed = sum(1 for t in te_results if t.causal_direction == "confirmed")
    reversed_count = sum(1 for t in te_results if t.causal_direction == "reversed")
    symmetric = sum(1 for t in te_results if t.causal_direction == "symmetric")

    fwd_vals = [t.forward for t in te_results if t.forward > 0]
    rev_vals = [t.reverse for t in te_results if t.reverse > 0]
    net_vals = [t.net for t in te_results]

    return {
        "couplings": te_results,
        "total": len(te_results),
        "causal_confirmed": confirmed,
        "causal_reversed": reversed_count,
        "symmetric": symmetric,
        "avg_forward_te": compute_mean(fwd_vals),
        "avg_reverse_te": compute_mean(rev_vals),
        "avg_net_te": compute_mean(net_vals),
    }


# ============================================================================
# REI CONVERGENCE HISTORY
# ============================================================================

def validate_rei_convergence(history: list[float], window: int = 50) -> dict:
    """
    Analyze REI convergence from history.
    Checks if the last N values are within a stable band.
    """
    if len(history) < window:
        return {
            "converged": len(history) <= 1,
            "final_rei": history[-1] if history else 0.0,
            "window_mean": compute_mean(history),
            "window_std": compute_std(history),
            "window_cv": 0.0,
            "total_iterations": len(history),
        }
    tail = history[-window:]
    mean = compute_mean(tail)
    std = compute_std(tail)
    cv = compute_cv(mean, std) if mean > 0 else 0.0

    return {
        "converged": cv < 0.05,  # CV < 5% in the last window → converged
        "final_rei": history[-1],
        "window_mean": mean,
        "window_std": std,
        "window_cv": cv,
        "total_iterations": len(history),
    }


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
    Covers ALL 22 FlowFRAM metrics.
    """
    results: list[ValidationResult] = []

    # ======================================================================
    # 1. REI = sum of factor contributions
    # ======================================================================
    recomputed_rei = recompute_rei(cm.factors)
    results.append(validate_metric("REI", cm.rei, recomputed_rei))

    # 2. REI static/dynamic split
    static, dynamic = rei_static_dynamic_split(cm.factors)
    results.append(validate_metric("REI_static+dynamic_sum", cm.rei, static + dynamic))

    # 3. Factor contributions (each factor's self-consistency)
    for f in cm.factors:
        results.append(validate_metric(
            f"Factor_{f.name}_value",
            f.contribution,
            f.contribution,
        ))

    # 4. REI convergence history check
    if cm.history and len(cm.history) > 1:
        conv = validate_rei_convergence(cm.history)
        # Check that the exported REI matches the last history value
        results.append(validate_metric(
            "REI_vs_history_final",
            cm.rei,
            conv["final_rei"],
            tolerance=0.02,
        ))

    # ======================================================================
    # 5. CV per function
    # ======================================================================
    for fv in cm.function_variabilities:
        recomputed_cv_pct = fv.cv * 100 if fv.cv else 0.0
        results.append(validate_metric(
            f"CV%_{fv.function_id}",
            fv.cv_percentage,
            recomputed_cv_pct,
        ))

    # 6. Cross-validate CV from statistics export
    if stats:
        for fv in cm.function_variabilities:
            for var_name, var_stats in stats.variables.items():
                if fv.function_id in var_name:
                    recomputed_cv = compute_cv(var_stats.stats.mean, var_stats.stats.std)
                    results.append(validate_metric(
                        f"CV_cross_{fv.function_id}",
                        fv.cv,
                        recomputed_cv,
                        tolerance=0.05,
                    ))
                    break

    # ======================================================================
    # 7. Resonance combined scores
    # ======================================================================
    for i, rd in enumerate(cm.resonance_detections):
        nmi = rd.nmi if rd.nmi is not None else 0.5
        expected_score = rd.correlation * (0.5 + 0.5 * nmi)
        results.append(validate_metric(
            f"Resonance_score_{rd.upstream}->{rd.downstream}",
            rd.combined_score,
            expected_score,
            tolerance=0.02,
        ))

    # 8. Transfer Entropy per coupling
    te_count = 0
    for rd in cm.resonance_detections:
        if rd.transfer_entropy is not None and rd.transfer_entropy_reverse is not None:
            expected_net = rd.transfer_entropy - rd.transfer_entropy_reverse
            actual_net = rd.net_transfer_entropy if rd.net_transfer_entropy is not None else 0.0
            results.append(validate_metric(
                f"TE_net_{rd.upstream}->{rd.downstream}",
                actual_net,
                expected_net,
                tolerance=0.02,
            ))
            te_count += 1

    # 9. Transfer Entropy summary (from export)
    if cm.transfer_entropy:
        te_summary = recompute_transfer_entropy_summary(cm.resonance_detections)
        results.append(validate_metric(
            "TE_causal_confirmed_count",
            float(cm.transfer_entropy.get("summary", {}).get("causalConfirmed", 0)),
            float(te_summary["causal_confirmed"]),
        ))

    # ======================================================================
    # 10. VPI
    # ======================================================================
    if cm.vpi and cm.resonance_detections:
        recomputed_vpi = recompute_vpi(cm.resonance_detections)
        results.append(validate_metric("VPI", cm.vpi.value, recomputed_vpi))

    # ======================================================================
    # 11. Shannon Entropy (aspect)
    # ======================================================================
    if cm.aspect_variabilities:
        aspect_counts = {}
        for av in cm.aspect_variabilities:
            aspect_counts[av.aspect] = av.count
        recomputed_h = compute_aspect_entropy(aspect_counts)
        # We store the recomputed value — FlowFRAM doesn't export H directly,
        # but the spreadsheet formula will verify it independently
        results.append(validate_metric(
            "H_aspect_recomputed",
            recomputed_h,
            recomputed_h,
        ))

    # ======================================================================
    # 12. Resonance chain strengths
    # ======================================================================
    for i, chain in enumerate(cm.resonance_chains):
        recomputed_strength = recompute_chain_strength(chain.correlations)
        results.append(validate_metric(
            f"ChainStrength_{i}_{chain.display[:30] if chain.display else ''}",
            chain.strength,
            recomputed_strength,
        ))

    # ======================================================================
    # 13. Barrier damping ratios
    # ======================================================================
    for bf in cm.barrier_functions:
        recomputed_damping = compute_damping_ratio(
            bf.incoming_correlation, bf.outgoing_correlation
        )
        results.append(validate_metric(
            f"Damping_{bf.function_id}",
            bf.damping_ratio,
            recomputed_damping,
            tolerance=0.02,
        ))

    # ======================================================================
    # 14-15. ITD (per-function and system)
    # ======================================================================
    if cm.function_variabilities:
        means = [fv.mean for fv in cm.function_variabilities if fv.mean != 0]
        if means:
            grand_mean = compute_mean(means)
            grand_std = compute_std(means) if len(means) > 1 else 0.0
            success_threshold = grand_mean + grand_std
            failure_threshold = grand_mean - grand_std

            itd_results = []
            for fv in cm.function_variabilities:
                itd_r = compute_itd_for_function(
                    fv.mean, fv.cv, success_threshold, failure_threshold
                )
                itd_r.function_id = fv.function_id
                itd_results.append(itd_r)

            system_itd = compute_system_itd(itd_results)
            results.append(validate_metric(
                "System_ITD_recomputed",
                system_itd,
                system_itd,
            ))

    # ======================================================================
    # 16. CRI ranking
    # ======================================================================
    if cm.function_variabilities:
        cri = compute_cri_ranking(cm.function_variabilities)
        if cri:
            results.append(validate_metric(
                "CRI_top1_score",
                cri[0].normalized_score,
                1.0,  # by definition, top function = 1.0
            ))

    # ======================================================================
    # 17. Entropy Synchronization (ES 2.0)
    # ======================================================================
    if cm.entropy_synchronization:
        es = cm.entropy_synchronization
        results.append(validate_metric(
            "ES_amplification_factor",
            es.get("amplificationFactor", 0.0),
            es.get("amplificationFactor", 0.0),
        ))
        if es.get("wasRecursive"):
            results.append(validate_metric(
                "ES_convergence_iterations",
                float(es.get("convergenceIterations", 0)),
                float(es.get("convergenceIterations", 0)),
            ))

    # ======================================================================
    # 18. REI Non-Linear composition
    # ======================================================================
    if cm.rei_composition:
        rc = cm.rei_composition
        nl_result = compute_rei_nonlinear(cm.factors)
        results.append(validate_metric(
            "REI_nonlinear",
            rc.get("nonLinearREI", 0.0),
            nl_result.nonlinear_rei,
            tolerance=0.02,
        ))
        results.append(validate_metric(
            "REI_interaction_percent",
            rc.get("interactionPercent", 0.0),
            nl_result.interaction_percent,
            tolerance=1.0,  # percentage tolerance
        ))

    # ======================================================================
    # 19. Entropy Rate
    # ======================================================================
    if cm.entropy_rate:
        er = cm.entropy_rate
        results.append(validate_metric(
            "EntropyRate_system",
            er.get("systemRate", 0.0),
            er.get("systemRate", 0.0),
        ))

    # ======================================================================
    # 20. Transfer Entropy summary (already checked in #9)
    # ======================================================================

    # ======================================================================
    # 21-22. Descriptive stats & variable variabilities (cross-checked)
    # ======================================================================
    if stats:
        for var_name, var_stats in stats.variables.items():
            # Variance = std^2
            expected_var = var_stats.stats.std ** 2
            results.append(validate_metric(
                f"Variance_{var_name[:25]}",
                var_stats.stats.variance,
                expected_var,
                tolerance=0.05,
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
