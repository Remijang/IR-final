# 5.5 The Definite Integral

The integral of $v ( x )$ is an antiderivative $f ( x )$ plus a constant $C$ . This section takes two steps. First, we choose $C$ . Second, we construct $f ( x )$ . The object is to define the integral—in the most frequent case when a suitable $f ( x )$ is not directly known.

The indefinite integral contains $^ { 6 6 } { + } C$ .” The constant is not settled because $f ( x ) + C$ has the same slope for every $C$ . When we care only about the derivative, $C$ makes no difference. When the goal is a number—a definite integral— $C$ can be assigned a definite value at the starting point.

For mileage traveled, we subtract the reading at the start. This section does the same for area. Distance is $f ( t )$ and area is $f ( x )$ —while the definite integral is $f ( b ) - f ( a )$ . Don’t pay attention to $t$ or $x$ , pay attention to the great formula of integral calculus:

$$
\int _ { a } ^ { b } v ( t ) d t = \int _ { a } ^ { b } v ( x ) d x = f ( b ) - f ( a ) .
$$

Viewpoint $1 { : }$ When $f$ is known, the equation gives the area from $a$ to $b$ .

Viewpoint 2 W When $f$ is not known, the equation defines $f$ from the area.

For a typical $v ( x )$ , we can’t find $f ( x )$ by guessing or substitution. But still $v ( x )$ has an “area” under its graph—and this yields the desired integral $f ( x )$ .

Most of this section is theoretical, leading to the definition of the integral. You may think we should have defined integrals before computing them—which is logically true. But the idea of area (and the use of rectangles) was already pretty clear in our first examples. Now we go much further. Every continuous function $v ( x )$ has an integral (also some discontinuous functions). Then the Fundamental Theorem completes the circle: The integral leads back to $d f / d x = v ( x )$ . The area up to $x$ is the antiderivative that we couldn’t otherwise discover.

# THE CONSTANT OF INTEGRATION

Our goal is to turn $f ( x ) + C$ into a definite integral— the area between $a$ and $b$ . The first requirement is to have are $a = z e r o$ at the start:

$$
f ( a ) + C = { \mathrm { s t a r t i n g ~ a r e a } } = 0 \quad { \mathrm { s o } } \quad C = - f ( a ) .
$$

For the area up to $x$ (moving endpoint, indefinite integral), use $t$ as the dummy variable:

the area from a ${ \begin{array} { r l } { \textit { t o x i s } \int _ { a } ^ { x } v ( t ) d t { = } f ( x ) { - } f ( a ) } & { ( i n d e f i n i t e i n t e g r a l ) } \\ { t o b i s \int _ { a } ^ { b } v ( x ) d x { = } f ( b ) { - } f ( a ) } & { ( d e f i n i t e i n t e g r a l ) } \end{array} }$ the area from a

EXAMPLE 1 The area under the graph of $5 ( x + 1 ) ^ { 4 }$ from $a$ to $b$ has $f ( x ) = ( x + 1 ) ^ { 5 }$ :

$$
\begin{array} { r } { \int _ { a } ^ { b } 5 ( x + 1 ) ^ { 4 } d x = ( x + 1 ) ^ { 5 } \Big ] _ { a } ^ { b } = ( b + 1 ) ^ { 5 } - ( a + 1 ) ^ { 5 } . } \end{array}
$$

The calculation has two separate steps—first find $f ( x )$ , then substitute $b$ and $a$ . After the first step, check that $d f / d x$ is $v$ . The upper limit in the second step gives plus

$f ( b )$ , the lower limit gives minus $f ( a )$ . Notice the brackets (or the vertical bar):

$$
f ( x ) \big ] _ { a } ^ { b } = f ( b ) - f ( a ) \quad x ^ { 3 } | _ { 1 } ^ { 2 } = 8 - 1 \quad \big [ \cos x \big ] _ { 0 } ^ { 2 t } = \cos 2 t - 1 .
$$

