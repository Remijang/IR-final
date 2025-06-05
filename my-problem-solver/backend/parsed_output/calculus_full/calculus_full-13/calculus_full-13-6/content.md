# 13.6 Maxima, Minima, and Saddle Points

The outstanding equation of differential calculus is also the simplest: $d f / d x = 0$ : The slope is zero and the tangent line is horizontal. Most likely we are at the top or bottom of the graph—a maximum or a minimum. This is the point that the engineer or manager or scientist or investor is looking for—maximum stress or production or velocity or profit. With more variables in $f ( x , y )$ and $f ( x , y , z )$ ; the problem becomes more realistic. The question still is: How to locate the maximum and minimum?

The answer is in the partial derivatives. When the graph is level, they are zero. Deriving the equations $f _ { x } = 0$ and $f _ { y } = 0$ is pure mathematics and pure pleasure. Applying them is the serious part. We watch out for saddle points, and also for a minimum at a boundary point—this section takes extra time. Remember the steps for $f ( x )$ in one-variable calculus:

1. The leading candidates are stationary points (where $d f / d x = 0 )$ .   
2. The other candidates are rough points (no derivative) and endpoints $( a { \mathrm { ~ o r ~ } } b )$ ).   
3. Maximum vs. minimum is decided by the sign of the second derivative.

In two dimensions, a stationary point requires $\partial f / \partial x = 0$ and $\partial f / \partial y = 0$ : The tangent line becomes a tangent plane. The endpoints $a$ and $b$ are replaced by a boundary curve. In practice boundaries contain about $40 \%$ of the minima and $80 \%$ of the work.

Finally there are three second derivatives $f _ { x x } , f _ { x y }$ ; and $f _ { y y }$ : They tell how the graph bends away from the tangent plane—up at a minimum, down at a maximum, both ways at a saddle point. This will be determined by comparing $( f _ { x x } ) ( f _ { y y } )$ with $( f _ { x y } ) ^ { 2 }$ :

# STATIONARY POINT $$ HORIZONTAL TANGENT $$ ZERO DERIVATIVES

Suppose $f$ has a minimum at the point $( x _ { 0 } , y _ { 0 } )$ . This may be an absolute minimum or only a local minimum. In both cases $f ( x _ { 0 } , y _ { 0 } ) \leqslant f ( x , y )$ near the point. For an absolute minimum, this inequality holds wherever $f$ is defined. For a local minimum, the inequality can fail far away from $( x _ { 0 } , y _ { 0 } )$ : The bottom of your foot is an absolute minimum, the end of your finger is a local minimum. We assume for now that $( x _ { 0 } , y _ { 0 } )$ is an interior point of the domain of $f .$ At a boundary point, we cannot expect a horizontal tangent and zero derivatives.

Main conclusion: At a minimum or maximum (absolute or local) a nonzero derivative is impossible. The tangent plane would tilt. In some direction $f$ would decrease. Note that the minimum point is $( x _ { 0 } , y _ { 0 } )$ ; and the minimum value is $f ( x _ { 0 } , y _ { 0 } )$

13J If derivatives exist at an interior minimum or maximum, they are zero: $\partial f / \partial x = 0 \quad { \mathrm { a n d } } \quad { \hat { \sigma } } f / { \hat { \sigma } } y = 0 \quad ( t o g e t h e r t h i s i s \operatorname { g r a d } f = \bf { 0 } ) .$ (1) For a function $f ( x , y , z )$ of three variables, add the third equation $\partial f / \partial z = 0$ :

The reasoning goes back to the one-variable case. That is because we look along the lines $x = x _ { 0 }$ and $y = y _ { 0 }$ : The minimum of $f ( x , y )$ is at the point where the lines meet. So this is also the minimum along each line separately.

Moving in the $x$ direction along $y = y _ { 0 }$ ; we find $\partial f / \partial x = 0$ : Moving in the $y$ direction, $\partial f / \partial y = 0$ at the same point. The slope in every direction is zero. In other words grad $f = \mathbf { 0 }$ :

