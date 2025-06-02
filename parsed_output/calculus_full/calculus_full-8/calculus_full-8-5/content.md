# 8.5 Masses and Moments

This chapter concludes with two sections related to engineering and physics. Each application starts with a finite number of masses or forces. Their sum is the total mass or total force. Then comes the “continuous case,” in which the mass is spread out instead of lumped. Its distribution is given by a density function $\rho$ (Greek rho), and the sum changes to an integral.

The first step (hardest step ? ) is to get the physical quantities straight. The second step is to move from sums to integrals (discrete to continuous, lumped to distributed). By now we hardly stop to think about it—although this is the key idea of integral calculus. The third step is to evaluate the integrals. For that we can use substitution or integration by parts or tables or a computer.

Figure 8.13 shows the one-dimensional case: masses along the $x$ axis. The total mass is the sum of the masses. The new idea is that of moments—when the mass or force is multiplied by a distance:

moment of mass around the $y$ axis $= m x = ( m a s s )$ times (distance to axis):

$$
 \begin{array} { r l r l }  \operatorname* { m a s s }  | \begin{array} { l l l l } { m _ { 1 } + m _ { 2 } } & { } & { + m _ { 3 } = M } & { } & { \qquad { \mathrm { f o r c e } } { | \begin{array} { l l l l } { F _ { 1 } + F _ { 2 } } \\ { \qquad \vdots } & { } & { \qquad \vdots } \end{array} | } } & { } & { + F _ { 3 } = F } \\  \operatorname* { m o m e n t } { | \begin{array} { l l l l } { \qquad \bullet \qquad { \mathord { | \begin{array} { l l l l } { \qquad \overline { { x } } } \\ { m _ { 1 } x _ { 1 } + m _ { 2 } x _ { 2 } } & { } \end{array}  \kern - delimiterspace } } } & { } & { \qquad } & { \qquad \tan \operatorname { f o u e } { | \begin{array} { l l l l } { \qquad x _ { 1 } } & { } & { \qquad \vdots } \end{array} | } } & { } & { } \\ { \qquad } & { } & { \qquad \tan \operatorname { f o r c e } { | \begin{array} { l l l l } { F _ { 1 } x _ { 1 } + F _ { 2 } x _ { 2 } } & { } & { + F _ { 3 } x _ { 3 } = H \bar { x } } \\ { \qquad \vdots } & { } & { \qquad \vdots } \end{array} | } } & { } & { } \end{array} } \end{array} \end{array}
$$

The figure has masses 1; 3; 2. The total mass is 6. The “lever arms” or “moment arms” are the distances $x = 1 , 3 , 7$ . The masses have moments 1 and 9 and 14 (since $m x$ is 2 times 7). The total moment is $1 + 9 + 1 4 = 2 4$ . Then the balance point is at $\bar { x } = M _ { x } / M = 2 4 / 6 = 4$ .

The total mass is the sum of the $m$ ’s. The total moment is the sum of $m _ { n }$ times $x _ { n }$ (negative on the other side of $x = 0$ ). If the masses are children on a seesaw, the balance point is the center of gravity $\bar { x }$ —also called the center of mass:

# DEFINITION

$$
{ \bar { x } } = { \frac { \sum m _ { n } x _ { n } } { \sum m _ { n } } } = { \frac { \mathrm { t o t a l ~ m o m e n t } } { \mathrm { t o t a l ~ m a s s } } } .
$$

If all masses are moved to $\bar { x }$ , the total moment (6 times 4) is still 24: The moment equals the mass $\sum m _ { n }$ times $\bar { x }$ . The masses act like a single mass at $\bar { x }$ .

Also: If we moPve the axis to $\bar { x }$ , and leave the children where they are, the seesaw balances. The masses on the left of $\bar { x } = 4$ will offset the mass on the right. Reason: The distances to the new axis are $x _ { n } - { \bar { x } }$ . The moments add to zero by equation .1/:

$$
\mathrm { m o m e n t ~ a r o u n d ~ n e w ~ a x i s } = \sum m _ { n } ( x _ { n } - \bar { x } ) = \sum m _ { n } x _ { n } - \sum m _ { n } \bar { x } = 0 .
$$

Turn now to the continuous case, when mass is spread out along the line. Each piece of length $\Delta x$ has an average density $\rho _ { n } =$ .mass of piece//.length of piece/ $\ O =$ $\Delta m / \Delta x$ . As the pieces get shorter, this approaches $d m / d x$ —the density at the point. The limit of (small mass)=(small length) is the density $\rho ( x )$ .

Integrating that derivative $\rho = d m / d x$ , we recover the total mass: $\sum \rho _ { n } \Delta x$ becomes

