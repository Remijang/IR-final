# 10.2 Convergence Tests: Positive Series

This is the third time we ha ve stopped the calculations to deal with the definitions. Chapter 2 said what a derivative is. Chapter 5 said what an integral is. Now we say what the sum of a series is—if it exists. In all three cases a limit is involved. That is the formal, careful, cautious part of mathematics, which decides if the active and progressive parts make sense.

The series 21 C 41 C ${ \frac { 1 } { 2 } } + { \frac { 1 } { 4 } } + { \frac { 1 } { 8 } } + \cdots$ converges to 1. The series $1 + { \frac { 1 } { 2 } } + { \frac { 1 } { 3 } } + \cdots$ diverges to infinity. The series 1 21 C 13 converges to $\ln 2$ . When we speak about convergence or divergence of a series, we are really speaking about convergence or divergence of its “partial sums.”

DEFINITION 1 The partial sum $s _ { n }$ of the series $a _ { 1 } + a _ { 2 } + a _ { 3 } + \cdots$ stops at $a _ { n }$

$$
s _ { n } = s u m \ o f t h e f t r s t \ n \ t e r m s \ = a _ { 1 } + a _ { 2 } + \cdots + a _ { n } .
$$

Thus $s _ { n }$ is part of the total sum. The example ${ \frac { 1 } { 2 } } + { \frac { 1 } { 4 } } + { \frac { 1 } { 8 } } + \cdots$ has partial sums

$$
s _ { 1 } = { \frac { 1 } { 2 } } \qquad s _ { 2 } = { \frac { 3 } { 4 } } \qquad s _ { 3 } = { \frac { 7 } { 8 } } \qquad s _ { n } = 1 - { \frac { 1 } { 2 ^ { n } } } .
$$

Those add up larger and larger parts of the series—what is the sum of the whole series ? The answer is: The series ${ \frac { 1 } { 2 } } + { \frac { 1 } { 4 } } + \ldots$ converges to 1 because its partial sums $s _ { n }$ converge to 1. The series $a _ { 1 } + a _ { 2 } + a _ { 3 } + \ldots$ converges to $s$ when its partial sums—going further and further out—approach this limit $s$ . Add the $a$ ’s, not the $s$ ’s.

DEFINITION 2 The sum of a series is the limit of its partial sums $s _ { n }$ .

We repeat: if the limit exists. The numbers $s _ { n }$ may have no limit. When the partial sums jump around, the whole series has no sum. Then the series does not converge. When the partial sums approach $s$ , the distant terms $a _ { n }$ are approaching zero. More than that, the sum of distant terms is approaching zero.

The new idea . $\textstyle \sum a _ { n } = s )$ / has been converted to the old idea $( s _ { n } \to s )$ /.

EXAMPLE 1 The geometric series $\textstyle { \frac { 1 } { 1 0 } } + { \frac { 1 } { 1 0 0 } } + { \frac { 1 } { 1 0 0 0 } } + \cdots$ converges to $\begin{array} { r } { s = \frac { 1 } { 9 } } \end{array}$

The partial sums $s _ { 1 } , s _ { 2 } , s _ { 3 } , s _ { 4 }$ areÑ:1; :11; :111; :1111. They are approaching $\begin{array} { r } { s = \frac { 1 } { 9 } } \end{array}$ . Note again the differÑence between the series of $a$ ’s and the sequence of $s ^ { \prime } \mathrm { s }$ . TheÑseries $1 + 1 + 1 + \cdots$ diverges because the sequence of $s$ ’s is 1; 2; 3; : : : : A sharper example is the harmonic series: $1 + { \frac { 1 } { 2 } } + { \frac { 1 } { 3 } } + \cdots$ diverges because its partial sums $1 , 1 { \frac { 1 } { 2 } } , \ldots$ eventually go past every numberÑ $s$ : We saw that in 2:6 and will see it again here.

Do not confuse ${ a _ { n } } \to 0$ with $s _ { n } \to s$ : You cannot be sure that a series converges, just on the basis that ${ a _ { n } } \to 0$ : The harmonic series is the best example: $a _ { n } = 1 / n \to 0$ but still $s _ { n } \to \infty$ : This makes infinite series into a delicate game, which mathematicians enjoy. The line between divergence and convergence is hard to find and easy to cross. A slight push will speed up ${ a _ { n } } \to 0$ and make the $s _ { n }$ converge. Even though ${ a _ { n } } \to 0$ does not by itself guarantee convergence, it is the first requirement:

