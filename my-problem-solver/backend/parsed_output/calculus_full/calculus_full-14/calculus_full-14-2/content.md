# 14.2 Change to Better Coordinates

You don’t go far with double integrals before wanting to change variables. Many regions simply do not fit with the $x$ and $y$ axes. Two examples are in Figure 14.5, a tilted square and a ring. Those are excellent shapes—in the right coordinates.

We have to be able to answer basic questions like these:

Find the area $\iint d A { \mathrm { ~ a n d ~ m o m e n t } } \iint x d A { \mathrm { ~ a n d ~ m o m e n t ~ o f ~ i n e r t i a ~ } } \iint$

The problem is: What is $d A \operatorname { \mathrm { ? } }$ We are leaving the $x y$ variables where $d A = d x d y$ :

The reason for changing is this: The limits of integration in the $y$ direction are miserable. I don’t know them and I don’t want to know them. For every $x$ we would need the entry point $P$ of the line $x =$ constant, and the exit point $\boldsymbol { Q }$ : The heights of $P$ and $\boldsymbol { Q }$ are the limits on $\int d y$ ; the inner integral. The geometry of the square and ring are totally missed, if we stick rigidly to $x$ and $y$ :

Which coordinates are better ? Any sensible person agrees that the area of the tilted square is 1: “Just turn it and the area is obvious.” But that sensible person may not know the moment or the center of gravity or the moment of inertia. So we actually have to do the turning.

The new coordinates $u$ and $v$ are in Figure 14.6a. The limits of integration on $v$ are 0 and 1: So are?the limits on $u$ : But when you change variables, you don’t just change limits. Two other changes come with new variables:

1. The small area $d A = d x d y$ becomes $d A = - d u d v$ :   
2. The integral of $x$ becomes the integral of

Substituting $u = { \sqrt { x } }$ in a single integral, we make the same changes. Limits $x = 0$ and $x = 4$ become $u = 0$ and $u = 2$ : Since $x$ is $u ^ { 2 }$ ; $d x$ is $2 u d u$ : The purpose of the change is to find an antiderivative. For double integrals, the usual purpose is to improve the limits—but we have to accept the whole package.

To turn the square, there are formulas connecting $x$ and $y$ to $u$ and $v$ : The geometry is clear—rotate axes by $\alpha$ —but it has to be converted into algebra:

$$
\begin{array} { l l } { { u = x \cos \alpha + y \sin \alpha } } & { { x = u \cos \alpha - v \sin \alpha } } \\ { { } } & { { { \mathrm { a n d ~ i n ~ r e v e r s e } } } } \\ { { v = - x \sin \alpha + y \cos \alpha } } & { { y = u \sin \alpha + v \cos \alpha . } } \end{array}
$$

Figure 14.6 shows the rotation. As points move, the whole square turns. A good way to remember equation (1) is to follow the corners as they become $( 1 , 0 )$ and $( 0 , 1 )$ :

The change from $\iint x d A$ to $\iint { \frac { \partial \mathbf { u } \ d v } { \partial \mathbf { u } \ d v } }$ is partly decided by equation (1). It gives $x$ as a function of $u$ and $v$ : We also need $d A$ : For a pure rotation the first guess is correct: The area $d x$ dy equals the area $d u d v$ : For most changes of variable this is false. The general formula for $d A$ comes after the examples.

EXAMPLE 1 Find $\iint d A$ and $\iint x d A$ and $\textstyle { \overline { { x } } }$ and also $\iint x ^ { 2 } d A$ for the tilted square.

Solution The area of the square is $\textstyle \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } d u d v = 1$ : Notice the good limits. Then

$$
\begin{array} { r } { \iint x d A = \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } ( u \cos \alpha - v \sin \alpha ) d u d v = \frac 1 2 \cos \alpha - \frac 1 2 \sin \alpha . } \end{array}
$$

This is the moment around the $y$ axis. The factors $\frac { 1 } { 2 }$ come from ${ \scriptstyle { \frac { 1 } { 2 } } } u ^ { 2 }$ and ${ \scriptstyle { \frac { 1 } { 2 } } } v ^ { 2 }$ : The $x$ coordinate of the center of gravity is

$$
{ \overline { { x } } } = \int \int x d A { \bigg / } \int \int d A = \left( { \textstyle { \frac { 1 } { 2 } } } \cos \alpha - { \textstyle { \frac { 1 } { 2 } } } \sin \alpha \right) / 1 .
$$