$$
\begin{array} { r } { t o t a l m a s s ~ M = \int \rho ( x ) d x . } \end{array}
$$

When the mass is spread evenly, $\rho$ is constant. Then $M = \rho L =$ density times length.

# 8 Applications of the Integral

The moment formula is similar. For each piece, the moment is mass $\rho _ { n } \Delta x$ multiplied by distance $x$ —and we add. In the continuous limit, $\rho ( x ) d x$ is multiplied by $x$ and we integrate:

$$
\begin{array} { r } { { t o t a l m o m e n t a r o u n d y a x i s = M _ { y } = \int x \rho ( x ) d x } . } \end{array}
$$

Moment is mass times distance. Dividing by the total mass $M$ gives “average distance”:

$$
c e n t e r o f m a s s \bar { x } = \frac { \mathrm { m o m e n t } } { \mathrm { m a s s } } = \frac { M _ { y } } { M } = \frac { \int x \rho ( x ) d x } { \int \rho ( x ) d x } .
$$

Remark If you studied Section 8:4 on probability, you will notice how the formulas match up. The mass $\int \rho ( x ) d x$ is like the total probability $\int { p ( x ) d x }$ . The moment $\int x \rho ( x ) d x$ is like the meanr $x p ( x ) d x$ . The moment of inertia $\int { ( x - \bar { x } ) ^ { 2 } \rho ( x ) d x }$ is the variance. Mathematics keeps hammering away at the same basic ideas! The only difference is that the total probability is always 1: The mean really corresponds to the center of mass $\bar { x }$ , but in probability we didn’t notice the division by $\int { p ( x ) d x } = 1$ .

EXAMPLE 1 With constant density $\rho$ from 0 to $L$ , the mass is $M = \rho L$ . The moment is

$$
\begin{array} { r } { M _ { y } = \int _ { 0 } ^ { L } x \rho d x = \frac { 1 } { 2 } \rho x ^ { 2 } \big ] _ { 0 } ^ { L } = \frac { 1 } { 2 } \rho L ^ { 2 } . } \end{array}
$$

The center of mass is $\bar { x } = M _ { y } / M = L / 2$ . It is halfway along.

EXAMPLE 2 With density $e ^ { - x }$ the mass is 1, the moment is 1, and $\bar { x }$ is 1:

$$
\begin{array} { r } { \int _ { 0 } ^ { \infty } e ^ { - x } d x = \left[ - e ^ { - x } \right] _ { 0 } ^ { \infty } = 1 \quad \mathrm { a n d } \quad \int _ { 0 } ^ { \infty } x e ^ { - x } d x = \left[ - x e ^ { - x } - e ^ { - x } \right] _ { 0 } ^ { \infty } = 1 . } \end{array}
$$

# MASSES AND MOMENTS IN TWO DIMENSIONS

Instead of placing masses along the $x$ axis, suppose $m _ { 1 }$ is at the point $( x _ { 1 } , y _ { 1 } )$ in the plane. Similarly $m _ { n }$ is at $( x _ { n } , y _ { n } )$ . Now there are two moments to consider. Around the $y$ axis $M _ { y } = \Sigma m _ { n } x _ { n }$ and around the $x$ axis $M _ { x } = \Sigma m _ { n } y _ { n }$ . Please notice that the $x$ ’s go into the moment $M _ { y }$ —because the $x$ coordinate gives the distance from the $y$ axis!

Around the $x$ axis, the distance is $y$ and the moment is $M _ { x }$ . The center of mass is the point $( { \bar { x } } , { \bar { y } } )$ at which everything balances:

$$
\bar { x } = \frac { M _ { y } } { M } = \frac { \sum m _ { n } x _ { n } } { \sum m _ { n } } \quad \mathrm { a n d } \quad \bar { y } = \frac { M _ { x } } { M } = \frac { \sum m _ { n } y _ { n } } { \sum m _ { n } } .
$$

In the continuous case these sums become two-dimensional integrals. The total mass is $\iint \rho ( x , y ) d x d y$ , when the density is $\rho { = } \mathrm { m a s s }$ per unit area. These “double integrals” are for the future (Section 14:1). Here we consider the most important case: $\rho = c o n s t a n t$ . Think of a thin plate, made of material with constant density (say $\rho = 1$ ). To compute its mass and moments, the plate is cut into strips Figure 8.14:

$$
\begin{array} { r l } & { \texttt { s s } ^ { i n } - \texttt { a t a u s t y } ^ { \mathrm { p a u c } } } \\ & { \texttt { t } M _ { y } = \int \left( \mathrm { d i s t a n c e } \ x \right) \left( \mathrm { l e n g t h ~ o f ~ v e r t i c a l ~ s t r i p } \right) d x } \\ & { \texttt { t } M _ { x } = \int \left( \mathrm { h e i g h t } \ y \right) \left( \mathrm { l e n g t h ~ o f ~ h o r i z o n t a l ~ s t r i p } \right) d y . } \end{array}
$$

