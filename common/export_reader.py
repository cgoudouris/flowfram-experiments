"""
export_reader.py — Read and parse FlowFRAM JSON export files.

FlowFRAM produces 3 JSON exports per scenario:
  1. *-complexity-metrics-results-*.json  — REI, factors, resonance, chains, barriers
  2. *-statistics-results-*.json          — Per-variable descriptive statistics
  3. *-message-flow-results-*.json        — Raw message trace

This module provides unified readers for all three formats.
"""
from __future__ import annotations

import json
import os
import glob
import re
from dataclasses import dataclass, field
from typing import Any


# ============================================================================
# DATA CLASSES
# ============================================================================

@dataclass
class FunctionVariability:
    function_id: str
    cv: float
    cv_percentage: float
    mean: float
    precision_phenotype: str = "N/A"
    variability_level: str = "low"


@dataclass
class ResonanceDetection:
    upstream: str
    downstream: str
    aspect: str
    correlation: float
    nmi: float | None = None
    combined_score: float = 0.0
    transfer_entropy: float | None = None
    transfer_entropy_reverse: float | None = None
    net_transfer_entropy: float | None = None
    te_confidence: str | None = None
    type: str = "unknown"  # amplifying, dampening, neutral


@dataclass
class Factor:
    name: str
    value: float
    contribution: float
    category: str = "static"  # static or dynamic


@dataclass
class ResonanceChain:
    path: list[str] = field(default_factory=list)
    correlations: list[float] = field(default_factory=list)
    strength: float = 0.0
    type: str = "unknown"
    display: str = ""


@dataclass
class BarrierFunction:
    function_id: str
    incoming_correlation: float
    outgoing_correlation: float
    cv: float
    damping_ratio: float
    effectiveness: str = "unknown"


@dataclass
class AspectVariability:
    aspect: str
    full_name: str
    cv: float
    cv_percentage: float
    mean: float
    count: int
    variability_level: str = "low"


@dataclass
class VariableVariability:
    name: str
    cv: float
    cv_percentage: float
    mean: float
    min_value: float = 0.0
    max_value: float = 0.0
    range: float = 0.0
    functions: list[str] = field(default_factory=list)
    aspects: list[str] = field(default_factory=list)
    variability_level: str = "low"


@dataclass
class VPI:
    value: float
    type: str  # amplifying, dampening, neutral
    description: str = ""
    upstream_count: int = 0
    downstream_count: int = 0


@dataclass
class ComplexityMetricsExport:
    """Parsed complexity-metrics-results JSON export."""
    # Metadata
    export_date: str = ""
    iteration: int = 0
    total_iterations: int = 0
    # Summary
    rei: float = 0.0
    rei_percentage: float = 0.0
    status: str = "SAFE"
    thresholds: dict = field(default_factory=dict)
    # Detailed data
    factors: list[Factor] = field(default_factory=list)
    function_variabilities: list[FunctionVariability] = field(default_factory=list)
    resonance_detections: list[ResonanceDetection] = field(default_factory=list)
    vpi: VPI | None = None
    resonance_chains: list[ResonanceChain] = field(default_factory=list)
    barrier_functions: list[BarrierFunction] = field(default_factory=list)
    aspect_variabilities: list[AspectVariability] = field(default_factory=list)
    variable_variabilities: list[VariableVariability] = field(default_factory=list)
    history: list[float] = field(default_factory=list)
    stats: dict = field(default_factory=dict)
    # Epistemological extensions (V2/V3)
    entropy_synchronization: dict | None = None
    rei_composition: dict | None = None
    entropy_rate: dict | None = None
    transfer_entropy: dict | None = None
    # Raw JSON for additional access
    raw: dict = field(default_factory=dict)


@dataclass
class DescriptiveStats:
    count: int = 0
    mean: float = 0.0
    std: float = 0.0
    min: float = 0.0
    max: float = 0.0
    p5: float = 0.0
    p25: float = 0.0
    p50: float = 0.0
    p75: float = 0.0
    p95: float = 0.0
    variance: float = 0.0
    sum: float = 0.0


@dataclass
class VariableStatistics:
    variable_name: str
    stats: DescriptiveStats = field(default_factory=DescriptiveStats)
    histogram: list[dict] = field(default_factory=list)
    values: list[float] = field(default_factory=list)


@dataclass
class StatisticsExport:
    """Parsed statistics-results JSON export."""
    total_iterations: int = 0
    variables: dict[str, VariableStatistics] = field(default_factory=dict)
    timestamp: int = 0
    raw: dict = field(default_factory=dict)