Graphically, $( x _ { 0 } , y _ { 0 } )$ is the low point of the surface $z = f ( x , y )$ : Both cross sections in Figure 13.16 touch bottom. The phrase “if derivatives exist” rules out the vertex of a cone, which is a rough point. The absolute value $f = \left| x \right|$ has a minimum without $d f / d x = 0$ ; and so does the distance $f = r$ : The rough point is $( 0 , 0 )$ :

EXAMPLE 1 Minimize the quadratic $f ( x , y ) = x ^ { 2 } + x y + y ^ { 2 } - x - y + 1 .$ : To locate the minimum (or maximum), set $f _ { x } = 0$ and $f _ { y } = 0$ :

$$
f _ { x } = 2 x + y - 1 = 0 \quad { \mathrm { a n d } } \quad f _ { y } = x + 2 y - 1 = 0 .
$$

Notice what’s important: There are two equations for two unknowns $x$ and $y$ . Since $f$ is quadratic, the equations are linear. Their solution is $\begin{array} { r } { x _ { 0 } = \frac { 1 } { 3 } , y _ { 0 } = \frac { 1 } { 3 } } \end{array}$ (the stationary point). This is actually a minimum, but to prove that you need to read further.

The constant 1 affects the minimum value $\begin{array} { r } { f = \frac { 2 } { 3 } } \end{array}$ —but not the minimum point. The graph shifts up by 1: The linear terms $- x - y$ affect $f _ { x }$ and $f _ { y }$ : They move the minimum away from $( 0 , 0 )$ : The quadratic part $x ^ { 2 } + x y + y ^ { 2 }$ makes the surface curve upwards. Without that curving part, a plane has its minimum and maximum at boundary points.

EXAMPLE 2 (Steiner’s problem) Find the point tahat is nearest to three given points.

This example is worth your attention. We are locating an airport close to three cities. Or we are choosing a house close to three jobs. The problem is to get as near as possible to the corners of a triangle. The best point depends on the meaning of “near.”

The distance to the first corner $( x _ { 1 } , y _ { 1 } )$ is $d _ { 1 } = \sqrt { ( x - x _ { 1 } ) ^ { 2 } + ( y - y _ { 1 } ) ^ { 2 } }$ : The distances to the other corners $( x _ { 2 } , y _ { 2 } )$ and $( x _ { 3 } , y _ { 3 } )$ are $d _ { 2 }$ and $d _ { 3 }$ : Depending on whether cost equals (distance) or .distance/2 or $( d i s t a n c e ) ^ { p }$ , our problem will be:

$$
\begin{array} { r } { M i n i m i z e \quad d _ { 1 } + d _ { 2 } + d _ { 3 } \quad o r \quad d _ { 1 } ^ { 2 } + d _ { 2 } ^ { 2 } + d _ { 3 } ^ { 2 } \quad o r e \nu e n \quad d _ { 1 } ^ { p } + d _ { 2 } ^ { p } + d _ { 3 } ^ { p } . } \end{array}
$$

The second problem is the easiest, when $d _ { 1 } ^ { 2 }$ and $d _ { 2 } ^ { 2 }$ and $d _ { 3 } ^ { 2 }$ are quadratics:

$$
\begin{array} { r l } & { \qquad f ( x , y ) = ( x - x _ { 1 } ) ^ { 2 } + ( y - y _ { 1 } ) ^ { 2 } + ( x - x _ { 2 } ) ^ { 2 } + ( y - y _ { 2 } ) ^ { 2 } + ( x - x _ { 3 } ) ^ { 2 } + ( y - y _ { 3 } ) ^ { 2 } } \\ & { \qquad \partial f / \hat { \sigma } x = 2 [ x - x _ { 1 } + x - x _ { 2 } + x - x _ { 3 } ] = 0 \quad \partial f / \hat { \sigma } y = 2 [ y - y _ { 1 } + y - y _ { 2 } + y - y _ { 3 } ] = 0 . } \end{array}
$$

