Up to now, points have been located by their $x$ and $y$ coordinates. But if you were a flight controller, and a plane appeared on the screen, you would not give its position that way. Instead of $x$ and $y$ , you would read off the direction of the plane and its distance. The direction is given by an angle $\theta$ : The distance is given by a positive number $r$ : Those are the polar coordinates of the point, where $x$ and $y$ are the rectangular coordinates.

The angle $\theta$ is measured from the horizontal.Suppose the distance is 2 and the direction is $3 0 ^ { \circ }$ or $\pi / 6$ (degrees preferred by flight controllers, radians by mathematicians). A pilot looking along the $x$ axis would give the plane’s direction as “11 o’clock.” This totally destroys our system of units, by measuring direction in hours. But the angle and the distance locate the plane.

How far to a landing strip at $r = 1$ and $\theta = - \pi / 2 ?$ For that question polar coordinates are not good. They are perfect for distance from the origin (which equals $r _ { \cdot }$ ), but for most other distances I would switch to $x$ and $y$ : It is extremely simple to determine $x$ and $y$ from $r$ and $\theta$ , and we will do it constantly. The most used formulas?in this chapter come from Figure?9.1—where the right triangle has angle $\theta$ and hypotenuse $r$ : The sides of that triangle are $x$ and $y$ :

$$
x = r \cos \theta \quad a n d \quad y = r \sin \theta .
$$

The point at $r = 2 , \theta = \pi / 6$ has $x = 2 \cos { ( \pi / 6 ) }$ and $y = 2 \sin ( \pi / 6 )$ : The cosine of $\pi / 6$ is ${ \sqrt { 3 } } / 2$ and the sine is $\frac { 1 } { 2 }$ : So $x = \sqrt { 3 }$ and $y = 1$ : Polar coordinates convert easily to $x y$ coordinates—now we go the other way.

Always $x ^ { 2 } + y ^ { 2 } = r ^ { 2 }$ :?In this example $( { \sqrt { 3 } } ) ^ { 2 } + ( 1 ) ^ { 2 } = ( 2 ) ^ { 2 }$ : Pythagor?as produces $r$ from $x$ and $y$ : The direction $\theta$ is also available, but the formula is not so beautiful:

$$
r = \sqrt { x ^ { 2 } + y ^ { 2 } } a n d \tan \theta = \frac { y } { x } a n d ( a l m o s t ) \theta = \tan ^ { - 1 } \frac { y } { x } .
$$

Our point has $y / x = 1 / \sqrt { 3 }$ : One angle with this tangent is $\theta = \tan ^ { - 1 } ( 1 / { \sqrt { 3 } } ) = \pi / 6$ :

EXAMPLE 1 Point $B$ in Figure 9.1c is at a negative angle $\theta = - \pi / 4$ : The $x$ coordinate $r \cos ( - \pi / 4 )$ is the same as $r$ cos $\pi / 4$ (the cosine is even). But the $y$ coordinate $r$ s $\mathfrak { n } ( - \pi / 4 )$ is negative. Computing $r$ and $\theta$ from $x = 1$ and $y = 1$ , the distance is $r = { \sqrt { 1 + 1 } }$ and tan $\theta$ is $- 1 / 1$ :

Warning To any angle $\theta$ we can add or subtract $2 \pi$ —which goes a full $3 6 0 ^ { \circ }$ circle and keeps the same direction. Thus $- \pi / 4$ or $- 4 5 ^ { \circ }$ is the same angle as $7 \pi / 4$ or $3 1 5 ^ { \circ }$ : So is $1 5 \pi / 4$ or $6 7 5 ^ { \circ }$ :

If we add or subtract $1 8 0 ^ { \circ }$ , the tangent doesn’t change. The point $( 1 , - 1 )$ is on the $- 4 5 ^ { \circ }$ line at $r = { \sqrt { 2 } }$ : The point $( - 1 , 1 )$ is on the $1 3 5 ^ { \circ }$ line also with $r = \sqrt { 2 }$ : Both have tan $\theta = - 1$ : We had to write “almost” in equation (2), because a point has many $\theta$ ’s and two points have the same $r$ and tan $\theta$ :

Even worse, we could say that $B = ( 1 , - 1 )$ is on the $1 3 5 ^ { \circ }$ line but at a negative distance $r = - { \sqrt { 2 } }$ : A negative $r$ carries the point backward along the $1 3 5 ^ { \circ }$ line, which is forward to $B$ : In giving the position of $B$ , I would always keep $r > 0$ : But in drawing the graph of a polar equation, $r < 0$ is allowed. We move now to those graphs.

# THE CIRCLE $r = \cos \theta$

The basis for Chapters 1–8 was $y = f ( x )$ : The key to this chapter is $r = F ( \theta )$ : That is a relation between the polar coordinates, and the points satisfying an equation like $r = \cos \theta$ produce a polar graph.