10A If a series converges . $( s _ { n } \to s )$ then its terms must approach zero $( a _ { n } \to 0 )$ :

Proof Suppose $s _ { n }$ approaches $s$ (as required by convergence). Then also $s _ { n - 1 }$ approaches $s$ , and the difference $s _ { n } - s _ { n - 1 }$ approaches zero. That difference is $\scriptstyle a _ { n }$ : So ${ a _ { n } } \to 0$ :

EXAMPLE 1 (continued) For the geometric series $1 + x + x ^ { 2 } + \cdots$ , the test $a _ { n } $ 0 is the same as $x ^ { n } \to 0$ : The  test is failed if $\left| x \right| \geqslant 1$ , beÑcause the powers of $x$ don’t go to zero. Automatically the series diverges. The test is passed if $- 1 < x < 1$ : But to prove convergence, we cannot rely on ${ a _ { n } } \to 0$ . It is the partial sums that must converge:

$$
s _ { n } = 1 + x + \cdots + x ^ { n - 1 } = { \frac { 1 - x ^ { n } } { 1 - x } } \quad { \mathrm { a n d } } \quad s _ { n } \to { \frac { 1 } { 1 - x } } . \quad { \mathrm { T h i s ~ i s ~ } } s .
$$

|For  other se|rie|s, first check that ${ a _ { n } } \to 0$ (otherwise there is no chance of convergence). The $a _ { n }$ will not have the special form $x ^ { n }$ —so we need sharper tests.

The geometric series stays in our mind for this reason. Many convergence tests are comparisons with that series. The right comparison gives enough information: If $\textstyle \left| a _ { 1 } \right| < { \frac { 1 } { 2 } }$ and $\left| a _ { 2 } \right| < \frac { 1 } { 4 }$ and : : : ; then $a _ { 1 } + a _ { 2 } + \ldots$ converges faster than ${ \frac { 1 } { 2 } } + { \frac { 1 } { 4 } } + \ldots$ More generally, the terms in $a _ { 1 } + a _ { 2 } + a _ { 3 } + \ldots$ may be smaller than $a x + a x ^ { 2 } +$ $a x ^ { 3 } + \ldots$ Provided $x < 1$ , the second series converges. Then $\sum a _ { n }$ also converges. We move now to convergence by comparison or divergence bPy comparison.

Throughout the rest of this section, all numbers $a _ { n }$ are assumed positive.

# COMPARISON TEST AND INTEGRAL TEST

In practice it is rare to compute the partial sums $s _ { n } = a _ { 1 } + \cdots + a _ { n } .$ : Usually a simple formula can’t be found. We may never know the exact limit $s$ : But it is still possible to decide convergence—whether there is a sum—by comparison with another series that is known to converge.

10B (Comparison test) Suppose that $0 \leqslant a _ { n } \leqslant b _ { n }$ and $\sum b _ { n }$ converges. Then $\sum a _ { n }$ converges.

The smaller terms $a _ { n }$ add to a smaller sum: $\sum a _ { n }$ is below $\sum b _ { n }$ and must converge. On  the other hand suppose $a _ { n } \geqslant c _ { n }$ an dP $\sum c _ { n } = \infty$ : TPhis comparison forces $\sum a _ { n } = \infty$ : A series diverges if it is above  nPother divergent series.

Note that a series of positive terms can only diverge “to infinity.” It cannot oscillate, because each term moves it forward. Either the $s _ { n }$ creep up on $s$ , passing every number below it, or they pass all numbers and diverge. If an increasing sequence $s _ { n }$ is bounded above, it must converge. The line of real numbers is complete, and has no holes.

The harmonic series $1 + { \textstyle \frac { 1 } { 2 } } + { \textstyle \frac { 1 } { 3 } } + { \textstyle \frac { 1 } { 4 } } + \dots$ diverges to infinity.   
A comparison series is 1 C 1 C 1 C 1 C 1 C 1 $1 + { \textstyle \frac { 1 } { 2 } } + { \textstyle \frac { 1 } { 4 } } + { \textstyle \frac { 1 } { 4 } } + { \textstyle \frac { 1 } { 8 } } + { \textstyle \frac { 1 } { 8 } } + { \textstyle \frac { 1 } { 8 } } + { \textstyle \frac { 1 } { 8 } } + \dots .$ The harmonic series   
is larger. But this compariso2n se4ries 4is re8ally $1 + { \textstyle \frac { 1 } { 2 } } + { \textstyle \frac { 1 } { 2 } } + { \textstyle \frac { 1 } { 2 } } + \ldots$ 18 18 because $\textstyle { \frac { 1 } { 2 } } = { \frac { 2 } { 4 } } =$   
$\frac { 4 } { 8 }$ $i t$

