"""Finite worst-case BM diagnostic control with task-preserving interventions.

A world can change under a declared action; actions emit observations. The
receiving task is inherited along each allowed transition. No probabilities.
"""

from __future__ import annotations

import json
import random
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
from typing import Hashable


Obj = Hashable


@dataclass(frozen=True)
class Action:
    name: str
    cost: Fraction
    edges: dict[Obj, frozenset[tuple[Obj, Obj]]]

    def validate(self, worlds, target) -> None:
        assert self.cost > 0
        for state, options in self.edges.items():
            assert state in worlds and options
            for observation, successor in options:
                assert successor in worlds
                if target[successor] != target[state]:
                    raise ValueError(
                        f"action {self.name} changes declared target: {state} -> {successor}"
                    )


def successors(candidates, action: Action):
    if any(w not in action.edges for w in candidates):
        return ()
    observations = set()
    for w in candidates:
        observations.update(o for o, _ in action.edges[w])
    return tuple(
        (obs, frozenset(w2 for w in candidates for o, w2 in action.edges[w] if o == obs))
        for obs in sorted(observations, key=repr)
    )


def all_nonempty_subsets(worlds):
    ordered = sorted(worlds, key=repr)
    return tuple(frozenset(x for i, x in enumerate(ordered) if mask & (1 << i))
                 for mask in range(1, 1 << len(ordered)))


def exact_belief_game(worlds, initial, target, actions):
    worlds = frozenset(worlds)
    initial = frozenset(initial)
    assert initial and initial <= worlds and set(target) == set(worlds)
    for a in actions:
        a.validate(worlds, target)

    beliefs = all_nonempty_subsets(worlds)
    terminal = {b for b in beliefs if len({target[w] for w in b}) == 1}
    values = {b: (Fraction(0) if b in terminal else None) for b in beliefs}
    chosen = {}
    stages = 0
    # With positive costs, a guaranteed terminating memoryless belief policy
    # cannot require revisiting the same belief along one execution.
    for horizon in range(1, len(beliefs) + 1):
        updated = dict(values)
        for b in beliefs:
            if b in terminal:
                continue
            for a in actions:
                next_beliefs = successors(b, a)
                if not next_beliefs:
                    continue
                costs = [values[next_b] for _, next_b in next_beliefs]
                if any(v is None for v in costs):
                    continue
                cost = a.cost + max(costs)
                if updated[b] is None or cost < updated[b]:
                    updated[b] = cost
                    chosen[b] = (a.name, tuple((repr(o), tuple(sorted(map(repr, b2))))
                                               for o, b2 in next_beliefs))
        stages = horizon
        if updated == values:
            break
        values = updated
    return values[initial], chosen, {
        "beliefs": len(beliefs), "iterations": stages,
        "terminal_beliefs": len(terminal),
        "solvable_beliefs": sum(v is not None for v in values.values()),
    }


def brute_bounded_cost(candidates, target, actions, depth):
    if len({target[w] for w in candidates}) == 1:
        return Fraction(0)
    if depth == 0:
        return None
    scores = []
    for action in actions:
        next_c = successors(candidates, action)
        if not next_c:
            continue
        downstream = [brute_bounded_cost(b, target, actions, depth - 1)
                      for _, b in next_c]
        if all(cost is not None for cost in downstream):
            scores.append(action.cost + max(downstream))
    return min(scores) if scores else None


def run():
    worlds = frozenset((0, 1, 2, 3))
    target = {0: 0, 1: 1, 2: 0, 3: 1}
    activate = Action("activate", Fraction(1), {
        0: frozenset((("ready", 2),)),
        1: frozenset((("ready", 3),)),
    })
    read = Action("read", Fraction(1), {
        2: frozenset(((0, 2),)),
        3: frozenset(((1, 3),)),
    })
    result, policy, details = exact_belief_game(worlds, (0, 1), target,
                                                (activate, read))
    assert result == 2

    # The same two initial worlds cannot be separated by a passive
    # self-looping action that always reports a common response.
    no_information = Action("stuck", Fraction(1), {
        0: frozenset((("?", 0),)),
        1: frozenset((("?", 1),)),
    })
    never, _, _ = exact_belief_game(worlds, (0, 1), target, (no_information,))
    assert never is None

    destructive = Action("erases-original-answer", Fraction(1), {
        0: frozenset((("ok", 1),)),
        1: frozenset((("ok", 1),)),
    })
    try:
        exact_belief_game(worlds, (0, 1), target, (destructive,))
    except ValueError:
        unsafe_rejected = True
    else:
        raise AssertionError("must reject native actions changing original target")

    # Independent depth-limited tree enumeration agrees with backward belief
    # value iteration. This is exact on the tiny declared random test inputs.
    rng = random.Random(20261101)
    random_checks = 0
    random_feasible = 0
    for _ in range(150):
        n = rng.randint(2, 4)
        ws = frozenset(range(n))
        y = {w: rng.randrange(2) for w in ws}
        acts = []
        for j in range(rng.randint(1, 3)):
            edges = {}
            for w in ws:
                if rng.random() < 0.8:
                    same_task = [v for v in ws if y[v] == y[w]]
                    ops = frozenset((rng.randrange(3), rng.choice(same_task))
                                    for _ in range(rng.randint(1, 2)))
                    edges[w] = ops
            if edges:
                acts.append(Action(f"a{j}", Fraction(rng.randint(1, 3)), edges))
        acts = tuple(acts)
        start = frozenset(ws)
        cost, _, _ = exact_belief_game(ws, start, y, acts)
        expected = brute_bounded_cost(start, y, acts, (1 << n) - 1)
        assert cost == expected
        random_checks += 1
        random_feasible += cost is not None

    return {
        "scope": "finite controlled task-preserving transitions with adversarial outcomes",
        "activation_then_read_worst_case_cost": str(result),
        "activation_game": details,
        "activation_policy_records": len(policy),
        "noninformative_repeated_probe_guarantees_termination": False,
        "original_task_mutating_action_rejected": unsafe_rejected,
        "random_backward_vs_explicit_tree_checks": random_checks,
        "random_feasible_cases": random_feasible,
        "limitations": [
            "Task is inherited along actions to preserve original question",
            "Only finite worlds, finite actions, positive costs and worst-case outcomes",
            "Allows interventions changing native world and legal query menu",
            "No external world or physical accuracy inference",
            "State and action relations must be supplied; no automatic law discovery",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
