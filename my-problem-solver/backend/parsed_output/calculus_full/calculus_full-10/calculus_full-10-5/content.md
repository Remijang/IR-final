This section studies the properties of a power series. When the basepoint is zero, the powers are $x ^ { n }$ . The series is $\Sigma a _ { n } x ^ { n }$ . When the basepoint is $x = a$ , the powers are $( x - a ) ^ { n }$ . We want to know when and where (and how quickly) the series converges to the underlying function. For $e ^ { x }$ and cos $x$ and sin $x$ there is convergence for all $x$ —but that is certainly not true for $1 / ( 1 - x )$ . The convergence is best when the function is smooth.

First I emphasize that power series are not the only series. For many applications they are not the best choice. An alternative is a sum of sines, $f ( x ) = \Sigma b _ { n }$ sin $n x$ . That is a “Fourier sine series”, which treats all $x$ ’s equally instead of picking on a basepoint. A Fourier series allows jumps and corners in the graph—it takes the rough with the smooth. By contrast a power series is terrific near its basepoint, and gets worse as you move away. The Taylor coefficients $a _ { n }$ are totally determined at the basepoint—where all derivatives are computed. Remember the rule for Taylor series:

$$
a _ { n } = ( n \mathrm { t h ~ d e r i v a t i v e ~ a t ~ t h e ~ b a s e p o i n t } ) / n ! = f ^ { ( n ) } ( a ) / n !
$$

A remarkable fact is the convergence in a symmetric interval around $x = a$ .

10M A power series $\Sigma a _ { n } x ^ { n }$ either converges for all $x$ , or it converges only at the basepoint $x = 0$ , or else it has a radius of convergence $r$ :

The series $\Sigma x ^ { n } / n !$ converges for all $x$ (the sum is $e ^ { x }$ ). The series $\Sigma n ! x ^ { n }$ converges for no $x$ (except $x = 0$ ). The geometric series $\Sigma { { x } ^ { n } }$ converges absolutel|y for $| x | <$ 1 and diverges for $\left| x \right| > 1$ . Its radius of convergence is $r = 1$ . Note that its sum $1 / ( 1 - x )$ is perfectly good for $\left| x \right| > 1$ —the function is all right but the series has given up. If something goes wrong at the distance $r$ , a power series can’t get past that point.

When the basepoint is $x = a$ , the interval of convergence shifts over to $\left| x - a \right| < r$ : The series converges for $x$ between $a - r$ and $a + r$ (symmetric around $a$ ). We cannot say in advance whether the endpoints $a \pm r$ give divergence or convergence (absolute or conditional). Inside the interval, an easy comparison test will now prove convergence.

PROOF OF 10M Supp|ose $\Sigma a _ { n } X ^ { n }$ conv||erges |at a p|articul|ar point $X$ . The proof will show that $\Sigma a _ { n } x ^ { n }$ converges when $| x |$ is less than the number $\vert X \vert$ . Thus convergence at $X$ gives convergence at all closer points $x$ (I mean closer to the basepoint 0). Proof: Since $\Sigma a _ { n } X ^ { n }$ converges, its terms approach zero. Eventually $\left| a _ { n } X ^ { n } \right| < 1$ and then

$$
| a _ { n } x ^ { n } | = | a _ { n } X ^ { n } | | x / X | ^ { n } < | x / X | ^ { n } .
$$

Our series $\Sigma a _ { n } x ^ { n }$ is absolutely convergent by comparison with the geometric series for $\left| x / X \right|$ , which converges since $\left| x / X \right| < 1$ .

EXAMPLE 1 The series $\Sigma n x ^ { n } / 4 ^ { n }$ has radius of convergence $r = 4$ .

The ratio test and root test are best for power series. The ratios between terms approach $x / 4$ (and so does the $n$ th root of $n x ^ { n } / 4 ^ { n } .$ ):

$$
{ \frac { ( n + 1 ) x ^ { n + 1 } } { 4 ^ { n + 1 } } } { \Bigg / } { \frac { n x ^ { n } } { 4 ^ { n } } } = { \frac { x } { 4 } } { \frac { n + 1 } { n } } { \mathrm { ~ a p p r o a c h e s ~ } } L = { \frac { x } { 4 } } .
$$

The ratio test gives convergence if $L < 1$ , which means $\vert x \vert < 4$ .

EXAMPLE 2 The sine series $x - { \frac { x ^ { 3 } } { 3 ! } } + { \frac { x ^ { 5 } } { 5 ! } } - \cdots$ has $r = \infty$ (it converges everywhere).

