# 13.7 Constraints and Lagrange Multipliers

This section faces up to a practical problem. We often minimize one function $f ( x , y )$ while another function $g ( x , y )$ is fixed. There is a constraint on $x$ and $y$ ; given by $g ( x , y ) = k$ : This restricts the material available or the funds available or the energy available. With this constraint, the problem is to do the best possible . $f _ { \mathrm { m a x } }$ or $f _ { \mathrm { m i n } } )$ :

At the absolute minimum of $f ( x , y )$ ; the requirement $g ( x , y ) = k$ is probably violated. In that case the minimum point is not allowed. We cannot use $f _ { x } = 0$ and $f _ { y } = 0$ —those equations don’t account for $g$ :

Step 1 Find equations for the constrained minimum or constrained maximum. They will involve $f _ { x }$ and $f _ { y }$ and also $g _ { x }$ and $g _ { y }$ ; which give local information about $f$ and $g$ : To see the equations, look at two examples.

EXAMPLE 1 Minimize $f = x ^ { 2 } + y ^ { 2 }$ subject to the constraint $g = 2 x + y = k$ :

Trial runs The constraint allows $x = 0 , y = k$ ; where $f = k ^ { 2 }$ : Also $( \textstyle { \frac { 1 } { 2 } } k , 0 )$ satisfies the constraint, and $\textstyle f = { \frac { 1 } { 4 } } k ^ { 2 }$ is smaller. Also $\begin{array} { r } { x = y = \frac { 1 } { 3 } k } \end{array}$ gives $\textstyle f = { \frac { 2 } { 9 } } k ^ { 2 }$ (best so far).

Idea of solution Look at the level curves of $f ( x , y )$ in Figure 13.21. They are circles $x ^ { 2 } + y ^ { 2 } = c$ : When $c$ is small, the circles do not touch the line $2 x + y = k$ : There are no points that satisfy the constraint, when $c$ is too small. Now increase $c$ :

Eventually the growing circles $x ^ { 2 } + y ^ { 2 } = c$ will just touch the line $x + 2 y = k$ : The point where they touch is the winner. It gives the smallest value of $c$ that can be achieved on the line. The touching point is $( x _ { \mathrm { m i n } } , y _ { \mathrm { m i n } } )$ ; and the value of $c$ is $f _ { \mathrm { m i n } }$ :

What equation describes that point? When the circle touches the line, they are tangent. They have the same slope. The perpendiculars to the circle and the line $g o$ in the same direction. That is the key fact, which you see in Figure 13.21a.The direction perpendicular to $f = c$ is given by grad $f = ( f _ { x } , f _ { y } )$ : The direction perpendicular to $g = k$ is given by grad $\boldsymbol { g } = ( g _ { x } , g _ { y } )$ : The key equation says that those two vectors are parallel. One gradient vector is a multiple of the other gradient vector, with a multiplier $\lambda$ (called lambda) that is unknown:

13N At the minimum of $f ( x , y )$ subject to $g ( x , y ) = k$ ; the gradient of $f$ is parallel to the gradient of $g$ —with an unknown number $\lambda$ as the multiplier: $\operatorname { g r a d } f = \lambda \operatorname { g r a d } g \quad \operatorname { s o } \quad { \frac { \partial f } { \partial x } } = \lambda { \frac { \partial g } { \partial x } } \quad { \mathrm { a n d } } \quad { \frac { \partial f } { \partial y } } = \lambda { \frac { \partial g } { \partial y } } .$ (1)

Step 2 There are now three unknowns $x , y , \lambda$ : There are also three equations:

$$
\begin{array}{c} \begin{array} { l } { { \begin{array} { r l } { \partial f / \partial x = \lambda \partial g / \partial x \mathrm { ~ i s ~ } } \end{array} } } & { { \begin{array} { l } { 2 x = 2 \lambda } \\ { 2 y = \lambda } \end{array} } } \\ { { \begin{array} { l } { g ( x , y ) = k \partial g / \partial y \mathrm { ~ i s ~ } } \end{array} } } & { { \begin{array} { l } { 2 y = \lambda } \\ { 2 x + y = k . } \end{array} } } \end{array}  \end{array}
$$

