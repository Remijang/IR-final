# 15.2 Line Integrals

A line integral is an integral along a curve. It can equal an area, but that is a special case and not typical. Instead of area, here are two important line integrals in physics and engineering:

$$
W o r k ~ a l o n g ~ a ~ c u r v e = \int _ { c } \mathbf { F } \cdot \mathbf { T } ~ d s ~ F l o w ~ a c r o s s ~ a ~ c u r v e = \int _ { c } \mathbf { F } \cdot \mathbf { n } ~ d s .
$$

In the first integral, $\mathbf { F }$ is a force field. In the second integral, $\mathbf { F }$ is a flow field. Work is done in the direction of movement, so we integrate ${ \bf { F } } \cdot { \bf { T } }$ . Flow is measured through the curve $C$ , so we integrate $\mathbf { F } \cdot \mathbf { n }$ . Here $\mathbf { T }$ is the unit tangent vector, and ${ \bf { F } } \cdot { \bf { T } }$ is the force component along the curve. Similarly $\mathbf { n }$ is the unit normal vector, at right angles with $\mathbf { T }$ . Then $\mathbf { F } \cdot \mathbf { n }$ is the component of flow perpendicular to the curve.

We will write those integrals in several forms. They may never be as comfortable as $\int y ( x ) d x$ , but eventually we get them under control. I mention these applications early, so you can see where we are going. This section concentrates on work, and flow comes later. (It is also called flux—the Latin word for flow.) You recognize $d s$ as the step along the curve, corresponding to $d x$ on the $x$ axis. Where $\textstyle \int d x$ gives the length of an interval (it equals $b - a )$ ), $\int d s$ is the length of the curve.

EXAMPLE 1 Flight from Atlanta to Los Angeles on a straight line and a semicircle.

According to Delta Airlines, the distance straight west is 2000 miles. Atlanta is at $( 1 0 0 0 , 0 )$ and Los Angeles is at $( - 1 0 0 0 , 0 )$ , with the origin halfway between. The semicircle route $C$ has radius 1000. This is not a great circle route. It is more of a “flat circle,” which goes north past Chicago. No plane could fly it (it probably goes into space).

The equation for the semicircle is $x ^ { 2 } + y ^ { 2 } = 1 0 0 0 ^ { 2 }$ . Parametrically this path is $x = 1 0 0 0 \cos t , y = 1 0 0 0 \sin t$ . For a line integaral the parameter is better. The plane leaves Atlanta at $t = 0$ and reaches L.A. at $t = \pi$ ,more than  three hours later. On the straight 2000-mile path, Delta could almost do it. Around the semicircle $C$ , the distance is $1 0 0 0 \pi$ miles and the speed has to be 1000 miles pe rhour. Remember that speed is distance $d s$ divided by time $d t$ :

$$
d s / d t = { \sqrt { ( d x / d t ) ^ { 2 } + ( d y / d t ) ^ { 2 } } } = 1 0 0 0 { \sqrt { ( - \sin t ) ^ { 2 } + ( - \cos t ) ^ { 2 } } } = 1 0 0 0 .
$$

The tangent vector to $C$ is proportional to $( d x / d t , d y / d t ) = ( - 1 0 0 0 \sin t , 1 0 0 0 \cos t ) .$ Bu»t $\mathbf { T }$ is a unit ve»ctor, so we divide by 1000—»which is the speed.

Suppose the wind bl ows due east with force $\mathbf { F } = M \mathbf { i }$ . The componentsare $M$ and zero. For $M =$ constant, compute the dot product ${ \bf { F } } \cdot { \bf { T } }$ and the work $- 2 0 0 0 \ : M$ :