The mass equals the area because $\rho = 1$ . For moments, all points in a vertical strip are the same distance from the $y$ axis. That distance is $x$ . The moment is $x$ times area, or $x$ times length times $d x$ —and the integral accounts for all strips.

Similarly the $x$ -moment of a horizontal strip is $y$ times strip length times $d y$

EXAMPLE 3 A plate has sides $x = 0$ and $y = 0$ and $y = 4 - 2 x$ . Find $M , M _ { y } , M _ { x }$ .

$$
\begin{array} { r } { \operatorname* { m a s s } M = \mathrm { a r e a } = \int _ { 0 } ^ { 2 } y \ d x = \int _ { 0 } ^ { 2 } \left( 4 - 2 x \right) d x = \left[ 4 x - x ^ { 2 } \right] _ { 0 } ^ { 2 } = 4 . } \end{array}
$$

The vertical strips go up to $y = 4 - 2 x$ , and the horizontal strips go out to $\scriptstyle x = { \frac { 1 } { 2 } } ( 4 -$ $y \backslash$ /:

$$
{ \begin{array} { r l } & { { \mathrm { m o m e n t } } M _ { y } = \int _ { 0 } ^ { 2 } x ( 4 - 2 x ) d x = { \biggl [ } 2 x ^ { 2 } - { \frac { 2 } { 3 } } x ^ { 3 } { \biggr ] } _ { 0 } ^ { 2 } = { \frac { 8 } { 3 } } } \\ & { { \mathrm { m o m e n t } } M _ { x } = \int _ { 0 } ^ { 4 } y { \frac { 1 } { 2 } } ( 4 - y ) d y = { \biggl [ } y ^ { 2 } - { \frac { 1 } { 6 } } y ^ { 3 } { \biggr ] } _ { 0 } ^ { 4 } = { \frac { 1 6 } { 3 } } . } \end{array} }
$$

The “center of mass” has $\bar { x } = M _ { y } / M = 2 / 3$ and $\bar { y } = M _ { x } / M = 4 / 3$ . This is the centroid of the triangle (and also the “center of gravity”). With $\rho = 1$ these terms all refer to the same balance point $( { \bar { x } } , { \bar { y } } )$ . The plate will not tip over, if it rests on that point.

EXAMPLE 4 Find $M _ { y }$ and $M _ { x }$ for the half-circle below $x ^ { 2 } + y ^ { 2 } = r ^ { 2 }$ .

$M _ { y } = 0$ because the region is symmetric—Figure 8.14 balances on the $y$ axis. In the $x$ -moment we integrate $y$ times the length of a horizontal strip (notice the factor 2):

$$
\begin{array} { r } { M _ { x } = \int _ { 0 } ^ { r } y \cdot 2 \sqrt { x ^ { 2 } - y ^ { 2 } } \ d y = - \frac { 2 } { 3 } ( r ^ { 2 } - y ^ { 2 } ) ^ { 3 / 2 } { \mathit { \Omega } } ] _ { 0 } ^ { r } = \frac { 2 } { 3 } r ^ { 3 } . } \end{array}
$$

Divide by the mass (the area ${ \frac { 1 } { 2 } } \pi r ^ { 2 } )$ to find the height of the centroid: $\bar { y } = M _ { x } / M =$ $4 r / 3 \pi$ .This is less than ${ \frac { 1 } { 2 } } r$ because the bottom of the semicircle is wider than the top.

# MOMENT OF INERTIA

The moment of inertia comes from multiplying each mass by the square of its distance from the axis. Around the $y$ axis, the distance is $x$ . Around the origin, it is $r$ :

$$
I _ { y } = \Sigma x _ { n } ^ { 2 } m _ { n } \mathrm { a n d } I _ { x } = \Sigma y _ { n } ^ { 2 } m _ { n } \mathrm { a n d } I _ { 0 } = \Sigma r _ { n } ^ { 2 } m _ { n } .
$$

Notice that $I _ { x } + I _ { y } = I _ { 0 }$ because $x _ { n } ^ { 2 } + y _ { n } ^ { 2 } = r _ { n } ^ { 2 }$ . In the continuous case we integrate.

The moment of inertia around the $y$ axis is $\begin{array} { r } { I _ { y } = \int \int x ^ { 2 } \rho ( x , y ) d x d y } \end{array}$ . With a constant density $\rho = 1$ , we again keep together the points on a strip. On a vertical strip they share the same $x$ . On a horizontal strip they share $y$ :

