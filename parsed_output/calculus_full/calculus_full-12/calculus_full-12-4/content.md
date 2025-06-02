# 12.4 Polar Coordinates and Planetary Motion

This section has a general purpose—to do vector calculus in polar coordinates. It also has a specific purpose—to study central forces and the motion of planets. The main gravitational force on a planet is from the sun. It is a central force, because it comes from the sun at the center. Polar coordinates are natural, so the two purposes go together.

You may feel that the planets are too old for this course. But Kepler’s laws are more than theorems, they are something special in the history of mankind—“the greatest scientific discovery of all time.” If we can recapture that glory we should do it. Part of the greatness is in the difficulty—Kepler was working sixty years before Newton discovered calculus. From pages of observations, and some terrific guesses, a theory was born. We will try to preserve the greatness without the difficulty, and show how elliptic orbits come from calculus. The first conclusion is quick.

Motion in a central force field always stays in a plane.

$\mathbf { F }$ is a multiple of the vector $\mathbf { R }$ from the origin (central force). $\mathbf { F }$ also equals ma (Newton’s Law). Therefore $\mathbf { R }$ and a are in the same direction and $\mathbf { R } \times \mathbf { a } = \mathbf { 0 }$ : Then $\mathbf { R } \times \mathbf { v }$ has zero derivative and is constant:

$$
{ \mathrm { b y ~ t h e ~ p r o d u c t ~ r u l e : ~ } } \ { \frac { d } { d t } } ( \mathbf { R } \times \mathbf { v } ) = \mathbf { v } \times \mathbf { v } + \mathbf { R } \times \mathbf { a } = \mathbf { 0 } + \mathbf { 0 } .
$$

$\mathbf { R } \times \mathbf { v }$ is a constant vector H: So R stays in the plane perpendicular to $\mathbf { H }$ :

How does a planet move in that plane ? We turn to polar coordinates. At each point except the origin (where the sun is), ${ \bf u } _ { r }$ is the unit vector pointing outward. It is the position vector $\mathbf { R }$ divided by its length $r$ (which is $\sqrt { x ^ { 2 } + y ^ { 2 } } )$ :

$$
{ \bf u } _ { r } = { \bf R } / r = ( x { \bf i } + y { \bf j } ) / r = \cos \theta { \bf i } + \sin \theta { \bf j } .
$$

That is a unit vector because $\cos ^ { 2 } \theta + \sin ^ { 2 } \theta = 1$ : It goes out from the center. Figure 12.9 shows ${ \bf u } _ { r }$ and the second unit vector ${ \bf u } _ { \theta }$ at a $9 0 ^ { \circ }$ angle:

$$
\mathbf { u } _ { \theta } = - \sin \theta \mathbf { i } + \cos \theta \mathbf { j } .
$$

The dot product is $\mathbf { u } _ { r } \cdot \mathbf { u } _ { \theta } = 0$ : The subscripts $r$ and $\theta$ indicate direction (not derivative).

Question 1: How do ${ \bf u } _ { r }$ and ${ \bf u } _ { \theta }$ change as $r$ changes (out a ray) ? They don $\mathbf { \Phi } _ { t }$ .

Question 2: How do ${ \bf u } _ { r }$ and ${ \bf u } _ { \theta }$ change as $\theta$ changes ? Take the derivative:

$$
\begin{array} { r l } & { d \mathbf { u } _ { r } / d \theta = - \sin \theta \mathbf { i } + \cos \theta \mathbf { j } = \mathbf { u } _ { \theta } } \\ & { d \mathbf { u } _ { \theta } / d \theta = - \cos \theta \mathbf { i } + \sin \theta \mathbf { j } = - \mathbf { u } _ { r } . } \end{array}
$$

Since ${ \bf u } _ { r } = { \bf R } / r$ , one formula is simple: The position vector is $\mathbf { R } = r \mathbf { u } _ { r }$ : For its derivative $\mathbf { v } = d \mathbf { R } / d t$ , use the chain rule $d \mathbf { u } _ { r } / d t = ( d \mathbf { u } _ { r } / d \theta ) ( d \theta / d t ) = ( d \theta / d t ) \mathbf { u } _ { \theta }$

$$
T h e \nu e l o c i t y i s \ \mathrm { v } = { \frac { d } { d t } } ( r \mathbf { u } _ { r } ) = { \frac { d r } { d t } } \mathbf { u } _ { r } + r { \frac { d \theta } { d t } } \mathbf { u } _ { \theta } .
$$