Solving $\partial f / \partial x = 0$ gives $\begin{array} { r } { x = \frac { 1 } { 3 } ( x _ { 1 } + x _ { 2 } + x _ { 3 } ) } \end{array}$ : Then $\partial f / \partial y = 0$ gives $\begin{array} { r } { y = \frac { 1 } { 3 } } \end{array}$ $( y _ { 1 } + y _ { 2 } + y _ { 3 } )$ : The best point is the centroid of the triangle (Figure 13.17a). It is the nearest point to the corners when the cost is .distance/2: Note how squaring makes the derivatives linear. Least squares dominates an enormous part of applied mathematics.



The real “Steiner problem” is to minimize $f ( x , y ) = d _ { 1 } + d _ { 2 } + d _ { 3 }$ : We are laying down Broad Bs from the corners, with cost proportional to length. The equations $f _ { x } = 0$ and $f _ { y } = 0$ look complicated because of square roots. But the nearest point in Figure 13.17b has a remarkable property, which you will appreciate.

CBalculus takes derivativeBs of $d _ { 1 } ^ { 2 } = ( x - x _ { 1 } ) ^ { 2 } + ( y - y _ { 1 } ) ^ { 2 }$ : The $x$ derivative leaves $2 d _ { 1 } ( \partial d _ { 1 } / \partial x ) = 2 ( x - x _ { 1 } )$ : Divide both sides by $2 d _ { 1 }$ :

$$
{ \frac { \partial d _ { 1 } } { \partial x } } = { \frac { x - x _ { 1 } } { d _ { 1 } } } \quad { \mathrm { a n d } } \quad { \frac { \partial d _ { 1 } } { \partial y } } = { \frac { y - y _ { 1 } } { d _ { 1 } } } \quad { \mathrm { s o } } \quad { \mathrm { g r a d } } d _ { 1 } = \left( { \frac { x - x _ { 1 } } { d _ { 1 } } } , { \frac { y - y _ { 1 } } { d _ { 1 } } } \right) .
$$

This gradient is a unit vector. The sum of $( x - x _ { 1 } ) ^ { 2 } / d _ { 1 } ^ { 2 }$ and $( y - y _ { 1 } ) ^ { 2 } / d _ { 1 } ^ { 2 }$ is $d _ { 1 } ^ { 2 } / d _ { 1 } ^ { 2 } =$ 1: This was already in Section 13.4: Distance increases with slope 1 away from the center. The gradient of $d _ { 1 }$ (call it ${ \bf u } _ { 1 }$ ) is a unit vector from the center point $( x _ { 1 } , y _ { 1 } )$ :

Similarly the gradients of $d _ { 2 }$ and $d _ { 3 }$ are unit vectors ${ \bf u } _ { 2 }$ and ${ \bf u } _ { 3 }$ : They point directly away from the other corners of the triangle. The total cost is $f ( x , y ) = d _ { 1 } + d _ { 2 } + d _ { 3 }$ ; so we add the gradients. The equations $f _ { x } = 0$ and $f _ { y } = 0$ combine into the vector equation

The three unit vectors add to zero! Moving away from one corner brings us closer to another. The nearest point to the three corners is where those movements cancel. This is the meaning of “grad $f = \mathbf { 0 }$ at the minimum.”

It is unusual for three unit vectors to add to zero—this can only happen in one way. The three directions must form angles of $1 2 0 ^ { \circ }$ : The best point has this property, which is repeated in Figure 13.18a. The unit vectors cancel each other. At the “Steiner point,” the roads to the corners make $1 2 0 ^ { \circ }$ angles. This optimal point solves the problem, except for one more possibility.

The other possibility is a minimum at a rough point. The graph of the distance function $d _ { 1 } ( x , y )$ is a cone. It has a sharp point at the center $( x _ { 1 } , y _ { 1 } )$ : All three corners of the triangle are rough points for $d _ { 1 } + d _ { 2 } + d _ { 3 }$ ; so all of them are possible minimizers.

