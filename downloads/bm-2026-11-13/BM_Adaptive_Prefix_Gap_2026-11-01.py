"""Reproducible finite cases for the prefix-probe adaptivity gap.

Source: BM_Adaptive_Seed_Diagnostics_2026-11-01.py.
The general theorem is proved separately; exhaustive checks are only small cases.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import product
from pathlib import Path
from runpy import run_path

_api = run_path(str(Path(__file__).with_name("BM_Adaptive_Seed_Diagnostics_2026-11-01.py")))
Probe = _api["Probe"]
optimal_strategy = _api["optimal_strategy"]
smallest_fixed_query_bundle = _api["smallest_fixed_query_bundle"]


def instance(depth: int):
    assert depth >= 1
    worlds = frozenset("".join(bits) for bits in product("01", repeat=depth))
    targets = {w: w for w in worlds}
    probes = []
    for prefix_length in range(depth):
        for bits in product("01", repeat=prefix_length):
            prefix = "".join(bits)
            probes.append(Probe(
                name="prefix:" + (prefix or "root"),
                cost=Fraction(1),
                outcomes={w: frozenset((w[prefix_length] if w.startswith(prefix)
                                          else "outside",)) for w in worlds},
                enabled=worlds,
            ))
    return worlds, targets, tuple(probes)


def run():
    checks = []
    for depth in range(1, 5):
        worlds, targets, probes = instance(depth)
        adaptive, _, _ = optimal_strategy(worlds, targets, probes)
        fixed = smallest_fixed_query_bundle(worlds, targets, probes)
        assert adaptive == depth
        assert fixed is not None and fixed[0] == 2 ** (depth - 1)
        checks.append({
            "binary_seed_depth": depth,
            "number_of_worlds": len(worlds),
            "number_of_declared_probes": len(probes),
            "optimal_adaptive_worst_case_cost": str(adaptive),
            "optimal_fixed_battery_cost": str(fixed[0]),
        })
    return {
        "theorem_scope": "finite prefix-restricted deterministic tests; positive unit costs",
        "small_case_exhaustive_verification": checks,
        "proven_for_arbitrary_depth": {
            "adaptive_cost": "depth",
            "nonadaptive_cost": "2^(depth-1)",
            "ratio": "2^(depth-1)/depth; unbounded",
        },
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
