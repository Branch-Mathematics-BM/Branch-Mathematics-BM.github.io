# Branch Mathematics — Jordan returns and certified nonlinear bounds

21 October 2026 · Continuation of the 20 October development

This development completes the long-return calculation for Jordan chains of every length and supplies exact upper and lower certificates for a concrete four-state nonlinear construction. It does **not** assert that the remaining continuous four-state minimax problem is solved. The distinction between a global bound and a bound for one encoder/decoder family is maintained throughout.

The proofs are internally checked mathematical arguments. The finite numerical certificates are verified with exact rational arithmetic. Independent proof review and historical novelty assessment remain separate obligations.

The earlier frozen BM foundation is unchanged. The two imported BM results are BM20-J1–J2 (ordered refinement and mutual-return obstruction) and, for the optional extension from invariant polynomials to all sampled-autonomous polynomials, BM18-J1. Their full proofs are included in the accompanying package.

## Contract and notation

For a positive integer n, let N be the Jordan nilpotent matrix with ones immediately above the diagonal. Thus

\[
 (e^{\tau N}x)_{k+1}
 =\sum_{j=k}^{n-1}\frac{\tau^{j-k}}{(j-k)!}x_{j+1},
 \qquad 0\le k<n.
\]

The dynamics are \(\dot x=\varepsilon Nx\), with \(\varepsilon\ne0\). Exact scalar closure means that a **globally continuous** map \(R:\mathbb R^n\to\mathbb R\) satisfies

\[
 R(e^{\varepsilon hN}x)=F(R(x))\quad(x\in\mathbb R^n)
\]

for a fixed \(h>0\) and a single-valued F on the image of R. F is not initially assumed invertible. The performance set is the Euclidean unit ball of initial states; closure is required on all of \(\mathbb R^n\). The performance set is not asserted to be invariant.

Let \(V_k=\{x:x_{k+1}=\cdots=x_n=0\}\), with \(V_0=\{0\}\). The output trajectory operator on its first k coordinates is

\[
 (\mathcal O_{k,T}z)(t)=\sum_{j=0}^{k-1}
 \frac{(\varepsilon t)^j}{j!}z_{j+1},\qquad 0\le t\le T.
\]

A decoder may return any trajectory in the chosen \(L^p[0,T]\) space unless an explicit restricted decoder is named.

## 1. All long-return endpoint pairs

### BM21-J1. Complete long-return relation for every Jordan chain

Fix any sequence \(\tau_j\) with \(|\tau_j|\to\infty\). A pair (x,y) can occur as

\[
 z_j\longrightarrow x,\qquad e^{\tau_jN}z_j\longrightarrow y
\]

if and only if it has the following form:

| Chain length | Exactly the possible endpoint pairs |
|---|---|
| \(n=2m\) | \(x,y\in V_m\), with their first m coordinates arbitrary and independent. |
| \(n=2m+1\) | \(x=(a,c,0_m)\), \(y=(b,(-1)^m c,0_m)\), where \(a,b\in\mathbb R^m\) and \(c\in\mathbb R\). |

Here \(0_m\) denotes m trailing zeros. The statement holds for either time direction and for every prescribed diverging sequence, including \(\tau_j=2j\varepsilon h\). For n=1 it says x=y, as it should for the identity dynamics.

**Proof.** Associate to a state z the polynomial

\[
 p(s)=\sum_{k=0}^{n-1}z_{k+1}s^k/k!.
\]

Its derivatives at 0 are the state z; its derivatives at \(\tau\) are the state \(e^{\tau N}z\).

First let n=2m. The derivatives of orders 0 through m−1 at 0 and at \(\tau\ne0\) uniquely determine a polynomial of degree at most 2m−1. Indeed, the difference of two such polynomials is divisible by \(s^m(s-\tau)^m\), which has degree 2m. This proves uniqueness; the square linear interpolation system then also has a solution.