@dataclass
class MessageFlowExport:
    """Parsed message-flow-results JSON export."""
    messages: list[dict] = field(default_factory=list)
    total_count: int = 0
    raw: dict = field(default_factory=dict)


# ============================================================================
# PARSERS
# ============================================================================

def read_complexity_metrics(filepath: str) -> ComplexityMetricsExport:
    """Read a complexity-metrics-results JSON export."""
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    result = ComplexityMetricsExport(raw=data)

    # Metadata
    meta = data.get("metadata", {})
    result.export_date = meta.get("exportDate", "")
    result.iteration = meta.get("iteration", 0)
    result.total_iterations = meta.get("totalIterations", 0)

    # Summary
    summary = data.get("summary", {})
    result.rei = summary.get("rei", 0.0)
    result.rei_percentage = summary.get("reiPercentage", 0.0)
    result.status = summary.get("status", "SAFE")
    result.thresholds = summary.get("thresholds", {})

    # Factors
    for f in data.get("factors", []):
        result.factors.append(Factor(
            name=f.get("name", ""),
            value=f.get("value", 0.0),
            contribution=f.get("contribution", 0.0),
            category=f.get("category", "static"),
        ))

    # Function variabilities
    for fv in data.get("functionVariabilities", []):
        result.function_variabilities.append(FunctionVariability(
            function_id=fv.get("functionId", ""),
            cv=fv.get("cv", 0.0),
            cv_percentage=fv.get("cvPercentage", 0.0),
            mean=fv.get("mean", 0.0),
            precision_phenotype=fv.get("precisionPhenotype", "N/A"),
            variability_level=fv.get("variabilityLevel", "low"),
        ))

    # Resonance detections
    for rd in data.get("resonanceDetections", []):
        result.resonance_detections.append(ResonanceDetection(
            upstream=rd.get("upstream", ""),
            downstream=rd.get("downstream", ""),
            aspect=rd.get("aspect", ""),
            correlation=rd.get("correlation", 0.0),
            nmi=rd.get("nmi"),
            combined_score=rd.get("combinedScore", rd.get("correlation", 0.0)),
            transfer_entropy=rd.get("transferEntropy"),
            transfer_entropy_reverse=rd.get("transferEntropyReverse"),
            net_transfer_entropy=rd.get("netTransferEntropy"),
            te_confidence=rd.get("teConfidence"),
            type=rd.get("type", "unknown"),
        ))

    # VPI
    vpi_data = data.get("vpi")
    if vpi_data:
        result.vpi = VPI(
            value=vpi_data.get("value", 0.0),
            type=vpi_data.get("type", "neutral"),
            description=vpi_data.get("description", ""),
            upstream_count=vpi_data.get("upstreamCount", 0),
            downstream_count=vpi_data.get("downstreamCount", 0),
        )

    # Resonance chains
    for chain in data.get("resonanceChains", []):
        result.resonance_chains.append(ResonanceChain(
            path=chain.get("path", []),
            correlations=chain.get("correlations", []),
            strength=chain.get("strength", 0.0),
            type=chain.get("type", "unknown"),
            display=chain.get("display", ""),
        ))

    # Barrier functions
    for bf in data.get("barrierFunctions", []):
        result.barrier_functions.append(BarrierFunction(
            function_id=bf.get("functionId", ""),
            incoming_correlation=bf.get("incomingCorrelation", 0.0),
            outgoing_correlation=bf.get("outgoingCorrelation", 0.0),
            cv=bf.get("cv", 0.0),
            damping_ratio=bf.get("dampingRatio", 0.0),
            effectiveness=bf.get("effectiveness", "unknown"),
        ))

    # Aspect variabilities
    for av in data.get("aspectVariabilities", []):
        result.aspect_variabilities.append(AspectVariability(
            aspect=av.get("aspect", ""),
            full_name=av.get("fullName", ""),
            cv=av.get("cv", 0.0),
            cv_percentage=av.get("cvPercentage", 0.0),
            mean=av.get("mean", 0.0),
            count=av.get("count", 0),
            variability_level=av.get("variabilityLevel", "low"),
        ))

    # Variable variabilities
    for vv in data.get("variableVariabilities", []):
        result.variable_variabilities.append(VariableVariability(
            name=vv.get("name", ""),
            cv=vv.get("cv", 0.0),
            cv_percentage=vv.get("cvPercentage", 0.0),
            mean=vv.get("mean", 0.0),
            min_value=vv.get("minValue", 0.0),
            max_value=vv.get("maxValue", 0.0),
            range=vv.get("range", 0.0),
            functions=vv.get("functions", []),
            aspects=vv.get("aspects", []),
            variability_level=vv.get("variabilityLevel", "low"),
        ))

    # History and stats
    result.history = data.get("history", [])
    result.stats = data.get("stats", {})

    # Epistemological extensions
    result.entropy_synchronization = data.get("entropySynchronization")
    result.rei_composition = data.get("reiComposition")
    result.entropy_rate = data.get("entropyRate")
    result.transfer_entropy = data.get("transferEntropy")

    return result


