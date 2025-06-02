# 13.4 Directional Derivatives and Gradients

As $x$ changes, we know how $f ( x , y )$ changes. The partial derivative $\partial f / \partial x$ treats $y$ as constant. Similarly $\partial f / \partial y$ keeps $x$ constant, and gives the slope in the $y$ direction. But east-west and north-south are not the only directions to move. We could go along a $4 5 ^ { \circ }$ line, where $\Delta x = \Delta y$ . In principle, before we draw axes, no direction is preferred. The graph is a surface with slopes in all directions.

On that surface, calculus looks for the rate of change (or the slope). There is a dBire cBtional Bderi vBative, whatever the direction. In the $4 5 ^ { \circ }$ case we are inclined to divide $\Delta f$ by $\Delta x$ , but we would be wrong. Let me state the problem. We are given $f ( x , y )$ around a point $P = ( x _ { 0 } , y _ { 0 } )$ . We are also given a direction u (a unit vector). There must be a natural definition of $D _ { u } f$ —the derivative of $f$ in the direction u: To compute this slope at $P$ ; we need a formula. Preferably the formula is based on $\partial f / \partial x$ and $\partial f / \partial y$ ; which we already know.

Note that the $4 5 ^ { \circ }$ direction has $\mathbf { u } = \mathbf { i } / 2 + \mathbf { j } / 2$ . The square root of 2 is going to enter the derivative. This shows that dividing $\Delta f$ by $\Delta x$ is wrong. We should divide by the step length $\Delta s$ .

EXAMPLE 1 Stay on the surface $z = x y$ . When $( x , y )$ moves a distance $\Delta s$ in the $4 5 ^ { \circ }$ direction fr?om $( 1 , 1 )$ , w?hat is $\Delta z / \Delta s ?$