In the third equation, substitute $2 \lambda$ for $2 x$ and ${ \frac { 1 } { 2 } } \lambda$ for $y$ : Then $2 x + y$ equals $\textstyle { \frac { 5 } { 2 } } \lambda$ equals $k$ : Knowing $\lambda = \textstyle { \frac { 2 } { 5 } } k$ ; go back to the first two equations for $x , y$ ; and $f _ { \mathrm { m i n } }$ :

$$
x = \lambda = \frac { 2 } { 5 } k , \quad y = \frac { 1 } { 2 } \lambda = \frac { 1 } { 5 } k , \quad f _ { \mathrm { m i n } } = \left( \frac { 2 } { 5 } k \right) ^ { 2 } + \left( \frac { 1 } { 5 } k \right) ^ { 2 } = \frac { 5 } { 2 5 } k ^ { 2 } = \frac { 1 } { 5 } k ^ { 2 } .
$$

The winning point $( x _ { \mathrm { m i n } } , y _ { \mathrm { m i n } } )$ is $( \textstyle { \frac { 2 } { 5 } } k , \textstyle { \frac { 1 } { 5 } } k )$ . It minimizes the “distance squared,” $\textstyle f = x ^ { 2 } + y ^ { 2 } = { \frac { 1 } { 5 } } k ^ { 2 }$ ; from the origin to the line.

Question What is the meaning of the Lagrange multiplier ?

Mysterious answer The derivative of $\scriptstyle { \frac { 1 } { 5 } } k ^ { 2 } i s \ { \frac { 2 } { 5 } } k$ ; which equals $\lambda$ : The multiplier $\lambda$ is the derivative of $f _ { \mathrm { m i n } }$ with respect to $k$ . Move the line by $\Delta k$ ; and $f _ { \mathrm { m i n } }$ changes by about $\lambda \Delta k$ : Thus the Lagrange multiplier measures the sensitivity to $k$ :

Pronounce his name “Lagronge” or better “Lagrongh” as if you are French.

EXAMPLE 2 Maximize and minimize $f = x ^ { 2 } + y ^ { 2 }$ on the ellipse $g = ( x - 1 ) ^ { 2 } +$ $4 y ^ { 2 } = 4$ :

Idea and equations The circles $x ^ { 2 } + y ^ { 2 } = c$ grow until they touch the ellipse. The touching point is $( x _ { \mathrm { m i n } } , y _ { \mathrm { m i n } } )$ and that smallest value of $c$ is $f _ { \mathrm { m i n } }$ : As the circles grow they cut through the ellipse. Finally there is a point $( x _ { \mathrm { m a x } } , y _ { \mathrm { m a x } } )$ / where the last circle touches. That largest value of $c$ is $f _ { \mathrm { m a x } }$ :

The minimum and maximum are described by the same rule: the circle is tangent to the ellipse (Figure 13.21b). The perpendiculars go in the same direction. Therefore $( f _ { x } , f _ { y } )$ is a multiple of $( g _ { x } , g _ { y } )$ ; and the unknown multiplier is $\lambda$ :

$$
\begin{array} { c c c } { { f _ { x } = \lambda g _ { x } : } } & { { } } & { { 2 x = \lambda 2 ( x - 1 ) \nonumber } } \\ { { f _ { y } = \lambda g _ { y } : } } & { { } } & { { 2 y = \lambda 8 y \nonumber } } \\ { { g = k : } } & { { } } & { { ( x - 1 ) ^ { 2 } + 4 y ^ { 2 } = 4 . } } \end{array}
$$

Solution The second equation allows two possibilities: $y = 0$ or $\textstyle { \lambda = { \frac { 1 } { 4 } } }$ : Following up $y = 0$ ; the last equation gives $( x - 1 ) ^ { 2 } = 4$ : Thus $x = 3$ or $x = - 1$ : Then the first equation gives $\lambda = 3 / 2$ or $\lambda = 1 / 2$ : The values of $f$ a?re $x ^ { 2 } + y ^ { 2 } = 3 ^ { 2 } + 0 ^ { 2 } = 9$ and $x ^ { \bar { 2 } } + y ^ { 2 } = ( - 1 ) ^ { 2 } + { \overset { . } { 0 } } ^ { 2 } = 1$ :

