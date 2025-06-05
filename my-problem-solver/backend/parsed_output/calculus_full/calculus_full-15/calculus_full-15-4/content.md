# 15.4 Surface Integrals

The double integral in Green’s Theorem is over a flat surface $R$ . Now the region moves out of the plane. It becomes a curved surface $S$ , part of a sphere or cylinder or cone. When the surface has only one $z$ for each $( x , y )$ , it is the graph of a function $z ( x , y )$ . In other cases $S$ can twist and close up—a sphere has an upper $z$ and a lower $z$ . In all cases we want to compute area and flux. This is a necessary step (it is our last step) before moving Green’s Theorem to three dimensions.

First a quick review. The basic integrals are $\textstyle \int d x$ and $\iint d x d y$ and $\iiint d x d y d z$ . The one that didn’t fit was $\int d s$ —the length of a curve. When we go from curves to surfaces, $d s$ becomes $d S$ . Area is $\iint d S$ and flux is $\iint \mathbf { F } \cdot \mathbf { n } d S$ , with double integrals because the surfaces are two-dimensional. The main difficulty is in $d S$ .

All formulas are summarized in a table at the end of the section.

There are two ways to deal with $d s$ (along curves). The same methods apply to $d S$ (on surfaces). The first is in $x y z$ coordinates; the second uses parameters. Before this subject gets complicated, I will explain those two methods.

Method 1 is for the graph of a function: curve $y ( x )$ or surface $z ( x , y )$ .

A small piece of the curve is almost straight. It goes across by $d x$ and up by $d y$ :

$$
\operatorname { l e n g t h } d s = { \sqrt { ( d x ) ^ { 2 } + ( d y ) ^ { 2 } } } = { \sqrt { 1 + ( d y / d x ) ^ { 2 } } } d x .
$$

A small piece of the surface is practically flat. Think  Bof a Btiny sloping rectan gBle.  BOne side goes across by $d x$ and up by $( \partial z / \partial x ) d x$ . The neighboring side goes along by $d y$ and up by $( \partial z / \partial y ) d y$ . Computing the area is a linear problem (from Chapter 11), because the flat piece isin a plane.

Two vectors $\mathbf { A }$ and $\mathbf { B }$ form a parallelogram. The length of their cross product is the area. In the present case, the Bvect Borsare $\mathbf { A } = \mathbf { i } + ( \partial z / \partial x ) \mathbf { k }$ and ${ \bf B } = { \bf j } + ( \partial z / \partial y ) { \bf k }$ Then $\mathbf { A } d x$ and $\mathbf { B } d y$ arethe sidesBof  tBhesmall piece, and we compute $\mathbf { A } \times \mathbf { B }$ :

$$
\mathbf { A \times B } = { \left| \begin{array} { l l l } { \mathbf { i } } & { \mathbf { j } } & { \mathbf { k } } \\ { 1 } & { 0 } & { { \hat { \partial } } z / { \hat { \partial } } x } \\ { 0 } & { 1 } & { { \hat { \partial } } z / { \hat { \partial } } y } \end{array} \right| } = - { \hat { \partial } } z / { \hat { \partial } } x \mathbf { i } - { \hat { \partial } } z / { \hat { \partial } } y \mathbf { j } + \mathbf { k } .
$$

This is exac|tly thenorm|al v|ec|tor $\mathbf { N }$ to the tan Bgen tBplane a Bnd  tBhe surface, from Chapter 13. Please note: The small flat piece is actually a parallelogram (not always a rectangle). Its area $d S$ is much like $d s$ , but the length of $\mathbf { N } = \mathbf { A } \times \mathbf { B }$ involves two derivatives:

$$
d S = | \mathbf { A } d x \times \mathbf { B } d y | = | \mathbf { N } | d x d y = { \sqrt { 1 + ( { \hat { \sigma } } z / { \hat { \sigma } } x ) ^ { 2 } + ( { \hat { \sigma } } z / { \hat { \sigma } } y ) ^ { 2 } } } d x d y .
$$

EXAMPLE 1 Find the area on the plane $z = x + 2 y$ above a base area $A$ .

This is the example to visualize. The area down in the $x y$ plane is $A$ . The area up on the sloping plane is greater than $A$ . A roof has more area than the room underneath it. If the roof goes up at a $4 5 ^ { \circ }$ angle, the ratio is $\sqrt { 2 }$ . Formula (3) yields the correct ratio for any surface—including our plane $z = x + 2 y$ .