def read_statistics(filepath: str) -> StatisticsExport:
    """Read a statistics-results JSON export."""
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    result = StatisticsExport(raw=data)
    result.total_iterations = data.get("totalIterations", 0)
    result.timestamp = data.get("timestamp", 0)

    for var_name, var_data in data.get("variables", {}).items():
        vs = VariableStatistics(variable_name=var_data.get("variableName", var_name))
        raw_stats = var_data.get("stats", {})
        vs.stats = DescriptiveStats(
            count=raw_stats.get("count", 0),
            mean=raw_stats.get("mean", 0.0),
            std=raw_stats.get("std", 0.0),
            min=raw_stats.get("min", 0.0),
            max=raw_stats.get("max", 0.0),
            p5=raw_stats.get("p5", 0.0),
            p25=raw_stats.get("p25", 0.0),
            p50=raw_stats.get("p50", 0.0),
            p75=raw_stats.get("p75", 0.0),
            p95=raw_stats.get("p95", 0.0),
            variance=raw_stats.get("variance", 0.0),
            sum=raw_stats.get("sum", 0.0),
        )
        vs.histogram = var_data.get("histogram", [])
        vs.values = var_data.get("values", [])
        result.variables[var_name] = vs

    return result


def read_message_flow(filepath: str) -> MessageFlowExport:
    """Read a message-flow-results JSON export."""
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Message flow can be a list directly or wrapped in an object
    if isinstance(data, list):
        messages = data
    else:
        messages = data.get("messages", data.get("data", []))

    return MessageFlowExport(
        messages=messages,
        total_count=len(messages),
        raw=data if isinstance(data, dict) else {"messages": data},
    )


# ============================================================================
# SCENARIO DISCOVERY
# ============================================================================

@dataclass
class ScenarioFiles:
    """Grouped files for a single scenario."""
    scenario_name: str
    complexity_metrics_file: str | None = None
    statistics_file: str | None = None
    message_flow_file: str | None = None


def discover_scenarios(data_dir: str) -> list[ScenarioFiles]:
    """
    Auto-discover scenario files in a data directory.

    Expects filenames following FlowFRAM export naming:
      {scenario-slug}-complexity-metrics-results-YYYY-MM-DD_HH-MM.json
      {scenario-slug}-statistics-results-YYYY-MM-DD_HH-MM.json
      {scenario-slug}-message-flow-results-YYYY-MM-DD_HH-MM.json

    Groups files by scenario prefix.
    """
    if not os.path.isdir(data_dir):
        return []

    all_files = sorted(glob.glob(os.path.join(data_dir, "*.json")))

    # Extract scenario prefix by removing the known suffixes
    scenario_map: dict[str, ScenarioFiles] = {}

    for filepath in all_files:
        basename = os.path.basename(filepath)

        # Match the file type
        cm_match = re.match(r"^(.+?)-complexity-metrics-results-.*\.json$", basename)
        st_match = re.match(r"^(.+?)-statistics-results-.*\.json$", basename)
        mf_match = re.match(r"^(.+?)-message-flow-results-.*\.json$", basename)

        if cm_match:
            prefix = cm_match.group(1)
            if prefix not in scenario_map:
                scenario_map[prefix] = ScenarioFiles(scenario_name=prefix)
            scenario_map[prefix].complexity_metrics_file = filepath
        elif st_match:
            prefix = st_match.group(1)
            if prefix not in scenario_map:
                scenario_map[prefix] = ScenarioFiles(scenario_name=prefix)
            scenario_map[prefix].statistics_file = filepath
        elif mf_match:
            prefix = mf_match.group(1)
            if prefix not in scenario_map:
                scenario_map[prefix] = ScenarioFiles(scenario_name=prefix)
            scenario_map[prefix].message_flow_file = filepath

    return sorted(scenario_map.values(), key=lambda s: s.scenario_name)


def load_scenario(sf: ScenarioFiles) -> tuple[
    ComplexityMetricsExport | None,
    StatisticsExport | None,
    MessageFlowExport | None,
]:
    """Load all available exports for a scenario."""
    cm = read_complexity_metrics(sf.complexity_metrics_file) if sf.complexity_metrics_file else None
    st = read_statistics(sf.statistics_file) if sf.statistics_file else None
    mf = read_message_flow(sf.message_flow_file) if sf.message_flow_file else None
    return cm, st, mf
