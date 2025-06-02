# 8.6 Force, Work, and Energy

Chapter 1 introduced derivatives $d f / d t$ and $d f / d x$ : The independent variable could be $t$ or $x$ . For velocity it was natural to use the letter $t$ : This section is about two important physical quantities—force and work—for which $x$ is the right choice.

The basic formula is $W = F x$ : Work equals force times distance moved (distance in the direction of $F$ ). With a force of 100 pounds on a car that moves 20 feet, the work is 2000 foot-pounds. If the car is rolling forward and you are pushing backward, the work is $- 2 0 0 0$ foot-pounds. If your force is only 80 pounds and the car doesn’t move, the work is zero. In these examples the force is constant.

$W = F x$ is completely parallel to $f = v t$ : When $v$ is constant, we only need multiplication. It is a changing velocity that requires calculus. The integral $\int \dot { v } ( t ) d t$ adds up small multiplications over short times. For a changing force, we add up small pieces of work $F d x$ over short distances:

$$
\begin{array} { r }  { \begin{array} { r l r l } { W = F x } & { ( c o n s t a n t f o r c e ) } & & { W = \int F ( x ) d x } & & { ( c h a n g i n g f o r c e ) . } \end{array} } \end{array}
$$

In the first case we lift a suitcase weighing $F = 3 0$ pounds up $x = 2 0$ feet of stairs. The work is $W = 6 0 0$ foot-pounds. The suitcase doesn’t get heavier as we go up—it only seems that way. Actually it gets lighter (we study gravity below).

In the second case we stretch a spring, which needs more force as $x$ increases. Hooke’s law says that $F ( x ) = k x$ : The force is proportional to the stretching distance $x$ . Starting from $x = 0$ ; the work increases with the square of $x$ :

$$
\begin{array} { r } { F = k x \qquad \mathrm { a n d } \qquad W = \int _ { 0 } ^ { x } k x \ d x = \frac 1 2 k x ^ { 2 } . } \end{array}
$$

In metric units the force is measured in Newtons and the distance in meters. The unit of work is a Newton-meter (a joule). The 600 foot-pounds for an American suitcase would have been about 800 joules in France.

EXAMPLE 1 Suppose a force of $F = 2 0$ pounds stretches a spring 1 foot.

(a) Find $k$ : The elastic constant is $k = F / x = 2 0$ pounds per foot. (b) Find $W$ : The work is ${ \scriptstyle { \frac { 1 } { 2 } } } k x ^ { 2 } = { \scriptstyle { \frac { 1 } { 2 } } } \cdot 2 0 \cdot 1 ^ { 2 } = 1 0$ foot-pounds. (c) Find $x$ when $F = - 1 0$ pounds. This is compression not stretching: $\scriptstyle x = - { \frac { 1 } { 2 } }$ foot.

Compressing the same spring through the same distance requires the same work. For compression $x$ and $F$ are negative. But the work $\begin{array} { r } { W = \frac { 1 } { 2 } \bar { k } x ^ { 2 } } \end{array}$ is still positive. Please note that $W$ does not equal $k x$ times $x$ Š That is the whole point of variable force (change $F x$ to $\int F ( x ) d x )$ .

May I add another important quantity from physics ? It comes from looking at the situation from the viewpoint of the spring. In its natural position, the spring rests comfortably. It feels no strain and has no energy. Tension or compression gives it potential energy. More stretching or more compression means more energy. The change in energy equals the work. The potential energy of the suitcase increases by 600 foot-pounds, when it is lifted 20 feet.

Write $V ( x )$ for the potential energy. Here $x$ is the height of the suitcase or the extension of the spring. In moving from $x = a$ to $x = b$ ; $w o r k =$ increase in potential:

$$
\begin{array} { r } { W = \int _ { a } ^ { b } F ( x ) d x = V ( b ) - V ( a ) . } \end{array}
$$

