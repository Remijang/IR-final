# 3.1 Linear Approximation

The book started with a straight line $f = v t$ : The distance is linear when the velocity is constant. As soon as $v$ begins to change, $f = v t$ falls apart. Which velocity do we choose, when $v ( t )$ is not constant? The solution is to take very short time intervals, in which $v$ is nearly constant:

$$
\begin{array} { r l } { f = v t } & { { } i s \ c o m p l e t e l y f a l s e } \\ { \Delta f = v \Delta t } & { { } i s \ n e a r l y t r u e } \\ { d f = v d t } & { { } i s \ e x a c t l y t r u e } \end{array}
$$

For a brief moment the function $f ( t )$ is line1ar—andstays near its tangent line.

In Section 2.3 we found the tangent line to $y = f ( x )$ : At $x = a$ , the slope of the curve and the slope of the line are $f ^ { \prime } ( a )$ : For points on the line, start at $y = f ( a )$ : Add the slope times the “increment” $x - a$ :

$$
Y = f ( a ) + f ^ { \prime } ( a ) ( x - a ) .
$$

We write a ca?pital $Y$ for the line and a small $y$ for the curve. The who?le point of tangents is that th?ey are close .provided we don’t move too far from $a$ /:

$$
y \approx Y \qquad { \mathrm { o r } } \qquad f ( x ) \approx f ( a ) + f ^ { \prime } ( a ) ( x - a ) .
$$

That is the all-purpose linear approximation. Figure 3.1 shows the square root function $y = { \sqrt { x } }$ and its tangent line at $x = a = 1 0 0$ : At the point $y = { \sqrt { 1 0 0 } } = 1 0$ , the slope is $1 / 2 { \sqrt { x } } = 1 / 2 0$ : The table beside the figure compares $y ( x )$ with $Y ( x )$ :

The accuracy gets worse as $x$ departs from 100: The tangent line leaves the curve. The arrow points to a good approximation at 102, and at 101 it would be even better. In this example $Y$ is larger than $y$ —th?e straigh?t line is above the curve. The slope of the line stays constant, and the slope of thecurve is decreasing. Such a curve will soon be called “concave downward,”and its tangent lines are above it.

Look again at $x = 1 0 2$ , where the approximation is good. In Chapter 2, when we were approaching $d y / d x$ , we started with $\Delta y / \Delta x$ :

$$
{ \mathrm { s l o p e } } \approx { \frac { { \sqrt { 1 0 2 } } - { \sqrt { 1 0 0 } } } { 1 0 2 - 1 0 0 } } .
$$

Now that is turned around! The slope is $1 / 2 0$ : What we don’t know is $\sqrt { 1 0 2 }$ :

$$
{ \sqrt { 1 0 2 } } \approx { \sqrt { 1 0 0 } } + ( { \mathrm { s l o p e } } ) ( 1 0 2 - 1 0 0 ) .
$$

You work with what you have. Earlier we didn’t know $d y / d x$ , so we used .3/: Now we are experts at $d y / d x$ , and we use .4/: After computing $y ^ { \prime } { = } 1 / 2 0$ once and for all, the tangent line stays near $\sqrt { x }$ for every number near 100: When that nearby number is $1 0 0 + \Delta x$ , notice the error as the approximation is squared:

$$
\left( \sqrt { 1 0 0 } + \frac { 1 } { 2 0 } \Delta x \right) ^ { 2 } = 1 0 0 + \Delta x + \frac { 1 } { 4 0 0 } ( \Delta x ) ^ { 2 } .
$$

The desired answer is $1 0 0 + \Delta x$ , and we are off by the last term involving $( \Delta x ) ^ { 2 }$ : The whole point of linear approximation is to ignore every term after $\Delta x$ :

There is nothing magic about $x = 1 0 0$ , except that it has a nice square root. Other points and other functions allow $y \approx Y$ : I would like to express this same idea in different symbols. Instead of starting from a and going to $x$ , we start from $x$ and $g o$ a distance $\Delta x$ to $x + \Delta x$ . The letters are different but the mathematics is identical.

3A At any point $x$ , and for any smooth function $y = f ( x )$ ,

$$
{ \mathrm { s l o p e ~ a t } } x \approx { \frac { f ( x + \Delta x ) - f ( x ) } { \Delta x } } .
$$

For the approximation to $f ( x + \Delta x )$ , multiply both sides by $\Delta x$ and add $f ( x )$ :

$$
f ( x + \Delta x ) \approx f ( x ) + ( \mathrm { s l o p e \ a t } x ) ( \Delta x ) .
$$

EXAMPLE 1 An important linear approximation: $( 1 + x ) ^ { n } \approx 1 + n x$ for $x$ near zero.

EXAMPLE 2 A second important approximation: $1 / ( 1 + x ) ^ { n } \approx 1 - n x$ for $x$ near zero.