$I _ { y } = \int ( x ^ { 2 } )$ (vertical strip length) $d x$ and $I _ { x } = \int ( y ^ { 2 } )$ (horizontal strip length) $d y$ :

In engineering and physics, it is rotation that leads to the moment of inertia. Look at the energy of a mass $m$ going around a circle of radius $r$ . It has $I _ { 0 } = m r ^ { 2 }$ .

$$
\begin{array} { r } { \mathrm { k i n e t i c \ e n e r g y } = \frac { 1 } { 2 } m v ^ { 2 } = \frac { 1 } { 2 } m ( r \omega ) ^ { 2 } = \frac { 1 } { 2 } I _ { 0 } \omega ^ { 2 } . } \end{array}
$$

The angular velocity is $\omega$ (radians per second). The speed is $v = r \omega$ (meters per second).

An ice skater reduces $I _ { 0 }$ by putting her arms up instead of out. She stays close to the axis of rotation $\dot { \boldsymbol { r } }$ is small). Since her rotational energy ${ \scriptstyle { \frac { 1 } { 2 } } } I _ { 0 } \omega ^ { 2 }$ does not change, $\omega$ increases as $I _ { 0 }$ decreases. Then she spins faster.

Another example: It takes force to turn a revolving door. More correctly, it takes torque. The force is multiplied by distance from the turning axis: $T = F x$ , so a push further out is more effective.

To see the physics, replace Newton’s law $F = m a = m d v / d t$ by its rotational form: $T = I d \omega / d t$ . Where $F$ makes the mass move, the torque $T$ makes it turn. Where m measures unwillingness to change speed, $I$ measures unwillingness to change rotation.

EXAMPLE 5 Find the moment of inertia of a rod about (a) its end and (b) its center.

The distance $x$ from the end of the rod goes from 0 to $L$ . The distance from the center goes from $- L / 2$ to $L / 2$ . Around the center, turning is easier because $I$ is smaller:

$$
I _ { \mathrm { e n d } } = \int _ { 0 } ^ { L } x ^ { 2 } d x = { \textstyle { \frac { 1 } { 3 } } } L ^ { 3 } \qquad I _ { \mathrm { c e n t e r } } = \int _ { - L / 2 } ^ { L / 2 } x ^ { 2 } d x = { \textstyle { \frac { 1 } { 1 2 } } } L ^ { 3 } .
$$

# MOMENT OF INERTIA EXPERIMENT

Experiment: Roll a solid cylinder (a coin), a hollow cylinder (a ring), a solid ball (a marble), and a hollow ball (not a pingpong ball) down a slope. Galileo dropped things from the Leaning Tower—this experiment requires a Leaning Table. Objects that fall together from the tower don’t roll together down the table.

Question 1 What is the order of finish ? Record your prediction first! Question 2 Does size make a difference if shape and density are the same ? Question 3 Does density make a difference if size and shape are the same ?

# 8.5 Masses and Moments

Question 4 Find formulas for the velocity $v$ and the finish time $T$ .

To compute $v$ , the key is that potential energy plus kinetic energy is practically constant. Energy loss from rolling friction is very small. If the mass is $m$ and the vertical drop is $h$ , the energy at the top (all potential) is $m g h$ . The energy at the bottom (all kinetic) has two parts: $\scriptstyle { \frac { 1 } { 2 } } { \bar { m } } v ^ { 2 }$ from movement along the plane plus ${ \scriptstyle { \frac { 1 } { 2 } } } I \omega ^ { 2 }$ from turning. Important fact: $v = \omega r$ for a rolling cylinder or ball of radius $r$ .

Equate energies and set $\omega = v / r$ :

$$
m g h = \frac { 1 } { 2 } m v ^ { 2 } + \frac { 1 } { 2 } I \omega ^ { 2 } = \frac { 1 } { 2 } m v ^ { 2 } \left( 1 + \frac { I } { m r ^ { 2 } } \right) .
$$

The ratio $I / m r ^ { 2 }$ is critical. Call it $J$ and solve .11/ for $v ^ { 2 }$ :

$$
v ^ { 2 } = \frac { 2 g h } { 1 + J } \ ( s m a l l e r J \ m e a n s \ l a r g e r \ \nu e l o c i t y ) .
$$

The order of $J$ ’s, for different shapes and sizes, should decide the race. Apparently the density doesn’t matter, because it is a factor in both $I$ and $m$ —so it cancels in $J = { I } / { m r ^ { 2 } }$ . A hollow cylinder has $J = 1$ , which is the largest possible—all its mass is at the full distance $r$ from the axis. So the hollow cylinder should theoretically come in last. This experiment was developed by Daniel Drucker.

Problems $3 5 - 3 7$ find the other three $J$ ’s. Problem 40 finds the time $T$ by integration. Your experiment will show how close this comes to the measured time.