Now follow $\lambda = 1 / 4$ : The first equation yields $x = - 1 / 3$ : Then the last equation requires $y ^ { 2 } = 5 / 9$ : Since $x ^ { 2 } = 1 / 9$ we find $x ^ { 2 } + y ^ { 2 } = 6 / 9 = 2 / 3$ : This is $f _ { \mathrm { m i n } }$ :

Conclusion The equations (3) have four solutions, at which the circle and ellipse are tangent. The four points are $( 3 , 0 ) , ( - 1 , 0 ) , ( - 1 / 3 , \sqrt { 5 } / 3 )$ ; and $( - 1 / 3 , - \dot { \sqrt { 5 } } / 3 )$ : The four values of $f$ are $9 , 1 , { \frac { 2 } { 3 } } , { \frac { 2 } { 3 } }$ :

Summary The three equations are $f _ { x } = \lambda g _ { x }$ and $f _ { y } = \lambda g _ { y }$ and $g = k$ : The unknowns are $x , y$ ; and $\lambda$ : There is no absolute system for solving the equations (unless they are linear; then use elimination or Cramer’s Rule). Often the first two equations yield $x$ and $y$ in terms of $\lambda$ ; and substituting into $g = k$ gives an equation for $\lambda$ :



At the minimB um, the lBevel curve $f ( x , y ) = c$ is tangent to the constraint curve $g ( x , y ) = k$ : If that constraint curve is given parametrically by $x ( t )$ and $y ( t )$ ; then minimizing $f ( x ( t ) , y ( t ) )$ uses the chain rule:

$$
{ \frac { d f } { d t } } = { \frac { \partial f } { \partial x } } { \frac { d x } { d t } } + { \frac { \partial f } { \partial y } } { \frac { d y } { d t } } = 0 \quad { \mathrm { o r } } \quad ( { \mathrm { g r a d ~ } } f ) \cdot ( { \mathrm { t a n g e n t ~ t o ~ c u r v e } } ) = 0 .
$$

This is the calculus proof that grad $f$ is perpendicular to the curve.Thus grad $f$ is parallel to grad $g$ : This means $( f _ { x } , f _ { y } ) = \lambda ( g _ { x } , g _ { y } )$ .

We have lost $f _ { x } = 0$ and $f _ { y } = 0$ : But a new function $L$ has three zero derivatives:

Note that $\partial L / \partial \lambda = 0$ automatically produces $g = k$ : The constraint is “built in” to $L$ : Lagrange has included a term $\lambda ( g - k )$ ; which is destined to be zero—but its derivatives are absolutely needed in the equations! At the solution, $g = k$ and $L = f$ and $\partial L / \partial k = \lambda$ :

What is important is $f _ { x } = \lambda g _ { x }$ and $f _ { y } = \lambda g _ { y }$ ; coming from $L _ { x } = L _ { y } = 0$ : In words: The constraint $g = k$ forces $\begin{array} { r } { d g = g _ { x } d x + g _ { y } d y = 0 } \end{array}$ : This restricts the movements $d x$ and $d y$ : They must keep to the curve. The equations say that $d f = f _ { x } d x + f _ { y } d y$ is equal to $\lambda d g$ : Thus $d f$ is zero in the allowed direction—which is the key point.

# MAXIMUM AND MINIMUM WITH TWO CONSTRAINTS

The whole subject of min(max)imization is called optimization. Its applications to business decisions make up operations research. The special case of linear functions is always important—in this part of mathematics it is called linear programming. A book about those subjects won’t fit inside a calculus book, but we can take one more step—to allow a second constraint.

The function to minimize or maximize is now $f ( x , y , z )$ : The constraints are $g ( x , y , z ) = k _ { 1 }$ and $h ( x , y , z ) = k _ { 2 }$ : The multipliers are $\lambda _ { 1 }$ and $\lambda _ { 2 }$ : We need at least three variables $x , y , z$ because two constraints would completely determine $x$ and $y$ :

