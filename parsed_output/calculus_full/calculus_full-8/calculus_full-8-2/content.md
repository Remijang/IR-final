# 8.2 Length of a Plane Curve

The graph of $y = x ^ { 3 / 2 }$ is a curve in the $x { - } y$ plane. How long is that curve ? A definite integral needs endpoints, and we specify $x = 0$ and $x = 4$ : The first problem is to know what “length function” to integrate.

The distance along a curve is the arc length. To set up an integral, we break the problem into small pieces. Roughly speaking, small pieces of a smooth curve are nearly straight. We know the exact length $\Delta s$ of a straight piece, and Figure 8.8 shows how it comes close to a curved piece.

Here is the unofficial reasoning that gives the length of the curve. A straight piece has $( \Delta s ) ^ { 2 } = ( \Delta x ) ^ { 2 } + ( \Delta y ) ^ { 2 }$ : Within that right triangle, the height $\Delta y$ is the slope $( \Delta y / \Delta x )$ times $\Delta x$ : This secant slope isaclose to the slope of the curve. Thus $\Delta y$ is approximately $( d y / d x ) \Delta x$ :

$$
\Delta s \approx { \sqrt { ( \Delta x ) ^ { 2 } + ( d y / d x ) ^ { 2 } ( \Delta x ) ^ { 2 } } } = { \sqrt { 1 + ( d y / d x ) ^ { 2 } } } \Delta x .
$$

Now add these pieces and make them smaller. The infinitesimal triangle has $( d s ) ^ { 2 } = ( d x ) ^ { 2 } + ( d y ) ^ { 2 }$ : Think of $d s$ as $\sqrt { 1 + ( d y / d x ) ^ { 2 } } d x$ and integrate:

$$
l e n g t h o f c u r \nu e = \int d s = \int \sqrt { 1 + ( d y / d x ) ^ { 2 } } d x .
$$

E?XAMPLE 1 Keep $y = x ^ { 3 / 2 }$ a?nd $\begin{array} { r } { d y / d x = \frac { 3 } { 2 } x ^ { 1 / 2 } } \end{array}$ : Watch out for $\frac { 3 } { 2 }$ and $\frac { 9 } { 4 }$ :

$$
\begin{array} { r } { \mathrm { l e n g t h } = \int _ { 0 } ^ { 4 } \sqrt { 1 + \frac { 9 } { 4 } x } \ d x = \left( \frac { 2 } { 3 } \right) \left( \frac { 4 } { 9 } \right) \left( 1 + \frac { 9 } { 4 } x \right) ^ { 3 / 2 } \biggr ] _ { 0 } ^ { 4 } = \frac { 8 } { 2 7 } ( 1 0 ^ { 3 / 2 } - 1 ^ { 3 / 2 } ) . } \end{array}
$$

This answer is just above 9: A straight line from $( 0 , 0 )$ to $( 4 , 8 )$ has exact length $\sqrt { 8 0 }$ : Note $4 ^ { 2 } + 8 ^ { 2 } = 8 0$ : Since $\sqrt { 8 0 }$ is just below 9; the curve is surprisingly straight.

You may not approve of those numbers (or the reasoning behind them). We can fix the reasoning, but n?othing can be d?one ab?out the numbers. This example $y = x ^ { 3 / 2 }$ had to be chosen carefully to make the integration possible at all. The length integral is difficult because of the square root. In most cases we integrate numerically.

EXAMPLE 2 The straight line $y = 2 x$ from $x = 0$ to $x = 4$ has $d y / d x = 2$ :

$$
\begin{array} { r } { \mathrm { l e n g t h } = \int _ { 0 } ^ { 4 } \sqrt { 1 + 4 } \ d x = 4 \sqrt { 5 } = \sqrt { 8 0 } \ \mathrm { a s \ b e \mathrm { - } f o r e } \qquad \mathrm { ( j u s t \ c h e c k i n g ) . } } \end{array}
$$

We return briefly to the reasoning. The curve is the graph of $y = f ( x )$ : Each piece contains at least one point where secant slope equals tangent slope: $\Delta y / \Delta x = f ^ { \prime } ( c )$ :

The Mean Value Theorem applies when the slope is continuous—this is required for a smooth curve. The straight length $\Delta s$ is exactly $\sqrt { ( \Delta x ) ^ { 2 } + ( f ^ { \prime } ( c ) \Delta x ) ^ { 2 } }$ : Adding the $n$ pieces gives the length of the broken line (close to the curve):