Similarly the integral of $y$ leads to $\overline { { y } }$ : The answer is no mystery—the point $( { \overline { { x } } } , { \overline { { y } } } )$ is at the center of the square! Substituting $x = u$ cos $\alpha - v$ sin $\alpha$ made $x d A$ look worse, but the limits 0 and 1 are much better.

The moment of inertia $I _ { y }$ around the $y$ axis is also simplified:

$$
\iint x ^ { 2 } d A = \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } ( u \cos \alpha - v \sin \alpha ) ^ { 2 } d u d v = { \frac { \cos ^ { 2 } \alpha } { 3 } } - { \frac { \cos \alpha \sin \alpha } { 2 } } + { \frac { \sin ^ { 2 } \alpha } { 3 } } .
$$

You know this next fact but I will write it anyway: The answers don’t contain u or $v$ : Those are dummy variables like $x$ and $y$ : The answers do contain $\alpha$ ; because the square has turned. (The area is fixed at 1:) The moment of inertia $I _ { x } = \iint y ^ { 2 } d A$ is the same as equation (3) but with all plus signs.

Question The sum $I _ { x } + I _ { y }$ simplifies to $\frac { 2 } { 3 }$ (a constant). Why no dependence on $\alpha$ ? Answer $I _ { x } + I _ { y }$ equals $I _ { 0 }$ : This moment of inertia around $( 0 , 0 )$ is unchanged by rotation. We are turning the square around one of its corners.

# CHANGE TO POLAR COORDINATES

The next change is to $r$ and $\theta$ : A small area becomes $d A = r d r d \theta$ (definitely not $d r d \theta )$ ). Area always comes from multiplying two lengths, and $d \theta$ is not a length. Figure 14.7 shows the crucial region—a “polar rectangle” cut out by rays and circles. Its area $\Delta A$ is found in two ways, both leading to $r d r d \theta$ :

(Approximate) The straight sides have length $\Delta r$ : The circular arcs are close to $r \Delta \theta$ : The angles are $9 0 ^ { \circ }$ : So $\Delta A$ is close to $( \Delta r ) ( r \Delta \theta )$ :

(Exact) A wedge has area ${ \frac { 1 } { 2 } } r ^ { 2 } \Delta \theta$ : The difference between wedges is $\Delta A$ :

$$
\Delta A = \frac { 1 } { 2 } \left( r + \frac { \Delta r } { 2 } \right) ^ { 2 } \Delta \theta - \frac { 1 } { 2 } \left( r - \frac { \Delta r } { 2 } \right) ^ { 2 } \Delta \theta = r \Delta r \Delta \theta .
$$

The exact method places $r$ dead center (see figure). The approximation says: Forget the change in $r \Delta \theta$ as you move outward. Keep only the first-order terms.

A third method is coming, which requires no picture and no geometry. Calculus always has a third method! The change of variables $x = r$ cos $\theta , y = r$ sin $\theta$ will go into a general formula for $d A$ ; and out will come the area $r d r d \theta$ :

EXAMPLE 2 Find the area and center of gravity of the ring. Also find $\iint x ^ { 2 } d A$ :

Solution The limits on $r$ are 4 and 5: The limits on $\theta$ are 0 and $2 \pi$ : Polar coordinates are perfect for a ring. Compared with limits like $x = \sqrt { 2 5 - y ^ { 2 } }$ ; the change to $r d r d \theta$ is a small price to pay:

$$
\scriptstyle { \mathrm { a r e a } } = { \int { \int { \int r d r d \theta } } } = 2 \pi \left[ { \frac { 1 } { 2 } } r ^ { 2 } \right] _ { 4 } ^ { 5 } = \pi 5 ^ { 2 } - \pi 4 ^ { 2 } = 9 \pi .
$$

The $\theta$ integral is $2 \pi$ (full circle). Actually the ring is a giant polar rectangle. We could have used the exact formula $r \Delta r \Delta \theta$ ; with $\Delta \theta = 2 \pi$ and $\Delta r = 5 - 4$ : When the radius $r$ is centered at 4:5; the product $r \Delta r \Delta \theta$ is $( 4 . 5 ) ( 1 ) ( 2 \pi ) = 9 \pi$ as above.

Since the ring is symmetric around $( 0 , 0 )$ ; the integral of $x d A$ must be zero:

$$
\begin{array} { r } { \underset { \pmb { R } } { \iint } x d A = \int \int \int ( r \cos \theta ) r d r d \theta = \Big [ \frac { 1 } { 3 } r ^ { 3 } \Big ] _ { 4 } ^ { 5 } \Big [ \sin \theta \Big ] _ { 0 } ^ { 2 \pi } = 0 . } \end{array}
$$

