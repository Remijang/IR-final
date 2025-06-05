# 15.5 The Divergence Theorem

This section returns to the fundamental law $( f l o w o u t ) - ( f l o w i n ) = ( s o u r c e )$ . In two dimensions, the flow was in and out through a closed curve $C$ . The plane region inside was $R$ . In three dimensions, the flow enters and leaves through a closed surface S: The solid region inside is $V .$ Green’s Theorem in its normal form (for the flux of a smooth vector field) now becomes the great three-dimensional balance equation— the Divergence Theorem:

15K The flux of $\mathbf { F } = M \mathbf { i } + N \mathbf { j } + P \mathbf { k }$ through the boundary surface $S$ equals the integral of the divergence of $\mathbf { F }$ inside $V .$ The Divergence Theorem is $\int \int \mathbf { F } \cdot \mathbf { n } d S = \iiint \mathrm { d i v } \mathbf { F } d V = \iiint \left( { \frac { \partial M } { \partial x } } + { \frac { \partial N } { \partial y } } + { \frac { \partial P } { \partial z } } \right) d x d y d z .$ (1)

In Green’s Theorem the divergence was $\hat { \sigma } M / \hat { \sigma } x + \hat { \sigma } N / \hat { \sigma } y$ : The new term ${ \partial P } / { \partial z }$ accounts for upward flow. Notice that a constant upward component $P$ adds nothing to the divergence (its derivative is zero). It also adds nothing to the flux (flow up through the top equals flow up through the bottom). When the whole field $\mathbf { F }$ is constant, the theorem becomes $0 = 0$ :

There are other vector fieldswith div $\mathbf { F } = 0$ : Theyare of the greatest importance. The Divergence Theorem for those fields is again $0 = 0$ ; and there is conservation of fluid. When div $\mathbf { F } = 0$ ; flow in equals flow out. We begin with examples of these “divergence-free” fields.

EXAMPLE 1 The spin fields $- y \mathbf { i } + x \mathbf { j } + 0 \mathbf { k }$ and $0 \mathbf { i } - z \mathbf { j } + y \mathbf { k }$ have zero divergence.

The first is an old friend, spinning around the $z$ axis. The second is new, spinning around the $x$ axis. Three-dimensional flow has a great variety of spin fields. The separate terms $\hat { \sigma } M / \hat { \sigma } x , \hat { \sigma } N / \hat { \sigma } y , \hat { \sigma } P / \hat { \sigma } z$ are all zero, so div $\mathbf { F } = 0$ : The flow goes around in circles, and whatever goes out through $S$ comes back in. (We might have put a circle on $\iint _ { s }$ as we did on $\bar { \oint _ { c } }$ ; to emphasize that $S$ is closed.)

EXAMPLE 2 The position field $\mathbf { R } = x \mathbf { i } + y \mathbf { j } + z \mathbf { k }$ has div $\begin{array} { r } { { \bf R } = 1 + 1 + 1 = 3 . } \end{array}$ :

This is radial flow, straight out from the origin. Mass has to be added at every point to keep the flow going. On the right side of the divergence theorem is $\int \int { 3 d V }$ : Therefore the flux is three times the volume.

Example 11 in Section 15.4 found the flux of $\mathbf { R }$ through acylinder. The answer was $3 \pi b$ : Now we also get $3 \pi b$ from the Divergence Theorem, since the volume is $\pi b$ : This is one of many cases in which the triple integral is easier than the double integral.

# EXAMPLE 3 An electrostatic field $\mathbf { R } / \rho ^ { 3 }$ or gravity field $- \mathbf { R } / \rho ^ { 3 }$ almost has div $\mathbf { F } = 0$ :

