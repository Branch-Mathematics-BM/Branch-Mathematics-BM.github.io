"""No-probability finite adaptive Seed-law diagnosis under declared queries.

Only static worlds and passive observations are modeled. A probe's outcome set
is an adversarial set, not a probability law. The receiver's target may include
the mathematical task and Passport status. Python 3.10+, standard library.
"""

from __future__ import annotations

import json
import random
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from typing import Hashable


Obj = Hashable
INF = None


@dataclass(frozen=True)
class Probe:
    name: str
    cost: Fraction
    outcomes: dict[Obj, frozenset[Obj]]
    enabled: frozenset[Obj]

    def verify(self, worlds: frozenset[Obj]) -> None:
        assert self.cost > 0 and self.enabled <= worlds
        assert set(self.outcomes) == set(self.enabled)
        assert all(self.outcomes[w] for w in self.enabled)


def deterministic(name: str, values: dict, cost=1, enabled=None) -> Probe:
    domains = frozenset(values) if enabled is None else frozenset(enabled)
    return Probe(name, Fraction(cost), {w: frozenset((values[w],)) for w in domains}, domains)


def query_successors(candidates: frozenset[Obj], probe: Probe):
    """Return possible retained world sets conditional on each observed value."""
    if not candidates <= probe.enabled:
        return ()
    observations = set().union(*(probe.outcomes[w] for w in candidates))
    return tuple(
        (value, frozenset(w for w in candidates if value in probe.outcomes[w]))
        for value in sorted(observations, key=repr)
    )


def optimal_strategy(worlds: frozenset[Obj], targets: dict, probes: tuple[Probe, ...]):
    assert worlds and set(targets) == set(worlds)
    for probe in probes:
        probe.verify(worlds)
    memo = {}

    @lru_cache(maxsize=None)
    def solve(candidates: frozenset[Obj]):
        task_values = {targets[w] for w in candidates}
        if len(task_values) == 1:
            record = (Fraction(0), {"resolved": repr(next(iter(task_values)))})
            memo[candidates] = record
            return record
        best = None
        for probe in probes:
            split = query_successors(candidates, probe)
            if not split or any(part == candidates for _, part in split):
                # In a static, worst-case model, this possible non-progress
                # observation can be adversarially repeated forever.
                continue
            branches = [(outcome, solve(part)) for outcome, part in split]
            if any(answer[0] is None for _, answer in branches):
                continue
            score = probe.cost + max(answer[0] for _, answer in branches)
            if best is None or score < best[0]:
                best = (score, {"ask": probe.name, "branches": {
                    repr(outcome): answer[1] for outcome, answer in branches
                }})
        result = best if best is not None else (None, {"unresolved": [repr(v) for v in task_values]})
        memo[candidates] = result
        return result

    value, tree = solve(worlds)
    return value, tree, memo


def independent_explicit_cost(candidates, targets, probes):
    """Exhaustively evaluate all strictly-progressing first-probe choices.

    Independent, deliberately nonmemoized recurrence; used only for tiny sets.
    """
    if len({targets[w] for w in candidates}) == 1:
        return Fraction(0)
    scores = []
    for probe in probes:
        if not candidates <= probe.enabled:
            continue
        observed = set().union(*(probe.outcomes[w] for w in candidates))
        parts = [frozenset(w for w in candidates if o in probe.outcomes[w]) for o in observed]
        if any(part == candidates for part in parts):
            continue
        subtree_values = [independent_explicit_cost(part, targets, probes) for part in parts]
        if all(value is not None for value in subtree_values):
            scores.append(probe.cost + max(subtree_values))
    return min(scores) if scores else None


def smallest_fixed_query_bundle(worlds, targets, probes):
    """A nonadaptive reference: all chosen deterministic queries are run.

    The result is exact for this declared finite deterministic catalogue.
    """
    assert all(all(len(v) == 1 for v in p.outcomes.values()) for p in probes)
    best = None
    for k in range(len(probes) + 1):
        for ids in combinations(range(len(probes)), k):
            selected = tuple(probes[i] for i in ids)
            if not all(worlds <= p.enabled for p in selected):
                continue
            codes = {w: tuple(next(iter(p.outcomes[w])) for p in selected) for w in worlds}
            if all(codes[x] != codes[y] or targets[x] == targets[y]
                   for x, y in combinations(worlds, 2)):
                cost = sum((p.cost for p in selected), Fraction(0))
                if best is None or cost < best[0]:
                    best = (cost, tuple(p.name for p in selected))
    return best


