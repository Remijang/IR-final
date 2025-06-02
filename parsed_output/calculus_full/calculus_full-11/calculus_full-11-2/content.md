# 11.2 Planes and Projections

The most important “curves” are straight lines. The most important functions are linear. Those sentences take us back to the beginning of the book—the graph of $m x + b$ is a line. The goal now is to move into three dimensions, where graphs are surfaces. Eventually the surfaces will be curved. But calculus starts with the flat surfaces that correspond to straight lines:

What are the most important surfaces ? Planes.   
What are the most important functions ? Still linear.

The geometrical idea of a plane is turned into algebra, by finding the equation of a plane. Not just a general formula, but the particular equation of a particular plane.

A line is determined by one point $( x _ { 0 } , y _ { 0 } )$ and the slope m. The point-slope equation is $y - y _ { 0 } = m ( x - x _ { 0 } )$ . That is a linear equation, it is satisfied when $y = y _ { 0 }$ and $x = x _ { 0 }$ , and $d y / d x$ is $m$ . For a plane, we start again with a particular point— which is now $( x _ { 0 } , y _ { 0 } , z _ { 0 } )$ . But the slope of a plane is not so simple. Many planes climb at a $4 5 ^ { \circ }$ angle—with “slope 1”—and more information is needed.

The direction of a plane is described by a vector $\mathbf { N }$ . The vector is not $\dot { \iota } n$ the plane, but perpendicular to the plane. In the plane, there are many directions. Perpendicular to the plane, there is only one direction. A vector in that perpendicular direction is a normal vector.

The normal vector $\mathbf { N }$ can point “up” or “down”. The length of $\mathbf { N }$ is not crucial (we often make it a unit vector and call it $\mathbf { n }$ ). Knowing $\mathbf { N }$ and the point $P _ { 0 } = ( x _ { 0 } , y _ { 0 } , z _ { 0 } )$ , we know the plane (Figure 11.9). For its equation we switch to algebra and use the dot product—which is the key to perpendicularity.

$\mathbf { N }$ is described by its components $( a , b , c )$ . In other words $\mathbf { N }$ is $a \mathbf { i } + b \mathbf { j } + c \mathbf { k }$ . This vector is perpendicular to every direction in the plane. A typical direction goes from

$P _ { 0 }$ to another point $P = ( x , y , z )$ in the plane. The vector from $P _ { 0 }$ to $P$ has components $( x - x _ { 0 } , y - y _ { 0 } , z - z _ { 0 } )$ : This vector lies in the plane, so its dot product with $\mathbf { N }$ is zero:

11C The plane through $P _ { 0 }$ perpendicular to $\mathbf { N } = ( a , b , c )$ has the equation $( a , b , c ) \cdot ( x - x _ { 0 } , y - y _ { 0 } , z - z _ { 0 } ) = 0 \quad { \mathrm { o r } } \quad$ $a ( x - x _ { 0 } ) + b ( y - y _ { 0 } ) + c ( z - z _ { 0 } ) = 0 .$ : (1)   
The point $P$ lies on the plane when its coordinates $x , y , z$ satisfy this equation.

# 11.2 Planes and Projections

EXAMPLE 1 The plane through $P _ { 0 } = ( 1 , 2 , 3 )$ perpendicular to ${ \bf N } = ( 1 , 1 , 1 )$ has the equation $( x - 1 ) + ( y - 2 ) + ( z - 3 ) = 0 .$ . That can be rewritten as $x + y + z =$ 6.

Notice three things. First, $P _ { 0 }$ lies on the plane because $1 + 2 + 3 = 6$ . Second, ${ \bf N } = ( 1 , 1 , 1 )$ can be recognized from the $x , y , z$ coefficients in $x + y + z = 6$ . Third, we could change $\mathbf { N }$ to $( 2 , 2 , 2 )$ and we could change $P _ { 0 }$ to $( 8 , 2 , - 4 )$ —because $\mathbf { N }$ is still perpendicular and $P _ { 0 }$ is still in the plane: $8 + 2 - 4 = 6$ .

