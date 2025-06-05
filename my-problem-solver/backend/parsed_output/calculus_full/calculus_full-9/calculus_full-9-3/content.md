# 9.3 Slope, Length, and Area for Polar Curves

The previous sections introduced polar coordinates and polar equations and polar graphs. There was no calculus! We now tackle the problems of area (integral calculus) and slope (differential calculus), when the equation is $r = F ( \theta )$ . The use of $F$ instead of $f$ is a reminder that the slope is not $d F / d \theta$ and the area is not $\int F ( \theta ) d \theta$ .

Start with area. The region is always divided into small pieces—what is their shape ? Look between the angles $\theta$ and $\theta + \Delta \theta$ in Figure 9.6a. Inside the curve is a narrow wedge—almost a triangle, with $\Delta \theta$ as its small angle. If the radius is constant the wedge is a sector of a circle. It is a piece of pie cut at the extremely narrow angle $\Delta \theta$ . The area of that piece is a fraction (the angle $\Delta \theta$ divided by the whole angle $2 \pi$ ) of the whole area $\pi r ^ { 2 }$ of the circle:



$$
a r e a o f w e d g e = \frac { \Delta \theta } { 2 \pi } \pi r ^ { 2 } = \frac { 1 } { 2 } r ^ { 2 } \Delta \theta = \frac { 1 } { 2 } \left[ F ( \theta ) \right] ^ { 2 } \Delta \theta .
$$

We admit that the exact shape is not circular. The true radius $F ( \theta )$ varies with $\theta -$ but in a narrow angle that vari»ation is small». When we add up the wedges and let $\Delta \theta$ approach zero, the area becomes an integral.

$$
a r e a = \int { \frac { 1 } { 2 } } r ^ { 2 } d \theta = \int { \frac { 1 } { 2 } } \left[ F ( \theta ) \right] ^ { 2 } d \theta .
$$

EXAMPLE 1 Find the area inside the circle $r = \cos \theta$ of radius $\frac { 1 } { 2 }$ (Figure 9.6).

$$
a r e a = \int _ { 0 } ^ { 2 \pi } { \frac { 1 } { 2 } } \cos ^ { 2 } \theta d \theta = { \frac { \cos \theta \sin \theta + \theta } { 4 } } \Biggr ] _ { 0 } ^ { 2 \pi } = { \frac { 2 \pi } { 4 } } .
$$

That is wrong! The correct area of a circle of radius $\textstyle { \frac { 1 } { 2 } }$ is $\pi / 4$ . The mistake is that we went twice around the circle as $\theta$ increased to $2 \pi$ . Integrating from $\theta$ to $\pi$ gives $\pi / 4$ .

EXAMPLE 2 Find the area between the circles $r = \cos \theta$ and $\begin{array} { r } { r = \frac { 1 } { 2 } } \end{array}$

The circles cross at the points where $r = \cos \theta$ agrees with $\begin{array} { r } { r = \frac { 1 } { 2 } } \end{array}$ . Figure 9.6 shows these points at $\pm 6 0 ^ { \circ }$ , or $\theta = \pm \pi / 3$ . Those are the limits of integration, where cos $\theta =$ $\frac { 1 } { 2 }$ .

The integral adds up the difference between two wedges,one out to $r = \cos \theta$ and a smaller one with r D 21 :

$$
a r e a = \int _ { - \pi / 3 } ^ { \pi / 3 } { \frac { 1 } { 2 } } \left[ ( \cos \theta ) ^ { 2 } - \left( { \frac { 1 } { 2 } } \right) ^ { 2 } \right] d \theta .
$$

Note tha»t chopped wedges have area $\begin{array} { r } { \frac { 1 } { 2 } ( F _ { 1 } ^ { 2 } - F _ { 2 } ^ { 2 } ) \Delta \theta } \end{array}$ and not ${ \textstyle \frac { 1 } { 2 } } ( F _ { 1 } - F _ { 2 } ) ^ { 2 } \Delta \theta .$ .

EXAMPLE 3 Find the area between the cardioid $r = 1 + \cos \theta$ and the circle $r = 1$ .

$$
a r e a = \int _ { - \pi / 2 } ^ { \pi / 2 } { \frac { 1 } { 2 } } \left[ ( 1 + \cos \theta ) ^ { 2 } - 1 ^ { 2 } \right] d \theta \quad \left( { \mathrm { l i m i t s ~ } } \theta = \pm { \frac { \pi } { 2 } } { \mathrm { ~ w h e r e ~ } } 1 + \cos \theta = 1 \right)
$$

# SLOPE OF A POLAR CURVE

Where is the highest point on the cardioid $r = 1 + \cos \theta \ ?$ What is the slope at $\theta = \pi / 4 ?$ Those are not the most important questions in calculus, but still we should know how to answer them. I will describe the method quickly, by switching to rectangular coordinates:

$$
x = r \cos \theta = ( 1 + \cos \theta ) \cos \theta \qquad { \mathrm { a n d } } \qquad y = r \sin \theta = ( 1 + \cos \theta ) \sin \theta .
$$

For the highest point, maximize $y$ by setting its derivative to zero:

$$
d y / d \theta = ( 1 + \cos \theta ) ( \cos \theta ) + ( - \sin \theta ) ( \sin \theta ) = 0 .
$$