The outward speed is $d r / d t$ : The circular speed is $r d \theta / d t$ : The sum of squares is $| \mathbf { v } | ^ { 2 }$

Return one more time to steady motion around a circle, say $r = 3$ and $\theta = 2 t$ : The velocity is $\mathbf { v } = 6 \mathbf { u } _ { \theta }$ , all circular. The acceleration is $- 1 2 \mathbf { u } _ { r }$ , all inward. For circles ${ \bf u } _ { \theta }$ is the tangent vector $\mathbf { T }$ : But the unit vector ${ \bf u } _ { r }$ points outward and $\mathbf { N }$ points inward— the way the curve turns.

Now we tackle acceleration for any motion in polar coordinates. There can be speedup in $r$ and speedup in $\theta$ (also change of direction). Differentiate $\mathbf { v }$ in (5) by the product rule:

$$
{ \frac { d \mathbf { v } } { d t } } = { \frac { d ^ { 2 } r } { d t ^ { 2 } } } \mathbf { u } _ { r } + { \frac { d r } { d t } } { \frac { d \mathbf { u } _ { r } } { d t } } + { \frac { d r } { d t } } { \frac { d \theta } { d t } } \mathbf { u } _ { \theta } + r { \frac { d ^ { 2 } \theta } { d t ^ { 2 } } } \mathbf { u } _ { \theta } + r { \frac { d \theta } { d t } } { \frac { d \mathbf { u } _ { \theta } } { d t } } .
$$

For $d { \bf { u } } _ { r } / { d t }$ and $d { \bf { u } } _ { \theta } / d t$ , multiply equation (4) by $d \theta / d t$ : Then all terms contain ${ \bf u } _ { r }$ or ${ \bf u } _ { \theta }$ : The formula for $\mathbf { a }$ is famous but not popular (except it got us to the moon):

$$
\mathbf { a } = { \frac { d \mathbf { v } } { d t } } = \left( { \frac { d ^ { 2 } r } { d t ^ { 2 } } } - r \left( { \frac { d \theta } { d t } } \right) ^ { 2 } \right) \mathbf { u } _ { r } + \left( r { \frac { d ^ { 2 } \theta } { d t ^ { 2 } } } + 2 { \frac { d r } { d t } } { \frac { d \theta } { d t } } \right) \mathbf { u } _ { \theta } .
$$

In the steady motion with $r = 3$ and $\theta = 2 t$ , only one acceleration term is nonzero: $\mathbf { a } = - 1 2 \mathbf { u } _ { r }$ : Formula (6) can be memorized (maybe). Problem 14 gives a new way to reach it, using rei :

EXAMPLE 1 Find $\mathbf { R }$ and $\mathbf { v }$ and a for speedup $\theta = t ^ { 2 }$ around the circle $r = 1$ :

Solution The position vector is ${ \bf R } = { \bf u } _ { r }$ : Then $\mathbf { v }$ and a come from $( 5 - 6 )$ :

$$
\mathbf { v } = ( r d \theta / d t ) \mathbf { u } _ { \theta } = 2 t \mathbf { u } _ { \theta } \qquad \mathbf { a } = - ( 2 t ) ^ { 2 } \mathbf { u } _ { r } + 2 \mathbf { u } _ { \theta } .
$$

This question and answer were also in Example 6 of the previous section. The acceleration was $2 \mathbf { T } + 4 t ^ { 2 } \mathbf { N }$ : Notice again that $\mathbf { T } = \mathbf { u } _ { \theta }$ and $\mathbf { N } = - \mathbf { u } _ { r }$ , going round the circle.

EXAMPLE 2 Find $\mathbf { R }$ and $\mathbf { v }$ and $| \mathbf { v } |$ and a for the spiral motion $r = 3 t , \theta = 2 t$ :

Solution The position vector is $\mathbf { R } = 3 t \mathbf { u } _ { r }$ : Equation (5) gives velocity and speed:

$$
\mathbf { v } = 3 \mathbf { u } _ { r } + = 6 t \mathbf { u } _ { \theta } \quad { \mathrm { a n d } } \quad | \mathbf { v } | = { \sqrt { ( 3 ) ^ { 2 } + ( 6 t ) ^ { 2 } } } .
$$

The motion goes out and also around. From (6) the acceleration is $- 1 2 t { \bf u } _ { r } + 1 2 { \bf u } _ { \theta }$ : The same answers would come more slowly from $\mathbf { R } = 3 t \cos 2 t \mathbf { i } + 3 t \sin 2 t \mathbf { j }$ :