Figure $1 3 . 2 2 \mathrm { a }$ shows the geometry behind these equations. For convenience $f$ is $x ^ { 2 } + y ^ { 2 } + z ^ { 2 }$ ; so we are minimizing distance (squared). The constraints $g = x + y +$ $z = 9$ and $h = x + 2 y + 3 z = 2 0$ are linear—their graphs are planes. The constraints keep $( x , y , z )$ on both planes—and therefore on the line where they meet. We are finding the squared distance from $( 0 , 0 , 0 )$ to a line.

What equation do we solve? Thñe level surfaces $x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = c$ are spheres. They grow as $c$ increases. The first sphñere to touch the line is tangent to it. That touching point gives the solution (the smallest $c$ ). All three vectors grad $f ,$ ; grad $g$ ; grad $h$ are perpendicular to the line:

line tangent to sphere $\Rightarrow$ grad $f$ perpendicular to line line in both planes $\Rightarrow$ grad $g$ and grad $h$ perpendicular to line.

Thus grad $f ,$ grad $g$ ; grad $h$ are in the same plane—perpendicular to the line. With three vectors in a plane, grad $f$ is a combination of grad $g$ and grad $h$ :

$$
( f _ { x } , f _ { y } , f _ { z } ) = \lambda _ { 1 } ( g _ { x } , g _ { y } , g _ { z } ) + \lambda _ { 2 } ( h _ { x } , h _ { y } , h _ { z } ) .
$$

This is the key equation (5). It applies to curved surfaces as well as planes.

In (Figure 13.22b), the normals to those planes are grad $g = ( 1 , 1 , 1 )$ and grad $h =$ .1; 2; 3/: The gradient of $f = x ^ { 2 } + y ^ { 2 } + \overline { { z } } ^ { 2 }$ is $( 2 x , 2 y , 2 z )$ : The equations (5)– (6) are

$$
2 x = \lambda _ { 1 } + \lambda _ { 2 } , \quad 2 y = \lambda _ { 1 } + 2 \lambda _ { 2 } , \quad 2 z = \lambda _ { 1 } + 3 \lambda _ { 2 } .
$$

Substitute these $x , y , z$ into the other two equations $g = x + y + z = 9$ and $h = 2 0$ :

$$
\frac { \lambda _ { 1 } + \lambda _ { 2 } } { 2 } + \frac { \lambda _ { 1 } + 2 \lambda _ { 2 } } { 2 } + \frac { \lambda _ { 1 } + 3 \lambda _ { 2 } } { 2 } = 9 \quad \mathrm { a n d } \quad \frac { \lambda _ { 1 } + \lambda _ { 2 } } { 2 } + 2 \frac { \lambda _ { 1 } + 2 \lambda _ { 2 } } { 2 } + 3 \frac { \lambda _ { 1 } + 3 \lambda _ { 2 } } { 2 } = 2 0 .
$$

After multiplying by 2; these simplify to $3 \lambda _ { 1 } + 6 \lambda _ { 2 } = 1 8$ and $6 \lambda _ { 1 } + 1 4 \lambda _ { 2 } = 4 0$ The solutions are $\lambda _ { 1 } = 2$ and $\lambda _ { 2 } = 2$ : Now the previous equations give $( x , y , z ) = ( 2 , 3 , 4 )$ :

