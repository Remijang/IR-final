# 6.2 The Exponential $e ^ { x }$

The last section discussed $b ^ { x }$ and $\log _ { b } y$ : The base $b$ was arbitrary—it could be 2 or 6 or 9:3 or any positive number except 1: But in practice, only a few bases are used. I have never met a logarithm to base 6 or 9:3: Realistically there are two leading candidates for $b$ , and 10 is one of them. This section is about the other one, which is an extremely remarkable number. This number is not seen in arithmetic or algebra or geometry, where it looks totally clumsy and out of place. In calculus it comes into its own.

The number is $e$ : That symbol was chosen by Euler (initially in a fit of selfishness, but he was a wonderful mathematician). It is the base of the natural logarithm. It also controls the exponential $e ^ { x }$ , which is much more important than ln $x$ : Euler also chose $\pi$ to stand for perimeter—anyway, our first goal is to find $e$ :

Remember that the derivatives of $b ^ { x }$ and $\log _ { b } y$ include a constant $c$ that depends on $b$ : Equations (10) and (11) in the previous section were

$$
{ \frac { d } { d x } } b ^ { x } = c b ^ { x } \qquad { \mathrm { a n d } } \qquad { \frac { d } { d y } } \log _ { b } y = { \frac { 1 } { c y } } .
$$

At $x = 0$ , the graph of $b ^ { x }$ starts from $b ^ { 0 } = 1$ : The slope is $c$ : At $y = 1$ , the graph of $\log _ { b } y$ starts from $\log _ { b } 1 = 0$ : The logarithm has slope $1 / c$ : With the right choice of the base $b$ those slopes will equal 1 (because $c$ will equal 1).

For $y = 2 ^ { x }$ the slopeÑ $c$ is near :7: We already tried $\Delta x = . 1$ and found $\Delta y \approx . 0 7$ : The base has to be larger than 2; for a starting slope of $c = 1$ :

We begin with a direct computation of the slope of $\log _ { b } y$ at $y = 1$ :

$$
{ \frac { 1 } { c } } = { \mathrm { s l o p e ~ a t ~ } } 1 = \operatorname* { l i m } _ { h \to 0 } { \frac { 1 } { h } } { \Big [ } \log _ { b } ( 1 + h ) - \log _ { b } 1 { \Big ] } = \operatorname* { l i m } _ { h \to 0 } \log _ { b } { \Big [ } ( 1 + h ) ^ { 1 / h } { \Big ] } .
$$

Always $\log _ { b } 1 = 0$ : The fraction in the m8iddle is $\log _ { b } ( 1 + h )$ times the number $1 / h$ : This number can go up into the exponent, and it did.

The quantity $( \bar { 1 } + \bar { h } ) ^ { 1 / h }$ is unusual, to put it mildly. As $h \to 0$ , the number $1 + h$ is approaching 1: At the same time, $1 / h$ is approaching infinity. In the limit $_ { w e }$ have $1 ^ { \infty }$ : But that expression is meaningless (like $0 / 0$ ). Everything depends on the balance between “nearly 1” and “nearly $\infty$ :” This balance produces the extraordinary number $e$ :

DEFINITION The number $e$ is equal to $\operatorname* { l i m } _ { h \to 0 } ( 1 + h ) ^ { 1 / h }$ : Equivalently $e = \operatorname* { l i m } _ { h \to 0 } \left( 1 + { \frac { 1 } { n } } \right) ^ { n } .$

Before computing $e$ , look again at the slope $1 / c$ : At the end of equation (2) is the logarithm of $e$ :

$$
1 / c = \log _ { b } e .
$$

When the base is $b = e$ ; the slope is $\log _ { e } e = 1$ : That base $e$ has $c = 1$ as desired:

$$
\gamma _ { \ l } e d e r i v a t i v e \ o f e ^ { \ l ^ { x } } i s \ l \cdot e ^ { \ l ^ { x } } a n d t h e \ d e r i v a t i v e \ o f \log _ { e } \ y i s \frac { \ l 1 } { 1 \cdot y } .
$$

is is why the base $e$ is all-important in calculus. It makes $c = 1$ :