The new normal vector ${ \bf N } = ( 2 , 2 , 2 )$ produces $2 ( x - 1 ) + 2 ( y - 2 ) + 2 ( z - 3 ) =$ 0. That can be rewritten as $2 x + 2 y + 2 z = 1 2 .$ Same normal direction, same plane.

The new point $P _ { 0 } = ( 8 , 2 , - 4 )$ produces $( x - 8 ) + ( y - 2 ) + ( z + 4 ) = 0 .$ . That is another form of $x + y + z = 6$ . All we require is a perpendicular $\mathbf { N }$ and a point $P _ { 0 }$ in the plane.

EXAMPLE 2 The plane through .1;2;4/ with the same ${ \bf N } = ( 1 , 1 , 1 )$ has a different equation: $( x - 1 ) + ( y - 2 ) + ( z - 4 ) = 0$ . This is $x + y + z = 7$ (instead of 6). These planes with 7 and 6 are parallel.

Starting from $a ( x - x _ { 0 } ) + b ( y - y _ { 0 } ) + c ( z - z _ { 0 } ) = 0$ , we often move $a x _ { 0 } + b y _ { 0 } +$ $c z _ { 0 }$ to the right hand side—and call this constant $d$ :

EXAMPLE 3 The plane $x - y + 3 z = 0$ goes through the origin $( 0 , 0 , 0 )$ . The normal vector is read directly from the equation: $\mathbf { N } = ( 1 , - 1 , 3 )$ . The equation is satisfied by $P _ { 0 } = ( 1 , 1 , 0 )$ and $P = ( 1 , 4 , 1 )$ . Subtraction gives a vector $\mathbf { V } = ( 0 , 3 , 1 )$ that is in the plane, and $\mathbf { N } { \cdot } \mathbf { V } = 0$ .

The parallel planes $x - y + 3 z = d$ have the same $\mathbf { N }$ but different $d$ ’s. These planes miss the origin because $d$ is not zero . $( x = 0 , y = 0 , z = 0$ on the left side needs $d = 0$ on the right side). Note that $3 x - 3 y + 9 z = - 1 5$ is parallel to both planes. $\mathbf { N }$ is changed to 3N in Figure 11.9, but its direction is not changed.

EXAMPLE 4 The angle between two planes is the angle between their normal vectors.

The planes $x - y + 3 z = 0$ and $3 y + z = 0$ ar|e perpen|d i|cula||r, be|cause $( 1 , - 1 , 3 )$ $( 0 , 3 , 1 ) = 0$ . The planes $z = 0$ and $y = 0$ are also perpendicular, because $( 0 , 0 , 1 )$ $( 0 , 1 , 0 ) = 0$ . (Those are the $x y$ plane and the $x z$ plane.) The planes $x + y = 0$ and $x + z = 0$ make a $6 0 ^ { \circ }$ angle, because cos $6 0 ^ { \circ } = ( 1 , 1 , 0 ) \cdot ( 1 , 0 , 1 ) / \sqrt { 2 } \sqrt { 2 } = \frac { 1 } { 2 }$ .

The cosine of the angle between two planes is $\left| { \bf N } _ { 1 } \cdot { \bf N } _ { 2 } \right| / \left| { \bf N } _ { 1 } \right| \left| { \bf N } _ { 2 } \right|$ . See Figure 11.10.

Remark 1 We gave the “point-slope” equation of a line (using $m$ ), and the “pointnormal” equationof a plane (using $\mathbf { N }$ ). What is the normal vector $\mathbf { N }$ toa line ?

The vector $\mathbf { V } = ( 1 , m )$ is parallel to the line $y = m x + b$ . The line goes across by 1 and up by $m$ . The perpendicular vector is $\mathbf { N } = ( - m , 1 )$ . The dot product $\mathbf { N } { \cdot } \mathbf { V }$ is $- m + m = 0$ . Then the point-normal equation matches the point-slope equation:

$$
- m ( x - x _ { 0 } ) + 1 ( y - y _ { 0 } ) = 0 { \mathrm { ~ i s ~ t h e ~ s a m e ~ a s ~ } } y - y _ { 0 } = m ( x - x _ { 0 } ) .
$$

Remark 2 What is the point-slope equation for a plane ? The difficulty is that a plane has different slopes in the $x$ and $y$ directions. The function $f ( x , y ) =$ $m ( x - x _ { 0 } ) + M ( y - y _ { 0 } )$ has two derivatives $m$ and $M$ .

This remark has to stop. In Chapter 13; “slopes” become “partial derivatives.”

# A LINE IN SPACE

In three dimensions, a line is not as simple as a plane. $A$ line in space needs two equations. Each equation gives a plane, and the line is the intersection of two planes.

Two points on that line are $P _ { 0 } = ( 1 , 1 , 1 )$ and $\mathcal { Q } = ( 3 , 0 , 0 )$ . They satisfy both equations so they lie on both planes. Therefore they are on the line of intersection. The direction of that line, subtracting coordinates of $P _ { 0 }$ from $\boldsymbol { Q }$ , is along the vector $\mathbf { V } = 2 \mathbf { i } - \mathbf { j } - \mathbf { k }$ .

The line goes through $P _ { 0 } = ( 1 , 1 , 1 )$ in the direction of ${ \bf V } = 2 { \bf i } - { \bf j } - { \bf k }$ :

Starting from $( x _ { 0 } , y _ { 0 } , z _ { 0 } ) = ( 1 , 1 , 1 ) ,$ , add on any multiple $t { \bf V }$ . Then $x = 1 + 2 t$ and

$y = 1 - t$ and $z = 1 - t$ . Those are the components of the vector equation $\mathbf { P } = \mathbf { P } _ { 0 } + t \mathbf { V }$ —which produces the line.

Here is the problem. The line needs two equations—or a vector equation with a parameter $t$ . Neither form is as simple as $a x + b y + c z = d$ . Some books push ahead anyway, to give full details about both forms. After trying this approach, I believe that those details should wait. Equations with parameters are the subject of Chapter 12; and a line in space is the first example. Vectors and planes give plenty to do here—especially when a vector is projected onto another vector or a plane.

# PROJECTION OF A VECTOR

What is the projection of a vector $\mathbf { B }$ onto another vector A ? One part of $\mathbf { B }$ goes along A—that is the projection. The other part of $\mathbf { B }$ is perpendicular to A. We now compute these two parts, which are $\mathbf { P }$ and $\mathbf { B } - \mathbf { P }$ .

In geometry, projections involve $\cos \theta$ . In algebra, we use the dot product (which is closely tied to $\cos \theta$ ). In applications, the vector $\mathbf { B }$ might be a velocity $\mathbf { V }$ or a force F:

An airplane flies northeast, and a 100-mile per hour wind blows due east. What is the projection of $\mathbf { V } = ( 1 0 0 , 0 )$ in the flight direction A ?

Gravity makes a ball roll down the surface $2 x + 2 y + z = 0$ . What are the projections of $\mathbf { F } = ( 0 , 0 , - m g )$ in the plane and perpendicular to the plane ?

The component of $\mathbf { V }$ along $\mathbf { A }$ is the push from the wind (tail wind). The other component of $\mathbf { V }$ pushes sideways (crosswind). Similarly the force parallel to the surface makes the ball move. Adding the two components brings back $\mathbf { V }$ or $\mathbf { F }$ .

We now compute the projection of B onto A. Call this projection $\mathbf { P }$ . |Sin|ce its direction i|s |kno |wn|—P is along A—we can describe $\mathbf { P }$ in twoways:

1) Give the length of P along A   
2) Give the vector P as a multiple of A.