Changing the example to $f ( x ) = ( x + 1 ) ^ { 5 } - 1$ gives an equally good antiderivative— and now $f ( 0 ) = 0$ . But $f ( b ) - f ( a )$ stays the same, because the $^ { - 1 }$ disappears:

$$
\left[ ( x + 1 ) ^ { 5 } - 1 \right] _ { a } ^ { b } = ( ( b + 1 ) ^ { 5 } - 1 ) - ( ( a + 1 ) ^ { 5 } - 1 ) = ( b + 1 ) ^ { 5 } - ( a + 1 ) ^ { 5 } .
$$

EXAMPLE 2 When $v = 2 x$ sin $x ^ { 2 }$ we recognize $f = - \cos x ^ { 2 }$ . The area from 0 to 3 is

$$
\scriptstyle \int _ { 0 } ^ { 3 } 2 x \sin x ^ { 2 } d x = - \cos x ^ { 2 } \displaystyle \int _ { 0 } ^ { 3 } = - \cos 9 + \cos 0 .
$$

The upper limit copies the minus sign. The lower limit gives $- ( - \cos 0 )$ , which is $+ \cos 0$ . That e»xample shows the »right form for sol»ving exercises on definite integrals.

Example 2 jumped directly to $f ( x ) = - \cos x ^ { 2 }$ . But most problems involving the chain rule go more slowly—by substitution. Set $u = x ^ { 2 }$ , with $d u / d x = 2 x$ :

$$
\int _ { 0 } ^ { 3 } 2 x \sin x ^ { 2 } d x = \int _ { 0 } ^ { 3 } \sin u { \frac { d u } { d x } } d x = \int _ { ? } ^ { ? } \sin u d u .
$$

We need new limits when u replaces $x ^ { 2 }$ . Those limits on $u$ are $a ^ { 2 }$ and $b ^ { 2 }$ . (In this case $\scriptstyle a ^ { 2 } = 0 ^ { 2 }$ an»d $b ^ { 2 } = 3 ^ { 2 } = 9 .$ .) If $x$ go»es from a to $b$ , then $u$ goes from $u ( a )$ to $u ( b )$ .

$$
\int _ { a } ^ { b } v ( u ( x ) ) { \frac { d u } { d x } } d x = \int _ { u ( a ) } ^ { u ( b ) } v ( u ) d u = f ( u ( b ) ) - f ( u ( a ) ) .
$$

$$
\int _ { x = 0 } ^ { 1 } ( x ^ { 2 } + 5 ) ^ { 3 } x d x = \int _ { u = 5 } ^ { 6 } u ^ { 3 } { \frac { d u } { 2 } } = { \frac { u ^ { 4 } } { 8 } } { \Bigg ] } _ { 5 } ^ { 6 } = { \frac { 6 ^ { 4 } } { 8 } } - { \frac { 5 ^ { 4 } } { 8 } } .
$$

In this case $u = x ^ { 2 } + 5$ . Therefore $d u / d x = 2 x$ (or $d u = 2 x d x$ for differentials). We have to account for the missing 2. The integral is ${ \textstyle \frac { 1 } { 8 } } u ^ { 4 }$ . The limits on $u = x ^ { 2 } + 5$ are $u ( 0 ) = 0 ^ { 2 } + 5$ and $u ( 1 ) = 1 ^ { 2 } + 5$ . That is why the $u$ -integral goes from 5 to 6. The alternative is to find $\begin{array} { r } { f ( x ) = \frac { 1 } { 8 } ( x ^ { 2 } + 5 ) ^ { 4 } } \end{array}$ in one jump (and check it).

# EXAMPLE 4 $\int _ { 0 } ^ { 1 } \ d \mathbf { 0 }$ sin $x ^ { 2 } d x = ? ?$ (no elementary function gives this integral).