The vecBtor $\mathbf { R } = x \mathbf { i } + y \mathbf { j } + z \mathbf { k }$ has lengBth ${ \sqrt { x ^ { 2 } + y ^ { 2 } + z ^ { 2 } } } = \rho$ : Then $\mathbf { F }$ has length $\rho / \rho ^ { 3 }$ (inverse square law). Gravity from a point mass pulls inward (mBinus BsignB). T hBe eBlect rBic field from a point charge repels outward. The three steps almost show that div $\mathbf { F } = 0$ :

Step $1 . \ \partial \rho / \partial x = x / \rho , \ \partial \rho / \partial y = y / \rho , \ \partial \rho / \partial z = z / \rho$ —but do not add those three. $\mathbf { F }$ is not $\rho$ or $1 / \rho ^ { 2 }$ (these are scalars). The vector field is $\mathbf { R } / \rho ^ { 3 }$ : We need $\hat { \sigma } M / \partial x , \hat { \sigma } N / \partial y$ ; ${ \partial P } / { \partial z }$ :

Step 2. $\hat { \mathcal { O } } M / \hat { \mathcal { O } } x = \partial / \partial x ( x / \rho ^ { 3 } )$ is equal to $1 / \rho ^ { 3 } - ( 3 x \partial \rho / \partial x ) / \rho ^ { 4 } = 1 / \rho ^ { 3 } - 3 x ^ { 2 } / \rho ^ { 5 }$ : For $\partial N / \partial y$ and ${ \partial P } / { \partial z }$ ; replace $3 x ^ { 2 }$ by $3 y ^ { 2 }$ and $3 z ^ { 2 }$ : Now add those three.



The calculation div $\mathbf { F } = 0$ leaves a puzzle. One side of the Divergence Theorem seems to give $\iiint 0 d V = 0$ : Then the other side should be $\iint \mathbf { F } \cdot \mathbf { n } d S = 0$ : But the flux is not zero when all flow is outward:

The unit normal vector to the sphere $\rho =$ constant is ${ \bf { n } } = { \bf { R } } / \rho$ : The outward flow $\mathbf { F } \cdot \mathbf { n } = ( \mathbf { R } / \rho ^ { 3 } ) \cdot ( \mathbf { R } / \rho ) = \rho ^ { 2 } / \rho ^ { 4 }$ is always positive. Then $\textstyle \iint \mathbf { F } \cdot \mathbf { n } d S = \iint d S / \rho ^ { 2 } = 4 \pi \rho ^ { 2 } / \rho ^ { 2 } = 4 \pi .$ We have reached $4 \pi =$ 0:

This paradox in three dimensions is the same as for ${ \bf R } / r ^ { 2 }$ in two dimensions. Section 15.3 reached $2 \pi = 0$ ; and the explanation was a point source at the origin. Same explanation here: $M , N , P$ are infinite when $\rho = 0$ : The divergence is a “delta function” times $4 \pi$ ; from the point source. The Divergence Theorem does not apply (unless we allow delta functions). That single point makes all the difference.

Every surface enclosing the origin has flux $= 4 \pi$ : Our calculation was for a sphere. The surface integral is much harder when $S$ is twisted (Figure 15.21a). But the Divergence Theorem takes care of everything, because div $\mathbf { F } = 0$ in the volume $V$ between these surfaces. Therefore $\iint \mathbf { F } \cdot \mathbf { n } d S = 0$ for the two surfaces together. The flux $\iint \mathbf { F } \cdot \mathbf { n } d S = - 4 \pi$ into the sphere must be balanced by $\iint \mathbf { F } \cdot \mathbf { n } d S = 4 \pi$ out of the twisted surface.

Instead of a paradox $4 \pi = 0$ ; this example leads to Gauss’s Law. A mass $M$ at the origin produces a gravity field $\mathbf { F } = - G M \mathbf { R } / \rho ^ { 3 }$ : A charge $q$ at the origin produces an electric field ${ \bf E } = ( q / 4 \pi \varepsilon _ { 0 } ) { \bf R } / \rho ^ { 3 }$ : The physical constants are $G$ and $\scriptstyle { \varepsilon _ { 0 } }$ ; the mathematical constant is the relation between divergence and flux. Equation (1) yields equation (2), in which the mass densities $M ( x , y , z )$ and charge densities $q ( x , y , z )$ need not be concentrated at the origin:

15L Gauss’s law in differential form: div $\mathbf { F } = - 4 \pi G M$ and div ${ \bf E } = \boldsymbol { q } / \varepsilon _ { 0 }$ : Gauss’s law in integral form: Flux is proportional to total mass or charge: $\int \int \mathbf { F } \cdot \mathbf { n } d S = - \iiint 4 \pi G M d V { \mathrm { ~ a n d ~ } } \iint \mathbf { E \cdot n } d S = \iiint q d V / \varepsilon _ { 0 } .$ (2)

# THE REASONING BEHIND THE DIVERGENCE THEOREM

The general principle is clear: Flow out minus flow in equals source. Our goal is to see why the divergence of $\mathbf { F }$ measures the source. Ina small box around each point, we show that div $\mathbf { F } d V$ balances $\mathbf { F } \cdot \mathbf { n } d S$ through the six sides.

So consider a small box. Its center is at $( x , y , z )$ : Its edges have length $\Delta x , \Delta y , \Delta z$ : Out of the top and bottom, the normal vectors are $\mathbf { k }$ and $- \mathbf { k }$ : T Bhe d oBt product with $\mathbf { F } = M \mathbf { i } + N \mathbf { j } + P \mathbf { k }$ is $+ P$ or $- P$ : The area $\Delta S$ is $\Delta x \Delta y$ : So the two fluxes are close to $P ( x , y , z + \textstyle { \frac { 1 } { 2 } } \Delta z ) \Delta x \Delta y$ and $- P ( x , y , z - \textstyle \frac { 1 } { 2 } \Delta z ) \dot { \Delta x } \Delta y$ : When the top is combined with the bottom, the difference of those $P$ ’s is $\Delta P$ :

$$
n e t f u x ~ u p w a r d \approx \Delta P \Delta x \Delta y = ( \Delta P / \Delta z ) \Delta x \Delta y \Delta z \approx ( \partial P / \partial z ) \Delta V .
$$

Similarly, the combined flux on two side faces is approximately $( \partial N / \partial y ) \Delta V$ : On the front and back it is $( { \hat { o } } M / { \hat { o } } x ) \Delta V .$ : Adding the six faces, we reach the key point:

$$
\begin{array} { r } { \iint u x \ : o u t \ : o f t h e \ : b o x \approx ( \partial M / \partial x + \partial N / \partial y + \partial P / \partial z ) \Delta V . } \end{array}
$$

This is $( \operatorname { d i v } \mathbf { F } ) \Delta V .$ : For a constant field both sides are zero—the flow goes straight through. For $\mathbf { F } = x \mathbf { i } + y \mathbf { j } + z \mathbf { k }$ ; a little moreÑgoes out than comes in. The divergence is 3; so $3 \Delta V$ is created inside the box. By the balance equation the flux is also $3 \Delta V .$

The approximation symbol $\approx$ means that the leading term is correct (probably not the next term). The ratio $\Delta P / \Delta z$ is not exactly ${ \partial P / \partial z }$ : The difference is of order $\Delta z$ ; so the error in (3) is of higher order $\Delta V \Delta z$ : Added over many boxes (about $1 / \Delta V$ boxes), this error disappears as $\Delta z  0$ :