Figure 11.11b shows the projection $\mathbf { P }$ and its length. The hypotenuse is $\mathbf { \left| B \right| }$ . The length is $| \mathbf { P } | = | \mathbf { B } | \cos \theta$ . The perpendicular component $\mathbf { B } - \mathbf { P }$ has length $\left| \mathbf { B } \right| \sin \theta$ . The cosine is positive for angles less than $9 0 ^ { \circ }$ : The cosine (and $\mathbf { P } !$ ) are zero when A and $\mathbf { B }$ are perpendicular. $\| \mathbf { B } | \cos \theta$ is negative for angles greater than $9 0 ^ { \circ }$ ; and the projection points along – A (the length is $| \mathbf { B } | | \cos \theta | )$ . Unless the angle is $0 ^ { \circ }$ or $3 0 ^ { \circ }$ or $4 5 ^ { \circ }$ or $6 0 ^ { \circ }$ or $9 0 ^ { \circ }$ ; we don’t want to compute cosines—and we don’t have to. The dot product does it automatically:

$$
\left| \mathbf { A } \right| \left| \mathbf { B } \right| \cos \theta = \mathbf { A } \cdot \mathbf { B } { \mathrm { ~ } } s o t h e { ~ l e n g t h ~ o f ~ } \mathbf { P } { \mathrm { ~ } } a l o n g { \mathrm { ~ A ~ } } i s \ \left| \mathbf { B } \right| \cos \theta = { \frac { \mathbf { A } \cdot \mathbf { B } } { \left| \mathbf { A } \right| } } .
$$

Notice that the length of $\mathbf { A }$ cancels out at the end of (4). If $\mathbf { A }$ is doubled, $\mathbf { P }$ is unchanged. But if $\mathbf { B }$ is doubled, the projection is doubled.

What is the vector $\mathbf { P }$ ? Its length along $\mathbf { A }$ is $\mathbf { A \cdot B } / | \mathbf { A } |$ . If $\mathbf { A }$ is a unit vector, then $| \mathbf { A } | = 1$ and the projection is $\mathbf { A \cdot B }$ times A. Generally $\mathbf { A }$ is not a unit vector, until we divide by $\mathbf { \left| A \right| }$ . Here is the projection P of B along A:

$$
\mathbf { P } = ( l e n g t h o f \mathbf { P } ) ( u n i t \nu e c t o r ) = \left( { \frac { \mathbf { A } \cdot \mathbf { B } } { | \mathbf { A } | } } \right) \left( { \frac { \mathbf { A } } { | \mathbf { A } | } } \right) = { \frac { \mathbf { A } \cdot \mathbf { B } } { | \mathbf { A } | ^ { 2 } } } \mathbf { A } .
$$

EXAMPLE 5 For the wind velocity $\mathbf { V } = ( 1 0 0 , 0 )$ and flying direction $\mathbf { A } = ( 1 , 1 )$ , find P. Here $\mathbf { V }$ points east, $\mathbf { A }$ points northeast. The projection of $\mathbf { V }$ onto $\mathbf { A }$ is $\mathbf { P }$ :

$$
\operatorname { l e n g t h } | \mathbf { P } | = { \frac { \mathbf { A } \cdot \mathbf { V } } { | \mathbf { A } | } } = { \frac { 1 0 0 } { \sqrt { 2 } } } \quad { \mathrm { ~ v e c t o r ~ } } \mathbf { P } = { \frac { \mathbf { A } \cdot \mathbf { V } } { | \mathbf { A } | ^ { 2 } } } \mathbf { A } = { \frac { 1 0 0 } { 2 } } ( 1 , 1 ) = ( 5 0 , 5 0 ) .
$$

EXAMPLE 6 Project $\mathbf { F } = ( 0 , 0 , - m g )$ onto the plane with normal ${ \bf N } = ( 2 , 2 , 1 )$ .

The projection of $\mathbf { F }$ along $\mathbf { N }$ is not the answer. But compute that first:

$$
{ \frac { \mathbf { F } \cdot \mathbf { N } } { | \mathbf { N } | } } = - { \frac { m g } { 3 } } \quad \mathbf { P } = { \frac { \mathbf { F } \cdot \mathbf { N } } { | \mathbf { N } | ^ { 2 } } } \mathbf { N } = - { \frac { m g } { 9 } } ( 2 , 2 , 1 ) .
$$

$\mathbf { P }$ is the component of| $\mathbf { F }$ perpendicular to the plane. It does not move the ball. The in-plane component is the difference $\mathbf { F } - \mathbf { P }$ . Any vector $\mathbf { B }$ has two projections, along $\mathbf { A }$ and perpendicular:

The projection $\mathbf { P } = { \frac { \mathbf { A \cdot B } } { | \mathbf { A } | ^ { 2 } } } \mathbf { A }$ is perpendicular to the remaining component $\mathbf { B } - \mathbf { P }$

EXAMPLE 7 Express $\mathbf { B } = \mathbf { i } - \mathbf { j }$ as the sum of a vector $\mathbf { P }$ parallel to $\mathbf { A } = 3 \mathbf { i } + \mathbf { j }$ and a vector $\mathbf { B } - \mathbf { P }$ perpendicular to A. Note $\mathbf { A \cdot B } = 2$ .

$$
\mathbf { P } = { \frac { \mathbf { A } \cdot \mathbf { B } } { | \mathbf { A } | ^ { 2 } } } \mathbf { A } = { \frac { 2 } { 1 0 } } \mathbf { A } = { \frac { 6 } { 1 0 } } \mathbf { i } + { \frac { 2 } { 1 0 } } \mathbf { j } . \quad \operatorname { T h e n } \mathbf { B } - \mathbf { P } = { \frac { 4 } { 1 0 } } \mathbf { i } - { \frac { 1 2 } { 1 0 } } \mathbf { j } .
$$

Check: $\begin{array} { r } { \mathbf { P } { \cdot } ( \mathbf { B } - \mathbf { P } ) = \left( \frac { 6 } { 1 0 } \right) \left( \frac { 4 } { 1 0 } \right) - \left( \frac { 2 } { 1 0 } \right) \left( \frac { 1 2 } { 1 0 } \right) = 0 } \end{array}$ : These projections of $\mathbf { B }$ are perpendicular.

Pythagoras: $| { \bf P } | ^ { 2 } + | { \bf B } - { \bf P } | ^ { 2 }$ equals $| \mathbf { B } | ^ { 2 }$ . Check that too: $0 . 4 + 1 . 6 = 2 . 0$ .

Question When is $\mathbf { P } = \mathbf { 0 }$ ? Answer When $\mathbf { A }$ and $\mathbf { B }$ are perpendicular.

EXAMPLE 8 Find the nearest point to the origin on the plane $x + 2 y + 2 z =$ 5.

The shortest distance from the origin is along the normal vector N. The vector $\mathbf { P }$ to the nearest point (Figure 11.12) is $t$ times $\mathbf { N }$ , for some unknown number $t$ . We find $t$ by requiring $\mathbf { P } = t \mathbf { N }$ to lie on the plane.

The plane $x + 2 y + 2 z = 5$ has normal vector ${ \bf N } = ( 1 , 2 , 2 )$ . Therefore $\mathbf { P } = t \mathbf { N } =$ $( t , 2 t , 2 t )$ . To lie on the plane, this must satisfy $x + 2 y + 2 z = 5$ :

$$
t + 2 ( 2 t ) + 2 ( 2 t ) = 5 \quad \mathrm { o r } \quad 9 t = 5 \quad \mathrm { o r } \quad t = \frac { 5 } { 9 } .
$$

