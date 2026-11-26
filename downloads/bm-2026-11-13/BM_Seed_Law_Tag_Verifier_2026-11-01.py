"""Exact finite Branch Mathematics Seed/model-identity certificate experiments.

Additive research demonstration. Does not alter canonical BM V1 or claim novelty.
Python 3.10+ standard library only. All finite task values are deterministic.
"""

from __future__ import annotations

import json
import random
import sys
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
from typing import Hashable


Value = Hashable


@dataclass(frozen=True)
class Law:
    name: str
    states: tuple[Value, ...]
    seed: dict[Value, Value]
    task: dict[Value, Value]
    step: dict[Value, Value]

    def validate(self) -> None:
        assert self.states and len(set(self.states)) == len(self.states)
        domain = set(self.states)
        assert set(self.seed) == set(self.task) == set(self.step) == domain
        assert set(self.step.values()) <= domain


def future_trace(law: Law, state: Value, horizon: int) -> tuple[Value, ...]:
    assert horizon >= 0
    out = []
    s = state
    for _ in range(horizon + 1):
        out.append(law.task[s])
        s = law.step[s]
    return tuple(out)


def intrinsic_collisions(law: Law, horizon: int) -> list[tuple[Value, Value]]:
    return [
        (x, y)
        for x, y in combinations(law.states, 2)
        if law.seed[x] == law.seed[y]
        and future_trace(law, x, horizon) != future_trace(law, y, horizon)
    ]


def conflict_graph(
    laws: tuple[Law, ...], horizon: int
) -> tuple[set[tuple[int, int]], dict[tuple[int, int], tuple[Value, Value]]]:
    for law in laws:
        law.validate()
        collision = intrinsic_collisions(law, horizon)
        if collision:
            raise ValueError(f"intrinsic insufficiency in {law.name}: {collision[0]}")
    edges = set()
    witnesses = {}
    for i, j in combinations(range(len(laws)), 2):
        first, second = laws[i], laws[j]
        for x in first.states:
            for y in second.states:
                if (
                    first.seed[x] == second.seed[y]
                    and future_trace(first, x, horizon)
                    != future_trace(second, y, horizon)
                ):
                    edges.add((i, j))
                    witnesses[(i, j)] = (x, y)
                    break
            if (i, j) in edges:
                break
    return edges, witnesses


def closure_graph(
    laws: tuple[Law, ...]
) -> tuple[set[tuple[int, int]], dict[tuple[int, int], tuple[Value, Value]]]:
    """Cost for a single decoder AND an autonomous one-step Seed-code update.

    Each law is unchanged by the update, the same tag persists, and all steps
    are total. A closed update on (seed value, tag) must be single-valued.
    """
    for law in laws:
        law.validate()
        for x, y in combinations(law.states, 2):
            if law.seed[x] == law.seed[y] and (
                law.task[x] != law.task[y]
                or law.seed[law.step[x]] != law.seed[law.step[y]]
            ):
                raise ValueError(f"intrinsic closure insufficiency: {law.name} ({x}, {y})")
    edges = set()
    witnesses = {}
    for i, j in combinations(range(len(laws)), 2):
        a, b = laws[i], laws[j]
        for x in a.states:
            for y in b.states:
                if a.seed[x] == b.seed[y] and (
                    a.task[x] != b.task[y]
                    or a.seed[a.step[x]] != b.seed[b.step[y]]
                ):
                    edges.add((i, j))
                    witnesses[(i, j)] = (x, y)
                    break
            if (i, j) in edges:
                break
    return edges, witnesses


def has_autonomous_code(laws: tuple[Law, ...], tag: tuple[int, ...]) -> bool:
    decoder = {}
    transition = {}
    for i, law in enumerate(laws):
        for x in law.states:
            code = (law.seed[x], tag[i])
            target = law.task[x]
            successor_code = (law.seed[law.step[x]], tag[i])
            if code in decoder and decoder[code] != target:
                return False
            if code in transition and transition[code] != successor_code:
                return False
            decoder[code] = target
            transition[code] = successor_code
    return True


def direct_min_closed_colors(laws: tuple[Law, ...]) -> int:
    for k in range(1, len(laws) + 1):
        for colors in product(range(k), repeat=len(laws)):
            if has_autonomous_code(laws, colors):
                return k
    raise AssertionError("tag every law, when individually closed")