Suppose the angle at a corner exceeds $1 2 0 ^ { \circ }$ : Then there is no Steiner point. Inside the triangle, the angle would become even wider. The best point must be a rough point—one of the corners. The winner is the corner with the wide angle. In the figure that means $d _ { 1 } = 0$ : Then the sum $d _ { 2 } + d _ { 3 }$ comes from the two shortest edges.

Summary The solution is at a $1 2 0 ^ { \circ }$ point or a wide-angle corner. That is the theory.   
The real problem is to compute the Steiner point—which I hope you will do.

Remark 1 Steiner’s problem for four points is surprising. We don’t minimize $d _ { 1 } + d _ { 2 } + d _ { 3 } + d _ { 4 }$ —there is a better problem. Connect the four points with roads, minimizing their total length, and allow the roads to branch. A typical solution is in Figure 13.18c. The angles at the branch points are $1 2 0 ^ { \circ }$ : There are at most two branBch  pBoints (two less thanthe number of corners).

Remark 2 For other powers $p$ ; t hBe cost is $( d _ { 1 } ) ^ { p } + ( d _ { 2 } ) ^ { p } + ( d _ { 3 } ) ^ { p }$ : The $x$ derivative is

$$
\partial f / \partial x = p ( d _ { 1 } ) ^ { p - 2 } ( x - x _ { 1 } ) + p ( d _ { 2 } ) ^ { p - 2 } ( x - x _ { 2 } ) + p ( d _ { 1 } ) ^ { p - 2 } ( x - x _ { 3 } ) .
$$

The key equations are still $\partial f / \partial x = 0$ and $\partial f / \partial y = 0$ : Solving them requires a computer and an algorithm. To share the work fairly, I will supply the algorithm (Newton’s method) if you supply the computer. Seriously, this is a terrific example. It is typical of real problems—we know $\partial f / \partial x$ and $\partial f / \partial y$ but not the point where they are zero. You can calculate that nearest point, which changes as $p$ changes. You can also discover new mathematics, about how that point moves. I will collect all replies I receive to Problems 38 and 39:

# MINIMUM OR MAXIMUM ON THE BOUNDARY

Steiner’s problem had no boundaries. The roads could go anywhere. But most applications have restrictions on $x$ and $y$ ; like $x \geqslant 0$ or $y \leqslant 0$ or $x ^ { 2 } + y ^ { 2 } \geqslant 1$ : The minimum with these restrictions is probably higher than the absolute minimum. There are three possibilities:

.1/ stationary point $f _ { x } = 0 , f _ { y } = 0$ .2/ rough point .3/ boundary point

That third possibility requires us to maximize or minimize $f ( x , y )$ along the boundary.

EXAMPLE 3 Minimize $f ( x , y ) = x ^ { 2 } + x y + y ^ { 2 } - x - y + 1$ in the half-plane $x \geqslant$ 0:

The minimum in Example 1 was $\frac { 2 } { 3 }$ : It occurred at $\begin{array} { r } { x _ { 0 } = \frac { 1 } { 3 } , y _ { 0 } = \frac { 1 } { 3 } } \end{array}$ : This point is still allowed. It satisfies the restriction $x \geqslant 0$ : So the minimum is not moved.

EXAMPLE 4 Minimize the same $f ( x , y )$ restricted to the lower half-plane $y \leqslant 0$ :

Now the absolute minimum at $\bigl ( { \frac { 1 } { 3 } } , { \frac { 1 } { 3 } } \bigr )$ is not allowed. There are no rough points. We look for a minimum on the boundary line $y = 0$ in Figure 13.19a. Set $y = 0$ ; so $f$ depends only on $x$ : Then choose the best $x$ :

$$
f ( x , 0 ) = x ^ { 2 } + 0 - x - 0 + 1 \quad { \mathrm { a n d } } \quad f _ { x } = 2 x - 1 = 0 .
$$