$$
\mathbf { F } \cdot \mathbf { T } = M \mathbf { i } \cdot ( - \sin t \mathbf { i } + \cos t \mathbf { j } = M ( - \sin t ) + 0 ( \cos t ) = - M \sin t
$$

$$
\int _ { c } \mathbf { F } \cdot \mathbf { T } d s = \int _ { t = 0 } ^ { \pi } ( - M \sin t ) \left( { \frac { d s } { d t } } d t \right) = \int _ { 0 } ^ { \pi } - 1 0 0 0 M \sin t d t = - 2 0 0 0 M .
$$

Work is force times distance moved. It is negative, because the wind acts against the movement. You may point out that the work could have been found more simply—go 2000 miles and multiply by $- M . 1$ would object that this straight route is a different path. But you claim that the path doesn’t matter—the work of the wind is $- 2 0 0 0 M$ on every path. I concede that this time you are right (but not always).

Most line integrals depend on the path. Those that don’t are crucially important. For a gradient field, we only need to know the starting point $P$ and the finish $\boldsymbol { Q }$ .

15B When $\mathbf { F }$ is the gradient of a potential function $f ( x , y )$ , the work $\int _ { c } \mathbf { F } \cdot \mathbf { T } d s$ depends only on the endpoints $P$ and $\boldsymbol { Q }$ . The work is the change in $\bar { f }$ :

$$
\mathbf { F } = { \hat { \sigma } } f / { \hat { \sigma } } x \mathbf { i } + { \hat { \sigma } } f / { \hat { \sigma } } y \mathbf { j } \quad { \mathrm { t h e n } } \quad \int _ { c } \mathbf { F } \cdot \mathbf { T } d s = f ( Q ) - f ( P ) .
$$

When $\mathbf { F } = M \mathbf { i }$ , its components $M$ and  zero are the partial derivatives of $f = M x$ . To compute the line integral, just evaluate $f$ at the endpoints. Atlanta has $x = 1 0 0 0$ , Los Angeles has $x = - 1 0 0 0$ , and the potential function $f = M x$ is like an antiderivative:

$$
\mathrm { w o r k } = f ( Q ) - f ( P ) = M ( - 1 0 0 0 ) - M ( 1 0 0 0 ) = - 2 0 0 0 M .
$$

May I give a rough explanation of the work integral $\int \mathbf { F } \cdot \mathbf { T } d s ?$ It becomes clearer when the small movement T $d s$ is written as $d x \mathbf { i } + d y \mathbf { j }$ j. The work is the dot product with $\mathbf { F }$ :

$$
\mathbf { F } \cdot \mathbf { T } d s = \left( { \frac { \partial f } { \partial x } } \mathbf { i } + { \frac { \partial f } { \partial y } } \mathbf { j } \right) \cdot ( d x \mathbf { i } + d y \mathbf { j } ) = { \frac { \partial f } { \partial x } } d x + { \frac { \partial f } { \partial y } } d y = d f .
$$

The infinitesimal work is $d f$ . The total work is $\begin{array} { r } { \int d f = f ( Q ) - f ( P ) } \end{array}$ . This is the Fundamental Theorem for a line integral. Only one warning: When $\mathbf { F }$ is not the gradient of any $f$ (Example 2), the Theorem does not apply.

EXAMPLE 2 Fly these paths against the non-constant force field $\mathbf { F } = M y \mathbf { i }$ .   
Compute the work.

There is no force on the straight path where $y = 0$ . Along the $x$ axis the wind does no work. But the se micircle goes up where $y = 1 0 0 0 \sin t$ and the windis strong:

$$
\mathbf { F } { \boldsymbol { \cdot } } \mathbf { T } ( M y \mathbf { i } ) { \boldsymbol { \cdot } } ( - \sin t \mathbf { i } + \cos t \mathbf { j } ) = - M y \sin t = - 1 0 0 0 M \sin ^ { 2 } t
$$

$$
\int _ { c } \mathbf { F } \cdot \mathbf { T } d s = \int _ { 0 } ^ { \pi } ( - 1 0 0 0 M \sin ^ { 2 } t ) { \frac { d s } { d t } } d t = \int _ { 0 } ^ { \pi } - 1 0 ^ { 6 } M \sin ^ { 2 } t d t = - { \frac { \pi } { 2 } } 1 0 ^ { 6 } M .
$$

This work is enormous (and unrealistic). But the calculations make an important point— everything is converted to the parameter $t$ . The second point is that $\mathbf { F } = M y \mathbf { i }$ is not a gradient field. First reason: The work was zero on the straight path and nonzero on the semicircle. Second reason: No function has $\partial f / \partial x = M y$ and $\partial f / \partial y = 0$ . (The first makes $f$ depend on $y$ and the second forbids it. This $\mathbf { F }$ is called a shear force.) Without a potential we cannot substitute $P$ and $\boldsymbol { \mathcal { Q } }$ —and the work depends on the path.

# THE DEFINITION OF LINE INTEGRALS

We go back to the start, to define $\int \mathbf { F } \cdot \mathbf { T } d s$ . We can think of ${ \bf { F } } \cdot { \bf { T } }$ as a function $g ( x , y )$ along the path, and define its integral as a limit of sums:

$$
\int _ { c } g ( x , y ) d s = \mathrm { { l i m i t } } \mathrm { { o f } } \sum _ { i = 1 } ^ { N } g ( x _ { i } , y _ { i } ) \Delta s _ { i } \quad \mathrm { { a s } } \quad ( \Delta s ) _ { \mathrm { { m a x } } }  0 .
$$

The points $( x _ { i } , y _ { i } )$ lie on the curve $C$ . The last point $\boldsymbol { Q }$ is $( x _ { N } , y _ { N } )$ ; the first point $P$ is $( x _ { 0 } , y _ { 0 } )$ . The step $\Delta { { s } _ { i } }$ is the distance to $( x _ { i } , y _ { i } )$ from the previous point. As the steps get small . $\Delta s  0 )$ the straight pieces follow the curve. Exactly as in Section 8:2, the special case $g = 1$ gives the arc length. As long as $g ( x , y )$ is piecewise continuous (jumps allowed) and the path is piecewise smooth (corners allowed), the limit exists and defines the line integral.

