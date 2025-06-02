# This vector field grad $f$ is everywhere perpendicular to the level curves $f ( x , y ) =$ $c$ :

The length grad $f |$ tells how fast $f$ is changing (in the direction it changes fastest). Invent a function like $f = x ^ { 2 } y$ ; and you immediately have its gradient field $\mathbf { F } = 2 x y \mathbf { i } + x ^ { 2 } \mathbf { j }$ : To repeat, $M$ is $\partial f / \partial x$ and $N$ is $\partial f / \partial y$ :

For every vector field you should ask two questions: $I s$ it a gradient field? If so, what is $f 2$ Here are answers for the radial fields and spin fields:

15A The radial fields $\mathbf { R }$ and ${ \bf R } / r$ and ${ \bf R } / r ^ { 2 }$ are all gradient fields. The spin fields $\mathbf { S }$ and $\mathbf { S } / r$ are not gradients of any $f ( x , y )$ : The spin field $\mathbf { S } / r ^ { 2 }$ is the gradient of the polar angle $\theta = \tan ^ { - 1 } ( y / x )$ :

The derivatives of $f = { \textstyle \frac { 1 } { 2 } } ( x ^ { 2 } + y ^ { 2 } )$ are $x$ and $y$ : Thus $\mathbf { R }$ is a gradient field. The gradient of $f = r$ is the unit vector ${ \bf R } / r$ pointing outwards. Both fields are perpendicular to circles around the origin. Those are the level curves of $\scriptstyle f = { \frac { 1 } { 2 } } r ^ { 2 }$ and $f = r$ :

Question Is every $\mathbf { R } / r ^ { n }$ a gradient field? Answer Yes. But among the spin fields, the only gradient is $\mathbf { S } / r ^ { 2 }$ :

A major goal of this chapter is to recognize gradient fields by a simple test. The rejection of S and $\mathbf { S } / r$ will be interesting. For some reason $- y \mathbf { i } + x \mathbf { j }$ is rejected and $y \mathbf { i } + x \mathbf { j }$ is accepted. (It is the gradient of :) The acceptance of $\mathbf { S } / r ^ { 2 }$ as the gradient of $f = \theta$ contains a surprise at the origin (Section 15.3).

Gradient fields are called conservative. The function $f$ is the potential function. These words, and the next examples, come from physics and engineering.

# EXAMPLE 5 The velocity field is $\mathbf { V }$ and the flow field is $\rho \mathbf { V }$ :

Suppose fluid moves steadily down a pipe. Or a river flows smoothly (no waterfall). Or the air circulates in a fixed pattern. The velocity can be different at different points, but there is no change with time. The velocity vector $\mathbf { V }$ gives the direction of flow and speed of flow at every point.

In reality the velocity field is $\mathbf { V } ( x , y , z )$ ; with three components $M , N , P$ : Those are the velocities $v _ { 1 } , v _ { 2 } , v _ { 3 }$ in the $x , y , z$ directions. The speed $| \mathbf { V } |$ is the length: $| \mathbf { V } | ^ { 2 } = v _ { 1 } ^ { 2 } + v _ { 2 } ^ { 2 } + v _ { 3 } ^ { 2 }$ : In a “plane flow” the $\mathbf { k }$ component is zero, and the velocity field is $v _ { 1 } \mathbf { i } + v _ { 2 } \mathbf { j } = M \mathbf { i } + N \mathbf { j }$ :

For a compact disc or a turning wheel, $\mathbf { V }$ is a spin field $\mathbf { V } = { \boldsymbol { \omega } } \mathbf { S }$ , $\omega =$ angular velocity). A tor|nad|o might be closer to ${ \mathbf { V } } = { \mathbf { S } } / r ^ { 2 }$ (except for a dead spot at the center). An explosion could have ${ \mathbf V } = { \mathbf R } / r ^ { 2 }$ : A quieter example is flow in and out of a lake with steady rain as a source term.

The flow field $\rho \mathbf { V }$ is the density $\rho$ times the velocity field. While $\mathbf { V }$ gives the rate of movement, $\rho \mathbf { V }$ gives the rate of movement of mass. A greater density means a greater rate $| \rho \mathbf { V } |$ of “mass transport.” It is like the number of passengers on a bus times the speed of the bus.

EXAMPLE 6 Force fields from gravity: $\mathbf { F }$ is dowBnwa rBd in the classroom, $\mathbf { F }$ is radial in space.

When gravity pulls downward, it has only one nonzero component: $\mathbf { F } = - m g \mathbf { k }$ : This assumes that vectors to the center of the Earth are parallel—almost true in a classroom. Then $\mathbf { F }$ is the gradient of $- m g z$ (note $\partial f / \partial z = - m g )$ .

In physics the usual potential is not $- m g z$ but $+ m g z$ : The force field is minus grad $f$ also in electrical engineering. Electrons flow from high potential to low potential. The mathematics is the same, but the sign is reversed.

In space, the force is radial inwards: $\mathbf { F } = - m M G \mathbf { R } / r ^ { 3 }$ : Its magnitude is proportional to $1 / r ^ { 2 }$ (Newton’s inverse square law). The masses are $m$ and $M$ ; and the gravitational constant is $G = 6 . 6 7 2 \times 1 0 ^ { - 1 1 } \mathrm { . }$ —with distance in meters, mass in kilograms, and time inBseconds. The dimensioBns of $G$ are .force/.diBstance $\cdot ^ { 2 } / ( \mathrm { m a s s } ) ^ { 2 }$ : This is different fBrom the acceleration $g = 9 . 8 \mathrm { m } / \mathrm { s e c } ^ { 2 }$ ; whichB already accounts for the mass and radius of the Earth.