Notice $r$ cos $\theta$ from $x$ —the other $r$ is from $d A$ : The moment of inertia is

$$
\begin{array} { l } { \iint x ^ { 2 } d A = \int _ { 0 } ^ { 2 \pi } \int r ^ { 2 } \cos ^ { 2 } \theta r d r d \theta = \left[ \frac { 1 } { 4 } r ^ { 4 } \right] _ { 4 } ^ { 5 } \int \cos ^ { 2 } \theta d \theta = \frac { 1 } { 4 } ( 5 ^ { 4 } - 4 ^ { 4 } ) \pi . } \end{array}
$$

This $\theta$ integral is $\pi$ not $2 \pi$ ; because the average of $\cos ^ { 2 } \theta$ is $\frac { 1 } { 2 }$ not 1:

For reference here are the moments of inertia when the density is $\rho ( x , y )$

$$
\begin{array} { r l } { I _ { y } = \iint { x ^ { 2 } \rho d A } } & { { } I _ { x } = \iint { y ^ { 2 } \rho d A } \quad I _ { 0 } = \iint { r ^ { 2 } \rho d A } = p o l a r m o m e n t = I _ { x } + I _ { y } . } \end{array}
$$

EXAMPLE 3 Find masses and moments for semicircular plates: $\rho = 1$ and $\rho = 1 - r$ :

Solution The semicircles in Figure 14.8 have $r = 1$ :The angle goes from 0 to $\pi$ (the upper half-circle). Polar coordinates are best. The mass is the integral of the density $\rho$ :

$$
M = \int \displaylimits _ { 0 } ^ { \pi } \int r d r d \theta = ( \textstyle { \frac { 1 } { 2 } } ) ( \pi ) \quad \mathrm { a n d } \quad M = \int \displaylimits _ { 0 } ^ { \pi } \int ( 1 - r ) r d r d \theta = ( \textstyle { \frac { 1 } { 6 } } ) ( \pi ) .
$$

The first mass $\pi / 2$ equals the area (because $\rho = 1$ ). The second mass $\pi / 6$ is smaller (because $\rho < 1$ ). Integrating $\rho = 1$ is the same as finding a volume when the height is $z = 1$ (part of a cylinder). Integrating $\rho = 1 - r$ is the same as finding a volume when the height is $z = 1 - r$ (part of a cone). Volumes of cones have the extra factor $\begin{array} { l } { { \frac { 1 } { 3 } } } \end{array}$ : The center of gravity involves the moment $M _ { x } = \iint y \rho d A$ : The distance from the $x$ axis is $y$ ; the mass of a small piece is $\rho d A$ ; integrate to add mass times distance. Polar coordinates are still best, with $y = r \sin \theta$ : Again $\rho = 1$ and $\rho = 1 - r$ :

$$
\iint y d A = \int _ { 0 } ^ { \pi } \int r \sin \theta r d r d \theta = \frac { 2 } { 3 } \qquad \iint y ( 1 - r ) d A = \int _ { 0 } ^ { \pi } \int r \sin \theta ( 1 - r ) r d r d \theta = \frac { 1 } { 6 } .
$$

The height of the center of gravity is $\overline { { y } } = M _ { x } / M = \imath$ moment divided by mass:

$$
\overline { { y } } = \frac { 2 / 3 } { \pi / 2 } = \frac { 4 } { 3 \pi } \quad \mathrm { w h e n } \ \rho = 1 \qquad \overline { { y } } = \frac { 1 / 6 } { \pi / 6 } = \frac { 1 } { \pi } \quad \mathrm { w h e n } \ \rho = 1 - r .
$$

Question Compare $\overline { { y } }$ for $\rho = 1$ and $\rho =$ other positive constants and $\rho = 1 - r$ : Answer Any constant $\rho$ gives $\overline { { y } } = 4 / 3 \pi$ : Since $1 - r$ is dense at $r = 0$ ; $\overline { { y } }$ drops to $1 / \pi$ :

Question How is $\overline { { y } } = 4 / 3 \pi$ related to the “average” of $y$ in the semicircle ? Answer They are identical. This is the point of $\overline { { y } }$ : Divide the integral by the area:

$$
T h e a \nu e r a g e \nu a l u e o f a f u n c t i o n i s \int \int f ( x , y ) d A \bigg / \iint d A .
$$