When $g$ is the density of a wire, the line integral is the total mass. When $g$ is $\mathbf { F } \cdot \mathbf { T }$ , the integra»l is the work. »But nobody does the calculation by formula (5). We now introduce a parameter $t$ —which could be the time, or the arc length $s$ , or the distance $x$ along the base.

The differential ds becomes $( d s / d t ) d t$ . Everything changes over to $t$ :

$$
\int g ( x , y ) d s = \int _ { t = a } ^ { t = b } g ( x ( t ) , y ( t ) ) \sqrt { ( d x / d t ) ^ { 2 } + ( d y / d t ) ^ { 2 } } d t .
$$

The curve starts when $t = a$ , runs through the points $( x ( t ) , y ( t ) )$ , and ends when $t = b$ . The square root in the integral is the speed $d s / d t$ . In three dimensions the points on $C$ are $( x ( t ) , y ( t ) , z ( t ) )$ and $( d z / d t ) ^ { 2 }$ is in the square root.

EXAMPLE 3 T?he points on a coil spring are $( x , y , z ) = ( \cos t , \sin t , t )$ . Find the mass of two complete turns (from $t = 0$ to $t = 4 \pi$ ) if the density is $\rho = 4$ .

Solution The key is $( d x / d t ) ^ { 2 } + ( d y / d t ) ^ { 2 } + ( d z / d t ) ^ { 2 } = \sin ^ { 2 } t + \cos ^ { 2 } t + 1 =$ 2.   
Thus $d s / d t = \sqrt { 2 }$ . To find the mass, integrate the mass per unit length which is $g = \rho = 4$ :

