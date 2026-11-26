#!/usr/bin/env python3
"""Small, exact BM application demonstrations, not deployment evaluations.

Python 3.10+, standard library. Runs the bundled unchanged BM finite analyzer
and its certificate checker. Additional parity/provenance checks use exact
enumeration. All worlds, tasks, actions and costs are declared toy models.
"""
from pathlib import Path
from itertools import combinations, product
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
import json

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'sources/BM_Necessity_Analyzer_2026-10-23.py'
PIN = 'c6c62b009f463f0ce4f0dcf4542492e534c2239667b9d4c3481b5c4756fb2021'


def main():
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == PIN
    spec = importlib.util.spec_from_file_location('bm_finite', SOURCE)
    bm = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bm)
    cases = {}

    def run(name, p):
        r = bm.analyze(p)
        assert bm.verify_result(p, r), name
        cases[name] = {'input': p, 'certificate': r}
        return r

    def candidate(r, features):
        return next(c for c in r['candidates'] if set(c['features']) == set(features))

    stock = {'states': ['stock_0', 'stock_1', 'stock_2'], 'actions': {},
             'tasks': {'in_stock': [False, True, True]},
             'observations': {'in_stock': [False, True, True], 'count': [0, 1, 2]}}
    r = run('migration_current_query', stock)
    assert candidate(r, ['in_stock'])['feasible'] and r['minimum_code_states_if_feasible'] == 2
    dynamic = {**stock, 'actions': {'reserve': [None, 0, 1]}}
    r = run('migration_future_updates', dynamic)
    assert not candidate(r, ['in_stock'])['feasible'] and r['minimum_code_states_if_feasible'] == 3

    bench = {'states': ['rule_A', 'rule_B', 'always_zero', 'always_one'], 'actions': {},
             'tasks': {'deployment_truth_table': ['0011', '0101', '0000', '1111']},
             'observations': {'old_tests_00_11': ['01', '01', '00', '11'],
                              'probe_01': [0, 1, 0, 1], 'probe_10': [1, 0, 0, 1]},
             'feature_costs': {'old_tests_00_11': 0, 'probe_01': 1, 'probe_10': 1}}
    r = run('benchmark_missing_distinction', bench)
    assert not candidate(r, ['old_tests_00_11'])['feasible']
    assert r['minimum_feature_cost'] == '1'

    logs = {'states': ['healthy', 'sensor_fault', 'actuator_fault', 'both_faults'],
            'actions': {}, 'tasks': {'fault_class': [0, 1, 2, 3]},
            'observations': {'alarm': [0, 1, 1, 1], 'sensor_test': [0, 1, 0, 1],
                             'actuator_test': [0, 0, 1, 1], 'verbose_trace': [0, 1, 2, 3]},
            'feature_costs': {'alarm': 1, 'sensor_test': 1, 'actuator_test': 1, 'verbose_trace': 10}}
    r = run('minimum_diagnostic_logging', logs)
    assert r['minimum_feature_cost'] == '2'
    assert r['minimum_cost_candidates'] == [['actuator_test', 'sensor_test']]

    pairs = list(product((0, 1), repeat=2))
    obs = {'parity_cache': [a ^ b for a, b in pairs],
           'component_A': [a for a, b in pairs], 'component_B': [b for a, b in pairs]}
    cache = {'states': [f'{a}{b}' for a, b in pairs], 'actions': {},
             'tasks': {'parity': obs['parity_cache']}, 'observations': obs}
    old = run('cache_original_task', cache)
    assert candidate(old, ['parity_cache'])['feasible'] and old['minimum_code_states_if_feasible'] == 2
    new = run('cache_expanded_task', {**cache, 'tasks': {**cache['tasks'], 'first_component': obs['component_A']}})
    assert not candidate(new, ['parity_cache'])['feasible']
    assert candidate(new, ['parity_cache', 'component_A'])['feasible']
    assert new['minimum_code_states_if_feasible'] == 4

    histories = list(product((0, 1), repeat=2))  # (previous display, current display)
    undo = {'states': [f'previous_{p}_current_{c}' for p, c in histories],
            'actions': {'undo': [histories.index((p, p)) for p, c in histories]},
            'tasks': {'display': [c for p, c in histories]},
            'observations': {'current': [c for p, c in histories], 'previous': [p for p, c in histories]}}
    r = run('undo_save_state', undo)
    assert r['minimum_code_states_if_feasible'] == 4 and not candidate(r, ['current'])['feasible']
    assert candidate(r, ['current', 'previous'])['feasible']

    reward = {'states': ['not_done_not_reported', 'not_done_reported', 'done_not_reported', 'done_reported'],
              'actions': {}, 'tasks': {'completed': [0, 0, 1, 1]},
              'observations': {'score_reported_completion': [0, 1, 0, 1], 'verified_completion': [0, 0, 1, 1]}}
    r = run('reward_metric_gap', reward)
    assert not candidate(r, ['score_reported_completion'])['feasible']
    assert candidate(r, ['verified_completion'])['feasible']

    curriculum = {'states': ['neither_skill', 'only_B', 'only_A', 'both_skills'], 'actions': {},
                  'tasks': {'next_lesson': ['A_and_B', 'A', 'B', 'advanced']},
                  'observations': {'total_score': [0, 1, 1, 2], 'item_A': [0, 0, 1, 1], 'item_B': [0, 1, 0, 1]},
                  'feature_costs': {'total_score': 0, 'item_A': 1, 'item_B': 1}}
    r = run('curriculum_diagnostic', curriculum)
    assert not candidate(r, ['total_score'])['feasible'] and r['minimum_feature_cost'] == '1'

    corpora = {parity: [row for row in product((0, 1), repeat=3) if sum(row) % 2 == parity] for parity in (0, 1)}
    equal_marginals = []
    for size in (1, 2):
        for columns in combinations(range(3), size):
            margins = [Counter(tuple(row[i] for i in columns) for row in corpora[p]) for p in (0, 1)]
            assert margins[0] == margins[1]
            equal_marginals.append(list(columns))
    parity_means = [sum((Fraction(sum(row) % 2) for row in corpora[p]), Fraction()) / 4 for p in (0, 1)]
    assert parity_means == [0, 1]

    origins = {'three_copies': ['source_A', 'source_A', 'source_A'],
               'three_sources': ['source_A', 'source_B', 'source_C']}
    assert len(origins['three_copies']) == len(origins['three_sources']) == 3
    assert len(set(origins['three_copies'])) == 1 and len(set(origins['three_sources'])) == 3

    out = {
        'date': '2026-10-29', 'status': 'passed',
        'scope': 'Exact finite illustrations, not empirical application trials or proof of BM exclusivity.',
        'analyzer_source_sha256': PIN, 'analyzer_contracts_verified': len(cases),
        'finite_contracts': cases,
        'synthetic_data': {'even_corpus': corpora[0], 'odd_corpus': corpora[1],
                           'equal_single_and_pair_marginals': equal_marginals,
                           'parity_task_means': [str(x) for x in parity_means]},
        'provenance': {'source_lists': origins, 'distinct_source_counts': [1, 3],
                       'limitation': 'Distinct source identifiers do not prove statistical independence or truth.'},
        'summary': {'migration_current_code_states': 2, 'migration_future_code_states': 3,
                    'additional_benchmark_probes': 1, 'diagnostic_feature_cost': '2',
                    'cache_old_code_states': 2, 'cache_new_code_states': 4,
                    'undo_code_states': 4, 'additional_curriculum_item_cost': '1',
                    'matching_low_order_marginals': len(equal_marginals)},
    }
    (ROOT / 'BM_Application_Demonstrations_2026-10-29.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({'status': out['status'], 'analyzer_contracts_verified': len(cases),
                      'summary': out['summary']}, indent=2))


if __name__ == '__main__':
    main()