The derivatives are $\partial z / \partial x = 1$ and $\partial z / \partial y = 2$ . They are constant (planes are easy). The square r oBot i nB (3) contains $1 + 1 ^ { 2 } + 2 ^ { 2 } = 6$ . Therefore $d S = { \sqrt { 6 } } d x d y$ . An area in the $x y$ plane is multiplied by $\sqrt { 6 }$ up in the surface (Figure 15.14a). The vectors A and $\mathbf { B }$ are no longer needed—their work was done when we reached formula (3)—but here they are:

$$
{ \bf A } = { \bf i } + ( \partial z / \partial x ) { \bf k } = { \bf i } + { \bf k } \quad { \bf B } = { \bf j } + ( \partial z / \partial y ) { \bf k } = { \bf j } + 2 { \bf k } \quad { \bf N } = - { \bf i } - 2 { \bf j } + { \bf k } .
$$

The length of $\mathbf { N } = \mathbf { A } \times \mathbf { B }$ is $\sqrt { 6 }$ . The angle between $\mathbf { k }$ and $\mathbf { N }$ has $\cos \theta = 1 / \sqrt { 6 }$ . That is the angle between base plane and sloping plane. Therefore the sloping area is $\sqrt { 6 }$ times the base area. For curved surfaces the idea is the same, except that the square root in $| \mathbf { N } | = 1 / \cos \theta$ changes as we move around the surface.

Method 2 is for curves $x ( t ) , y ( t )$ and surfaces $x ( u , v )$ ; $y ( u , v )$ ; $z ( u , v )$ with parameters.

A curve has one parameter $t$ . A surface has two parameters $u$ and $v$ (it is twodimensional). One advantage of parameters is that $x , y , z$ get equal treatment, instead of picking out $z$ as $f ( x , y )$ . Here are the first two examples:

$$
c o n e x = u \cos v , y = u \sin v , z = u \quad c y l i n d e r x = \cos v , y = \sin v , z = u .
$$

Each choice of $u$ and $v$ gives a point on the surface. By making all choices, we get the complete surface. Notice that a parameter can equal a coordinate, as in $z = u$ . Sometimes both parameters are coordinates, as in $x = u$ and $y = v$ and $z = f ( u , v )$ . That is just $z = f ( x , y )$ in disguise—the surface without parameters. In other cases we find the xyz equation by ealiminating u and $v$ :

$$
\begin{array} { c c c c } { { ( u \cos v ) ^ { 2 } + ( u \sin v ) ^ { 2 } = u ^ { 2 } } } & { { \mathrm { o r } } } & { { x ^ { 2 } + y ^ { 2 } = z ^ { 2 } } } & { { \mathrm { o r } } } & { { z = \sqrt { x ^ { 2 } + y ^ { 2 } } } } \\ { { t e r } } & { { ( \cos v ) ^ { 2 } + ( \sin v ) ^ { 2 } = 1 } } & { { \mathrm { o r } } } & { { x ^ { 2 } + y ^ { 2 } = 1 . } } \end{array}
$$

The cone is the garaph of $f = { \sqrt { x ^ { 2 } + y ^ { 2 } } }$ . The cylinder is not the graph of any function. There is a line of $z ^ { \prime } \mathrm { s }$ through each point on the circle $x ^ { 2 } + y ^ { 2 } = 1$ . That?is what $z = u$ tells us: Give $u$ all values, and you get the whole line. Give $u$ and $v$ all values, and you get the whole cylinder. Parameters allow a surface to close up and even go through itself—which the graph of $f ( x , y )$ can never do.

Actually $z = \sqrt { x ^ { 2 } + y ^ { 2 } }$ gives only the top half of the cone. (A function produces only one $z$ .) The parametric form gives the bottom half also. Similarly $y = { \sqrt { 1 - x ^ { 2 } } }$ gives only the top of a circle, while $x = \cos t$ ; $y = \sin t$ goes all the way around.

Now we find $d S$ , usingBparameBters. Small movemBents giBve a piBece of the surface, practically flat. One side comes from the change $d u$ , the neighboring side comes from $d v$ . The two sides are given by small vectors $\mathbf { A } d u$ and $\mathbf { B } d v$ :

$$
\mathbf { A } = \frac { \partial x } { \partial u } \mathbf { i } + \frac { \partial y } { \partial u } \mathbf { j } + \frac { \partial z } { \partial u } \mathbf { k } \quad \mathrm { a n d } \quad \mathbf { B } = \frac { \partial x } { \partial v } \mathbf { i } + \frac { \partial y } { \partial v } \mathbf { j } + \frac { \partial z } { \partial v } \mathbf { k } .
$$

To find the area $d S$ of the parallelogram, start with the cross product $\mathbf { N } = \mathbf { A } \times \mathbf { B }$ :