This example uses polar coordinates, but the motion is not circular. One of Kepler’s inspirations, after many struggles, was to get away from circles.

# KEPLER’S LAWS

You may know that before Newton and Leibniz and calculus and polar coordinates, Johannes Kepler discovered three laws of planetary motion. He was the court mathematician to the Holy Roman Emperor, who mostly wanted predictions of wars. Kepler also determined the date of every Easter—no small problem. His triumph was to discover patterns in the observations made by astronomers (especially by Tycho Brahe). Galileo and Copernicus expected circles, but Kepler found ellipses.

Law 1: Each planet travels in an ellipse?with one focus at the sun.

Law 2: The vector from sun to planet sweeps out area at a steady rate: $d A / d t =$ constant.

Law 3: The length of the planet’s year is $T = k a ^ { 3 / 2 }$ , where $a =$ maximum distance from the center (not the sun) and $k \overset { \cdot } { = } 2 \pi / \sqrt { G M }$ is the same for all planets.

With calculus the proof of these laws is a thousand times quicker. But Law 2 is the only easy one. The sun exerts a central force. Equation (1) gave $\mathbf { R } \times \mathbf { v } = \mathbf { H } = { \mathrm { c o n } } .$ stant for central forces. Replace $\mathbf { R }$ by $r \mathbf { u } _ { r }$ and replace $\mathbf { v }$ by equation (5):

$$
\mathbf { H } = r \mathbf { u } _ { r } \times \left( { \frac { d r } { d t } } \mathbf { u } _ { r } + r { \frac { d \theta } { d t } } \mathbf { u } _ { \theta } \right) = r ^ { 2 } { \frac { d \theta } { d t } } ( \mathbf { u } _ { r } \times \mathbf { u } _ { \theta } ) .
$$

This vector $\mathbf { H }$ is constant, so its length $h = r ^ { 2 } d \theta / d t$ is constant. In polar coordinates, the area is $\begin{array} { r } { d A = \frac { 1 } { 2 } r ^ { 2 } d \theta } \end{array}$ : This area $d A$ is swept out by the planet (Figure 12.10), and we have proved Law 2:

$$
\begin{array} { r } { d A / d t = \frac { 1 } { 2 } r ^ { 2 } d \theta / d t = \frac { 1 } { 2 } h = c o n s t a n t . } \end{array}
$$

Near the sun $r$ is small. So $d \theta / d t$ is big and planets go around faster.

Now for Law 1, about ellipses. We are aiming for $1 / r = C - D \cos$ s $\theta$ , which is the polar coordinate equation of an ellipse.It is easier to write $q$ than $1 / r$ , and find an equation for $q$ : The equation we will reach is $d ^ { 2 } q / d \theta ^ { 2 } + q = C$ : The desired $q = C - D$ cos $\theta$ solves that equation (check this), and gives us Kepler’s ellipse.

The first step is to connect $d r / d t$ to $d q / d \theta$ by the chain rule:

$$
{ \frac { d r } { d t } } = { \frac { d } { d t } } \left( { \frac { 1 } { q } } \right) = { \frac { - 1 } { q ^ { 2 } } } { \frac { d q } { d t } } = { \frac { - 1 } { q ^ { 2 } } } { \frac { d q } { d \theta } } { \frac { d \theta } { d t } } = - h { \frac { d q } { d \theta } } .
$$

Notice especially $d \theta / d t = h / r ^ { 2 } = h q ^ { 2 }$ : What we really want are second derivatives:

$$
{ \frac { d ^ { 2 } r } { d t ^ { 2 } } } = - h { \frac { d } { d t } } \left( { \frac { d q } { d \theta } } \right) = - h { \frac { d } { d \theta } } \left( { \frac { d q } { d \theta } } \right) { \frac { d \theta } { d t } } = - h ^ { 2 } q ^ { 2 } { \frac { d ^ { 2 } q } { d \theta ^ { 2 } } } .
$$

After this trick of introducing $q$ , we are ready for physics. The planet obeys Newton’s Law $\mathbf { F } = m \mathbf { a }$ , and the central force $\mathbf { F }$ is the sun’s gravity:

$$
{ \frac { \mathbf { F } } { m } } = { \mathbf { a } } \ { \mathrm { \ i s } } \quad - { \frac { G M } { r ^ { 2 } } } = { \frac { d ^ { 2 } r } { d t ^ { 2 } } } - r \left( { \frac { d \theta } { d t } } \right) ^ { 2 } .
$$

