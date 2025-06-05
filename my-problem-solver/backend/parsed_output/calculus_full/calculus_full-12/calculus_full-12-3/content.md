# 12.3 Curvature and Normal Vector

A driver produces acceleration three ways—by the gas pedal, the brake, and steering wheel. The first two change the speed |.  T|urning the wheel changes the direction. $A l l$ three change the veloc|it |y (they give acceleration). For steady motion around a circle, the change is from steering—the acceleration $d { \bf v } / d t$ points to the center. We now look at motion along other curves, to separate change in the speed $| \mathbf { v } |$ from change in the direction $\mathbf { T }$ :

The direction of motion is $\mathbf { T } = \mathbf { v } / | \mathbf { v } |$ : It depends on the path but not the speed (because we divide by $| \mathbf { v } | )$ . For turning we measure two things:

1. How fast T turns: this will be the curvature $\kappa$ (kappa).   
2. Which direction T turns: this will be the normal vector N.

$\kappa$ and $\mathbf { N }$ depend, like $s$ and $\mathbf { T }$ , only on the shape of the curve. Replacing $t$ by $2 t$ or $t ^ { 2 }$ leaves them unchanged. For a circle we give the answers in advance. The normal vector $\mathbf { N }$ points to the center. The curvature $\kappa$ is 1=radius.

A smaller turning circle means a larger curvature $\kappa$ : more bending.

The curvature $\kappa$ is change i|n directi|on $| d \mathbf { T } |$ divided by cha|ngein | p |o s|ition $| d s |$ : There are three formulas for $\kappa$ —a direct one for graphs $y ( x )$ , a brutal but valuable one for any parametric curve $( x ( t ) , y ( t ) )$ ; and a neat formula that uses the vectors $\mathbf { v }$ and a: We begin with the definition and the neat formula.

$$
\begin{array} { r } { \kappa = | d \mathbf { T } / d s | \qquad { \mathsf { F O R M U L A } } \quad \kappa = | \mathbf { v } \times \mathbf { a } | / | \mathbf { v } | ^ { 3 } } \end{array}
$$

The definition does not involve the parameter $t$ —but the calculations do. The position vector $\mathbf { R } ( t )$ yields $\mathbf { v } = d \mathbf { R } / d t$ and $\mathbf { a } = d \mathbf { v } / d t$ : If $t$ is changed to $2 t$ , the velocity $\mathbf { v }$ is doubled and a is multi|pl |ied by 4: Then $| \mathbf { v } \times \mathbf { a } |$ and $\mathbf { \left| v \right| } ^ { 3 }$ are multiplied by 8, and their ratio $\kappa$ is unchanged.

Proof of formula (1) Start from $\mathbf { v } = | \mathbf { v } | \mathbf { T }$ and compute its derivative a:

$$
\mathbf { a } = { \frac { d | \mathbf { v } | } { d t } } \mathbf { T } + | \mathbf { v } | { \frac { d \mathbf { T } } { d t } } { \mathrm { ~ b y ~ t h e ~ p r o d u c t ~ r u l e . } }
$$

Now take the cross product with $\mathbf { v } = | \mathbf { v } | \mathbf { T }$ : Remember that $\mathbf { T } \times \mathbf { T } = \mathbf { 0 }$ :

$$
\mathbf { v } \times \mathbf { a } = | \mathbf { v } | \mathbf { T } \times | \mathbf { v } | { \frac { d \mathbf { T } } { d t } } .
$$

We know that $\left. \mathbf { T } \right. = 1$ : |E q|uation (4) will show that $\mathbf { T }$ is perpendi|cu |lar to $d { \bf T } / d t$ : So $| \mathbf { v } \times \mathbf { a } |$ is the first length $| \mathbf { v } |$ times the second length $\lvert \mathbf { v } \rvert \lvert d \mathbf { T } / d t \rvert$ : The factor sin $\theta$ in the length of a cross product is |1 from t|he $9 0 ^ { \circ }$ angle. In other words

