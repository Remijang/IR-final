# 7.5 Improper Integrals

“Improper” means that some part of $\textstyle \int _ { a } ^ { b } y ( x ) d x$ becomes infinite. It might be $b$ or $a$ or the function $y$ : The region under the graph reach8es infinitely far8—to the right or left or up or down. (Those come from $b = \infty$ and $a = - \infty$ and $y  \infty$ and $y  - \infty .$ ) Nevertheless the integral may “converge.” Just because the region is infinite, it is not automatic that the area is infinite. That is the point of this section—to?decide when improper integrals have proper answers.

The first examples show finite area when $b = \infty$ ; then $a = - \infty$ ; then $y = 1 / \sqrt { x }$ at $x = 0$ : The areas in Figure 7.6 are 1; 1; 2:

$$
\int _ { 1 } ^ { \infty } { \frac { d x } { x ^ { 2 } } } = - { \frac { 1 } { x } } \int _ { 1 } ^ { \infty } = 1 \quad \int _ { - \infty } ^ { 0 } e ^ { x } d x = e ^ { x } \int _ { - \infty } ^ { 0 } = 1 \quad \int _ { 0 } ^ { 1 } { \frac { d x } { \sqrt { x } } } = 2 { \sqrt { x } } \bigg ] _ { 0 } ^ { 1 } = 2 .
$$

In practice we substitute the dangerous limits and watch what happens. When the integral is $- 1 / x$ ; substituting $b = \infty$ gives “ $- 1 / \infty = 0$ :” When the integral is $e ^ { x }$ ; substituting» $a = - \infty$ gives $\mathbf { \partial } ^ { \cdot } e ^ { - \infty } = 0$ :” I think t»hat is fair, and I know i»t is successful. But it is not completely precise.

The strict rules involve a limiÑt.8Calculus sneaks up8on $1 / \infty$ and $e ^ { - \infty }$ just as it sneaks up on $0 / 0$ : Instead of swallowing an infinite region all at once, the formal definitions push out to the limit:

$$
\int _ { a } ^ { \infty } y ( x ) d x = \operatorname* { l i m } _ { b \to \infty } \int _ { a } ^ { b } y ( x ) d x \qquad \int _ { - \infty } ^ { b } y ( x ) d x = \operatorname* { l i m } _ { a \to - \infty } \int _ { a } ^ { b } y ( x ) d x .
$$

The conclusion is the same. The first examples»c8onverged to 1; 1;82: Now come two more examples going out to $b = \infty$ :

$$
\begin{array} { l } { \displaystyle \mathrm { T h e ~ a r e a ~ u n d e r ~ } 1 / x \mathrm { ~ i s ~ } i n f u n i t e \cdot \int _ { 1 } ^ { \infty } \frac { d x } { x } = \ln { x } \bigg ] _ { 1 } ^ { \infty } = \infty } \\ { \displaystyle \mathrm { T h e ~ a r e a ~ u n d e r ~ } 1 / x ^ { p } \mathrm { ~ i s ~ } f u n i t e \mathrm { ~ i f ~ } p > 1 : \int _ { 1 } ^ { \infty } \frac { d x } { x ^ { p } } = \frac { x ^ { 1 - p } } { 1 - p } \bigg ] _ { 1 } ^ { \infty } = \frac { 1 } { p - 1 } . } \end{array}
$$

The area under $1 / x$ is like $1 + { \textstyle \frac { 1 } { 2 } } + { \textstyle \frac { 1 } { 3 } } + { \textstyle \frac { 1 } { 4 } } + \cdots$ , which is also infinite. In fact the sum approximates the integral—the curved area is close to the rectangular area. They go together (slowly to infinity).

A larger $p$ brings the graph more quickly to zero. Figure $7 . 7 \mathrm { a }$ shows a finite area $1 / ( p - 1 ) = 1 0 0$ : The region is still infinite, but we can cover it with strips cut out of a square! The borderline for finite area is $p = 1 . \mathrm { ~ I ~ }$ call it the borderline, but $p = 1$ is strictly on the side of divergence.

The borderline is also $p = 1$ when the function climbs the $y$ axis. A t $x = 0$ ; the graph of $y = 1 / x ^ { p }$ goes to infinity. For $p = 1$ ; the area under $1 / x$ is again infinite. But at $x = 0$ it is a small $p$ (m8eaning $p < 1$ ) that produces finite area:

$$
\int _ { 0 } ^ { 1 } { \frac { d x } { x } } = \ln x \bigg ] _ { 0 } ^ { 1 } = \infty \qquad \int _ { 0 } ^ { 1 } { \frac { d x } { x ^ { p } } } = { \frac { x ^ { 1 - p } } { 1 - p } } \bigg ] _ { 0 } ^ { 1 } = { \frac { 1 } { 1 - p } } \quad \mathrm { i f ~ } p < 1 .
$$

