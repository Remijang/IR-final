# 9.4 Complex Numbers

Real numbers are sufficient for most of calculus. Starting from $x ^ { 2 } + 4$ , its integral ${ \frac { 1 } { 3 } } x ^ { 3 } + 4 x + C$ is also real. If we are given $x ^ { 3 } - 1$ , its derivative $3 x ^ { 2 }$ is real. But the roots (or zeros) of those polynomials are complex numbers:

$$
x ^ { 2 } + 4 = 0 \quad a n d \quad x ^ { 3 } - 1 = 0 \quad h a \nu e \ c o m p l e x \ s o l u t i o n s .
$$

We expect two square roots of $^ { - 4 }$ . There are three cube roots of 1. Complex numbers are unavoidable, in order to find $n$ roots for each polynomial of degree $n$ .

This section explains how to work with complex numbers. You will see their relation to polar coordinates. At the end, we use them to solve differential equations.

Start with the imaginary number $i$ . Everybody knows that $x ^ { 2 } = - 1$ has no real solution. When you square a real number, the result is never negative. So the world has agreed on a solution called $i$ . (Except that electrical engineers call it $j . )$ Imaginary numbers follow the normal rules of addition, subtraction, multiplication, and division, with one difference: Whenever $i ^ { 2 }$ appears it is replaced by $^ { - 1 }$ . In particular $- i$ times $- i$ gives $+ i ^ { 2 } = - 1$ . In other words, $- i$ is also a square root of $^ { - 1 }$ . There are two solutions . $i$ and $- i$ / to the equation $x ^ { 2 } + 1 = 0$ .

Finding cube roots of 1 will stretch us further. We need complex numbers—real plus imaginary.

9B A complex number (say $1 + 3 i ^ { \cdot }$ ) is the sum of a real number .1/ and a pure imaginary number .3i/. Addition keeps those parts separate; multiplication uses $i ^ { 2 } = - 1$ : $\begin{array} { r l } { \bigg | } & { \quad \mathrm { A d d i t i o n } : \quad ( 1 + 3 i ) + ( 1 + 3 i ) = 1 + 1 + i ( 3 + 3 ) = 2 + 6 i } \\ & { \quad \mathrm { M u l t i p l i c a t i o n } : \quad ( 1 + 3 i ) ( 1 + 3 i ) = 1 + 3 i + 3 i + 9 i ^ { 2 } = - 8 + 6 i . } \end{array}$

Adding $1 + 3 i$ to $5 - i$ is easy $( 6 + 2 i )$ . Multiplying is longer, but you see the rules:

$$
( 1 + 3 i ) ( 5 - i ) = 5 + 1 5 i - i - 3 i ^ { 2 } = 8 + 1 4 i .
$$

The point is this: We don’t have to imagine any more new numbers. After accepting $i$ , the rest is straightforward. A real number isjust a complex number with no imaginary part! When $1 + 3 i$ combines with its “complex conjugate” $1 - 3 i$ —adding or multiplying—the answer is real:

$$
\begin{array} { l } { { ( 1 + 3 i ) + ( 1 - 3 i ) { = } 2 \quad ( r e a l ) } } \\ { { ( 1 + 3 i ) ( 1 - 3 i ) { = } 1 - 3 i + 3 i - 9 i ^ { 2 } { = } 1 0 . \quad ( r e a l ) } } \end{array}
$$

The complex conjugate offers a way to do division, by making the denominator real:

$$
{ \frac { 1 } { 1 + 3 i } } = { \frac { 1 } { 1 + 3 i } } { \frac { 1 - 3 i } { 1 - 3 i } } = { \frac { 1 - 3 i } { 1 0 } } \qquad { \mathrm { a n d } } \qquad { \frac { 1 } { x + i y } } = { \frac { 1 } { x + i y } } { \frac { x - i y } { x - i y } } = { \frac { x - i y } { x ^ { 2 } + y ^ { 2 } } } .
$$

9C The complex number $x + i y$ has real part $x$ and imaginary part $y$ . Its complex conjugate is $x - i y$ . The product $( x + i y ) ( x - i y )$ equals $x ^ { 2 } + y ^ { 2 } = r ^ { 2 }$ . The absolute value (or modulus) is $r = | x + i y | = \sqrt { x ^ { 2 } + y ^ { 2 } }$ .

# THE COMPLEX PLANE

Complex numbers correspond to points in a plane. The number $1 + 3 i$ corresponds to the point .1; 3/. Similarly $x + i y$ is paired with $( x , y )$ —which is $x$ units along the “real axis” and $y$ units up the “imaginary axis.” The ordinary plane turns into the complex plane. The absolute value $r$ is the same as the polar coordinate $r$ (Figure 9.8a).