The sum of $( \operatorname { d i v } \mathbf { F } ) \Delta V$ over all the boxes approaches $\iiint ( \mathrm { d i v } \mathbf { F } ) d V .$ On the other side of the equation is a sum of fluxes. There is $\mathbf { F } { \cdot } \mathbf { n } \Delta S$ out of the top of one box, plus $\mathbf { F } { \cdot } \mathbf { n } \Delta S$ out of the bottom of the box above. The first has $\mathbf { n } = \mathbf { k }$ and the second has $\mathbf { n } = - \mathbf { k }$ : They cancel each other—the flow goes from box to box. This happens every time two boxes meet. The only fluxes that survive (because nothing cancels them) are at the outer surface $S$ : The final step, as $\Delta x , \Delta y , \Delta z  0$ ; is that those outside terms approach $\iint \mathbf { F } \cdot \mathbf { n } d S$ : Then the local divergence the Borem B(4) becomes the global Divergence Theorem (1).

Remark on the proof That “final step” is not easy, because the box surfaces don’t line up with the outer surface $S$ : A formal proof of the Divergence Theorem would imitate the proof of Green’s Theorem. On a very simple region $\iiint ( \partial P / \partial z ) d x d y d z$ equals $\iint P d x d y$ over the top minus $\iint P d x d y$ over the bottom. After checking the orientation this is $\iint { P \mathbf { k } } \cdot \mathbf { n } d S$ : Similarly the volume integrals of $\partial M / \partial x$ and $\partial N / \partial y$ are the surface integrals $\iint M \mathbf { i } \cdot \mathbf { n } d S$ and $\iint N \mathbf { j } \cdot \mathbf { n } d S$ : Adding the three integrals gives the Divergence Theorem. Since Green’s Theorem was already proved in this way, the reasoning behind (4) is more helpful than repeating a detailed proof.

The discoverer of the Divergence Theorem was probably Gauss. His notebooks only contain the outline of a proof—but after all, this is Gauss. Green and Ostrogradsky both published proofs in 1828; one in England and the other in St. Petersburg (now Leningrad). As the theorem was studied, the requirements came to light (smoothness of $\mathbf { F }$ and $S$ ; avoidance of one-sided Möbius strips).

New applications are discovered all the time—when a scientist writes down a balance equation in a small box. The source is known. The equation is div $\mathbf { F } =$ source. After Example 5 we explain F:

EXAMPLE 4 If the temperature inside the sun is $T = \ln { 1 } / \rho$ ; find the heat flow $\mathbf { F } =$ grad $T$ and the source div $\mathbf { F }$ and the flux $\iint \mathbf { F } \cdot \mathbf { n } d S$ : The sun is a ball of radius $\rho _ { 0 }$ :

Solution» $\mathbf { F }$ i $; - \mathrm { g r a d } \ln 1 / \rho = + \mathrm { g r a d } \ln \rho .$ : Derivatives of $\ln \rho$ bring division by $\rho$ :

$$
\mathbf { F } = ( \hat { \sigma } \rho / \hat { \sigma } x \mathbf { i } + \hat { \sigma } \rho / \hat { \sigma } y \mathbf { j } + \hat { \sigma } \rho / \hat { \sigma } z \mathbf { k } ) / \rho = ( x \mathbf { i } + y \mathbf { j } + z \mathbf { k } ) / \rho ^ { 2 } .
$$

This flow is radially outward, of magnitude $1 / \rho$ : The normal vector $\mathbf { n }$ is also radially outward, of magnitude 1: The dot product on the sun’s surface is $1 / \rho _ { 0 }$ :

$$
\iint \mathbf { F \cdot n } d S = \iint d S / \rho _ { 0 } = ( \mathrm { s u r f a c e \ a r e a } ) / \rho _ { 0 } = 4 \pi \rho _ { 0 } ^ { 2 } / \rho _ { 0 } = 4 \pi \rho _ { 0 } .
$$

Check that answer by the Divergence Theorem. Example 5 will find div $\mathbf { F } = 1 / \rho ^ { 2 }$ : Integrate over the sun. In spherical coordinates we integrate $d \rho$ , sin $\phi d \phi$ ; and $d \theta$ :

