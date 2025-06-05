# 14.4 Cylindrical and Spherical Coordinates

Cylindrical coordinates are good for describing solids that are symmetric around an axis. The solid is three-dimensional, so there are three coordinates $r , \theta , z$ :

r : out from the axis : around the axis¤ z: along the axis.

This is a mixture of polar coordinates $r \theta$ in a plane, plus $z$ upward. You will not find $r \theta z$ difficult to work with. Start with a cylinder centered on the $z$ axis:

solid cylinder W $0 \leqslant r \leqslant 1$ flat bottom and top $\ 0 \leqslant z \leqslant 3$ half-cylinder W $0 \leqslant \theta \leqslant \pi$ Integration over this half-cylinder is $\int _ { 0 } ^ { 3 } \int _ { 0 } ^ { \pi } \int _ { 0 } ^ { 1 } \mathcal { \underline { { \ ? \ } } } \ d r \ d \theta \ d z$ . These limits on $r , \theta , z$ are especially simple. Two other axially symmetric solids are almost as convenient:

$$
c o n e : i n t e g r a t e \ t o \ r + z = 1 \qquad s p h e r e : i n t e g r a t e \ t o \ r ^ { 2 } + z ^ { 2 } = R ^ { 2 }
$$

I would not use cylindrical coordinates for a box. Or a tetrahedron.

The integral needs one thing more—the volume $d V$ . The movements $d r$ and $d \theta$ and $d z$ give a “curved box” in $x y z$ space, drawn in Figure 14.15c. The base is a polar rectangle, with area $r \ d r \ d \theta$ . The new part is the height $d z$ . The volume of the curved box is $r d r d \theta d z$ . Then $r$ goes in the blank space in the triple integral—the stretching factor is $J = r$ . There are six orders of integration (we give two):

$$
{ \mathrm { v o l u m e } } = \int _ { z } \int _ { \theta } \int _ { r } r \ d r \ d \theta \ d z = \int _ { \theta } \int _ { z } \int _ { r } r \ d r \ d z \ d \theta .
$$

EXAMPLE 1 (Volume of the half-cylinder). The integral of $\textit { r d r }$ from 0 to 1 is $\frac { 1 } { 2 }$ The $\theta$ integral is $\pi$ and the $z$ integral is 3. The volume is $3 \pi / 2$ .

EXAMPLE 2 The surface $r = 1 - z$ encloses the cone in Figure 14.16. Find its volume.

First solution Since $r$ goes out to $_ { 1 - z }$ , the integral of $\textit { r d r }$ is $\scriptstyle { { \frac { 1 } { 2 } } ( 1 - z ) ^ { 2 } }$ . The $\theta$ integral is $2 \pi$ (a full rotation). Stop there for a moment.

We have reached $\begin{array} { r } { \int \int r \ d r \ d \theta = \frac { 1 } { 2 } ( 1 - z ) ^ { 2 } 2 \pi } \end{array}$ . This is the area of a slice at height $z$ . The slice is a circle, its radius is $1 - z$ , its area is $\pi ( 1 - z ) ^ { 2 }$ . The $z$ integral adds those slices to give $\pi / 3$ . That is correct, but it is not the only way to compute the volume.



Second solution Do the $z$ and $\theta$ integrals first. Since $z$ goes up to $1 - r$ , and $\theta$ goes around to $2 \pi$ , those integrals produce $\begin{array} { r } { \int \int r ~ d z ~ d \theta = r ( 1 - r ) 2 \pi } \end{array}$ . Stop again— this must be the area of something.

After the $z$ and $\theta$ integrals we have a shell at radius $r$ . The height is $1 - r$ (the outer shells are shorter). This height times $2 \pi r$ gives the area around the shell. The choice between shells and slices is exactly as in Chapter 8: Different orders of integration give different ways to cut up the solid.

The volume of the shell is area times thickness $d r$ . The volume of the complete cone is the integral of shell volumes: $\textstyle \int _ { 0 } ^ { 1 } r ( 1 - r ) 2 \pi d r = \pi / 3$ .

Third solution Do the $r$ and $z$ integrals first: $\textstyle \int \int r  d r d z = { \frac { 1 } { 6 } }$ . Then the $\theta$ integral is $\int { \frac { 1 } { 6 } } d \theta$ , which gives $\frac { 1 } { 6 }$ times $2 \pi$ . This is the volume $\pi / 3$ —but what is ${ \begin{array} { r } { { \frac { 1 } { 6 } } \ d \theta \ ? } \end{array} }$