The ratio of $x ^ { n + 2 } / ( n + 2 ) !$ to $x ^ { n } / n !$ is $x ^ { 2 } / ( n + 2 ) ( n + 1 )$ . This approaches $L = 0$ .

EXAMPLE 3 The series $\Sigma ( x - 5 ) ^ { n } / n ^ { 2 }$ has radius $r = 1$ around its basepoint $a =$ 5.

The ratios between terms approach $L = x - 5 .$ (The fractions $n ^ { 2 } / ( n + 1 ) ^ { 2 }$ go toward 1.) There is absolute convergence if $| x - 5 | < 1$ . This is the interval $4 < x < 6$ , symmetric around the basepoint. This series happens to converge at the endpoints 4 and 6, because of the factor $1 / n ^ { 2 }$ . That factor decides the delicate question—convergence at the endpoints—but all powers of $n$ give the same interval of convergence $4 < x < 6$ .

# CONVERGENCE TO THE FUNCTION: REMAINDER TERM AND RADIUS $\boldsymbol { r }$

Remember that a Taylor series starts with a function $f ( x )$ . The derivatives at the basepoint produce the series. Suppose the series converges: Does it converge to the function ? This is a question about the remainder $R _ { n } ( x ) = f ( x ) - s _ { n } ( x )$ , which is the difference between $f$ and the partial sum $s _ { n } = a _ { 0 } + \cdots + a _ { n } ( x - a ) ^ { n }$ . The remainder $R _ { n }$ is the error if we stop the series, ending with the $n$ th derivative term $a _ { n } ( x - a ) ^ { n }$ .

10N Suppose $f$ has an $( n + 1 )$ st derivative from the basepoint $a$ out to $x$ . Then for some point $c$ in between (position not known) the remainder at $x$ equals

$$
R _ { n } ( x ) = f ( x ) - s _ { n } ( x ) = f ^ { ( n + 1 ) } ( c ) ( x - a ) ^ { n + 1 } / ( n + 1 ) !
$$

The error in stopping at the $n$ th derivativ1e is controlled by t2he $( n + 1 )$ st derivative.

You will guess, correctly, that the unknown point $c$ comes from the Mean Value Theorem. For $n = 1$ the proof is at the end of Section 3.8. That was the error $e ( x )$ in linear approximation:

$$
\begin{array} { r } { R _ { 1 } ( x ) = f ( x ) - f ( a ) - f ^ { \prime } ( a ) ( x - a ) = \frac { 1 } { 2 } f ^ { \prime \prime } ( c ) ( x - a ) ^ { 2 } . } \end{array}
$$

For every $n$ , the proof compares ${ \boldsymbol { R _ { n } } }$ with $( x - a ) ^ { n + 1 }$ . Their $( n + 1 ) \mathrm { s t }$ derivatives are $f ^ { ( n + 1 ) }$ and $( n + 1 ) !$ The generalized Mean Value Theorem says that the ratio of $R _ { n }$ to $( x - a ) ^ { n + 1 }$ equals the ratio of those derivatives, at the right point $c$ . That is equation (2). The details can stay in Section 3.8 and Problem 23, because the main point is what we want. The error is exactly like the next term $a _ { n + 1 } ( x - a ) ^ { n + 1 }$ , except that the $( n + 1 ) \mathrm { s t }$ derivative is at $c$ instead of the basepoint $a$ .

EXAMPLE 4 When $f$ is $e ^ { x }$ , the $( n + 1 )$ st derivative is $e ^ { x }$ . Therefore the error is

$$
R _ { n } = e ^ { x } - \left( 1 + x + \cdots + { \frac { x ^ { n } } { n ! } } \right) = e ^ { c } { \frac { x ^ { n + 1 } } { ( n + 1 ) ! } } .
$$

At $x = 1$ and $n = 2$ , the error is $e - ( 1 + 1 + { \textstyle { \frac { 1 } { 2 } } } ) \approx . 2 1 8$ . The right side is $e ^ { c } / 6$ The unknown point is $c = \ln ( . 2 1 8 \cdot 6 ) = . 2 7$ . Thus $c$ lies between the basepoint $a = 0$ and the error point $x = 1$ , as required. The series converges to the function, because $R _ { n } \to 0$ .



In practice, $n$ is the number of derivatives to be calculated. We may aim for an error $\big | R _ { n } \big |$ below $1 0 ^ { - 6 }$ . Unfortunately, the high derivative in formula .2/ is awkward to estimate (except for $e ^ { x }$ ). And high derivatives in formula .1/ are difficult to compute. Most real calculations use only a few terms of a Taylor series. For more accuracy we move the basepoint closer, or switch to another series.