Let \(h_{0k},h_{1k}\), \(0\le k<m\), be the corresponding Hermite basis on the fixed interval with endpoints 0 and 1: the kth specified derivative at the named endpoint is one and all other specified derivatives are zero. If the endpoint derivative data are \(u_k,v_k\), the interpolant obeys

\[
 H_\tau(\tau s)=\sum_{k=0}^{m-1}\tau^k
 \bigl(u_k h_{0k}(s)+v_k h_{1k}(s)\bigr).
\]

For bounded data, every endpoint derivative of order r≥m is therefore

\[
 O(|\tau|^{m-1-r})\longrightarrow0.
\]

This proves necessity: any converging states and their converging endpoints have bounded lower derivative data and hence vanishing upper halves. Conversely, choose fixed lower data equal to the desired x and y coordinates and use this interpolant at each \(\tau_j\). Its full derivative vectors converge to the specified endpoints. This proves the even case.

Now let n=2m+1 with m≥1. Construct the same degree-\((2m-1)\) interpolant H for the lower m derivatives at each endpoint. The additional degree of freedom is a multiple of

\[
 q(s)=s^m(s-1)^m,
 \qquad q^{(m)}(0)=(-1)^m m!,\quad q^{(m)}(1)=m!.
\]

If the initial mth derivative is \(u_m\), the unique degree-at-most-2m polynomial is

\[
 p_\tau(t)=H_\tau(t)+
 \frac{u_m-H_\tau^{(m)}(0)}{(-1)^m m!}
 \tau^m q(t/\tau).
\]

Its mth derivative at the other endpoint is

\[
 p_\tau^{(m)}(\tau)
 =H_\tau^{(m)}(\tau)+(-1)^m
 \bigl(u_m-H_\tau^{(m)}(0)\bigr).
\]

Both H derivatives are \(O(1/|\tau|)\). The endpoint mth derivatives consequently tend to c and \((-1)^m c\). All derivatives above order m tend to zero: those of H do, and those of the added term have size \(O(|\tau|^{m-r})\) for r>m. This proves necessity for bounded converging endpoint data, and sufficiency by choosing fixed lower data and \(u_m=c\). The case n=1 follows directly. ∎

This theorem classifies endpoint limits of the **native linear flow**. It does not assert that these pairs exhaust the fibers of every scalar factor.

## 2. What every continuous scalar code must forget

### BM21-J2. Forced scalar identifications and trajectory lower bounds

Under the stated global continuous closure contract:

* For n=2m, R is constant on \(V_m\).
* For n=2m+1, there is a continuous scalar function \(\phi\) such that
  \(R(a,c,0_m)=\phi(c)\). If m is odd, \(\phi(c)=\phi(-c)\).

Consequently define

\[
 k(n)=\left\lfloor\frac n2\right\rfloor
 +\begin{cases}1,&n\equiv3\pmod4,\\0,&\text{otherwise}.\end{cases}
\]

For every \(z\in V_{k(n)}\), \(R(z)=R(-z)\). For any trajectory decoder, any T>0 and any \(1\le p\le\infty\),

\[
 \boxed{E^{\mathrm{closed,cont}}_{p,T}(n,1)
 \ \ge\ \|\mathcal O_{k(n),T}\|_{\ell_2\to L^p}.}
\]

For k=0 the right side is zero. This is a lower bound, not a general equality assertion.

**Proof.** BM20-J1 supplies a continuous refinement q of R and an interval homeomorphism g with \(qU=gq\), where \(U=e^{\varepsilon hN}\); it permits F itself to be noninjective. Its mutual-return consequence BM20-J2 is elementary once that refinement exists: \(g^2\) is increasing. If two limiting q-values lie on opposite sides of a point u, then either \(g^2(u)\ge u\), making the upper half-interval forward invariant, or \(g^2(u)\le u\), making the lower half-interval forward invariant. Thus even forward iterates cannot approach each endpoint from the other.