That right side is the ${ \bf u } _ { r }$ component of a in (6). Change $r$ to $1 / q$ and change $d \theta / d t$ to $h q ^ { 2 }$ : The preparation in(10) allows us to rewrite $d ^ { 2 } r / d t ^ { 2 }$ in equation (11). That equation becomes

$$
- G M \ q ^ { 2 } = - h ^ { 2 } q ^ { 2 } { \frac { d ^ { 2 } q } { d \theta ^ { 2 } } } - { \frac { 1 } { q } } ( h q ^ { 2 } ) ^ { 2 } .
$$

Dividing by $- h ^ { 2 } q ^ { 2 }$ gives what we hoped for—the simple equation for $q$ :

$$
d ^ { 2 } q / d \theta ^ { 2 } + q = G M / h ^ { 2 } = C { \ : } ( a c o n s t a n t ) .
$$

The solution is $q = C - D$ cos $\theta$ : Section 9:3 gave this polar equation for an ellipse or parabola or hyperbola. To be sure it is an ellipse, an astronomer computes $C$ and $D$ from the sun’s mass $M$ and the constant $G$ and the earth’s position and velocity. The main point is that $C > D$ : Then $q$ is never zero and $r$ is never infinite. Hyperbolas and parabolas are ruled out, and the orbit in Figure 12.10 must be an ellipse.

Astronomy is really impressive. You should visit the Greenwich Observatory in London, to see how Halley watched his comet. He amazed the world by predicting the day it would return. Also the discovery of Neptune was pure mathematics—the path of Uranus was not accounted for by the sun and known planets. LeVerrier computed a point in the sky and asked a Berlin astronomer to look. Sure enough Neptune was there.

Recently one more problem was solved—to explain the gap in the asteroids around Jupiter. The reason is “chaos”—the three-body problem goes unstable and an asteroid won’t stay in that orbit. We have come a long way from circles.

Department of Royal Mistakes The last pound note issued by the Royal Mint showed Newton looking up from his great book Principia Mathematica. He is not smiling and we can see why. The artist put the sun at the center! Newton has just proved it is at the focus. True, the focus is marked $S$ and the planet is $P$ : But those rays at the center brought untold headaches to the Mint—the note is out of circulation. I gave an antique dealer three pounds for it (in coins).

Kepler’s third law gives the time $T$ to go around the ellipse—the planet’s year. What is special in the formula is $a ^ { 3 / 2 }$ —and for Kepler himself, the 15th of May 1618 was unforgettable: “the right ratio outfought the darkness of my mind, by the great proof afforded by my labor of seventeen years on Brahe’s observations.” The second law $\textstyle d A / d t = { \frac { 1 } { 2 } } h$ is the key, plus two facts about an ellipse—it?s area ab and the height $b ^ { 2 } / a$ above the sun:

1. The area $A = \int _ { 0 } ^ { T } { \frac { d A } { d t } } d t = { \frac { 1 } { 2 } } h T$ must equal ab, so $T = \frac { 2 \pi a b } { h }$   
2. The distance $r = 1 / C$ at $\theta = \pi / 2$ must equal $b ^ { 2 } / a$ , so $b = { \sqrt { a / C } }$ :

The height $b ^ { 2 } / a$ is in Figure 12.10 and Problems 25 26: The constant $C = G M / h ^ { 2 }$ is in equation (12). Put them together to find the period:

$$
T = { \frac { 2 \pi a b } { h } } = { \frac { 2 \pi a } { h } } { \sqrt { \frac { a } { C } } } = { \frac { 2 \pi } { \sqrt { G M } } } a ^ { 3 / 2 } .
$$

To think of Kepler guessing $a ^ { 3 / 2 }$ is amazing. To think of Newton proving Kepler’s laws by calculus is also wonderful—because we can do it too.

EXAMPLE 3 When a satelliteagoes around in a circle, find the time $T$ :

Let $r$ be the radius and $\omega$ be the angular velocity. The time for a complete circle (angle $2 \pi )$ is $T = 2 \pi / \omega$ : The acceleration is $G M / \hat { r } ^ { 2 }$ from gravity, and it is also $r \omega ^ { 2 }$ for circular motion. Therefore Kepler is proved right:

$$
r \omega ^ { 2 } = G M / r ^ { 2 } \quad \Rightarrow \quad \omega = \sqrt { G M / r ^ { 3 } } \quad \Rightarrow \quad T = 2 \pi / \omega = 2 \pi r ^ { 3 / 2 } / \sqrt { G M } .
$$