The minimum is at $\begin{array} { r } { x = \frac { 1 } { 2 } } \end{array}$ and $y = 0$ ; where $\textstyle f = { \frac { 3 } { 4 } }$ : This is up from $\frac { 2 } { 3 }$ :

# EXAMPLE 5 Minimize the same $f ( x , y )$ on or outside the circle $x ^ { 2 } + y ^ { 2 } = 1$ :

One possibility is $f _ { x } = 0$ and $f _ { y } = 0$ : But this is at ${ \bigl ( } { \frac { 1 } { 3 } } , { \frac { 1 } { 3 } } { \bigr ) }$ ; inside the circle. The other possibility is a minimum at aboundary point, on the circle.

To follow this boundary we can set $\overset { \cdot } { y } = \sqrt { 1 - x ^ { 2 } }$ : The function $f$ gets complicated, and $d f / d x$ is worse. There is a way to avoid square roots: Set $x = \cos t$ and $y = \sin t$ : Then $f = x ^ { 2 } + x y + y ^ { 2 } - x - y + 1$ is a function of the angle $t$ :

$$
\begin{array} { r l } & { \quad f ( t ) = 1 + \cos t \sin t - \cos t - \sin t + 1 } \\ & { \quad d f / d t = \cos ^ { 2 } t - \sin ^ { 2 } t + \sin t - \cos t = ( \cos t - \sin t ) ( \cos t + \sin t - 1 ) . } \end{array}
$$

Now ${ d f } / { d t } = 0$ locates a minimum or maximum along the boundary. The first factor . $\cos t - \sin t$ / is zero when $x = y$ : The second factor is zero when cos $t + \sin t = 1$ ; or $x + y = 1$ : Those points on the circle are the candidates. Problem 24 sorts them out, and Section 13.7 finds the minimum in a new way—using “Lagrange multipliers.” Minimization on a boundary is a serious problem—it gets difficult quickly—and multipliers are ultimately the best solution.

# MAXIMUM VS. MINIMUM VS. SADDLE POINT

How to separate the maximum from the minimum? When possible, try all candidates and decide. Compute $f$ at every stationary point and other critical point (maybe also out at infinity), and compare. Calculus offers another approach, based on second derivatives.

With one variable the second derivative test was simple: $f _ { x x } > 0$ at a minimum, $f _ { x x } = 0$ at an inflection point, $f _ { x x } < 0$ at a m¡aximum. This¡is a local test, which may not give a global answer. But it decides whether the slope is increasing (bottom of the graph) or decreasing (top of the graph). We now find a similar test for $f ( x , y )$ :

The new test involves all three second derivatives. It applies where $f _ { x } = 0$ and $f _ { y } = 0$ : The tangent plane is horizontal. We ask whether the graph of $f$ goes above or below that plane. The tests $f _ { x x } > 0$ and $f _ { y y } > 0$ guarantee a minimum in the $x$ an dB $y$ direcBtion sB, but there are other directions.

EXAMPLE 6 $f ( x , y ) = x ^ { 2 } + 1 0 x y + y ^ { 2 }$ has $f _ { x x } = 2$ ; $f _ { x y } = 1 0$ ; $f _ { y y } = 2$ (minimum or not?)

All second derivatives are positive—but wait and see. The stationary point is $( 0 , 0 )$ ; where $\partial f / \partial x$ and $\partial f / \partial y$ are both zero. Our function is the sum of $x ^ { 2 } + y ^ { 2 }$ ; which goes upward, and $1 0 x y$ which has a saddle. The second derivatives must decide whether $x ^ { 2 } + y ^ { 2 }$ or $1 0 x y$ is stronger.

Along the $x$ axis, where $y = 0$ and $f = x ^ { 2 }$ ; our point is at the bottom. The minimum in the $x$ direction is at $( 0 , 0 )$ : Similarly for the $y$ direction. But $( 0 , 0 )$ is not $\pmb { a }$ minimum point for the whole function, because of $1 0 x y$ :