$$
\left| { \frac { d \mathbf { T } } { d t } } \right| = { \frac { | \mathbf { v } \times \mathbf { a } | } { | \mathbf { v } | ^ { 2 } } } \quad { \mathrm { a n d } } \quad \kappa = \left| { \frac { d \mathbf { T } } { d s } } \right| = \left| { \frac { d \mathbf { T } / d t } { d s / d t } } \right| = { \frac { | \mathbf { v } \times \mathbf { a } | } { | \mathbf { v } | ^ { 3 } } } .
$$

The chain rule brings the extra $| d s / d t | = | \mathbf { v } |$ into the denominator.

Before any examples, we show that $d { \bf T } / d t$ is pe1rpendicular to $\mathbf { T }$ : The reason is that $\mathbf { T }$ is a unit vector. Differentiate both sides of $\mathbf { T } \cdot \mathbf { T } = 1$ :

$$
{ \frac { d \mathbf { T } } { d t } } \cdot \mathbf { T } + \mathbf { T } \cdot { \frac { d \mathbf { T } } { d t } } = 0 \qquad o r \qquad 2 \mathbf { T } \cdot { \frac { d \mathbf { T } } { d t } } = 0 .
$$

That proof used the product rule $\mathbf { U } ^ { \prime } \cdot \mathbf { V } + \mathbf { U } \cdot \mathbf { V } ^ { \prime }$ for the derivative of $\mathbf { U } \cdot \mathbf { V }$ (Problem 23, with $\mathbf { U } = \mathbf { V } = \mathbf { T }$ ). Think of the vector $\mathbf { T }$ moving around the unit sphere.

To keep a constant length $( \mathbf { T } + d \mathbf { T } ) \cdot ( \mathbf { T } + d \mathbf { T } ) = 1$ , we need $2 \mathbf { T } \cdot d \mathbf { T } = 0$ : Movement $d \mathbf { T }$ is perpendicular to radius vector $\mathbf { T }$ :

Our first ex1amples 1will be plane curves. The position v1ector $\mathbf { R } ( t )$ has components $x ( t )$ and $y ( t )$ but no $z ( t )$ : Look at the components of $\mathbf { v }$ and a and $\mathbf { v } \times \mathbf { a }$ ( $x ^ { \prime }$ means $d x / d t )$ :

$$
\begin{array} { c c c c c } { { \mathrm { \bf ~ R } } } & { { x ( t ) } } & { { y ( t ) } } & { { 0 } } & { { \nonumber } } \\ { { \mathrm { \bf ~ v } } } & { { x ^ { \prime } ( t ) } } & { { y ^ { \prime } ( t ) } } & { { 0 } } & { { | \mathrm { \bf ~ v } | = \sqrt { | x ^ { \prime } | ^ { 2 } + | y ^ { \prime } | ^ { 2 } } \nonumber } } \\ { { \mathrm { \bf ~ a } } } & { { x ^ { \prime \prime } ( t ) } } & { { y ^ { \prime \prime } ( t ) } } & { { 0 } } & { { \nonumber } } \\ { { \mathrm { \bf ~ v } \times \mathrm { \bf ~ a } } } & { { 0 } } & { { 0 } } & { { x ^ { \prime } y ^ { \prime \prime } - y ^ { \prime } y ^ { \prime \prime } } } & { { \kappa = \displaystyle \frac { | x ^ { \prime } y ^ { \prime \prime } - y ^ { \prime } x ^ { \prime \prime } | } { ( ( x ^ { \prime } ) ^ { 2 } + ( y ^ { \prime } ) ^ { 2 } ) ^ { 3 / 2 } } } } \end{array}
$$

Equation (5) is the brutal but valuable formula for $\kappa$ : Apply it to movement around a circle. We should find $\kappa = 1 / { \mathrm { r a d i u s } } a$ :

EXAMPLE 1 When $x = a$ cos $\omega t$ and $y = a$ sin !t we substitute $x ^ { \prime } , y ^ { \prime } , x ^ { \prime \prime } , y ^ { \prime \prime }$ into (5):