$$
\operatorname* { m a s s } = \int _ { 0 } ^ { 4 \pi } \rho { \frac { d s } { d t } } d t = \int _ { 0 } ^ { 4 \pi } 4 { \sqrt { 2 } } d t = 1 6 { \sqrt { 2 } } \pi .
$$

That is a line integral in three-dimensional space. It shows how to introduce $t$ . But it misses the main point of this section, because it contains no vector field $\mathbf { F }$ . This section is about work, not just mass.

# DIFFERENT FORMS OF THE WORK INTEGRAL

The work integral $\int \mathbf { F } \cdot \mathbf { T } d s$ can be written in a better way. The force is ${ \bf F } = M { \bf i } +$ $N { \bf j }$ . A small step along the curve is $d x \mathbf { i } + d y \mathbf { j }$ . Work is force times distance, but it is only the force component along the path that counts. The dot product $\mathbf { F } { \boldsymbol { \cdot } } \mathbf { T } d s$ finds that component automatically.

15C The vector to a point on $C$ is $\mathbf { R } = x \mathbf { i } + y \mathbf { j }$ . Then d R D T ds D dx i C dy j W

$$
w o r k = \int _ { c } \mathbf { F } \cdot d \mathbf { R } = \int _ { c } M d x + N d y .
$$

Along a space curve the work is $\begin{array} { r } { \int \mathbf { F } { \cdot } \mathbf { T } d s = \int \mathbf { F } { \cdot } d \mathbf { R } = \int M d x + N d y + P d z . } \end{array}$

The product $M d x$ is (force in $x$ direction)(movement in $x$ direction). This is zero if either factor is zero. When the only force is gravity, pushing a piano takes no work. It is friction that hurts. Carrying the piano up the stairs brings in $P d z$ , and the total work is the piano weight $P$ times the change in $z$ .

To connect the new $\int \mathbf { F } \cdot d \mathbf { R }$ with the old $\int \mathbf { F } \cdot \mathbf { T } d s$ , remember the tangent vector T. It is $d \mathbf { R } / d s$ . Therefore T ds is $d \mathbf { R }$ . The best for computations is $d \mathbf { R }$ , because the unit vector T has a division by $d s / d t = \sqrt { ( d x / d t ) ^ { 2 } + ( d y / d t ) ^ { 2 } }$ . Later we multiply by this square root, in converting $d s$ to $( d s / d t ) d t$ . It makes no sense to compute the square root, divide by it, and then multiply by it. That is avoided in the improved form $\int M d x + N d y$ .

EXAMPLE 4 Vector field $\mathbf { F } = - y \mathbf { i } + x \mathbf { j }$ , path from $( 1 , 0 )$ to $( 0 , 1 )$ : Find the work.

Note 1 This $\mathbf { F }$ is the spin field S. It goes around the origin, while $\mathbf { R } = x \mathbf { i } + y \mathbf { j }$ goes outward. Their dot product is $\mathbf { F } \cdot \mathbf { R } = - y x + x y = 0$ . This does not mean that $\mathbf { F } \cdot d \mathbf { R } = 0$ . The force is perpendicular to $\mathbf { R }$ , but not to the change in $\mathbf { R }$ . The work to move from $( 1 , 0 )$ to $( 0 , 1 )$ , $x$ axis to $y$ axis, is not zero.

Note 2 We have not described the path $C$ . That must be done. The spin field is not a gradient field, and the work along a straight line does not equal the work on a quarter-circle:

Calculation of work Change $\mathbf { F } \cdot d \mathbf { R } = M \ d x + N \ d y$ to the parameter $t$ :

$$
\therefore \int - y d x + x d y = \int _ { 0 } ^ { 1 } - t ( - d t ) + ( 1 - t ) d t = 1
$$

$$
\int - y d x + x d y = \int _ { 0 } ^ { \pi / 2 } - \sin t ( - \sin t d t ) + \cos t ( \cos t d t ) = { \frac { \pi } { 2 } } .
$$