Solution The step is $\Delta s$ tim?es the unit vector u. Starting from $x = y = 1$ the step ends at $x = y = 1 + \Delta s / \sqrt { 2 }$ . (The components of $\mathbf { u } \Delta s$ are $\Delta s / { \sqrt { 2 } } .$ / Then $z = x y$ is

$$
z = ( 1 + \Delta s / \sqrt { 2 } ) ^ { 2 } = 1 + \sqrt { 2 } \Delta s + \textstyle { \frac { 1 } { 2 } } ( \Delta s ) ^ { 2 } , \mathrm { w h i c h } \mathrm { m e a n s } \Delta z = \sqrt { 2 } \Delta s + \textstyle { \frac { 1 } { 2 } } ( \Delta s ) ^ { 2 }
$$

The ratio $\Delta z / \Delta s$ approaches $\sqrt { 2 }$ as $\Delta s \to 0$ : That is the slope in the $4 5 ^ { \circ }$ direction.

DEFINITION The derivative of $f$ in the direction u at the point $P$ is $D _ { \mathbf { u } } f ( P )$ :

$$
D _ { \mathbf { u } } f ( P ) = \operatorname* { l i m } _ { \Delta s \to 0 } { \frac { \Delta f } { \Delta s } } = \operatorname* { l i m } _ { \Delta s \to 0 } { \frac { f ( P + \mathbf { u } \Delta s ) - f ( P ) } { \Delta s } } .
$$

The step from $P = ( x _ { 0 } , y _ { 0 } )$ has length $\Delta s$ . It takes us to $( x _ { 0 } + u _ { 1 } \Delta s , y _ { 0 } + u _ { 2 } \Delta s )$ . We compute the chBang eB $\Delta f$ and divide by $\Delta s$ . But formula (2) below saves time. The $x$ direction is ${ \bf u } = ( 1 , 0 )$ : Then $\mathbf { u } \Delta s$ is $( \Delta s , 0 )$ andweB rec Bover $\partial f / \partial x$ :

$$
\frac { \Delta f } { \Delta s } = \frac { f ( x _ { 0 } + \Delta s , y _ { 0 } ) - f ( x _ { 0 } , y _ { 0 } ) } { \Delta s } \mathrm { ~ a p p r o a c h e s ~ } D _ { ( 1 , 0 ) } f = \frac { \partial f } { \partial x } .
$$

Similarly $D _ { \mathbf { u } } f = \partial f / \partial y$ ; when $\mathbf { u } = ( 0 , 1 )$ is in the $y$ direction. What is $D _ { \mathbf { u } } f$ when $\mathbf { u } = ( 0 , - 1 ) \ ?$ BThat is tBhe n eBgative $y$ direction, so $D _ { \mathbf { u } } f = - \partial f / \partial y$ .

# CALCULATING THE DIRECTIONAL DERIVATIVE

$D _ { \mathbf { u } } f$ is the slope of the surface $z = f ( x , y )$ in the direction $\mathbf { u }$ . How do you compute it? From $\partial f / \partial x$ and $\partial f / \partial y$ ; in two special directions, there is a quick way to find $D _ { \mathbf { u } } f$ in all directions. Remember that $\mathbf { u }$ is a unit vector.

13E The directional derivative $D _ { \mathbf { u } } f$ in the direction $\mathbf { u } = ( u _ { 1 } , u _ { 2 } )$ equals $D _ { \mathbf { u } } f = \frac { \partial f } { \partial x } u _ { 1 } + \frac { \partial f } { \partial y } u _ { 2 } .$

The reasoning goes back to the linear approximation of $\Delta f$ :

$$
\Delta f \approx \frac { \partial f } { \partial x } \Delta x + \frac { \partial f } { \partial y } \Delta y = \frac { \partial f } { \partial x } u _ { 1 } \Delta s + \frac { \partial f } { \partial y } u _ { 2 } \Delta s .
$$

Divide by $\Delta s$ and let $\Delta s$ approach zero. Formula (2) is the limit of $\Delta f / \Delta s$ ; as the approximation becomes exact. A more careful argument guarantees this limit provided $f _ { x }$ and $f _ { y }$ are continuous at the basepoint $( x _ { 0 } , y _ { 0 } )$ :

Main point: Slopes in all directions are known from slopes in two directions.

EXAMPLE 1 (repeated) $f = x y$ and $P = ( 1 , 1 )$ and $\mathbf { u } = ( 1 / \sqrt { 2 } , 1 / \sqrt { 2 } )$ : Find $D _ { \mathbf { u } } f ( P )$ :

The derivatives $f _ { x } = y$ and $f _ { y } = x$ equal 1 at $P$ . The $4 5 ^ { \circ }$ der Bivative is

$$
D _ { \mathbf { u } } f ( P ) = f _ { x } u _ { 1 } + f _ { y } u _ { 2 } = 1 ( 1 / \sqrt { 2 } ) + 1 ( 1 / \sqrt { 2 } ) = \sqrt { 2 }
$$

EXAMPLE 2 The linear function $f = 3 x + y + 1$ has slope $D _ { \mathbf { u } } f = 3 u _ { 1 } + u _ { 2 }$ .

The $x$ direction is $u = ( 1 , 0 )$ ; and $D _ { \mathbf { u } } f = 3$ : That is $\partial f / \partial x$ : In the $y$ direction $D _ { \mathbf { u } } f = 1$ : Two other directions are special—along the level lines of $f ( x , y )$ and perpendicular:

Level direction: $D _ { \mathbf { u } } f$ is zero because $f$ is constant Steepest direction: $D _ { \mathbf { u } } f$ is as large as possible .with $u _ { 1 } ^ { 2 } + u _ { 2 } ^ { 2 } = 1 \qquad $ /:

To find those directions, look at $D _ { \mathbf { u } } f = 3 u _ { 1 } + u _ { 2 }$ : The level direction has $3 u _ { 1 } +$ $u _ { 2 } = 0$ : Then $u$ is proportional to $( 1 , - 3 )$ : Changing $x$ by 1 and $y$ by $^ { - 3 }$ produces no change in $f = 3 x + y + 1$ :

In the steepest direction $\mathbf { u }$ is proportion?al to $( 3 , 1 )$ : Note the partial deriva?tives $f _ { x } = 3$ and $f _ { y } = 1$ : The dot product of $( 3 , 1 )$ and $( 1 , - 3 )$ is zero—steepest direction is perpendicular to level direction. To make $( 3 , 1 )$ a unit vector, divide by $\sqrt { 1 0 }$ :

Steepest climb: $\begin{array} { r l } & { D _ { \mathbf { u } } f = 3 ( 3 / \sqrt { 1 0 } ) + 1 ( 1 / \sqrt { 1 0 } ) = 1 0 / \sqrt { 1 0 } = \sqrt { 1 0 } } \\ & { \mathrm { R e v e r s e ~ t o ~ } \mathbf { u } = ( - 3 / \sqrt { 1 0 } , - 1 / \sqrt { 1 0 } ) \quad \mathrm { a n d } \quad D _ { \mathbf { u } } f = - \sqrt { 1 0 } . } \end{array}$ Steepest descent:

The contour lines around a mountain follow $D _ { \mathbf { u } } f = 0$ . The creeks are perpendicular. On a plane like $f = 3 x + y + 1$ ; those directions stay the same at all points (Figure 13.12). On a mountain the steepest direction changes as the slopes change.

# THE GRADIENT VECTOR

Look again at $f _ { x } u _ { 1 } + f _ { y } u _ { 2 }$ ; which is the directional derivative $D _ { \mathbf { u } } f .$ This iBs the dotB product of two vectors. One vector is $\mathbf { u } = ( u _ { 1 } , u _ { 2 } )$ ; which sets the directBion. The other vector is $( f _ { x } , f _ { y } )$ ; wBhich coBmes from theBfunction. This second vector is the gradient.

DEFINI $\begin{array} { l } { { \displaystyle { \sf T } \mathsf { I O N \quad T h e } g r a d i e n t \mathrm { o f } f ( x , y ) \mathrm { i s t h e v e c t o r w h o s e c o m p o n e n t s a r e } \frac { \partial f } { \partial x } } } \\ { { \displaystyle \mathrm { g r a d ~ } f = \nabla f = \frac { \partial f } { \partial x } { \bf i } + \frac { \partial f } { \partial y } { \bf j } \quad \left( \mathrm { a d d } \frac { \partial f } { \partial z } { \bf k } \mathrm { i n \ t h r e e } \mathrm { d i m e n s i o n s } \right) . } } \end{array}$ and $\frac { \partial f } { \partial y }$

The space-saving symbol $\nabla$ is read as “grad.” In Chapter 15 it becomes “del.”

For the linear function $3 x + y + 1$ ; the gradient is the constant vector .3; 1/: It is the way to climb the plane. For the nonlinear function $x ^ { 2 } + x y$ ; the gradient is the non-constant vector $( 2 x + y , x )$ : Notice that grad $f$ shares the two derivatives in $\mathbf { N } = ( f _ { x } , f _ { y } , - 1 )$ : But the gradient is not the normal vector. $\mathbf { N }$ is in three dimensions, pointing away from the surface $z = f ( x , y )$ : The|gradien|t vector is in the $x y$ plane! The gradient tells which way on the surface is up, but it does that from down in the base.

The level curve is also in the $x y$ plane, perpendicularto the gradient. The contour map is a projection on the base plane of what the hiker sees on thebmountain. The vector grad $f$ tells the direction of climb, and its length |grad $f |$ gives the steepness.

13F The directional derivative is $D _ { \mathbf { u } } f = ( \mathrm { g r a d \ } f ) \cdot \mathbf { u }$ : The level directio|n is perpendicular|to grad $f ,$ since $D _ { \mathbf { u } } f = 0$ : The slope $D _ { \mathbf { u } } f$ is la|rgest when u is parallel to grad $f .$ : That maximum slope is the length grad $f | = \sqrt { f _ { x } ^ { 2 } + f _ { y } ^ { 2 } }$ : for $\mathbf { u } = { \frac { \mathrm { g r a d ~ } f } { | \mathrm { g r a d ~ } f | } } \quad t h e s l o p e \ i s \quad ( \mathrm { g r a d ~ } f ) \cdot \mathbf { u } = { \frac { | \mathrm { g r a d ~ } f | ^ { 2 } } { | \mathrm { g r a d ~ } f | } } = | \mathrm { g r a d ~ } f | .$

The example $f = 3 x + y + 1$ had grad $f = ( 3 , 1 )$ : Its steepest slope was in the direction $\mathbf { u } = ( 3 , 1 ) / \sqrt { 1 0 }$ : The maximum slope was ${ \sqrt { 1 0 } } .$ : That is grad $f | = { \sqrt { 9 + 1 } }$ :

Important point: The maximum of .grad $f ) \cdot { \mathbf { u } }$ is the length grad $f |$ : In nonlinear examples, the gradient and steepest direction and slope will vary. But look at one particular point in Figure 13.13. Near that point, and near any point, the linear picture takes over.