The integral of $f$ is divided by the integral of 1 (the area). In one dimension $\int _ { a } ^ { b } v ( x ) d x$ was divided by $\textstyle \int _ { a } ^ { b } 1 d x$ (the length $b - a )$ . That gave the average value of $v ( x )$ in Section 5:6: Equation (5) is the same idea for $f ( x , y )$ :

EXAMPLE 4 Compute $A { = } \displaystyle \int _ { - \infty } ^ { \infty } e ^ { - x ^ { 2 } } d x { = } \sqrt { \pi }$ from $A ^ { 2 } = \int _ { - \infty } ^ { \infty } e ^ { - x ^ { 2 } } d x \int _ { - \infty } ^ { \infty } e ^ { - y ^ { 2 } } d y =$ $\pi$ :

$A$ is the area under a “bell-shaped curve”—see Figure 14.9. This is the most important definite integral in the study of probability. It is difficult because a factor $2 x$ is not present. Int»eg8rating» $2 x e ^ { - x ^ { 2 } }$ gives $- e ^ { - x ^ { 2 } }$ ; but»integr»at8ing $e ^ { - x ^ { 2 } }$ is impossible— except approximately by a computer. How can we hope to show that $A$ is exactly $\sqrt { \pi }$ ? The trick ist8o go fro8m an area integral $A$ to a volume integral $A ^ { 2 }$ : This is unusual (and hard to like), but the end justifies the means:

$$
A ^ { 2 } = \int _ { x = - \infty } ^ { \infty } \int _ { y = - \infty } ^ { \infty } e ^ { - x ^ { 2 } } e ^ { - y ^ { 2 } } d y d x = \int _ { \theta = 0 } ^ { 2 \pi } \int _ { r = 0 } ^ { \infty } e ^ { - r ^ { 2 } } r d r d \theta .
$$

The double integrals cover the whole plane. The $r ^ { 2 }$ comes from $x ^ { 2 } + y ^ { 2 }$ ; and?the key factor $r$ appears in polar coordinates. It is now possible to substitute $u = r ^ { 2 }$ : The $r$ integral is $\begin{array} { r } { \frac { 1 } { 2 } \int _ { 0 } ^ { \infty } \bar { e } ^ { - u } d u = \frac { 1 } { 2 } } \end{array}$ : The $\theta$ integral is $2 \pi$ : The double integral is $\textstyle { \bigl ( } { \frac { 1 } { 2 } } { \bigr ) } ( 2 \pi )$ : Therefore $A ^ { 2 } = \pi$ and the single integral is $A = { \sqrt { \pi } }$ :

# EXAMPLE 5? Apply Example 4 to»th8e “normal distributi»on8” p.x/ D e x2=2= 2:

Section 8:4 discussed probability. It8emphasized the import8ance of this particular $p ( x )$ : At that time we could not verify that $\int p ( x ) d x = 1$ : Now we can:

$$
x = { \sqrt { 2 } } y \quad { \mathrm { y i e l d s } } \quad { \frac { 1 } { \sqrt { 2 \pi } } } \int _ { - \infty } ^ { \infty } e ^ { - x ^ { 2 } / 2 } d x = { \frac { 1 } { \sqrt { \pi } } } \int _ { - \infty } ^ { \infty } e ^ { - y ^ { 2 } } d y = 1 .
$$

Question Why include the 2’s in $p ( x ) ^ { . }$ ? The integral of $e ^ { - x ^ { 2 } } / \sqrt { \pi }$ also equals 1: Answer With the 2’s the “variance” is $\int x ^ { 2 } p ( x ) d x = 1$ : This is a convenient number.

# CHANGE TO OTHER COORDINATES

A third method was promised, to find $r d r d \theta$ without a picture and without geometry. The method works directly from $x = r$ cos $\theta$ and $y = r$ sin $\theta$ : It also finds the 1 in $d u d v$ ; after a rotation of axes. Most important, this new method finds the factor $J$ in the area $d A = J d u d v$ ; for any change of variables. The change is from $x y$ to $u v$ :

For single integrals, the “stretching factor” $J$ between the original $d x$ and the new $d u$ is (not surprisingly) the ratio $d x / d u$ : Where we have $d x$ ; we write $( d x / d u ) d u$ : Where we have $( d u / d x ) d x$ ; we write $d u$ : That was the idea of substitutions—the main way to simplify integrals.

