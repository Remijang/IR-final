# 12.2 Plane Motion: Projectiles and Cycloids

The previous section started with $\mathbf { R } ( t )$ : From this position vector we computed $\mathbf { v }$ and a: Now we find $\mathbf { R } ( t )$ itself, from more basic information. The laws of physics govern projectiles, and the motion of a wheel produces a cycloid (which enters problems in robotics). The projectiles fly without friction, so the only force is gravity.

These motions occur in a plane. The two components of position will be $x$ (across) and $y$ (up). A projectile moves as $t$ changes, so we look for $x ( t )$ and $y ( t )$ : We are shooting a basketball or firing a gun or peacefully watering the lawn, and we have to aim in the right direction (not directly at the target). If the hose delivers water at 10 meters=second; can you reach the car 12 meters away ?

The usual initial position is $( 0 , 0 )$ : Some flights start higher, at $( 0 , h )$ : The initial velocity is $( v _ { 0 } \cos \alpha , v _ { 0 } \sin \alpha )$ ; where $v _ { 0 }$ is the speed and $\alpha$ is the angle with the horizontal. The acceleration from gravity is purely vertical: $d ^ { 2 } y / d t ^ { 2 } = - g$ : So the horizontal velocity stays at its initial value. The upward velocity decreases by $- g t$ :

$$
d x / d t = v _ { 0 } \cos \alpha , d y / d t = v _ { 0 } \sin \alpha - g t .
$$

The horizontal distance $x ( t )$ is steadily increasing. The height $y ( t )$ increases and then decreases. To find the position, integrate the velocities (for a high start add $h$ to $y$ ):

$$
\begin{array} { r } { \textbf {  { s } } x ( t ) = ( v _ { 0 } \cos \alpha ) t , y ( t ) = ( v _ { 0 } \sin \alpha ) t - \frac { 1 } { 2 } g t ^ { 2 } . } \end{array}
$$

This path is a parabola. But it is not written as $y = a x ^ { 2 } + b x + c$ : It could be, if we eliminated $t$ : Then we would lose track of time. The parabola is $y ( x )$ , with no parameter, where we have $x ( t )$ and $y ( t )$ :

Basic question: Where does the projectile hit the ground ? For the parabola, we solve $y ( x ) = 0$ : That gives the position $x$ : For the projectile we solve $y ( t ) = 0$ : That gives the time it hits the ground, not the place. If that time is $T$ ; then $x ( T )$ gives the place.

The information is there. It takes two steps insteadof one, but we learn more.

EXAMPLE 1 Water leaves the hose at 10 meters=second (this is $v _ { 0 }$ ). It starts up at the angle $\alpha$ : Find the time $T$ when $y$ is zero again, and find where the projectile lands.

Solution The flight ends when $y = ( 1 0 \sin \alpha ) T - { \textstyle { \frac { 1 } { 2 } } } g T ^ { 2 } = 0$ : The flight time is $T = ( 2 0 \sin \alpha ) / g$ : At that time, the horizontal distance is

$$
x ( T ) = ( 1 0 \cos \alpha ) T = ( 2 0 0 \cos \alpha \sin \alpha ) / g . \mathrm { T h i s ~ i s ~ t h e ~ } r a n g e ~ .
$$

The projectile (or water from the hose) hits the ground at $x = R$ : To simplify, replace 200 cos $\alpha$ sin $\alpha$ by $1 0 0 \sin 2 \alpha$ : Since $g = 9 . 8$ meters= $\sec ^ { 2 }$ ; we can’t reach the car:

The range $R = ( 1 0 0 \sin 2 \alpha ) / 9 . 8$ is at most 100=9:8: This is less than 12:

The range is greatest when sin $2 \alpha = 1 ( \alpha \mathrm { i s } 4 5 ^ { \circ } )$ . To reach 12 meters we could stand on a ladder (Problem 14). To hit a baseball against air resistance, the best angle is nearer to $3 5 ^ { \circ }$ : Figure 12.5 shows symmetric parabolas (no air resistance) and unsymmetric flight paths that drop more steeply.

12B The flight time $T$ and the horizontal range $R = x ( T )$ are reached when $y = 0$ , which means $\begin{array} { r } { ( v _ { 0 } \sin \alpha ) T = \frac { 1 } { 2 } g T ^ { 2 } } \end{array}$ : $T = ( 2 v _ { 0 } \sin \alpha ) / g$ and $R = ( v _ { 0 } \cos \alpha ) T = ( v _ { 0 } ^ { 2 } \sin 2 \alpha ) / g .$ :

