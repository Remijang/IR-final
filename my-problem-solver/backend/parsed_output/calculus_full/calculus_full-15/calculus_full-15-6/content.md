# 15.6 Stokes’ Theorem and the Curl of F

For the Divergence Theorem, the surface was closed. $S$ was the boundary of $V$ . Now the surface is not closed and $S$ has its own boundary—a curve called $C$ . We are back near the original setting for Green’s Theorem (region bounded by curve, double integral equal to work integral). But Stokes’ Theorem, also called Stokes’s Theorem, iBs in  tBhree-dBime nBsional space. There is a curved surface $S$ bounded by a space curve $C$ . This is our first integral around a space curve.

The move to three dimensions brings a change in the vector field. The plane field $\mathbf { F } ( x , y ) = M \mathbf { i } + N \mathbf { j }$ becomes a space field $\mathbf { F } ( x , y , z ) = M \mathbf { i } + N \mathbf { j } + P \mathbf { k }$ . The work $M d x + N d y$ now includes $P d z$ . The critical quantity in the double integral (it was $\hat { \sigma } N / \hat { \sigma } x - \hat { \sigma } M / \hat { \sigma } y )$ must change too. We called this scalar quantity “curl $\mathbf { F }$ ,” but in reality it is only the thirdcomponent of a vector. Stokes’ Theorem needs all three components of that vector—which is curl $\mathbf { F }$ .

DEFINITION The curl of a vector field $\mathbf { F } ( x , y , z ) = M \mathbf { i } + N \mathbf { j } + P \mathbf { k }$ is the vector field

$$
\operatorname { c u r l } \mathbf { F } = \left( { \frac { \partial P } { \partial y } } - { \frac { \partial N } { \partial z } } \right) \mathbf { i } + \left( { \frac { \partial M } { \partial z } } - { \frac { \partial P } { \partial x } } \right) \mathbf { j } + \left( { \frac { \partial N } { \partial x } } - { \frac { \partial M } { \partial y } } \right) \mathbf { k } .
$$

The symbol $\nabla \times \mathbf { F }$ stands for a determinant that yields those six derivatives:

$$
\mathrm { c u r l } { \mathbf { F } } = \nabla \times { \mathbf { F } } = \left| \begin{array} { c c c } { \mathbf { i } } & { \mathbf { j } } & { \mathbf { k } } \\ { \partial / \partial x } & { \partial / \partial y } & { \partial / \partial z } \\ { M } & { N } & { P } \end{array} \right| .
$$

The three products i $\partial / \partial y \ P$ and j $\partial / \partial z \ M$ and $\textbf { k } \partial / \partial x \textbf { } N$ have plus signs. The three products like k $\partial / \partial y \ M$ , down to the left, have minus signs. TherBe is a Bcyclic symmetry. This determinant helps the memory, even if it looks and is illegal. A determinant is not supposed to have a row of vectors, a row of operators, and a row of functions.

EXAMPLE 1 The plane field $M ( x , y ) \mathbf { i } + N ( x , y ) \mathbf { j }$ has $P = 0$ and $\partial M / \partial z = 0$ and $\partial N / \partial z = 0$ . Only two terms survive: curl ${ \bf F } = ( \hat { \sigma } N / \hat { \sigma } x - \hat { \sigma } M / \hat { \sigma } y ) { \bf k }$ . Back to Green.

EXAMPLE 2 The cross product $\mathbf { a } \times \mathbf { R }$ is a spin field S. Its axis is thefixed vector $\mathbf { a } = a _ { 1 } \mathbf { i } + a _ { 2 } \mathbf { j } + a _ { 3 } \mathbf { k }$ . The flow in Figure 15.23 turns around a, and its components are

$$
\mathbf { S } = \mathbf { a } \times \mathbf { R } = { \left| \begin{array} { l l l } { \mathbf { i } } & { \mathbf { j } } & { \mathbf { k } } \\ { a _ { 1 } } & { a _ { 2 } } & { a _ { 3 } } \\ { x } & { y } & { z } \end{array} \right| } = ( a _ { 2 } z - a _ { 3 } y ) \mathbf { i } + ( a _ { 3 } x - a _ { 1 } z ) \mathbf { j } + ( a _ { 1 } y - a _ { 2 } x ) \mathbf { k } .
$$