If we try cos $x ^ { 2 }$ , the chain rule produces an extra $2 x$ —no adjustment will work. Does sin $x ^ { 2 }$ still have an antiderivative? Yes! Every continuous $v ( x )$ has an $f ( x )$ . Whether $f ( x )$ has an algebraic formula or not, we can write it as $\int v ( x ) d x$ . To define that integral, we now take the limit of rectangular areas.

# INTEGRALS AS LIMITS OF “RIEMANN SUMS”

We have come to the definition of the integral. The chapter started with the integrals of $x$ and $x ^ { 2 }$ , from formulas for $1 + \cdots + n$ and $1 ^ { 2 } + \cdots + n ^ { 2 }$ . We will not go back to those formulas. But for other functions, too irregular to find exact sums, the rectangular areas also approach a limit.

That limit is the integral. This definition is a major step in the theory of calculus. It can be studied in detail, or understood in principle. The truth is that the definition is not so painful—you virtually know it already.

Problem Integrate the continuous function $v ( x )$ over the interval $[ a , b ]$ .   
Step 1 Split $[ a , b ]$ into $n$ subintervals $[ a , x _ { 1 } ] , [ x _ { 1 } , x _ { 2 } ] , \dotsc , [ x _ { n - 1 } , b ]$ .

The “meshpoints” $x _ { 1 } , x _ { 2 } , \ldots$ divide up the interval from $a$ to $b$ . The endpoints are $x _ { 0 } = a$ and $x _ { n } = b$ . The length of subinterval $k$ is $\Delta x _ { k } = x _ { k } - x _ { k - 1 }$ . In that smaller interval, the minimum of $v ( x )$ is $m _ { k }$ . The maximum is $M _ { k }$ .

Now construct rectangles. The “lower rectangle” over interval $k$ has height $m _ { k }$ . The “upper rectangle” re¥aches to $M _ { k }$ . Since $v$ is co ntinuous, there are points $x _ { \mathrm { m i n } }$ and $x _ { \mathrm { m a x } }$ where $v = m _ { k }$ and $v = M _ { k }$ (extreme value theorem). The graph of $v ( x )$ is in between.

Important: The area under $v ( x )$ contains the area $\cdot _ { s } , \cdot _ { \ l }$ of the lower rectangles:

$$
\begin{array} { r } { \int _ { a } ^ { b } v ( x ) d x \geqslant m _ { 1 } \Delta x _ { 1 } + m _ { 2 } \Delta x _ { 2 } + \cdots + m _ { n } \Delta x _ { n } = s . } \end{array}
$$

The area under $v ( x )$ is contained in the area $\mathbf { \nabla } \cdot S ^ { \mathbf { \nabla } , \mathbf { \mu } }$ of the upper rectangles:

$$
\begin{array} { r } { \int _ { a } ^ { b } v ( x ) d x \leqslant M _ { 1 } \Delta x _ { 1 } + M _ { 2 } \Delta x _ { 2 } + \cdots + M _ { n } \Delta x _ { n } = S . } \end{array}
$$

The lower sum $s$ and the upper sum $S$ were computed earlier in special cases— when $v$ was $x$ or $x ^ { 2 }$ and the spacings $\Delta x$ were equal. Figure $5 . 9 \mathrm { a }$ shows why $s \leqslant$ area $\leqslant S$ .

Notice an important fact. When a new dividing point $x ^ { \prime }$ is added, the lower sum increases. The minimum in on¤e piec¤e can¤be gre¤ater (see second figure) than the original $m _ { k }$ . Similarly the upper sum decreases. The maximum in one piece can be below the overall maximum. As new points are added, $s$ goes up and $S$ comes down. So the sums come closer together:

$$
\begin{array} { r l r } { s \leqslant s ^ { \prime } \leqslant } & { { } \leqslant S ^ { \prime } \leqslant S . } \end{array}
$$

I have left space in between for the curved area—the integral of $v ( x )$ .