General method The path is given by $x ( t )$ and $y ( t )$ . Substitute those into $M ( x , y )$ and $N ( x , y )$ —then $\mathbf { F }$ is a function of $t$ . Also find $d x / d t$ and $d y / d t$ . Integrate $M d x / d t + N d y / d t$ from the starting time $t$ to the finish.

For practice, take the path down the $x$ axis to the origin . $( x = 1 - t , y = 0 )$ /. Then go up the $y$ axis $( x = 0 , y = t - 1 )$ . The starting time at $( 1 , 0 )$ is $t = 0$ . The turning time at the origin is $t = 1$ . The finishing time at $( 0 , 1 )$ is $t = 2$ . The integral has two parts because this new path has two parts:

$$
\mathrm { e n t } \mathrm { p a t h } \colon \int - y d x + x d y = 0 + 0 ( y = 0 \mathrm { o n ~ o n e ~ p a r t , t h e n } x = 0 ) .
$$

Note 3 The answer depended on the path, for this spin field $\mathbf { F } = \mathbf { S } .$ . The answer did not depend on the choice of parameter. If we follow the same path at a different speed, the work is the same. We ca nchoo se another parameter $\tau$ , since $( d s / d t ) d t$ and $( d s / d \tau ) d \tau$ both equal $d s$ . Traveling twice as fast on the straight path $( x = 1 - 2 \tau$ ; $y = 2 \tau$ / we finish at $\begin{array} { r } { \tau = \frac { 1 } { 2 } } \end{array}$ instead of $t = 1$ . The work is still 1:

$$
\int - y d x + x d y = \int _ { 0 } ^ { 1 / 2 } ( - 2 \tau ) ( - 2 d \tau ) + ( 1 - 2 \tau ) ( 2 d \tau ) = \int _ { 0 } ^ { 1 / 2 } 2 d \tau = 1 .
$$

# C»ONSERVATION OF TOTAL ENERGY (KINETIC C POTENTIAL)

When a force field does work on a mass $m$ , it normally gives that mass a new velocity. Newton’s Law is $\mathbf { F } = m \mathbf { a } = m d \mathbf { v } / d t$ . (It is a vector law. Why write out three components?) The work $\int \mathbf { F } \cdot d \mathbf { R }$ is

$$
\int ( m d \mathbf { v } / d t ) \cdot ( \mathbf { v } d t ) = { \frac { 1 } { 2 } } m \mathbf { v } \cdot \mathbf { v } \mathbf { ] } _ { P } ^ { Q } = { \frac { 1 } { 2 } } m | \mathbf { v } ( Q ) | ^ { 2 } - { \frac { 1 } { 2 } } m | \mathbf { v } ( P ) | ^ { 2 } .
$$

The work equals the change in the kinetic energy $\begin{array} { r } { \frac { 1 } { 2 } m \left| \mathbf { v } \right| ^ { 2 } } \end{array}$ . But for a gradient field the work is also the change in potential—wit |h  a| minus sign from physics:

$$
w o r k = \int \mathbf { F } \cdot d \mathbf { R } = - \int d f = f ( P ) - f ( Q ) .
$$

Comparing .8/ with .9/, the combination $\scriptstyle { \frac { 1 } { 2 } } m \left| \mathbf { v } \right| ^ { 2 } + f$ is the same at $P$ and $\boldsymbol { Q }$ . The total energy, kinetic plus potential, is conserved.

# INDEPENDENCE OF PATH: GRADIENT FIELDS

The work of the spin field S depends on the path. Example 4 took three paths— straight line, quarter-circle, bent line. The work was 1, $\pi / 2$ , and 0, different on each path. This happens for more than $9 9 . 9 9 \%$ of all vector fields. It does not happen for the most important fields. Mathematics and physics concentrate on very special fields—for which the work depends only on the endpoints. We now explain what happens, when the integral is independent of the path.