$$
\kappa = { \frac { ( - \omega a \sin \omega t ) ( - \omega ^ { 2 } a \sin \omega t ) - ( \omega a \cos \omega t ) ( - \omega ^ { 2 } a \cos \omega t ) } { [ ( \omega a \sin \omega t ) ^ { 2 } + ( \omega a \cos \omega t ) ^ { 2 } ] ^ { 3 / 2 } } } = { \frac { \omega ^ { 2 } a ^ { 2 } } { [ \omega ^ { 2 } a ^ { 2 } ] ^ { 3 / 2 } } } .
$$

This is $\omega ^ { 3 } a ^ { 2 } / \omega ^ { 3 } a ^ { 3 }$ and $\omega$ cancels. The speed makesano difference to $\kappa = 1 / a$ :

The third formula for $\kappa$ applies to an ordinary plane curve given by $y ( x )$ : The parameter $t$ is $x$ ! You see the square root in the speed $| \mathbf { v } | = d s / d x$ :

$$
{ \begin{array} { l l l l l l } { \mathbf { R } } & { x } & { y ( x ) } & { 0 } & { } & { } \\ { \mathbf { v } } & { 1 } & { d y / d x } & { 0 } & { } & { | \mathbf { v } | = { \sqrt { 1 + ( d y / d x ) ^ { 2 } } } } \\ { \mathbf { a } } & { 0 } & { d ^ { 2 } y / d x ^ { 2 } } & { 0 } & { } & { } \\ { \mathbf { v } \times \mathbf { a } } & { 0 } & { 0 } & { d ^ { 2 } y / d x ^ { 2 } } & { } & { \kappa = { \frac { | d ^ { 2 } y / d x ^ { 2 } | } { ( 1 + ( d y / d x ) ^ { 2 } ) ^ { 3 / 2 } } } } \end{array} }
$$

In practice this is the most popular formula for $\kappa$ :|Th|e most popular approximation is $| d ^ { \bar { 2 } } y / d x ^ { 2 } |$ : (The denominator is omitted.) For the bending of a beam, the nonlinear equation uses $\kappa$ and the linear equation uses $d ^ { 2 } y / d x ^ { 2 }$ :We can see the difference for a parabola:

EXAMPLE 2 The curvature of $\scriptstyle y = { \frac { 1 } { 2 } } x ^ { 2 }$ is $\kappa = | y ^ { \prime \prime } | / ( 1 + ( y ^ { \prime } ) ^ { 2 } ) ^ { 3 / 2 } = 1 / ( 1 + x ^ { 2 } ) ^ { 3 / 2 } .$

The approximation is $y ^ { \prime \prime } { = } 1$ : This agrees with $\kappa$ at $x = 0$ , where the parabola turns the corner. But for large $x$ , the curvature approaches zero. Far out on the parabola, we go a long way for a small change in direction.

The parabola $\scriptstyle y = - { \frac { 1 } { 2 } } x ^ { 2 }$ , opening down, has the same $\kappa$ : Now try a space curve.

EXAMPLE 3 Find the curvature of the unit helix $\mathbf { R } = \cos t \mathbf { i } + \sin t \mathbf { j } + t \mathbf { k }$ :

Take the cross product of $\mathbf { v } = - \sin t \mathbf { i } + \cos t \mathbf { j } + \mathbf { k }$ and $\mathbf { a } = - \cos t \mathbf { i } - \sin t ; $ j:

$$
\mathbf { v } \times \mathbf { a } = { \left| \begin{array} { l l l } { \mathbf { i } } & { \mathbf { j } } & { \mathbf { k } } \\ { - \sin t } & { \cos t } & { 1 } \\ { - \cos t } & { - \sin t } & { 0 } \end{array} \right| } = \sin t \mathbf { i } - \cos t \mathbf { j } + \mathbf { k } .
$$