$$
\begin{array}{c} \mathbf { N } = \left| \begin{array} { l l l } { \mathbf { i } } & { \mathbf { j } } & { \mathbf { k } } \\ { x _ { u } } & { y _ { u } } & { z _ { u } } \\ { x _ { v } } & { y _ { v } } & { z _ { v } } \end{array} \right| = \left( \frac { \hat { \sigma } y } { \hat { \sigma } u } \frac { \hat { \sigma } z } { \hat { \sigma } v } - \frac { \hat { \sigma } z } { \hat { \sigma } u } \frac { \hat { \sigma } y } { \hat { \sigma } v } \right) \mathbf { i } + \left( \frac { \hat { \sigma } z } { \hat { \sigma } u } \frac { \hat { \sigma } x } { \hat { \sigma } v } - \frac { \hat { \sigma } x } { \hat { \sigma } u } \frac { \hat { \sigma } z } { \hat { \sigma } v } \right) \mathbf { j } + \left( \frac { \hat { \sigma } x } { \hat { \sigma } u } \frac { \hat { \sigma } y } { \hat { \sigma } v } - \frac { \hat { \sigma } y } { \hat { \sigma } u } \frac { \hat { \sigma } x } { \hat { \sigma } v } \right) \mathbf { k } .  \end{array}
$$

Ademittedly this looks complicated—actual examples are often fairly simple. The area $d S$ ofBtheBsmall BpiecBe of surfacBe is $| \mathbf { N } | d u d v$ . The lengtBh $| \mathbf { N } |$ is a BsquBare root:

$$
d S = \sqrt { \left( \frac { \partial y } { \partial u } \frac { \partial z } { \partial v } - \frac { \partial z } { \partial u } \frac { \partial y } { \partial v } \right) ^ { 2 } + \left( \frac { \partial z } { \partial u } \frac { \partial x } { \partial v } - \frac { \partial x } { \partial u } \frac { \partial z } { \partial v } \right) ^ { 2 } + \left( \frac { \partial x } { \partial u } \frac { \partial y } { \partial v } - \frac { \partial y } { \partial u } \frac { \partial x } { \partial v } \right) ^ { 2 } } d u d v .
$$

EXAMPLE 2 Find $\mathbf { A }$ and $\mathbf { B }$ and $\mathbf { N } = \mathbf { A } \times \mathbf { B }$ and $d S$ for the cone and cylinder.

The cone |has $x = u \cos v$ , $y = u$ sinv, $z = u$ . The $u$ derivatives produce $\mathbf { A } = \partial \mathbf { R } / \partial u =$ $\cos v \mathbf { i } + \sin v \mathbf { j } + \mathbf { k }$ . The $v$ derivatives produce the other tangent vector $\mathbf { B } = \partial \mathbf { R } / \partial v =$ $- u \sin v \mathbf { i } + u \cos v \mathbf { j }$ . The normal vector is $\mathbf { A } \times \mathbf { B } = - u \cos v \mathbf { i } - u \sin v \mathbf { j } + u \mathbf { k }$ . Its length gives $d S$ :

$$
d S = | \mathbf { A } \times \mathbf { B } | d u d v = { \sqrt { ( u \cos v ) ^ { 2 } + ( u \sin v ) ^ { 2 } + u ^ { 2 } } } d u d v = { \sqrt { 2 } } u d u d v .
$$

The cylinder is even simpler: $\mathop { d S } = \mathop { d u d v }$ . In these and many other examples, $\mathbf { A }$ is perpendicular to $\mathbf { B }$ . The small piece is a rectangle. Its sides have length $| \mathbf { A } | d u$ and $| \mathbf { B } | d v$ . (The cone has $| \mathbf { A } | = u$ and $| \mathbf { B } | = { \sqrt { 2 } }$ , the cylinder has $| \mathbf { A } | = | \mathbf { B } | = 1 )$ . The cross product is hardly needed for area, when we can just multiply $| \mathbf { A } | d u$ times $| \mathbf { B } | d v$ .

Remark on the two methods Method 1 also used parameters, but a very special choice— $\boldsymbol { \cdot } \boldsymbol { u }$ is $x$ and $v$ is $y$ . The parametric equations are $x = x$ , $y = y$ , $z = f ( x , y )$ . If you go through the long square root in (7), changing $u$ to $x$ and $v$ to $y$ , it simplifies to the square root in (3). (The terms $\partial y / \partial x$ and $\partial x / \partial y$ are zero; $\partial x / \partial x$ and $\partial y / \partial y$ are 1.) Still it pays to remember the shorter formula from Method 1.

Don’|t forget tha|t after |computing $d S$ , you have to integrate it. Many times the good is with polar coordinates. Surfaces are often symmetric around an axis or a point. Those are the surfaces of revolution—which we saw in Chapter 8 and will come back to.

