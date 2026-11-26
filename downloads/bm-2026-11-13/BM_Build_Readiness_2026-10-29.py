#!/usr/bin/env python3
"""Build an additive BM readiness supplement without changing the old inventory.

This checks identifier structure, not mathematical validity or completeness of
dependencies. Source trace reviews are internal and do not imply peer review.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import sys


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def main(root):
    ledger_path = root / 'source_evidence/BM_Completeness_Readiness_2026-10-23.json'
    base = read(ledger_path)
    trace = read(root / 'BM_Source_Trace_2026-10-29.json')
    integrity = read(root / 'BM_Source_Integrity_2026-10-29.json')
    network = read(root / 'BM_Network_Seed_Results_2026-10-29.json')
    replay = read(root / 'BM_Comparison_Replay_2026-10-29.json')
    examples = read(root / 'BM_Proof_Examples_Verifier_2026-10-29.json')
    comparison = read(root / 'comparison/BM_Comparison_Results_2026-10-24.json')
    assert all(integrity['files']) and all(f['matches_manifest'] for f in integrity['files'])
    assert network['status'] == replay['status'] == examples['status'] == comparison['status'] == 'passed'
    assert trace['base_inventory_sha256'] == hashlib.sha256(ledger_path.read_bytes()).hexdigest()
    inventory = base['inventory']
    ids = [r['id'] for r in inventory]
    assert len(ids) == len(set(ids)), 'Duplicate inventory ID'
    all_ids = set(ids)
    bm = [r for r in inventory if r['framework'] == 'BM']
    assert all(r['statement'] and r['sources'] for r in bm)
    graph = {r['id']: set(filter(None, r['dependencies'].split(';'))) for r in bm}
    original_edges = sum(map(len, graph.values()))
    named_review_edges = 0
    for row in trace['rows']:
        review = row['internal_review']
        if review:
            direct = review['direct_BM_results']
            named_review_edges += len(direct)
            graph[row['id']].update(direct)
    canonical = base['readiness_supplement']['canonical_proof_map']
    canonical_edges = sum(len(row['direct_proof_dependencies']) for row in canonical)
    for row in canonical:
        graph[row['id']].update(row['direct_proof_dependencies'])
    unresolved = [(identifier, dep) for identifier, deps in graph.items()
                  for dep in deps if dep not in all_ids]
    assert not unresolved, unresolved
    state = {}
    def visit(node):
        if state.get(node) == 1:
            raise ValueError('Cycle in listed BM dependency graph at ' + node)
        if state.get(node) == 2:
            return
        state[node] = 1
        for dep in graph.get(node, ()):
            visit(dep)
        state[node] = 2
    for node in graph:
        visit(node)
    summary = comparison['summary']
    counts = {key: summary[key] for key in ('finite_cases', 'interface_cases', 'linear_cases', 'noisy_cases')}
    assert sum(counts.values()) == 162 and summary['mathematical_disagreements'] == 0
    nt = network['tests']
    supplement = {
        'date': '2026-10-29',
        'scope': 'Additive Branch Mathematics development; frozen foundation and original inventory are unchanged.',
        'source_hashes_verified': integrity['checked'],
        'BM_inventory_count': len(bm),
        'BM_classification_counts': dict(Counter(r['classification'] for r in bm)),
        'source_locators': trace['source_locators'],
        'new_internal_proof_basis_reviews': trace['new_manually_reviewed'],
        'previously_empty_dependency_rows_awaiting_basis_review': trace['still_requiring_dependency_review'],
        'proof_locator_file': 'BM_Source_Trace_2026-10-29.json',
        'proof_review_scope': 'Internal review of the source argument and stated scope; not independent review, a formal proof, or historical priority.',
        'dependency_structure': {
            'BM_records_with_previously_listed_dependencies': sum(bool(r['dependencies']) for r in bm),
            'previously_listed_dependency_links': original_edges,
            'new_review_named_links': named_review_edges,
            'earlier_canonical_proof_map_links': canonical_edges,
            'combined_distinct_listed_links': sum(map(len, graph.values())),
            'unresolved_identifiers': unresolved,
            'directed_cycle_detected': False,
            'limitations': 'Identifier resolution and acyclicity do not prove the links are complete, necessary, sufficient, or mathematically valid.',
        },
        'direct_comparison': {
            **counts, 'total_cases': sum(counts.values()),
            'mathematical_disagreements': summary['mathematical_disagreements'],
            'CLUE_exact_linear_cases': counts['linear_cases'],
            'independent_peer_review': False,
            'scope': 'Fixed internal benchmark, same declared task contracts; no general speed or unique-advantage claim.',
        },
        'independent_code_replay': replay,
        'finite_network_seed_development': {
            'join_tree_models': nt['join_tree']['random_models'],
            'local_tuple_extensions': nt['join_tree']['local_tuples_with_global_extensions'],
            'cycle_parity': nt['cycle_parity'],
            'recurrence': nt['recurrence'],
            'weighted_inner_consistency_counterexample': nt['annotated_counterexample'],
            'spatial_seed_model_is_a_physical_law': False,
        },
        'example_checks': examples,
        'outstanding_gates': [
            'Independently check proofs, long analytic arguments, and imported theorem hypotheses.',
            'Substantively audit previously populated dependency lists; identifier checks do not prove completeness.',
            'Address the six broad open families in the accompanying BM completion report under precise assumptions.',
            'Test practical added value on declared real applications and continue historical comparison.',
            'Recover unavailable prior research records before claiming a complete historical archive.',
        ],
        'overall_status': 'Scoped progress; completion of every intended BM claim has not been established.',
    }
    assert base['inventory'] == inventory
    base['completion_supplement_2026_10_29'] = supplement
    output = root / 'BM_Readiness_Register_2026-10-29.json'
    output.write_text(json.dumps(base, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps({'BM_records': len(bm), 'reviewed': trace['new_manually_reviewed'],
                      'remaining_in_review_set': trace['still_requiring_dependency_review'],
                      'listed_links': supplement['dependency_structure']['combined_distinct_listed_links'],
                      'comparison_cases': sum(counts.values())}, indent=2))


if __name__ == '__main__':
    main(Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve())