This cross product has length $\sqrt { 2 }$ : Also the speed is $| \mathbf { v } | = { \sqrt { \sin ^ { 2 } t + \cos ^ { 2 } t + 1 } } =$ $\sqrt { 2 }$ W

$$
\begin{array} { r } { \kappa = | \mathbf { v } \times \mathbf { a } | / | \mathbf { v } | ^ { 3 } = \sqrt { 2 } / ( \sqrt { 2 } ) ^ { 3 } = \frac { 1 } { 2 } . } \end{array}
$$

Compare with a unit circle. Without the climbing term $t \mathbf { k }$ , the curvature would be 1: Because of climbing, each turn of the helix is longer and $\begin{array} { r } { \kappa = \frac { 1 } { 2 } } \end{array}$ :

That makes one think: Is the helix twice as long as the circle $? ~ \mathrm { N o }$ . The length of a turn is only increased by $| \mathbf { v } | = { \sqrt { 2 } }$ : The other $\bar { \sqrt { 2 } }$ is because the tangent $\mathbf { T }$ slopes upward. The shadow in the base turns a full $3 6 0 ^ { \circ }$ , but $\mathbf { T }$ turns less.

# THE NORMAL VECTOR N

The discussion is bringing us to an important vector. Where $\kappa$ measures the rate of turning, the unit vector $\mathbf { N }$ gives the direction of turning. $\mathbf { N }$ is perpendicular to $\mathbf { T }$ , and in the plane that leaves practically no choice. Turn left or right. For a space curve, follow $d \mathbf { T }$ : Remember e|quation (|4), which makes $d \mathbf { T }$ perpendicular|to $\mathbf { T }$ :

The normal vector N is a unit vector along $d \mathbf { T } / d t . \mathbf { \nabla } _ { I t }$ is perpendicular to T:

$$
\mathbf { N } = { \frac { d \mathbf { T } / d s } { | d \mathbf { T } / d s | } } = { \frac { 1 } { \kappa } } { \frac { d \mathbf { T } } { d s } } \qquad { \mathsf { F O R M U L A } } \quad \mathbf { N } = { \frac { d \mathbf { T } / d t } { | d \mathbf { T } / d t | } } .
$$

EXAM P|L |E 4 Find the normal vector $\mathbf { N }$ for the same helix $\mathbf { R } = \cos t \mathbf { i } + \sin t \mathbf { j } +$ $t \mathbf { k }$ :

Solution Copy v from Example 3, divide by $| \mathbf { v } |$ , and compute $d { \bf T } / d t$ :

$$
\mathbf { T } = \mathbf { v } / | \mathbf { v } | = ( - \sin t \mathbf { i } + \cos t \mathbf { j } + \mathbf { k } ) / \sqrt { 2 } \quad \mathrm { a n d } \quad d \mathbf { T } / d t = ( - \cos t \mathbf { i } - \sin t \mathbf { j } ) / \sqrt { 2 } .
$$

To change $d { \bf T } / d t$ into a unit vector, cancel the $\sqrt { 2 }$ : The normal vector is $\mathbf { N } =$ $- \cos t { \bf i } - \sin t { \bf j }$ : It is perpendicularto $\mathbf { T }$ : Since the $\mathbf { k }$ component is zero, $\mathbf { N }$ is horizontal. The tangent $\mathbf { T }$ slopes up at $4 5 ^ { \circ }$ —it goes around the circle at that latitude. The normal $\mathbf { N }$ is tangent to this circle $\mathbf { N }$ is tangent to the path of the tangent!). So $\mathbf { N }$ stays horizontal as the helix climbs.

There is also a third direction, perpendicular to $\mathbf { T }$ and $\mathbf { N }$ : It is the binormal vector $\mathbf B = \mathbf T \times \mathbf N$ , computed in Problems $2 5 - 3 0$ : The unit vectors $\mathbf { T } , \mathbf { N } , \mathbf { B }$ provide the natural coordinate system for the path—along the curve, in the plane of the curve, and out of that plane. The theory is beautiful but the computations are not often done—we stop here.