Strictly speaking, the integral starts with $\Delta S$ (not $d S$ ). A flat piece has area $\mathbf { \left| A \times B \right| } \Delta x \Delta y$ or $\mathbf { \left| A \times B \right| } \Delta u \Delta v$ . The area of a curved surface is properly defined as a limit. The key step of calculus, from sums of $\Delta S$ to the integral of $d S$ , is safe for smooth surfaces. In examples, the hard part is computing the double integral and substituting the limits on $x , y$ or $u , v$ .



EBXAMPLE 3 Find theB surface area of the cone $z = \sqrt { x ^ { 2 } + y ^ { 2 } }$ up to the height $z = a$ .   
We use Method 1 (no parameters). The derivatives of $z$ are computed, squared, and added:

$$
{ \frac { \partial z } { \partial x } } = { \frac { x } { \sqrt { x ^ { 2 } + y ^ { 2 } } } } \qquad { \frac { \partial z } { \partial y } } = { \frac { y } { \sqrt { x ^ { 2 } + y ^ { 2 } } } } \qquad | \mathbf { N } | ^ { 2 } = 1 + { \frac { x ^ { 2 } } { x ^ { 2 } + y ^ { 2 } } } + { \frac { y ^ { 2 } } { x ^ { 2 } + y ^ { 2 } } } = 2 .
$$

Conclusion: $| \mathbf { N } | = { \sqrt { 2 } }$ and $d S = \sqrt { 2 } d x d y$ . The cone is on a $4 5 ^ { \circ }$ slope, so the area $d x d y$ in the base is multiplied by $\sqrt { 2 }$ in the surface above it (Figure 15.15). The square root in $d S$ accounts for the extra area due to slope. A horizontal surface has $\dot { d S } = \sqrt { 1 } d x d y$ , as we have known all year.

Now for a key point. The integration is down in the base plane. The limits on $x$ and $y$ are given by the “shadow” of the cone. To locate that shadow set $z =$ $\sqrt { x ^ { 2 } + y ^ { 2 } }$ equal to $z = a$ . The plane cuts the c?one at the circle $x ^ { 2 } + y ^ { 2 } = a ^ { 2 }$ . We integrate over the inside of that circle (where the shadow is):

$$
{ \mathrm { s u r f a c e ~ a r e a ~ o f ~ c o n e } } = \iint ~ { \sqrt { 2 } } d x d y = { \sqrt { 2 } } \pi a ^ { 2 } .
$$

EXAMPLE 4 Find the same area using $d S = { \sqrt { 2 } } u d u d v$ from Example 2.

With parameters, $d S$ looks different and the shadow in the base looks different. The circle $x ^ { 2 } + y ^ { 2 } = a ^ { 2 }$ becomes $u ^ { 2 } \cos ^ { 2 } v + u ^ { 2 } \sin ^ { 2 } v = a ^ { 2 }$ . In other?words $u = a$ . (The cone has $z = u$ , the plane has $z = a$ , they meet when $u = a$ .) The angle parameter $v$ goes from 0 to $2 \pi$ . The effect of these parameters is to switch us “automatically” to polar coordinates, where area is $r d r d \theta$ :

$$
{ \mathrm { s u r f a c e ~ a r e a ~ o f ~ c o n e } } = \int \int d S = \int \int { \int { \sqrt { 2 } } u d u d v } = { \sqrt { 2 } } \pi a ^ { 2 } .
$$

EXAMPLE 5 Find the area of the same cone up to the sloping plane $\begin{array} { r } { z = 1 - \frac { 1 } { 2 } x } \end{array}$ .

Solution The cone still has $d S = \sqrt { 2 } d x d y$ , but the limits of integration are changed. The plane cuts the cone in an ellipse. Its shadow down in the $x y$ plane is another

ellipse (Figure 15.15c). To find the edge of the shadow, set $z = { \sqrt { x ^ { 2 } + y ^ { 2 } } }$ equal to $\begin{array} { r } { z = 1 - \frac { 1 } { 2 } x } \end{array}$ . We square both sides:

$$
x ^ { 2 } + y ^ { 2 } = 1 - x + { \frac { 1 } { 4 } } x ^ { 2 } \qquad { \mathrm { o r } } \qquad { \frac { 3 } { 4 } } ( x + { \frac { 2 } { 3 } } ) ^ { 2 } + y ^ { 2 } = { \frac { 4 } { 3 } } .
$$