Then $\mathbf { P } { = } \textstyle { \frac { 5 } { 9 } } \mathbf { N } { = } ( \textstyle { \frac { 5 } { 9 } } , \frac { 1 0 } { 9 } , \frac { 1 0 } { 9 } )$ . That locates the nearest point. The distance is $\begin{array} { r } { \frac { 5 } { 9 } | { \bf N } | = \frac { 5 } { 3 } } \end{array}$ . This example is important enough to memorize, with lett?ers not numbers:

$$
P = { \frac { ( d a , d b , d c ) } { a ^ { 2 } + b ^ { 2 } + c ^ { 2 } } } . \qquad { \mathrm { T h e ~ d i s t a n c e ~ i s } } \quad { \frac { | d | } { \sqrt { a ^ { 2 } + b ^ { 2 } + c ^ { 2 } } } } .
$$

The steps are the same. $\mathbf { N }$ has components $_ { a , b , c }$ . The nearest point on the plane is a multiple $( t a , t b , t c )$ . It lies on the plane if $a ( t a ) + b ( t b ) + c ( t c ) = d$ .

Thus $t = d / ( a ^ { 2 } + b ^ { 2 } + c ^ { 2 } )$ . The point $( t a , t b , t c ) = t \mathbf { N }$ is in equation (7). The distance to the plane is $\lvert t \mathbf { N } \rvert = \lvert d \rvert / \lvert \mathbf { N } \rvert$ .

Question How far is the plane from an arbitrary point $Q = ( x _ { 1 } , y _ { 1 } , z _ { 1 } ) ^ { \prime }$ ?

Answer The vector from $\boldsymbol { Q }$ to $P$ is our multiple $t \mathbf { N }$ . In vector form ${ \bf P } = { \bf Q } + t { \bf N }$ . This reaches the plane if $\mathbf { P } \cdot \mathbf { N } = d$ , and again we find $t$ :

$$
( { \bf Q } + t { \bf N } ) \cdot { \bf N } = d \mathrm {  ~ \ y i e l d s ~ } t = ( d - { \bf Q } \cdot { \bf N } ) / | { \bf N } | ^ { 2 } .
$$

This new term $\mathbf { Q \cdot N }$ enters the distance from $\boldsymbol { Q }$ to the plane:

$$
d i s t a n c e = | t { \bf N } | = | d - { \bf Q } \cdot { \bf N } | / | { \bf N } | = | d - a x _ { 1 } - b y _ { 1 } - c z _ { 1 } | / \sqrt { a ^ { 2 } + b ^ { 2 } + c ^ { 2 } } .
$$

When the point is on the plane, that distance is zero—because $a x _ { 1 } + b y _ { 1 } + c z _ { 1 } = d$ .   
When $\mathbf { Q }$ is $\mathbf { i } + 3 \mathbf { j } + 2 \mathbf { k }$ , the figure shows $\mathbf { Q \cdot N } = 1 1$ and distance $= 2$ .

# PROJECTIONS OF THE HEART VECTOR

An electrocardiogram has leads to your right arm–left arm–left leg. You produce the voltage. The machine amplifies and records the readings. There are also six chest leads, to add a front-back dimension that is monitored across the heart. We will concentrate on the big “Einthoven triangle,” named after the inventor of the ECG.

The graphs show voltage variations plotted against time. The first graph plots the voltage difference between the arms. Lead II connects the left leg to the right arm. Lead III completes the triangle, which has roughly equal sides (especially if you are a little lopsided). So the projections a re based on $6 0 ^ { \circ }$ and $1 2 0 ^ { \circ }$ angles.

The heart vector $\mathbf { V }$ is the sum of many small vectors—all moved to the same origin. $\mathbf { V }$ is the net effect of action potentials from the cells—small dipoles adding to a single dipole. The pacemaker $S { - } A$ node) starts the impulse. The atria depolarize to give the $\mathrm { \bf P }$ wave on the graphs. This is actually a $\mathrm { \bf P }$ loop of the heart vector— the graphs only show its projections. The impulse reaches the $A V$ node, pauses, and moves quickly through the ventricles. This produces the QRS complex—the large sharp movement on the graph.