On the graph of $f ,$ the special vectors are the level direction $\mathbf { L } = ( f _ { y } , - f _ { x } , 0 )$ and the uphill direction $\mathbf { U } = ( f _ { x } , f _ { y } , f _ { x } ^ { 2 } + f _ { y } ^ { 2 } )$ and the normal $\mathbf { N } = ( f _ { x } , f _ { y } , - 1 )$ : Problem 18 checks that tho se are perpendicular.

EXAMPLE 3 The gradient of $f ( x , y ) = ( 1 4 - x ^ { 2 } - y ^ { 2 } ) / 3 \mathrm { i s } \nabla f = ( - 2 x / 3 , - 2 y / 3 )$ :

On the surface, the normal vector is $\mathbf { N } = ( - 2 x / 3 , - 2 y / 3 , - 1 )$ : At the point $( 1 , 2 , 3 )$ ; this perpendicular is $\mathbf { N } = ( - 2 / 3 , - 4 / 3 , - 1 )$ : At the point $( 1 , 2 )$ down in the base, the gradient is $( - 2 / 3 , - 4 / 3 )$ : The length of grad $f$ is the slope $\sqrt { 2 0 } / 3$ :

Probably a hiker does not go straight up. A “grade” of $\sqrt { 2 0 } / 3$ is fairly steep (almost $1 5 0 \%$ ). To estimate the slope in other directions, measure the distance along the path between two contour lines. If $\Delta f = 1$ in a distance $\Delta s = 3$ the slope is about $1 / 3$ : This calculation is not exact until the limit of $\Delta f / \Delta s$ , which is $D _ { \mathbf { u } } f .$