There is a direct connection between the function and the convergence radius $r$ . A hint came for $f ( x ) = 1 / ( 1 - x )$ . The function blows up at $x = 1$ —which also ends the convergence interval for the series. Another hint comes for $f = 1 / x$ , if we expand around $x = a = 1$ :

$$
{ \frac { 1 } { x } } = { \frac { 1 } { 1 - ( 1 - x ) } } = 1 + ( 1 - x ) + ( 1 - x ) ^ { 2 } + \cdots .
$$

This geometric series converges for $\left| 1 - x \right| < 1$ . Convergence s|to|ps  at the end point $x = 0 .$ —exactly where $1 / x$ blows up. The failure of the function stops the convergence of the series. But note that $1 / ( 1 + x ^ { 2 } )$ , which never seems to fail, also has convergence radius $r = 1$ :

$$
1 / ( 1 + x ^ { 2 } ) = 1 - x ^ { 2 } + x ^ { 4 } - x ^ { 6 } + \cdots { \mathrm { ~ c o n v e r g e s ~ o n l y ~ f o r ~ } } | x | < 1 .
$$

When you see the reason, you will know why $r$ is a “radius.” There is a circle, and the function fails at the edge of the circle. The circle contains complex numbers as well as real numbers. The imaginary points $i$ and $- i$ are at the edge of the circle. The function fails at those points because $1 / ( 1 + i ^ { 2 } ) = \infty$ .

Complex numbers are pulling the strings, out of sight. The circle of convergence reaches out to the nearest “singularity” of $f ( x )$ , real or imaginary or complex. For $1 / ( 1 + x ^ { 2 } )$ , the singularities at $i$ and $- i$ make $r = 1$ . If we expand around $a = 3$ , the distance to $i$ and $- i$ is $r = { \sqrt { 1 0 } }$ . If we change to $\ln ( 1 + x )$ , which blows up at $x = - 1$ , the radius of convergence of $x - { \textstyle { \frac { 1 } { 2 } } } x ^ { 2 } + { \overline { { { \frac { 1 } { 3 } } } } } x ^ { 3 } - \cdots$ is $r = 1$ .

# THE BINOMIAL SERIES

We close this chapter with one more series. It is the Taylor series for $( 1 + x ) ^ { p }$ , around the basepoint $x = 0$ . A typical power is $\begin{array} { r } { p = \frac { 1 } { 2 } } \end{array}$ , where we want the terms in

$$
{ \sqrt { 1 + x } } = 1 + { \textstyle { \frac { 1 } { 2 } } } x + a _ { 2 } x ^ { 2 } + \cdots .
$$

The slow way is to square both sides, which gives $\textstyle 1 + x + ( 2 a _ { 2 } + { \frac { 1 } { 4 } } ) x ^ { 2 }$ on the right. Since $1 + x$ is on the left, $a _ { 2 } = - { \frac { 1 } { 8 } }$ is needed to remove the $x ^ { 2 }$ term. Eventually $a _ { 3 }$ can be found. The fast way is to match the derivatives of $f = ( 1 + x ) ^ { 1 / 2 }$ :

$$
\begin{array} { r l r l r l } { f ^ { \prime } = \frac { 1 } { 2 } ( 1 + x ) ^ { - 1 / 2 } } & { } & { f ^ { \prime \prime } = \big ( \frac { 1 } { 2 } \big ) \big ( - \frac { 1 } { 2 } \big ) ( 1 + x ) ^ { - 3 / 2 } } & { } & { f ^ { \prime \prime } = \big ( \frac { 1 } { 2 } \big ) \big ( - \frac { 1 } { 2 } \big ) \big ( - \frac { 3 } { 2 } \big ) ( 1 + x ) ^ { - 5 / 2 } . } \end{array}
$$

At $x = 0$ those derivatives are $\textstyle { \frac { 1 } { 2 } } , - { \frac { 1 } { 4 } } , { \frac { 3 } { 8 } }$ . Dividing by 1Š; 2Š; 3Š gives

$$
a _ { 1 } = { \frac { 1 } { 2 } } a _ { 2 } = - { \frac { 1 } { 8 } } a _ { 3 } = { \frac { 1 } { 1 6 } } a _ { n } = { \frac { 1 } { n ! } } \left( { \frac { 1 } { 2 } } \right) \left( { \frac { 1 } { 2 } } - 1 \right) \cdots \left( { \frac { 1 } { 2 } } - n + 1 \right) .
$$

These are the binomial coefficients when the power is $\begin{array} { r } { p = \frac { 1 } { 2 } } \end{array}$ .