Try $x = 1 , y = - 1$ : Then $f = 1 - 1 0 + 1$ ; which is negative. The graph goes below the $x y$ plane in that direction. The stationary point at $x = y = 0$ is a saddle point.

$$
\boxed { 1 + 2 x ^ { 2 } } \times \boxed { 1 + 3 x ^ { 2 } } \times \boxed { 1 + 3 x ^ { 2 } } \boxed { 1 + 3 x ^ { 2 } }
$$

EXAMPLE 7 $f ( x , y ) = x ^ { 2 } + x y + y ^ { 2 }$ has $f _ { x x } = 2 , f _ { x y } = 1 , f _ { y y } = 2$ (minimum or not?)

The second derivatives 2; 1; 2 are again positive. The graph curves up in the $x$ and $y$ directions. But there is a big difference from Example 6: $f _ { x y }$ is reduced from 10 to 1: It is the size of $f _ { x y }$ (not its sign!) that makes the difference. The extra terms $- x - y + 4$ in Example 1 moved the stationary point to ${ \bigl ( } { \frac { 1 } { 3 } } , { \frac { 1 } { 3 } } { \bigr ) }$ : The second derivatives are still 2¡; 1; 2; and they pass the tes t for a minimum:

For a direct proof, split $f ( x , y )$ into two parts by “completing the square:”

$$
a x ^ { 2 } + 2 b x y + c y ^ { 2 } = a \left( x + { \frac { b } { a } } y \right) ^ { 2 } + { \frac { a c - b ^ { 2 } } { a } } y ^ { 2 } .
$$

That algebra can be checked (notice the $2 b$ ). It is the conclusion that’s important:

if $a > 0$ and $a c > b ^ { 2 }$ ; both parts are positive: minimum at $( 0 , 0 )$ if $a < 0$ and $a c > b ^ { 2 }$ ; both parts are negative: maximum at $( 0 , 0 )$ if $a c < b ^ { 2 }$ ; the parts have opposite signs: saddle point at $( 0 , 0 )$ :

Since the test involves the square of $b$ ; its sign has no importance. Example 6 had $b = 5$ and a saddle point.Example 7 had $\begin{array} { r } { \dot { b } = \frac { 1 } { 2 } } \end{array}$ and a minimum. Reversing to $- x ^ { 2 } - x y - y ^ { 2 }$ yields a maximum. So does $- x ^ { 2 } + \overline { { x } } y - y ^ { 2 }$ :

Now comes the final step, from $a x ^ { 2 } + 2 b x y + c y ^ { 2 }$ to a general function $f ( x , y )$ : For all functions, quadratics or not, it is the second order terms that we test.

EXAMPLE 8 $f ( x , y ) = e ^ { x } - x - \cos y$ has a stationary point at $x = 0 , y = 0$ :

The first derivatives are $e ^ { x } - 1$ and sin $y$ ; both zero. The second derivatives are $f _ { x x } = e ^ { x } = 1$ and $f _ { y y } = \cos y = 1$ and $f _ { x y } = 0$ : We only use the derivatives at the stationary point. The first derivatives are zero, so the second order terms come to the front in the series for $e ^ { x } - x - \cos y$ :

$$
( 1 + x + { \textstyle \frac { 1 } { 2 } } x ^ { 2 } + \cdots ) - x - ( 1 - { \textstyle \frac { 1 } { 2 } } y ^ { 2 } + \cdots ) = { \textstyle \frac { 1 } { 2 } } x ^ { 2 } + { \textstyle \frac { 1 } { 2 } } y ^ { 2 } + \mathrm { h i g h e r ~ o r d e r ~ t e r m s } .
$$

There is a minimum at the origin. The quadratic part ${ \textstyle { \frac { 1 } { 2 } } } x ^ { 2 } + { \textstyle { \frac { 1 } { 2 } } } y ^ { 2 }$ goes upward. The $x ^ { 3 }$ and $y ^ { 4 }$ terms are too small to protest. Eventually those terms get large, but near a stationary point it is the quadratic that counts. We didn’t need the whole series, because from $f _ { x x } = f _ { y y } = 1$ and $f _ { x y } = 0$ we knew it would start with ${ \textstyle { \frac { 1 } { 2 } } } x ^ { 2 } + { \textstyle { \frac { 1 } { 2 } } } y ^ { 2 }$ :