Loosely speaking “ $ \ln 0 = \infty$ :” Strictly speaking we integrate from the point $x = a$ near zero, to get $\textstyle \int _ { a } ^ { 1 } d x / x = - \ln a$ : As $a$ approaches zero, the area shows itself as infinite. For $y = 1 / x ^ { 2 }$ ; which blows up faster, the area $- 1 / x ] _ { 0 } ^ { 1 }$ is again infinite.

For $y = 1 / \sqrt { x }$ ; the area from 0 to 1 is 2: In that case $\begin{array} { r } { p = \frac { 1 } { 2 } } \end{array}$ : For $p = 9 9 / 1 0 0$ the area is $1 / ( 1 - p ) = 1 0 0$ : Approaching $p = 1$ the borderline in Figure 7.7 seems clear. But that cutoff is not as sharp as it looks.

Narrower borderline Under the graph of $1 / x$ ; the area is infinite. When we divide by ln $x$ or $( \ln x ) ^ { 2 }$ ; the borderline is somewhere in between. One has infinite area (going out to $x = \infty$ ), the other area is finite:

$$
\int _ { e } ^ { \infty } { \frac { d x } { x ( \ln x ) } } = \ln ( \ln x ) \int _ { e } ^ { \infty } = \infty \qquad \int _ { e } ^ { \infty } { \frac { d x } { x ( \ln x ) ^ { 2 } } } = - { \frac { 1 } { \ln x } } \biggr ] _ { e } ^ { \infty } = 1 .
$$

The first is $\int d u / u$ with $u = \ln x$ : The logarithm of ln $x$ does eventually make it to infinity. At $x = 1 0 ^ { 1 0 }$ ; the l8ogarithm is near 23 an8d $\ln ( \ln x )$ is near 3: That is slow! Even slower is $\ln ( \ln ( \ln x ) )$ in Problem 11: No function is exactly on the borderline.

The second integral in equation (4) is convergent (to 1). It is $\int d u / u ^ { 2 }$ with $u =$ ln $x$ : At first I wrote it with $x$ going from zero to infinity. That gave an answer I couldn’t believe:

$$
\int _ { 0 } ^ { \infty } { \frac { d x } { x ( \ln x ) ^ { 2 } } } = - { \frac { 1 } { \ln x } } \Biggr ] _ { 0 } ^ { \infty } = 0
$$

There must be a mistake, because we are integrating a positive functiÑon.8The area can’t be zero. It is8true that $1 / \ln b$ goes to zero a8s $b \to \infty$ : It is also true that $1 / \ln a$ goes to zero as $a \to 0$ : But there is another infinity in this integral. The trouble is at $x = 1$ ; where ln $x$ is zero and the area is infinite.

EXAMPLE 1 The factor $e ^ { - x }$ overrides any power $x ^ { p }$ (but only as $x \to \infty$ ).

$$
\textstyle \int _ { 0 } ^ { \infty } x ^ { 5 0 } e ^ { - x } d x = 5 0 ! \quad { \mathrm { b u t } } \quad \int _ { 0 } ^ { \infty } x ^ { - 1 } e ^ { - x } d x = \infty .
$$

The first integral is .50/.49/.48/ .1/: It comes from fifty integrations by parts (not recommended). Changing 50 to $\frac { 1 } { 2 }$ ; the integral defines $\bar { } ^ { 1 } \bar { } \frac { 1 } { 2 }$ factorial:” The product

# 7.5 Improper Integrals

${ \frac { 1 } { 2 } } { \Big ( } - { \frac { 1 } { 2 } } { \Big ) } { \Big ( } - { \frac { 3 } { 2 } } { \Big ) } \cdots$ has no way to stop, but somehow $\textstyle { \frac { 1 } { 2 } } !$ is $\scriptstyle { \frac { 1 } { 2 } } { \sqrt { \pi } }$ : See Problem 28: Th e inte gral $\textstyle \int _ { 0 } ^ { \infty } x ^ { 0 } e ^ { - x } d x = 1$ is the reason behind “zero factorial” ${ \bf \bar { \Psi } } = 1$ : That seems the most surprising of all.

The area under $e ^ { - x } / x$ is $( - 1 ) ! = \infty$ : The factor $e ^ { - x }$ is absolutely no help at $x =$ 0: That is an example (the first of many) in which we do not know an antiderivative— but still we get a decision. To integrate $e ^ { - x } / x$ we ne¤ed a computer. But to decide that an improper integral is infinite (in this case) or finite (in other cases), we rely on the following comparison test:

7C (Comparison test) Suppose that $0 \leqslant u ( x ) \leqslant v ( x )$ : Then the area under u.x is smaller than the area under $v ( x )$ : $\int u ( x ) d x < \infty$ if $\int v ( x ) d x < \infty$ if $\int u ( x ) d x = \infty$ then $\int v ( x ) d x = \infty$ :

Comparison can decide if the area is finite. We don’t get the exact area, but we learn about one function from the other. The trick is to construct a simple function (like $1 / x ^ { p } )$ which is on one side of the given function—and stays close to it:

EXAMPLE 2 $\int _ { 1 } ^ { \infty } { \frac { d x } { x ^ { 2 } + 4 x } } { \mathrm { ~ c o n v e r g e s ~ b y ~ c o m p a r i s o n ~ w i t h ~ } } \int _ { 1 } ^ { \infty } { \frac { d x } { x ^ { 2 } } } = 1 .$   
EXAMPLE 3 $\int _ { 1 } ^ { \infty } { \frac { d x } { \sqrt { x } + 1 } } { \mathrm { ~ d i v e r g e s ~ b y ~ c o m p a r i s o n ~ w i t h ~ } } \int _ { 1 } ^ { \infty } { \frac { d x } { 2 { \sqrt { x } } } } = \infty .$   
EXAMPLE 4 $\int _ { 0 } ^ { 1 } { \frac { d x } { x ^ { 2 } + 4 x } } { \mathrm { ~ d i v e r g e s ~ b y ~ c o m p a r i s o n ~ w i t h ~ } } \int _ { 0 } ^ { 1 } { \frac { d x } { 5 x } } = \infty .$   
EXAMPLE 5 $\int _ { 0 } ^ { 1 } { \frac { d x } { \sqrt { x } + 1 } } { \mathrm { ~ c o n v e r g e s ~ b y ~ c o m p a r i s o n ~ w i t h ~ } } \int _ { 0 } ^ { 1 } { \frac { d x } { 1 } } = 1 .$

In Examples 2 and 5, the integral on the right is larger than the integral on the left. Removing $_ { 4 x }$ and $\sqrt { x }$ increased the area. Therefore the integrals on the left are somewhere between»0 and 1:

In Examples 3 and 4, we increased the denominators. The integrals on the right are smaller, but still they diverge. So the integrals on the left diverge. The idea of comparing functions is seen in the next examples and Figure 7.8.

EXAMPLE 6 $\int _ { 0 } ^ { \infty } e ^ { - x ^ { 2 } } d x \ \mathrm { i s \ b e l o w } \int _ { 0 } ^ { 1 } 1 \ d x + \int _ { 1 } ^ { \infty } e ^ { - x } d x = 1 + 1 .$   
EXAMPLE 7 $\int _ { 1 } ^ { e } { \frac { d x } { \ln x } } { \mathrm { ~ i s ~ a b o v e } } \int _ { 1 } ^ { e } { \frac { d x } { x \ln x } } = \infty .$   
EXAMPLE 8 $\int _ { 0 } ^ { 1 } { \frac { d x } { \sqrt { x - x ^ { 2 } } } } { \mathrm { ~ i s ~ b e l o w } } \int _ { 0 } ^ { 1 } { \frac { d x } { \sqrt { x } } } + \int _ { 0 } ^ { 1 } { \frac { d x } { \sqrt { 1 - x } } } = 2 + 2 .$

There are two situations not yet mentioned, and both are quite common. The first is an integral all the way from $a = - \infty$ to $b = + \infty$ Ñ: T8hat is split into twÑo8parts, and each part must converge. By definition, the limits at $- \infty$ and $+ \infty$ are kept separate:

$$
\int _ { - \infty } ^ { \infty } y ( x ) d x = \int _ { - \infty } ^ { 0 } y ( x ) d x + \int _ { 0 } ^ { \infty } y ( x ) d x = \operatorname* { l i m } _ { a \to - \infty } \int _ { a } ^ { 0 } y ( x ) d x + \operatorname* { l i m } _ { b \to \infty } \int _ { 0 } ^ { b } y ( x ) d x .
$$

The bell-shaped curve y D e8 x2 covers a finite area (exactly $\sqrt { \pi } )$ .8The region extends to infinity in both dir8ectio8ns, and the separate areas are $\scriptstyle { \frac { 1 } { 2 } } { \dot { \sqrt { \pi } } }$ : But notice:

$$
\begin{array} { r } { \int _ { - \infty } ^ { \infty } x d x i s n o t d e f i n e d e \nu e n t h o u g h \int _ { - b } ^ { b } x d x = 0 f o r e \nu e r y b . } \end{array}
$$

The area under $y = x$ is $+ \infty$ on one side of zero. The area is $- \infty$ on the other side. We cannot accept $\infty - \infty = 0$ . The two areas must be separately finite, and in this case they are not.

EXAMPLE 9 $1 / x$ has balancing regions left and right8of $x = 0$ : Compute $\int _ { - 1 } ^ { 1 } d x / x$ :

This integral does not exist. There is no answer, even for the region in Figure $7 . 8 \mathrm { c }$ . (They are mirror images because $1 / x$ is an odd function.) You may feel that the combined integral from $^ { - 1 }$ to 1 should be zero. Cauchy agreed with that—his “principal value integral” is zero. But the rules say no: $\infty - \infty$ is not zero.