The comparison series diverges. The harmonic series, above , must also diverge.

To apply the comparison test, we need something to compare with. In Example 2, we thought of another series. It was convenient because of those $\frac { 1 } { 2 }$ ’s. But a different series will need a different comparison, and where will it come from ? There is an automatic way to think of a comparison series. It comes from the integral test.

Allow me to apply the integral test to the same example. To understand the integral test, look at the areas in Figure 10.2. The test compares rectangles with curved areas.

EXAMPLE 2 (again) Compare $1 + { \frac { 1 } { 2 } } + { \frac { 1 } { 3 } } + \ldots$ : with the area under the curve $y = 1 / x$ . Every term $a _ { n } = 1 / n$ is the area of a rectangle. We are comparing it with a curved area $c _ { n }$ : Both areas are between $x = n$ and $x = n + 1$ , and the rectangle is above the curve. So $a _ { n } > c _ { n }$ :

$$
\mathrm { \ r e c t a n g u l a r { a r e a } } a _ { n } = { \frac { 1 } { n } } \quad \mathrm { e x c e e d s { c u r v e d } } \mathrm { a r e a } c _ { n } = \int _ { n } ^ { n + 1 } { \frac { d x } { x } } .
$$

Here is the point. Those $c _ { n }$ ’s look complicated, but we can add them up. The sum $c _ { 1 } + . . . + c _ { n }$ is the whole area, from 1 to $n + 1$ : It equals $\ln ( n + 1 )$ —we know the integral of $1 / x$ : We also know that the logarithm goes to infinity.

The rectangular area $1 + 1 / 2 + . . . + 1 / n$ is above the curved area. By comparison of areas, the harmonic series diverges to infinity—a little faster than $\ln ( n + 1 )$ :

Remark The integral of $1 / x$ has another advantage over the series with $\frac { 1 } { 2 }$ ’s. First, the integral test was automatic. From $1 / n$ in the series, we went to $1 / x$ in the integral. Second, the comparison is closer. Instead of adding only $\frac { 1 } { 2 }$ when the number of terms is doubled, the true partial sums grow like ln» $n$ : To prove that, put rectangles under the curve.

Rectangles below the curve give an area below the integral. Figure $1 0 . 2 \mathrm { b }$ omits the first rectangle, to get under the curve. Then we have the opposite to the first comparison—the sum is now smaller than the integral:

$$
{ \frac { 1 } { 2 } } + { \frac { 1 } { 3 } } + \cdots + { \frac { 1 } { n } } < \int _ { 1 } ^ { n } { \frac { d x } { x } } = \ln n .
$$

Adding 1 to both sides, $s _ { n }$ is below $1 + \ln n$ . From the previous test, $s _ { n }$ is above $\ln ( n + 1 )$ . That is a narrow space—we have an excellent estimate of $s _ { n }$ : The sum of $1 / n$ and the integral of $1 / x$ diverge together. Problem 43 will show that the difference between $s _ { n }$ and ln $n$ approaches “Euler’s constant,” which is $\gamma = . 5 7 7 \dots$

Main point: Rectangular area is $s _ { n }$ : Curved area is close. W e are using integrals to help with sums (it used to be the opposite).

Question If a computer adds a million terms every second for a million years, how large is the partial sum of the harmonic series ?

Answer The number of terms is $n = 6 0 ^ { 2 } \cdot 2 4 \cdot 3 6 5 \cdot 1 0 ^ { 1 2 } < 3 . 2 \cdot 1 0 ^ { 1 9 }$ : Therefore $\ln n$ is less than ln $3 . 2 + 1 9 \ln 1 0 < 4 5$ : By the integral test $s _ { n } < 1 + \ln n$ ; the partial sum after a million years has not reached 46:

For other series, $1 / x$ changes to a different function $y ( x )$ : At $x = n$ this function must equal $a _ { n }$ : Also $y ( x )$ must be decreasing. Then a rectangle of height $a _ { n }$ is above the graph to the right of $x = n$ , and below the graph to the left of $x = n$ : The series and the integral box each other in: left sum $\geqslant$ integral $\geqslant$ right sum. The reasoning is the same as it was for $a _ { n } = 1 / n$ and $y ( x ) = 1 / x$ : There is finite area in the rectangles when there is finite area under the curve.

When we can’t add the $a$ ’s, we integrate $y ( x )$ and compare areas:

10C (Integral test) If $y ( x )$ is decreasing and $y ( n )$ agrees with $a _ { n }$ , then 8 a1 Ca2 Ca3 C and y.x/ dx bot8h converg»e 8or both diverge: 1

EXAMPLE 3 The “ $p$ -serie ${ \frac { 1 } { 2 ^ { p } } } + { \frac { 1 } { 3 ^ { p } } } + { \frac { 1 } { 4 ^ { p } } } + \cdots$ converges if $p > 1 .$ Integrate $y = \frac { 1 } { x ^ { p } }$

$$
{ \frac { 1 } { n ^ { p } } } < \int _ { n - 1 } ^ { n } { \frac { d x } { x ^ { p } } } \quad { \mathrm { s o ~ b y ~ a d d i t i o n } } \quad \sum _ { n = 2 } ^ { \infty } { \frac { 1 } { n ^ { p } } } < \int _ { 1 } ^ { \infty } { \frac { d x } { x ^ { p } } } .
$$

In Figure $1 0 . 2 \mathrm { c }$ , the area is finite if $p > 1$ : The integral equals $\left[ x ^ { 1 - p } / ( 1 - p ) \right] _ { 1 } ^ { \infty }$ which is $1 / ( p - 1 )$ : Finite area means convergent seri?es. If $1 / \bar { 1 } ^ { p }$ is the first term, add 1 to the c?urved area:

$$
{ \frac { 1 } { 1 ^ { p } } } + { \frac { 1 } { 2 ^ { p } } } + { \frac { 1 } { 3 ^ { p } } } + \cdots < 1 + { \frac { 1 } { p - 1 } } = { \frac { p } { p - 1 } } .
$$

The borderline case $p = 1$ is the harmonic series (divergent). By the comparison test, every $p < 1$ also produces divergence. Thus $\Sigma { 1 } / { \sqrt { n } }$ diverges by comparison with $\int d x / { \sqrt { x } }$ (and also by comparison with $\Sigma 1 / n$ ). Section 7.5 on improper integrals runs parallel to this section on “improper sums” (infinite series).

Notice the special cases $p = 2$ and $p = 3$ : The series $1 + { \frac { 1 } { 4 } } + { \frac { 1 } { 9 } } + \cdots$ converges. Euler found $\pi ^ { 2 } / 6$ as its sum. The series $1 + { \frac { 1 } { 8 } } + { \frac { 1 } { 2 7 } } + \cdots$ also converges. That is proved by comparing $\Sigma { 1 / n ^ { 3 } }$ with $\Sigma { 1 / n ^ { 2 } }$ or with $\int d x / x ^ { 3 }$ : But the sum for $p = 3$ is unknown.

Extra credit problem The sum of the $p$ -series leads to the most important problem in pure mathematics. The “zeta function” is $Z ( p ) = \Sigma { 1 } / n ^ { p }$ , so $Z ( 2 ) = \pi ^ { 2 } / 6$ and $Z ( 3 )$ is unknown. Riemann studied the complex numbers $p$ where $Z ( p ) = 0$ (there are infinitely many). He conjectured that thereal part of those $p$ is always $\frac { 1 } { 2 }$ . That has been tested for the first billion zeros, but never proved.

# COMPARISON WITH THE GEOMETRIC SERIES

We can compare any new series $a _ { 1 } + a _ { 2 } + \cdots$ with $1 + x + \cdots$ : Remember that the first million terms have nothing to do with convergence. It is further out, as $n \to \infty$ , that the comparison stands or falls. We still assume that $a _ { n } > 0$ :

10D (Ratio test) If $a _ { n + 1 } / a _ { n }$ approache¡s a limit $L < 1$ , the series converges.   
10E (Root test) If the $n$ th root $( a _ { n } ) ^ { 1 / n }$ approaches $L < 1$ , the series converges.