$$
\iiint \mathrm { d i v } \mathbf { F } d V = \int _ { 0 } ^ { 2 \pi } \int _ { 0 } ^ { \pi } \int _ { 0 } ^ { \rho _ { 0 } } \rho ^ { 2 } \sin \phi d \rho d \phi d \theta / \rho ^ { 2 } = ( \rho _ { 0 } ) ( 2 ) ( 2 \pi ) \mathrm { a }
$$

This example illustrates the basic framework of equilibrium. The pattern appears everywhere in applied mathematics—electromagnetism, heat flow, elasticity, even relativity. There is usually a constant $c$ that depends on the material (the example has $c = 1$ ). The names change, but we always take the divergence of the gradient:

potential $f $ force field c grad $f .$ Then div. $- c$ grad $f ) =$ electric charge temperature $\mathit { T } \to \mathit { \ f l o w f i e l d - c }$ grad $T .$ : Then div. $- c$ grad $T$ / $\ c =$ heat source displacement u stress field Cc grad $u$ : Then div. $- c$ grad u/ D outside force:

You are studying calculus, not physics or thermodynamics or elasticity. But please notice the main point. The equation to solve is div. $- c$ grad $f ) =$ known source. The divergence and gradient are exactly what the applications need. Calculus teaches the right things.

This framework is developed in many books, including my own text Introduction to Applied Mathematics (Wellesley-Cambridge Press). It governs equilibrium, in matrix equations and differential equations.

# PRODUCT RULE FOR VECTORS: INTEGRATION BY PARTS

May I go back to basic facts about the divergence? First the definition:

$$
\mathbf { F } ( x , y , z ) = M \mathbf { i } + N \mathbf { j } + P \mathbf { k } \operatorname { h a s } \operatorname { d i v } \mathbf { F } = \nabla \cdot \mathbf { F } = \partial M / \partial x + \widehat { \varrho } N / \partial y + \widehat { \varrho } P / \widehat { \varrho } z .
$$

The divergence is a scalar (not a vector). At each point div $\mathbf { F }$ is a number. In fluid flow, it is the rate at which mass leaves—the “flux per unit volume” or “flux density.”

The symbol $\nabla$ stands for aB ve cBtor whoBse c BomponeBnts  aBre operations not numbers:

$$
\nabla = { ^ { \ast } \mathbf { d e l } ^ { \prime \prime } } = \mathbf { i } \hat { \sigma } / \hat { \sigma } x + \mathbf { j } \hat { \sigma } / \hat { \sigma } y + \mathbf { k } \hat { \sigma } / \hat { \sigma } z .
$$

This vector is illegal but very useful. First, apply it to an ordinary function $f ( x , y , z )$ :

$$
\nabla f = { ^ { \ast } \mathbf { d e l } } \ f ^ { \prime \prime } = { \mathbf { i } } \widehat { \partial } f / \widehat { \partial } x + { \mathbf { j } } \widehat { \partial } f / \widehat { \partial } y + { \mathbf { k } } \widehat { \partial } f / \widehat { \partial } z = g r a d i e n t o f \ f .
$$

Second, take the dot product $\nabla \cdot \mathbf { F }$ with a vector function ${ \bf F } ( x , y , z ) = M { \bf i } + N { \bf j } +$ $P \mathbf { k }$ :

$$
\nabla \cdot \mathbf { F } = { ^ { \circ } } { \mathrm { d e l ~ d o t ~ } } \mathbf { F } ^ { \prime \prime } = \partial M / \partial x + \partial N / \partial y + \partial P / \partial z = d i v e r g e n c e ~ o f ~ \mathbf { F } .
$$

Third, take the cross product $\nabla \times \mathbf { F }$ : This produces the vector curl $\mathbf { F }$ (next section):

$$
\nabla \times \mathbf { F } = { \mathfrak { s d e l } } \operatorname { c r o s s } \mathbf { F } ^ { \prime \prime } = { \mathfrak { . . . } } ( { \mathrm { t o ~ b e ~ d e f i n e d } } ) . . . = c u r l o f \mathbf { F } .
$$