To compute the actual number $e$ from $( 1 + h ) ^ { 1 / h }$ , choose $h = 1 , 1 / 1 0 , 1 / 1 0 0 , \ldots .$ Then the exponents $1 / h$ are $n = 1 , 1 0 , 1 0 0 , \ldots$ (All limits and derivatives will become official in Section 6:4:) The table shows $( 1 + h ) ^ { 1 / h }$ approaching $e$ as $h  0$ and $n \to \infty$ :

$$
{ \begin{array} { c c c c c } { n } & { h = { \frac { 1 } { n } } } & { 1 + h = 1 + { \frac { 1 } { n } } } & { ( 1 + h ) ^ { 1 / h } = \left( 1 + { \frac { 1 } { n } } \right) ^ { n } } \\ { 1 } & { 1 . 0 } & { 2 . 0 } & { 2 . 0 } \\ { 2 } & { 0 . 5 } & { 1 . 5 } & { 2 . 2 5 } \\ { 1 0 } & { 0 . 1 } & { 1 . 1 } & { 2 . 5 9 3 7 4 2 } \\ { 1 0 0 } & { 0 . 0 1 } & { 1 . 0 1 } & { 2 . 7 0 4 8 1 4 } \\ { 1 0 0 0 } & { 0 . 0 0 1 } & { 1 . 0 0 1 } & { 2 . 7 1 6 9 2 4 } \\ { 1 0 0 0 } & { 0 . 0 0 0 1 } & { 1 . 0 0 0 1 } & { 2 . 7 1 8 1 4 6 } \end{array} }
$$

The last column is converging to $e$ (not quickly). There is an infinite series that converges much faster. We know 125; 000 digits of $e$ (and a billion digits of $\pi$ ). There are no definite patterns, although you might think so from the first sixteen digits:

$$
e = 2 . 7 1 8 2 8 1 8 2 8 4 5 9 0 4 5 \cdots ( \mathrm { a n d } 1 / e \approx . 3 7 ) .
$$

The powers of $e$ produce $y = e ^ { x }$ : At $x = 2 . 3$ and 5; we are close to $y = 1 0$ and 150:

The logarithm is the inverse function. The logarithms of 150 and 10; to the base $e$ , are close to $x = 5$ and $x = 2 . 3$ : There is a special name for this logarithm—the natural logarithm. There is also a special notation “ln” to show that the base is $e$ :

# ln y means the same as $\log _ { e } y$ : The natural logarithm is the exponent in $e ^ { x } = y$

The notation ln $y$ (or ln $x$ —it is the function that matters, not the variable) is standard in calculus courses. After calculus, the base is generally assumed to be $e$ : In most of science and engineering, the natural logarithm is the automatic choice. The symbol “exp $( x ) ^ { \prime \prime }$ means $e ^ { x }$ , and the truth is that the symbol “log $x ^ { , \ast }$ generally means ln $x$ : Base $e$ is understood even without the letters ln : But in any case of doubt—on a calculator key for example—the symbol “ln $x ^ { , \ast }$ emphasizes that the base is $e$ :

# THE DERIVATIVES OF $e ^ { x }$ AND ln $x$

Come back to derivatives and slopes. The derivative of $b ^ { x }$ is $c b ^ { x }$ ; and the derivative of $\log _ { b } y$ is $1 / c y$ : If $b = e$ then $c = 1$ . For all bases, equation (3) is $1 / c = \log _ { b } e$ : This gives $c$ —the slope of $b ^ { x }$ at $x = 0$ :

6E The number $c$ is $1 / \log _ { b } e = \log _ { e } b$ : Thus c equals ln b.

$c = \ln b$ is the mysterious constant that was not available earlier. The slope of $2 ^ { x }$ is $\ln 2$ times $2 ^ { x }$ : The slope of $e ^ { x }$ is $\ln { e }$ times $e ^ { x }$ (but ln $e = 1$ ). We have the derivatives on which this chapter depends:

6F The derivatives of $e ^ { x }$ and ln $y$ are $e ^ { x }$ and $1 / y$ : For other bases

$$
{ \frac { d } { d x } } b ^ { x } = ( \ln b ) b ^ { x } \qquad { \mathrm { a n d } } \qquad { \frac { d } { d y } } \log _ { b } y = { \frac { 1 } { ( \ln b ) y } } .
$$

To make clear that those derivatives come from the functions (and not at all from the dummy variables), we rewrite them using $t$ and $x$ :

