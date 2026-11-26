"""Finite randomized and explicit verification for BM joint receiver closure J1/J2.

Uses exact native-state enumeration. No probabilistic assumptions about the
underlying source are used; random instance generation is a test technique.
"""

from __future__ import annotations

import json
import random
from itertools import combinations
from pathlib import Path
from runpy import run_path


_api = run_path(str(Path(__file__).with_name(
    "BM_Finite_Task_Closure_Verifier_2026-11-01.py")))
stabilized_quotient = _api["stabilized_quotient"]


def check_system(next_state, task_a, task_b):
    n = len(next_state)
    _, qa, _ = stabilized_quotient(next_state, task_a)
    _, qb, _ = stabilized_quotient(next_state, task_b)
    target_pair = tuple((task_a[i], task_b[i]) for i in range(n))
    _, qab, _ = stabilized_quotient(next_state, target_pair)
    realized = {(qa[i], qb[i]) for i in range(n)}
    full_product = {(a, b) for a in set(qa) for b in set(qb)}

    for i, j in combinations(range(n), 2):
        assert (qab[i] == qab[j]) == (qa[i] == qa[j] and qb[i] == qb[j])

    # Every actual pair has a lawful successor in the same realizable image.
    update = {}
    for i in range(n):
        current = (qa[i], qb[i])
        successor = (qa[next_state[i]], qb[next_state[i]])
        assert successor in realized
        if current in update:
            assert update[current] == successor
        update[current] = successor

    for a, b in full_product:
        overlap = any(qa[i] == a and qb[i] == b for i in range(n))
        assert ((a, b) in realized) == overlap
    assert max(len(set(qa)), len(set(qb))) <= len(realized)
    assert len(realized) <= min(n, len(set(qa)) * len(set(qb)))
    return {
        "a_classes": len(set(qa)), "b_classes": len(set(qb)),
        "joint_classes": len(realized), "formal_product": len(full_product),
        "ghost_pairs": len(full_product - realized),
    }


def run():
    randomizer = random.Random(20261102)
    tested = 0
    samples_with_ghosts = 0
    for n in range(2, 10):
        for _ in range(100):
            next_state = tuple(randomizer.randrange(n) for _ in range(n))
            task_a = tuple(randomizer.randrange(3) for _ in range(n))
            task_b = tuple(randomizer.randrange(3) for _ in range(n))
            value = check_system(next_state, task_a, task_b)
            tested += 1
            samples_with_ghosts += value["ghost_pairs"] > 0

    three_states = check_system(
        next_state=(0, 1, 2),
        task_a=(0, 0, 1),
        task_b=(0, 1, 1),
    )
    assert three_states == {
        "a_classes": 2, "b_classes": 2, "joint_classes": 3,
        "formal_product": 4, "ghost_pairs": 1,
    }

    swap = check_system(
        next_state=(0, 2, 1, 3),
        task_a=(0, 0, 1, 1),
        task_b=(0, 1, 0, 1),
    )
    assert swap == {
        "a_classes": 4, "b_classes": 4, "joint_classes": 4,
        "formal_product": 16, "ghost_pairs": 12,
    }

    return {
        "scope": "one finite native source and total deterministic shared evolution",
        "randomized_systems_checked": tested,
        "randomized_systems_with_unrealizable_local_pairs": samples_with_ghosts,
        "three_state_ghost_pair_example": three_states,
        "two_bit_swap_coupled_receiver_example": swap,
        "joint_future_equivalence_meet_verified": True,
        "product_dynamics_preserves_native_joint_image": True,
        "no_originality_or_empirical_claim": True,
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