For double integrals the stretching factor appears in the area: $d x d y$ becomes $\mid J \mid d u d v$ : The old and new variables are related by $x = x ( u , v )$ and $y = y ( u , v )$ : The point with coordinates $u$ and $v$ comes from the point with coordinates $x$ and $y$ : A whole region $S$ ; full of points in the $u v$ plane, comes from the region $R$ full of corresponding points in the $x y$ plane. A small piece with area $\mid J \mid d u d v$ comes from a small piece with area $d x d y$ : The formula for $J$ is a two-dimensional version of $d x / d u$ :

14B The str»e»tching factor for area»i»s the 2 by 2 Jacobian determinant $J ( u , v )$ :

$$
J = \left| \begin{array} { l l } { \partial x / \partial u } & { \partial x / \partial v } \\ { \partial y / \partial u } & { \partial y / \partial v } \end{array} \right| = \frac { \partial x } { \partial u } \frac { \partial y } { \partial v } - \frac { \partial x } { \partial v } \frac { \partial y } { \partial u } .
$$

An integral over $R$ in the $x y$ plane becBomes an  iBntegral over $S$ in the $u v$ plane:

$$
\iint _ { R } f ( x , y ) d x d y = \iint _ { S } f ( x ( u , v ) , y ( u , v ) ) | J | d u d v .
$$

The determinant $J$ is often written $\hat { \cal { O } } ( x , y ) / \hat { \cal { O } } ( u , v )$ ; as a reminder that this stretching factor is like $d x / d u$ : We require $J \neq 0$ : That keeps the stretching and shrinking under control.

You naturally ask: Why take the absolute value $\vert J \vert$ in equation (9) ? Good question—it wasn’t done for single integrals. The reason is in the limits of integration. The single integral $\textstyle \int _ { 0 } ^ { 1 } d x$ is $\int _ { 0 } ^ { - 1 } \left( - d u \right)$ after changing $x$ to $- u$ : We keep the minus sign and allow single integrals to run back ward . Double integrals could too, but normally they go left to right Band  BdownBto u Bp. We use the absolute value $\left| J \right|$ and run forward.

EXAMPLE 6 Polar coordinates have $x = u$ cos $v = r$ cos $\theta$ and $y = u$ sin $v = r \sin \theta$ :

$$
\begin{array} { r } { J = \left| \begin{array} { l l } { \partial x / \partial r } & { \partial x / \partial \theta } \\ { \partial y / \partial r } & { \partial y / \partial \theta } \end{array} \right| = \left| \begin{array} { l l } { \cos \theta } & { - r \sin \theta } \\ { \sin \theta } & { r \cos \theta } \end{array} \right| = r . } \end{array}
$$

EXAMPLE 7 Find $J$ for the linear change to $x = a u + b v$ and $y = c u + d v$ :

$$
J = \left| \begin{array} { l l } { \partial x / \partial u } & { \partial x / \partial v } \\ { \partial y / \partial u } & { \partial y / \partial v } \end{array} \right| = \left| \begin{array} { l l } { a } & { b } \\ { c } & { d } \end{array} \right| = a d - b c .
$$

Why make this simple change, in which ${ a , b , c , d }$ are all constant ? It straightens parallelograms into squares (and rotatesthose squares). Figure 14.10 is typical.

Common sense indicated $J = 1$ for pure rotation—no change in area. Now $J = 1$ comes from equations (1) and (11), because $a d - b c$ is $\cos ^ { 2 } \alpha + \sin ^ { 2 } \alpha$ :

In practice, $x y$ rectangles generally go into $u v$ rectangles. The sides can be curved (as in polar rectangles) but the angles are often $9 0 ^ { \circ }$ : The change is “orthogonal.” The next example has angles that are not $9 0 ^ { \circ }$ ; and $J$ still gives the answer.

EXAMPLE 8 FindBthe  aBrea oBf $R$ iBn Figure 14.10. Also compute $\iint _ { R } e ^ { x } d x d y$ :

Solution The figure shows $\begin{array} { r } { x = \frac { 2 } { 3 } u + \frac { 1 } { 3 } v } \end{array}$ and $\begin{array} { r } { y = \frac { 1 } { 3 } u + \frac { 2 } { 3 } v } \end{array}$ : The determinant is

$$
J = \left| { \begin{array} { c c } { \partial x / \partial u } & { \partial x / \partial v } \\ { \partial y / \partial u } & { \partial y / \partial v } \end{array} } \right| = \left| { \begin{array} { c c } { 2 / 3 } & { 1 / 3 } \\ { 1 / 3 } & { 2 / 3 } \end{array} } \right| = { \frac { 4 } { 9 } } - { \frac { 1 } { 9 } } = { \frac { 1 } { 3 } } .
$$