Roughly speaking, these tests make $a _ { n }$ comparable with $L ^ { n }$ —therefore convergent. The tests also establish divergence if $L > 1$ : They give no decision when $L = 1$ : Unfortunately $L = 1$ is the most important and the hardest case.

# 10 Infinite Series

On the other hand, you will now see that the ratio test is fairly easy.

EXAMPLE 4 The geometric series $x + x ^ { 2 } + \cdots$ has ratio exactly $x$ : The $n$ th root is alsoÑex8actly $x$ : So $L = x$ : There is convergence if $x < 1$ (known) and divergence if $x > 1$ (also known). The divergence of $1 + 1 + \cdots$ is too delicate (!) for the ratio test and root test, because $L = 1$ :

EXAMPLE 5 The $p$ -series has $a _ { n } = 1 / n ^ { p }$ and $a _ { n + 1 } / a _ { n } = n ^ { p } / ( n + 1 ) ^ { p }$ : The limit as $n \to \infty$ is $L = 1$ , for every $p$ : The ratio test does not feel the difference between $p = 2$ (convergence) and $p = 1$ (divergence) or even $p = - 1$ (extreme divergence). Neither does the root test. So the integral test is sharper.

EXA|M |PL E 6 A combination of $p$ -series and geometric series can now be decided:

$$
{ \frac { x } { 1 ^ { p } } } + { \frac { x ^ { 2 } } { 2 ^ { p } } } + \cdots + { \frac { x ^ { n } } { n ^ { p } } } + \cdots \operatorname { h a s } \operatorname { r a t i o } { \frac { a _ { n + 1 } } { a _ { n } } } = { \frac { x ^ { n + 1 } } { ( n + 1 ) ^ { p } } } { \frac { n ^ { p } } { x ^ { n } } } \operatorname { a p p r o a c h i n g } L = x .
$$

It is $\left| x \right| < 1$ that decides convergence, not $p$ . The powers $x ^ { n }$ are stronger than any $n ^ { p }$ . The factorials $n$ ! will now prove stronger than any $x ^ { n }$ :

EXAMPLE 7 The exponential series $e ^ { x } = 1 + x + { \textstyle { \frac { 1 } { 2 } } } x ^ { 2 } + { \textstyle { \frac { 1 } { 6 } } } x ^ { 3 } + \cdots$ converges for all $x$ :

The terms of this series are $x ^ { n } / n !$ ! The ratio between neighboring terms is

$$
{ \frac { x ^ { n + 1 } / ( n + 1 ) ! } { x ^ { n } / n ! } } { = } { \frac { x } { n + 1 } } , { \mathrm { w h i c h ~ a p p r o a c h e s ~ } } L = 0 { \mathrm { ~ a s ~ } } n \to \infty .
$$

With $x = 1$ , this ratio test gives convergence of $\textstyle \sum 1 / n !$ The s um is $e$ . With $x = 4$ , the larger series $\sum 4 ^ { n } / n !$ also converges. We knoPw this sum too—it is $e ^ { 4 }$ : Also the sum of $x ^ { n } n ^ { p } / n !$ Pconverges for any $x$ and $p$ : Again $L = 0$ —the ratio test is not even close. The factorials take over; and give convergence.

Here is the proof of convergence when the ratios approach $L < 1$ . Choose $x$ halfway from $L$ to 1: Then $x < 1$ : Eventually the ratios go below $x$ and stay below:

$$
a _ { N + 1 } / a _ { N } < x \qquad a _ { N + 2 } / a _ { N + 1 } < x \qquad a _ { N + 3 } / a _ { N + 2 } < x \quad \cdots
$$

Mu ltiply the first two inequalities. Then multiply all three:

$$
a _ { N + 1 } / a _ { N } < x \qquad a _ { N + 2 } / a _ { N } < x ^ { 2 } \qquad a _ { N + 3 } / a _ { N } < x ^ { 3 } \quad \dots
$$

Therefore $a _ { N + 1 } + a _ { N + 2 } + a _ { N + 3 } + \cdots$ is less than $a _ { N } ( x + x ^ { 2 } + x ^ { 3 } + \cdots )$ : Since $x < 1$ ; comparison with the geometric series gives convergence.