The third cone is cut into wedges. The volume of a wedge is ${ \begin{array} { l } { { \frac { 1 } { 6 } } } \end{array} } d \theta$ . It is quite common to do the $\theta$ integral last, especially when it just multiplies by $2 \pi$ . It is not so common to think of wedges.

Question Is the volume ${ \begin{array} { l } { { \frac { 1 } { 6 } } \ d \theta } \end{array} }$ equal to an area $\frac { 1 } { 6 }$ times a thickness $d \theta$ ? Answer No! The triangle in the third cone has area $\frac { 1 } { 2 }$ not $\frac { 1 } { 6 }$ . Thickness is never $d \theta$ .

This cone is typical of a solid of revolution. The axis is in the $z$ direction. The $\theta$ integral yields $2 \pi$ , whether it comes first, second, or third. The $r$ integral goes out to a radius $f ( z )$ , which is 1 for the cylinder and $_ { 1 - z }$ for the cone. The integral $\int \int r \ d r \ { \dot { d } } \theta$ is $\pi ( f ( z ) ) ^ { 2 } =$ area of circular slice. This leaves the $z$ integral $\int \pi ( f ( z ) ) ^ { 2 } d z$ . That is our old volume formula $\int \pi ( f ( x ) ) ^ { 2 } d x$ from Chapter 8; where the slices were cut through the $x$ axis.

EXAMPLE 3 The moment of inertia around the $z$ axis is $\int \int r ^ { 3 } d r \ d \theta \ d z$ . The extra $r ^ { 2 }$ is .distance to axis/2. For the cone this tr?iple integral is $\pi / 1 0$ .

EXAMPLE 4 The moment around the $z$ axis is $\iint r ^ { 2 } d r d \theta d z$ . For the cone this is $\pi / 6$ . The average distance $\overline { r }$ is .moment/=.volume/ $= ( \pi / 6 ) / ( \pi / 3 ) = { \textstyle { \frac { 1 } { 2 } } }$ .

EXAMPLE 5 A sphere of radius $R$ has the boundary $r ^ { 2 } + z ^ { 2 } = R ^ { 2 }$ , in cylindrical coordinates. The outer limit on the $r$ integral is $\scriptstyle { \sqrt { R ^ { 2 } - z ^ { 2 } } }$ . That is not acceptable in difficult problems. To avoid it we now change to coordinates that are natural for a sphere.



# SPHERICAL COORDINATES

The Earth is a solid sphere (or near enough). On its surface we use two coordinates— latitude and longitude. To dig inward or fly outward, there is a third coordinate—the distance $\rho$ from the center. This Greek letter rho replaces $r$ to avoid confusion with cylindrical coordinates. Where $r$ is measured from the $z$ axis, $\rho$ is measured from the origin. Thus $r ^ { 2 } = x ^ { 2 } + y ^ { 2 }$ and $\rho ^ { 2 } = x ^ { 2 } + y ^ { 2 } + z ^ { 2 }$ .

The angle $\theta$ is the same as before. It goes from 0 to $2 \pi$ . It is the longitude, which increases as you travel east arou¤nd t¤he Equator.

The angle $\phi$ is new. It equals 0 at the North Pole and $\pi$ (not $2 \pi$ ) at the South Pole. It is the polar angle, measured down from the $z$ axis. The Equator has a latitude of 0 but a polar angle of $\pi / 2$ (halfway down). Here are some typical shapes:

The angle $\phi$ is constant on a cone from the origin. It cuts the surface in a circle (Figure 14.17b), but not a great circle. The angle $\theta$ is constant along a half-circle from pole to pole. The distance $\rho$ is constant on each inner sphere, starting at the center $\rho = 0$ and moving out to $\rho = R$ .

In spherical coordinates the volume integral is $\int \int \int \rho ^ { 2 } \sin \ \phi \ d \rho \ d \phi \ d \theta$ . To explain that surprising factor $J = \rho ^ { 2 } \sin \phi$ , start with $x = r \cos \theta$ and $y = r$ sin $\theta$ . In spherical coordinates $r$ is $\rho$ sin $\phi$ and $z$ is $\rho$ cos $\phi$ —see the triangle in the figure. So substitute $\rho$ sin $\phi$ for $r$ :