Suppose you integrate from $P$ to $\boldsymbol { Q }$ on one path, and back to $P$ on another path. Combined,that is a closed path from $P$ to $P$ (Figure 15:7). But a backward integral is the negative of a forward integral, since $d \mathbf { R }$ switches sign. If the integrals from $P$ to $\boldsymbol { Q }$ are equal, the integral around the closed path is zero:

$$
\oint _ { P } ^ { P } \mathbf { F } \cdot d \mathbf { R } = \int _ { P } ^ { Q } \mathbf { F } \cdot d \mathbf { R } + \int _ { Q } ^ { P } \mathbf { F } \cdot d \mathbf { R } = \int _ { P } ^ { Q } \mathbf { F } \cdot d \mathbf { R } - \int _ { P } ^ { Q } \mathbf { F } \cdot d \mathbf { R } = 0 .
$$

closed path 1 back path 2 path 1 path 2

The circle on the first integral indicates a closed path. Later we will drop the $P ^ { \prime } s$ .

Not all closed path integrals are zero! For most fields F, different paths yield dwifofrek eanrtouwnodrka. Fclors“ecdonpsatehrvcaotinvse”rvfiees desn,earlglyp.aTthseybiiegldqtuhesstiaomneisw:orHko.wThteondzecriode which fields are conservative, without trying all paths? Here is the crucial information about conservative fields, in a plane region $R$ with no holes:

15D $\mathbf { F } = M ( x , y ) \mathbf { i } + N ( x , y ) \mathbf { j }$ is a conservative field if it has these properties:

A. The work $\int \mathbf { F } \cdot d \mathbf { R }$ around every closed path is zero.   
B. The work $\int _ { P } ^ { Q } \mathbf { F } \cdot d \mathbf { R }$ depends only on $P$ and $\boldsymbol { Q }$ , not on the path.   
C. F is a gradient field: $M =  { \partial } f /  { \partial } x$ and $N =  { \partial } f /  { \partial } y$ for some potential $f ( x , \mathbf { \boldsymbol { \mathbf { \mathit { y } } } } )$ .   
D. The components satisfy $\hat { \sigma } M / \partial y = \hat { \sigma } N / \partial x$ .   
A field with one of these properties has them all. $\mathbf { D }$ is the quick test.

These statements $\mathbf { A } - \mathbf { D }$ bring everything together for conservative fields (alias gradient fields). A closed path goes one way to $\boldsymbol { Q }$ and back the other way to $P$ . The work cancels, and statements $\mathbf { A }$ and $\mathbf { B }$ are equivalent. We now connect them to C. Note: Test $\mathbf { D }$ says that the “curl” of $\mathbf { F }$ is zero. That can wait for Green’s Theorem in the next section—the full discussion of the curl comes in 15:6.

First, $\pmb { a }$ gradient field $\mathbf { F } =$ grad $f$ is conservative. The work isB $f ( Q ) - f ( P )$ , by the fBund aBmental theorem for line integrals. It depends only on the endpoints and not the path. Therefore statement C leads back to B.

Our job is in the other direction, to show that conservative fields $M \mathbf { i } + N \mathbf { j }$ are gradients. Assume that the work integral depends only on the endpoints. We must construct a potential $f$ , so that $\mathbf { F }$ is its gradient. In other words, $\partial f / \partial x$ must be $M$ and $\partial f / \partial y$ must be $N$ .

# Fix the pointP:Define $f ( Q ) { \pmb { a s } }$ the work to reach $\boldsymbol { Q }$ :Then F equals grad $f .$ :

Check the reasoning. At the starting point $P , f$ is zero. At every other point $Q , f$ is the work $\int M d x + N d y$ to reach that point. All paths from $P$ to $\boldsymbol { Q }$ give the same $f ( Q )$ , because the field is assumed conservative. After two examples we prove that grad $f$ agrees with $\mathbf { F }$ —the construction succeeds.