$$
\Delta y = f ^ { \prime } ( c ) \Delta x \overbrace { \int _ { c } \Delta s \ \cdots \int _ { c } \Delta s _ { 2 } } ^ { \Delta x } \qquad \sum _ { i } ^ { n } \Delta s _ { i } = \sum _ { 1 } ^ { n } \sqrt { 1 + [ f ^ { \prime } ( c _ { i } ) ] ^ { 2 } } \Delta x _ { i } .
$$

As $n \to \infty$ and $\Delta x _ { \mathrm { m a x } } \to 0$ this approaches the integral that gives arc length.

$$
\begin{array} { r } { s = \int d s = \int _ { a } ^ { b } { \sqrt { 1 + [ f ^ { \prime } ( x ) ] ^ { 2 } } } d x = \int _ { a } ^ { b } { \sqrt { 1 + ( d y / d x ) ^ { 2 } } } d x . } \end{array}
$$

EXAMPLE 3 Fiand the length of the first quarter of the circle $y = { \sqrt { 1 - x ^ { 2 } } }$ :

Here $d y / d x = - x / \sqrt { 1 - x ^ { 2 } }$ : From Figure $8 . 9 \mathrm { a }$ , the integral goes from $x = 0$ to $x = 1$ :

$$
\mathrm { l e n g t h } = \int _ { 0 } ^ { 1 } { \sqrt { 1 + ( d y / d x ) ^ { 2 } } } d x = \int _ { 0 } ^ { 1 } { \sqrt { 1 + { \frac { x ^ { 2 } } { 1 - x ^ { 2 } } } } } d x = \int _ { 0 } ^ { 1 } { \frac { d x } { \sqrt { 1 - x ^ { 2 } } } } .
$$

The antiderivative is $\sin ^ { - 1 } x$ : It equals $\pi / 2$ at $x = 1$ : This length $\pi / 2$ is a quarter of the full circumference $2 \pi$ :

EXAMPLE 4 Compute the distance around a quarter of the ellipse $y ^ { 2 } + 2 x ^ { 2 } = 2$ :

The equation is $y = { \sqrt { 2 - 2 x ^ { 2 } } }$ and the slope is $d y / d x = - 2 x / \sqrt { 2 - 2 x ^ { 2 } } . \mathrm { S o } \int d$ is

$$
\int _ { 0 } ^ { 1 } { \sqrt { 1 + { \frac { 4 x ^ { 2 } } { 2 - 2 x ^ { 2 } } } } } d x = \int _ { 0 } ^ { 1 } { \sqrt { \frac { 2 + 2 x ^ { 2 } } { 2 - 2 x ^ { 2 } } } } d x = \int _ { 0 } ^ { 1 } { \sqrt { \frac { 1 + x ^ { 2 } } { 1 - x ^ { 2 } } } } d x .
$$

That integral can’t be done in closed form. The length of an ellipse can only be computed numerically. The denominator is zero at $x = 1$ , so a blind application of the trapezoidal rule or Simpson’s rule would give length $= \infty$ : The midpoint rule gives length $= 1 . 9 1$ with thousands of intervals.

# LENGTH OF A CURVE FROM PARAMETRIC EQUATIONS: $x ( f )$ AND $y ( f )$

We have met the unit circle in two forms. One is $x ^ { 2 } + y ^ { 2 } = 1$ : The other is $x = \cos t$ , $y = \sin t$ : Since $\cos ^ { 2 } t + \sin ^ { 2 } t = 1$ , this point goes around the correct circle. One advantage of the “parameter” $t$ is to give extra information—it tells where the point is and also when. In Chapter 1, the parameter was the time and also the angle— because we moved around the circle with speed 1:

Using $t$ is a natural way to give the position of a particle or a spacecraft. We can recover the velocity if we know $x$ and $y$ at every time $t$ : An equation $y = f ( x )$ tells the shape of the path,not the speed along it.

Chapter 12 deals with parametric equations for curves. Here we concentrate on the path length—which allows you to see the idea of a parameter $t$ without too much detail. We give $x$ as a function of $t$ and $y$ as a function of $t$ : The curve is still approximated by straight pieces, and each piece has $( \Delta s ) ^ { 2 } = ( \Delta x ) ^ { 2 } + ( \Delta y ) ^ { 2 }$ : But instead of using $\Delta y \approx ( d y / d x ) \Delta x$ ; we approximate $\Delta x$ and $\Delta y$ separately:

$$
\Delta x \approx ( d x / d t ) \Delta t , \quad \Delta y \approx ( d y / d t ) \Delta t , \quad \Delta s \approx \sqrt { ( d x / d t ) ^ { 2 } + ( d y / d t ) ^ { 2 } } \Delta t .
$$

8B The length of a parametric curve is an integral with respect to $t$ :

$$
\begin{array} { r } { \int d s = \int ( d s / d t ) d t = \int \sqrt { ( d x / d t ) ^ { 2 } + ( d y / d t ) ^ { 2 } } d t . } \end{array}
$$

EXAMPLE 5 Find the length of the quarter-circle using $x = \cos t$ and $y = \sin t$ :

$$
\int _ { 0 } ^ { \pi / 2 } { \sqrt { ( d x / d t ) ^ { 2 } + ( d y / d t ) ^ { 2 } } } d t = \int _ { 0 } ^ { \pi / 2 } { \sqrt { { \sin } ^ { 2 } t + { \cos } ^ { 2 } t } } d t = \int _ { 0 } ^ { \pi / 2 } d t = { \frac { \pi } { 2 } } .
$$

The integral is simpler than $1 / { \sqrt { 1 - x ^ { 2 } } }$ , and there is one new advantage. We can integrate around a whole circle with no trouble. Parametric equations allow a path to close up or?even cross itself. The time $t$ keeps going and the point $( x ( t ) , y ( t ) )$ keeps moving. In contrast, curves $y = f ( x )$ are limited to one $y$ for each $x$ :

EXAMPLE 6 Find the length of the quarter-ellipse: $x = \cos t$ and $y = { \sqrt { 2 } } \sin t$ :

On this path $y ^ { 2 } + 2 x ^ { 2 }$ is $2 \sin ^ { 2 } t + 2 \cos ^ { 2 } t = 2$ (same ellipse). The non-parametric equation $y = { \sqrt { 2 - 2 x ^ { 2 } } }$ comes from eliminating $t$ : We keep $t$ :

$$
\mathrm { l e n g t h } = \int _ { 0 } ^ { \pi / 2 } { \sqrt { ( d x / d t ) ^ { 2 } + ( d y / d t ) ^ { 2 } } } d t = \int _ { 0 } ^ { \pi / 2 } { \sqrt { \sin ^ { 2 } t + 2 \cos ^ { 2 } t } } d t .
$$

This integral (7) must equal (5). If one cannot be done, neither can the other. They are related by $x = \cos t$ , but (7) does not blow up at the endpoints. The trapezoidal rule gives 1:9101 with less than 100 intervals. Section 5.8 mentioned that calculators automatically do a substitution that makes (5) more like (7).

EXAMPLE 7 The path $x = t ^ { 2 }$ , $y = t ^ { 3 }$ goes from $( 0 , 0 )$ to $( 4 , 8 )$ : Stop at $t = 2$ :

To find this path without the parameter $t$ , first solve for $t = x ^ { 1 / 2 }$ : Then substitute into the equation for $y \colon y = t ^ { 3 } = x ^ { 3 / 2 }$ : The non-parametric form (with $t$ eliminated) is the same curve $y = x ^ { 3 / 2 }$ as in Example 1.

The length from the $t$ -integral equals the length from the $x$ -integral. This is Problem 22.

EXAMPLE 8 Special choice of parameter: $t$ is $x$ : The curve becomes $x = t$ , $y = t ^ { 3 / 2 }$

If $x = t$ then $d x / d t = 1$ : The square root in (6) is the same as the square root in (4). Thus the non-parametric form $y = f ( x )$ is a special case of the parametric form—just take $t = x$ :

Compare $x = t$ , $y = t ^ { 3 / 2 }$ with $x = t ^ { 2 }$ , $y = t ^ { 3 }$ : Same curve, same length, different speed.

EXAMPLE 9 Define “speed” by ${ \frac { \mathrm { s h o r t ~ d i s t a n c e } } { \mathrm { s h o r t ~ t i m e } } } = { \frac { d s } { d t } } . \quad \operatorname { I t i s } { \sqrt { \left( { \frac { d x } { d t } } \right) ^ { 2 } + \left( { \frac { d y } { d t } } \right) ^ { 2 } } } .$

When a ball is thrown straight upward, $d x / d t$ is zero. But the speed is not $d y / d t$ : It is $| d y / d t |$ : The speed is positive downward as well as upward.