$$
{ \frac { d } { d t } } e ^ { t } = e ^ { t } \qquad { \mathrm { a n d } } \qquad { \frac { d } { d x } } \ln x = { \frac { 1 } { x } } .
$$

Remark on slopes at $x = 0$ : It would be satisfying to see directly that the slope of $2 ^ { x }$ is below 1; and the slope of $4 ^ { x }$ is above 1: Quick proof: $e$ is between 2 and 4. But the idea is to see the slopes graphically. This is a small puzzle, which is fun to solve but can be skipped.

$2 ^ { x }$ rises from 1 at $x = 0$ to 2 at $x = 1$ : On that interval its average slope is 1: Its slope at the beginning is smaller than average, so it must be less than 1—as desired. On the other hand $4 ^ { x }$ rises from $\frac { 1 } { 2 }$ at $x = - \frac { 1 } { 2 }$ to 1 at $x = 0$ : Again the average slope is $\textstyle { \frac { 1 } { 2 } } { \Big / } { \frac { 1 } { 2 } } = 1$ : Since $x = 0$ comes at the end of this new interval, the slope of $4 ^ { x }$ at that poinıt exceeds 1: Somewhere between $2 ^ { x }$ and $4 ^ { x }$ is $e ^ { x }$ , which starts out with slope 1:

This is the graphical approach to $e$ : There is also the infinite series, and a fifth definition through integrals which is written here for the record:

1. $e$ is the number such that $e ^ { x }$ has slope 1 at $x = 0$   
2. $e$ is the base for which ln $y = \log _ { e } y$ has slope 1 at $y = 1$ $\left( 1 + { \frac { 1 } { n } } \right) ^ { \prime }$ n   
3. $e$ is the limit of as n $e = { \frac { 1 } { 0 ! } } + { \frac { 1 } { 1 ! } } + { \frac { 1 } { 2 ! } } + { \frac { 1 } { 3 ! } } + \cdots = 1 + 1 + { \frac { 1 } { 2 } } + { \frac { 1 } { 6 } } + \cdots$   
5. the area $\textstyle \int _ { 1 } ^ { e } x ^ { - 1 } d x$ equals 1:

The connections between 1, 2, and 3 have been made. The slopes are 1 when $e$ is the limit of $( 1 + 1 / n ) ^ { n }$ : Multiplying this out wlll lea8d to 4, the infinite series in Section 6.6. The official definition of $\ln x$ comes from $\int d x / x$ , and then 5 says that ln $e = 1$ : This approach to $e$ (Section 6.4) seems less intuitive than the others.

Figure $6 . 6 \mathsf { b }$ shows the graph of $e ^ { - x }$ : It is the mirror image of $e ^ { x }$ across the vertical axis. Their product is $e ^ { x } e ^ { - x } = 1$ : Where $e ^ { x }$ grows exponentially, $e ^ { - x }$ decays exponentially—or it grows as $x$ approaches $- \infty$ : Their growth and decay are faster than any power of $x$ . Exponential growth is more rapid than polynomial growth, so that $e ^ { x } / x ^ { n }$ goes to infinity (Problem 59). It is the fact that $e ^ { x }$ has slope $e ^ { x }$ which keeps the function climbing so fast.

The other curve is $y = e ^ { - x ^ { 2 } / 2 }$ : This is the famous “bell-shaped curve” of probability theory. After dividing by $\sqrt { 2 \pi }$ , it gives the normal distribution, which applies to so many averages and so many experiments. The Gallup Poll will be an example in Section 8.4. The curve is symmetric around its mean value $x = 0$ , since changing $x$ to $- x$ has no effect on $x ^ { 2 }$ :

About two thirds of the area under this curve is between $x = - 1$ and $x = 1$ : If you pick points at random below the graph, $2 / 3$ of all samples are expected in that interval. The points $x = - 2$ and $x = 2$ are “two standard deviations” from the center, enclosing $9 5 \%$ of the area. There is only a $5 \%$ chance of landing beyond. The decay is even faster than an ordinary exponential, because ${ \scriptstyle { \frac { 1 } { 2 } } } x ^ { 2 }$ has replaced $x$ :

# THE DERIVATIVES OF $e ^ { c x }$ AND $e ^ { u ( x ) }$

