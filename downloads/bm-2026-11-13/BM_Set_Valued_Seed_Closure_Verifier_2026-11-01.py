"""Exact finite verifier for BM set-valued Seed closure and branching.

Strong bisimulation by partition refinement; test trace-vs-branch difference,
and two individually valid receivers whose quotient meet is not jointly closed.
Python 3.10+ standard library, no source probabilities.
"""

from __future__ import annotations

import json
import random
from itertools import combinations
from pathlib import Path
from runpy import run_path


_p = run_path(str(Path(__file__).with_name(
    "BM_Finite_Task_Closure_Verifier_2026-11-01.py")))
normalize = _p["normalize"]
restricted_growth_partitions = _p["restricted_growth_partitions"]


def partition_task_closed(succ, task):
    n = len(task)
    assert n >= 1 and len(succ) == n
    assert all(part and all(0 <= x < n for x in part) for part in succ)
    labels = normalize(task)
    iterations = 0
    while True:
        refined = normalize(tuple((labels[i],
                                  frozenset(labels[j] for j in succ[i]))
                                 for i in range(n)))
        if refined == labels:
            return labels, iterations
        labels = refined
        iterations += 1
        assert iterations <= n - len(set(task))


def is_valid_quotient(succ, task, quotient):
    outputs = {}
    choices = {}
    for i, label in enumerate(quotient):
        successors = frozenset(quotient[j] for j in succ[i])
        if label in outputs and (outputs[label] != task[i] or
                                 choices[label] != successors):
            return False
        outputs[label] = task[i]
        choices[label] = successors
    return True


def task_trace_sets(succ, task, horizon):
    states = tuple(frozenset(((t,),)) for t in task)
    for _ in range(horizon):
        states = tuple(
            frozenset((task[i],) + suffix
                      for child in succ[i]
                      for suffix in states[child])
            for i in range(len(task))
        )
    return states


def examine(succ, task, exhaustive=False):
    q, steps = partition_task_closed(succ, task)
    assert is_valid_quotient(succ, task, q)
    assert steps <= len(task) - len(set(task))
    checked = 0
    if exhaustive:
        best = len(task) + 1
        for candidate in restricted_growth_partitions(len(task)):
            if is_valid_quotient(succ, task, candidate):
                checked += 1
                best = min(best, len(set(candidate)))
                for i, j in combinations(range(len(task)), 2):
                    assert candidate[i] != candidate[j] or q[i] == q[j]
        assert best == len(set(q))
    return q, steps, checked


def run():
    rng = random.Random(20261102)
    randomized = 0
    exhaustive = 0
    partitions_checked = 0
    for n in range(2, 9):
        for trial in range(75):
            succ = []
            for _ in range(n):
                part = frozenset(j for j in range(n) if rng.random() < .34)
                succ.append(part or frozenset((rng.randrange(n),)))
            task = tuple(rng.randrange(3) for _ in range(n))
            do_exhaustive = n <= 6 and trial < 35
            _, _, nchecked = examine(tuple(succ), task, do_exhaustive)
            randomized += 1
            exhaustive += do_exhaustive
            partitions_checked += nchecked

    # Trace-equivalent roots with distinct branching choices:
    # x,y,u,v,w,b,c indexed 0..6
    trace_succ = ((2,), (3, 4), (5, 6), (5,), (6,), (5,), (6,))
    trace_task = ("A", "A", "B", "B", "B", "0", "1")
    q_trace, _, _ = examine(trace_succ, trace_task, True)
    assert q_trace[0] != q_trace[1]
    for horizon in range(12):
        all_traces = task_trace_sets(trace_succ, trace_task, horizon)
        assert all_traces[0] == all_traces[1]

    # x,y,00,01,10,11 indexed 0..5; terminal states self-loop.
    coupled_succ = ((2, 5), (3, 4), (2,), (3,), (4,), (5,))
    task_a = (0, 0, 0, 0, 1, 1)
    task_b = (0, 0, 0, 1, 0, 1)
    qa, _, _ = examine(coupled_succ, task_a, True)
    qb, _, _ = examine(coupled_succ, task_b, True)
    qjoint, _, _ = examine(coupled_succ,
                            tuple(zip(task_a, task_b)), True)
    assert qa[0] == qa[1]
    assert qb[0] == qb[1]
    assert qjoint[0] != qjoint[1]
    meet = tuple((qa[i], qb[i]) for i in range(6))
    assert not is_valid_quotient(coupled_succ,
                                 tuple(zip(task_a, task_b)), meet)

    return {
        "scope": "finite, nonempty set-valued native successor relations",
        "randomized_finite_systems": randomized,
        "exhaustive_partition_search_cases": exhaustive + 4,
        "successful_candidate_partitions_exhaustively_checked": partitions_checked,
        "same_complete_trace_sets_but_distinct_branch_structure": True,
        "separate_receiver_bisimulation_meet_is_not_jointly_closed": True,
        "declared_no_probabilities": True,
        "no_historical_novelty_claim": True,
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