The figure shows two more copies of the complex plane. The one in the middle is for addition and subtraction. It uses rectangular coordinates. The one on the right is for multiplication and division and squaring. It uses polar coordinates. In squaring a complex number, $r$ is squared and $\theta$ is doubled—as the right figure and equation (3) both show.

Adding complex numbers is like adding vectors (Chapter 11). The real parts give $_ { 3 - 1 }$ and the imaginary parts give $1 + 1$ . The vector sum $( 2 , 2 )$ corresponds to the complex sum $2 + 2 i$ . The complex conjugate $3 - i$ is the mirror image across the real axis . $i$ reversed to $- i$ /. The connection to $r$ and $\theta$ is the same as before (you see it in the triangle):

$$
x = r \cos \theta \quad a n d \quad y = r \sin \theta \quad s o t h a t \quad x + i y = r ( \cos \theta + i \sin \theta ) .
$$

In the third figure, $1 + i$ has $r = { \sqrt { 2 } }$ and $\theta = \pi / 4$ . The polar form is ${ \sqrt { 2 } } \cos \pi / 4 +$ ${ \sqrt { 2 } } i$ sin $\pi / 4$ . When this number is squared, its $4 5 ^ { \circ }$ angle becomes $9 0 ^ { \circ }$ : The square is $( 1 + i ) ^ { 2 } = 1 + 2 i - 1 = 2 i$ . Its polar form is 2 cos $\pi / 2 + 2 i$ sin $\pi / 2$ .

9D Multiplication adds angles, division subtracts angles, and sq?uaring doubles angles. The absolute values are multiplied, divided, and squared:

$$
( r \cos \theta + i r \sin \theta ) ^ { 2 } = r ^ { 2 } \cos 2 \theta + i r ^ { 2 } \sin 2 \theta .
$$

For $n$ th powers we reach $r ^ { n }$ and $n \theta$ . For square roots, $r$ goes to $\sqrt { r }$ and $\theta$ goes to ${ \frac { 1 } { 2 } } \theta$ . The number $^ { - 1 }$ is at $1 8 0 ^ { \circ }$ , so its square root $i$ is at $9 0 ^ { \circ }$ .

To see why $\theta$ is doubled in equation (3), factor out $r ^ { 2 }$ and multiply as usual:

$$
( \cos \theta + i \sin \theta ) ( \cos \theta + i \sin \theta ) = \cos ^ { 2 } \theta - \sin ^ { 2 } \theta + 2 i \sin \theta \cos \theta .
$$

The right side is c $\cos 2 \theta + i \sin 2 \theta$ . The double-angle formulas from trigonometry match the squaring of complex numbers. The cube would be cos $3 \theta + i$ sin $3 \theta$ (because $2 \theta$ and $\theta$ add to $3 \theta$ , and $r$ is still 1). The $n$ th power is in de Moivre’s formula:

$$
( \cos \theta + i \sin \theta ) ^ { n } = \cos n \theta + i \sin n \theta .
$$

With $n = - 1$ we get co $\operatorname { s } ( - \theta ) + i \ \sin ( - \theta )$ —which is cos $\theta - i$ sin $\theta$ , the complex conjugate:

$$
{ \frac { 1 } { \cos \theta + i \sin \theta } } = { \frac { 1 } { \cos \theta + i \sin \theta } } { \frac { \cos \theta - i \sin \theta } { \cos \theta - i \sin \theta } } = { \frac { \cos \theta - i \sin \theta } { 1 } } .
$$

We are almost touching Euler’s formula, the key to all numbers on the unit circle:

$$
E u l e r ^ { \prime } s f o r m u l a : \qquad \cos \theta + i \sin \theta = e ^ { i \theta } .
$$

Squaring both sides gives $( e ^ { i \theta } ) ( e ^ { i \theta } ) = e ^ { 2 i \theta }$ . That is equation (3). The $^ { - 1 }$ power is $\stackrel { \cdot } { 1 } / e ^ { i \theta } = e ^ { - i \theta }$ . That is equation (5). Multiplying any $e ^ { i \theta }$ by $e ^ { i \phi }$ produces $e ^ { i ( \theta + \phi ) }$ . The special case $\phi = \theta$ gives the square, and the special case $\phi = - \theta$ gives $e ^ { i \theta } e ^ { - i \theta } =$ 1.

Euler’s formula appeared in Section 6.7, by changing $x$ to $i \theta$ in the series for $e ^ { x }$ :

$$
e ^ { x } = 1 + x + { \frac { x ^ { 2 } } { 2 } } + { \frac { x ^ { 3 } } { 6 } } + \cdots \quad { \mathrm { b e c o m e s } } \quad e ^ { i \theta } = 1 + i \theta - { \frac { \theta ^ { 2 } } { 2 } } - i { \frac { \theta ^ { 3 } } { 6 } } + \cdots .
$$