The gradient and divergeBnce Band curl Bare $\nabla$ and $\nabla$ B andB $\nabla \times$ : The three great operations of vector calculBus useB a singleB notatBion! YouBare frBee to write $\nabla$ or not—to make equations shorter or to help the memory. Notice that Laplace’s equation shrinks to

$$
\nabla \cdot \nabla f = \frac { \partial } { \partial x } \left( \frac { \partial f } { \partial x } \right) + \frac { \partial } { \partial y } \left( \frac { \partial f } { \partial y } \right) + \frac { \partial } { \partial z } \left( \frac { \partial f } { \partial z } \right) = 0 .
$$

Equation (10) gives the potential when the source is zero (very common). $\mathbf { F } = \operatorname { g r a d } f$ combines with div $\mathbf { F } = 0$ into Laplace’s equation div grad $f = 0$ : This equation is so important that it shrinks further to $\nabla ^ { 2 } { \bar { f } } = 0$ and even to $\Delta f = 0$ : Of course $\Delta f = f _ { x x } + f _ { y y } + f _ { z z }$ has nothing to do with $\Delta f = f ( x + \Delta x ) - f ( x )$ : Above all, remember that $f$ is a scalar and $\mathbf { F }$ is a vector: gradient of scalar is vector and divergence of vector is scalar.

Underlying this chapter is the idea of extending calculus to vectors. So far we have emphasized the Fundamental Theorem. The integral of $d f / d x$ is now the integral of div $\mathbf { F }$ : Instead of endpoints $a$ and $b$ ; we have a curve $C$ or surface $S$ : But it is the rules for derivatives and integrals that make calculus work, and we need them now for vectors. Remember the derivative of $u$ times $v$ and the integral (by parts) of $u d v / d x$ :

15»M» Scalar functions $u ( x , y , z )$ »and vector fields $\mathbf { V } ( x , y , z )$ »o»bey the product rule:

$$
\operatorname { d i v } ( u \mathbf { V } ) = u \operatorname { d i v } \mathbf { V } + \mathbf { V } \cdot ( \operatorname { g r a d } u ) .
$$

The reverse of the product rule is integration by parts (Gauss’s Formula):

$$
\iiint u \mathrm { d i v } \mathbf { V } d x d y d z = - \iiint \mathbf { V } \cdot ( \mathrm { g r a d } u ) d x d y d z + \iiint u \mathbf { V } \cdot \mathbf { n } d S .
$$

For a plane field this is Green’s Formula (and $u = 1$ gives Green’s Theorem):

Those look like heavy formulas. They are too much to memorize, unless you use them often. The important point is to connect vector calculus with “scalar calculus,” which is not heavy. Every product rule yields two terms:

$$
{ } _ { ^ { ( M ) } x } = u \partial M / \partial x + M \partial u / \partial x \quad ( u N ) _ { y } = u \partial N / \partial y + N \partial u / \partial y \quad ( u P ) _ { z } = u \partial P / \partial z + P \partial u / \partial x ,
$$

Add those ordinary rules and you have the vector rule (11) for the divergence of $u \mathbf { V }$ :

Integrating the two parts of $\operatorname { d i v } ( u \mathbf { V } )$ gives $\iint u \mathbf { V } \cdot \mathbf { n } d S$ by the Divergence Theorem. Then one part moves to the other side, producing the minus signs in (12) and (13). Integration by parts leaves a boundary term, in three and two dimensions as it did in one dimension: $\begin{array} { r } { \int u v ^ { \prime } d x = - \int u ^ { \prime } v \dot { d x } + [ u v ] _ { a } ^ { b } } \end{array}$ :

EXAMPLE 5 Find the divergence of ${ \bf F } = { \bf R } / \rho ^ { 2 }$ ; starting from grad ${ \boldsymbol \rho } = { \bf R } / \rho$ :

