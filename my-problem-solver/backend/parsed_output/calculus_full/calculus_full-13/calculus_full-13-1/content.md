# 13.1 Surfaces and Level Curves

# 

The graph of $y = f ( x )$ is a curve in the $x y$ plane. There are two variables— $x$ is independent and free, $y$ is dependent on $x$ : Above $x$ on the base line is the point $( x , y )$ on the curve. The curve can be displayed on a two-dimensional printed page. The graph of $z = f ( x , y )$ is a surface in xyz space. There are three variables— $x$ and $y$ are independent, $z$ is dependent. Above $( x , y )$ in the base plane is the point $( x , y , z )$ on the surface (Figure 13.1). Since the printed page remains two-dimensional, we shade or color or project the surface. The eyes are extremely good at converting two-dimensional images into three-dimensional understanding—they get a lot of practice. The mathematical part of our brain also has something new to work on—two partial derivatives.

This section uses examples and figures to illustrate surfaces and their level curves. The next section is also short. Then the work begins.

# EXAMPLE 1 Describe the surface and the level curves for $z = f ( x , y ) = { \sqrt { x ^ { 2 } + y ^ { 2 } } }$ :

The surface is a cone. Reason: $\sqrt { x ^ { 2 } + y ^ { 2 } }$ is the distance in the base plane from $( 0 , 0 )$ to $( x , y )$ : When we go out a distance 5 in the base plane, we go up the same distance 5 to the surface. The cone climbs with slope 1: The distance out to $( x , y )$ equals the distance up to $z$ (this is a $4 5 ^ { \circ }$ cone).

The level curves are circles. At height 5; the cone contains a circle of points—all at the same “level” on the surface. The plane $z = 5$ meets the surface $z = \sqrt { x ^ { 2 } + y ^ { 2 } }$ at those points (Figure 13.1b). The circle below them (in the base plane) is the level curve.

DEFINITION A level curve or contour line of $z = f ( x , y )$ contains all points $( x , y )$ that share the same value $f ( x , y ) = c$ . Above those points, the surface is at the height $z = c$ :

There are different level curves for different $c$ : To see the curve for $c = 2$ ; cut through the surface with the horizontal plane $z = 2$ : The plane meets the surface above the points where $f ( x , y ) = 2$ : The level curve in the base plane has the equation $f ( x , y ) = 2$ : Above it are all the points at “level $2 ^ { \circ }$ or “level $c ^ { , \dag }$ on the surface.

Every curve $f ( x , y ) = c$ is labeled by its constant $c$ : This produces a contour map (the base plane is full of curves). For the cone, the level curves are given by ${ \sqrt { x ^ { 2 } + y ^ { 2 } } } = c$ ; and the contour map consists of circles of radius $c$ :

Question What are the level curves of $z = f ( x , y ) = x ^ { 2 } + y ^ { 2 } ?$

Answer Still circles. But the surface is not a cone (it bends up like a parabola). The circle of radius 3 is the level curve $x ^ { 2 } + y ^ { 2 } = 9$ : On the surface above, the height is 9:

EXAMPLE 2 For the linear function $f ( x , y ) = 2 x + y$ ; the surface is a plane. Its level curves are straight lines. The surface $z = 2 x + y$ meets the plane $z = c$ in the line $2 x + y = c$ . That line is above the base plane when $c$ is positive, and below when $c$ is negative. The contour lines are in the base plane. Figure $1 3 . 2 \mathrm { b }$ labels these parallel lines according to their height in the surface.

Question If the level curves are all straight lines, must they be parallel? Answer No. The surface $z = y / x$ has level curves $y / x = c$ : Those lines $y = c x$ swing around the origin, as the surface climbs like a spiral playground slide.

EXAMPLE 3 The weather map shows contour lines of the temperature function. Each level curve connects points at a constant temperature. One line runs from Seattle to Omaha to Cincinnati to Washington. In winter it is painful even to think about the line through L.A. and Texas and Florida. USA Today separates the contours by color, which is better. We had never seen a map of universities.

Question From a contour map, how do you find the highest point? Answer The level curves form loops around the maximum point. As $c$ increases the loops become tighter. Similarly the curves squeeze to the lowest point as $c$ decreases.

EXAMPLE 4 A contour map of a mountain may be the best example of all. Normally the level curves are separated by 100 feet in height. On a steep trail those curves are bunched together—the trail climbs quickly. In a flat region the contour lines are far apart. Water runs perpendicular to the level curves. On my map of New Hampshire that is true of creeks but looks doubtful for rivers.

Question Which direction in the base plane is uphill on the surface? Answer The steepest direction is perpendicular to the level curves. This is important. Proof to come.

EXAMPLE 5 In economics $x ^ { 2 } y$ is a utility function and $x ^ { 2 } y = c$ is an indifference curve.

The utility function $x ^ { 2 } y$ gives the value of $x$ hours awake and $y$ hours asleep. Two hours awake and fifteen minutes asleep have the value $f = ( 2 ^ { 2 } ) ( \textstyle { \frac { 1 } { 4 } } )$ : This is the same

as one hour of each: $f = ( 1 ^ { 2 } ) ( 1 )$ : Those lie on the same level curve in Figure 13.4a.   
We are indifferent, and willing to exchange any two points on a level curve.

The indifference curve is “convex.” We prefer the average of any two points. The line between two points is up on higher level curves.

Figure $1 3 . 4 \mathrm { b }$ shows an extreme case. The level curves are straight lines $4 x + y = c$ Four quarters are freely substituted for one dollar. The value is $f = 4 x + y$ dollars.

Figure $1 3 . 4 \mathrm { c }$ shows the other extreme. Extra left shoes or extra right shoes are useless. The value (or utility) is the smaller of $x$ and $y$ : That counts pairs of shoes.