Our favorite spin field $- y \mathbf { i } + x \mathbf { j }$ has $( a _ { 1 } , a _ { 2 } , a _ { 3 } ) = ( 0 , 0 , 1 )$ and its axis is $\mathbf a = \mathbf k$ .

BThe divBergence ofB a spinB field is $M _ { x } + N _ { y } + P _ { z } = 0 + 0 + 0$ . Note how the divergence uses $M _ { x }$ while the curl uses $N _ { x }$ and $P _ { x }$ . The curl of S is the vector 2a:

$$
\bigg ( \frac { \partial P } { \partial y } - \frac { \partial N } { \partial z } \bigg ) \mathbf { i } + \bigg ( \frac { \partial M } { \partial z } - \frac { \partial P } { \partial x } \bigg ) \mathbf { j } + \bigg ( \frac { \partial N } { \partial x } - \frac { \partial M } { \partial y } \bigg ) \mathbf { k } = 2 a _ { 1 } \mathbf { i } + 2 a _ { 2 } \mathbf { j } + 2 a _ { 3 } \mathbf { k } = 2 \mathbf { a } .
$$

This example begins to reveal the meaning of the curl. It measures the spin! The direction of curl $\mathbf { F }$ is the axis of rotation—in this case along a. The magnitude of

curl $\mathbf { F }$ is twice the speed of rotation. In this case ${ \big | } \mathrm { c u r l } \ \mathbf { F } { \big | } = 2 { \big | } \mathbf { a } { \big | }$ and the angular velocity is $\left. \mathbf { a } \right.$ .

EXAMPLE 3 (!!) Every gradient field $\mathbf { F } = \partial f / \partial x \ \mathbf { i } + \partial f / \partial y \ \mathbf { j } + \partial f / \partial z$ k has curl $\mathbf { F } = \mathbf { 0 }$ :

$$
\operatorname { c u r l } \mathbf { F } = \left( { \frac { \partial } { \partial y } } { \frac { \partial f } { \partial z } } - { \frac { \partial } { \partial z } } { \frac { \partial f } { \partial y } } \right) \mathbf { i } + \left( { \frac { \partial } { \partial z } } { \frac { \partial f } { \partial x } } - { \frac { \partial } { \partial x } } { \frac { \partial f } { \partial z } } \right) \mathbf { j } + \left( { \frac { \partial } { \partial x } } { \frac { \partial f } { \partial y } } - { \frac { \partial } { \partial y } } { \frac { \partial f } { \partial x } } \right) \mathbf { k } = \mathbf { 0 } .
$$

Always $f _ { y z }$ equBals $f _ { z y }$ . ThBey cancel.BAlsoB $f _ { x z } = f _ { z x }$ and $f _ { y x } = f _ { x y }$ .BSo curl grad $f = \mathbf { 0 }$ .

EXAMPLE 4 (twin of Example 3) The divergence of curl $\mathbf { F }$ is also automatically zero:

$$
\operatorname { d i v } \operatorname { c u r l } \mathbf { F } = { \frac { \hat { \mathcal { O } } } { { \hat { \mathcal { O } } } x } } \left( { \frac { { \hat { \mathcal { O } } } P } { \partial y } } - { \frac { { \hat { \mathcal { O } } } N } { { \hat { \mathcal { O } } } z } } \right) + { \frac { \hat { \mathcal { O } } } { { \hat { \mathcal { O } } } y } } \left( { \frac { { \hat { \mathcal { O } } } M } { { \hat { \mathcal { O } } } z } } - { \frac { { \hat { \mathcal { O } } } P } { { \hat { \mathcal { O } } } x } } \right) + { \frac { \hat { \mathcal { O } } } { { \hat { \mathcal { O } } } z } } \left( { \frac { { \hat { \mathcal { O } } } N } { { \hat { \mathcal { O } } } x } } - { \frac { { \hat { \mathcal { O } } } M } { { \hat { \mathcal { O } } } y } } \right) = 0 .
$$