$$
\begin{array} { r l } { \cdot \underbrace { \overbrace { \int _ { \vphantom { \int _ { \varepsilon } } \mathbf { f } \cdot d \mathbf { R } = 0 } ^ { \mathrm { b a c k } \mathrm { p a t h } 2 } } ^ { \mathrm { b a c k ~ p a t h } 2 } } _ { \mathrm { p a t h } 1 } \times \sum _ { \vphantom { \int _ { \varepsilon } } \varepsilon } ^ { \mathrm { F } } } & { { } \underbrace { f ( Q ) = \int _ { \vphantom { \int _ { \varepsilon } } \mathbf { F } \cdot d \mathbf { R } } ^ { Q } \mathrm { d } \mathbf { F } } _ { \mathrm { F } \cdot \underbrace { d \mathbf { R } \cdot F } _ { \mathrm { F } } } , } \end{array}
$$

EXA»MPLE 5 Find $f ( x , y )$ when $\mathbf { F } = M \mathbf { i } + N \mathbf { j } = 2 x y \mathbf { i } + x ^ { 2 } \mathbf { j }$ . We want $\partial f / \partial x = 2 x y$ and $\partial f / \partial y = x ^ { 2 }$ :

Solution 1 Choose $P = ( 0 , 0 )$ . Integrate $M d x + N d y$ along to $( x , 0 )$ and up to $( x , y )$ :

$$
\int _ { ( 0 , 0 ) } ^ { ( x , 0 ) } 2 x y d y = 0 \operatorname { ( s i n c e } y = 0 ) \qquad \int _ { ( x , 0 ) } ^ { ( x , y ) } x ^ { 2 } d y = x ^ { 2 } y ( { \mathrm { w h i c h i s ~ } } f ) .
$$

Certainly $f = x ^ { 2 } y$ meets the requirements: $f _ { x } = 2 x y$ and $f _ { y } = x ^ { 2 }$ . Thus $\mathbf { F } =$ grad $f$ . Note that $d y = 0$ in the first integral (on the $x$ axis). Then $d x = 0$ in the second integra»l ( $x$ is fixed). The integrals add to $f = x ^ { 2 } y$ .

Solution 2 Integrate $2 x y d x + x ^ { 2 } d y$ on the straight line $( x t , y t )$ from $t = 0$ to $t = 1$ :

$$
\int _ { 0 } ^ { 1 } 2 ( x t ) ( y t ) ( x d t ) + ( x t ) ^ { 2 } ( y d t ) = \int _ { 0 } ^ { 1 } 3 x ^ { 2 } y t ^ { 2 } d t = x ^ { 2 } y t ^ { 3 } ] _ { 0 } ^ { 1 } = x ^ { 2 } y .
$$

Most authors use Solution 1. I use Solution 2. Most students use Solution 3:

Solution 3 Directly solve $\partial f / \partial x = M = 2 x y$ and then fix up $d f / d y = N = x ^ { 2 }$ :

$$
\partial f / \partial x = 2 x y \quad { \mathrm { g i v e s } } \quad f = x ^ { 2 } y ( p l u s a n y f u n c t i o n \ o f y ) .
$$

In this example $x ^ { 2 } y$ already has the correct derivative $\partial f / \partial y = x ^ { 2 }$ . No additional function of $y$ is necessary. When we integrate with respect to $x$ ,the constant of integration (usually $C$ ) becomes a function $C ( y )$ .

You will get practice in finding $f$ . This is only possible for conservative fields! I tested $M = 2 x y$ and $N = x ^ { 2 }$ in advan»ce (using D) to be sure that $\hat { \sigma } M / \partial y = \hat { \sigma } N / \partial x$ .

EXAMPLE 6 Look for $f ( x , y )$ when $M \mathbf { i } + N \mathbf { j }$ is the spin field $- y \mathbf { i } + x \mathbf { j }$ .

Attempted solution 1 Integrate $- y d x + x d y$ from $( 0 , 0 )$ to $( x , 0 )$ to $( x , y )$ :

