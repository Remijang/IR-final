# 14.3 Triple Integrals

At this point in the book, I feel I can speak to you directly. You can guess what triple integrals are like. Instead of a small interval or a small rectangle, there is a small box. Instead of length $d x$ or area $d x d y$ ; the box has volume $d V = d x d y d z$ : That is length times width times height. The goal is to put small boxes together (by integration). The main problem will be to discover the correct limits on $x , y , z$ :

We could dream up more and more complicated regions in three-dimensional space. But I don’t think you can see the method clearly without seeing the region clearly. In practice six shapes are the most important:

box prism cylinder cone tetrahedron sphere.

The box is easiest and the sphere may be the hardest (but no problem in spherical coordinates). Circular cylinders and cones fall in the middle, where $x y z$ coordinates are possible but $r \theta z$ are the best. I start with the box and prism and $x y z$ :

EXAMPLE 1 By triple integrals find the volume of a box and a prism (Figure 14.12).

$$
\iiint d V = \int \int \int \int \int \int d x d y d z \quad { \mathrm { a n d } } \quad \iiint d V = \int \int \int \int \int \int d x d y d z
$$

The inner integral for both is $\textstyle \int d x = 2$ : Lines in the $x$ direction have length 2; cutting through the box and the prism. The middle integrals show the limits on $y$ (since $d y$ comes second):

$$
\int _ { y = 0 } ^ { 3 } 2 d y = 6 \quad { \mathrm { a n d } } \quad \int _ { y = 0 } ^ { 3 - 3 z } 2 d y = 6 - 6 z .
$$

After twointegrations these are areas. The first area 6 is for a plane section through the box. The second area $6 - 6 z$ is cut through the prism. The shaded rectangle goes from $y = 0$ to $y = 3 - 3 z$ —we needed and used the equation $y + 3 z = 3$ for the boundary of the prism. $\mathbf { } A t \mathbf { \Sigma }$ this point $z$ is still constant! But the area depends on $z$ ; because the prism gets thinner going upwards. The base area is $6 - 6 z = 6$ ; the top area is $6 - 6 z = 0$ :

The outer integral multiplies those areas by $d z$ ; to give the volume of slices. They are horizontal slices because $z$ came last. Integration adds up the slices to find the total volume:

$$
{ \mathrm { b o x ~ v o l u m e } } = \int _ { z = 0 } ^ { 1 } 6 d z = 6 \qquad { \mathrm { p r i s m ~ v o l u m e } } = \int _ { z = 0 } ^ { 1 } ( 6 - 6 z ) d z = \left[ 6 z - 3 z ^ { 2 } \right] _ { 0 } ^ { 1 } = 3 .
$$

The box vo»lum»e $2 \cdot 3 \cdot 1$ didn’t need calc»ulu»s. The prism is half o»f the box, so its volume was sure to be 3—but it is satisfying to see how $6 z - 3 z ^ { 2 }$ gives the answer. Our purpose is to see how a triple integral works.

Question Find the prism volume in the order dz dy $d x$ (six orders are possible).

$$
\int _ { 0 } ^ { 2 } \int _ { 0 } ^ { 3 } \int _ { 0 } ^ { ( 3 - y ) / 3 } d z d y d x = \int _ { 0 } ^ { 2 } \int _ { 0 } ^ { 3 } \left( { \frac { 3 - y } { 3 } } \right) d y d x = \int _ { 0 } ^ { 2 } { \frac { 3 } { 2 } } d x = 3 .
$$

To find those limits on the $z$ integral, follow a line in the $z$ direction. It enters the prism at $z = 0$ and exits at the sloping face $y + 3 z = 3$ : That gives the upper limit $z = ( 3 - y ) / 3$ : It is the height of a thin stick as in Section 14:1: This section writes out $\int d z$ for the height, but a quicker solution starts at the double integral.

What is the number $\frac { 3 } { 2 }$ in the last integral ? It is the area of a vertical slice, cut by a plane $x =$ constant. The outer integral adds up slices.