$$
x = \rho \sin \phi \cos \theta , y = \rho \sin \phi \sin \theta , z = \rho \cos \phi .
$$

Remember those two steps, $\rho \phi \theta$ to $r \theta z$ to $x y z$ . We check that $x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = \rho ^ { 2 }$ :

$$
\rho ^ { 2 } ( \sin ^ { 2 } \phi \cos ^ { 2 } \theta + \sin ^ { 2 } \phi \sin ^ { 2 } \theta + \cos ^ { 2 } \phi ) = \rho ^ { 2 } ( \sin ^ { 2 } \phi + \cos ^ { 2 } \phi ) = \rho ^ { 2 } .
$$

The volume integral is explained by Figure 14.17c. That shows a “spherical box” with right angles and curved edges. Two edges are $d \rho$ and $\rho d \phi$ . The third edge is horizontal. The usual $r d \theta$ becomes $\rho$ sin $\phi d \ell$ : Multiplying those lengths gives $d V$ .

Th»e vol»um»e of the box is $d V = \rho ^ { 2 } \sin \phi d \rho d \phi d \theta .$ This is a distance cubed, from $\rho ^ { 2 } d \rho$ .

EXAMPLE 6 A solid ball of radius $R$ has known volume $\begin{array} { r } { V = \frac { 4 } { 3 } \pi R ^ { 3 } } \end{array}$ . Notice the limits:

$$
\int _ { 0 } ^ { 2 \pi } \int _ { 0 } ^ { \pi } \int _ { 0 } ^ { R } \rho ^ { 2 } \sin \phi d \rho d \phi d \theta = \big [ { \textstyle \frac { 1 } { 3 } } \rho ^ { 3 } \big ] _ { 0 } ^ { R } \big [ - \cos \phi \big ] _ { 0 } ^ { \pi } \big [ \theta \big ] _ { 0 } ^ { 2 \pi } = ( { \textstyle \frac { 1 } { 3 } } R ^ { 3 } ) ( 2 ) ( 2 \pi ) .
$$

Question What is the volume above the cone in Figure 14.17 ?

Answer The $\phi$ integral stops at $\begin{array} { r } { [ - \cos \phi ] _ { 0 } ^ { \pi / 3 } = \frac { 1 } { 2 } } \end{array}$ . The volume is $\scriptstyle ( { \frac { 1 } { 3 } } R ^ { 3 } ) ( { \frac { 1 } { 2 } } ) ( 2 \pi )$ .

EXAMPLE 7 The surface area of a sphere is $A = 4 \pi R ^ { 2 }$ . Forget the $\rho$ integral:

$$
A = \int _ { 0 } ^ { 2 \pi } \int _ { 0 } ^ { \pi } R ^ { 2 } \sin \phi d \phi d \theta = R ^ { 2 } \big [ - \cos \phi \big ] _ { 0 } ^ { \pi } \big [ \theta \big ] _ { 0 } ^ { 2 \pi } = R ^ { 2 } ( 2 ) ( 2 \pi ) .
$$

After those examples from geometry, here is the real thing from science. I want to compute one of the most important triple integrals in physics—“the gravitational attraction of a solid sphere.” For some reason Isaac Newton had trouble with this integral. He refused to publish his masterpiece on astronomy until he had solved it. I think he didn’t use spherical coordinates—and the integral is not easy even now.

The answer that Newton finally found is beautiful. The sphere acts as if all its mass were concentrated at the center. At an outside point $( 0 , 0 , D )$ , the force of gravity is proportional to $1 / D ^ { 2 }$ . The force from a uniform solid sphere equals the force from a point mass, at every outside point $P$ . That is exactly what Newton wanted and needed, to explain the solar system and to prove Kepler’s laws.

Here is the difficulty. Some parts of the sphere are closer than $D$ , some parts are farther away. The actual distance $q$ , from the outside point $P$ to a typical inside point, is shown in Figure 14.18. The average distance $\overline { { q } }$ to all points in the sphere is not $D$ . But what Newton needed was a different average, and by good luck or some divine calculus it works perfectly: The average of $1 / q$ is $1 / D$ . This gives the potential energy:

$$
p o t e n t i a l a t p o i n t P = \int \int _ { \mathrm { s p h e r e } } ^ { } { \frac { 1 } { q } } d V = { \frac { \mathrm { V o l u m e ~ o f ~ s p h e r e } } { D } } .
$$

