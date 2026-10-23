# BM/GURF — verified parameter freeze DD-2262–DD-2270

17 September 2026. User-proposed register, checked and retained with the qualifications below. This record strengthens the explicit lower-bound construction in the earlier weak-coupling obstruction note. It does not change T01–T55 and does not establish a continuum Yang–Mills mass gap. No external novelty claim is made.

## Native Passport

Four-dimensional hypercubic Wilson SU(2), Haar probability on each oriented link, inverse on a reversed link, one contribution per unoriented elementary plaquette:

\[
 d\mu_\beta\propto\exp\left[\beta\sum_p\tfrac12\operatorname{ReTr}U_p\right]\prod_e dU_e,\qquad\beta\ge0.
\]

Use an interior link with all six plaquettes and 18 distinct neighboring links, without small-period identifications. All raw-link conditioning configurations are permitted; no gauge fixing is imposed. Total variation is \(\sup_A|\mu(A)-\nu(A)|\), not twice this value. Weighted distances below use the link-interaction graph, where any two distinct links sharing a plaquette have distance one.

## DD-2262 — actual raw-link influence

\[
 c_{ef}(\beta)=\sup_{\eta_{-f}=\eta'_{-f}}
 \|\mu_e(\cdot\mid\eta)-\mu_e(\cdot\mid\eta')\|_{\rm TV},
 \qquad c_{ee}=0.
\]

Here \(\eta,\eta'\) specify links other than \(e\). The conditional law is

\[
 d\mu_e(U\mid H)\propto
 \exp[\tfrac\beta2\operatorname{ReTr}(UH)]\,dU,
\]

where each staple is oriented to give this convention. This is the native conditional response being examined.

## DD-2263 — rigorous upper certificate

Changing one shared plaquette changes its contribution to the conditional log density by a function with oscillation at most \(4\beta\). The change-of-density inequality with oscillation \(s\) gives total variation at most \(\tanh(s/4)\). Thus

\[
 c_{ef}\le\tanh(n_{ef}\beta)\le n_{ef}\tanh\beta,
 \qquad \sum_{f\ne e}n_{ef}\le18.
\]

Distinguish the actual coefficient from its bound:

\[
 q_{\rm raw}(\beta):=\sup_e\sum_{f\ne e}c_{ef}(\beta),
 \qquad U(\beta):=18\tanh\beta,
 \qquad q_{\rm raw}\le U.
\]

The integer inequality follows by iterating \(\tanh(x+y)\le\tanh x+\tanh y\) for nonnegative arguments.

## DD-2264 — sufficient threshold and decay

\[
 \beta_{\rm suff}=\operatorname{artanh}(1/18)
 =\tfrac12\log(19/17)=0.05561281755511219\ldots.
\]

For \(0<\beta<\beta_{\rm suff}\), the comparison bound supplies link-graph decay exponent

\[
 \kappa_\beta=-\log U(\beta)>0.
\]

At \(\beta=0\), links are independent and \(\kappa=+\infty\) is only a limiting notation.

| β | U(β), not necessarily the actual row sum | κβ |
|---:|---:|---:|
| 0.01 | 0.179994000240 | 1.714831760648 |
| 0.02 | 0.359952007679 | 1.021784568422 |
| 0.04 | 0.719616245601 | 0.329037201284 |
| 0.05 | 0.899250749242 | 0.106193363221 |

This is a sufficient mixing region, not a phase boundary. The exponent is in link-graph units, not an already established continuum physical mass.

## DD-2265 — weighted upper certificate

Define the weighted **actual raw influence**, for \(\gamma\ge0\), by

\[
 q^{\rm raw}_\gamma:=\sup_e\sum_{f\ne e}e^{\gamma d(e,f)}c_{ef}.
\]

Since only distance-one neighbors contribute,

\[
 q^{\rm raw}_\gamma=e^\gamma q_{\rm raw}
 \le18e^\gamma\tanh\beta.
\]

The exact sufficient threshold for this upper bound is

\[
 \beta_{\rm suff}(\gamma)
 =\operatorname{artanh}(e^{-\gamma}/18).
\]

Use an ordinary \(\le\), not an unspecified \(\lesssim\). This identity depends on the graph metric stated above. Do not identify this actual-influence quantity silently with a separate mixed-oscillation majorant \(Q_\gamma\) used elsewhere in the research notes.

## DD-2266 — explicit cancellation and lower bound

The proposed cancellation is realizable. The six three-link staple paths surrounding an interior link use 18 distinct links; they share vertices but no link variables. Therefore one can prescribe the six staple products independently by setting two links on each path to identity and setting the third appropriately.

For a chosen neighbor \(f\), reserve its staple as the affected path. On the other five paths prescribe

\[
 S_j=\cos(2\pi j/5)I+i\sin(2\pi j/5)\sigma_3,
 \qquad j=0,\ldots,4.
\]

These are SU(2) matrices and \(\sum_jS_j=0\). On the affected path, hold its other two links fixed at identity and change only \(f\) between \(I\) and \(-I\). The central link then sees \(H=+I\) or \(H=-I\), respectively. Orientation reversal preserves this sign change. This construction is available for every neighboring \(f\); the supremum defining each coefficient may use its own conditioning configurations.

Writing \(U=\cos\theta I+i\sin\theta\,\mathbf n\cdot\boldsymbol\sigma\), the two densities are

\[
 q_\beta^\pm(U)=Z(\beta)^{-1}e^{\pm\beta\cos\theta},
 \qquad Z(\beta)=2I_1(\beta)/\beta,\quad Z(0)=1.
\]

Their positive likelihood-difference region is \(\cos\theta>0\). Haar measure gives marginal \((2/\pi)\sin^2\theta\,d\theta\), hence

\[
 \mathcal C(\beta)=\frac{2}{\pi Z(\beta)}
 \int_0^{\pi/2}(e^{\beta\cos\theta}-e^{-\beta\cos\theta})\sin^2\theta\,d\theta,
 \qquad c_{ef}\ge\mathcal C(\beta).
\]

Point conditioning is legitimate for this continuous, everywhere positive finite-temperature specification; nearby configurations approach the same values.

## DD-2267 — monotonicity and asymptotics

Let \(X=\cos\theta\) under Haar measure. Its density is \(2\sqrt{1-x^2}/\pi\) on \([-1,1]\). Then

\[
 \mathcal C(\beta)
 =\frac{\mathbb E\sinh(\beta|X|)}{\mathbb E\cosh(\beta X)}
 =2\mathbb P_\beta(X>0)-1,
\]

where \(\mathbb P_\beta\) tilts Haar measure by \(e^{\beta X}\). Differentiating gives

\[
 \mathcal C'(\beta)=2\operatorname{Cov}_\beta(\mathbf1_{X>0},X)>0.
\]

Strict positivity follows because both half-intervals have positive mass and the conditional mean on the positive half exceeds the conditional mean on the negative half. Thus the inverse used in DD-2269 and DD-2270 is well defined for values in \((0,1)\).

Expansion of the numerator and denominator gives, more precisely,

\[
 \mathcal C(\beta)=\frac4{3\pi}\beta-\frac7{90\pi}\beta^3+O(\beta^5).
\]

For large β, the negative-half numerator is \(2/(\pi\beta)[1+O(\beta^{-2})]\), while \(Z(\beta)=\sqrt{2/\pi}\,e^\beta\beta^{-3/2}[1+O(\beta^{-1})]\). Therefore

\[
 \mathcal C(\beta)=1-2\sqrt{2/\pi}\sqrt\beta\,e^{-\beta}[1+O(\beta^{-1})].
\]

In particular each neighboring coefficient tends to one and the interior row sum tends to 18.

## DD-2268 — checked numerical values

| β | C(β) |
|---:|---:|
| 0.05561 | 0.023597360333 |
| 0.10 | 0.042416577637 |
| 0.50 | 0.209163915201 |
| 1 | 0.401239897675 |
| 2 | 0.693281929281 |
| 4 | 0.939526671526 |
| 8 | 0.998434389966 |
| 16 | 0.999999266985 |

| Target C | Numerical inverse β |
|---:|---:|
| 0.50 | 1.290702524462 |
| 0.90 | 3.412378101142 |
| 0.95 | 4.217952176900 |
| 0.99 | 6.006210301770 |
| 0.999 | 8.476117547705 |

These values were independently recalculated using scaled Bessel normalization and quadrature. Decimal entries are numerical approximations, not exact equalities.

## DD-2269 — obstruction threshold, with certified rounding

\[
 18\mathcal C(\beta)\le q_{\rm raw}(\beta)\le18\tanh\beta.
\]

Define the exact obstruction threshold implicitly:

\[
 \beta_{\rm obs}=\mathcal C^{-1}(1/18).
\]

Then \(\beta\ge\beta_{\rm obs}\) rules out the strict criterion \(q_{\rm raw}<1\). Exact rational series bounds, including a rational enclosure of π, certify

\[
 \boxed{0.131030771115<\beta_{\rm obs}<0.131030771116.}
\]

Consequently **β ≥ 0.131030772 is a safe rounded sufficient failure condition**. The shorter decimal 0.13103077 is slightly below the exact threshold and must not be used as an exact guaranteed cutoff.

The interval \([\beta_{\rm suff},\beta_{\rm obs})\) is undecided by these two certificates. Equality at the upper-certificate threshold does not prove contraction. The actual transition of this particular row-sum criterion need not occur at either endpoint. No assertion of an actual thermodynamic phase transition is made.

The β-obstruction equation belongs to DD-2269; retain DD-2270 for the weighted obstruction rather than duplicating that identifier.

## DD-2270 — weighted obstruction

\[
 q^{\rm raw}_\gamma\ge18e^\gamma\mathcal C(\beta),
 \qquad
 \beta_{\rm obs}(\gamma)=\mathcal C^{-1}(e^{-\gamma}/18).
\]

The weighted strict criterion fails whenever \(\beta\ge\beta_{\rm obs}(\gamma)\).

| γ | βsuff(γ), numerical | βobs(γ), numerical |
|---:|---:|---:|
| 0 | 0.055612817555 | 0.131030771115 |
| 0.02 | 0.054509405245 | 0.128431141304 |
| 0.05 | 0.052895356293 | 0.124628440038 |
| 0.10 | 0.050311151908 | 0.118540013209 |

The inverse formula defines the exact threshold. Except for the separately certified unweighted bracket above, these displayed weighted decimals are quadrature/root-finding approximations.

## Canonical interpretation and next task

Retain \(U<1\) as a **raw-link mixing/contraction certificate**. It does not, on its own, prove exact BM response closure, continuum reconstruction, or a physical spectral gap. Retain \(18\mathcal C\ge1\) as an **obstruction to the specified raw-link Dobrushin criterion**. It is not an obstruction to Yang–Mills dynamics, uniqueness by another method, or a mass gap.

The defensible conclusion is: **this raw-link worst-case total-variation contraction criterion fails at sufficiently weak coupling and cannot by itself supply the desired continuum bridge.** Raw links can still be used in other proof methods. Gauge-invariant coarse variables are one justified next research direction, not the only logically possible approach.

Before assigning \(q_{\rm phys}^{\rm upper}\) or \(q_{\rm phys}^{\rm lower}\), specify the coarse map, exact induced measure, feasible configurations and compatibility constraints, comparison metric, observables, and physical length scale. Gauge invariance alone supplies none of the required contraction inequalities.

The coarse response must also preserve joint observables. For coarse information \(\mathcal G\), the exact repair identity remains

\[
 \operatorname{Cov}(F,G)=
 \operatorname{Cov}(\mathbb E[F\mid\mathcal G],\mathbb E[G\mid\mathcal G])
 +\mathbb E[\operatorname{Cov}(F,G\mid\mathcal G)].
\]

Both retained and omitted terms need adequate control. The replacement uniform continuum estimate remains open in this BM/GURF attempt.

## Appendix — exact threshold certification

The following Python 3 script uses only exact rational arithmetic. It bounds π with Machin's identity and alternating arctangent series. Positive moment-series tails enclose the numerator and denominator of C. This certifies the bracket independently of floating-point quadrature.

```python
from fractions import Fraction as F
from math import factorial

def atan_bounds(x,n):
    s=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(n)),F(0))
    nxt=(-1)**n*x**(2*n+1)/F(2*n+1)
    return min(s,s+nxt),max(s,s+nxt)
a,b=atan_bounds(F(1,5),45);c,d=atan_bounds(F(1,239),15)
pi_lo,pi_hi=16*a-4*d,16*b-4*c

def bounds(beta,K=7):
    # N = E[sinh(beta*abs(X))], D = E[cosh(beta*X)] for Haar SU(2).
    p=sum((F(4**(k+2)*factorial(k)*factorial(k+2),factorial(2*k+4))*beta**(2*k+1)/factorial(2*k+1) for k in range(K+1)),F(0))
    nlo=p/pi_hi
    n_tail=beta**(2*K+3)/factorial(2*K+3)/(1-beta**2/F((2*K+4)*(2*K+5)))
    nhi=p/pi_lo+n_tail
    dlo=sum((beta**(2*k)/F(4**k*factorial(k)*factorial(k+1)) for k in range(K+1)),F(0))
    d_tail=beta**(2*K+2)/F(4**(K+1)*factorial(K+1)*factorial(K+2))/(1-beta**2/F(4*(K+2)*(K+3)))
    dhi=dlo+d_tail
    return nlo/dhi,nhi/dlo
left,right=F('0.131030771115'),F('0.131030771116')
l=bounds(left);r=bounds(right)
assert l[1]<F(1,18)<r[0]
print('Exact rational certification passed: 0.131030771115 < beta_obs < 0.131030771116')
print('Signs relative to 1/18:',float(l[1]-F(1,18)),float(r[0]-F(1,18)))

```