Notice the differencefrom thebinomials in Chapter 2. For those, thepower $p$ was a positive integer. The series $( 1 + x ) ^ { 2 } = 1 + 2 x + \overline { { x } } ^ { 2 }$ stopped at $x ^ { 2 }$ . The coefficients for $p = 2$ were $1 , 2 , 1 , 0 , 0 , 0 ,$ : : : : For fractional $p$ or negative $p$ those later coefficients are not zero, and wefind them from the derivativesof $( 1 + x ) ^ { p }$ :

$$
( 1 + x ) ^ { p } \quad p ( 1 + x ) ^ { p - 1 } \quad p ( p - 1 ) ( 1 + x ) ^ { p - 2 } \quad f ^ { ( n ) } = p ( p - 1 ) \cdots ( p - n + 1 ) ( 1 + x ) ^ { p - n } .
$$

Dividing by $0 ! , 1 ! , 2 ! , \ldots , n !$ at $x = 0$ , the binomial coefficients are

$$
1 \quad p \quad { \frac { p ( p - 1 ) } { 2 } } \cdots { \frac { f ^ { ( n ) } ( 0 ) } { n ! } } = { \frac { p ( p - 1 ) \cdots ( p - n + 1 ) } { n ! } } .
$$

For $p = n$ that last binomial coefficient is $n ! / n ! = 1$ . It gives the final $x ^ { n }$ at the end of $( 1 + x ) ^ { n }$ . For other values of $p$ , the binomial series never stops. $\ b { I t }$ converges for $\left| x \right| < 1$ :

$$
( 1 + x ) ^ { p } = 1 + p x + { \frac { p ( p - 1 ) } { 2 } } x ^ { 2 } + \cdots = \sum _ { n = 0 } ^ { \infty } { \frac { p ( p - 1 ) \cdots ( p - n + 1 ) } { n ! } } x ^ { n } .
$$

When $p = 1 , 2 , 3$ ;|: : : the?binomial coefficient $p ! / n ! ( n - p ) !$ counts the number of ways to select a group of $n$ friends out of a group of $p$ friends. If you have 20 friends, you can choose 2 of them in $( 2 0 ) ( 1 9 ) / 2 = 1 9 0$ way8s.

Suppose $p$ is not a positive integer. What goes wrong with $( 1 + x ) ^ { p }$ , to stop the convergence at $\left| x \right| = 1 ?$ The failure is at $x = - 1$ . If $p$ is negative, $( 1 + x ) ^ { p }$ blow up. If $p$ is positive, as in $\sqrt { 1 + x }$ , the higher derivatives blow up. Only for a positive integer $p = n$ does the convergence radius move out to $r = \infty$ . In that case the series for $( 1 + x ) ^ { n }$ stops at $x ^ { n }$ , and $f$ never fails.

A power series is a function in a new form. It is not a simple form, but sometimes it is the only form. To compute $f$ we have to sum the series. To square $f$ we have to multiply series. But the operations of calculus—derivative and integral—are easier. That explains why power series help to solve differential equations, which are a rich source of new funct ions. (Numerically the series are not always so good.) I shoul|d have said that the derivative and integral are easy for each separate term $a _ { n } x ^ { n }$ —and fortunately the convergence radius of the whole series is not changed.

If $f ( x ) = \Sigma a _ { n } x ^ { n }$ has convergence radius $r$ , so do its derivative and its integral: $\begin{array} { r } { d f / d x = \Sigma n a _ { n } x ^ { n - 1 } \quad \mathrm { a n d } \quad \int f ( x ) d x = \Sigma a _ { n } x ^ { n + 1 } / ( n + 1 ) } \end{array}$ also converge for $| x | < r$

EXAMPLE 5 The series for $1 / ( 1 - x )$ and its derivative $1 / ( 1 - x ) ^ { 2 }$ and its integral $- \ln ( 1 - x )$ all have $r = 1$ (because they all have trouble at $x = 1$ ). The series are $\Sigma { { x } ^ { n } }$ and $\Sigma n x ^ { n - 1 }$ and $\Sigma x ^ { n + 1 } / ( n + 1 )$ .

# 10 Infinite Series

EXAMPLE 6 We can integrate $e ^ { x ^ { 2 } }$ (previously impossible) by integrating every term in its series:

$$
\int e ^ { x ^ { 2 } } d x = \int \left( 1 + x ^ { 2 } + { \frac { 1 } { 2 ! } } x ^ { 4 } + \cdots \right) d x = x + { \frac { x ^ { 3 } } { 3 } } + { \frac { 1 } { 2 ! } } \left( { \frac { x ^ { 5 } } { 5 } } \right) + { \frac { 1 } { 3 ! } } \left( { \frac { x ^ { 7 } } { 7 } } \right) + \cdots .
$$

This always converges .r D /. The derivative of ex2 was never a problem.