Again the mixed derivatives give $P _ { x y } = P _ { y x }$ and $N _ { x z } = N _ { z x }$ and $M _ { z y } = M _ { y z }$ . The terms cancel in pairs. In “curl grad” and “div curl”, everything is arranged to give zero.

15N The curl of the gradient of every $f ( x , y , z )$ is curl grad $\boldsymbol { f } = \nabla \times \nabla f = \mathbf { 0 }$ . The divergence of the curl of every $\mathbf { F } ( x , y , z )$ is div curl $\mathbf { F } = \nabla \cdot \nabla \times \mathbf { F } = 0$ .

The spin field S has no divergence. The position field $\mathbf { R }$ has no curl. $\mathbf { R }$ is the gradient of $f = { \textstyle \frac { 1 } { 2 } } ( x ^ { 2 } + y ^ { 2 } + z ^ { 2 } )$ . S is the curl of a suitable $\mathbf { F }$ . Then div $\mathbf { S } =$ div curl $\mathbf { F }$ and curl $\mathbf { R } =$ curl grad $f$ are automatically zero.

You correctly believe that curl $\mathbf { F }$ measures the “spin” of the field. You may expect that curl $( \mathbf { F } + \mathbf { G } )$ is curl $\mathbf { F } + \mathrm { c u r l } \mathbf { G }$ . Also correct. Finally you may think that a field of parallel vectors has no spin. That is wrong. Example 5 has parallel vectors, but their different lengths produce spin.

EXAMPLE 5 The field $\mathbf { V } = z \mathbf { i }$ in the $x$ direction has curl $\mathbf { V } = \mathbf { j }$ in the $y$ direction.

If you put a wheel in the $x z$ plane, this field will turn it. The velocity $z \mathbf { i }$ at the top of the wheel is greater than $z \mathbf { i }$ at the bottom (Figure 15.23c). So the top goes faster and the wheel rotates. The axis of rotation is curl $\mathbf { V } = \mathbf { j }$ . The turning speed is $\frac { 1 } { 2 }$ , because this curl has magnitude 1.

Another velocity field $\mathbf { v } = - x \mathbf { k }$ produces the same spin: curl $\mathbf { v } = \mathbf { j }$ . The flow is in the $z$ direction, it varies in the $x$ direction, and the spin is in the $y$ direction. Also interesting is $\mathbf { V } + \mathbf { v }$ . The two “shear fields” add to a perfect spin field $\mathbf { S } = z \mathbf { i } - x \mathbf { k }$ , whose curl is 2j.

# 15.6 Stokes’ Theorem and the Curl of F

# THE MEANING OF CURL F

Example 5 put a paddlewheel into the flow. This is possible for any vector field $\mathbf { F }$ , and it gives insight into curl $\mathbf { F }$ . The turning of the wheel (if it turns) depends on its location $( x , y , z )$ . The turning also depends on the orientation of the wheel. We could put it into a spin field, and if the wheel axis $\mathbf { n }$ is perpendicular to the spin axis a, the wheel won’t turn! The general rule for turning speed is this: the angular velocity of the wheel is $\scriptstyle { \frac { 1 } { 2 } } ( \mathbf { c u r l } \mathbf { F } ) \cdot \mathbf { n }$ . This is the “directional spin,” just as .grad $f ) \cdot { \mathbf { u } }$ was the “directional derivative”—and $\mathbf { n }$ is a unit vector like u.

There is no spin anywhere in a gradient field. It is irrotational: curl grad $f = \mathbf { 0 }$ .

The pure spin field $\mathbf { a } \times \mathbf { R }$ h |as curl $\mathbf { F } = 2 \mathbf { a }$ . The angular velocity is $\mathbf { a } \cdot \mathbf { n }$ (note that $\frac { 1 } { 2 }$ cancels 2). This turning is everywhere, not just at the origin. If you put a penny on a compact disk, it turns once when the disk rotates once. That spin is “around itself,” and it is the same whether the penny is at the center or not.

