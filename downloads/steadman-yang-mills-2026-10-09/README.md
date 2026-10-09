# Steadman–Yang–Mills multi-plaquette review bundle

Start with `Steadman_Yang_Mills_Multi_Plaquette_2026-10-09.md`.

The bundle proves and checks finite SU(2) lattice gap bounds on a square,
two-square strip, 2×2 patch and cube. It does not claim a continuum theory,
continuum gap, universal Steadman law, novelty or independent peer review.

Python 3 and NumPy are needed for the multi-plaquette code. The tested NumPy
version is pinned in `requirements.txt`; runtime details are recorded separately.

```bash
python3 -m pip install -r requirements.txt
python3 audit_multi_plaquette.py
```

The audit checks exact rational witnesses, including the auxiliary local
single-square bounds. It does not recalculate eigenvalues in floating point.

To reconstruct the patch and cube matrices using different maximal trees:

```bash
python3 audit_multi_plaquette.py --check-trees
```

To recalculate all spectral bounds using the stored exact matrices:

```bash
python3 multi_plaquette.py --geometry all
```

Supported geometry options are `single`, `strip`, `patch`, `cube`, and `all`.
The default couplings are 0.00348, 0.1, 0.5, 1, 2 and 3. Exact rational strings
can be supplied with `--beta`. For example:

```bash
python3 multi_plaquette.py --geometry cube --beta 1 3
```

This overwrites that geometry's certificate JSON with the requested cases.
Make a working copy before experimenting. To rebuild the original exact
matrices, move the four `*_matrices.json` files into a backup directory and run
the full default calculation again.

The prior single-plaquette work is also included:

- `Steadman_Yang_Mills_Research_2026-10-09.md` is the earlier report.
- `single_plaquette_certificates.py` is its original verification program,
  copied under a descriptive filename. It uses only the Python standard library.
- `certificate_results.json` contains its 12 SU(2)/SU(3) single-plaquette cases.

```bash
python3 single_plaquette_certificates.py
```

The many-plaquette calculation is SU(2) only. SU(3) appears only in the included
earlier single-plaquette calculation.

`audit_results.json` records the completed 24-case audit and exact alternate-tree
matches. Some saved witnesses use conservative outward-rounded rational decimal
endpoints; regenerating them may give slightly tighter bounds in the last digits.
Runtime measurements and corresponding file hashes can also change on rerun.

`SHA256SUMS.txt` records every bundled file except the manifest itself.
