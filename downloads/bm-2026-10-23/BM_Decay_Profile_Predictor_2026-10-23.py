#!/usr/bin/env python3
"""Finite response-tree predictor for BM23-I1; exact rational construction.

The caller supplies a profile oracle and independently proves the uniform tail
bound M L**k. This program checks parameters and the finite supplied values; it
cannot establish a tail property of an arbitrary black-box native system.
"""
from fractions import Fraction as F
from dataclasses import dataclass


def rational(x):
    if isinstance(x, bool) or not isinstance(x, (int, str, F)):
        raise ValueError('Use integer/rational inputs, not floats/bools.')
    return F(x)


def rounding_index(x, h):
    y = x/h + F(1, 2)
    return y.numerator // y.denominator


@dataclass(frozen=True)
class Tree:
    label: tuple
    children: tuple


def parameters(actions, dimension, bound, contraction, epsilon):
    if isinstance(actions, bool) or not isinstance(actions, int) or actions < 1:
        raise ValueError('Positive integer action count required.')
    if isinstance(dimension, bool) or not isinstance(dimension, int) or dimension < 1:
        raise ValueError('Positive integer output dimension required.')
    m, l, e = map(rational, (bound, contraction, epsilon))
    if m < 0 or not 0 <= l < 1 or e <= 0:
        raise ValueError('Require M>=0, 0<=L<1 and epsilon>0.')
    k = 0
    while m*l**k > e/2:
        k += 1
    h = e/(2*dimension)
    ratio = m/h
    j = -((-ratio.numerator)//ratio.denominator)+1
    q = (2*j+1)**dimension
    node_counts = []
    profile_count = 0
    total = 1
    for depth in range(1, k+1):
        profile_count = 1 + actions*profile_count
        node_counts.append(profile_count)
        total += q**profile_count
    return {'actions': actions, 'dimension': dimension, 'M': m, 'L': l,
            'epsilon': e, 'K': k, 'h': h, 'J': j, 'label_count': q,
            'codebook_state_bound': total, 'level_node_counts': node_counts,
            'tail_bound': m*l**k,
            'oracle_coordinate_error_allowed': e/(4*dimension)}


def build(profile, p):
    """profile(word) gives p coordinates within the stated oracle accuracy.

    The returned initial state belongs to one finite universal codebook. Child
    selection is its update. None is the zero-output absorbing state.
    """
    def visit(word, remaining):
        if remaining == 0:
            return None
        values = tuple(rational(v) for v in profile(word))
        if len(values) != p['dimension']:
            raise ValueError('Profile output dimension mismatch.')
        if any(abs(v) > p['M'] + p['oracle_coordinate_error_allowed'] for v in values):
            raise ValueError('Supplied profile exceeds the declared bound.')
        label = tuple(rounding_index(v, p['h']) for v in values)
        if any(abs(v) > p['J'] for v in label):
            raise ValueError('Quantized label outside codebook.')
        children = tuple(visit(word+(a,), remaining-1) for a in range(p['actions']))
        return Tree(label, children)
    return visit((), p['K'])


def output(tree, p):
    if tree is None:
        return (F(0),)*p['dimension']
    return tuple(p['h']*v for v in tree.label)


def update(tree, action, p):
    if isinstance(action, bool) or not isinstance(action, int) or not 0 <= action < p['actions']:
        raise ValueError('Action outside alphabet.')
    return None if tree is None else tree.children[action]


def certificate(p):
    """The analytic contract, not a black-box verification of native dynamics."""
    return {k: (str(v) if isinstance(v, F) else v) for k, v in p.items()}