Discussion Those are really the same. By changing $n$ to $- n$ in Example 1, it becomes Example 2. These are linear approximations using th e slopes $n$ and $- n$ at $x = 0$ :

$$
( 1 + x ) ^ { n } \approx 1 + ( s l o p e a t z e r o ) { \mathrm { ~ t i m e s ~ } } ( x - 0 ) = 1 + n x
$$

Here is the same thingwith $f ( x ) = x ^ { n }$ :The basepoint in equation (6) is now 1 or $x$ :

$$
( 1 + \Delta x ) ^ { n } \approx 1 + n \Delta x \qquad ( x + \Delta x ) ^ { n } \approx x ^ { n } + n x ^ { n - 1 } \Delta x .
$$

Better than that, here are numbers. For $n = 3$ and $^ { - 1 }$ and 100, take $\Delta x = . 0 1$ :

$$
( 1 . 0 1 ) ^ { 3 } \approx 1 . 0 3 \qquad \frac { 1 } { 1 . 0 1 } \approx . 9 9 \qquad \left( 1 + \frac { 1 } { 1 0 0 } \right) ^ { 1 0 0 } \approx 2
$$

Actually that last number is no good. The 100th power is too much. Linear approximation gives $1 + 1 0 0 \Delta x = 2$ , but a calculator gives $( 1 . 0 1 ) ^ { 1 0 0 } = 2 . 7 .$ : : : This is close to $e$ , the all-important number in Chapter 6. The binomial formula shows why the approximation failed:

$$
( 1 + \Delta x ) ^ { 1 0 0 } = 1 + 1 0 0 \Delta x + { \frac { ( 1 0 0 ) ( 9 9 ) } { ( 2 ) ( 1 ) } } ( \Delta x ) ^ { 2 } + \cdots .
$$

Linear approximation forgets the $( \Delta x ) ^ { 2 }$ term. For $\Delta x = 1 / 1 0 0$ that error is nearly $\frac { 1 } { 2 }$ : It is too big to overlook. The exact error is ${ \scriptstyle { \frac { 1 } { 2 } } } ( \Delta x ) ^ { 2 } f ^ { \prime \prime } ( c )$ , where the Mean Value Theorem in Section 3.8 places $c$ between $x$ and $x + \Delta x$ : You already see the point:

$y - Y$ is of order $( \Delta x ) ^ { 2 }$ : Linear approximation, quadratic error.

# DIFFERENTIALS

There is one more notation for this linear approximation. It has to be presented, because it is often used. The notation is suggestive and confusing at the same time—it keeps the same symbols $d x$ and $d y$ that appear in the derivative. Earlier we took great pains to emphasize that $d y / d x$ is not an ordinary fraction. $^ \dagger$ Until this paragraph, $d x$ and $d y$ have had no independent meaning. Now they become separate variables, like $x$ and $y$ but with their own names. These quantities $d x$ and $d y$ are called differentials.

The symbols $d x$ and $d y$ measure changes along the tangent line. They do for the approximation $Y ( x )$ exactly what $\Delta x$ and $\Delta y$ did for $y ( x )$ : Thus $d x$ and $\Delta x$ both measure distance across.

Figure 3.2 has $\Delta x = d x$ : But the change in $y$ does not equal the change in $Y$ : One is $\Delta y$ (exact for the function). The other is $d y$ (exact for the tangent line). The differential $d y$ is equal to $\Delta Y$ , the change along the tangent line. Where $\Delta y$ is the true change, $d y$ is its linear approximation $( d y / d x ) d x$ :

You often see $d y$ written as $f ^ { \prime } ( x ) d x$ :

$\Delta y =$ change in $y$ (along curve) $d y =$ change in $Y$ (along tangent)

EXAMPLE 3 $y = x ^ { 2 }$ has $d y / d x = 2 x$ so $d y = 2 x d x$ : The table has basepoint $x = 2$ : The prediction $d y$ differs from the true $\Delta y$ by exactly $( \Delta x ) ^ { 2 } = . 0 1$ and :04 and :09:

$$
{ \begin{array} { r l } { d x \ } & { d y \quad \quad \Delta x \quad \Delta y } \\ { y = x ^ { 2 } \quad \quad . 1 \quad 0 . 4 \quad \quad . 1 \quad 0 . 4 1 \quad \quad \Delta y = ( 2 + \Delta x ) ^ { 2 } - 2 ^ { 2 } } \\ { d y = 4 d x \quad \quad . 2 \quad 0 . 8 \quad \quad . 2 \quad 0 . 8 4 \quad \quad \Delta y = 4 \Delta x + ( \Delta x ) ^ { 2 } } \\ { \quad . 3 \quad 1 . 2 \quad \quad . 3 \quad 1 . 2 9 } \end{array} }
$$