This is absolutely beautiful. The work $W$ is the definite integral. The potential $V$ is the indefinite integral. If we carry the suitcase up the stairs and back down, our total work is zero. We may feel tired, but the trip down should have given back our energy. (It was in the suitcase.) Starting with a spring that is compressed one foot, and ending with the spring extended one foot, again we have done no work. $\scriptstyle V = { \frac { 1 } { 2 } } k x ^ { 2 }$ is the same for $x = - 1$ and $x = 1$ : But an extension from $x = 1$ to $x = 3$ requires work:



$$
\begin{array} { r } { { \cal W } = \operatorname { c h a n g e } \operatorname { i n } V = \frac { 1 } { 2 } k ( 3 ) ^ { 2 } - \frac { 1 } { 2 } k ( 1 ) ^ { 2 } . } \end{array}
$$

Indefinite int8egrals like $V$ come with a property that we know well. They include an arbitrary constant $C$ . The correct potential is not simply ${ \scriptstyle { \frac { 1 } { 2 } } } k x ^ { 2 }$ ; it is ${ \scriptstyle { \frac { 1 } { 2 } } } \dot { k } x ^ { 2 } + C$ : To compute a change in potential, we don’t need $C$ : The constant cancels. But to determine $V$ itself, we have to choose $C$ . By fixing $V = 0$ at one point, the potential is determined at all other points. A common choice is $V = 0$ at $x = 0$ : Sometimes $V = 0$ at $x = \infty$ (for gravity). Electric fields can be “grounded” at any point.

There is another connection between the potential $V$ and the force $F$ : According to (2), $V$ is the indefinite integral of $F$ : Therefore $F ( x )$ is the derivative of $V ( x )$ : The fundamental theorem of calculus is also fundamental to physics:

$$
{ \begin{array} { r l } & { { \mathrm { f o r c e ~ e x e r t e d ~ } } o n { \mathrm { ~ s p r i n g : ~ } } F = \ d V / d x } \\ & { { \mathrm { ~ f o r c e ~ e x e r t e d ~ } } b y { \mathrm { ~ s p r i n g : ~ } } F = - d V / d x } \end{array} }
$$

Those lines say the same thing. One is our force pulling on the spring, the other is the “restoring force” pulling back. (3a) and (3b) are a warning that the sign of $F$ depends on the point of view. Electrical engineers and physicists use the minus sign. In mechanics the plus sign is more common. It is one of the ironies of fate that $F = V ^ { \prime }$ ; while distance and velocity have those letters reversed: $v = f ^ { \prime }$ : Note the change to capital letters and the change to $x$ :

# EXAMPLE 2 Newton’s law of gravitation (inverse square law):

${ \mathrm { ~ f o r c e ~ t o ~ o v e r c o m e ~ g r a v i t y } } = G M m / x ^ { 2 } \qquad { \mathrm { f o r c e ~ e x e r t e d ~ b y ~ g r a v i t y } } = - G M m / x ^ { 2 }$ An engine pushes a rocket forward. Gravity pulls it back. The gravitational constant is $G$ and the Earth’s mass is $M$ : The mass of the rocket or satellite or suitcase is $m$ ; and the potential is the indefinite integral:

$$
\begin{array} { r } { V ( x ) = \int F ( x ) d x = - G M m / x + C . } \end{array}
$$

Usually $C = 0$ ; which makes the potential8zero at $x = \infty$ :

Remark When carrying the suitcase upstairs, $x$ changed by 20 feet. The weight was regarded as constant—which it nearly is. But an exact calculation of work uses the integral of $F ( x )$ ; not just the multiplication 30 times 20: The serious difference comes when the suitcase is carried to $x = \infty$ : With constant force that requires infinite work. With the correct (decreasing) force, the work equals $V$ at infinity (which is zero) minus $V$ at the pickup point $x _ { 0 }$ : The change in $V$ is $W { = } G M m / x _ { 0 }$ :

# KINETIC ENERGY

This optional paragraph carries the physics one step further. Suppose you release the spring or drop the suitcase. The external force changes to $F = 0$ : But the internal force still acts on the spring, and gravity still acts on the suitcase. They both start moving. The potential energy of the suitcase is converted to kinetic energy, until it hits the bottom of the stairs.

Time enters the problem, either through Newton’s law or Einsatein’s:

$$
( N e w t o n ) \ F = m a = m \frac { d v } { d t } ( E i n s t e i n ) \ F = \frac { d } { d t } ( m v ) .
$$

Here we stay with Newton, and pretend the mass is constant. Exercise 21 follows Einstein; the mass increases with velocity. There $m = m _ { 0 } / \sqrt { 1 - v ^ { 2 } / c ^ { 2 } }$ goes to infinity as $v$ approaches $c$ ; the speed of light. That correction comes from the theory of relativity, and is not needed for suit-cases.

What happens as the suitcase falls ? From $x = a$ at the top of the stairs to $x = b$ at the bottom, pot»ential energy is» lost. But kinetic energy $\scriptstyle { \frac { 1 } { 2 } } m v ^ { 2 }$ is gained, as we see from integrating Newton’s law:

$$
{ \begin{array} { r l } & { { \mathrm { ~ f o r c e ~ } } F \ = \ m { \frac { d v } { d t } } = m { \frac { d v } { d x } } { \frac { d x } { d t } } = m v { \frac { d v } { d x } } } \\ & { { \mathrm { ~ w o r k } } \displaystyle \int _ { a } ^ { b } F d x \ = \ \int _ { a } ^ { b } m v { \frac { d v } { d x } } d x = { \frac { 1 } { 2 } } m v ^ { 2 } ( b ) - { \frac { 1 } { 2 } } m v ^ { 2 } ( a ) . } \end{array} }
$$

This same force $F$ is given by $- d V / d x$ : So the work is also the change in $V$ :

$$
\operatorname { w o r k } \int _ { a } ^ { b } F d x = \int _ { a } ^ { b } \left( - { \frac { d V } { d x } } \right) d x = - V ( b ) + V ( a ) .
$$

Since $( 6 ) = ( 7 )$ , the total energy ${ \scriptstyle { \frac { 1 } { 2 } } } m v ^ { 2 } + V$ (kinetic plus potential) is constant:

$$
{ \begin{array} { c } { { \frac { 1 } { 2 } } m v ^ { 2 } ( b ) + V ( b ) = { \frac { 1 } { 2 } } m v ^ { 2 } ( a ) + V ( a ) . } \end{array} }
$$

This is the law of conservation of energy. The total energy is conserved.

EXAMPLE 3 Attach a mass $m$ to the end of a stretched spring and let go. The spring’s energy $\scriptstyle V = { \frac { 1 } { 2 } } k x ^ { 2 }$ is gradually converted to kinetic energy of the mass. At $x = 0$ the change to kinetic energy is complete: the original ${ \scriptstyle { \frac { 1 } { 2 } } } k x ^ { 2 }$ has become ${ \scriptstyle { \frac { 1 } { 2 } } } m v ^ { 2 }$ : Beyond $x = 0$ the potential energy increases, the force reverses sign and pulls back, and kinetic energy is lost. Eventually all energy is potential—when the mass reaches the other extreme. It is simple harmonic motion, exactly as in Chapter 1 (where the mass was the shadow of a circling ball). The equation of motion is the statement that the rate of change of energy is zero (and we cancel $v = d x / d t$ ):

$$
{ \frac { d } { d t } } \left( { \frac { 1 } { 2 } } m v ^ { 2 } + { \frac { 1 } { 2 } } k x ^ { 2 } \right) = m v { \frac { d v } { d t } } + k x { \frac { d x } { d t } } = 0 \quad { \mathrm { o r } } \quad m { \frac { d ^ { 2 } x } { d t ^ { 2 } } } + k x = 0 .
$$

That is $F = m a$ in disguise. For a spring, the solution $x = \cos \sqrt { k / m } t$ will be found in this book. For more complicated structures, engineers spend a billion dollars a year computing the solution.

# PRESSUREAND HYDROSTATIC FORCE

Our forces have been concentrated at a single points. That is not the case for pressure. A fluid exerts a force all over the base and sides of its container. Suppose a water tank or swimming pool has constant depth $h$ (in meters or feet). The water has weight-density $w \approx 9 8 0 0 \mathrm { N / m ^ { 3 } } \approx 6 2 \mathrm { l b / f t ^ { 3 } }$ : On the base, the pressure is $w$ times $h$ : The force is $w h$ times the base area $A$ W