The turning speed is greatest when the wheel axis $\mathbf { n }$ lines up with the spin axis a. Then $\mathbf { a } \cdot \mathbf { n }$ is the full length $\left. \mathbf { a } \right.$ . The gra|dient g|ives the direction of fastest growth, and the curl gives the direction of fastest turning:

maximum growth rate of $f$ is grad $f |$ in the direction of grad $f$ maximum rotation rate of $\mathbf { F }$ is ${ \frac { 1 } { 2 } } \left| \operatorname { c u r l } \mathbf { F } \right|$ in the direction of curl F.

# STOKES’ THEOREM

Finally we come to the big theorem. It will be like Green’s Theorem—a line integral equals a surface integral. The line integral is still the work $\oint \mathbf { F } \cdot d \mathbf { R }$ around a curve. The surface integral in Green’s Theorem is $\iint ( N _ { x } - M _ { y } ) \dot { d x } d y$ . The surface is flat (in the $x y$ plane). Its normal direction is $\mathbf { k }$ , and we now recognize $N _ { x } - M _ { y }$ as the $\mathbf { k }$ component of the curl. Green’s Theorem uses only this component because the normal direction is always $\mathbf { k }$ . For Stokes’ Theorem on a curved surface, we need all three components of curl $\mathbf { F }$ .

Figure 15.24 shows a hat-shaped surface $S$ and its boundary $C$ (a closed curve). Walking in the positive direction around $C$ , with your head pointing in the direction of n, the surface is on your left. You may be standing straight up $\mathbf { \tilde { n } = k }$ in Green’s Theorem). You may even be upside down . $\mathbf { { \dot { n } } = - k }$ is allowed/. In that case you must go the other way around $C$ , to keep th¾e two sides »of»equation (6) equal. The surface is still on the left. A Möbius strip is not allowed, because its normal direction cannot be established. The unit vector $\mathbf { n }$ determines the “counterclockwise direction” along $C$ .

15O .Stokes’ Theorem/

$$
\oint _ { c } \mathbf { F } \cdot d \mathbf { R } = \int \int _ { s } \left( \operatorname { c u r l } \mathbf { F } \right) \cdot \mathbf { n } d S .
$$

The right side adds up small spins in the surface. The left side is the total circulation (or work) around $C$ . That is not easy to visualize—this may be the hardest theorem in the book—but notice one simple conclusion. $\pmb { I f }$ curl $\mathbf { F } = \mathbf { 0 }$ then $\oint \mathbf { F } \cdot d \mathbf { R } = 0$ . This applies above all to gradient fields—as we know.

A gradient field has no curl, by (4). A gradient field does no work, by (6). In three dimensions as in two dimensions, gradient fields are conservative fields. They will be the focus of this section, after we outline a proof (or two proofs) of Stokes’ Theorem.

The first proof shows why the theorem is true. The second proof shows that it really is true (and how to compute). You may prefer the first.

First proof Figure 15.24 has a triangle $A B C$ attached to atriangle $A C D$ . Later there can be more triangles. $S$ will be piecewise flat, close to a curved surface. Two triangles are enough to make the point. In the plane of each triangle (they have different n’s) Green’s Theorem is known:

$$
\oint _ { \substack { A B + B C + C A } } \mathbf { F } \cdot d \mathbf { R } = \iint \mathbf { \Phi } \operatorname { c u r l } \mathbf { F } \cdot \mathbf { n } d S \oint \mathbf { \Phi } \mathbf { F } \cdot d \mathbf { R } = \iint \operatorname { c u r l } \mathbf { F } \cdot \mathbf { n } d S .
$$

Now add. The right sides give $\iint \mathrm { c u r l } \mathbf { F } { \cdot } \mathbf { n } d S$ over the two triangles. On the left, the integral over $C A$ cancels the’integral over $A C$ . The “crosscut” disappears. That leaves $A B + B C + C D + D A$ . This line integral goes around the outer boundary $C$ —which is the left side of Stokes’ Theorem.