Thus cos $\theta + \cos 2 \theta = 0$ , which happens at $6 0 ^ { \circ }$ . The height is $y = ( 1 + \textstyle { \frac { 1 } { 2 } } ) ( \sqrt { 3 } / 2 )$ .

For the slope, use the chain rule $d y / d \theta = ( d y / d x ) ( d x / d \theta )$ :

$$
{ \frac { d y } { d x } } = { \frac { d y / d \theta } { d x / d \theta } } = { \frac { ( 1 + \cos \theta ) ( \cos \theta ) + ( - \sin \theta ) ( \sin \theta ) } { ( 1 + \cos \theta ) ( - \sin \theta ) + ( - \sin \theta ) \cos \theta } } .
$$

Equations (3) and (4) avoid the awkward (or impossible) step of eliminating $\theta$ . Instead of trying to find $y$ as a function of $x$ , we keep $x$ and $y$ as functions of $\theta$ . At $\theta = \pi / 4$ , the ratio in equation (4) yields $d y / d x = - 1 / ( 1 + \sqrt { 2 } )$ .

Problem 18 finds a general formula for the slope, using $d y / d x = ( d y / d \theta ) / ( d x / d \theta )$ . Problem 20 finds a more elegant formula, by looking at the question differently.

# LENGTH OF A POLAR CURVE

The length integral always starts with $d s = \sqrt { ( d x ) ^ { 2 } + ( d y ) ^ { 2 } }$ . A polar curve has $x = r$ cos $\theta = F ( \theta ) \cos \theta$ and $y = F ( \theta ) \sin \theta$ . Now take derivatives by the product rule:

$$
d x = ( F ^ { \prime } ( \theta ) \cos \theta - F ( \theta ) \sin \theta ) d \theta \qquad { \mathrm { a n d } } \qquad d y = ( F ^ { \prime } ( \theta ) \sin \theta + F ( \theta ) \cos \theta ) d \theta .
$$

Squaring and adding (note $\cos ^ { 2 } \theta + \sin ^ { 2 } \theta .$ ) gives the element of length $d s$ :

$$
d s = { \sqrt { \left[ F ^ { \prime } ( \theta ) \right] ^ { 2 } + \left[ F ( \theta ) \right] ^ { 2 } } } d \theta .
$$

The figure shows $( d s ) ^ { 2 } = ( d r ) ^ { 2 } + ( r d \theta ) ^ { 2 }$ , the same formula with different letters.   
The total arc length is $\int d s$ .

The area of a surface of revolution is $\int 2 \pi y d s$ (around the $x$ axis) or $\int 2 \pi x d s$ (around the $y$ axis). Write $x , y$ , and $d s$ in terms of $\theta$ and $d \theta$ . Then integrate.

EXAMPLE 4 The circle $r = \cos \theta$ has $d s = { \sqrt { 1 } } d \theta$ . So its length is $\pi$ (not $2 \pi$ !!— don’t go around twice). Revolved around the $y$ axis the circle yields a doughnut with no hole. Since $x = r$ cos $\theta = \cos ^ { 2 } \theta$ , the surface area of the doughnut is

$$
\int 2 \pi x d s = \int _ { 0 } ^ { \pi } 2 \pi \cos ^ { 2 } \theta d \theta = \pi ^ { 2 } .
$$

EXAMPLE 5 The length of $r = 1 + \cos \theta$ is, by symmet»ry, double the integral from 0 to $\pi$ :

$$
\begin{array} { l } { { \displaystyle \mathrm { l e n g t h ~ o f ~ c a r d i o i d } = 2 \int _ { 0 } ^ { \pi } \sqrt { ( - \sin \theta ) ^ { 2 } + ( 1 + \cos \theta ) ^ { 2 } } d \theta } } \\ { { \displaystyle \qquad = 2 \int _ { 0 } ^ { \pi } \sqrt { 2 + 2 \cos \theta } d \theta = 4 \int _ { 0 } ^ { \pi } \cos \displaystyle \frac { \theta } { 2 } d \theta = 8 . } } \end{array}
$$

We substituted $4 \cos ^ { 2 } { \frac { 1 } { 2 } } \theta$ for $2 + 2 \cos \theta$ in the square root. It is possible to skip symmetry and inte»grate fro»m 0 to $2 \pi$ —but that needs the absolute value $\scriptstyle { \big | } \cos { \frac { 1 } { 2 } } \theta { \big | }$ to maintain a positive square root.

EXAMPLE 6 The logarithmic spiral $r = e ^ { - \theta }$ has $d s = { \sqrt { e ^ { - 2 \theta } + e ^ { - 2 \theta } } } d \theta$ . It spirals to zero as $\theta$ goes to infinity, and the total length is finite:

$$
\int d s = \int _ { 0 } ^ { \infty } { \sqrt { 2 } } e ^ { - \theta } d \theta = - { \sqrt { 2 } } e ^ { - \theta } \exists _ { 0 } ^ { \infty } = { \sqrt { 2 } } .
$$

Revolve this spiral for a mathematical seashell with area $\int _ { 0 } ^ { \infty } ( 2 \pi e ^ { - \theta } \cos \theta ) \sqrt { 2 } e ^ { - \theta } d \theta$ .