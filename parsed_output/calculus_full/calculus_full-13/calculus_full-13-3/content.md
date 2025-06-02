# 13.3 1Tangent Planes and Linear Approximations

Over a short range, a smooth curve $y = f ( x )$ is almost straight. The curve changes direction, but the tangent line $y - y _ { 0 } = f ^ { \prime } ( x _ { 0 } ) ( x - x _ { 0 } )$ keeps the same slope forever. The tangent line immediately gives the linear approximation to $y = f ( x )$ W $y \approx y _ { 0 } + f ^ { \prime } ( x _ { 0 } ) ( x - x _ { 0 } )$ :

What happens with two variables? The function is $z = f ( x , y )$ ; and its graph is a surface. We are at a point on that surface, and we are near-sighted. We don’t see far away. The surface may curve out of sight at the horizon, or it may be a bowl or a saddle. To our myopic vision, the surface looks flat. We believe we are on a plane (not necessarily horizontal), and we want the equation of this tangent plane.

Notation The bBase pBoint hasB co oBrdinates $x _ { 0 }$ and $y _ { 0 }$ . The height on  tBhe  sBurface is $z _ { 0 } = f ( x _ { 0 } , y _ { 0 } )$ . Other letters are possible: the point can be $( a , b )$ with height $w$ . The subscript $\mathbf { 0 }$ indicates the value of $x$ or $y$ or $z$ or $\partial f / \partial x$ or $\partial f / \partial y$ at the point.

With one variable the tangent line has slope $d f / d x$ . With two variables there are two derivatives $\partial f / \partial x$ and $\partial f / \partial y$ . At the particular point, they are $( \partial f / \partial x ) _ { 0 }$ and $( \partial f / \partial y ) _ { 0 }$ . Those are the slopes of the tangent plane . Its equation is the key to this chapter:

13A The tangent plane at $( x _ { 0 } , y _ { 0 } , z _ { 0 } )$ has the same slopes as the surface $z = 1$ $f ( x , y )$ : The equation of the tangent plane (a linear equation) is

$$
z - z _ { 0 } = \left( { \frac { \partial f } { \partial x } } \right) _ { 0 } ( x - x _ { 0 } ) + \left( { \frac { \partial f } { \partial y } } \right) _ { 0 } ( y - y _ { 0 } ) .
$$

The normal vector $\mathbf { N }$ to that plane has components $( \partial f / \partial x ) _ { 0 } , ( \partial f / \partial y ) _ { 0 } , - 1 .$

EXAMPLE 1 Find the tangent plane to $z = 1 4 - x ^ { 2 } - y ^ { 2 }$ at $( x _ { 0 } , y _ { 0 } , z _ { 0 } ) = ( 1 , 2 , 9 )$ .

Solution The derivatives are $\partial f / \partial x = - 2 x$ and $\partial f / \partial y = - 2 y$ . When $x = 1$ and $y = 2$ those are $( \partial f / \partial x ) _ { 0 } = - 2$ and $( \partial f / \partial y ) _ { 0 } = - 4$ . The equation of the tangent plane is

$$
z - 9 = - 2 ( x - 1 ) - 4 ( y - 2 ) \qquad { \mathrm { o r } } \qquad z + 2 x + 4 y = 1 9 .
$$

This $z ( x , y )$ has derivatives $^ { - 2 }$ and $^ { - 4 }$ ; just like the surface. So the plane is tangent.

The normal vector $\mathbf { N }$ has components $^ { - 2 , - 4 , - 1 }$ : The equation of the normal line is $( x , y , z ) = ( 1 , 2 , 9 ) + t ( - 2 , - 4 , - 1 ) .$ : Starting from .1; 2; 9/ the line goes out along N—perpendicular to the plane and the surface.

Figure 13.7 shows more detail about the tangent plane. The dotted lines are the $x$ and $y$ tangent lines. They lie in the plane. All tangent lines lie in the tangent plane! These particular lines are tangent to the “partial functions”—where $y$ is fixed at $y _ { 0 } =$ 2 or $x$ is fixed at $x _ { 0 } = 1$ . The plane is balancing on the surface and touching at the tangent point.

