"""Exact small-case verifier for finite task-closed Seed quotient (F1/F2).

Tests finite deterministic total maps using exhaustive equivalence and
finite-partition enumeration. Random instance generation makes no
probabilistic assumption about the mathematical source.
Python 3.10+, standard library only.
"""

from __future__ import annotations

import json
import random
from itertools import combinations


def normalize(labels):
    look = {}
    result = []
    for label in labels:
        if label not in look:
            look[label] = len(look)
        result.append(look[label])
    return tuple(result)


def stabilized_quotient(transition, task):
    n = len(transition)
    assert n >= 1 and len(task) == n
    assert all(0 <= p < n for p in transition)
    ids = normalize(task)
    history = [ids]
    h = 0
    while True:
        new_ids = normalize(tuple((task[i], ids[transition[i]]) for i in range(n)))
        if new_ids == ids:
            return h, ids, history
        ids = new_ids
        history.append(ids)
        h += 1
        assert h <= n - len(set(task))


def can_evolve(partition, transition):
    induced = {}
    for i, block in enumerate(partition):
        outgoing = partition[transition[i]]
        if block in induced and induced[block] != outgoing:
            return False
        induced[block] = outgoing
    return True


def determines_task(partition, task):
    decoded = {}
    for i, block in enumerate(partition):
        if block in decoded and decoded[block] != task[i]:
            return False
        decoded[block] = task[i]
    return True


def finite_horizon(transition, task, state, horizon):
    values = []
    for _ in range(horizon + 1):
        values.append(task[state])
        state = transition[state]
    return tuple(values)


def restricted_growth_partitions(n):
    """Enumerate every set partition via its unique restricted-growth code."""
    if n == 1:
        yield (0,)
        return

    def generate(prefix, maximum):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for block in range(maximum + 2):
            yield from generate(prefix + [block], max(maximum, block))

    yield from generate([0], 0)


def check_instance(transition, task, enumerate_representation=False):
    n = len(task)
    h, quotient, history = stabilized_quotient(transition, task)
    assert h <= n - len(set(task))
    assert determines_task(quotient, task)
    assert can_evolve(quotient, transition)
    for left, right in combinations(range(n), 2):
        same_quotient = quotient[left] == quotient[right]
        same_future = finite_horizon(transition, task, left, n * n + 1) == \
                      finite_horizon(transition, task, right, n * n + 1)
        assert same_quotient == same_future
    if enumerate_representation:
        admissible_count = 0
        smallest = n + 1
        for candidate in restricted_growth_partitions(n):
            if determines_task(candidate, task) and can_evolve(candidate, transition):
                admissible_count += 1
                smallest = min(smallest, len(set(candidate)))
                for left, right in combinations(range(n), 2):
                    assert candidate[left] != candidate[right] or \
                           quotient[left] == quotient[right]
        assert smallest == len(set(quotient))
        assert admissible_count > 0
    return h, quotient, len(history)


def run():
    rng = random.Random(20261102)
    randomized = 0
    exhaustive = 0
    sharp = []
    for n in range(2, 11):
        f = tuple(min(i + 1, n - 1) for i in range(n))
        t = tuple(int(i == n - 1) for i in range(n))
        h, q, _ = check_instance(f, t, enumerate_representation=(n <= 6))
        assert h == n - 2
        assert len(set(q)) == n
        sharp.append({"worlds": n, "distinct_current_outputs": 2,
                      "first_stable_horizon": h})

    for n in range(2, 10):
        for trial in range(75):
            f = tuple(rng.randrange(n) for _ in range(n))
            t = tuple(rng.randrange(min(n, 4)) for _ in range(n))
            enumerate_representation = n <= 6 and trial < 35
            check_instance(f, t, enumerate_representation)
            randomized += 1
            exhaustive += enumerate_representation

    # Two source bits: current first-bit observation not enough to evolve.
    swap = (0, 2, 1, 3)
    present = (0, 0, 1, 1)
    h, q, _ = check_instance(swap, present, enumerate_representation=True)
    assert h == 1 and len(set(q)) == 4
    assert determines_task(present, present)
    assert not can_evolve(present, swap)

    return {
        "scope": "finite deterministic source maps, exact task and state partitions",
        "randomized_source_instances": randomized,
        "small_size_full_partition_enumeration_instances": exhaustive + 1,
        "sharp_bound_witnesses": sharp,
        "two_bit_present_task_is_not_autonomous": True,
        "all_checked_partitions_refine_canonical_task_closed_quotient": True,
        "no_originality_or_empirical_claim": True,
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