def switching_code_valid(
    worlds: tuple[Value, ...],
    law_at: dict[Value, int],
    seed_at: dict[Value, Value],
    task_at: dict[Value, Value],
    step_at: dict[Value, Value],
    tags: tuple[int, ...],
) -> bool:
    """Check a deterministic Root/Seed code when the source law can change."""
    decoder = {}
    update = {}
    for w in worlds:
        code = (seed_at[w], tags[law_at[w]])
        next_w = step_at[w]
        next_code = (seed_at[next_w], tags[law_at[next_w]])
        if code in decoder and decoder[code] != task_at[w]:
            return False
        if code in update and update[code] != next_code:
            return False
        decoder[code] = task_at[w]
        update[code] = next_code
    return True


def switching_constraint_valid(
    worlds: tuple[Value, ...],
    law_at: dict[Value, int],
    seed_at: dict[Value, Value],
    task_at: dict[Value, Value],
    step_at: dict[Value, Value],
    tags: tuple[int, ...],
) -> bool:
    """Independent pairwise implication certificate for switching closure."""
    for x, y in combinations(worlds, 2):
        if seed_at[x] != seed_at[y]:
            continue
        if tags[law_at[x]] != tags[law_at[y]]:
            continue
        if task_at[x] != task_at[y]:
            return False
        if seed_at[step_at[x]] != seed_at[step_at[y]]:
            return False
        if tags[law_at[step_at[x]]] != tags[law_at[step_at[y]]]:
            return False
    return True


def switching_min_tags(
    worlds: tuple[Value, ...],
    law_at: dict[Value, int],
    seed_at: dict[Value, Value],
    task_at: dict[Value, Value],
    step_at: dict[Value, Value],
) -> tuple[int | None, tuple[int, ...] | None]:
    n = max(law_at.values()) + 1
    for k in range(1, n + 1):
        for tags in product(range(k), repeat=n):
            if switching_code_valid(worlds, law_at, seed_at, task_at, step_at, tags):
                return k, tags
    return None, None


def chromatic_number(n: int, edges: set[tuple[int, int]]) -> tuple[int, tuple[int, ...]]:
    assert n >= 1
    neighbors = [set() for _ in range(n)]
    for i, j in edges:
        assert 0 <= i < j < n
        neighbors[i].add(j)
        neighbors[j].add(i)
    order = sorted(range(n), key=lambda i: (-len(neighbors[i]), i))
    for palette in range(1, n + 1):
        colors = [-1] * n

        def search(i: int) -> bool:
            if i == n:
                return True
            vertex = order[i]
            used = {colors[other] for other in neighbors[vertex]}
            for color in range(palette):
                if color not in used:
                    colors[vertex] = color
                    if search(i + 1):
                        return True
                    colors[vertex] = -1
            return False

        if search(0):
            return palette, tuple(colors)
    raise AssertionError("n colors always suffice")


def has_uniform_decoder(laws: tuple[Law, ...], tag: tuple[int, ...], horizon: int) -> bool:
    seen = {}
    for i, law in enumerate(laws):
        for state in law.states:
            code = (law.seed[state], tag[i])
            trace = future_trace(law, state, horizon)
            if code in seen and seen[code] != trace:
                return False
            seen[code] = trace
    return True


def independent_oracle_min_colors(laws: tuple[Law, ...], horizon: int) -> int:
    for k in range(1, len(laws) + 1):
        for tags in product(range(k), repeat=len(laws)):
            if has_uniform_decoder(laws, tags, horizon):
                return k
    raise AssertionError("tag each law separately")


def make_law(name, states, seeds, tasks, steps=None) -> Law:
    if steps is None:
        steps = {x: x for x in states}
    return Law(name, tuple(states), dict(seeds), dict(tasks), dict(steps))


def graph_realization(n: int, edges: set[tuple[int, int]]) -> tuple[Law, ...]:
    """Construct a law family with exactly the supplied conflict graph."""
    states = [[] for _ in range(n)]
    seeds = [dict() for _ in range(n)]
    tasks = [dict() for _ in range(n)]
    for i, j in sorted(edges):
        symbol = ("edge", i, j)
        for vertex, value in ((i, 0), (j, 1)):
            state = ("state", symbol, vertex)
            states[vertex].append(state)
            seeds[vertex][state] = symbol
            tasks[vertex][state] = value
    for i in range(n):
        if not states[i]:
            state = ("isolated", i)
            states[i].append(state)
            seeds[i][state] = ("private", i)
            tasks[i][state] = 0
    return tuple(
        make_law(str(i), states[i], seeds[i], tasks[i]) for i in range(n)
    )