# TANGENTIAL AND NORMAL COMPONENTS OF ACCELERATION

May I return a last time to the gas pedal and brake and steering wheel ? The first two give acceleration along T: Turning gives acceleration along $\mathbf { N }$ : The rate of turning (curvature $\kappa$ ) and the direction $\mathbf { N }$ are established. We now ask about the force

# 12 Motion along a Curve

required. Newton’s Law is $\mathbf { F } = m \mathbf { a }$ , so we need the acceleration a—especially its component along $\mathbf { T }$ and its component along $\mathbf { N }$ :

$$
T h e \ a c c e l e r a t i o n \ i s \ \mathbf { a } = \frac { d ^ { 2 } s } { d t ^ { 2 } } \mathbf { T } + \kappa \biggl [ \frac { d s } { d t } \biggr ] ^ { 2 } \mathbf { N } .
$$

For a straight path, $d ^ { 2 } s / d t ^ { 2 }$ is the only acceleration—the ordinary second derivative. The term $\kappa ( d s / d t ) ^ { 2 }$ is the acceleration in turning. Both have the dimension of length=(time)2:

The force to steer around a corner depends on curvature and speed—as all drivers know. Acceleration is the derivative of $\mathbf { v } = | \mathbf { v } | \mathbf { T } = ( d s / d t ) \mathbf { T }$ :

$$
\mathbf { a } = { \frac { d ^ { 2 } s } { d t ^ { 2 } } } \mathbf { T } + { \frac { d s } { d t } } { \frac { d \mathbf { T } } { d t } } = { \frac { d ^ { 2 } s } { d t ^ { 2 } } } \mathbf { T } + { \frac { d s } { d t } } { \frac { d \mathbf { T } } { d s } } { \frac { d s } { d t } } .
$$

That last term is $\kappa ( d s / d t ) ^ { 2 } \mathbf { N } .$ , since $d \mathbf { T } / d s = \kappa \mathbf { N }$ by formula (7). So (8) is proved.

EXAMPLE 5 A fixed speed $d s / d t = 1$ gives $d ^ { 2 } s / d t ^ { 2 } = 0$ : The only acceleration is $\kappa \mathbf { N }$ :

EXAMPLE 6 Find the components of a for circular speed-up $\mathbf { R } ( t ) = \cos t ^ { 2 } \mathbf { i } + \sin t ^ { 2 } \mathbf { j }$ :

Without stopping to think, compute $d \mathbf { R } / d t = \mathbf { v }$ and $d s / d t = | \mathbf { v } |$ and $\mathbf { v } / | \mathbf { v } | = \mathbf { T }$ :

$$
\mathbf { v } = - 2 t \sin t ^ { 2 } \mathbf { i } + 2 t \cos t ^ { 2 } \mathbf { j } , | \mathbf { v } | = 2 t , \mathbf { T } = - \sin t ^ { 2 } \mathbf { i } + \cos t ^ { 2 } \mathbf { j } .
$$

The derivative of $d s / d t = | \mathbf { v } |$ is $d ^ { 2 } s / d t ^ { 2 } = 2$ : The derivative of $\mathbf { v }$ is a:

$$
\mathbf { a } = - 2 \sin t ^ { 2 } \mathbf { i } + 2 \cos t ^ { 2 } \mathbf { j } - 4 t ^ { 2 } \cos t ^ { 2 } \mathbf { i } - 4 t ^ { 2 } \sin t ^ { 2 } \mathbf { j } .
$$

In the first terms of a we see 2T: In the last terms we must be seeing $\kappa | \mathbf { v } | ^ { 2 } \mathbf { N }$ : Certainly $\lvert \mathbf { v } \rvert ^ { 2 } = 4 t ^ { 2 }$ and $\kappa = 1$ , because the circle has radius 1: Thus $\mathbf { a } = 2 \mathbf { T } + 4 t ^ { 2 } \mathbf { N }$ has the tangential component 2 and normal component $4 t ^ { 2 }$ —acceleration along the circle and in to the center.

Table of Form|ulas