$$
\int _ { ( 0 , 0 ) } ^ { ( x , 0 ) } - y d x = 0 \quad { \mathrm { a n d } } \quad \quad \int _ { ( x , 0 ) } ^ { ( x , y ) } x d y = x y { \mathrm { ~ ( w h i c h ~ s e e m s ~ l i k e ~ } } f { \mathrm { ) } } .
$$

Attempted solution 2 Integrate $- y d x + x d y$ on the line $( x t , y t )$ frBom $t = 0$ to 1:

$$
\int _ { 0 } ^ { 1 } - ( y t ) ( x d t ) + ( x t ) ( y d t ) = 0 ( { \mathrm { a } } \operatorname { d i f f e r e n t } f , { \mathrm { a l s o } } { \mathrm { w r o n g } } ) .
$$

BAtte Bmpted solution 3 Directly solve $\partial f / \partial x = - y$ and try to fix up $\partial f / \partial y = x$ :

$$
\partial f / \partial x = - y \quad { \mathrm { g i v e s ~ } } f = - x y
$$

The $y$ derivative of this $f$ is $- x + d C / d y$ . That does not agree with the required $\partial f / \partial y = x$ . Conclusion: The spin field $- y \mathbf { i } + x \mathbf { j }$ is not conservative. There is no $f$ . Test $\mathbf { D }$ gives $\partial M / \partial y = - 1$ and $\partial N / \partial x = + 1$ .

To finish this section, we move from examples to a proof. The potential $f ( Q )$ is defined as the work to reach $\boldsymbol { Q }$ . We must show that its partial derivatives are $M$ and $N$ .BTh iBs seems reasonable from the formula $\textstyle f ( Q ) = { \bar { \int } } M d x + N d y$ , but we have to think it througBh.

Remember statement $\mathbf { A }$ , that all paths give the same $f ( Q )$ . Take a path that goes from $P$ toB the Bleft of $\boldsymbol { Q }$ . It comes in to $\boldsymbol { Q }$ on a line $y =$ constant (so $d y = 0$ ). As the path reaches $\boldsymbol { Q }$ , we are only integrating $M d x$ . The derivative of this integral, at $\boldsymbol { Q }$ , is $\partial f / \partial x = M$ . That is the Fundamental Theorem of Calculus.

To show that $\partial f / \partial y = N$ , take a different path. Go from $P$ to a point below $\boldsymbol { Q }$ . The path comes up to $\boldsymbol { Q }$ on a vertical line (so $d x = 0$ ). Near $\boldsymbol { Q }$ we are only integrating $N d y$ , so $\partial f / \partial y = N$ .

The requirement that the region must have no holes will be critical for test D.

# 15.2 Line Integrals

EXAMPLE 7 Find f .x; y/ D r .0x;0/ x dx C y dy: Test D is passed: N= x D 0 D $\partial M / \partial y$ :

Solution 1 $\textstyle \int _ { ( 0 , 0 ) } ^ { ( x , 0 ) } x d x = { \frac { 1 } { 2 } } x ^ { 2 }$ is added to r .0x;0/ y dy D 21 y2.

Solution 2 $\begin{array} { r } { \int _ { 0 } ^ { 1 } ( x t ) ( x d t ) + ( y t ) ( y d t ) = \int _ { 0 } ^ { 1 } ( x ^ { 2 } + y ^ { 2 } ) t d t = \frac { 1 } { 2 } ( x ^ { 2 } + y ^ { 2 } ) . } \end{array}$

Solution 3 $\partial f / \partial x = x$ gives $\begin{array} { r } { f = \frac { 1 } { 2 } x ^ { 2 } + C ( y ) } \end{array}$ . Then $\partial f / \partial y = y$ needs $C ( y ) =$ ${ \scriptstyle { \frac { 1 } { 2 } } } y ^ { 2 }$ .