Second proof Now the surface can be curved. A new proof may seem excessive, but it brings f¶ormulas you co¶uld compute with. From $z = f ( x , y )$ we have

$$
d z = \hat { \sigma } f / \hat { \sigma } x ~ d x + \hat { \sigma } f / \hat { \sigma } y ~ d y \quad \mathrm { a n d } \quad \mathbf { n } d S = ( - \hat { \sigma } f / \hat { \sigma } x \mathbf { i } - \hat { \sigma } f / \hat { \sigma } y \mathbf { j } + \mathbf { k } ) d x ~ d y .
$$

For nd $S$ , see equation 15.4.11. With this $d z$ , the line integral in Stokes’ Theorem is

$$
\oint _ { C } \mathbf { F } \cdot d \mathbf { R } = \oint _ { \mathrm { \tiny ~ s h a d o w o f ~ C } } M d x + N d y + P ( \partial f / \partial x ~ d x + \partial f / \partial y ~ d y ) .
$$

The dot product of curl $\mathbf { F }$ and ${ \bf n } d S$ gives the surface integral $\iint _ { \mathrm { \tiny ~ S } } \mathrm { c u r l } \mathbf { F } \cdot \mathbf { n } d S$ :

$$
\int \displaylimits _ { \mathrm { I o w o f } } ^ { \infty } [ ( P _ { y } - N _ { z } ) ( - \partial f / \partial x ) + ( M _ { z } - P _ { x } ) ( - \partial f / \partial y ) + ( N _ { x } - M _ { y } ) ] d x d y .
$$

To prove ${ ( 7 ) = ( 8 ) }$ , change $M$ in Green’s Theorem to $M + P \hat { \sigma } f / \partial x$ . Also change $N$ to $N + P \partial f / \partial y$ . Then $( 7 ) = ( 8 )$ is Green’s Theorem down on the shadow (Problem 47). This proves Stokes’ Theorem up on $S$ . Notice how Green’s Theorem (flat surface) was the key to both proofs of Stokes’ Theorem (curved surface).

EXAMPLE 6 Stokes’ Theorem in electricity and magnetism yields Faraday’s Law.

Stokes’ Theorem is not heavily used for calculations—equation (8) shows why. But the spin or curl or vorticity of a flow is absolutely basic in fluid mechanics. The other important application, coming now, is to electric fields. Faraday’s Law is to Gauss’s Law as Stokes’ Theorem is to the Divergence Theorem.

Suppose the curve $C$ is an actual wire. We can produce current along $C$ by varying the magnetic field $\mathbf { B } ( t )$ . The flux $\varphi = \iint \mathbf { B } \cdot \mathbf { n } d S$ , passing within $C$ and changing in time, creates an electric field $\mathbf { E }$ that doe’s work:

$$
F a r a d a y ^ { \prime } s L a w \ ( \mathrm { i n t e g r a l ~ f o r m } ) : \mathrm { w o r k } = \oint _ { C } \mathbf { E } \cdot d \mathbf { R } = - d \varphi / d t .
$$

That is physics. It may be true, it may be an appBrox iBmation.N Bow c Bomes mathematics (surely true), which turns this integral form into a differential equation. Information at points is more convenient than information around curves. Stokes converts the line integral of $\mathbf { E }$ into the surface integral of curl $\mathbf { E }$ :

$$
\oint _ { C } \mathbf { E } \cdot d \mathbf { R } = \iint _ { S } \subset \mathrm { c u r l } ~ \mathbf { E } \cdot \mathbf { n } d S ~ \mathrm { a n d ~ a l s o } ~ - \hat { \sigma } \varphi / \hat { \sigma } t = \iint _ { S } - ( \hat { \sigma } \mathbf { B } / \hat { \sigma } t ) \cdot \mathbf { n } d S .
$$

These are equal for any curve $C$ , however small. So the right sides are equal for any surface $S$ . We squeeze to a point. The right hand sides give one of Maxwell’s equations:

$$
F a r a d a y ^ { \prime } s L a w ( \mathrm { d i f f e r e n t i a l ~ f o r m } ) \colon \mathrm { c u r l ~ } \mathbf { E } = - \hat { \sigma } \mathbf { B } / \hat { \sigma } t .
$$

# COBNSE BRVATIVE FIELDS AND POTENTIAL FUNCTIONS

The chapter ends with our constant and important question: Which fields do no work around closed curves? Remember test $\mathbf { D }$ for plane curves and plane vector fields:

if $\partial M / \partial y = \partial N / \partial x$ theBn F  iBs conservative and ${ \bf F } =$ grad $f$ and $\oint \mathbf { F } \cdot d \mathbf { R } = 0 .$

Now allow a three-dimensional field like $\mathbf { F } = 2 x y \ \mathbf { i } + ( x ^ { 2 } + z ) \mathbf { j } + y \mathbf { k }$ . Does it do work around a space curve? $O r$ is it a gradient field? That will require $\partial f / \partial x = 2 x y$ and ${ \partial f } / { \partial y } = x ^ { 2 } + z$ and $\partial f / \partial z = y$ . We have three equations for one function $f ( x , y , z )$ . Normally they can’t be solved. When test $\mathbf { D }$ is passed (now it is the threedimensional test: curl $\mathbf { F } = \mathbf { 0 }$ ) they can be solved. This example passes test $\mathbf { D }$ , and $f$ is $x ^ { 2 } y + y z$ .

15 $\mathrm { ~ \bf ~ { ~ P ~ } ~ } ( x , y , z ) = M \mathbf { i } + N \mathbf { j } + P \mathbf { k }$ is a conservative field if it has these properties:

A. The work $\oint \mathbf { F } \cdot d \mathbf { R }$ around every closed path in space is zero.   
B. The work $\int _ { P } ^ { Q } \mathbf { F } \cdot d \mathbf { R }$ depends on $P$ and $\boldsymbol { Q }$ , not on the path in space.   
C. $\mathbf { F }$ is a gradientñfield:ñ $M = \partial f / \partial x$ and $N =  { \partial } f /  { \partial } y$ and $P = \partial f / \partial z$ .   
D. The components satisfy $M _ { y } = N _ { x } , M _ { z } = P _ { x }$ , and $N _ { z } = P _ { y }$ (curl Fis zero).

A field with one of these properties has them all. $\mathbf { D }$ is the quick test.

A detailed proof of $\mathbf { A } \Rightarrow \mathbf { B } \Rightarrow \mathbf { C } \Rightarrow \mathbf { D } \Rightarrow \mathbf { A }$ is not needed. Only notice how $\mathbf C \Rightarrow \mathbf D$ : curl grBad $\mathbf { F }$ Bis always zeñro. The newest part is $\mathbf { D } \Rightarrow \mathbf { A } . \pmb { I } f$ curl $\mathbf { F } = \mathbf { 0 }$ then $\oint \mathbf { F } \cdot d \mathbf { R } = 0$ . But thaBt is  Bnot news. It is Stokes’BThe Boremñ.

The interesting problem is to solve the three equations for $f$ , when test $\mathbf { D }$ is passed. The example above had

$\partial f / \partial x = 2 x y \Rightarrow f = \int 2 x y d x = x ^ { 2 } y$ plus any function $C ( y , z )$ $\partial f / \partial y = x ^ { 2 } + z = x ^ { 2 } + \partial C / \partial y \Rightarrow C = y z$ plus any function $c ( z )$ $\partial f / \partial z = y = y + d c / d z \Rightarrow c ( z )$ can be zero.

The first step leaves an arbitrary $C ( y , z )$ to fix thesecond step. The second step leaves an arbitrary $c ( z )$ to fix the third step (not needed here). Assembling the three steps, $f = x ^ { 2 } y + C = x ^ { 2 } y + y z + c = x ^ { 2 } y + y z$ . Please recognize thBat th Be “fix-up” is only possible when curl $\mathbf { F } = \mathbf { 0 }$ . Test $\mathbf { D }$ must be passed.