$$
F = w h A { \mathrm { ~ ( p o u n d s ~ o r ~ N e w t o n s ) } } \qquad p = F / A = w h ( \mathrm { l b / f t ^ { 2 } \ o r N / m ^ { 2 } } ) .
$$

Thus pressure is force per unit area. Here $p$ and $F$ are computed by multiplication, because the depth $h$ is constant. Pressure is proportional to depth (as divers know). Down the side wall, $h$ varies and we need calculus.

The pressure on the side is still $w h$ —the same in all directions. We divide the side into horizontal strips of thickness $\Delta h$ . Geometry gives the length $l ( h )$ at depth $h$ (Figure 8.17). The area of a strip is $l ( h ) \Delta h$ : The pressure $w h$ is nearly constant on the strip—the depth only changes by $\Delta h$ : The force on the strip is $\Delta F = w h l \Delta h$ . Adding those forces, and narrowing the strips so that $\Delta h  0$ ; the total force approaches an integral:

$$
\begin{array} { r } { t o t a l f o r c e F = \int \ w h l ( h ) \ d h } \end{array}
$$

EXAMPLE 4 Find the total force on the trapezoidal dam in Figure 8.17.

The side length is $l = 6 0$ when $h = 0$ : The depth $h$ increases from 0 to 20: The main problem is to find $l$ at an in-between depth $h$ : With straight sides the relation is linear: $l = 6 0 + c h$ . We choose $c$ to give $l = 5 0$ when $h = 2 0$ : Then $5 0 = 6 0 + c ( 2 0 )$ yields $\begin{array} { r } { c = - \frac { 1 } { 2 } } \end{array}$ ·

The total force is the integral of $w h l$ : So substitute $l = 6 0 - { \textstyle { \frac { 1 } { 2 } } } h$ :

$$
\begin{array} { r } { F = \int _ { 0 } ^ { 2 0 } w h ( 6 0 - \frac { 1 } { 2 } h ) d h = \Big [ 3 0 w h ^ { 2 } - \frac { 1 } { 6 } w h ^ { 3 } \Big ] _ { 0 } ^ { 2 0 } = 1 2 0 0 0 w - \frac { 1 } { 6 } ( 8 0 0 0 w ) . } \end{array}
$$

With distance in feet and $w = 6 2  \mathrm { l b } / \mathrm { f t } ^ { 3 }$ , $F$ is in pounds. With distance in meters and $w = 9 8 0 0 \mathrm { N } / \mathrm { m } ^ { 3 }$ , the force is in Newtons.

Note that .weight-density $w ) =$ .mass-density $\rho \mathrm { \Phi }$ / times $( g ) = ( 1 0 0 0 ) ($ 9:8/:These SI units were chosen to make the density of water at $0 ^ { \circ } \mathrm { C }$ exactly $\rho = 1 0 0 0 \mathrm { k g } / \mathrm { m } ^ { 3 }$ :

EXAMPLE 5 Find the work to pump water out of a tank. The area at depth $h$ is $A ( h )$ .

Imagine lifting out one layer of water at a time. The layer weighs $w A ( h ) \Delta h$ : The work to lift it to the top is its weight times the distance $h$ ; or $w h A ( h ) \Delta h$ : The work

# 8 Applications of the Integral

to empty the whole tank is theintegral:

$$
\begin{array} { r } { W = \int \ w h A ( h ) \ d h . } \end{array}
$$

Suppose the tank is the bottom half of a sphere of radius $R$ . The cross-sectional area at depth $h$ is $A = \pi ( R ^ { 2 } - h ^ { 2 } )$ : Then the work is the integral (12) from 0 to $R$ : It equals $W = \pi w R ^ { 4 } / 4$ .

Units: $w =$ force=.distance/3 times $R ^ { 4 } = ( \mathrm { d i s t a n c e } ) ^ { 4 }$ gives work $W =$ .force/.distance/.