The area of the $x y$ parallelogram becomes an integral over the $u v$ square:

$$
\iint d x d y = \iint _ { S } | J | d u d v = \int _ { 0 } ^ { 3 } \int { \frac { 1 } { 3 } } d u d v = { \textstyle { \frac { 1 } { 3 } } } \cdot 3 \cdot 3 = 3 .
$$

The square has area 9; the parallelogram has area 3: I don’t know if $\begin{array} { r } { J = \frac { 1 } { 3 } } \end{array}$ is a stretching factor or a shrinking factor. The other integral $\iint e ^ { x } d x d y$ is

$$
\int _ { 0 } ^ { 3 } \int _ { 0 } ^ { 3 } e ^ { 2 u / 3 + v / 3 } { \frac { 1 } { 3 } } d u d v = \left[ { \frac { 3 } { 2 } } e ^ { 2 u / 3 } \right] _ { 0 } ^ { 3 } \left[ 3 e ^ { v / 3 } \right] _ { 0 } ^ { 3 } { \frac { 1 } { 3 } } = { \frac { 3 } { 2 } } ( e ^ { 2 } - 1 ) ( e - 1 ) .
$$

Main point: The change to $u$ and $v$ makes the limits ea sBy (j uBst 0 anBd 3 )B.

Why is the stretching factor $J$ a determinant ? With straight sides, this goes back to Section 11:3 on vectors. The area of a parallelogram is a determinant. Here the sides are curved, but that only produces $( d u ) ^ { 2 }$ and $( d v ) ^ { 2 }$ ; which we ignore.

A change $d u$ gives one side of Figure 14.11—it is $( \partial x / \partial u { \bf i } + \partial y / \partial u { \bf j } ) d u$ : Side 2 is $( \partial x / \partial v { \bf i } + \partial y / \partial v { \bf j } ) d v$ : The curving comes from second derivatives. The area (the cross product of the sides) is $\mid J \mid d u d v$ :

Final remark I can’t resist looking at the change in the reverse direction. Now the rectangle is in $x y$ and the paBral lBelograBm i sB in $u v$ : In all formulas, exchange $x$ for $u$ and $y$ for $v$ :

$$
n e w \ J = { \left| \begin{array} { l l } { \displaystyle \partial u / \partial x } & { \displaystyle \partial u / \partial y } \\ { \displaystyle \partial v / \partial x } & { \displaystyle \partial v / \partial y } \end{array} \right| } = { \frac { \partial ( u , v ) } { \partial ( x , y ) } } = { \frac { 1 } { o l d \ J } } .
$$

This is exactly like $d u / d x = 1 / ( d x / d u ) .$ : It is the derivative of the inverse function. The product of slopes is 1—stBretc hB out,Bshri Bnk backB. F rBom $x y$ to B $u v$ we have 2 by 2 matrices, and the identity matrix $I$ takes the place of 1:

$$
\frac { d x } { d u } \frac { d u } { d x } = 1 \quad \mathrm { b e c o m e s } \quad \left[ \begin{array} { l l } { \hat { \partial } x / \hat { \partial } u } & { \hat { \partial } x / \hat { \partial } v } \\ { \hat { \partial } y / \hat { \partial } u } & { \hat { \partial } y / \hat { \partial } v } \end{array} \right] \left[ \begin{array} { l l } { \hat { \partial } u / \hat { \partial } x } & { \hat { \partial } u / \hat { \partial } y } \\ { \hat { \partial } v / \hat { \partial } x } & { \hat { \partial } v / \hat { \partial } y } \end{array} \right] = \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] .
$$

The first row times the first column is $( \partial x / \partial u ) ( \partial u / \partial x ) + ( \partial x / \partial v ) ( \partial v / \partial x ) =$ $\partial x / \partial x = 1$ : The first row times the second column is $( \partial x / \partial u ) ( \partial u / \partial y ) + ( \partial x / \partial v )$ $( \partial v / \partial y ) = \partial x / \partial y = 0$ : The matrices are inverses of each other. The determinants of a matrix and its inverse obey our rule: old $J$ times new $J = 1$ : Those $J$ ’s cannot be zero, just as $d x / d u$ and $d u / d x$ were not zero. (Inverse functions increase steadily or decrease steadily.)

In two dimensions, an area $d x d y$ goes to $\textit { J d u d v }$ and comes back to $d x d y$ :