It is not obvious why $r = \cos \theta$ gives a circle. The equations $r = \cos 2 \theta$ and $r = \cos ^ { 2 } \theta$ and $r = 1 + \cos \theta$ produce entirely different graphs—not circles. The direct approach is to take $\theta = 0 ^ { \circ } , 3 0 ^ { \circ } , 6 0 ^ { \circ } , \ldots$ and go out the distance $r = \cos \theta$ on each ray. The points are marked in Figure 9.2a, and connected into a curve. It seems to be a circle of radius $\frac { 1 } { 2 }$ , with its center at the point $\textstyle { \big ( } { \frac { 1 } { 2 } } , 0 { \big ) }$ : We have to be able to show mathematically that $r = \cos \theta$ represents a shifted circle.

One point must be mentioned. The angles from 0 to $\pi$ give the whole circle. The number $r = \cos \theta$ becomes negative after $\pi / 2$ , and we go backwards along each ray.

At $\theta = \pi$ (to the left of the origin) the cosine is $^ { - 1 }$ : Going backwards brings us to the same point as $\theta = 0$ and $r = + 1$ —which completes the circle.

When $\theta$ continues from $\pi$ to $2 \pi$ we go around again. The polar equation gives the circle twice. (Or more times, when $\theta$ continues past $2 \pi$ :) If you don’t like negative $r$ ’s and multiple circles, restrict $\theta$ to the range from $- \pi / 2$ to $\pi / 2$ : We still have to see why the graph of $r = \cos \theta$ is a circle.

Method 5 Multiply by $r$ and convert to rectangular coordinates $x$ and $y$ :

$$
r = \cos \theta \quad \Rightarrow \quad r ^ { 2 } = r \cos \theta \quad \Rightarrow \quad x ^ { 2 } + y ^ { 2 } = x .
$$

This is a circle because of $x ^ { 2 } + y ^ { 2 }$ : From rewriting as $( x - { \textstyle \frac { 1 } { 2 } } ) ^ { 2 } + y ^ { 2 } = ( { \textstyle \frac { 1 } { 2 } } ) ^ { 2 }$ we recognize its center and radius. Center at $\begin{array} { r } { x = \frac { 1 } { 2 } } \end{array}$ and $y = 0$ ; radius $\textstyle { \frac { 1 } { 2 } }$ : Done.

Method 6 Write $x$ and $y$ separately as functions of $\theta$ : Then $\theta$ is a “parameter”:

$$
x = r \cos \theta = \cos ^ { 2 } \theta \qquad { \mathrm { a n d } } \qquad y = r \sin \theta = \sin \theta \cos \theta .
$$

These are not polar equations but parametric equations. The parameter $\theta$ is the angle, but it could be the time—the curve would be the same. Chapter 12 studies parametric equations in detail—here we stay with the circle.

To find the circle, square $x$ and $y$ and add. This produces $x ^ { 2 } + y ^ { 2 } = x$ in Problem 26: But here we do something new: Start with the circle and find equation (4). In case you don’t reach Chapter 12, the idea is this. Add the vectors $o c$ to the center and $C P$ out the radius:

The point $P$ in Figure 9.2 has $\begin{array} { r } { ( x , y ) = O C + C P = ( \frac { 1 } { 2 } , 0 ) + ( \frac { 1 } { 2 } \cos t , \frac { 1 } { 2 } \sin t ) . } \end{array}$

The parameter $t$ is the angle at the center of the circle. The equations are $\textstyle x = { \frac { 1 } { 2 } } + { \frac { 1 } { 2 } } \cos t$ and $\begin{array} { r } { y = \frac { 1 } { 2 } \sin t { } } \end{array}$ : A trigonometric person sees a double angle and sets $t = 2 \theta$ : The result is equation (4) for the circle:

$$
\begin{array} { r } { x = \frac { 1 } { 2 } + \frac { 1 } { 2 } \cos 2 \theta = \cos ^ { 2 } \theta \qquad \mathrm { a n d } \qquad y = \frac { 1 } { 2 } \sin 2 \theta = \sin \theta \cos \theta . } \end{array}
$$

This step rediscovers a basic theorem of geometry: The angle t at the center is twice the angle $\theta$ at the circumference. End of quick introduction to parameters.

A second circle is $r = \sin \theta$ , drawn in Figure $9 . 2 \mathrm { c }$ . A third circle is $r = \cos \theta +$ sin $\theta$ , not drawn. Problem 27 asks you to find its $x y$ equation and its radius. All calculations go back to $x = r \cos \theta$ and $y = r$ sin $\theta$ —the basic facts of polar coordinates! The last exercise shows a parametric equation with beautiful graphs, because it may be possible to draw them now. Then the next section concentrates on $r = F ( \theta )$ —and goes far beyond circles.