Like all radial fields, gravity is a gradient field. It comes from a potential $f$ :

EXAMPLE 7 (a short example) Current in a wire produces a magnetic field B: It is the spin field $\mathbf { S } / r ^ { 2 }$ around the wire, times the strength of the current.

# STREAMLINES AND LINES OF FORCE

Drawing a vector field is not always easy. Even the spin field looks messy when the vectors are too long (they go in circles and fall across each other). The circles give

a clearer picture than the vectors. In any field, the vectors are tangent to “field lines”— which in the spin case are circles.

DEFINITION $C$ is a field line or integral curve if the vectors $\mathbf { F } ( x , y )$ are tangent to $C$ : The slope $d y / d x$ of the curve $C$ equals the slope $N / M$ of the vector $\mathbf { F } =$ $M \mathbf { i } + N \mathbf { j }$ :

$$
{ \frac { d y } { d x } } = { \frac { N ( x , y ) } { M ( x , y ) } } \quad \left( = - { \frac { x } { y } } { \mathrm { ~ f o r ~ t h e ~ s p i n ~ f i e l d } } \right) .
$$

We are still drawing the field of vectors, but now they are infinitesimally short. They are connected into curves! What is lost is their length, because $\mathbf { s }$ and $\mathbf { S } / r$ and $\mathbf { S } / r ^ { 2 }$ all have the same field lines (circles). For the position field $\mathbf { R }$ and gravity field ${ \bf R } / r ^ { 3 }$ ; the field lines are rays from the origin. In this case the “curves” are actually straight.

EXAMPLE 8 Show that the field lines for the velocity field $\mathbf { V } = y \mathbf { i } + x \mathbf { j }$ are hyperbolas.

$$
{ \frac { d y } { d x } } = { \frac { N } { M } } = { \frac { x } { y } } \Rightarrow y d y = x d x \Rightarrow { \frac { 1 } { 2 } } y ^ { 2 } - { \frac { 1 } { 2 } } x ^ { 2 } = { \mathrm { c o n s t a n t . } }
$$

At every point these hyperbolas line up with the velocity V: Each particle of fluid travels on a field line. In fluid flow those hyperbolas are called streamlines. Drop a leaf into a river, and it follows a stre Bamli Bne. Figu rBe 15 B.4 shows the streamlines for a river going around a bend.

Don’t forget the essential question about each vector field. Is it a gradient field? For $\mathbf { V } = y \mathbf { i } + x \mathbf { j }$ the answer is yes, and the potential is $f = x y$ :



When there is a potential, it has level curves. They connect points of equal potential, so the curves $f ( x , y ) = c$ are called equipotentials. Here they are the curves $x y =$ $c$ — also hyperbolas. Since gradients are perpendicular to level curves, the streamlines are perpendicular to the equipotentials. Figure 15.4 is sliced one way by streamlines and the other way by equipotentials.

A gradient field $\mathbf { F } = { \boldsymbol { \partial } } f / { \partial x } { \mathbf { i } } + { \boldsymbol { \partial } } f / { \partial y } { \mathbf { j } }$ is tangent to the field lines (streamlines) and perpendicular to the equipotentials (level curves of $f$ ).

# 15 Vector Calculus

In the gradient direction $f$ changes fastest. In the level direction $f$ doesn’t change at all. The chain rule along $f ( x , y ) = c$ proves these directions to be perpendicular:

$$
{ \frac { \partial f } { \partial x } } { \frac { d x } { d t } } + { \frac { \partial f } { \partial y } } { \frac { d y } { d t } } = 0 \quad { \mathrm { o r } } \quad ( { \mathrm { g r a d ~ } } f ) \cdot ( { \mathrm { t a n g e n t ~ t o ~ l e v e l ~ c u r v e } } ) = 0 .
$$

EXAMPLE 9 The streamlines of $\mathbf { S } / r ^ { 2 }$ are circles around $( 0 , 0 )$ . The equipotentials are rays $\theta = c$ : Add rays to Figure 15.2 for the gradient field $\mathbf { S } / r ^ { 2 }$ :

For the gravity field those are reversed. A body is pulled in along the field lines (rays). The equipotentials are the circles where $f = 1 / r$ is constant. The plane is crisscrossed by “orthogonal trajectories”—curves that meet everywhere at right angles.

If you bring a magnet near a pile of iron filings, a little shake will display the field lines. In a force field, they are “lines of force.” Here are the other new words.

Vector field $\mathbf { F } ( x , y , z ) = M \mathbf { i } + N \mathbf { j } + P \mathbf { k }$ Plane field $\mathbf { F } = M ( x , y ) \mathbf { i } + N ( x , y ) \mathbf { j } { \big | }$ Radial field: multiple of $\mathbf { R } = x \mathbf { i } + y \mathbf { j } + z \mathbf { k }$ Spin field: multiple of $\mathbf { S } = - y \mathbf { i } + x \mathbf { j }$ Gradient field $\ b =$ conservative field: $M = \partial f / \partial x , N = \partial f / \partial y , P = \partial f / \partial z$ Potential $f ( x , y )$ (not a vector) Equipotential curves $f ( x , y ) = c$ Streamline $\ b =$ field line $\ b =$ integral curve: a curve that has $\mathbf { F } ( x , y )$ as its tangent vectors.