The Lagrange function with two constraints is $L ( x , y , z , \lambda _ { 1 } , \lambda _ { 2 } ) = f - \lambda _ { 1 } ( g -$ $k _ { 1 , { \vec { } } }$ / $- \lambda _ { 2 } ( h - k _ { 2 } )$ : Its five derivatives are zero—those are our five equations. Lagrange has increased the number of unknowns from 3 to 5; by adding $\lambda _ { 1 }$ and $\lambda _ { 2 }$ : The best point .2; 3; 4/ gives $f _ { \mathrm { m i n } } = 2 9$ : The $\lambda$ ’s give $\partial f / \partial k$ —the sensitivity to changes in 9 and 20:

INEQUALITY CONSTRAINTS

In practice, applications involve inequalities as well as equations. The constraints might be $g \leqslant k$ and $h \geqslant 0$ : The first means: It is not required to use the whole resource $k$ ; but you cannot use more. The second means: $h$ measures a quantity that cannot be negative. $A t$ the minimum point, the multipliers must satisfy the same inequalities: $\lambda _ { 1 } \leqslant 0$ and $\lambda _ { 2 } \geqslant 0$ :There are inequalities on the $\lambda$ ’s when there are inequalities in the constraints.

Brief reasoning: With $g \leqslant k$ the minimum can be on or inside the constraint curve. Inside the curve, where $g < k$ ; we are free to move in all directions. The constraint is not really constraining. This brings back $f _ { x } = 0$ and $f _ { y } = 0$ and $\lambda = 0$ —an ordinary minimum. On the curve, where $g = k$ constrains the minimum from going lower, we have $\lambda < 0$ : W¥e don’t know in advance which to expect.

For 100 constraints $g _ { i } \leqslant k _ { i }$ ; there are $1 0 0 \lambda$ ’s. Some $\lambda$ ’s are zero (when $g _ { i } < k _ { i }$ ) and some are nonzero (when $g _ { i } = k _ { i }$ ). It is those $2 ^ { 1 0 0 }$ possibilities that make optimization interesting. In linear programming with two variables,¥the constraints are $x \geqslant 0 , y \geqslant 0$ :

EXAMPLE 4 Minimixe $f = 5 x + 6 y$ with $g = x + y = 4$ and $h = x \geqslant 0$ and $\scriptstyle H = y \geqslant$ 0:

The constraint $g = 4$ is an equation, $h$ and $H$ yield inequalities. Each has its own Lagrange multiBplier—anBd the ineqBualities reBquire $\lambda _ { 2 } \geqslant 0$ and $\lambda _ { 3 } \geqslant 0$ : The derivatives of $f , g , h , H$ are no problem to compute:

$$
\begin{array} { r l } & { \displaystyle \frac { \partial f } { \partial x } = \lambda _ { 1 } \frac { \partial g } { \partial x } + \lambda _ { 2 } \frac { \partial h } { \partial x } + \lambda _ { 3 } \frac { \partial H } { \partial x } \quad \mathrm { y i e l d s } \quad 5 = \lambda _ { 1 } + \lambda _ { 2 } } \\ & { \displaystyle \frac { \partial f } { \partial y } = \lambda _ { 1 } \frac { \partial g } { \partial y } + \lambda _ { 2 } \frac { \partial h } { \partial y } + \lambda _ { 3 } \frac { \partial H } { \partial y } \quad \mathrm { y i e l d s } \quad 6 = \lambda _ { 1 } + \lambda _ { 3 } . } \end{array}
$$

Those equations make $\lambda _ { 3 }$ larger than $\lambda _ { 2 }$ : Therefore $\lambda _ { 3 } > 0$ ; which means that the co¥nstraint on $H$ must be an equation. (Inequality for the multiplier means equality for the constraint.) In other words $H = y = 0$ : Then $x + y = 4$ leads to $x = 4$ : The solution is at $( x _ { \mathrm { m i n } } , y _ { \mathrm { m i n } } ) = ( 4 , 0 )$ ; where $f _ { \mathrm { m i n } } = 2 0$ :

At this minimum, $h = x = 4$ is above zero. The multiplier for the constraint $h \geqslant 0$ must be $\lambda _ { 2 } = 0$ : Then the first equation gives $\lambda _ { 1 } = 5$ : As always, the multiplier measures sensitivity.¥When $g = 4$ is increased by $\Delta k$ ; the cost $f _ { \mathrm { m i n } } = 2 0$ is increased by $5 \Delta k$ : In economics $\lambda _ { 1 } = 5$ is called a shadow price—it is the cost of increasing the constraint.

Behind this example is a nice problem in geometry. The constraint curve $x + y = 4$ is a line. The inequalities $x \geqslant 0$ and $y \geqslant 0$ leave a piece of that line—from $P$ to $\boldsymbol { Q }$ in Figure 13.23. The level curves $f = 5 x + 6 y = c$ move out as $c$ increases, until they touch the line. The first touching point is $\mathcal { Q } = ( 4 , 0 )$ ; which is the solution. ${ \mathbf { } } _ { I t }$ is always an endpoint—or a corner of the triangle $P Q R$ : It gives the smallest cost $f _ { \mathrm { m i n } }$ ; which is $c = 2 0$ :