More is true. In the surface, every curve through the point is tangent to the plane. Geometrically, the curve goes up to the point and “kisses” the plane. $\dagger$ The tangent $\mathbf { T }$ to the curve and the normal $\mathbf { N }$ to the surface are perpendicular: T $\mathbf { \partial } \cdot \mathbf { N } = 0$ .

EXAMPLE 2 Find the tangent plane to the sphere $z ^ { 2 } = 1 4 - x ^ { 2 } - y ^ { 2 }$ at .1; 2; 3/:

Solution aInstead of $z = 1 4 - x ^ { 2 } - y ^ { 2 }$ we have $z = \sqrt { 1 4 - x ^ { 2 } - y ^ { 2 } }$ : At $x _ { 0 } = 1$ ; $y _ { 0 } = 2$ the heightis now $z _ { 0 } = 3$ a. The surface is a sphere with radius $\sqrt { 1 4 }$ . The only trouble from the square root is its derivatives:

$$
{ \frac { \hat { \sigma } z } { \partial x } } = { \frac { \hat { \sigma } } { \partial x } } { \sqrt { 1 4 - x ^ { 2 } - y ^ { 2 } } } = { \frac { { \frac { 1 } { 2 } } ( - 2 x ) } { \sqrt { 1 4 - x ^ { 2 } - y ^ { 2 } } } } \quad { \mathrm { a n d } } \quad { \frac { \hat { \sigma } z } { \partial y } } = { \frac { { \frac { 1 } { 2 } } ( - 2 y ) } { \sqrt { 1 4 - x ^ { 2 } - y ^ { 2 } } } }
$$

At $( 1 , 2 )$ those slopes are $- { \frac { 1 } { 3 } }$ and $- \textstyle { \frac { 2 } { 3 } }$ : The equation of the tangent plane is linear: $z -$ $\begin{array} { r } { 3 = - \frac { 1 } { 3 } ( x - 1 ) - \frac { 1 } { 3 } ( y - 2 ) } \end{array}$ . I cannot resist improving the equation, by multiplying through by 3 and moving all terms to the left side:

$$
t a n g e n t p l a n e t o \ s p h e r e : \quad 1 ( x - 1 ) + 2 ( y - 2 ) + 3 ( z - 3 ) = 0 .
$$

If mathematics is the “science of patterns,” equation (4) is a prime candidate for study. The numbers 1; 2; 3 appear twice. The coordinates are $( x _ { 0 } , y _ { 0 } , z _ { 0 } ) = ( 1 , 2 , 3 )$ : The normal vector is $1 \mathbf { i } + 2 \mathbf { j } + 3 \mathbf { k }$ : The tangent equation is $1 x + 2 y + 3 z = 1 4$ : None of this can be an accident, but the square root of $1 4 - x ^ { 2 } - y ^ { 2 }$ made a simple pattern look complicated.

This square root is not necessary. Calculus offers a direct way to find $d z / d x$ — implicit differentiation. Just differentiate every termas it stands:

$$
x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = 1 4 \quad { \mathrm { l e a d s ~ t o } } \quad 2 x + 2 z \partial z / \partial x = 0 \quad { \mathrm { a n d } } \quad 2 y + 2 z \partial z / \partial y = 0 .
$$

Canceling the 2’s, the derivatives on a sphere are $- x / z$ and $- y / z$ . Those are the same as in (3). The equation for the tangent plane has an extremely symmetric form:

$$
z - z _ { 0 } = - \frac { x _ { 0 } } { z _ { 0 } } ( x - x _ { 0 } ) - \frac { y _ { 0 } } { z _ { 0 } } ( y - y _ { 0 } ) \mathrm { ~ o r ~ } x _ { 0 } ( x - x _ { 0 } ) + y _ { 0 } ( y - y _ { 0 } ) + z _ { 0 } ( z - z _ { 0 } ) = 0 .
$$

