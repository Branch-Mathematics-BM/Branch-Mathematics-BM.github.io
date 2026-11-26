#!/usr/bin/env python3
"""Independent exhaustive finite oracle and adversarial checks for necessity audit."""
import copy
from importlib.util import spec_from_file_location, module_from_spec
from itertools import product, combinations
import json
from pathlib import Path
import random
import time

ROOT = Path(__file__).resolve().parent
spec = spec_from_file_location("necessity", ROOT / "BM_Necessity_Analyzer_2026-10-23.py")
bm = module_from_spec(spec)
spec.loader.exec_module(bm)


def partitions(n):
    def go(xs):
        if len(xs) == n:
            yield tuple(xs)
        else:
            for q in range(max(xs, default=-1) + 2):
                yield from go(xs + [q])
    return list(go([]))


def oracle(p, features):
    # Enumerate every possible code partition, instead of computing future
    # equivalence or using the analyzer's refinement/witness procedures.
    n = len(p['states'])
    best = None
    for c in partitions(n):
        okay = True
        for x, y in combinations(range(n), 2):
            sameobs = all(json.dumps(p['observations'][f][x]) == json.dumps(p['observations'][f][y]) for f in features)
            if sameobs and c[x] != c[y]:
                okay = False
                break
            if c[x] == c[y]:
                if any(json.dumps(v[x]) != json.dumps(v[y]) for v in p['tasks'].values()):
                    okay = False
                    break
                for row in p['actions'].values():
                    a, b = row[x], row[y]
                    if (a is None) != (b is None) or (a is not None and c[a] != c[b]):
                        okay = False
                        break
            if not okay:
                break
        if okay:
            size = len(set(c))
            best = size if best is None else min(size, best)
    return best


def check_problem(p, counters):
    result = bm.analyze(p)
    assert bm.verify_result(p, result)
    counters['certificates_checked'] += 1
    for candidate in result['candidates']:
        best = oracle(p, candidate['features'])
        assert candidate['feasible'] == (best is not None)
        if best is not None:
            assert best == result['minimum_code_states_if_feasible']
        counters['independent_candidate_comparisons'] += 1
    for w in result['quotient']['separation_witnesses']:
        assert bm.verify_failure(p, w)
        assert len(w['word']) <= result['strict_round_bound']
        for length in range(len(w['word'])):
            for word in product(sorted(p['actions']), repeat=length):
                x, y = w['states']
                for a in word:
                    row = p['actions'][a]
                    x, y = None if x is None else row[x], None if y is None else row[y]
                if x is None or y is None:
                    assert x is None and y is None
                else:
                    assert all(json.dumps(v[x]) == json.dumps(v[y]) for v in p['tasks'].values())
                counters['shorter_word_checks'] += 1
        counters['separation_witnesses_replayed'] += 1
    return result


def examples():
    states = list(product(range(2), repeat=2))
    delayed = {'states': [str(s) for s in states], 'actions': {'step': [states.index((v,v)) for x,v in states]},
               'tasks': {'position': [x for x,v in states]},
               'observations': {'position': [x for x,v in states], 'velocity': [v for x,v in states]}}
    xyz = list(product(range(2), repeat=3))
    discard = {'states': [str(s) for s in xyz], 'actions': {'step': [xyz.index((a,c,c)) for a,b,c in xyz]},
               'tasks': {'a': [a for a,b,c in xyz]},
               'observations': {'a': [a for a,b,c in xyz], 'b': [b for a,b,c in xyz]}}
    duplicate = {'states': ['0','1'], 'actions': {}, 'tasks': {'answer': [0,1]},
                 'observations': {'primary': [0,1], 'backup': [0,1]}, 'feature_costs': {'primary':'2','backup':'1/2'}}
    unavailable = {'states':['enabled','disabled'], 'actions':{'run':[0,None]},
                   'tasks':{'answer':[0,0]}, 'observations':{'reading':[0,0]}}
    xor = {'states':[str(s) for s in states], 'actions':{},
           'tasks':{'xor':[a^b for a,b in states]},
           'observations':{'a':[a for a,b in states], 'b':[b for a,b in states]}}
    empty = {'states':['s'], 'actions':{}, 'tasks':{}, 'observations':{}}
    catalogue_empty = {**duplicate, 'candidates': [], 'comparison_scope':'empty supplied class; no infeasibility conclusion beyond that class'}
    legacy = copy.deepcopy(discard)
    legacy['tasks']['retained_b'] = legacy['observations']['b'][:]
    return {'delayed_velocity':delayed, 'discard_nonpredictive_observation':discard,
            'duplicate_observations':duplicate, 'availability_obstruction':unavailable,
            'joint_xor':xor, 'empty_observation_success':empty,
            'empty_candidate_catalogue':catalogue_empty, 'legacy_retention_changes_contract':legacy}