A highlight of Chapter 10 is to recognize two new series on the right. The real terms $\begin{array} { r } { 1 - \frac { 1 } { 2 } \theta ^ { 2 } + \cdots } \end{array}$ add up to cos $\theta$ . The imaginary part $\begin{array} { r } { \theta - \frac { 1 } { 6 } \theta ^ { 3 } + \cdots } \end{array}$ adds up to sin $\theta$ . Therefore $e ^ { i \theta }$ equals cos $\theta + i$ sin $\theta$ . It is fantastic that the most important periodic functions in all of mathematics come together in this graceful way.

We learn from Euler (pronounced oiler) that $e ^ { 2 \pi i } = 1$ . The cosine of $2 \pi$ is 1, the sine is zero. If you substitute $x = 2 \pi i$ into the infinite series, somehow everything cancels except the 1—this is almost a miracle. From the viewpoint of angles, $\theta = 2 \pi$ carries us around a full circle and back to $e ^ { 2 \pi i } = 1$ .

Multiplying Euler’s formula by $r$ , we have a third way to write a complex number:

$$
E { \nu } e r y ~ c o m p l e x ~ n u m b e r ~ i s ~ x + i y = r ~ \cos \theta + i r ~ \sin \theta = r e ^ { i \theta } .
$$

EXAMPLE 1 $2 e ^ { i \theta }$ times $3 e ^ { i \theta }$ equals $6 e ^ { 2 i \theta }$ . For $\theta = \pi / 2 , 2 i$ times $3 i$ is $^ { - 6 }$ .

EXAMPLE 2 Find $w ^ { 2 }$ and $w ^ { 4 }$ and $w ^ { 8 }$ and $w ^ { 2 5 }$ when $w = e ^ { i \pi / 4 }$ .

Solution $e ^ { i \pi / 4 }$ is $1 / { \sqrt { 2 } } + i / { \sqrt { 2 } }$ . Note that $\begin{array} { r } { r ^ { 2 } = \frac { 1 } { 2 } + \frac { 1 } { 2 } = 1 . } \end{array}$ Now watch angles:

$$
w ^ { 2 } = e ^ { i \pi / 2 } = i \quad w ^ { 4 } = e ^ { i \pi } = - 1 \quad w ^ { 8 } = 1 \quad w ^ { 2 5 } = w ^ { 8 } w ^ { 8 } w ^ { 8 } w = w .
$$

Figure 9.9 shows the eight powers of $w$ . They are the eighth roots of 1.

$$
w ^ { 3 } \bigoplus _ { w ^ { 5 } } ^ { w ^ { 2 } = i } w ^ { w = e ^ { i \pi / 4 } } \qquad { \mathrm { ( L ) } } ^ { - { \frac { 1 } { 2 } } + { \frac { \sqrt { 3 } } { 2 } } i } ,
$$

EXAMPLE 3 . $( x ^ { 2 } + 4 = 0 )$ The square roots of $^ { - 4 }$ are $2 i$ and $- 2 i$ . Instead of $( i ) ( i ) = - 1$ we have $( 2 i ) ( 2 i ) = - 4 .$ If Euler insists, we write $2 i$ and $- 2 i$ as $2 e ^ { i \pi / 2 }$ and 2ei3=2.

EXAMPLE 4 (The cube roots of 1) In rectangular coordinates we have to solve $( x + i y ) ^ { 3 } = 1$ , which is not easy. In polar coordinates this same equation is $r ^ { 3 } e ^ { 3 i \theta } = 1$ . Immediately $r = 1$ . The angle $\theta$ can be $2 \pi / 3$ or $4 \pi / 3$ or $6 \pi / 3$ —the cube roots in the figure are evenly spaced:

$$
( e ^ { 2 \pi i / 3 } ) ^ { 3 } = e ^ { 2 \pi i } = 1 \quad ( e ^ { 4 \pi i / 3 } ) ^ { 3 } = e ^ { 4 \pi i } = 1 \quad ( e ^ { 6 \pi i / 3 } ) ^ { 3 } = e ^ { 6 \pi i } = 1 .
$$

You see why the angle $8 \pi / 3$ gives nothing new. It completes a full circle back to $2 \pi / 3$ .

The nth roots of 1 are $e ^ { 2 \pi i / n }$ , $e ^ { 4 \pi i / n }$ , : : :, 1. There are n of them.   
They lie at angles $2 \pi / n$ , $4 \pi / n$ , : : :, $2 \pi$ around the unit circle.

# SOLUTION OF DIFFERENTIAL EQUATIONS

The algebra of complex numbers is now applied to the calculus of complex functions. The complex number is $c$ , the complex function is $e ^ { c t }$ . It will solve the2equations $y ^ { \prime \prime } { = } - 4 y$ and $y ^ { \prime \prime \prime } = y$ , by connecting them to $c ^ { 2 } = - 4$ and $c ^ { 3 } = 1$ . Chapter 16 does the same for all lineardifferential equationswith constant coefficients—this is an optional preview.