Now add more and more meshpoints in such a way that $\Delta x _ { \mathrm { m a x } } \to 0$ . The lower sums increase and the upper sums decrease. They never pass each other. If $v ( x )$ is continuous, those sums close in on a single number $A$ . That number is the definite integral—the area under the graph.

DEFINITION The area $A$ is the common limit of the lower and upper sums:

$$
s \to A { \mathrm { ~ a n d ~ } } S \to A { \mathrm { ~ a s ~ } } \Delta x _ { \mathrm { m a x } } \to 0 .
$$

This limit $A$ exists for all continuous $v ( x )$ , and also for some discontinuous functions.   
When it exists, $A$ is the “Riemann integral” of $v ( x )$ from $a$ to $b$ .

# 5.5 The Definite Integral

# REMARKS ON THE INTEGRAL

As for derivatives, so for integrals: The definition involves a limit. Calculus is built on limits, and we always add “if the limit exists.” That is the delicate point. I hope the next five remarks (increasingly technical) will help to distinguish functions that are Riemann integrable from functions that are not.

Remark 1 The sums $s$ and $S$ may fail to approach the same limit. A standard example has $V ( x ) = 1$ at all fractions $x = p / q$ , and $V ( x ) = 0$ at all other points. Every interval contains rational points (fractions) and irrational points (nonrepeating decimals). Therefore $m _ { k } = 0$ and $M _ { k } = 1$ . The lower sum is always $s = 0$ . The upper sum is always $S = b - a$ (the sum of 1’s times $\Delta x$ ’s). The gap in equation (7) stays open. This function $V ( x )$ is not Riemann integrable. The area under its graph is not defined (at least by RiemanÑn—see Remark 5).

Remark 2 The step function $U ( x )$ is discontinuous but still integrable. On every interval the minimum $m _ { k }$ equals the maximum $M _ { k }$ —except on theÑinterval contÑaining the jump. That jump interval has $m _ { k } = 0$ and $M _ { k } = 1$ . But when we multiply by $\Delta x _ { k }$ , and require $\Delta x _ { \mathrm { m a x } } \to 0$ Ñ, the difference between $s$ and $S$ goes to zero. The area under a step function is clear—the rectangles fit exactly.

Remark 3 With patience another key step could be proved: If $s \to A$ and $S \to A$ for one sequence of meshpoints, then this limit $A$ is approached by every choice of meshpoints with $\Delta x _ { \mathrm { m a x } } \to 0$ . The integral is the lower bound of all upper sums $S$ , and it is the upper bound of all possible $s$ —provided those bounds are equal. The gap must close, to define the integral.

The same limit $A$ is approached by “in-between rectangles.” The height $v ( x _ { k } ^ { * } )$ can be computed at any point $x _ { k } ^ { * }$ in subinterval $k$ . See Figures $5 . 9 \mathrm { c }$ and 5.10. Then the total rectangular area is a “Riemann sum” between $s$ and $S$ :

$$
S ^ { * } = v ( x _ { 1 } ^ { * } ) \Delta x _ { 1 } + v ( x _ { 2 } ^ { * } ) \Delta x _ { 2 } + \cdots + v ( x _ { n } ^ { * } ) \Delta x _ { n } .
$$

We cannot tell whether the true area is above or below $S ^ { * }$ . Very often $A$ is closer to $S ^ { * }$ than to $s$ or $S$ . The midpoint rule takes $x ^ { * }$ in the middle of its interval (Figure 5.10), and Section 5.8 will establish its extra accuracy. The extreme sums $s$ and $S$ are used in the definition while $S ^ { * }$ is used in computation.