EXAMPLE 2 What are the correct angles $\alpha$ for a given range $R$ and given $v _ { 0 }$ ?

Solution The range is $R = ( v _ { 0 } ^ { 2 } \sin { 2 \alpha } ) / g$ : This determines the sine of $2 \alpha$ —but two angles can have the same sine. We might find $2 \alpha = 6 0 ^ { \circ }$ or $1 2 0 ^ { \circ }$ : The starting angles $\alpha = 3 0 ^ { \circ }$ and $\alpha = 6 0 ^ { \circ }$ in Figure 12.5 give the same sin $2 \alpha$ and the same range $R$ : The flight times contain sin $\alpha$ and are different.

By calculus, the maximum height occurs when $d y / d t = 0$ : Then $v _ { 0 } \sin \alpha = g t$ , which means that $t = ( v _ { 0 } \sin \alpha ) / g$ : This is half of the total flight time $T$ —the time going up equals the time coming down. The value of $y$ at this halfway time $\begin{array} { r } { t = \frac { 1 } { 2 } T } \end{array}$ is

$$
y _ { \operatorname* { m a x } } = ( v _ { 0 } \sin \alpha ) ( v _ { 0 } \sin \alpha ) / g - \textstyle { \frac { 1 } { 2 } } g ( v _ { 0 } \sin \alpha / g ) ^ { 2 } = ( v _ { 0 } \sin \alpha ) ^ { 2 } / 2 g .
$$

EXAMPLE 3 If a ski jumper goes 90 meters down a $3 0 ^ { \circ }$ slope, after taking off at 28 meters=second; find equations for the flight time and the ramp angle $\alpha$ :

Solution The jumper lands at the point $x = 9 0 \cos 3 0 ^ { \circ }$ ; $y = - 9 0$ sin $3 0 ^ { \circ }$ (minus sign for obvious reasons). The basic equation (2) is $x = ( 2 8 \cos \alpha ) t$ ; $y = ( 2 8 \sin \alpha ) t -$ $\scriptstyle { \frac { 1 } { 2 } } { \bar { g t } } ^ { 2 }$ : Those are two equations for $\alpha$ and $t$ : Note that $t$ is not $T$ , the flight time to $y = 0$ :

Conclusion The position of a projectile involves three parameters $v _ { 0 } , \alpha$ , and $t$ : Three pieces of information determine the flight (almost). The reason for the word almost is the presence of sin $\alpha$ and cos $\alpha$ : Some flight requirements cannot be met (reaching a car at 12 meters). Other requirements can be met in two ways (when the car is close). The equation sin $\alpha = c$ is more likely to have no solution or two solutions than exactly one solution.

Watch for the three pieces of information in each problem. When a football starts at $v _ { 0 } = 2 0$ meters=second and hits the ground at $x = 4 0$ meters, the third fact is This is like a lawyer who is asked the fee and says $\$ 1000$ for three questions. “Isn’t that steep ? ” says the client. “Yes,” says the lawyer, “now what’s your last question ? ”

# CYCLOIDS

A projectile’s path is a parabola. To compute it, eliminate $t$ from the equations for $x$ and $y$ : Problem 5 finds $y = a x ^ { 2 } + b x$ , a parabola through the origin. The path of a point on a wheel seems equally simple, but eliminating $t$ is virtually impossible. The cycloid is a curve that really needs and uses a parameter.

To trace out a cycloid, roll a circle of radius a along the $x$ axis. Watch the point that starts at the bottom of the circle. It comes back to the bottom at $x = 2 \pi a$ , after a complete turn of the circle. The path in between is shown in Figure 12.6. After a century of looking for the $x y$ equation, a series of great scientists (Galileo, Christopher Wren, Huygens, Bernoulli, even Newton and l’Hôpital) found the right way to study a cycloid—by introducing a parameter. We will call it $\theta$ ; it could also be t:



The parameter is the angle $\theta$ throughwhich the circle turns. (This angle is not at the origin, like $\theta$ in polar coordinates.) The circle rolls a distance $a \theta$ , radius times angle, along the $x$ axis. So the center of the circle is at $x = a \theta$ ; $y = a$ : To account for the segment $C P$ , subtract $a$ sin $\theta$ from $x$ and $a$ cos $\theta$ from $y$ :

$$
T h e p o i n t P h a s x = a ( \theta - \sin \theta ) a n d y = a ( 1 - \cos \theta ) .
$$

At $\theta = 0$ the position is $( 0 , 0 )$ : At $\theta = 2 \pi$ the position is $( 2 \pi a , 0 )$ : In between, the slope of the cycloid comes from the chain rule:

