"""Finite regression checks for BM dynamic Seed horizon/closure distinctions.

All native worlds are binary registers. This is a finite analogue, not
a proof about infinitely many time steps or compact infinite products.
Python 3.10+; standard library only.
"""

from __future__ import annotations

import json
from itertools import combinations, product


def states(register_length: int):
    return tuple(product((0, 1), repeat=register_length))


def advance(world):
    return world[1:] + (0,)


def export(world, indices):
    return tuple(world[i] for i in indices)


def task_horizon(world, steps: int):
    answers = []
    state = world
    for _ in range(steps + 1):
        answers.append(state[0])
        state = advance(state)
    return tuple(answers)


def determines(worlds, indices, requested):
    seen = {}
    for world in worlds:
        encoded = export(world, indices)
        required = requested(world)
        if encoded in seen and seen[encoded] != required:
            return False
        seen[encoded] = required
    return True


def closed(worlds, indices):
    transitions = {}
    for world in worlds:
        current = export(world, indices)
        future = export(advance(world), indices)
        if current in transitions and transitions[current] != future:
            return False
        transitions[current] = future
    return True


def exhaustive_battery(worlds, horizon):
    n = len(worlds[0])
    requested = lambda world: task_horizon(world, horizon)
    valid = []
    for size in range(n + 1):
        for indices in combinations(range(n), size):
            if determines(worlds, indices, requested):
                valid.append(indices)
        if valid:
            return size, tuple(valid)
    raise AssertionError("complete source observation must determine tasks")


def run():
    result = []
    verified_closure_obstructions = 0
    verified_horizons = 0
    for n in (3, 4, 5, 6):
        worlds = states(n)
        cases = []
        for horizon in range(n):
            cost, batteries = exhaustive_battery(worlds, horizon)
            assert cost == horizon + 1
            assert tuple(range(horizon + 1)) in batteries
            cases.append({"steps_ahead": horizon, "minimum_fixed_readings": cost})
            verified_horizons += 1

        for size in range(1, n + 1):
            for indices in combinations(range(n), size):
                if max(indices) < n - 1:
                    assert not closed(worlds, indices)
                    verified_closure_obstructions += 1

        assert closed(worlds, tuple(range(n)))
        suffix = tuple(range(n - 1, n))
        assert closed(worlds, suffix)
        assert not determines(worlds, suffix, lambda world: world[0])
        assert not closed(worlds, (0,))
        result.append({
            "register_length": n,
            "native_worlds": len(worlds),
            "fixed_battery_horizons": cases,
            "full_register_is_closed": True,
            "last_bit_only_is_closed_but_cannot_recover_present_task": True,
        })
    return {
        "scope": "finite deterministic shift registers with zero append",
        "tested_native_register_lengths": (3, 4, 5, 6),
        "horizon_optimality_cases": verified_horizons,
        "tested_nonclosure_coordinate_projections": verified_closure_obstructions,
        "cases": result,
        "warning": "No finite test establishes the theorem for the infinite shift space",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