This is the ellipse in the base—where h?eight makes no difference and $z$ is gone. The area of an ellipse is $\pi a b$ , when the equation is in the form $( x / a ) ^ { 2 } + ( y / b ) ^ { 2 } = 1$ . After multiplying by $3 / 4$ we find $a = 4 / 3$ and $b = { \sqrt { 4 / 3 } }$ . Then $\iint { \sqrt { 2 } } d x d y =$ ${ \sqrt { 2 } } \pi a b$ is the surface area of the cone.

The hard part was finding the shadow ellipse (I went quickly). Its area $\pi a b$ came from Example 15:3:2. The new part is $\sqrt { 2 }$ from the slope.

EXAMPLE 6 Find the surface area of a sphere of radius $a$ (known to be $4 \pi a ^ { 2 }$ ).

This is a good example, because both methods almost work. The equation of the sphere is $x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = a ^ { 2 }$ . Method 1 writes $z = \sqrt { a ^ { 2 } - x ^ { 2 } - y ^ { 2 } }$ . The $x$ and $y$ derivatives are $- x / z$ and $- y / z$ :

$$
1 + \left( { \frac { \partial z } { \partial x } } \right) ^ { 2 } + \left( { \frac { \partial z } { \partial y } } \right) ^ { 2 } = { \frac { z ^ { 2 } } { z ^ { 2 } } } + { \frac { x ^ { 2 } } { z ^ { 2 } } } + { \frac { y ^ { 2 } } { z ^ { 2 } } } = { \frac { a ^ { 2 } } { z ^ { 2 } } } = { \frac { a ^ { 2 } } { a ^ { 2 } - x ^ { 2 } - y ^ { 2 } } } .
$$

The square root gives $d S = a d x d y / \sqrt { a ^ { 2 } - x ^ { 2 } - y ^ { 2 } }$ . Notice that $z$ is gone (as it should be). Now integrate $d S$ over the shadow of the sphere, which is a circle. Instead of $d x d y$ , switch to polar coordinates and $r d r d \theta$ :

$$
\int _ { \mathrm { s h a d o w } } d S = \int _ { 0 } ^ { 2 \pi } \int _ { 0 } ^ { a } { \frac { a r d r d \theta } { \sqrt { a ^ { 2 } - r ^ { 2 } } } } { = } - 2 \pi a \sqrt { a ^ { 2 } - r ^ { 2 } } \big ] _ { 0 } ^ { a } { = } 2 \pi a ^ { 2 } .
$$

This calculation is successful but wrong. $2 \pi a ^ { 2 }$ is the area of the half-sphere above the $x y$ plane. The lower half takes the negative square root of $z ^ { 2 } = \overset { \cdot } { a ^ { 2 } } - x ^ { 2 } - y ^ { 2 }$ . This shows the danger of Method 1, when the surface is not the graph of a function.

EXAMPLE 7 (same sphere by Method 2: use parameters) The natural choice is s pBher iBcal c Boor dBinates.  BEve rBy po iBnt h Bas an angl e $u = \phi$ down from the North Pole and an angle $v = \theta$ around the equator. The $x y z$ coordinates from Section 14.4 are $x = a \sin \phi \cos \theta , \ y = a \sin \phi \sin \theta , \ z = a \cos \phi$ . The radius $\rho = a$ is fixed (not a parameter). Compute the first term in equation (6), noting $\partial z / \partial \theta = 0$ :

$$
( { \hat { \sigma } } y / { \hat { \sigma } } \phi ) ( { \hat { \sigma } } z / { \hat { \sigma } } \theta ) - ( { \hat { \sigma } } z / { \hat { \sigma } } \phi ) ( { \hat { \sigma } } y / { \hat { \sigma } } \theta ) = - ( - a \sin \phi ) ( a \sin \phi \cos \theta ) = a ^ { 2 } \sin ^ { 2 } \phi \cos \theta .
$$

The other terms in (6) are $a ^ { 2 } \sin ^ { 2 } \phi \sin \theta$ and $a ^ { 2 } \sin \phi \cos \phi$ . Then $d S$ in equation (7) squares these three components and adds. We factor out $a ^ { 4 }$ and simplify:

$$
a ^ { 4 } ( \sin ^ { 4 } \phi \cos ^ { 2 } \theta + \sin ^ { 4 } \phi \sin ^ { 2 } \theta + \sin ^ { 2 } \phi \cos ^ { 2 } \phi ) = a ^ { 4 } ( \sin ^ { 4 } \phi + \sin ^ { 2 } \phi \cos ^ { 2 } \phi ) = a ^ { 4 } \sin ^ { 2 } \phi .
$$

Conclusion: $d S = a ^ { 2 } \sin \phi d \phi d \theta$ . A spherical person will recognize this immediately. It is the volume element $d V = \rho ^ { 2 } \sin \phi d \rho d \phi d \theta$ , except $d \rho$ is missing. The small box has area $d S$ and thickness $d \rho$ and volume $d V$ . Here we only want $d S$ :