EXAMPLE 4 The gradient of $f ( x , y , z ) = x y + y z + x z$ has three components.

The pattern extends from $f ( x , y )$ to $f ( x , y , z )$ : The gradient is now the threedimensional vector $( f _ { x } , f _ { y } , f _ { z } )$ : For this function grad $f$ is $( y + z , x + z , x + y )$ : To draw the graph of $w = f ( x , y , z )$ would require a four-dimensional picture, with axes in the $x y z w$ directions.

Notice the dimensions. The graph is a 3-dimensional “surface” in 4-dimensional space. The gradient is down below in the 3-dimensional base. The level sets of $f$ come from $x y + y z + z x = c$ —they are 2-dimensional. The gradient is perpendicular to that level set (still downain 3 dimensions). The gradient is notaN! The normal vectorais $( f _ { x } , f _ { y } , f _ { z } , - 1 )$ ; perpendicular to the surface up in 4-dimensional space.

EXAMPLE 5 Find grad $z$ when $z ( x , y )$ is given implicitly: $F ( x , y , z ) = x ^ { 2 } + y ^ { 2 } -$ $z ^ { 2 } = 0$ :

In this case we find $z = \pm { \sqrt { x ^ { 2 } + y ^ { 2 } } }$ : The derivatives are $\pm x / \sqrt { x ^ { 2 } + y ^ { 2 } }$ and $\pm y / \sqrt { x ^ { 2 } + y ^ { 2 } }$ ,  which go into grad $z$ : But the point is this: To find that gradient faster, differentiate $F ( x , y , z )$ as it stands. Then divide by $F _ { z }$ :

$$
F _ { x } d x + F _ { y } d y + F _ { z } d z = 0 \qquad \mathrm { o r } \qquad d z = ( - F _ { x } d x - F _ { y } d y ) / F _ { z } .
$$