13L The test in 13K applies to the second derivatives $a = f _ { x x } , b = f _ { x y } , c = f _ { y y }$ of any $f ( x , y )$ at any stationary point. At all points the test decides whether the graph is concave up, concave down, or “indefinite.”

EXAMPLE 9 $f ( x , y ) = e ^ { x y }$ has $f _ { x } = y e ^ { x y }$ and $f _ { y } = x e ^ { x y }$ : The stationary point is $( 0 , 0 )$ :

The second derivatives at that point are $a = f _ { x x } = 0 , b = f _ { x y } = 1$ ; and $c = f _ { y y } = 0$ : The test $b ^ { 2 } > a c$ makes this a saddle point. Look at the infinite series:

$$
e ^ { x y } = 1 + x y + { \textstyle { \frac { 1 } { 2 } } } x ^ { 2 } y ^ { 2 } + \cdots .
$$

No linear term because $f _ { x } = f _ { y } = 0$ : The origin is a stationary point. No $x ^ { 2 }$ or $y ^ { 2 }$ term (only $x y$ ): The stationary point is a saddle point.

At $x = 2 , y = - 2$ we find $f _ { x x } f _ { y y } > ( f _ { x y } ) ^ { 2 }$ . The graph is concave up at that point—but it’s not a minimum since the first derivatives are not zero.

The series begins with the constant term—not important. Then come the linear terms—extremely important. Those terms are decided by first derivatives, and they give the tangent plane. It is only at stationary points—when the linear part disappears and the tangent plane is horizontal—that second derivatives take over. Around any basepoint, these constant-linear-quadratic terms are the start of the Taylor series.

# THE TAYLOR SERIES

We now put together the whole infinite series. It is a “Taylor series”—which means it is a power series that matches all derivatives of $f$ (at the basepoint). For one variable, the powers were $x ^ { n }$ when the basepoint was 0: For two variables, the powers are $x ^ { n }$ times $y ^ { m }$ when the basepoint is $( 0 , 0 )$ : Chapter 10 multiplied the nth derivative $d ^ { n } f / d x ^ { n }$ by $x ^ { n } / n$ Š Now every mixed derivative $( \hat { \sigma } / \hat { \sigma } x ) ^ { n } ( \hat { \sigma } / \hat { \sigma } y ) ^ { m } f ( x , y )$ is computed at the basepoint (subscript $\mathbf { 0 }$ ).



We multiply those numbers by $x ^ { n } y ^ { m } / n ! m !$ to match each derivative of $f ( x , y )$ :

13M When the baBsepoint is $( 0 , 0 )$ ; the TayBlor series is Ba Bdouble sum $\Sigma \Sigma a _ { n m } x ^ { n } y ^ { m }$ : The term $a _ { n m } x ^ { n } y ^ { m }$ has the same mixed derivative at $( 0 , 0 )$ as $f ( x , y )$ : The seriesBis

$$
\begin{array} { c } { { f ( 0 , 0 ) + x \left( \displaystyle \frac { \partial f } { \partial x } \right) _ { 0 } + y \left( \displaystyle \frac { \partial f } { \partial y } \right) _ { 0 } + \displaystyle \frac { x ^ { 2 } } { 2 } \left( \displaystyle \frac { \partial ^ { 2 } f } { \partial x ^ { 2 } } \right) _ { 0 } + x y \left( \displaystyle \frac { \partial ^ { 2 } f } { \partial x \partial y } \right) _ { 0 } } } \\ { { + \displaystyle \frac { y ^ { 2 } } { 2 } \left( \displaystyle \frac { \partial ^ { 2 } f } { \partial y ^ { 2 } } \right) _ { 0 } + \sum _ { n + m > 2 } \displaystyle \frac { x ^ { n } y ^ { m } } { n ! m ! } \left( \displaystyle \frac { \partial ^ { n + m } f } { \partial x ^ { n } \partial ^ { m } } \right) _ { 0 } . } } \end{array}
$$