$$
{ \mathrm { a r e a ~ o f ~ s p h e r e } } = \int \int d S = \int _ { 0 } ^ { 2 \pi } \int _ { 0 } ^ { \pi } a ^ { 2 } \sin \phi d \phi d \theta = 4 \pi a ^ { 2 } .
$$

Figure 15.16a shows a small surface with sides a $d \phi$ and $a \ \sin \phi d \theta$ . Their product is $d S$ . Figure 15.16b goes back to Method 1, where equation (8) gave $d S =$ $( a / z ) d x d y$ .

I doubt that you will like Figure 15.16c—and you don’t need it. With parameters $\phi$ and $\theta$ , the shadow of the sphere is a rectangle. The equator is the line down the middle, where $\phi = \pi / 2$ . The height is $z = a \cos \phi$ . The area $d \phi d \theta$ in the base is the shadow of $d S = a ^ { 2 } \sin \phi d \phi d \theta$ up in the sphere. Maybe this figure shows what we don’t halve to know about parameters.

EXAMPLE 8 Rotate $y = x ^ { 2 }$ around the $x$ axis. Find the surface area using parametears.

The first parameter is $x$ (from $a$ to $b$ ). The second parameter is the rotation angle $\theta$ (from 0 to $2 \pi$ ). The points on the surface in Figure 15.17 are $x = x$ , $y = x ^ { 2 } \cos \theta$ , $z = x ^ { 2 } \sin \theta$ . Equation (7) leads after much calculation to $d S = x ^ { 2 } { \sqrt { 1 + 4 x ^ { 2 } } } d x d \theta$ . Main point: $d S$ agrees with Section 8.3, where the area was $\int 2 \pi y$ $\sqrt { 1 + ( d y / d x ) ^ { 2 } } d x$ . The $2 \pi$ comes from the $\theta$ integral and $y$ is $x ^ { 2 }$ . Parameters give this formula automatically.

# VECTOR FIELDS AND THE INTEGRAL OF F n

Formulas for surface area are dominated by square roots. There is a square root in $d S$ , as there was in $d s$ . Areas are like arc lengths, one dimension up. The good point about line integrals $\int \mathbf { F } \cdot \mathbf { n } d s$ is that the square root disappears. It is in the denominator of $\mathbf { n }$ , where $d s$ cancels it: $\mathbf { F } \cdot \mathbf { n } d s = M d y - N d x$ . The same good thing will now happen for surface integrals $\int \int \mathbf { F } \cdot \mathbf { n } d S$ .

This formula tells what to integrate, given the surface and the vector field $f$ and $\mathbf { F }$ ). The $x y$ limits come from the shadow. Formula (10) takes the normal vector from Method 1:

$$
{ \bf N } = - \partial f / \partial x { \bf i } - \partial f / \partial y { \bf j } + { \bf k } \mathrm { a n d } | { \bf N } | = \sqrt { 1 + ( \partial f / \partial x ) ^ { 2 } + ( \partial f / \partial y ) ^ { 2 } } .
$$

For the unit normal vector $\mathbf { n }$ , divide $\mathbf { N }$ by its length: $\mathbf { n } { = } \mathbf { N } / | \mathbf { N } |$ . The square root is in the denominator, and the same square root is in $d S$ . See equation (3):

$$
\mathbf { F } \cdot \mathbf { n } d S = { \frac { \mathbf { F } \cdot \mathbf { N } } { \sqrt { \mathbf { \alpha } } } } { \sqrt { \mathbf { \alpha } } } d x d y = \left( - M { \frac { \partial f } { \partial x } } - N { \frac { \partial f } { \partial y } } + P \right) d x d y .
$$

That is formula (10), with cancellation of square roots. The expression $\mathbf { F } \cdot \mathbf { n } d S$ is often written as $\mathbf { F } \cdot d \mathbf { S }$ , again relying on boldface to make $d \mathbf { S }$ a vector. Then $d \mathbf { S }$ equals $\mathbf { n } d S$ , with direction $\mathbf { n }$ and magnitude $d S$ .

EXAMPLE 9 Find ndS for the plane $z = x + 2 y$ . Then find $\mathbf { F } { \cdot } \mathbf { n } d S$ for $\mathbf { F } = \mathbf { k }$ . This plane produced $\sqrt { 6 }$ in Example 1 (for area). For flux the $\sqrt { 6 }$ disappears:

$$
{ \mathbf { n } } d S = { \frac { \mathbf { N } } { | \mathbf { N } | } } d S = { \frac { - \mathbf { i } - 2 \mathbf { j } + \mathbf { k } } { \sqrt { 6 } } } { \sqrt { 6 } } d x d y = ( - \mathbf { i } - 2 \mathbf { j } + \mathbf { k } ) d x d y .
$$

For the flow field $\mathbf { F } = \mathbf { k }$ , the dot product $\mathbf { k } \cdot \mathbf { n } d S$ reduces to $1 d x d y$ . Thae slope of the plane makes no difference! The flow through the base also flows through the plane. The areas are different, but flux is like rain. Whether it hits a tent or the ground below, it is thesame rain (Figurea15.18). In this case $\textstyle \iint \mathbf { F } \cdot \mathbf { n } d S = \iint d x d y =$ shadow area in the base.

EXAMPLE 10 Find the flux of $\mathbf { F } = x \mathbf { i } + y \mathbf { j } + z \mathbf { k }$ through the cone $z = \sqrt { x ^ { 2 } + y ^ { 2 } }$ .

$$
\mathbf { F } \cdot \mathbf { n } d S = \left[ - x \left( { \frac { x } { \sqrt { x ^ { 2 } + y ^ { 2 } } } } \right) - y \left( { \frac { y } { \sqrt { x ^ { 2 } + y ^ { 2 } } } } \right) + { \sqrt { x ^ { 2 } + y ^ { 2 } } } \right] d x d y =
$$

The zero comes as a surprise, but it shouldn’t. The cone goes straight out from the origin, and so does $\mathbf { F }$ . The vector $\mathbf { n }$ that is perpendicular to the cone is also perpendicular to $\mathbf { F }$ . There is no flow through the cone, because $\mathbf { F } \cdot \mathbf { n } = 0$ . The flow travels out along rays.

In Example 10 the cone was $z = f ( x , y ) = \sqrt { x ^ { 2 } + y ^ { 2 } }$ . We found $d S$ by Method 1. Parameters were not needed (more exactly, they were $x$ and $y$ ). For surfaces that fold and twist, the formulas with $u$ and $v$ look complicated but the actual calculations can be simpler. This was certainly the case for $\mathop { d S } = \mathop { d u } \mathop { d v }$ on the cylinder.

A small piece of surface has area $d S = | \mathbf { A } \times \mathbf { B } | d u d v$ . The vectors along the sides are $\mathbf { A } = x _ { u } \mathbf { i } + y _ { u } \mathbf { j } + z _ { u } \mathbf { k }$ and $\mathbf { B } = \mathbf { x } _ { v } \mathbf { i } + y _ { v } \mathbf { j } + z _ { v } \mathbf { k }$ . They are tangent to the surface.

# 15.4 Surface Integrals

Now we put their cross product $\mathbf { N } = \mathbf { A } \times \mathbf { B }$ to another use, because $\mathbf { F } \cdot \mathbf { n } d S$ involves not only area but direction. We need the unit vector $\mathbf { n }$ to see how much flow goes through.

The direction vector is $\mathbf { n } { = } \mathbf { N } / | \mathbf { N } |$ . Equation (7) is $\mathop { d S } = | \mathbf { N } | \mathop { d u } \mathop { d v }$ , so the square root $| \mathbf { N } |$ cancels in ndS. This leaves a nice formula for the “normal component” of flow:

EXAMPLE 11 Find the flux of $\mathbf { F } = x \mathbf { i } + y \mathbf { j } + z \mathbf { k }$ through the cylinder $x ^ { 2 } + y ^ { 2 } =$ $1 , 0 \leqslant z \leqslant b$ .

Solution The surface of the cylinder is $x = \cos u$ , $y = \sin u$ , $z = v$ . The tangent vectors from (5) are $\mathbf { A } = ( - \sin u ) \mathbf { i } + ( \cos u ) \mathbf { j }$ and $\mathbf { B } = \mathbf { k }$ . The normal vector in Figure 15.19 goes straight out through the cylinder:

$$
\mathbf { N } = \mathbf { A } \times \mathbf { B } = \cos u \mathbf { i } + \sin u \mathbf { j } \qquad ( \mathrm { c h e c k } \ \mathbf { A } \cdot \mathbf { N } = 0 \ \mathrm { a n d } \ \mathbf { B } \cdot \mathbf { N } = 0 ) .
$$

To find $\mathbf { F } \cdot \mathbf { N }$ , switc»h $\mathbf { F } = x \mathbf { i } + y \mathbf { j } + z \mathbf { k }$ to the parameters $u$ and $v$ . Then $\mathbf { F } \cdot \mathbf { N } = 1$ :

