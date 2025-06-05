For single integrals, the interval $[ a , b ]$ is divided into short pieces of length $\Delta x$ : For double integrals, $R$ is divided into small rectangles of area $\Delta A = ( \Delta x ) ( \Delta y )$ : Above the $i$ th rectangle is a “thin stick” with small volume. That volume is the base area $\Delta A$ times the height above it—except that this height $z = f ( x , y )$ varies from point to point. Therefore we select a point $( x _ { i } , y _ { i } )$ in the $i$ th rectangle, and compute the volume from the height above that point:

$$
\nu o l u m e ~ o f o n e ~ s t i c k = f ( x _ { i } , y _ { i } ) \Delta A \quad \nu o l u m e ~ o f a l l ~ s t i c k s = \sum f ( x _ { i } , y _ { i } ) \Delta A .
$$

This is the crucial st»ep» for any integral—to see it as a sum of small pieces.

Now take limits: $\Delta x \to 0$ and $\Delta y \to 0$ : The height $z = f ( x , y )$ is nearly constant over each rectangle. (We assume thaÑt $f$ is a continuous function.) The sum approaches a limit, which depends only on the base $R$ and the surface above it. The limit is the volume of the solid, and it is the double integral of $f ( x , y )$ over $R$ :

$$
\iint _ { R } f ( x , y ) d A = \ \operatorname* { l i m } _ { { \Delta x \to 0 } \atop { \Delta y \to 0 } } \sum f ( x _ { i } , y _ { i } ) \Delta A .
$$

To reÑpeat: The limÑit is the same for all choices of the rectangles and the points $( x _ { i } , y _ { i } )$ : The rectangles will not fit exactly into $R$ ; if that base area is curved. The heights are not exact, if the surface $z = f ( x , y )$ is also curved. But the errors on the sides and top, where the pieces don’t fit and the heights are wrong, approach zero. Those errors are the volume of the “icing” around the solid, which gets thinner as $\Delta x \to 0$ and $\Delta y \to 0$ : A careful proof takes more space than we are willing to give. But the properties of the integral need and deserve attention:

1. Linearity: $\iint ( f + g ) d A = \iint f d A + \iint g d A$   
2. Constant comes outside: $\iiint c f ( x , y ) d A = c \iint f ( x , y ) d A$   
3. $R$ splits into $S$ and ${ \cal T } ( \mathrm { n o t o v e r l a p p i n g } ) \colon \iint f d A = \iint f d A + \iint f d A .$

In 1 the volume under $f + g$ has two parts. The “thin sticks” of height $f + g$ split into thin sticks under $f$ and under $g$ : In 2 the whole volume is stretched upward by $c$ : In 3 the volumes are side by side. As with single integrals, these properties help in computations.

By writing $d A$ ; we allow shapes other than rectangles. Polar coordinates have an extra factor $r$ in $d A = r d r d \theta$ : By writing $d x d y$ ; we choose rectangular coordinates and prepare for the splitting that comes now.

The double integral $\iiint f ( x , y ) d y d x$ will now be reduced to single integrals in $y$ and then $x$ : (Or vice versa. Our first integral could equally well be $\textstyle \int f ( x , y ) d x .$ :) Chapter 8 described the same idea for solids of revolution. First came the area of a slice, which is a single integral. Then came a second integral to add up the slices. For solids formed by revolving a curve, all slices are circular disks—now we expect other shapes.

Figure 14.2 shows a slice of»area $A ( x )$ : It cuts through the solid at a fixed value of $x$ : The cut starts at $y = c$ on one side of $R$ ; and ends at $y = d$ on the other side. This particular example goes from $y = 0$ to $y = 2$ ( $R$ is a rectangle). The area of a slice is the $y$ integral of $f ( x , y )$ : Remember that $x$ is fixed and $y$ goes from c to $d$ :

$$
A ( x ) = a r e a o f s l i c e = \int _ { c } ^ { d } f ( x , y ) d y \quad { \mathrm { ( t h e ~ a n s w e r ~ i s ~ a ~ f u n c t i o n ~ o f ~ } } x { ) } .
$$

$$
A = \int _ { y = 0 } ^ { 2 } ( 1 + x ^ { 2 } + y ^ { 2 } ) d y = \left[ y + x ^ { 2 } y + { \frac { y ^ { 3 } } { 3 } } \right] _ { y = 0 } ^ { y = 2 } = 2 + 2 x ^ { 2 } + { \frac { 8 } { 3 } } .
$$