The slope of $e ^ { x }$ is $e ^ { x }$ : This opens up a whole world of functions that calculus can deal with. The chain rule gives the slope of $e ^ { 3 x }$ and $e ^ { \sin x }$ and every $e ^ { u ( x ) }$ :

6G The derivative of $e ^ { u ( x ) }$ is $e ^ { u ( x ) }$ times du=dx:

Special case $u = c x$ W The derivative of $e ^ { c x }$ is $c e ^ { c x }$ :

EXAMPLE 1 The derivative of $e ^ { 3 x }$ is $3 e ^ { 3 x }$ (here $c = 3 \AA$ ). The derivative of $e ^ { \sin x }$ is $e ^ { \sin x } \cos x$ (here $u = \sin { x } ,$ ). The derivative of $f ( u ( x ) )$ is $d f / d u$ times $d u / d x$ : Here $f = e ^ { u }$ so $d f / d u = e ^ { u }$ : The chain rule demands that second factor $d u / d x$ .

EXAMPLE 2 $e ^ { ( \ln 2 ) x }$ is the same as $2 ^ { x }$ : Its derivative is $\ln 2$ times $2 ^ { x }$ : The chain rule rediscovers our constant $c = \ln 2$ : In the slope of $b ^ { x }$ it rediscovers the factor $c = \ln b$ :

Generally $e ^ { c x }$ is preferred to the original $b ^ { x }$ : The derivative just brings down the constant $c . H t$ is better to agree on $e$ as the base, and put all complications (like $c = \ln b$ ) up in the exponent. The second derivative of $e ^ { c x }$ is $c ^ { 2 } e ^ { c x }$ :

EXAMPLE 3 The derivative of $e ^ { - x ^ { 2 } / 2 }$ is $- x e ^ { - x ^ { 2 } / 2 }$ (here $u = - x ^ { 2 } / 2$ so $d u / d x = - x )$ .

EXAMPLE 4 The second derivative of $f = e ^ { - x ^ { 2 } / 2 }$ , by the chain rule and product rule, is

$$
f ^ { \prime \prime } = ( - 1 ) \cdot e ^ { - x ^ { 2 } / 2 } + ( - x ) ^ { 2 } e ^ { - x ^ { 2 } / 2 } = ( x ^ { 2 } - 1 ) e ^ { - x ^ { 2 } / 2 } .
$$

Notice how the exponential survives. With every derivative it is multiplied by more factors, but it is still there to dominate growth or decay. The points of inflection, where the bell-shaped curve has $f ^ { \prime \prime } { = } 0$ in equation (10), are $x = 1$ and $x = - 1$ .

EXAMPLE 5 . $\left( u = n \ln x \right)$ /: Since $e ^ { n \ln x }$ is $x ^ { n }$ in disguise, its slope must be $n x ^ { n - 1 }$ :

$$
{ \mathrm { s l o p e } } = e ^ { n \ln x } { \frac { d } { d x } } \left( n \ln x \right) = x ^ { n } \left( { \frac { n } { x } } \right) = n x ^ { n - 1 } .
$$

This slope is correct for all $n$ ; integer or not. Chapter 2 produced $3 x ^ { 2 }$ and $4 x ^ { 3 }$ from the binomial theorem. Now $n x ^ { n - 1 }$ comes from ln and exp and the chain rule.

EXAMPLE 6 An extreme case is $x ^ { x } = ( e ^ { \ln x } ) ^ { x }$ : Here $u = x$ ln $x$ and we need $d u / d x$

$$
{ \frac { d } { d x } } \left( x ^ { x } \right) = e ^ { x \ln x } \left( \ln x + x \cdot { \frac { 1 } { x } } \right) = x ^ { x } ( \ln x + 1 ) .
$$

The integral of» $e ^ { x }$ is $e ^ { x }$ : The integral of $e ^ { c x }$ is n»ot $e ^ { c x }$ . The derivative multiplies by $c$ so the integral divides by $c$ : The integral of $e ^ { c x }$ is $e ^ { c x } / c$ (pÑlus a constant).

$$
\int e ^ { 2 x } d x = { \frac { 1 } { 2 } } e ^ { 2 x } + C \qquad \int b ^ { x } d x = { \frac { b ^ { x } } { \ln b } } + C
$$

$$
\int e ^ { 3 ( x + 1 ) } d x = { \frac { 1 } { 3 } } e ^ { 3 ( x + 1 ) } + C \quad \int e ^ { - x ^ { 2 } / 2 } d x \to \mathrm { { f a i l u r e } }
$$