$$
\mathbf { F } \cdot \mathbf { N } = ( \cos u \mathbf { i } + \sin u \mathbf { j } + v \mathbf { k } ) \cdot ( \cos u \mathbf { i } + \sin u \mathbf { j } ) = \cos ^ { 2 } u + \sin ^ { 2 } u .
$$

For the flux, integrate $\mathbf { F } \cdot \mathbf { N } = 1$ and apply the limits on $u = \theta$ and $v = z$ :

$$
\mathrm { { f u x } } = \int _ { 0 } ^ { b } \int _ { 0 } ^ { 2 \pi } 1 d u d v = 2 \pi b = \mathrm { { s u r f a c e \ a r e a \ o f \ t h e \ c y l i n d e r . } }
$$

Note that the top and bottom were not included! We can find those fluxes too. The outward direction is $\mathbf { n } = \mathbf { k }$ at the top and $\mathbf { n } = - \mathbf { k }$ down through the bottom. Then $\mathbf { F } \cdot \mathbf { n }$ is $+ z = b$ at the top and $- z = 0$ at the bottom. The bottom flux is zero, the top flux is $b$ times the area (or $\pi b$ ). The total flux is $2 \pi b + \pi b = 3 \pi b .$ . Hold that answer for the next section.

Apology: I made $u$ the angle and $v$ the height. Then $\mathbf { N }$ goes outward not inward.

EXAMPLE 12 Find the flux of $\mathbf { F } = \mathbf { k }$ out the top half of the sphere $x ^ { 2 } + y ^ { 2 } + z ^ { 2 } =$ a2.

Solution Use spherical coordinates. Example 7 had $u = \phi$ and $v = \theta$ . We found

$$
\mathbf { N } = \mathbf { A } \times \mathbf { B } = a ^ { 2 } \sin ^ { 2 } \phi \cos \theta \ { \mathbf { i } } + a ^ { 2 } \sin ^ { 2 } \phi \sin \theta \ { \mathbf { j } } + a ^ { 2 } \sin ^ { 2 } \phi \cos \phi \ { \mathbf { k } } .
$$

The dot product with $\mathbf { F } = \mathbf { k }$ is $\mathbf { F } \cdot \mathbf { N } = a ^ { 2 } \sin \phi \cos \phi$ . The integral goes from the pole to the equator, $\phi = 0$ to $\phi = \pi / 2$ , and around from $\theta = 0$ to $\theta = 2 \pi$ :

$$
\mathrm { f l u x } = \int _ { 0 } ^ { 2 \pi } \int _ { 0 } ^ { \pi / 2 } { a ^ { 2 } \sin \phi \cos \phi d \phi d \theta } = 2 \pi a ^ { 2 } { \frac { \sin ^ { 2 } \phi } { 2 } } \Biggr ] _ { 0 } ^ { \pi / 2 } = \pi a ^ { 2 } .
$$

The next section will show that the flux remains at $\pi a ^ { 2 }$ through any surface (!) that is bounded by the equator. A special case is a flat surface—the disk of radius $a$ at the equator. Figure 15.18 shows $\mathbf { n } = \mathbf { k }$ pointing directly up, so $\mathbf { F } \cdot \mathbf { n } = \mathbf { k } \cdot \mathbf { k } = 1$ . The flux is $\textstyle \iint 1 d S =$ area of disk $= \pi a ^ { 2 }$ . All fluid goes past the equator and out through the’sphere.



I have to mention one more problem. It might not occur to a reasonable person, but sometimes a surface has only one side. The famous example is the MRobius strip, for which you take a strip of paper, twist it once, and tape the ends together. Its special property appears when you run a pen along the “inside.” The pen in Figure 15.20 suddenly goes “outside.” After another round trip it goes back “inside.” Those words are in quotation marks, because on a MRobius strip they have no meaning.

Suppose the pen represents the normal vector. On a sphere n points outward. Alternatively n could point inward; we are free to choose. But the MRobius strip makes the choiceimpossible.After moving the pen continuously, it comes back in the opposite direction. This surface is not orientable. We cannot integrate $\mathbf { F } \cdot \mathbf { n }$ to compute the flux, because we cannot decide the direction of n.

A surface is oriented when we can and do choose n. This uses the final property of cross products, that they have length and direction and also a right-hand rule. We can tell $\mathbf { A } \times \mathbf { B }$ from $\mathbf { B } \times \mathbf { A }$ . Those give the two orientations of n. For an open surface (like a wastebasket) you can select either one. For a closed surface (like a sphere) it is conventional for $\mathbf { n }$ to be outward. By making that decision once and for all, the sign of the flux is established: outward flux is positive.

FORMULAS FOR SURFACE INTEGRALS