The relation in BM21-J1 is symmetric. Apply its construction to \(\tau_j=2j\varepsilon h\), first with the endpoints in one order and then reversed. The mutual-return result identifies their q-values and hence their R-values. In the odd case with sign −1, applying the relation twice also proves independence of the first m coordinates at fixed c. This gives the claimed restrictions.

The indicated \(V_{k(n)}\) consists of forced antipodal pairs. Their true trajectories are opposites. If a decoder returns the same w for such a pair, the triangle inequality gives

\[
 \max\{\|\mathcal O_{k,T}z-w\|_p,
          \|-\mathcal O_{k,T}z-w\|_p\}
 \ge\|\mathcal O_{k,T}z\|_p.
\]

Take the supremum over unit z and then the infimum over codes and decoders. ∎

For p=2 the bound is the square root of the largest eigenvalue of the k×k matrix

\[
 G_{ij}=\frac{\varepsilon^{i+j}T^{i+j+1}}{i!j!(i+j+1)},
 \qquad 0\le i,j<k.
\]

For p=∞ the bound is

\[
 \left(\sum_{j=0}^{k-1}\frac{(\varepsilon T)^{2j}}{(j!)^2}\right)^{1/2}.
\]

The latter follows by commuting the two suprema and observing that the squared coefficient-vector norm increases with t≥0. The first chain lengths have \(k(n)=0,1,2,2,2,3,4,4\) for n=1,…,8. The parity distinction is part of the result; a stronger antipodal claim on every odd chain's full middle prefix has not been proved here.

For block-diagonal collections of Jordan chains the endpoint relation is the product of the block relations, using the same iterate counts. The same proof gives a scalar-code lower bound on the direct sum of their forced antipodal subspaces for any linear trajectory task. Different nonzero block couplings change the interpolation times but not the endpoint classification.

In particular, for n=4 and \(\varepsilon=T=1\),

\[
 \boxed{E^2\ge(4+\sqrt{13})/6
 \approx1.267591879244.}
\]

## 3. A substantially stronger certified four-state construction

### BM21-J3. A rational cubic encoder with squared error at most 1.2949

Write the four-state unit chain as

\[
 \dot a=b,\quad\dot b=c,\quad\dot c=d,\quad\dot d=0.
\]

Set

\[
 Q=c^2-2bd,\qquad I=c^3-3bcd+3ad^2,
\]

and choose the scalar encoder

\[
 \boxed{R(x)=\frac{1969d+8757I-7014dQ+159d^3}{10000}.}
\]

Decode it as the entire trajectory

\[
 \boxed{D(z)(t)=(1+t/2)z,\qquad 0\le t\le1.}
\]

Then R is a global polynomial first integral, so its exactly closed update is F=id for every sampling interval. For every initial state of Euclidean norm at most one,

\[
 \boxed{\int_0^1
 \left|a+bt+\frac{ct^2}{2}+\frac{dt^3}{6}-(1+t/2)R(x)\right|^2dt
 \le\frac{12949}{10000}=1.2949.}
\]

**Proof by an exact rational certificate.** Direct differentiation gives \(DQ=DI=Dd=0\), where \(D=b\partial_a+c\partial_b+d\partial_c\). Hence DR=0.

To certify the bound on the whole ball, introduce a fifth real variable e, and write

\[
 \rho=a^2+b^2+c^2+d^2+e^2,
 \quad R_h=\frac{1969d\rho+8757I-7014dQ+159d^3}{10000}.
\]

Let \(x=(a,b,c,d)^T\), let

\[
 G_{ij}=\frac{1}{i!j!(i+j+1)}\quad(0\le i,j\le3),
 \qquad k=(5/4,2/3,11/48,7/120)^T.
\]

Integration gives \(\|Ox\|_2^2=x^TGx\), \(\langle Ox,1+t/2\rangle=k^Tx\), and \(\|1+t/2\|_2^2=19/12\). The homogeneous degree-six polynomial