A small volume $d V$ at the distance $q$ contributes $d V / q$ to the potential (Section 8:6; with density 1). The integral adds the contributions from the whole sphere. Equation (2) says that the potential at $r = D$ is not changed when the sphere is squeezed to the center. The potential equals the whole volume divided by the single distance $D$ .

Important point: The average of $1 / q$ is $1 / D$ and not $1 / \overline { { q } }$ . The average of $\frac { 1 } { 2 }$ and $\textstyle { \frac { 1 } { 4 } }$ is not $\frac 1 3$ . Smaller point: I wrote “sphere” where I should have written “ball.” The sphere is solid: $0 \leqslant \rho \leqslant R , 0 \leqslant \phi \leqslant \pi , 0 \leqslant \theta \leqslant 2 \pi$ . What about the force ? For the small volume it is proportional to $d V / q ^ { 2 }$ (this is the inverse square law). But force is a vector, pulling the outside point toward $d V$ —not toward the center of the sphere. The figure shows the geometry and the symmetry. We want the z component of the force. (By symmetry the overall $x$ and $y$ components are zero.) The angle between the force vector and the $z$ axis is $\alpha$ , so for the $z$ component we multiply by cos $\alpha$ . The total force comes from the integral that Newton discovered:

$$
f o r c e a t p o i n t P = \iint _ { \mathrm { s p h e r e } } \frac { \cos \alpha } { q ^ { 2 } } d V = \frac { \mathrm { v o l u m e ~ o f ~ s p h e r e } } { D ^ { 2 } } .
$$

I will compute the integral (2) and leave you the privilege of solving (3). I mean that word seriously. If you have come this far, you deserve the pleasure of doing what at one time only Isaac Newton could do. Problem 26 offers a suggestion (just the law of cosines) but the integral is yours.

The law of cosines also helps with (2). For?the triangle in the figure it gives $q ^ { 2 } = D ^ { 2 } - 2 \rho D \cos { \phi } + \rho ^ { 2 } .$ Call this whole quantity $u$ . We do the surface integral first . $\dot { \boldsymbol { d } } \phi$ and $d \theta$ with $\rho$ fixed/. Then $\scriptstyle q ^ { 2 } = u$ and $q = { \sqrt { u } }$ and? $d u = 2 \rho D \sin \phi d \phi$ :

$$
\int _ { 0 } ^ { 2 \pi } \int _ { 0 } ^ { \pi } { \frac { \rho ^ { 2 } \sin \phi d \phi d \theta } { q } } = \int { \frac { 2 \pi \rho ^ { 2 } } { 2 \rho D } } { \frac { d u } { \sqrt { u } } } = \left[ { \frac { 2 \pi \rho } { D } } { \sqrt { u } } \right] _ { \phi = 0 } ^ { \phi = \pi } .
$$

$2 \pi$ came from the» $\theta$ integral. The integral of $d u / { \sqrt { u } }$ is $2 \sqrt { u }$ . Since cos $\phi = - 1$ at the upper limit, $u$ is $D ^ { 2 } + 2 \rho D + \rho ^ { 2 }$ . The square root of $u$ is $D + \rho$ . At the lower limit cos $\phi = + 1$ and $u = D ^ { 2 } - 2 \rho D + \rho ^ { 2 }$ . This is another perfect square— its square root is $D - \rho$ . The surface integral (4) with fixed $\rho$ is

$$
\int \int { \frac { d A } { q } } = { \frac { 2 \pi \rho } { D } } \big [ ( D + \rho ) - ( D - \rho ) \big ] = { \frac { 4 \pi \rho ^ { 2 } } { D } } .
$$

Last comes the $\rho$ integral: $\textstyle { \int _ { 0 } ^ { R } 4 \pi \rho ^ { 2 } d \rho / D = \frac { 4 } { 3 } \pi R ^ { 3 } } / { D }$ . This proves formula (2): potential equals volume of the sphere divided by $D$ .

Note 1 Physicists are also happy about equation (5). The average of $1 / q$ is $1 / D$ not only over the solid sphere but over each spherical shell of area $4 \pi \rho ^ { 2 }$ . The shells can have different densities, as they do in the Earth, and still Newton is correct. This also applies to the force integral (3)—each separate shell acts as if its mass were concentrated at the center. Then the final $\rho$ integral yields this property for the solid sphere.

Note 2 Physicists also know that force is minus the derivative of potential. The derivative of (2) with respect to $D$ produces the force integral (3). Problem 27 explains this shortcut to Equation (3).