def main():
    started = time.monotonic()
    counters = {'certificates_checked':0, 'independent_candidate_comparisons':0,
                'separation_witnesses_replayed':0, 'shorter_word_checks':0,
                'malformed_inputs_rejected':0, 'corrupted_certificates_rejected':0}
    exhaustive = 0
    for n in range(1,4):
        for action in product([None]+list(range(n)), repeat=n):
            for task in product(range(2), repeat=n):
                for obs in partitions(n):
                    p = {'states':list(map(str,range(n))), 'actions':{'a':list(action)},
                         'tasks':{'t':list(task)}, 'observations':{'o':list(obs)}}
                    check_problem(p,counters)
                    exhaustive += 1
    rng = random.Random(20261023)
    for case in range(180):
        n = 4 + case % 2
        p = {'states':list(map(str,range(n))),
             'actions':{k:[rng.choice([None]+list(range(n))) for _ in range(n)] for k in ('a','b')},
             'tasks':{'t':[rng.randrange(2) for _ in range(n)]},
             'observations':{k:[rng.randrange(2) for _ in range(n)] for k in ('x','y','z')}}
        check_problem(p,counters)
    ex = examples()
    results = {name:check_problem(p,counters) for name,p in ex.items()}
    assert results['delayed_velocity']['essential_features'] == ['position','velocity']
    assert results['delayed_velocity']['minimum_code_states_if_feasible'] == 4
    assert results['discard_nonpredictive_observation']['full_observation']['feasible']
    assert results['discard_nonpredictive_observation']['minimum_code_states_if_feasible'] == 2
    # Confirm that the unprocessed observation (a,b) really fails autonomy.
    p = ex['discard_nonpredictive_observation']
    x,y=0,1
    assert [v[x] for v in p['observations'].values()] == [v[y] for v in p['observations'].values()]
    xx,yy=p['actions']['step'][x],p['actions']['step'][y]
    assert [v[xx] for v in p['observations'].values()] != [v[yy] for v in p['observations'].values()]
    assert results['duplicate_observations']['essential_features'] == []
    assert results['duplicate_observations']['minimum_feature_cost'] == '1/2'
    assert not results['availability_obstruction']['full_observation']['feasible']
    assert results['availability_obstruction']['full_observation']['failure']['reason'] == 'availability'
    assert results['joint_xor']['essential_features'] == ['a','b']
    assert results['joint_xor']['minimum_code_states_if_feasible'] == 2
    assert results['empty_observation_success']['catalogue_has_feasible_candidate']
    assert not results['empty_candidate_catalogue']['catalogue_has_feasible_candidate']
    assert not results['legacy_retention_changes_contract']['full_observation']['feasible']
    p = ex['delayed_velocity']
    bads = []
    for change in ('task_float','bool_successor','outside_successor','duplicate_states','negative_cost','unknown_feature','duplicate_candidate','unknown_field'):
        bad = copy.deepcopy(p)
        if change == 'task_float': bad['tasks']['position'][0] = 0.5
        if change == 'bool_successor': bad['actions']['step'][0] = True
        if change == 'outside_successor': bad['actions']['step'][0] = 100
        if change == 'duplicate_states': bad['states'][1] = bad['states'][0]
        if change == 'negative_cost': bad['feature_costs'] = {'position':'-1'}
        if change == 'unknown_feature': bad['candidates'] = [['missing']]
        if change == 'duplicate_candidate': bad['candidates'] = [[],[]]
        if change == 'unknown_field': bad['stochastic'] = True
        bads.append(bad)
    for bad in bads:
        try: bm.analyze(bad)
        except ValueError: counters['malformed_inputs_rejected'] += 1
        else: raise AssertionError('malformed contract accepted')
    good = results['delayed_velocity']
    for change in ('hash','partition','transition','task','witness','missing_witness','cost','essential','encoder','candidate','minimum','scope','catalogue_scope','essentiality_scope'):
        bad = copy.deepcopy(good)
        if change == 'hash': bad['input_sha256'] = 'wrong'
        if change == 'partition': bad['quotient']['code_of_state'] = [0]*4
        if change == 'transition': bad['quotient']['actions']['step'][0] = 3
        if change == 'task': bad['quotient']['tasks']['position'][0] = 9
        if change == 'witness': bad['quotient']['separation_witnesses'][0]['word'] = []
        if change == 'missing_witness': bad['quotient']['separation_witnesses'].pop()
        if change == 'cost': bad['candidates'][0]['cost'] = '50'
        if change == 'essential': bad['essential_features'] = []
        if change == 'encoder': bad['full_observation']['encoder'][0]['code'] = 3
        if change == 'candidate': bad['candidates'].pop()
        if change == 'minimum': bad['minimum_code_states_if_feasible'] = 1
        if change == 'scope': bad['scope'] = 'all native sectors'
        if change == 'catalogue_scope': bad['catalogue_kind'] = 'supplied observation subsets'
        if change == 'essentiality_scope': bad['essentiality_status'] = 'unconditional indispensability'
        assert not bm.verify_result(p,bad), change
        counters['corrupted_certificates_rejected'] += 1
    output = {'status':'PASS', 'exhaustive_small_native_instances':exhaustive,
              'seeded_multi_action_instances':180, 'seed':20261023, 'worked_examples':len(ex),
              **counters, 'elapsed_seconds':round(time.monotonic()-started,3),
              'scope':'Internal differential checking against exhaustive code partitions; not external review or a proof assistant.'}
    (ROOT/'BM_Necessity_Examples_2026-10-23.json').write_text(json.dumps(ex,indent=2)+'\n')
    (ROOT/'BM_Necessity_Certificates_2026-10-23.json').write_text(json.dumps(results,indent=2)+'\n')
    (ROOT/'BM_Necessity_Verification_2026-10-23.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))


if __name__ == '__main__':
    main()