def run() -> dict:
    copy = make_law("copy", [(0, 0), (1, 1)], {(0, 0): 0, (1, 1): 1},
                    {(0, 0): 0, (1, 1): 1})
    invert = make_law("invert", [(0, 1), (1, 0)], {(0, 1): 0, (1, 0): 1},
                      {(0, 1): 1, (1, 0): 0})
    restricted = make_law("restricted", [(0, 0)], {(0, 0): 0}, {(0, 0): 0})
    static_laws = (copy, invert, restricted)
    static_edges, static_witnesses = conflict_graph(static_laws, 0)
    static_chi, static_tag = chromatic_number(len(static_laws), static_edges)
    assert static_edges == {(0, 1), (1, 2)}
    assert static_chi == 2 and has_uniform_decoder(static_laws, static_tag, 0)
    assert independent_oracle_min_colors(static_laws, 0) == 2

    hold = make_law("hold", [0, 1], {0: 0, 1: 1}, {0: 0, 1: 1}, {0: 0, 1: 1})
    flip = make_law("flip", [0, 1], {0: 0, 1: 1}, {0: 0, 1: 1}, {0: 1, 1: 0})
    future_laws = (hold, flip)
    future_cost = []
    for h in range(6):
        edges, witnesses = conflict_graph(future_laws, h)
        chi, tags = chromatic_number(2, edges)
        assert chi == independent_oracle_min_colors(future_laws, h)
        future_cost.append({"horizon": h, "tags": chi, "edges": sorted(edges)})
    assert [x["tags"] for x in future_cost] == [1, 2, 2, 2, 2, 2]

    reset_zero = make_law("reset_zero", [0, 1], {0: 0, 1: 1},
                          {0: 0, 1: 0}, {0: 0, 1: 0})
    reset_one = make_law("reset_one", [0, 1], {0: 0, 1: 1},
                         {0: 0, 1: 0}, {0: 1, 1: 1})
    reset_laws = (reset_zero, reset_one)
    assert all(not conflict_graph(reset_laws, h)[0] for h in range(8))
    reset_closed_edges, _ = closure_graph(reset_laws)
    assert reset_closed_edges == {(0, 1)}
    assert chromatic_number(2, reset_closed_edges)[0] == 2
    assert direct_min_closed_colors(reset_laws) == 2

    # Different task receivers can each need 2 model tags while jointly
    # needing 3. Each pair has a private Seed symbol and two task coordinates.
    receiver_edges = {"first": {(0, 1), (1, 2)}, "second": {(0, 2)}}
    receiver_laws = []
    for v in range(3):
        states = []
        seeds = {}
        tasks = {}
        for i, j in sorted(receiver_edges["first"] | receiver_edges["second"]):
            if v not in (i, j):
                continue
            s = ("edge", i, j, v)
            states.append(s)
            seeds[s] = (i, j)
            val = 0 if v == i else 1
            tasks[s] = (val, 0) if (i, j) in receiver_edges["first"] else (0, val)
        receiver_laws.append(make_law(str(v), states, seeds, tasks))
    receiver_laws = tuple(receiver_laws)

    def project_receiver(index: int) -> tuple[Law, ...]:
        return tuple(make_law(l.name, l.states, l.seed,
                              {s: l.task[s][index] for s in l.states}, l.step)
                     for l in receiver_laws)

    first_edges, _ = conflict_graph(project_receiver(0), 0)
    second_edges, _ = conflict_graph(project_receiver(1), 0)
    joined_edges, _ = conflict_graph(receiver_laws, 0)
    assert first_edges == receiver_edges["first"]
    assert second_edges == receiver_edges["second"]
    assert joined_edges == first_edges | second_edges
    assert chromatic_number(3, first_edges)[0] == 2
    assert chromatic_number(3, second_edges)[0] == 2
    assert chromatic_number(3, joined_edges)[0] == 3

    # A single source law L0 conceals two distinct outcomes. Passport/task
    # requires distinguishing their successor laws, making any law-only tag
    # impossible. One extra initial Seed bit repairs it.
    worlds = ("p", "q", "r", "s")
    law_at = {"p": 0, "q": 0, "r": 1, "s": 2}
    seed_at = {w: 0 for w in worlds}
    task_at = {"p": 0, "q": 0, "r": 0, "s": 1}
    step_at = {"p": "r", "q": "s", "r": "r", "s": "s"}
    no_tags = switching_min_tags(worlds, law_at, seed_at, task_at, step_at)
    assert no_tags == (None, None)
    repaired_seed_at = dict(seed_at, q=1)
    repair = switching_min_tags(worlds, law_at, repaired_seed_at, task_at, step_at)
    assert repair[0] == 2

    # Refining an output can break exact autonomous closure if a merged
    # predecessor has differently tagged successors. This does NOT mean
    # refining a code harms static task sufficiency.
    same_task = {w: 0 for w in worlds}
    assert switching_code_valid(worlds, law_at, seed_at, same_task,
                                step_at, (0, 0, 0))
    assert not switching_code_valid(worlds, law_at, seed_at, same_task,
                                    step_at, (0, 0, 1))

    # Law changes: two laws currently answer 0, but only one later changes
    # to the law that answers 1. Present task requires two tags; autonomous
    # closure requires three distinct tags in this particular contract.
    m_worlds = ("A", "B", "C")
    m_laws = {w: i for i, w in enumerate(m_worlds)}
    m_seeds = {w: 0 for w in m_worlds}
    m_tasks = {"A": 0, "B": 0, "C": 1}
    m_steps = {"A": "A", "B": "C", "C": "C"}
    m_minimum, m_tags = switching_min_tags(m_worlds, m_laws, m_seeds,
                                            m_tasks, m_steps)
    assert m_minimum == 3 and m_tags is not None

    random_switching_assignments = 0
    switch_rng = random.Random(160011)
    for _ in range(200):
        n = switch_rng.randint(2, 5)
        worlds_r = tuple(range(n))
        laws_r = {w: switch_rng.randrange(3) for w in worlds_r}
        seeds_r = {w: switch_rng.randrange(3) for w in worlds_r}
        tasks_r = {w: switch_rng.randrange(3) for w in worlds_r}
        steps_r = {w: switch_rng.randrange(n) for w in worlds_r}
        palettes = max(laws_r.values()) + 1
        for colors in product(range(3), repeat=palettes):
            assert switching_code_valid(worlds_r, laws_r, seeds_r, tasks_r,
                                        steps_r, colors) == switching_constraint_valid(
                                            worlds_r, laws_r, seeds_r, tasks_r,
                                            steps_r, colors)
            random_switching_assignments += 1

    bad = make_law("same-law-failure", [0, 1], {0: 0, 1: 0}, {0: 0, 1: 1})
    try:
        conflict_graph((bad, hold), 0)
    except ValueError:
        intrinsic_repair_needed = True
    else:
        raise AssertionError("law tags cannot repair within-law insufficiency")

    rng = random.Random(20261101)
    random_models = 0
    random_closed_models = 0
    finite_horizon_stabilization_checks = 0
    for _ in range(350):
        n = rng.randint(2, 5)
        laws = []
        for i in range(n):
            # An injective Seed ensures individual-law future sufficiency.
            size = rng.randint(1, 3)
            states = list(range(size))
            seed = {x: (x if rng.random() < 0.6 else x + 4) for x in states}
            task = {x: rng.randint(0, 2) for x in states}
            step = {x: rng.choice(states) for x in states}
            laws.append(make_law(str(i), states, seed, task, step))
        laws = tuple(laws)
        for h in range(4):
            edges, _ = conflict_graph(laws, h)
            optimum, coloring = chromatic_number(n, edges)
            oracle = independent_oracle_min_colors(laws, h)
            assert optimum == oracle
            assert has_uniform_decoder(laws, coloring, h)
            random_models += 1

        c_edges, _ = closure_graph(laws)
        c_optimum, c_color = chromatic_number(n, c_edges)
        assert c_optimum == direct_min_closed_colors(laws)
        assert has_autonomous_code(laws, c_color)
        random_closed_models += 1
        state_count = sum(len(l.states) for l in laws)
        # Moore partitions can strictly refine at most |W|-1 times.
        stabilized_edges, _ = conflict_graph(laws, state_count - 1)
        later_edges, _ = conflict_graph(laws, state_count + 3)
        assert stabilized_edges == later_edges
        finite_horizon_stabilization_checks += 1

    graph_checks = 0
    for n in range(1, 6):
        pairs = tuple(combinations(range(n), 2))
        for mask in range(1 << len(pairs)):
            edges = {pair for i, pair in enumerate(pairs) if mask & (1 << i)}
            laws = graph_realization(n, edges)
            got, _ = conflict_graph(laws, 0)
            assert got == edges
            optimum, coloring = chromatic_number(n, got)
            assert optimum == independent_oracle_min_colors(laws, 0)
            assert has_uniform_decoder(laws, coloring, 0)
            graph_checks += 1

    even = {x for x in product((0, 1), repeat=3) if sum(x) % 2 == 0}
    odd = {x for x in product((0, 1), repeat=3) if sum(x) % 2 == 1}
    assert even.isdisjoint(odd)
    assert all({(x[i], x[j]) for x in even} == {(x[i], x[j]) for x in odd}
               for i, j in combinations(range(3), 2))

    # A separate BM task-sufficiency check: nine straight panels give exact
    # polygonal area, not the unknown integral of an arbitrary smooth curve.
    panels = 9
    ordinates = [Fraction(i * i, panels * panels) for i in range(panels + 1)]
    panel_area = sum((ordinates[i] + ordinates[i + 1]) / (2 * panels)
                     for i in range(panels))
    true_parabola_area = Fraction(1, 3)
    error = panel_area - true_parabola_area
    certified_bound = Fraction(2, 12 * panels * panels)
    assert error == Fraction(1, 486) == certified_bound

    return {
        "scope": "Finite deterministic typed Seed law and task models, not a universal law",
        "static": {"laws": [l.name for l in static_laws],
                   "conflicts": sorted(static_edges), "minimal_tags": static_chi,
                   "coloring": static_tag,
                   "witnesses": {str(k): str(v) for k, v in static_witnesses.items()}},
        "future": future_cost,
        "within_law_inadequacy_caught": intrinsic_repair_needed,
        "random_same_contract_oracle_comparisons": random_models,
        "random_closed_code_oracle_comparisons": random_closed_models,
        "finite_horizon_stabilization_checks": finite_horizon_stabilization_checks,
        "future_only_vs_autonomous_counterexample": {
            "laws": [l.name for l in reset_laws],
            "task_trace_minimum_tags": 1,
            "autonomous_seed_update_minimum_tags": 2,
        },
        "simultaneous_receivers": {
            "receiver_1_minimum_tags": 2,
            "receiver_2_minimum_tags": 2,
            "joint_minimum_tags": 3,
        },
        "changing_law": {
            "impossible_with_only_law_tags": no_tags[0] is None,
            "one_extra_source_seed_bit_repairs": repair[0] == 2,
            "refinement_can_break_autonomous_closure": True,
            "three_laws_static_tags_needed": 2,
            "three_laws_autonomous_tags_needed": m_minimum,
            "random_pairwise_vs_full_closure_assignments": random_switching_assignments,
        },
        "all_graph_realizations_through_5_vertices": graph_checks,
        "even_odd_triples_pairwise_indistinguishable": True,
        "nine_segment_geometry": {
            "actual_polynomial_integral": str(true_parabola_area),
            "exact_polygonal_area": str(panel_area),
            "difference": str(error),
            "c2_interpolation_error_bound": str(certified_bound),
            "point_only_method_recovers_every_smooth_curve_area": False,
        },
        "known_limits": [
            "Output-trace and autonomous code-update requirements are separate",
            "The law name must itself be available to whoever emits a tag",
            "One total deterministic update per law; no partial or branching actions",
            "An explicitly separate switching-law model handles changing law identities",
            "Small exhaustive checks support but do not certify every theorem",
            "Graph coloring and future equivalence are established native ideas",
        ],
    }


if __name__ == "__main__":
    result_json = json.dumps(run(), sort_keys=True, indent=2, default=list) + "\n"
    if len(sys.argv) == 3 and sys.argv[1] == "--output":
        Path(sys.argv[2]).write_text(result_json, encoding="utf-8")
        print(f"Verified and wrote results: {sys.argv[2]}")
    elif len(sys.argv) == 1:
        print(result_json, end="")
    else:
        raise SystemExit("Usage: script.py [--output path.json]")