def run():
    worlds = frozenset("abcd")
    targets = {w: w for w in worlds}
    probes = (
        deterministic("region", {"a": 0, "b": 0, "c": 1, "d": 1}),
        deterministic("left-specific", {"a": 0, "b": 1, "c": 0, "d": 0}),
        deterministic("right-specific", {"a": 0, "b": 0, "c": 0, "d": 1}),
    )
    adaptive_cost, tree, memo = optimal_strategy(worlds, targets, probes)
    fixed = smallest_fixed_query_bundle(worlds, targets, probes)
    assert adaptive_cost == 2 and fixed == (Fraction(3), tuple(p.name for p in probes))

    # A Root's receiver Passport is a separate obligation from its task.
    laws = frozenset(("copy", "invert"))
    task_only = {w: "same-answer" for w in laws}
    with_passport = {"copy": ("same-answer", "accepted"),
                     "invert": ("same-answer", "rejected")}
    law_probe = deterministic("source-law-witness", {"copy": 0, "invert": 1})
    assert optimal_strategy(laws, task_only, (law_probe,))[0] == 0
    assert optimal_strategy(laws, with_passport, (law_probe,))[0] == 1

    # The cheap query is not guaranteed enabled in both candidate worlds.
    risky = deterministic("restricted-check", {0: 0}, cost=1)
    safe = deterministic("universal-check", {0: 0, 1: 1}, cost=4)
    assert optimal_strategy(frozenset((0, 1)), {0: 0, 1: 1}, (risky, safe))[0] == 4

    # Adversarial sensor overlap means a possible ambiguous response can be
    # repeated forever; repeated sensing cannot guarantee diagnosis.
    noisy = Probe("noisy", Fraction(1),
                  {0: frozenset((0, 1)), 1: frozenset((1, 2))},
                  frozenset((0, 1)))
    no_solution = optimal_strategy(frozenset((0, 1)), {0: 0, 1: 1}, (noisy,))
    assert no_solution[0] is None
    noisy_fallback = deterministic("certain", {0: 0, 1: 1}, cost=3)
    assert optimal_strategy(frozenset((0, 1)), {0: 0, 1: 1},
                            (noisy, noisy_fallback))[0] == 3

    # Joint witness matters. A single hidden calibration bit is persistent
    # across two probes. Per-query marginals are uninformative, but their
    # joint output parity reveals the task exactly.
    joint_worlds = frozenset(product((0, 1), repeat=2))  # (task, calibration)
    joint_target = {(t, h): t for t, h in joint_worlds}
    q1 = deterministic("calibration-read", {(t, h): h for t, h in joint_worlds})
    q2 = deterministic("coded-read", {(t, h): t ^ h for t, h in joint_worlds})
    joint_exact = optimal_strategy(joint_worlds, joint_target, (q1, q2))[0]
    assert joint_exact == 2
    marginal_q = Probe("marginal-only", Fraction(1),
                       {0: frozenset((0, 1)), 1: frozenset((0, 1))},
                       frozenset((0, 1)))
    joint_thrown_away = optimal_strategy(frozenset((0, 1)),
                                         {0: 0, 1: 1}, (marginal_q,))[0]
    assert joint_thrown_away is None

    rng = random.Random(20261101)
    cross_checks = 0
    infeasible = 0
    for _ in range(200):
        n = rng.randint(2, 5)
        wset = frozenset(range(n))
        goal = {w: rng.randrange(3) for w in wset}
        catalogue = []
        for q in range(rng.randint(1, 4)):
            enabled = frozenset(w for w in wset if rng.random() < .85)
            if not enabled:
                enabled = frozenset((rng.randrange(n),))
            outcome_map = {}
            for w in enabled:
                outcomes = frozenset(o for o in range(3) if rng.random() < .5)
                outcome_map[w] = outcomes or frozenset((rng.randrange(3),))
            catalogue.append(Probe(f"q{q}", Fraction(rng.randrange(1, 5)),
                                   outcome_map, enabled))
        catalogue = tuple(catalogue)
        got, _, _ = optimal_strategy(wset, goal, catalogue)
        expected = independent_explicit_cost(wset, goal, catalogue)
        assert got == expected
        cross_checks += 1
        infeasible += got is None

    return {
        "scope": "finite static source worlds, passive set-valued probes, no probabilities",
        "adaptive_vs_nonadaptive": {
            "minimum_worst_case_adaptive_cost": str(adaptive_cost),
            "minimum_fixed_bundle_cost": str(fixed[0]),
            "adaptive_policy": tree,
            "computed_information_states": len(memo),
        },
        "passport_requires_extra_probe": True,
        "partial_availability_test": {"safe_worst_case_cost": "4"},
        "noisy_indefinite_ambiguity_without_fallback": True,
        "noisy_with_certain_fallback_cost": "3",
        "persistent_hidden_witness": {
            "with_joint_source_state_worst_case_cost": "2",
            "with_only_unrelated_marginal_outcome_sets_certifiable": False,
        },
        "random_explicit_policy_cross_checks": cross_checks,
        "random_infeasible_instances": infeasible,
        "limitations": [
            "Probe outcome sets are adversarial, not probabilistic",
            "Worlds remain static; active interventions change the contract",
            "No joint correlation assumptions among separately specified probes",
            "Only declared candidate worlds and receiver requirements are certified",
            "Tests do not establish historical originality or field performance",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