Remark 4 Every continuous function is Riemann integrable. The proof is optional (in my class), but it belongs here for reference. It starts with continuity at $x ^ { * }$ : “For any " there is a $\delta$ . . . .” When the rectangles sit between $x ^ { * } - \delta$ and ${ x ^ { * } } + \delta$ , the bounds $M _ { k }$ and $m _ { k }$ differ by less than $2 \varepsilon$ . Multiplying by the base $\Delta x _ { k }$ , the areas differ by less than $2 \varepsilon ( \Delta x _ { k } )$ . Combining all rectangles, the upper and lower sums differ by less than $2 \varepsilon ( \Delta x _ { 1 } + \Delta x _ { 2 } + \cdots + \Delta x _ { n } ) = 2 \varepsilon ( b - a )$ .

# 5 Integrals

As $\varepsilon \to 0$ we conclude that $S$ comes arbitrarily close to $s$ . They squeeze in on a single number $A$ . The Riemann sums approach the Riemann integral, $i f v$ is continuous.

Two problems are hidden by that reasoning. One is at the end, where $S$ and $s$ come together. We have to know that the line of real numbers has no “holes,” so there is a number $A$ to which these sequences converge. That is true.

Any increasing sequence, if it is bounded above, approaches a limit.

The decreasing sequence $S$ , bounded below, converges to the same limit. So $A$ exists.

The other problem is about continuity. We assumed without saying so that the width 2ı is the same around every point $x ^ { * }$ . We did not allow for the possibility that $\delta$ might approach zero where $v ( x )$ is rapidly changing—in which case an infinite number of rectangles could be needed. Our reasoning requires that

$v ( x )$ is uniformly continuous: ı depends on " but not on the position of $x ^ { * }$ .

For each $\varepsilon$ there is a $\delta$ that works at all points in the interval. A continuous function on a closed interval is uniformly continuous. This fact (proof omitted) makes the reasoning correct, and $v ( x )$ is integrable.

On an infinite interval, even $v = { x } ^ { 2 }$ is not uniformly continuous. It changes across a subinterval by $( x ^ { * } + \delta ) ^ { 2 } - ( x ^ { * } - \delta ) ^ { 2 } = 4 x ^ { * } \delta$ . As $x ^ { * }$ gets larger, $\delta$ must get smaller— to keep $4 x ^ { * } \delta$ below $\varepsilon$ . No single $\delta$ succeeds at all $x ^ { * }$ . But on a finite interval $[ 0 , b ]$ , the choice $\delta = \varepsilon / 4 b$ works everywhere—so $v = x ^ { 2 }$ is uniformly continuous.

Remark 5 If those four remarks were fairly optional, this one is totally at your discretion. Modern mathematics needs to integrate the zero-one function $V ( x )$ in the first remark. Somehow $V$ has more 0’s than 1’s. The fractions (where $V ( x ) = 1 { \frac { } { } }$ ) can be put in a list, but the irrational numbers (where $V ( x ) = 0 )$ are “uncountable.” The integral ought to be zero, but Riemann’s upper sums all involve $M _ { k } = 1$ .

Lebesgue discovered a major improvement. He allowed infinitely many subintervals (smaller and smaller). Then all fractions can be covered with intervals of total width $\varepsilon$ : (Amazing, when the fractions are packed so densely.) The idea is to cover $1 / q , 2 / q , \dots , q / q$ by narrow intervals of total width $\varepsilon / 2 ^ { q }$ . Combining all $q = 1 , 2 , 3 , \ldots$ ; the total width to cover all fractions is no more than ${ \widehat { \varepsilon } } { \left( { \frac { 1 } { 2 } } + { \frac { 1 } { 4 } } + { \frac { 1 } { 8 } } + \cdots \right) } = \varepsilon$ .raSriyn, cthe $V ( x ) = 0$ uevienrtyewgrhaelr”e  eslsze,rothaesudpepsieresd.um $S$ is only $\varepsilon$ $\varepsilon$

That completes a fair amount of theory, possibly more than you want or need— but it is satisfying to get things straight. The definition of the integral is still being studied by experts (and so is the derivative, again to allow more functions). By contrast, the properties of the integral are used by everybody. Therefore the next section turns from definition to properties, collecting the rules that are needed in applications. They are very straightforward.