$$
\iiint f ( x , y , z ) d V ~ i s ~ c o m p u t e d f r o m ~ t h r e e ~ s i n g l e ~ i n t e g r a l s \int [ \int [ \int f ~ d x ~ ] d y ~ ] d z .
$$

That step cannot be taken in silence—some basic calculus is involved. The triple integral is the limit of $\sum f _ { i } \Delta V$ ; a sum over small boxes of volume $\Delta V .$ Here $f _ { i }$ is any value of $f ( x , y , z )$ Pin the $i$ th box. (In the limit, the boxes fit a curved region.) Now take those boxes in a certain order. Put them into lines in the $x$ direction and put the lines of boxes into planes. The lines lead to the inner $x$ integral, whose answer depends on $y$ and $z$ : The $y$ integral combines the lines into planes. Finally the outer integral accounts for all planes and all boxes.

Example 2 is important because it displays more possibilities than a box or prism.

EXAMPLE 2 Find the volume of a tetrahedron (4-sided pyramid). Locate $( { \overline { { x } } } , { \overline { { y } } } , { \overline { { z } } } )$ .

Solution A tetrahedron has four flat faces, all triangles. Th e fourth face in Figure 14.13 is on the plane $x + y + z = 1$ : A line in the $x$ direction enters at $x = 0$ and exits at $x = 1 - y - z$ : (The length depends on $y$ and $z$ : The equation of the boundary plane gives $x$ :) Then those lines are put into plane slices by the $y$ integral:

$$
\int _ { y = 0 } ^ { 1 - z } \int _ { x = 0 } ^ { 1 - y - z } d x d y = \int _ { y = 0 } ^ { 1 - z } ( 1 - y - z ) d y = { \Big [ } y - { \frac { 1 } { 2 } } y ^ { 2 } - z y { \Big ] } _ { 0 } ^ { 1 - z } = { \frac { 1 } { 2 } } ( 1 - z ) ^ { 2 } .
$$

What is this number ${ \scriptstyle { \frac { 1 } { 2 } } } ( 1 - z ) ^ { 2 } ?$ It is the area at height $z$ : The plane at that height slices out a right triangle, whose legs have length $_ { 1 - z }$ : The area is correct, but look at the limits of integration. $\pmb { I f x }$ goes to $1 - y - z$ ; why does $y$ go to $1 - z ?$ Reason: We are assembling lines, not points. The figure shows a line at every $y$ up to $_ { 1 - z }$ :

Adding the slices gives the volume: $\begin{array} { r } { \int _ { 0 } ^ { 1 } { \frac { 1 } { 2 } } ( 1 - z ) ^ { 2 } d z = \left[ { \frac { 1 } { 6 } } ( z - 1 ) ^ { 3 } \right] _ { 0 } ^ { 1 } = \frac { 1 } { 6 } } \end{array}$ : This agrees with $\frac 1 3$ (base times h eight), thevolume of a pyramid.

The height $\overline { { z } }$ of the centroid is $^ { * * } z _ { \mathrm { a v e r a g e } }$ :” We compute $\iiint z d V$ and divide by the volume. Each horizontal slice is multiplied by its height $z$ ; and the limits of integration don’t change:

$$
\iiint z d V = \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 - y } \int _ { 0 } ^ { 1 - y - z } z d x d y d z = \int _ { 0 } ^ { 1 } { \frac { z ( 1 - z ) ^ { 2 } } { 2 } } d z = { \frac { 1 } { 2 4 } } .
$$

This is quick because $z$ is constant in the $x$ and $y$ integrals. Each triangular slice contributes $z$ times its area $\scriptstyle { \frac { 1 } { 2 } } ( 1 - z ) ^ { 2 }$ times $d z$ : Then the $z$ integral gives the moment

$1 / 2 4$ : To find the average height, divide $1 / 2 4$ by the volume:

$$
{ \overline { { z } } } = { \mathrm { h e i g h t o f ~ c e n t r o i d } } = { \frac { \iiint z d V } { \iiint d V } } = { \frac { 1 / 2 4 } { 1 / 6 } } = { \frac { 1 } { 4 } } .
$$

By symmetry $\textstyle { \overline { { x } } } = { \frac { 1 } { 4 } }$ and $\begin{array} { r } { \overline { { y } } = \frac { 1 } { 4 } } \end{array}$ : The centroid is the point $\bigl ( { \frac { 1 } { 4 } } , { \frac { 1 } { 4 } } , { \frac { 1 } { 4 } } \bigr )$ : Compare that with $\bigl ( { \frac { 1 } { 3 } } , { \frac { 1 } { 3 } } \bigr )$ ; the centroid of the standard right triangle. Compare also with $\frac { 1 } { 2 }$ ; the center of the unit interval. There must be a five-sided region in four dimensions centered at $\bigl ( \frac { 1 } { 5 } , \frac { 1 } { 5 } , \frac { 1 } { 5 } , \frac { 1 } { 5 } \bigr )$ :

For area and volume we meet another pattern. Length of standard interval is 1; area of standard triangle is $\frac { 1 } { 2 }$ ; volume of standard tetrahedron is $\frac { 1 } { 6 }$ ; hypervolume in four dimensions must be : The interval reaches the point $\bar { x } = 1$ ; the triangle reaches the line $x + y = 1$ ; the tetrahedron reaches the plane $x + y + z = 1$ : The fourdimensional region stops at the hyperplane $\_ 1$ :

EXAMPLE 3 Find the volume $\iint d x d y d z$ inside the unit sphere $x ^ { 2 } + y ^ { 2 } + z ^ { 2 } =$ 1:

First question: What are the?limits on $x ?$ If a needle goes through the sphere in the $x$ direction, where does it enterandleave ? Moving in the $x$ direction, the numbers $y$ and $z$ stay constant. The inner integral deals only with $x$ : The smallest and largest $x$ are at the boundary wher?e $x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = 1$ : This equation does the work—we solve it for $x$ : Look at the limits on the $x$ integral:

$$
{ \mathrm { v o l u m e ~ o f ~ s p h e r e } } = \int \int \displaylimits _ { ? } ^ { ? } \int \displaylimits _ { - \sqrt { 1 - y ^ { 2 } - z ^ { 2 } } } ^ { \sqrt { 1 - y ^ { 2 } - z ^ { 2 } } } d x d y d z = \int \displaylimits _ { ? } ^ { ? } \int \displaylimits _ { ? } ^ { ? } 2 \sqrt { 1 - y ^ { 2 } - z ^ { 2 } } d y d z .
$$

The limits on $y$ are $- { \sqrt { 1 - z ^ { 2 } } }$ and $+ { \sqrt { 1 - z ^ { 2 } } }$ : You can use algebra on the boundary equation $x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = 1$ : But notice that $x$ is gone! Wewant the smallest and largest $y$ ; for each $z$ : It helps very much to draw the plane at height $z$ ; slicing through the sphere in Figure 14.14. The slice is a circle of radius $r = \sqrt { 1 - z ^ { 2 } }$ : So the area is $\pi r ^ { 2 }$ ; which must come from the $y$ integral:

$$
\begin{array} { r } { \int 2 \sqrt { 1 - y ^ { 2 } - z ^ { 2 } } d y = \mathrm { a r e a } \mathrm { o f } \mathrm { s l i c e } = \pi ( 1 - z ^ { 2 } ) . } \end{array}
$$

I admit that I didn’t integrate. Is it cheating to use the formula $\pi r ^ { 2 } ? \mathrm { ~ I ~ }$ don’t think so. Mathematics is hard enough, and we don’t have to work blindfolded. The goal is understanding, and if you know the area then use it. Of course the integral of $\sqrt { 1 - y ^ { 2 } - z ^ { 2 } }$ can be done if necessary—use Section 7:2:



The trip»le integral is down to a single integral. We went from one needle to a circle of needles and now to a sphere of needles. The volume isa sum of slices of area $\pi ( 1 - z ^ { 2 } )$ :The South Pole is at $z = - 1$ ; the North Pole is at $z = + 1$ ; and the integral is the volume $4 \pi / 3$ inside the unit sphere:

$$
\int _ { - 1 } ^ { 1 } \pi ( 1 - z ^ { 2 } ) d z = \pi \left( z - { \frac { 1 } { 3 } } z ^ { 3 } \right) \int _ { - 1 } ^ { 1 } = { \frac { 2 } { 3 } } \pi - \left( - { \frac { 2 } { 3 } } \pi \right) = { \frac { 4 } { 3 } } \pi .
$$

Question 1 A cone also has circular slices. How is the last integral changed ?

Answer The slices of a cone have radius $1 - z$ : Integrate $( 1 - z ) ^ { 2 }$ not $\sqrt { 1 - z ^ { 2 } }$ :

Question 2 How does this compare with a circular cylinder (height 1; radius 1) ?

Answer Now all slices have radius 1: Above $z = 0$ ; a cylinder has volume $\pi$ and a half-sphere has volume $\scriptstyle { \frac { 2 } { 3 } } \pi$ and a cone has volume $\scriptstyle { \frac { 1 } { 3 } } \pi$ :

For solids with equal surface area, the sphere has largest volume.

Question 3 What is the average height $\overline { { z } }$ in the cone and half-sphere and cylinder ?

Answer

$$
\overline { { z } } = \frac { \int z ( \mathrm { s l i c e \ a r e a } ) d z } { \int ( \mathrm { s l i c e \ a r e a } ) d z } = \frac { 1 } { 4 } \quad \mathrm { a n d } \quad \frac { 3 } { 8 } \quad \mathrm { a n d } \quad \frac { 1 } { 2 } .
$$

EXAMPLE 4 Find the volume $\iint d x d y d z$ inside the ellipsoid $x ^ { 2 } / a ^ { 2 } + y ^ { 2 } / b ^ { 2 } +$ $z ^ { 2 } / c ^ { 2 } = 1$ :

The limits on $x$ are now $\pm \sqrt { 1 - y ^ { 2 } / b ^ { 2 } - z ^ { 2 } / c ^ { 2 } }$ : The algebra looks terrible. The geometry is better—all slices are ellipses. A change of variable is absolutely the best.

Introduce $u = x / a$ and $v = y / b$ and $w = z / c$ : Then the outer boundary becomes $u ^ { 2 } + v ^ { 2 } + w ^ { 2 } = 1 .$ In these new variables the shape is a sphere. The triple integral for a sphere is $\iiint d u d v d w = 4 \pi / 3$ : But what volume $d V$ in $x y z$ space corresponds to a small box with sides $d u$ and $d v$ and $d w ?$

Every uvw box comes from an $x y z$ box. The box is stretched with no bending or twisting. Since $u$ is $x / a$ ; the length $d x$ is a $d u$ : Similarly $d y = b d v$ and $d z =$ $c d w$ : The volume of the $x y z$ box (Figure 14.14) is $d x d y d z = ( a b c ) d u d v d w$ :

# 14.3 Triple Integrals

The stretching factor $J = a b c$ is a constant, and the volume of the ellipsoid is

$$
\bigcap _ { \mathrm { e l l i p s o i d } } ^ { \mathrm { b a d l i m i t s } } d x d y d z = \overbrace { \iint _ { \mathrm { e l l i p s o i d } } } ^ { \mathrm { b e t t e r l i m i t s } } ( a b c ) d u d v d w = \frac { 4 \pi } { 3 } a b c .
$$

You realize that this is special—other volumes are much more complicated. The sphere and ellipsoid are curved, but the small $x y z$ boxes are straight. The next section introduces spherical coordinates, and we can finally write “good limits.” But then we need a different $J$ :