\[
 P=\frac{12949}{10000}\rho^3-\rho^2 x^TGx
       +2\rho R_h k^Tx-\frac{19}{12}R_h^2
\]

has the exact identity

\[
 P=m(a,b,c,d,e)^T H\,m(a,b,c,d,e),
\]

where m is the vector of all 35 degree-three monomials in five variables, in the order specified in the certificate. The supplied 35×35 rational matrix H has common denominator **630000000000**. The companion verifier checks all 210 degree-six coefficients exactly, computes an exact LDLᵀ factorization with 35 strictly positive pivots, and independently reconstructs H from that factorization. Thus H is positive definite and P≥0 everywhere.

For a state in the unit ball choose \(e=\sqrt{1-\|x\|^2}\). Then \(\rho=1\), \(R_h=R\), and P is precisely the asserted error bound minus the squared error. This proves the claim. No sampled numerical maximum or floating-point eigenvalue is used to accept the certificate. ∎

The exact matrix is in `BM_Jordan_Rational_Certificate_2026-10-21.json`. The standalone verifier uses only the Python standard library.

**Strict comparison with every closed linear scalar code.** A nonzero linear scalar factor must retain d alone: closure makes its kernel invariant, so its defining row is a left eigenvector of the unipotent Jordan update, hence a multiple of the last-coordinate row. At d=0, indistinguishable antipodal states give the squared lower bound \(\lambda_{\max}(G_{0:3,0:3})\), attained by decoding d as \(t^3d/6\). Thus the best such linear code has squared error approximately 1.301498187997. A rational Rayleigh vector (87,47,16) already gives

\[
 \lambda_{\max}\ge\frac{195887}{150510}
 >\frac{12949}{10000}.
\]

The new construction therefore improves squared worst-case error by at least

\[
 \frac{991601}{150510000}\approx0.006588273204
\]

over the optimum of that entire linear class. The previously established linear formula is retained in its linear scope; it is not substituted for the unrestricted nonlinear optimum.

Together, BM21-J2–J3 now certify the global continuous four-state interval

\[
 \boxed{\sqrt{\frac{4+\sqrt{13}}6}
 \ \le E^{\mathrm{closed,cont}}_{2,1}(4,1)
 \ \le\frac{\sqrt{12949}}{100}.}
\]

Numerically this is **1.1258738292 ≤ E ≤ 1.1379367294**. The endpoints are bounds; the exact value inside this interval has not been established.

## 4. How much remains possible within this cubic family?

### BM21-J4. A certified 0.0001 bracket for cubic invariant codes with the fixed decoder

Keep the decoder \(D(z)(t)=(1+t/2)z\), but allow **every invariant scalar polynomial of total degree at most three**, with arbitrary real coefficients. Let \(E_{\le3,v}\) be the resulting best worst-case error on the same unit ball. Then

\[
 \boxed{1.2948\le E_{\le3,v}^2\le1.2949.}
\]

BM18-J1 also makes this the bracket for every globally sampled-autonomous scalar polynomial of that degree with this decoder: such a polynomial is necessarily a first integral. This conclusion does not extend the fixed decoder restriction to arbitrary decoders.

**Proof.** The task is odd in x, and the ball is symmetric. Given an invariant polynomial R, its odd part \(R_o(x)=(R(x)-R(-x))/2\) is also invariant and has no larger worst-case error. Its residual at x is the average of the residual of R at x and the negative residual of R at −x, so this follows from convexity of the norm.

The odd invariant polynomials of degree at most three are exactly

\[
 R_o=\alpha d+\beta I+\gamma dQ+\delta d^3.
\]

For completeness, the degree-one kernel of D is spanned by d. Comparing coefficients of a general homogeneous cubic in \(DP=0\) eliminates the monomials involving \(a^3,a^2b,a^2c,a^2d,ab^2,abc,abd,ac^2,acd,b^3,b^2c,b^2d,bc^2,cd^2\); the remaining coefficients satisfy