The first one has $c = 2$ : The second has $c = \ln b$ —remember again that $b ^ { x } = e ^ { ( \ln b ) x }$ : The integral divides by $\ln { b }$ : In the third one, $e ^ { 3 ( x + 1 ) }$ is $e ^ { 3 x }$ times the number $e ^ { 3 }$

and that number is carried along. Or more likely we see $e ^ { 3 ( x + 1 ) }$ as $e ^ { u }$ : The missing $d u / d x = 3$ is fixed by dividing by 3: The last example fails because $d u / d x$ is not there. We cannot integrate without $d u / d x$ :

Here are three ex?amples with $d u / d x$ and one without it:

$$
\begin{array} { l l } { { \displaystyle \int e ^ { \sin x } \cos x d x = e ^ { \sin x } + C } } & { { \displaystyle \int x e ^ { x ^ { 2 } / 2 } d x = e ^ { x ^ { 2 } / 2 } + C } } \\ { { \displaystyle \int \frac { e ^ { \sqrt x } d x } { \sqrt x } = 2 e ^ { \sqrt x } + C } } & { { \displaystyle \int \frac { e ^ { x } d x } { ( 1 + e ^ { x } ) ^ { 2 } } = \frac { - 1 } { 1 + e ^ { x } } + C } } \end{array}
$$

The first is a pure $e ^ { u } d u$ : So is the second. The third has $u = { \sqrt { x } }$ and $d u / d x =$ $1 / 2 { \sqrt { x } }$ ,

so only the factor 2 had to be fixed. The fourth example does not belong with the others. It is the integral of $d u / u ^ { 2 }$ , not the integral of $e ^ { u } d u$ : I don’t know any way to tell you which substitution is best—except that the complicated part is $1 + e ^ { x }$ and it is natural to substitute $u$ . If it works, good.

Without an extra $e ^ { x }$ for $d u / d x$ ; the integral $\textstyle \int d x / ( 1 + e ^ { x } ) ^ { 2 }$ looks bad. But $u = 1 + e ^ { x }$ is still worth trying. It has $d u = e ^ { x } d x \overset { \sim } { = } ( u - 1 ) d x$ :

$$
\int \frac { d x } { ( 1 + e ^ { x } ) ^ { 2 } } = \int \frac { d u } { ( u - 1 ) u ^ { 2 } } = \int d u \left( \frac { 1 } { u - 1 } - \frac { 1 } { u } - \frac { 1 } { u ^ { 2 } } \right) .
$$

That last step is “partial fractions.” The integral splits into simpler pieces (explained in Section 7:4) and we integrate each piece. Here are three other integrals:

$$
\int e ^ { 1 / x } d x \quad \int e ^ { x } ( 4 + e ^ { x } ) d x \quad \int e ^ { - x } ( 4 + e ^ { x } ) d x
$$

The first can change to $- \int e ^ { u } d u / u ^ { 2 }$ , which is not much better. (It is just as impossible.) The second is actually $\int u d u$ , but I prefer a split: $\int 4 e ^ { x }$ and $\int e ^ { 2 x }$ are safer to do separately. The third is $\int ( 4 e ^ { - x } + 1 ) d x$ , which also separates. The exercises offer practice in reaching $e ^ { u } \bar { d } u / d x$ —ready to be integrated.

War»ning about definite integrals When th»e lower limit is $x = 0$ , there is a natural tendency to expect $f ( 0 ) = 0$ —in which case the lower limit contributes nothing. For a power $f = x ^ { 3 }$ that is true. For an exponential $f = e ^ { 3 x }$ it is definitely not true, because $f ( 0 ) = 1$ :

$$
\int _ { 0 } ^ { 1 } e ^ { 3 x } d x = { \frac { 1 } { 3 } } e ^ { 3 x } \int _ { 0 } ^ { 1 } = { \frac { 1 } { 3 } } \left( e ^ { 3 } - 1 \right) \quad \int _ { 0 } ^ { 1 } x e ^ { x ^ { 2 } } d x = { \frac { 1 } { 2 } } e ^ { x ^ { 2 } } \int _ { 0 } ^ { 1 } = { \frac { 1 } { 2 } } \left( e - 1 \right) .
$$