The differential $d y = f ^ { \prime } ( x ) d x$ is consistent with the derivative $d y / d x = f ^ { \prime } ( x )$ : We finally have $d y = ( d y / d x ) d x$ , but this is not as obvious as it seems! It looks like cancellation—it is really a definition. Entirely new symbols could be used, but $d x$ and $d y$ have two advantages: They suggest small steps and they satisfy $d y = f ^ { \prime } ( x ) d x$ : Here are three examples and three rules:

$$
\begin{array} { r l } { d ( x ^ { n } ) = n x ^ { n - 1 } d x \quad } & { d ( f + g ) = d f + d g } \\ { d ( \sin x ) = \cos x d x \quad } & { d ( c f ) = c d f } \\ { d ( \tan x ) = \sec ^ { 2 } x d x \quad } & { d ( f g ) = f d g + g d f } \end{array}
$$

Science and engineering and virtually all applications of mathematics depend on linear approximation. The true function is “linearized,” using its slope $v$ :

Increasing the time by $\Delta t$ increases the distance by $\approx v \Delta t$ Increasing the force by $\Delta f$ increases the deflection by $\approx v \Delta f$ Increasing the production by $\Delta p$ increases its value by $\approx v \Delta p$

The goal of dynamics or statics or economics is to predict this multiplier $v$ —the derivative that equals the slope of the tangent line. The multiplier gives a local prediction of the change in the function. The exact law is nonlinear—but Ohm’s law and Hooke’s law and Newton’s law are linear approximations.

# ABSOLUTE CHANGE, RELATIVE CHANGE, PERCENTAGE CHANGE

The change $\Delta y$ or $\Delta f$ can be measured in three ways. So can $\Delta x$ :

$$
\begin{array} { l l l } { { A b s o l u t e ~ c h a n g e } } & { { \Delta f } } & { { \Delta x } } \\ { { R e l a t i v e ~ c h a n g e } } & { { \displaystyle { \frac { \Delta f } { f ( x ) } } } } & { { \displaystyle { \frac { \Delta x } { x } } } } \\ { { P e r c e n t a g e ~ c h a n g e } } & { { \displaystyle { \frac { \Delta f } { f ( x ) } } \times 1 0 0 } } & { { \displaystyle { \frac { \Delta x } { x } } \times 1 0 0 } } \end{array}
$$

Relative change is often more rea listic than absolute change. If we know the distance to the moon within three miles, that is more impressive than knowing our own height within one inch. Absolutely, one inch is closer than three miles. Relatively, three miles is much closer:

$$
\frac { 3 \mathrm { m i l e s } } { 3 0 0 , 0 0 0 \mathrm { m i l e s } } < \frac { 1 \mathrm { i n c h } } { 7 0 \mathrm { i n c h e s } } \quad \mathrm { o r } \quad . 0 0 1 \% < 1 . 4 \% .
$$

EXAMPLE 4 The radius of the Earth is within 80 miles of $r = 4 , 0 0 0$ miles. (a) Find the variation $d V$ in the volume $\begin{array} { r } { V = \frac { 4 } { 3 } \pi r ^ { 3 } } \end{array}$ , using linear approximation. (b) Compute the relative variations $d r / r$ and $\bar { d } V / V$ and $\Delta V / V$ :

Solution The job of calculus is to produce the derivative. After $d V / d r = 4 \pi r ^ { 2 }$ , its work is done. The variation in volume is $d V = 4 \pi ( 4 0 0 0 ) ^ { 2 } ( 8 0 )$ cubic miles. A $2 \%$ relative variation in $r$ gives a $6 \%$ relative variation in $V$ :

$$
\frac { d r } { r } = \frac { 8 0 } { 4 0 0 0 } = 2 \% \qquad \frac { d V } { V } = \frac { 4 \pi ( 4 0 0 0 ) ^ { 2 } ( 8 0 ) } { 4 \pi ( 4 0 0 0 ) ^ { 3 } / 3 } = 6 \% .
$$

Without calculus we need the exact volume at $r = 4 0 0 0 + 8 0$ (also at $r = 3 9 2 0 \mathrm { \Omega }$ ):

$$
\frac { \Delta V } { V } = \frac { 4 \pi ( 4 0 8 0 ) ^ { 3 } / 3 - 4 \pi ( 4 0 0 0 ) ^ { 3 } / 3 } { 4 \pi ( 4 0 0 0 ) ^ { 3 } / 3 } \approx 6 . 1 \%
$$

One comment on $d V = 4 \pi r ^ { 2 } d r$ : This is (area of sphere) times (change in radius). It is the volume of a thin shell around the sphere. The shell is added when the radius grows by $d r$ : The exact $\Delta V / V$ is $3 9 1 7 3 1 2 / 6 4 0 0 0 0 \%$ ; but calculus just calls it $6 \%$ :