This is the re»verse of a partial derivative! The integral of $x ^ { 2 } d y$ ; with $x$ constant, is $x ^ { 2 } y$ : This “partial integral” is actually called an inner integral. After substituting the limits $y = 2$ and $y = 0$ and subtracting, we have the area $\begin{array} { r } { \bar { A } ( x ) = 2 + 2 x ^ { 2 } + \frac { 8 } { 3 } } \end{array}$ : Now the outer integral adds slices to find the volume $\int A ( x ) d x$ : The answer is a number:

$$
{ \mathrm { v o l u m e } } = \int _ { x = 0 } ^ { 1 } \left( 2 + 2 x ^ { 2 } + { \frac { 8 } { 3 } } \right) d x = \left[ 2 x + { \frac { 2 x ^ { 3 } } { 3 } } + { \frac { 8 } { 3 } } x \right] _ { 0 } ^ { 1 } = 2 + { \frac { 2 } { 3 } } + { \frac { 8 } { 3 } } = { \frac { 1 6 } { 3 } } .
$$

To complete this example, check the volume when the $x$ integral comes first:

$$
{ \mathrm { i n n e r ~ i n t e g r a l } } = \int _ { x = 0 } ^ { 1 } ( 1 + x ^ { 2 } + y ^ { 2 } ) d x = { \biggl [ } x + { \frac { 1 } { 3 } } x ^ { 3 } + y ^ { 2 } x { \biggr ] } _ { x = 0 } ^ { x = 1 } = { \frac { 4 } { 3 } } + y ^ { 2 }
$$

$$
{ \mathrm { o u t e r ~ i n t e g r a l } } = \int _ { y = 0 } ^ { 2 } \left( { \frac { 4 } { 3 } } + y ^ { 2 } \right) d y = \left[ { \frac { 4 } { 3 } } y + { \frac { 1 } { 3 } } y ^ { 3 } \right] _ { y = 0 } ^ { y = 2 } = { \frac { 8 } { 3 } } + { \frac { 8 } { 3 } } = { \frac { 1 6 } { 3 } } .
$$

The fact that double integrals can be split into single integrals is Fubini’s Theorem.

14A if $f ( x , y )$ is continuous on the rectangle $R$ ; then

$$
\iint _ { R } f ( x , y ) d A = \int _ { a } ^ { b } \left[ \int _ { c } ^ { d } f ( x , y ) d y \right] d x = \int _ { c } ^ { d } \left[ \int _ { a } ^ { b } f ( x , y ) d x \right] d y .
$$

The inner integrals are the cross-sectional areas $A ( x )$ and $a ( y )$ of the slices. The outer integrals add up the volumes $A ( x ) d x$ and $a ( y ) d y$ : Notice the reversing of limits.

Normally the brackets in (2) are omitted. When the $y$ integral is first, $d y$ is written inside $d x$ : The limits on $y$ are inside too. I strongly recommend that you compute the inner integral on one line and the outer integral on a separate line.

EXAMPLE 2 Find the volume below the plane $z = x - 2 y$ and above the base triangle $R$ :

The triangle $R$ has sides on the $x$ and $y$ axes and the line $x + y = 1$ : The strips in the $y$ direction have varying lengths. (So do the strips in the $x$ direction.) This is the main point of the example—the base is not a rectangle. The upper limit on the inner integral changes as $x$ changes. The top of the triangle is at $y = 1 - x$ :

Figure 14.3 shows the strips. The region should always be drawn (except for rectangles). Without a figure the limits are hard to find. A sketch of $R$ makes it easy:

The inner integral has variable limits and the outer integral has constant limits:

$$
\Big . \Big . \cdot \int _ { \nu = 0 } ^ { \nu = 1 - x } ( x - 2 y ) d y = \Big [ x y - y ^ { 2 } \Big ] _ { y = 0 } ^ { y = 1 - x } = x ( 1 - x ) - ( 1 - x ) ^ { 2 } = - 1 + 3 x - 2 x ^ { 2 }
$$

$$
\therefore \int _ { x = 0 } ^ { 1 } ( - 1 + 3 x - 2 x ^ { 2 } ) d x = \left[ - x + { \frac { 3 } { 2 } } x ^ { 2 } - { \frac { 2 } { 3 } } x ^ { 3 } \right] _ { 0 } ^ { 1 } = - 1 + { \frac { 3 } { 2 } } - { \frac { 2 } { 3 } } = - { \frac { 1 } { 6 } } .
$$

The volume is negative. Most of the solid is below the $x y$ plane. To check the answer $- { \frac { 1 } { 6 } }$ ; d»o the $x$ integral first: $x$ goes from 0 to $1 - y$ : Then $y$ goes from 0 to 1:

$$
\therefore \int _ { x = 0 } ^ { 1 - y } ( x - 2 y ) d x = \left[ { \frac { 1 } { 2 } } x ^ { 2 } - 2 x y \right] _ { 0 } ^ { 1 - y } = { \frac { 1 } { 2 } } ( 1 - y ) ^ { 2 } - 2 ( 1 - y ) y = { \frac { 1 } { 2 } } - 3 y + { \frac { 5 } { 2 } } y ^ { 2 }
$$

$$
\therefore \int _ { y = 0 } ^ { 1 } \left( { \frac { 1 } { 2 } } - 3 y + { \frac { 5 } { 2 } } y ^ { 2 } \right) d y = \left[ { \frac { 1 } { 2 } } y - { \frac { 3 } { 2 } } y ^ { 2 } + { \frac { 5 } { 6 } } y ^ { 3 } \right] _ { 0 } ^ { 1 } = { \frac { 1 } { 2 } } - { \frac { 3 } { 1 } } + { \frac { 5 } { 6 } } = - { \frac { 1 } { 6 } } .
$$

Same answer, very probably right. The next example computes $\int \int 1 d x d y = \operatorname { a r e a } \operatorname { o f } R .$

EXAMPLE 3 The area of $R$ is $\int _ { x = 0 } ^ { 1 } \int _ { y = 0 } ^ { 1 - x } d y d x { \mathrm { ~ a n d ~ a l s o ~ } } \int _ { y = 0 } ^ { 1 } \int _ { x = 0 } ^ { 1 - y } d x d y .$

The first has vertical strips. The inner integral equals $_ { 1 - x }$ : Then the outer integral (of $\left| 1 - x \right.$ has limits 0 and 1; and the area is $\frac { 1 } { 2 }$ : It is like an indefinite integral inside a definite integral.

EXAMPLE 4 Reverse the order of integration in $\int _ { x = 0 } ^ { 2 } \int _ { y = x ^ { 2 } } ^ { 2 x } x ^ { 3 } d y d x .$

Solution Draw a figure!?The inner integral goes from the parabola $y = x ^ { 2 }$ up to the straight line $y = 2 x$ : This gives vertical strips. The strips sit side by side between $x = 0$ and $x = 2$ : They stop where $2 x$ equals $x ^ { 2 }$ ; and the line meets the parabola.

The problem is to put the $x$ integral first. It goes along horizontal strips. On each line $y =$ constant, we need the entry value of $x$ and the exit value of $x$ : From the figure, $x$ goes from ${ \scriptstyle { \frac { 1 } { 2 } } } y$ to $\sqrt { y }$ : Those are the inner limits. Pay attention also to the outer limits, because they now apply to $y$ : The region starts at $y = 0$ and ends at $y = 4$ : No change in the integrand $x ^ { 3 }$ —that is the height of the solid:

$$
\int _ { x = 0 } ^ { 2 } \int _ { y = x ^ { 2 } } ^ { 2 x } x ^ { 3 } d y d x i s r e { \nu } e r s e d t o \int _ { y = 0 } ^ { 4 } \int _ { x = \frac { 1 } { 2 } y } ^ { \sqrt { y } } x ^ { 3 } d x d y .
$$

EXAMPLE 5 Find the volume bounded by the planes $x = 0 , y = 0 , z = 0$ ; and $2 x + y + z = 4$ :

Solution The solid is a tetrahedron (four sides). It goes from $z = 0$ (the $x y$ plane) up to the plane $2 x + y + z = 4$ : On that plane $z = 4 - 2 x - y$ : This is the height function $f ( x , y )$ to be integrated.

Figure 14.4 shows the base $R$ : To find its sides, set $z = 0$ : The sides of $R$ are the lines $x = 0$ and $y = 0$ and $2 x + y = 4$ : Taking vertical strips, $d y$ is inner:

$$
\int _ { y = 0 } ^ { 4 - 2 x } ( 4 - 2 x - y ) d y = \left[ ( 4 - 2 x ) y - { \frac { 1 } { 2 } } y ^ { 2 } \right] _ { 0 } ^ { 4 - 2 x } = { \frac { 1 } { 2 } } ( 4 - 2 x ) ^ { 2 }
$$

$$
\int _ { x = 0 } ^ { 2 } { \frac { 1 } { 2 } } ( 4 - 2 x ) ^ { 2 } d x = \left[ - { \frac { ( 4 - 2 x ) ^ { 3 } } { 2 \cdot 3 \cdot 2 } } \right] _ { 0 } ^ { 2 } = { \frac { 4 ^ { 3 } } { 2 \cdot 3 \cdot 2 } } = { \frac { 1 6 } { 3 } } .
$$

Question What is the meaning of the inner integr ${ \frac { 1 } { 2 } } ( 4 - 2 x ) ^ { 2 } \left( { \mathrm { a n d ~ a l s o } } { \frac { 1 6 } { 3 } } \right) ?$ Answer The first is $A ( x )$ ; the area of the slice. $\frac { 1 6 } { 3 }$ is the solid volume.

Question What if the inner integral $\int f ( x , y ) d y$ has limits that depend on $y$ ? Answer It can’t. Those limits must be wrong. Find them again.

EXAMPLE 6 Find the mass in a semicircle $0 \leqslant y \leqslant { \sqrt { 1 - x ^ { 2 } } }$ if the density is $\rho = y$ :

This is a new application of double integrals. The total mass is a sum of small masses $\overset { \cdot } { \rho }$ times $\Delta A$ ) in rectangles of area $\Delta A$ : The rectangles don’t fit perfectly inside the semicircle $R$ ; and the density is not constant in each rectangle—but those problems disappear in the limit. We are left with a double integral:

$$
t o t a l m a s s ~ M = \int \int _ { R } \rho d A = \int \int _ { R } \rho ( x , y ) d x d y .
$$

Set $\rho = y$ : Figure 14.4 shows the limits on $x$ and $y$ (try both $d y \ : d x$ and $d x d y$ ):

$$
\operatorname* { m a s s } M = \int _ { x = - 1 } ^ { 1 } \int _ { y = 0 } ^ { \sqrt { 1 - x ^ { 2 } } } y d y d x \quad { \mathrm { a n d ~ a l s o } } \quad M = \int _ { y = 0 } ^ { 1 } \int _ { - { \sqrt { 1 - y ^ { 2 } } } } ^ { { \sqrt { 1 - y ^ { 2 } } } } y d x d y .
$$

The first inner integral is ${ \scriptstyle { \frac { 1 } { 2 } } } y ^ { 2 }$ : Substituting the limits gives ${ \scriptstyle { \frac { 1 } { 2 } } } ( 1 - x ^ { 2 } )$ : The outer integral of ${ \scriptstyle { \frac { 1 } { 2 } } } ( 1 - x ^ { 2 } )$ yields the total mass $\begin{array} { r } { M = \frac { 2 } { 3 } } \end{array}$ :

The second inner integral is $x y$ : Substituting the limits on $x$ gives : Then the outer integral is $- { \textstyle \frac { 2 } { 3 } } ( 1 - y ^ { 2 } ) ^ { 3 / 2 }$ : Substituting $y = 1$ and $y = 0$ yields $M = \_$

Remark This same calculation also produces the moment around the $x$ axis, when the density is $\rho = 1$ : The factor $y$ is the distance to the $x$ axis. The moment is $\textstyle M _ { x } = \int \int y \ d \dot { A } = \frac { 2 } { 3 }$ : Dividing by the area of the semicircle (which is $\pi / 2$ ) locates the centroid: ${ \overline { { x } } } = 0$ by symmetry and

$$
\overline { { y } } = \mathrm { h e i g h t o f ~ c e n t r o i d } = \frac { \mathrm { m o m e n t } } { \mathrm { a r e a } } = \frac { 2 / 3 } { \pi / 2 } = \frac { 4 } { 3 \pi } .
$$

This is the “average height” of points inside the semicircle, found earlier in 8:5:

EXAMPLE 7 Integrate $\textstyle { \int _ { y = 0 } ^ { y = 1 } \int _ { x = y } ^ { x = 1 } \cos \ x ^ { 2 } d x \ d y }$ avoiding the impossible $\int \cos { x ^ { 2 } d x }$ : This is a famous example where reversing the order makes the calculation possible. The base $R$ is the triangle in Figure 14.4 (note that $x$ goes from $y$ to 1). In the opposite order $y$ goes from $_ { 0 t o x }$ . Then $\int \cos x ^ { 2 } d y = { \bar { x } }$ cos $x ^ { 2 }$ contains the factor $x$ that we need:

$$
{ \begin{array} { r l } & { \qquad 1 } \\ & { { \mathrm { o u t e r ~ i n t e g r a l : ~ } } { \int } x \cos x ^ { 2 } d x = { \Bigl [ } { \frac { 1 } { 2 } } \sin x ^ { 2 } { \Bigr ] } _ { 0 } ^ { 1 } = { \frac { 1 } { 2 } } \sin 1 . } \\ & { \qquad 0 } \end{array} }
$$