Reading off $\mathbf { N } = x _ { 0 } \mathbf { i } + y _ { 0 } \mathbf { j } + z _ { 0 } \mathbf { k }$ from the last equation, calculus proves something we already knew: The normal vector to a sphere points outward along the radius.

# THE TANGENT PLANE TO $F ( x , y , z ) = c$

The sphere suggests a question that is important for other surfaces. Suppose the equation is $F ( x , y , z ) = c$ instead of $z = f ( x , y )$ : Can the partial derivatives and tangent plane be found directly from $F$ ?

The answer is yes. It is not necessary to solve first for $z$ : The derivatives of $F$ ; computed at $( x _ { 0 } , y _ { 0 } , z _ { 0 } )$ , give a second formula for the tangent plane and normal vector.

Notice how this includes the original case $z = f ( x , y )$ . The function $F$ becomes $f ( x , y ) - z$ : Its partial derivatives are $\partial f / \partial x$ and $\partial f / \partial y$ and $^ { - 1 }$ : (The $^ { - 1 }$ is from the derivative of $- z$ :) Then equation (7) is the same as our original tangent equation (1).

EXAMPLE 3 The surface $F = x ^ { 2 } + y ^ { 2 } - z ^ { 2 } = c$ is a hyperboloid. Find its tangent plane.

Solution The partial derivatives are $F _ { x } = 2 x , F _ { y } = 2 y , F _ { z } = - 2 z$ : Equation (7) is

$$
2 x _ { 0 } ( x - x _ { 0 } ) + 2 y _ { 0 } ( y - y _ { 0 } ) - 2 z _ { 0 } ( z - z _ { 0 } ) = 0 .
$$

We can cancel the $2 \mathrm { { ^ { \circ } s } }$ . The normal vector is $\mathbf { N } = x _ { 0 } \mathbf { i } + y _ { 0 } \mathbf { j } - z _ { 0 } \mathbf { k }$ . For $c > 0$ this hyperboloid has one sheet (Figure 13.8). For $c = 0$ it is a cone and for $c < 0$ it breaks into two sheets (Problem 13.1.26).

# DIFFERENTIALS

Come back to the linear equation $z - z _ { 0 } = ( \partial z / \partial x ) _ { 0 } ( x - x _ { 0 } ) + ( \partial z / \partial y ) _ { 0 } ( y - y _ { 0 } )$ for the tangent plane. That may be the most important formula in this chapter. Move along the tangent plane instead of the curved surface. Movements in the plane are $d x$ and $d y$ and $d z$ —while $\Delta x$ and $\Delta y$ and $\Delta z$ are movements in the surface. The $d$ ’s are governed by thetangent equation—the $\Delta$ ’s are governed by $z = f ( x , y )$ . In Chapter 2 the $d$ ’s were differentials along the tangent line:

$$
d y = ( d y / d x ) d x \ { \mathrm { ~ ( s t r a i g h t ~ l i n e ) ~ a n d ~ } } \ \Delta y \approx ( d y / d x ) \Delta x \ { \mathrm { ~ ( o n ~ t h e ~ c u r v e ) . } }
$$

Now $y$ is independent like $x$ . The dependent variable is $z$ . The idea is the samBe. The dBistances $x - x _ { 0 }$ and $y - y _ { 0 }$ and ${ z - z _ { 0 } }$ (on the tangent plane) are $d x$ and $d y$ and $d z$ . The equation of the plane is

$$
d z = ( \partial z / \partial x ) _ { 0 } d x + ( \partial z / \partial y ) _ { 0 } d y \quad { \mathrm { o r } } \quad d f = f _ { x } d x + f _ { y } d y .
$$

This is the total differential. All letters $d z$ and $d f$ and $d w$ can be used, but $\partial z$ and $\partial f$ are not used. Differentials suggest small movements in $x$ and $y$ ; then $d z$ is the resulting movement in $z$ . On the tangent plane, equation (10) holds exactly.

A “centering transform” has put $x _ { 0 } , y _ { 0 } , z _ { 0 }$ at the center of coordinates. Then the “zoom transform” stretches the surface into its tangent plane.