The gradient is $( - F _ { x } / F _ { z } , - F _ { y } / F _ { z } )$ : Those derivatives are evaluated at $( x _ { 0 } , y _ { 0 } )$ : The computation does not need the explicit function $z = f ( x , y )$ :

$$
F = x ^ { 2 } + y ^ { 2 } - z ^ { 2 } \Rightarrow F _ { x } = 2 x , F _ { y } = 2 y , F _ { z } = - 2 z \Rightarrow \mathrm { g r a d } z = ( x / z , y / z ) .
$$

To go uphill on the cone, move in the direction $( x / z , y / z )$ : That gradient direction goes radially outward. The steepness of the cone is the length of the gradient vector:

$$
| \mathrm { g r a d } z | = \sqrt { ( x / z ) ^ { 2 } + ( y / z ) ^ { 2 } } = 1 \mathrm { b e c a u s e } z ^ { 2 } = x ^ { 2 } + y ^ { 2 } \mathrm { o n t h e \ c o n e } .
$$

# DERIVATIVES ALONG CURVED PATHS

On a straight path the derivative of $f$ is $D _ { \mathbf { u } } f = ( \mathrm { g r a d \ } f ) \cdot \mathbf { u } .$ : What is the derivative on a curved path? The path direction u is the tangent vector T. So replace u by $\mathbf { T }$ ; which gives the “direction” of the curve.

The path is given by the position vector $\mathbf { R } ( t ) = x ( t ) \mathbf { i } + y ( t ) \mathbf { j }$ : The velocity is $\mathbf { v } = ( d x / d t ) \mathbf { i } + ( d y / d t ) \mathbf { j }$ : The tangent vector is $\mathbf { T } = \mathbf { v } / | \mathbf { v } |$ : Notice the choice—to

move at any speed (with $\mathbf { v }$ ) or to go at unit speed (with $\mathbf { T }$ :) There is the same choice for the derivative of $f ( x , y )$ along this curve:

$$
{ \begin{array} { r l } { r a t e ~ o f c h a n g e } & { { \frac { d f } { d t } } = ( \operatorname { g r a d } ~ f ) \cdot \mathbf { v } ~ = { \frac { \partial f } { \partial x } } { \cfrac { d x } { d t } } + { \frac { \partial f } { \partial y } } { \cfrac { d y } { d t } } } \\ { s l o p e } & { { \frac { d f } { d s } } = ( \operatorname { g r a d } ~ f ) \cdot \mathbf { T } ~ = { \frac { \partial f } { \partial x } } { \cfrac { d x } { d s } } + { \frac { \partial f } { \partial y } } { \cfrac { d y } { d s } } } \end{array} }
$$

Th |e  |first involves time. If we move faster, $d f / d t$ increases. The second involves distance. If we move a distance $d s$ , at any speed, the function changes by $d f .$ : So the slope in that direction is $d f / d s$ : Chapter 1 introduced velocity as $d f / d t$ and slope as $d y / d x$ and mixed them up. Finally we see the difference. Uniform motion on a straight line has $\mathbf { R } = \mathbf { R } _ { 0 } + \mathbf { v } t$ : The velocity $\mathbf { v }$ is constant. The direction $\mathbf { T } = \mathbf { u } =$ $\mathbf { v } / | \mathbf { v } |$ is also constant. The directional derivative is .grad $f ) \cdot { \mathbf { u } }$ , but the rate of change is .grad $f ) \cdot \mathbf { v }$ :

Equations (4) and (5) look like chain rules. They are chain rules. The next section extends $d f / d t = ( d f / d x ) ( d x / d t )$ to more variables, proving (4) and (5). Here we focus on the meaning: $d f / d s$ is the derivative of $f$ in the direction $\mathbf { u } = \mathbf { T }$ along the curve.

EXAMPLE 7 Find $d f / d t$ and $d f / d s$ for $f = r$ : The curve is? $x = t ^ { 2 } , y = t$ in Figure 13.14a.