EXAMPLE 8 Everywhere inside a hollow sphere the force of gravity is zero.

When $D$ is smaller than $\rho$ , the lower limit $\sqrt { u }$ in the integral (4) changes from $D - \rho$ to $\rho - D$ . That way the square root stays positive. This changes the answer in (5) to $4 \pi \rho ^ { 2 } / \rho$ , so the potential no longer depends on $D$ . The potential is constant inside the hollow shell. Since the force comes from its derivative, the force is zero.

A more intuitive proof is in the second figure. The infinitesimal areas on the surface are proportional to $q ^ { 2 }$ and $\scriptstyle Q ^ { 2 }$ . But the distances to those areas are $q$ and $\boldsymbol { Q }$ , so the forces involve $1 / q ^ { 2 }$ and $1 / Q ^ { 2 }$ (the inverse square law). Therefore the two areas exert equal and opposite forces on the inside point, and they cancel each other. The total force from the shell is zero.

I believe this zero integral is the reason that the inside of a car is safe from lightning. Of course a car is not a sphere. But electric charge distributes itself to keep the surface at constant potential. The potential stays constant inside—therefore no force. The tires help to prevent conduction of current (and electrocution of driver).

P.S. Don’t just step out of the car. Let a metal chain conduct the charge to the ground. Otherwise you could be the conductor.

# CHANGE OF COORDINATES—STRETCHING FACTOR $J$

Once more we look to calculus for a formula. We need the volume of a small curved box in any ${ { u v w } }$ coordinate system. The $r \theta z$ box and the $\rho \phi \theta$ box have right angles, and their volumes were read off from the geometry (stretching factors $J = r$ and $J = \rho ^ { 2 } \sin \phi$ in Figures 14.15 and 14.17). Now we change from $x y z$ to other coordinates uvw—which are chosen to fit the problem.

Going from $x y$ to $u v$ , the area $d A = J d u d v$ was a 2 by 2 determinant. In three dimensions the determinant is 3 by 3. The matrix is always the “Jacobian matrix,” containing first derivatives. There were four derivatives from $x y$ to $u v$ , now there are nine from $x y z$ to ${ { u v w } }$ .

Remember that a 3 by 3 determinant is the sum of six terms (Section 11:5). One term in $J$ is $( \partial x / \partial u ) ( \partial y / \partial v ) ( \partial z / \partial w )$ , along the main diagonal. This comes from pure stretching, and the other five terms allow for rotation. The best way to exhibit the formula is for spherical coordinates—where the nine derivatives are easy but the determinant is not:

EXAMPLE 9 Find the factor $J$ for $x = \rho$ sin $\phi$ cos $\theta$ ; $y = \rho$ sin $\phi$ sin $\theta$ ; $z = \rho \cos \phi$ .

$$
J = \frac { \partial ( x , y , z ) } { \partial ( \rho , \phi , \theta ) } = \left| \begin{array} { c c c c } { { \sin \phi \cos \theta } } & { { \rho \cos \phi \cos \theta } } & { { - \rho \sin \phi \sin \theta } } \\ { { } } & { { } } & { { J } } \\ { { \sin \phi \sin \theta } } & { { \rho \cos \phi \sin \theta } } & { { \rho \sin \phi \cos \theta } } \\ { { } } & { { } } & { { - \rho \sin \phi } } & { { 0 } } \end{array} \right| .
$$

The determinant has six terms, but two are zero—because of the zero in the corner. The other four terms are $\rho ^ { 2 } \sin \phi \ \cos ^ { 2 } \phi \ \sin ^ { 2 } \theta$ and $\rho ^ { 2 } \sin \phi \ \cos ^ { 2 } \phi \ \cos ^ { 2 } \theta$ and $\rho ^ { 2 } \sin ^ { 3 } \phi \ \sin ^ { 2 } \theta$ and $\rho ^ { 2 } \sin ^ { 3 } \phi \ \cos ^ { 2 } \theta .$ Add the first two (note $\sin ^ { 2 } \theta + \cos ^ { 2 } \theta )$ 1 and separately add the second two. Then add the sums to reach $J = \rho ^ { 2 } \sin \phi$ .

Geometry already gave this answer. For most ${ \boldsymbol { u } } { \boldsymbol { v } } { \boldsymbol { w } }$ variables, use the determinant.