\[
 [ad^2]=3[c^3],\quad[bcd]=-3[c^3],\quad[bd^2]=-2[c^2d].
\]

Thus the cubic kernel has the three independent basis elements I, dQ and d³. Degree components do not mix under D.

On d=0, the encoder is simply \(\beta c^3\). Take the two exact rational unit-sphere states and positive rational weights in `BM_Jordan_Cubic_Family_Lower_Certificate_2026-10-21.json`. For orientation, their first three coordinates and weights are approximately

| State | a | b | c | Weight |
|---|---:|---:|---:|---:|
| 1 | 0.8737739 | 0.4711565 | 0.1205436 | 0.99773646 |
| 2 | 0.3520258 | 0.1775054 | −0.9190047 | 0.00226354 |

Both have d=0. The printed decimals are explanatory only; the certificate contains the exact rational coordinates, whose squared norms are exactly one, and exact weights summing to one.

With \(v=1+t/2\), form the weighted squared error

\[
 \sum_i w_i\|Ox_i-\beta c_i^3 v\|_2^2
 =A\beta^2-2B\beta+C,
\]

where

\[
 A=\frac{19}{12}\sum_iw_i c_i^6>0,\quad
 B=\sum_iw_i c_i^3 k^Tx_i,\quad
 C=\sum_iw_i x_i^TGx_i.
\]

Its minimum is the exact rational number \(C-B^2/A\). The verifier checks

\[
 C-B^2/A>\frac{3237}{2500}=1.2948.
\]

The numerical value is approximately 1.29480030513. A worst-case error is at least this weighted average for every β. For a polynomial with an even part, symmetrization justifies the reduction above; equivalently use each certificate state and its antipode with half its weight. This proves the lower bound for the whole stated family. BM21-J3 proves the upper bound. ∎

This is a bracket, not an exact symbolic optimum. It establishes that changing coefficients within this cubic family and keeping this decoder can improve the certified squared-error ceiling by **less than 0.0001**. A larger improvement requires changing the family, the decoder, or both. It does not obstruct a better general continuous scalar code.

## 5. Executed verification and remaining boundary

The certificate verifier accepted the exact polynomial identity, all 35 positive LDL pivots and their reconstruction, the invariant identities, the rational comparison with the linear optimum, and the two-state lower certificate. Its acceptance path uses rational arithmetic only. It also rejects deliberately changed matrix and weight certificates.

`BM_Jordan_Return_Bridge_2026-10-21.py` supplies the exact rational Hermite construction. Its included checks cover n=1 through n=12, both time signs and several endpoint choices, and verify the complete Jordan flow identity, exactly prescribed endpoint derivatives, and the integer-power decay of the undesignated derivatives. These finite checks support the implementation; the all-n statement is proved above, not inferred from examples.

The updated working audit adds four scoped theorem records without reclassifying the broad open Jordan row as solved. The other frameworks' classifications, physical gates, independent-review gate and frozen foundation remain unchanged.

The remaining Jordan research obligation is precise: determine the unrestricted continuous n=4 scalar optimum inside the displayed interval, and the other unsolved interior encoder dimensions. The results here do not supply those missing proofs. They do supply a complete native long-return calculation, general continuous lower bounds, an explicit strictly better nonlinear code, and exact certificates identifying how close that code is to the best one in its stated cubic family.

## Included dependencies

* `BM_Continuous_Closure_and_Completion_2026-10-20.md`, BM20-J1–J2: ordered refinement of a continuous scalar factor and the mutual even-return obstruction; full proofs and primary topology references.
* `BM_Completion_Development_2026-10-18.md`, BM18-J1: sampled scalar polynomial factors of unipotent maps are first integrals.

These dependencies are included as dated source snapshots in the combined package. New claims are attributed to the proofs and certificates above; no external paper is cited as proving them.