EXAMPLE 7 Is $\mathbf { F } = ( z - y ) \mathbf { i } + ( x - z ) \mathbf { j } + ( y - x ) \mathbf { k }$ the gradient of any $f ?$

Test $\mathbf { D }$ says no. This $\mathbf { F }$ is a spin field $\mathbf { a } \times \mathbf { R }$ . Its curl is ${ 2 \mathbf { a } } = ( 2 , 2 , 2 )$ , which is not zero. A search for $f$ is bound to fail, but we can try. To match ${ \partial f } / { \partial x } = z - y$ , we must have $f = z x - y x + C ( y , z )$ . The $y$ derivative is $- x + \partial C / \partial y$ : That never matches $N = x - z$ , so $f$ can’t exist.

EXAMPLEB8  BWhat cBhoic eBof $P$ makes $\mathbf { F } = y z ^ { 2 } \mathbf { i } + x z ^ { 2 } \mathbf { j } + P \mathbf { k }$ conservative? Find $f$ .

Solution We need curl $\mathbf { F } = 0$ , by test D. First check $\partial M / \partial y = z ^ { 2 } = \partial N / \partial x$ . Also

$$
\begin{array} { r } { \partial P / \partial x = \partial M / \partial z = 2 y z \quad \mathrm { ~ a n d ~ } \quad \partial P / \partial y = \partial N / \partial z = 2 x z . } \end{array}
$$

$P = 2 x y z$ passes all tests. To find $f$ we can solve the three equations, or notice that $f = x y z ^ { 2 }$ is successful. Its gradient is $\mathbf { F }$ .

A third method defines $f ( x , y , z )$ as the work to reach $( x , y , z )$ from $( 0 , 0 , 0 )$ . The path doesn’t matter. For practice we integrate $\mathbf { F } \cdot d \mathbf { R } = M d x + N d y + P d z$ along the straight line $( x t , y t , z t )$ :

$$
f ( x , y , z ) = \int _ { 0 } ^ { 1 } ( y t ) ( z t ) ^ { 2 } ( x d t ) + ( x t ) ( z t ) ^ { 2 } ( y d t ) + 2 ( x t ) ( y t ) ( z t ) ( z d t ) = x y z ^ { 2 } .
$$

EXAMPLE 9 Why is div curl g¾rad $f$ automa»tic»ally zero (in two ways)?

Solution First, curl grad $f$ is zero (always). Second, div curl $\mathbf { F }$ is zero (always).   
Those are the key identities of ve¾ctor calculus. »W»e end with a review.

$$
\begin{array} { r l r l } { G r e e n ` ~ T h e o r e m : } & { } & { \displaystyle \oint \mathbf { F } \cdot d \mathbf { R } } & { = \displaystyle \iint ( \hat { e } N / \partial x - \hat { e } M / \hat { e } y ) d x ~ d y } \\ { \oint \mathbf { F } \cdot \mathbf { n } d s } & { = \displaystyle \iint ( \hat { e } M / \hat { e } x + \hat { e } N / \hat { e } y ) d x ~ d y } \\ { D i v e r g e n c e ~ T h e o r e m : } & { } & { \displaystyle \iint \mathbf { F } \cdot \mathbf { n } d S } & { = \displaystyle \iint \int ( \hat { e } M / \partial x + \hat { e } N / \partial y + \hat { e } P / \hat { e } z ) d x ~ d y ~ d z } \\ { S t o k e s ^ { \prime } ~ T h e o r e m : } & { } & { \displaystyle \oint \mathbf { F } \cdot d \mathbf { R } } & { = \displaystyle \iint \exp \mathbf { I } . \mathbf { F } \cdot \mathbf { n } d S . } \end{array}
$$

The first form of Green’s Theorem leads to Stokes’ Theorem. The second form becomes the Divergence Theorem. You may ask, why not go to three dimensions in the first place? The last two theorems contain the first two (take $P = 0$ and a flat surface). We could have reduced this chapter to two theorems, not four. I admit that, but a fundamental principle is involved: “It is easier to generalize than to specialize.”

For the same reason $d f / d x$ came before partial derivatives and the gradient.