Solution Take $\mathbf { V } = \mathbf { R }$ and $u = 1 / \rho ^ { 2 }$ in the product rule (11). Then div $\mathbf { F } = ( \operatorname { d i v } \mathbf { R } ) /$ $\rho ^ { 2 } + \mathbf { R } \cdot ( \mathrm { g r a d } 1 / \rho ^ { 2 } )$ . The divergence of $\mathbf { R } = x \mathbf { i } + y \mathbf { j } + z \mathbf { k }$ is 3: For grad $1 / \rho ^ { 2 }$ apply the chain rule:

$$
\mathbf { R \cdot } ( \operatorname { g r a d } 1 / \rho ^ { 2 } ) = - 2 \mathbf { R \cdot } ( \operatorname { g r a d } \rho ) / \rho ^ { 3 } = - 2 \mathbf { R \cdot R } / \rho ^ { 4 } = - 2 / \rho ^ { 2 } .
$$

The two parts of div $\mathbf { F }$ combine into $3 / \rho ^ { 2 } - 2 / \rho ^ { 2 } = 1 / \rho ^ { 2 } .$ —as claimed in Example 4.

EXAMPLE 6 Find the balance equation for flow with velocity $\mathbf { V }$ and fluid density $\rho$ :

$\mathbf { V }$ is the rate of movement of fluid, while $\rho \mathbf { V }$ is the rate of movement of mass. Comparing the ocean to the atmosphere shows the difference. Air has a greater velocity than water, but a much lower density. So normally $\mathbf { F } = \rho \mathbf { V }$ is larger for the ocean. (Don’t confuse the density $\rho$ with the radial distance $\rho$ : The Greeks only used 24 letters.)

There is another difference between water and air. Water is virtually incompressible (meaning $\rho = { \mathrm { c o n s t a n t } } )$ . Air is certainly compreBssib lBe (its density varies). The balance equation is a fundamental law—the conservation of mass or the “continuity equation” for fluids. This is a mathematical statement about a physical floBw w Bithout sources or sinks:

$$
C o n t i n u i t y \ E q u a t i o n \colon \mathrm { d i v } ( \rho \mathbf { V } ) +  { \hat { \sigma } } \rho /  { \hat { \sigma } } t = 0 .
$$

Explanation: The mass in a region is $\iiint \rho d V .$ Its rate of decrease is $- \iiint { \hat { o } } p / { \hat { o } } t d V .$ The decrease comes from flow out through the surface (normal vector $\mathbf { n }$ ). The dot product $\mathbf { F } \cdot \mathbf { n } = \rho \mathbf { V } \cdot \mathbf { n }$ is the rate of mass flow through the surface. So the integral $\iint \mathbf { F } \cdot \mathbf { n } d S$ is the total rate that mass goes out. By the Divergence Theorem this is rrr div $\mathbf { F } d V .$ :

To balance $- \iiint { \hat { o } } \rho / { \hat { o } } t d V$ in every region, div $\mathbf { F }$ must equal $- \partial \rho / \partial t$ at every point. The figure shows this continuity equation (14) for flow in the $x$ direction.

$$
 \begin{array} { r } { { \begin{array} { l } { { \mathbf { m a s s i n } } } \\ { \rho \mathbf { V } d S d t } \end{array} } } \to { \begin{array} { r } { \left[ { \underline { { \mathbf { m a s s } } } } \rho d S d x \right] } \\ { d ( \rho \mathbf { V } ) d S d t } \end{array} } \to { \begin{array} { r } { \mathrm { e x t r a m a s s ~ o u t } } \\ { d ( \rho \mathbf { V } ) d S d t } \end{array} } = { \begin{array} { r } { { \mathbf { m a s s } } \mathbf { l o s s } } \\ { - d \rho d S d x } \end{array} } \end{array}
$$