Solution The velocity along the curve is $\mathbf { v } = 2 t \mathbf { i } + \mathbf { j }$ : At the typical point $t = 1$ it is ${ \bf v } = 2 { \bf i } + { \bf j }$ : The unit tangent is $\mathbf { \bar { T } } = \mathbf { v } / \sqrt { 5 }$ : The gradient is a unit vector $\mathbf { i } / \sqrt { 2 } + \mathbf { j } / \sqrt { 2 }$ pointing outward, when $f ( x , y )$ is the distance $r$ from the center. The dot product with $\mathbf { v }$ is $d f / d t = 3 / { \sqrt { 2 } }$ : The dot product with $\mathbf { T }$ is $d f / d s = 3 / \sqrt { 1 0 }$ :

When we slow down to speed 1 (with $\mathbf { T }$ ), the changes in $f ( x , y )$ slow down too.

EXAMPLE 8 Find $d f / d s$ for $f = x y$ along the circular path $x = \cos t , y = \sin t$ : First take a direct approach. On the circle, $x y$ equals $( \cos t ) ( \sin t )$ : Its derivative comes from the product rule: $d f / d t = \cos ^ { 2 } t - \sin ^ { 2 } t$ : Normally this is different from $d f / d s$ , because the time $t$ need not equal the arc length $s$ : There is a speed factor $d s / d t$ to divide by—but here the speed is 1: (A circle of length $s = 2 \pi$ is completed at $t = 2 \pi$ :) Thus the slope $d f / d s$ along the roller-coaster in Figure 13.14 is $\cos ^ { 2 } t -$ $\sin ^ { 2 } t$ :

The second approach uses the vectors grad $f$ and $\mathbf { T }$ : The gradient of $f = x y$ is $( y , x ) = ( \sin t , \cos t )$ : The unit tangent vector to the path is $\mathbf { T } = ( - \sin t , \cos t )$ : Their

dot product is the same $d f / d s$ :

$$
s l o p e a l o n g p a t h = ( \operatorname { g r a d } f ) \cdot \mathbf { T } = - \sin ^ { 2 } t + \cos ^ { 2 } t .
$$

# GRADIENTS WITHOUT COORDINATES

This section ends with a little “philosophy.” What is the coordinate-free definition of the gradient? Up to now, grad $f = ( f _ { x } , f _ { y } )$ depended totally on the choice of $x$ and $y$ axes. But the steepness of a surface is independent of the axes. Those are added later, to help us compute.

The steepness $d f / d s$ involves only $f$ and the direction, nothing else. The gradient should be a “te|nsor”—i|ts meaning does not depend on the coordinate system. The gradient has different formulas in different systems $( x y$ or $r \theta$ or . . . ), but the direction and length of grad $f$ are determined by $d f / d s$ —without any axes:

The direction of grad $f$ is the one in which $d f / d s$ is largest.   
The length $\left| \operatorname { g r a d } f \right|$ is that largest slope.

|The key|equation is .change in $f$ / .gradient off / .change in position/: That is another way to write $\Delta f \approx f _ { x } \Delta x + f _ { y } \Delta y$ : It is the multivariable form—we used two variables—of the basic linear approximation $\Delta y \approx ( d y / d x ) \Delta x$ :

EXAMPLE 9 $D ( x , y ) =$ distance from $( x , y )$ to $( x _ { 0 } , y _ { 0 } )$ : Without derivatives prove grad $| D | = 1$ : The graph of $D ( x , y )$ is a cone with slope 1 and sharp point $( x _ { 0 } , y _ { 0 } )$ :

First question In which direction does the distance $D ( x , y )$ increase fastest? Answer Going directly away from $( x _ { 0 } , y _ { 0 } )$ : Therefore this is the direction of grad $D$ :

Second question How quickly does $D$ increase in that steepest direction? Answer A step of length $\Delta s$ increases $D$ by $\Delta s$ : Therefore $\left| \operatorname { g r a d } D \right| = \Delta s / \Delta s =$ 1:

Conclusion grad $D$ is a unit vector. The derivatives of $D$ in Problem 48 are $( x - x _ { 0 } ) / D$ and $( y - y _ { 0 } ) / D$ : The sum of their squares is 1, because $( x - x _ { 0 } ) ^ { 2 } +$ $( y - y _ { 0 } ) ^ { 2 }$ equals $D ^ { 2 }$ :