EXAMPLE 4 The area of a triangle is $\begin{array} { r } { A = \frac { 1 } { 2 } a b \sin { \theta } } \end{array}$ . Find the total differential $d A$ .

Solution BThe base has lengthB $b$ and the sloping sBide has length $a$ . The angle between them is $\theta$ . You may prefer $\begin{array} { r } { A = \frac { 1 } { 2 } b h } \end{array}$ ; where $h$ is the perpendicular height $a \sin \theta$ . Either way we need the partial derivatives. If $\begin{array} { r } { A = \frac { 1 } { 2 } a b \sin { \theta } } \end{array}$ , then

$$
{ \frac { \partial A } { \partial a } } = { \frac { 1 } { 2 } } b \sin \theta \qquad { \frac { \partial A } { \partial b } } = { \frac { 1 } { 2 } } a \sin \theta \qquad { \frac { \partial A } { \partial \theta } } = { \frac { 1 } { 2 } } a b \cos \theta .
$$

These lead immediately to the total differential $d A$ (like a product rule):

$$
d A = { \bigg ( } { \frac { \partial A } { \partial a } } { \bigg ) } d a + { \bigg ( } { \frac { \partial A } { \partial b } } { \bigg ) } d b + { \bigg ( } { \frac { \partial A } { \partial \theta } } { \bigg ) } d \theta = { \frac { 1 } { 2 } } b \sin \theta d a + { \frac { 1 } { 2 } } a \sin \theta d b + { \frac { 1 } { 2 } } a b \cos \theta d \theta .
$$

EXAMPLE 5 The volume of a cylinder is $V = \pi r ^ { 2 } h$ . Decide whether $V$ is more sensitive to a change from $r = 1 . 0$ to $r = 1 . 1$ or from $h = 1 . 0$ to $h = 1 . 1$ .

Solution The partial derivatives are $\partial V / \partial r = 2 \pi r h$ and $\partial V / \partial h = \pi r ^ { 2 }$ . They measure the sensitivity to change. Physically, they are the side area and base area of the cylinder. The volume differential $d V$ comes from a shell around the side plus a layer on top:

$$
d V = { \mathrm { s h e l l } } + { \mathrm { l a y e r } } = 2 \pi r h \ d r + \pi r ^ { 2 } d h . 
$$

Starting from $r = h = 1$ , that differential is $d V = 2 \pi d r + \pi d h$ . With $d r = d h = . 1$ , the shell volume is : $2 \pi$ and the layer volume is only : $1 \pi$ . So $V$ is sensitive to $d r$ .

For a short cylinder like a penny, the layer has greater volume. $V$ is more sensitive to $d h$ . In our case $V = \pi r ^ { \bar { 2 } } h$ increases from $\bar { \pi ( 1 ) ^ { 3 } }$ to $\pi ( 1 . 1 ) ^ { 3 }$ . Compare $\Delta V$ to $d V$ :

$$
\Delta V = \pi ( 1 . 1 ) ^ { 3 } - \pi ( 1 ) ^ { 3 } = . 3 3 1 \pi \qquad \mathrm { a n d } \qquad d V = 2 \pi ( . 1 ) + \pi ( . 1 ) = . 3 0 0 \pi .
$$

The difference is $\Delta V - d V = . 0 3 1 \pi$ . The shell and layer missed a small volume in Figure 13.9, just above the shell and around the layer. The mistake is of order $( d r ) ^ { \tilde { 2 } } + ( d h ) ^ { 2 }$ . For $V = \pi r ^ { 2 } h$ , the differential $d V = 2 \pi r h \ d r + \pi r ^ { 2 } d h$ is a linear approximation to the true change $\Delta V$ . We now explain that properly.

# LINEAR APPROXIMATION

Tangents lead immediately to linear approximations. That is true of tangent planes as it was of tangent lines. The plane stays close to the surface, as the line stayed close to the curve. Linear functions are simpler than $f ( x )$ or $f ( x , y )$ or $F ( x , y , z )$ . All we need are first derivatives at the point. Then the approximation is good near the point. This key idea of calculus is already present in differentials. On the plane, $d f$ equals $f _ { x } d x + f _ { y } d y$ . On the curved surface that is a linear approximationto $\Delta f$ :