Please memorize the one key idea: Substitute $y = e ^ { c t }$ into the differential equation and solve for $c$ . Each derivative brings a factor $c$ , so $y ^ { \prime } = c e ^ { c t }$ and $y ^ { \prime \prime } { = } c ^ { 2 } e ^ { c t }$ :

$$
d ^ { 2 } y / d t ^ { 2 } = - 4 y \mathrm { l e a d s t o } c ^ { 2 } e ^ { c t } = - 4 e ^ { c t } , { \mathrm { w h i c h ~ g i v e s ~ } } c ^ { 2 } = - 4 .
$$

For this differential equation, $c$ must be a square root of $^ { - 4 }$ . We know the candidates . ${ \dot { c } } = 2 i$ and $c = - 2 i$ /. The equation has two “pure exponential solutions” $e ^ { c t }$ :

$$
y = e ^ { 2 i t } \qquad \mathrm { a n d } \qquad y = e ^ { - 2 i t } .
$$

Their combinations $y = A e ^ { 2 i t } + B e ^ { - 2 i t }$ give all solutions. In Chapter 16 we will choose the two numbers $A$ and $B$ to match two initial conditions at $t = 0$ .

The solution $y = e ^ { 2 i t } = \cos 2 t + i$ sin $2 t$ is complex. The differential equation is real. For real $y$ ’s, take the real and imaginary parts of the complex solutions:

$$
y _ { \mathrm { r e a l } } = \cos 2 t ~ { \mathrm { a n d } } ~ y _ { \mathrm { i m a g i n a r y } } = \sin 2 t .
$$

These are the “pure oscillatory solutions.” When $y = e ^ { 2 i t }$ travels around the unit circle, its imaginary part sin $2 t$ moves up and down. (It is like the ball and its shadow in Section 1.4, but twice as fast because of $2 t$ .) The real part cos $2 t$ goes backward and forward. By the chain rule, the second derivative of cos $2 t$ is 4 cos 2t . Thus $d ^ { 2 } y / d t ^ { 2 } = - 4 y$ and we have real solutions.

EXAMPLE 5 Find threesolutions and then three real solutions to $d ^ { 3 } y / d t ^ { 3 } = y$ .

Key step: Substitute $y = e ^ { c t }$ . The result is $c ^ { 3 } e ^ { c t } = e ^ { c t }$ . Thus $c ^ { 3 } = 1$ and $c$ is a cube root of 1. The candidate $c = 1$ gives $y = e ^ { t }$ (our first solution|). |The next $c$ i?s complex:

$$
c = e ^ { 2 \pi i / 3 } = - { \frac { 1 } { 2 } } + i { \frac { \sqrt { 3 } } { 2 } } y i e l d s y = e ^ { c t } = e ^ { - t / 2 } e ^ { i \sqrt { 3 } t / 2 } .
$$

The real part of the exponent leads to the absolute value $| y | = e ^ { - t / 2 }$ . It decreases as $t$ gets larger, so $y$ moves toward zero. At the same time, the factor $ e ^ { i \sqrt { 3 } t / 2 }$ goes around the unit circle. Therefore $y$ spirals in to zero (Figure 9.10). So does its complex

conjugate, which is the third exponential. Changing $i$ to $- i$ in (11) gives the third cube root of 1 and the third solution e t=2e i 3t=2.

The first real solution is $y = e ^ { t }$ . The others are the two parts of the spiral:

$$
y _ { \mathrm { r e a l } } = e ^ { - t / 2 } \cos { \sqrt { 3 } t } / 2 \qquad \mathrm { a n d } \qquad y _ { \mathrm { i m a g i n a r y } } = e ^ { - t / 2 } \sin { \sqrt { 3 } t } / 2 .
$$

That is $r$ cos $\theta$ and $r$ sin $\theta$ . It is the ultimate use (until Chapter 16) of polar coordinates and complex numbers. We might have discovered cos $2 t$ and sin $2 t$ without help, for $y ^ { \prime \prime } { = } - 4 y . \mathrm { I }$ don’t think22these solutions to $y ^ { \prime \prime \prime } = y$ would have been found.

EXAMPLE 6 Find four solutions to $d ^ { 4 } y / d t ^ { 4 } = y$ by substituting $y = e ^ { c t }$ .

Four derivatives lead to $c ^ { 4 } = 1$ . Therefore $c$ is $i$ or $^ { - 1 }$ or $- i$ or 1. The solutions are $y = e ^ { i t }$ , $e ^ { - t }$ , $e ^ { - i t }$ , and $e ^ { t }$ . If we want real solutions, $e ^ { i t }$ and $e ^ { - i t }$ combine into cos $t$ and sin $t$ . In all cases $y ^ { \prime \prime \prime } { = } y$ .