The total QRS interval should not exceed $1 / 1 0$ second $( 2 { \frac { 1 } { 2 } }$ spaces on the printout). V points first toward the right shoulder. This direction is opposite to the leads, so the tracings go slightly down. That is the Q wave, small and negative. Then the heart vector sweeps toward the left leg. In positions 3 and 4, its projection on lead I (between the arms) is strongly positive. The R wave is this first upward deflection in each lead. Closing the loop, the S wave is negative (best seen in leads I and aVR).

Question 1 How many graphs from the arms and leg are really independent ?

Answer Only two! In a plane, the heart vector $\mathbf { V }$ has two components. If we know two projections, we can compute the others. (The ECG does that for us.) Different vectors show better in different projections. A mathematician would use $9 0 ^ { \circ }$ angles, with an electrode at your throat.

Question 2 How are the voltages related ? What is the aVR lead ?

Answer Project the heart vector $\mathbf { V }$ onto the sides?of the triangle:

The lead vectors have $\mathbf { L } _ { \mathrm { I } } - \mathbf { L } _ { \mathrm { I I } } + \mathbf { L } _ { \mathrm { I I I } } = \mathbf { 0 } .$ — they form a triangle. The projections have $\mathbf { V } _ { \mathrm { I } } - \mathbf { V } _ { \mathrm { I I } } + \mathbf { V } _ { \mathrm { I I I } } = \mathbf { V } \cdot \mathbf { L } _ { \mathrm { I } } - \mathbf { V } \cdot \mathbf { L } _ { \mathrm { I I } } + \mathbf { V } \cdot \mathbf { L } _ { \mathrm { I I I } } = 0 .$

The aVR lead is $- { \textstyle \frac { 1 } { 2 } } \mathbf { L } _ { \mathbf { I } } - { \textstyle \frac { 1 } { 2 } } \mathbf { L } _ { \mathbf { I I } }$ . It is pure algebra (no wire). By vector addition it points toward the electrode on the right arm. Its length is $\sqrt { 3 }$ if the other lengths are 2:

Including aVL and aVF to the left arm and foot, there are six leads intersecting at equal angles. Visualize them going out f?rom a single point (the?origin in the chest).

Question 3 If the heart vector is ${ \bf V } = 2 { \bf i } - { \bf j }$ , what voltage differences are recorded ?

Answer The leads around the triangle have length 2: The machine projects $\mathbf { V }$ :

Lead I is the horizontal vector 2i. So $\mathbf { V } \cdot \mathbf { L _ { I } } = 4$ .   
Lead II is the $- 6 0 ^ { \circ }$ vector $\mathbf { i } - \sqrt { 3 } \mathbf { j }$ . So $\mathbf { V } \cdot \mathbf { L } _ { \Pi } = 2 + { \sqrt { 3 } }$ .   
Lead III is the $- 1 2 0 ^ { \circ }$ vector $- \mathbf { i } - \sqrt { 3 } \mathbf { j }$ . So $\mathbf { V } \cdot \mathbf { L } _ { \mathbf { I I I } } = - 2 + { \sqrt { 3 } }$ .

The first and third add to the second. The largest $\mathtt { R }$ waves are in leads I and $\mathrm { I I }$ . In aVR the projection of $\mathbf { V }$ will be negative (Problem 46), and will be labeled an S wave.

Question 4 What about the potential (not just its differences). Is it zero at the center ?

Answer It is zero if we say so. The potential contains an arbitrary constant $C$ . (It is like an indefinite integral. Its differences are like definite integrals.) Cardiologists define a “central terminal” where the potential is zero.

The average of $\mathbf { V }$ over a loop is the mean heart vector H. This average requires $\textstyle \int \mathbf { V } d t$ , by Chapter 5: With no time to integrate, the doctor looks for a lead where the area under the QRS complex is zero. Then the direction of $\mathbf { H }$ (the axis) is perpendicular to that lead. There is so much to say about calculus in medicine.