EXAMPLE 8 The series $\sum 1 / n ^ { n }$ is ideal for the root test. The $n$ th root is $1 / n$ : Its limit is $L = 0$ : ConvergencePis even faster than for $e = \sum 1 / n !$ The root test is easily explained, since $( a _ { n } ) ^ { 1 / n } < x$ yields $a _ { n } < x ^ { n }$ and $x$ is cloPse to $L < 1$ : So we compare with the geometric series.

# SUMMARY FOR POSITIVE SERIES

The convergence of geometric series and $p$ -series and exponential series is settled.   
I will put these $a _ { n }$ ’s in a line, going from most divergent to most convergent.

The crossover to convergence is after $1 / n$ :

You should know that this crossover is not as sharp as it looks. On the convergent side, $1 / n ( \ln n ) ^ { 2 }$ comes before all those $p$ -series. On the divergent side, $1 / n ( \ln n )$ and $1 / n ( \ln n ) ( \ln \ln n )$ belong after $1 / n$ : For any divergent (or convergent) series, there is another that diverges (or converges) more slowly.

Thus there is no hope of an ultimate all-purpose comparison test. But comparison is the best method available. Every series in that line can be compared with its neighbors, and o ther series can be placed in between. It is a topic that is understood best by examples.

EXAMPLE 9 $\sum \frac { 1 } { \ln n }$ diverges because $\sum { \frac { 1 } { n } }$ diverges. The comparison uses ln $n < n$ :

$$
\sum { \frac { 1 } { n ( \ln n ) ^ { 2 } } } \approx \int { \frac { d x } { x ( \ln x ) ^ { 2 } } } < \infty \quad \sum { \frac { 1 } { n ( \ln n ) } } \approx \int { \frac { d x } { x ( \ln x ) } } = \infty .
$$

The indefinite integrals are $- 1 / \ln x$ and $\ln ( \ln x )$ : The first goes to zero as $x \to \infty$ ; the integral and series b oth converge. The second inte gral $\ln ( \ln x )$ goesto infinity— very slowly but it gets there. So the second series diverges. These examples squeeze new series into the line, closer to the crossover.

$$
{ \frac { 1 } { n ^ { 2 } + 1 } } < { \frac { 1 } { n ^ { 2 } } } { \mathrm { ~ s o ~ } } { \frac { 1 } { 2 } } + { \frac { 1 } { 5 } } + { \frac { 1 } { 1 0 } } + \cdots < { \frac { 1 } { 1 } } + { \frac { 1 } { 4 } } + { \frac { 1 } { 9 } } + \cdots { \mathrm { ~ } } ( c o n v e r g e n c e ) .
$$

The constant 1 in this denominator has no effect—and again in the next example.

$$
{ \frac { 1 } { 2 n - 1 } } > { \frac { 1 } { 2 n } } \ \mathrm { ~ s o ~ } \ { \frac { 1 } { 1 } } + { \frac { 1 } { 3 } } + { \frac { 1 } { 5 } } + \cdots > { \frac { 1 } { 2 } } + { \frac { 1 } { 4 } } + { \frac { 1 } { 6 } } + \cdots .
$$

$\sum 1 / 2 n$ is $1 / 2$ times $\textstyle \sum 1 / n$ , so both series diverge. Two series behave in the same wPay if the ratios $a _ { n } / b _ { n }$ approach $L > 0$ . Examples $1 1 - 1 2$ have $n ^ { 2 } / ( n ^ { 2 } + 1 ) \to 1$ and $2 n / ( 2 n - 1 ) \to 1$ : That leads to our final test:

10F (Limit comparison test) If the ratio $a _ { n } / b _ { n }$ approaches a positive limit $L$ , th¡en $\sum a _ { n }$ and $\sum b _ { n }$ either both diverge or both converge.

Reason: $a _ { n }$ is smaller than $2 L b _ { n }$ , and larger than ${ \frac { 1 } { 2 } } L b _ { n }$ , at least when $n$ is large. So the two series behave in the same way. For example $\sum \sin \left( 7 / n ^ { p } \right)$ converges for $p > 1$ , not for $p \leqslant 1$ : It behaves like $\sum 1 / n ^ { p }$ (here $L = 7$ ). The tail end of a series (large $n$ ) controls convergence. The froPnt end (small $n$ ) controls most of the sum.

There are many more series to be investigated by comparison.