13C The linear approximation to $f ( x , y )$ near the point $( x _ { 0 } , y _ { 0 } )$ is

$$
f ( x , y ) \approx f ( x _ { 0 } , y _ { 0 } ) + \left( { \frac { \partial f } { \partial x } } \right) _ { 0 } ( x - x _ { 0 } ) + \left( { \frac { \partial f } { \partial y } } \right) _ { 0 } ( y - y _ { 0 } ) .
$$

In other words $\Delta f \approx f _ { x } \Delta x + f _ { y } \Delta y$ , as proved in Problem 24. The right side of (13) is a linear function $f _ { L } ( x , y )$ . At $( x _ { 0 } , y _ { 0 } )$ , the functions $f$ and $f _ { L }$ have the same slopes. Then $f ( x , y )$ curves away from $f _ { L }$ with an error of “second order:”

$$
| f ( x , y ) - f _ { L } ( x , y ) | \leqslant M [ ( x - x _ { 0 } ) ^ { 2 } + ( y - y _ { 0 } ) ^ { 2 } ] .
$$

This assumes that $f _ { x x } , f _ { x y }$ , and $f _ { y y }$ are continuous and bounded by $M$ along the line from $( x _ { 0 } , y _ { 0 } )$ to $( x , y )$ . Example 3 of Section 13.5 shows that $\vert f _ { t t } \vert \leqslant 2 M$ along that line. A factor $\frac { 1 } { 2 }$ comes from equation 3.8.12, for the error $f - f _ { L }$ with one variable.

For the volume of a cylinder, $r$ and $h$ went from 1.0 to 1.1. The second derivatives of $V = \pi r ^ { 2 } h$ are $V _ { r r } = 2 \pi h$ and $V _ { r h } = 2 \pi r$ and $V _ { h h } = 0$ . They are below $M = 2 . 2 \pi$ . Then (14) gives the error bound $2 . 2 \pi ( . 1 ^ { 2 } + . 1 ^ { 2 } ) = . 0 4 4 \pi$ , not far above the actual error : $0 3 1 \pi$ . The main point is that the error in linear approximation comes from the quadratic terms—those are the first terms to be ignored by $f _ { L }$ .

EXAMPLE 6 Find a linear approximation to the distance function $r = \sqrt { x ^ { 2 } + y ^ { 2 } }$

Solution The partial derivatives are $x / r$ and $y / r$ . Then $\Delta r \approx ( x / r ) \Delta x + ( y / r ) \Delta y$ . For $( x , y , r )$ near $( 1 , 2 , { \sqrt { 5 } } ) \colon { \sqrt { x ^ { 2 } + y ^ { 2 } } } \approx { \sqrt { 1 ^ { 2 } + 2 ^ { 2 } } } + ( x - 1 ) / { \sqrt { 5 } } + 2 ( y - 2 ) / { \sqrt { 5 } } .$ If $y$ is fixed at 2, this is a one-variable approximation to $\sqrt { x ^ { 2 } + 2 ^ { 2 } }$ . If $x$ is fixed at 1, it is a linear approximation in $y$ . Moving both variables, you might think $d r$ would involve $d x$ and $d y$ in a square root. It doesn’t. Distance involves $x$ and $y$ in a square root, but: change of distance is linear in $\Delta x$ and $\Delta y$ —to a first approximation.



There is a rough point at $x = 0 , y = 0$ . Any movement from $( 0 , 0 )$ gives $\Delta r =$ $\sqrt { ( \Delta x ) ^ { 2 } + ( \Delta y ) ^ { 2 } }$ . The square root has returned. The reason is that the partial derivatives $x / r$ and $y / r$ are not continuous at $( 0 , 0 )$ . The cone has a sharp point with no tangent plane. Linear approximation breaks down.