The derivatives of this series agree with the derivatives of $f ( x , y )$ at the basepoint.

The first three terms are the linear approximation to $f ( x , y )$ : They give the tangent plane at the basepoint. The $x ^ { 2 }$ term has $n = 2$ and $m = 0$ ; so $n ! m ! = 2$ : The $x y$ term has $n = m = 1$ ; and $n ! m ! = 1$ : The quadratic p art ${ \scriptstyle { \frac { 1 } { 2 } } } ( a x ^ { 2 } + 2 b x y + c y ^ { 2 } )$ is in control when the linear part is zero.

EXAMPLE 10 All derivatives of $e ^ { x + y }$ equal one at the origin. The Taylor series is

$$
e ^ { x + y } = 1 + x + y + { \frac { x ^ { 2 } } { 2 } } + x y + { \frac { y ^ { 2 } } { 2 } } + \cdots = \sum \sum { \frac { x ^ { n } y ^ { m } } { n ! m ! } }
$$

This happens to have $a c = b ^ { 2 }$ ; the special case that was omitted in 13M and 13N. $I t$ is the two-dimensional version of an inflection point. The second derivatives fail to decide the concavity. When $f _ { x x } f _ { y y } = ( f _ { x y } ) ^ { 2 }$ ; the decision is passed up to the higher derivatives. But in ordinary practice, the Taylor series is stopped after the quadratics.

If the basepoint moves to $( x _ { 0 } , y _ { 0 } )$ ; the powers become $( x - x _ { 0 } ) ^ { n } ( y - y _ { 0 } ) ^ { m }$ —and all derivatives are computed at this new basepoint.

Final questionW How would you compute a minimum numerically? One good way is to solve $f _ { x } = 0$ and $f _ { y } = 0$ : These are the functions $g$ and $h$ of Newton’s method (Section 13.3). At the current point $( x _ { n } , y _ { n } )$ ; the derivatives of $g = f _ { x }$ and $h = f _ { y }$ give linear equations for the steps $\Delta x$ and $\Delta y$ : Then the nextpoint $x _ { n + 1 } =$ $x _ { n } + \Delta x , y _ { n + 1 } = y _ { n } + \Delta y$ comes from those steps. The input is $( x _ { n } , y _ { n } )$ ; the output is the new point, and the linear equations are

$$
\begin{array} { c c } { ( g _ { x } ) \Delta x + ( g _ { y } ) \Delta y = - g ( x _ { n } , y _ { n } ) } & { ( f _ { x x } ) \Delta x + ( f _ { x y } ) \Delta y = - f _ { x } ( x _ { n } , y _ { n } ) } \\ { ( h _ { x } ) \Delta x + ( h _ { y } ) \Delta y = - h ( x _ { n } , y _ { n } ) } & { ( f _ { x y } ) \Delta x + ( f _ { y y } ) \Delta y = - f _ { y } ( x _ { n } , y _ { n } ) . } \end{array}
$$

When the sBeco nBd derivatives of $f$ are Bavailable, use Newton’s method.

When the problem is too complicated to go beyond first derivatives, here is an alternative—steepest descent. The goal is to move down the graph of $f ( x , y )$ ; like a boulder rolling down a mountain. The steepest direction at any point is given by the gradient, with a minus sign to go down instead of up. So move in the direction $\Delta x = - s \hat { \sigma } f / \hat { \sigma } x$ and $\Delta y = - s \hat { \sigma } f / \hat { \sigma } y$ :

The question is: How far to move? Like a boulder, a steep start may not aim directly toward the minimum. The stepsize $s$ is monitored, to end the step when the function $f$ starts upward again (Problem 54). At the end of each step, compute first derivatives and start again in the new steepest direction.