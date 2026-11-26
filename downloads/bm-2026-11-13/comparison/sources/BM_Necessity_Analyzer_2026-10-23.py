#!/usr/bin/env python3
"""Exact finite deterministic BM necessity audit; Python 3.10+, standard library.

Usage: python BM_Necessity_Analyzer_2026-10-23.py problem.json
Every native state is initially possible. Actions are partial deterministic maps.
Task values and observation labels are exact JSON scalars (no floats). A code may
be any deterministic function of the selected observations. The contract preserves
all task values and action availability for every finite action word. There is no
claim about regularity, stochastic processes, hardware cost or physical inference.
"""
from collections import deque
from fractions import Fraction
from itertools import combinations
import hashlib
import json
import sys

SCOPE = "finite partial deterministic; all states initially possible; arbitrary deterministic postprocessing; exact tasks and availability for all finite words"


def canon(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(problem):
    return hashlib.sha256(canon(problem).encode()).hexdigest()


def validate(problem):
    if not isinstance(problem, dict):
        raise ValueError("problem must be an object")
    allowed = {"states", "actions", "tasks", "observations", "feature_costs", "candidates", "comparison_scope"}
    if set(problem) - allowed:
        raise ValueError("unknown contract fields: " + ", ".join(sorted(set(problem) - allowed)))
    states = problem.get("states")
    if not isinstance(states, list) or not 1 <= len(states) <= 64 or any(not isinstance(x, str) for x in states) or len(set(states)) != len(states):
        raise ValueError("1..64 unique string state names required")
    n = len(states)
    for field in ("actions", "tasks", "observations"):
        data = problem.get(field)
        if not isinstance(data, dict) or any(not isinstance(k, str) or not k for k in data):
            raise ValueError(field + " must map nonempty names to arrays")
        for values in data.values():
            if not isinstance(values, list) or len(values) != n:
                raise ValueError(field + " arrays must have one value per state")
            if field == "actions":
                if any(v is not None and (type(v) is not int or not 0 <= v < n) for v in values):
                    raise ValueError("successors must be state indices or null")
            elif any(type(v) not in (str, int, bool, type(None)) for v in values):
                raise ValueError("exact scalar task/observation labels required; no floats")
    if len(problem["actions"]) > 8 or len(problem["observations"]) > 12:
        raise ValueError("implementation limit: 8 actions, 12 observations")
    costs = problem.get("feature_costs", {})
    if not isinstance(costs, dict) or set(costs) - set(problem["observations"]):
        raise ValueError("costs must name existing observations")
    for v in costs.values():
        if type(v) not in (str, int):
            raise ValueError("costs must be exact integers or rational strings")
        try:
            cost = Fraction(v)
        except (ValueError, ZeroDivisionError):
            raise ValueError("invalid rational cost") from None
        if cost < 0:
            raise ValueError("feature costs must be nonnegative")
    candidates = problem.get("candidates")
    if candidates is not None:
        if not isinstance(candidates, list):
            raise ValueError("candidates must be an explicitly supplied list of subsets")
        seen = set()
        for c in candidates:
            if not isinstance(c, list) or any(not isinstance(k, str) or k not in problem["observations"] for k in c) or len(set(c)) != len(c):
                raise ValueError("candidate must list distinct existing observation names")
            key = tuple(sorted(c))
            if key in seen:
                raise ValueError("duplicate candidate")
            seen.add(key)
    return problem


def task_key(p, state):
    # The tag distinguishes undefined action words from any legitimate task value.
    if state is None or state == len(p["states"]):
        return ("undefined",)
    return ("live", canon([p["tasks"][k][state] for k in sorted(p["tasks"])]))


def obs_key(p, features, state):
    return canon([p["observations"][k][state] for k in features])


def normalize(values):
    table = {}
    return [table.setdefault(v, len(table)) for v in values]


def future_partition(p):
    n = len(p["states"])
    actions = [p["actions"][a] + [None] for a in sorted(p["actions"])]
    initial = [task_key(p, x) for x in range(n + 1)]
    colors = normalize(initial)
    rounds = 0
    while True:
        signatures = [(colors[x], tuple(colors[n if row[x] is None else row[x]] for row in actions)) for x in range(n + 1)]
        updated = normalize(signatures)
        if updated == colors:
            break
        colors = updated
        rounds += 1
    return colors[:n], rounds, len(set(initial[:n]))


def distinguish(p, left, right):
    """Breadth-first search, independently replayable shortest action word."""
    todo = deque([(left, right, [])])
    seen = {(left, right)}
    while todo:
        x, y, word = todo.popleft()
        if task_key(p, x) != task_key(p, y):
            return {"states": [left, right], "word": word,
                    "reason": "availability" if x is None or y is None else "task",
                    "terminal_states": [x, y]}
        for a in sorted(p["actions"]):
            row = p["actions"][a]
            xx, yy = (None if x is None else row[x]), (None if y is None else row[y])
            if (xx, yy) not in seen:
                seen.add((xx, yy))
                todo.append((xx, yy, word + [a]))
    return None


def verify_failure(p, certificate, features=None):
    """Replay a negative witness using only the supplied native tables."""
    try:
        left, right = certificate["states"]
        n = len(p["states"])
        if any(type(v) is not int or not 0 <= v < n for v in (left, right)):
            return False
        if features is not None and obs_key(p, features, left) != obs_key(p, features, right):
            return False
        x, y = left, right
        if not isinstance(certificate["word"], list) or any(not isinstance(a, str) for a in certificate["word"]):
            return False
        for a in certificate["word"]:
            row = p["actions"][a]
            x, y = (None if x is None else row[x]), (None if y is None else row[y])
        reason = "availability" if x is None or y is None else "task"
        return task_key(p, x) != task_key(p, y) and certificate["terminal_states"] == [x, y] and certificate["reason"] == reason
    except (KeyError, IndexError, TypeError, ValueError):
        return False


def candidate(p, colors, features):
    features = sorted(features)
    seen = {}
    for x in range(len(colors)):
        key = obs_key(p, features, x)
        if key in seen and colors[seen[key]] != colors[x]:
            failure = distinguish(p, seen[key], x)
            assert failure is not None
            return {"features": features, "feasible": False, "failure": failure}
        seen.setdefault(key, x)
    return {"features": features, "feasible": True,
            "encoder": [{"observation": json.loads(key), "code": colors[x]} for key, x in seen.items()]}


def analyze(problem):
    p = validate(problem)
    colors, rounds, initial_blocks = future_partition(p)
    reps = [colors.index(k) for k in range(max(colors) + 1)]
    quotient = {"code_of_state": colors, "representatives": reps,
                "tasks": {k: [v[x] for x in reps] for k, v in sorted(p["tasks"].items())},
                "actions": {k: [None if v[x] is None else colors[v[x]] for x in reps] for k, v in sorted(p["actions"].items())},
                "separation_witnesses": [distinguish(p, x, y) for x, y in combinations(reps, 2)]}
    features = sorted(p["observations"])
    catalogue = p.get("candidates")
    if catalogue is None:
        catalogue = [list(c) for size in range(len(features) + 1) for c in combinations(features, size)]
    candidates = [candidate(p, colors, c) for c in catalogue]
    for c in candidates:
        c["cost"] = str(sum((Fraction(p.get("feature_costs", {}).get(k, 1)) for k in c["features"]), Fraction()))
    feasible = [c for c in candidates if c["feasible"]]
    full = candidate(p, colors, features)
    removals = {k: candidate(p, colors, [f for f in features if f != k]) for k in features}
    minimum_cost = min((Fraction(c["cost"]) for c in feasible), default=None)
    result = {"schema": "BM finite necessity certificate 1", "input_sha256": digest(p),
              "scope": SCOPE,
              "quotient": quotient, "minimum_code_states_if_feasible": len(reps),
              "strict_refinement_rounds": rounds, "initial_task_blocks": initial_blocks,
              "strict_round_bound": len(colors) - initial_blocks,
              "catalogue_kind": "all observation subsets" if "candidates" not in p else "supplied observation subsets",
              "candidates": candidates, "full_observation": full, "leave_one_out": removals,
              "essential_features": [k for k in features if full["feasible"] and not removals[k]["feasible"]],
              "essentiality_status": "nonvacuous relative to observation removal" if full["feasible"] else "full observation insufficient; no essentiality claim",
              "catalogue_has_feasible_candidate": bool(feasible),
              "inclusion_minimal_in_catalogue": [c["features"] for c in feasible if not any(set(d["features"]) < set(c["features"]) for d in feasible)],
              "minimum_feature_cost": None if minimum_cost is None else str(minimum_cost),
              "minimum_cost_candidates": [c["features"] for c in feasible if Fraction(c["cost"]) == minimum_cost]}
    return result


def verify_result(problem, result):
    """Positive descent + pair witnesses verify the quotient without refinement.

    Optimization/candidate metadata is recomputed by finite set operations. This is
    an internal exact checker, not proof-assistant certification or external review.
    """
    try:
        p = validate(problem)
        if result["schema"] != "BM finite necessity certificate 1" or result["input_sha256"] != digest(p):
            return False
        if result["scope"] != SCOPE:
            return False
        if result["catalogue_kind"] != ("all observation subsets" if "candidates" not in p else "supplied observation subsets"):
            return False
        q = result["quotient"]
        c, reps = q["code_of_state"], q["representatives"]
        n = len(p["states"])
        if len(c) != n or any(type(v) is not int or v < 0 for v in c) or c != normalize(c) or reps != [c.index(k) for k in range(max(c)+1)]:
            return False
        if result["minimum_code_states_if_feasible"] != len(reps):
            return False
        expected_tasks = {k: [v[x] for x in reps] for k, v in sorted(p["tasks"].items())}
        expected_actions = {k: [None if v[x] is None else c[v[x]] for x in reps] for k, v in sorted(p["actions"].items())}
        if canon(q["tasks"]) != canon(expected_tasks) or q["actions"] != expected_actions:
            return False
        for x in range(n):
            r = reps[c[x]]
            if task_key(p, x) != task_key(p, r):
                return False
            for row in p["actions"].values():
                xx, rr = row[x], row[r]
                if (xx is None) != (rr is None) or (xx is not None and c[xx] != c[rr]):
                    return False
        witnesses = q["separation_witnesses"]
        if len(witnesses) != len(reps)*(len(reps)-1)//2:
            return False
        for (x, y), witness in zip(combinations(reps, 2), witnesses):
            if witness["states"] != [x, y] or not verify_failure(p, witness):
                return False
        features = sorted(p["observations"])
        catalogue = p.get("candidates", [list(s) for k in range(len(features)+1) for s in combinations(features,k)])
        items = result["candidates"]
        if len(items) != len(catalogue) or [x["features"] for x in items] != [sorted(x) for x in catalogue]:
            return False
        all_checks = items + [result["full_observation"]] + list(result["leave_one_out"].values())
        if result["full_observation"]["features"] != features or set(result["leave_one_out"]) != set(features):
            return False
        if result["essentiality_status"] != ("nonvacuous relative to observation removal" if result["full_observation"]["feasible"] else "full observation insufficient; no essentiality claim"):
            return False
        for f in features:
            if result["leave_one_out"][f]["features"] != [k for k in features if k != f]:
                return False
        for item in all_checks:
            fs = item["features"]
            if type(item["feasible"]) is not bool:
                return False
            if item["feasible"]:
                enc = item["encoder"]
                lookup = {canon(e["observation"]): e["code"] for e in enc}
                if len(lookup) != len(enc) or set(lookup) != {obs_key(p, fs, x) for x in range(n)}:
                    return False
                if any(lookup[obs_key(p, fs, x)] != c[x] for x in range(n)):
                    return False
            elif not verify_failure(p, item["failure"], fs):
                return False
        feasible = [x for x in items if x["feasible"]]
        for item in items:
            cost = sum((Fraction(p.get("feature_costs", {}).get(k,1)) for k in item["features"]), Fraction())
            if item["cost"] != str(cost):
                return False
        minimum = min((Fraction(x["cost"]) for x in feasible), default=None)
        essential = [f for f in features if result["full_observation"]["feasible"] and not result["leave_one_out"][f]["feasible"]]
        if result["essential_features"] != essential or result["minimum_feature_cost"] != (None if minimum is None else str(minimum)):
            return False
        if result["catalogue_has_feasible_candidate"] != bool(feasible):
            return False
        if result["inclusion_minimal_in_catalogue"] != [x["features"] for x in feasible if not any(set(y["features"]) < set(x["features"]) for y in feasible)]:
            return False
        if result["minimum_cost_candidates"] != [x["features"] for x in feasible if Fraction(x["cost"]) == minimum]:
            return False
        initial_blocks = len({task_key(p,x) for x in range(n)})
        if result["initial_task_blocks"] != initial_blocks or result["strict_round_bound"] != n-initial_blocks:
            return False
        if type(result["strict_refinement_rounds"]) is not int or not 0 <= result["strict_refinement_rounds"] <= n-initial_blocks:
            return False
        # Runtime rounds are diagnostic; the minimality proof is the witness set.
        return True
    except (KeyError, IndexError, TypeError, ValueError, ZeroDivisionError):
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    with open(sys.argv[1], encoding="utf-8") as handle:
        problem = json.load(handle)
    result = analyze(problem)
    if not verify_result(problem, result):
        raise RuntimeError("internal certificate verification failed")
    print(json.dumps(result, ensure_ascii=False, indent=2))