$$
{ \frac { d y } { d x } } = { \frac { d y / d \theta } { d x / d \theta } } = { \frac { a \sin \theta } { a ( 1 - \cos \theta ) } } .
$$

This is infinite at $\theta = 0$ : The point on the circle starts staraight upward and the cycloid has a cusp. Note how all calculations use the parameter $\theta$ : We go?quickly:

Question 1 Find the area under one arch of the cycloid . $\overset { \cdot } { \theta } = 0$ to $\theta = 2 \pi$ /: Answer The area is $\textstyle { \int y d x } = \int _ { 0 } ^ { 2 \pi } a ( 1 - \cos \theta ) a ( 1 - \cos \theta ) d \theta . $ : This equals $3 \pi a ^ { 2 }$

Question 2 Find the length of the arch, using $d s = { \sqrt { ( d x / d \theta ) ^ { 2 } - ( d y / d \theta ) ^ { 2 } } } d \theta .$ Answer $\begin{array} { r } { \int d s = \int _ { 0 } ^ { 2 \pi } a \sqrt { ( 1 - \cos \theta ) ^ { 2 } - ( \sin \theta ) ^ { 2 } } d \theta = \int _ { 0 } ^ { 2 \pi } a \sqrt { 2 - 2 \cos \theta } d \theta . } \end{array}$ : Now substitute $1 - \cos \theta = 2 \sin ^ { 2 } { \frac { 1 } { 2 } } \theta$ : The square root is $2 \sin { \textstyle { \frac { 1 } { 2 } } \theta }$ : The length is $8 a$ :

Question 3 If the cycloid is turned over ( $y$ is downward), find the tiame to slide to the bottom. The slider starts with $v = 0$ at $y = 0$ :

Answer Kinetic plus potential energy is ${ \begin{array} { r l } { { \frac { 1 } { 2 } } m v ^ { 2 } - m g y = 0 } \end{array} }$ (?it starts from zero and can’t change). So the speed is $v = { \sqrt { 2 g y } }$ : This is $d s / d t$ and we know $d s$ :

$$
{ \mathrm { s l i d i n g ~ t i m e } } = \int d t = \int { \frac { d s } { \sqrt { 2 g y } } } = \int _ { 0 } ^ { \pi } { \frac { a { \sqrt { 2 - 2 \cos \theta } } d \theta } { \sqrt { 2 g a ( 1 - \cos \theta ) } } } = \pi { \sqrt { a / g } } .
$$

Check dimensions?: $a =$ distancea; $g =$ distance=.ti?mes/2; ${ \pi } { \sqrt { a / g } } = { \mathrm { t i m e } }$ : That is the shortest sliding time for any curve. The cycloid solves the “brachistochrone problem,” which minimizes the time?down curves from $o$ to $\boldsymbol { Q }$ (Figure 12.6). You might think a straight path would be quicker—it is certainly shorter. A straight line has the equation $x = \pi y / 2$ , so the sliding time is

$$
\begin{array} { r } { \int d t = \int d s / \sqrt { 2 g y } = \int _ { 0 } ^ { 2 a } \sqrt { ( \pi / 2 ) ^ { 2 } + 1 } d y / \sqrt { 2 g y } = \sqrt { \pi ^ { 2 } + 4 } \sqrt { a / g } . } \end{array}
$$

This is larger than the cycloid time $\pi { \sqrt { a / g } }$ : It is better to start out vertically and pick up speed early, even if the path is longer.

Instead of publishing his solution, John Bernoulli turned this problem into an international challenge: Prove that the cycloid gives the fastest slide. Most mathematicians couldn’t do it. The problem reached Isaac Newton (this was later in his life). As you would expect, Newton solved it. For some reason he sent back his proof with no name. But when Bernoulli received the answer, he was not fooled for a moment: “I recognize the lion by his claws.”

What is also amazing is a further property of the cycloid: The time to $\boldsymbol { \mathcal { Q } }$ is the same if you begin anywhere along the path. Starting from rest at $P$ instead of $o$ , the bottom is reached at the same time. This time Bernoulli got carried away: “You will be petrified with astonishment when I say...”.

There are other beautiful curves, closely related to the cycloid. For an epicycloid, the circl e rolls around the outside of another circle. For a hypocycloid, the rolling circle is inside the fixed circle. The astroid is the special case with radii in the ratio 1 to 4: It is the curved star in Problem 34, where $x = a \cos ^ { 3 } \theta$ and $y = a \sin ^ { 3 } \theta$ :

The cycloid even solves the old puzzle: What point moves backward when a train starts forward ? The train wheels have a flange that extends below the track, and $d x / d t < 0$ at the bottom of the flange.