The next example showshowto approximate $\Delta z$ from $\Delta x$ and $\Delta y$ , when the equation is $F ( x , y , z ) = c$ . We use the implicit derivatives in (7) instead of the explicit derivatives in (1). The idea is the same: Look at the tangent equation asa way to find $\Delta z$ , instead of an equation for $z$ . Here is Example 6 with new letters.

EXAMPLE 7 From $F = - x ^ { 2 } - y ^ { 2 } + z ^ { 2 } = 0$ find a linear approximation to $\Delta z$ :

Solution (implicit derivatives) Use the derivatives of $F ; - 2 x \Delta x - 2 y \Delta y + 2 z \Delta z \approx$ 0. Then solve for $\Delta z$ , which gives $\Delta z \approx ( x / z ) \Delta x + ( y / z ) \Delta y$ —the same as Example 6.

EXAMPLE 8 How does the equilibrium price change when the supply curve changes?

The equilibrium price is at the intersection of the supply and demand curves $( s u p p l y = d e m a n d )$ . As the price $p$ rises, the demand $q$ drops (the slope is $- . 2 )$ :

$$
\mathrm { d e m a n d l i n e } D D : p = - . 2 q + 4 0 .
$$

The supply (also $q$ ) goes up with the price. The slope $s$ is positive (here $s = . 4$ /:

$$
\mathrm { s u p p l y ~ l i n e } S S : p = s q + t = . 4 q + 1 0 .
$$

Those lines are in Figure 13.10. They meet at the equilibrium price $P = \$ 30$ . The quantity $Q = 5 0$ is available at $P$ (on $S S$ ) and demanded at $P$ (on $D D$ ). So it is sold.

Where do partial derivatives come in? The reality is that those lines $D D$ and $S S$ are not fixed for all time. Technology changes, and competition changes, and the value of money changes. Therefore the lines move. Therefore the crossing point $( { \boldsymbol { Q } } , { \boldsymbol { P } } )$ also moves. Please recognize that derivatives are hiding in those sentences.

Main point: The equilibrium price $P$ is $\pmb { a }$ function of $s$ and $t$ . Reducing $s$ by better technology lowers the supply line to $p = . 3 q + 1 0$ . The demand line has not changed. The customer is as eager or stingy as ever. But the price $P$ and quantity $\boldsymbol { Q }$ are different. The new equilibrium is at $Q = 6 0$ and $P = \$ 28$ , where the new line $X X$ crosses $D D$ .

If the technology is expensive, the supplier will raise $t$ when reducing $s$ . Line $Y Y$ is $p = . 3 q + 2 0$ . That gives a higher equilibrium $P = \$ 32$ at a lower quantity $Q =$ 40—the demand was too weak for the technology.

Calculus question Find ${ \partial P } / { \partial s }$ and ${ \partial P } / { \partial t }$ . The difficulty is that $P$ is not given as a function of $s$ and $t$ . So take implicit derivatives of the supply $\ c =$ demand equations:

$$
\begin{array} { r l r l r l } { { \mathrm { s u p p l y } } = \mathrm { d e m a n d } : } & { } & { P = - . 2 \mathcal { Q } + 4 0 = s \mathcal { Q } + t } \\ { s \mathrm { ~ d e r i v a t i v e } : } & { } & { P _ { s } = - . 2 \mathcal { Q } _ { s } = s \mathcal { Q } _ { s } + \mathcal { Q } } & & { ( \mathrm { n o t e ~ } t _ { s } = 0 } \\ { t \mathrm { ~ d e r i v a t i v e } : } & { } & { P _ { t } = - . 2 \mathcal { Q } _ { t } = s \mathcal { Q } _ { t } + 1 } & & { ( \mathrm { n o t e ~ } t _ { t } = 1 } \end{array}
$$

Now substitute $s = . 4 , t = 1 0 , P = 3 0 , Q = 5 0 .$ That is the starting point, around which we are finding a linear approximation. The last two equations give $P _ { s } = 5 0 / 3$ and

$P _ { t } = 1 / 3$ (Problem 25). The linear approximation is

$$
P = 3 0 + 5 0 ( s - . 4 ) / 3 + ( t - 1 0 ) / 3
$$

Comment This example turned out to be subtle (so is economics) . I hesitated before including it. The equations are linear and their derivatives are easy, but something in the problem is hard—there is no explicit formula for $P$ . The function $P ( s , t )$ is not known. Instead of a point on a surface, we are following the intersection of two lines. The solution changes as the equation changes.The derivative of the solution comes from the derivative of the equation.

Summary The foundation of this section is equation (1) for the tangent plane. Every thing builds on that—total differential, linear approximation, sensitivity to small change. Later sections go on to the chain rule and “directional derivatives” and “gradients.” The central idea of differential calculus is $\Delta f \approx f _ { x } \Delta x + f _ { y } \Delta y$ .

# NEWTON’S METHOD FOR TWO EQUATIONS

Linear approxi1mation is used to solve equations. To find out where a function is zero, look first to see where its approximation is zero. To find out where a graph crosses the $x y$ plane, look to see where its tangent plane crosses.

Remember Newton’s method for $f ( x ) = 0$ . The current guess is $x _ { n }$ . Around that point, $f ( x )$ is close to $f ( x _ { n } ) + ( x - x _ { n } ) f ^ { \prime } ( x _ { n } ) .$ . This is zero at the next guess $x _ { n + 1 } =$ $x _ { n } - f ( x _ { n } ) / f ^ { \prime } ( x _ { n } )$ . That is where the tangent line crosses the $x$ axis.

With two variables the idea is th eB sa mBe—buttwo unk Bnow Bns $x$ and $y$ require two equations. We solve $g ( x , y ) = 0$ an dB $h ( x , y ) = 0$ .  Both  functions have linear approximations that start from the current point $( x _ { n } , y _ { n } )$ —where derivatives are computed:

$$
\begin{array} { c } { { g ( x , y ) \approx g ( x _ { n } , y _ { n } ) + ( \partial g / \partial x ) ( x - x _ { n } ) + ( \partial g / \partial y ) ( y - y _ { n } ) } } \\ { { h ( x , y ) \approx h ( x _ { n } , y _ { n } ) + ( \partial h / \partial x ) ( x - x _ { n } ) + ( \partial h / \partial y ) ( y - y _ { n } ) . } } \end{array}
$$

The natural idea is to set these approximations to zero. That gives linear equations for $x - x _ { n }$ and $y - y _ { n }$ . Those are the steps $\Delta x$ and $\Delta y$ that take us to the next guess in Newton’s method:

13D Newton’s method to solve $g ( x , y ) = 0$ and $h ( x , y ) = 0$ has linear equations for the steps $\Delta x$ and $\Delta y$ that go from $( x _ { n } , y _ { n } )$ to $( x _ { n + 1 } , y _ { n + 1 } )$ : $\left( { \frac { \partial g } { \partial x } } \right) \Delta x + \left( { \frac { \partial g } { \partial y } } \right) \Delta y = - g ( x _ { n } , y _ { n } ) { \mathrm { a n d ~ } } \left( { \frac { \partial h } { \partial x } } \right) \Delta x + \left( { \frac { \partial h } { \partial y } } \right) \Delta y = - h ( x _ { n } , y _ { n } ) .$ : (19)

EXAMPLE 9 $g = x ^ { 3 } - y = 0$ and $h = y ^ { 3 } - x = 0$ have 3 solutions $( 1 , 1 ) , ( 0 , 0 )$ ;   
$( - 1 , - 1 )$ .

I will start at different points $( x _ { 0 } , y _ { 0 } )$ . The next guess is $x _ { 1 } = x _ { 0 } + \Delta x , y _ { 1 } = y _ { 0 } +$ $\Delta y$ . It is of extreme interest to know which solution Newton’s method will choose—if it converges at all. I made three small experiments.

1: Suppose $( x _ { 0 } , y _ { 0 } ) = ( 2 , 1 )$ . At that point $g = 2 ^ { 3 } - 1 = 7$ and $h = 1 ^ { 3 } - 2 = - 1$ . The derivatives are $g _ { x } = 3 x ^ { 2 } = 1 2 , g _ { y } = - 1 , h _ { x } = - 1 , h _ { y } = 3 y ^ { 2 } = 3$ . The steps $\Delta x$ and $\Delta y$ come from solving (19):

$$
\begin{array} { r } { 1 2 \Delta x - \Delta y = - 7 \quad \quad \Rightarrow \quad \Delta x = - 4 / 7 \quad \Rightarrow \quad x _ { 1 } = x _ { 0 } + \Delta x = 1 0 / 7 } \\ { - \Delta x + 3 \Delta y = + 1 \quad } \end{array}
$$

This new point $( 1 0 / 7 , 8 / 7 )$ is closer to the solution at $( 1 , 1 )$ . The next point is .1:1;   
1:05/ and convergence is clear. Soon convergence is fast.

2: Start at $( x _ { 0 } , y _ { 0 } ) = ( \textstyle { \frac { 1 } { 2 } } , 0 )$ . There we find $g = 1 / 8$ and $h = - 1 / 2$ :

$$
\begin{array} { c c c c c } { ( 3 / 4 ) \Delta x - } & { \Delta y = - 1 / 8 } & { } & { \Delta x = - 1 / 2 } & { } & { x _ { 1 } = x _ { 0 } + \Delta x = 0 } \\ { - \Delta x + 0 \Delta y = + 1 / 2 } & { } & { \Delta y = + 1 / 4 } & { } & { y _ { 1 } = y _ { 0 } + \Delta y = - 1 / 4 . } \end{array}
$$

Newton has jumped from $\textstyle { \left( { \frac { 1 } { 2 } } , 0 \right) }$ on the $x$ axis to $( 0 , - { \frac { 1 } { 4 } } )$ on the $y$ axis. The next step goes to $( 1 / 3 2 , 0 )$ ; back on  the $x$ axis. We are in t he “basin of attraction” of $( 0 , 0 )$ :

3: Now start further out the axis at $( 1 , 0 )$ , where $g = 1$ and $h = - 1$ :

$$
\begin{array} { c c c c c } { 3 \Delta x - \Delta y = - 1 } & & { \Delta x = - 1 } & & { x _ { 1 } = x _ { 0 } + \Delta x = 0 } \\ { - \Delta x + 0 \Delta y = + 1 } & & { \Delta y = - 2 } & & { y _ { 1 } = y _ { 0 } + \Delta y = - 2 . } \end{array}
$$

Newton moves from $( 1 , 0 )$ to $( 0 , - 2 )$ to $( 1 6 , 0 )$ . Convergence breaks down—the method blows up. This danger is ever-present, when we start far from a solution.

Please recognize that even a small computer will uncover amazing patterns. It can start from hundreds of points $( x _ { 0 } , y _ { 0 } )$ , and follow Newton’s method. Each solution has a basin of attraction, containing all $( x _ { 0 } , y _ { 0 } )$ leading to that solution. There is also a basin leading to infinity. The basins in Figure 13.11 are completely mixed together—a color figure shows them as fractals. The most extreme behavior is on the borderline between basins, when Newton can’t decide which way to go. Frequently we see chaos.

Chaos is irregular movement that follows a definite rule. Newton’s method determines an iteration from each point $( x _ { n } , y _ { n } )$ to the next. In scientific problems it normally converges to the solution we want. (We start close enough.) But the computer makes it possible to study iterations from faraway points. This has created a new part of mathematics—so new that any experiments you do are likely to be original.

Section 3.7 found chaos when trying to solve $x ^ { 2 } + 1 = 0$ : But don’t think Newton’s method is a failure. On the contrary, it is the best method to solve nonlinear equations. The error is squared as the algorithm converges, because linear approximations have errors of order $( \Delta x ) ^ { 2 } + ( \Delta y ) ^ { 2 }$ : Each step doubles the number of correct digits, near the solution. The example shows why it is important to be near.