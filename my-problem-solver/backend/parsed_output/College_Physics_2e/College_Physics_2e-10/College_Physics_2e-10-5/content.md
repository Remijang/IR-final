# 10.5 Angular Momentum and Its Conservation

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

Understand the analogy between angular momentum and linear momentum.   
• Observe the relationship between torque and angular momentum.   
• Apply the law of conservation of angular momentum.

Why does Earth keep on spinning? What started it spinning to begin with? And how does an ice skater manage to spin faster and faster simply by pulling her arms in? Why does she not have to exert a torque to spin faster? Questions like these have answers based in angular momentum, the rotational analog to linear momentum.

By now the pattern is clear—every rotational phenomenon has a direct translational analog. It seems quite reasonable, then, to define angular momentum $L$ as

$$
L = I { \omega } .
$$

This equation is an analog to the definition of linear momentum as $p = m v$ . Units for linear momentum are $\mathrm { { k g } \cdot \mathrm { { m } / \mathrm { { s } } } }$ while units for angular momentum are $\mathrm { k g } \cdot \mathrm { m } ^ { 2 } / \mathrm { s }$ . As we would expect, an object that has a large moment of inertia $I$ , such as Earth, has a very large angular momentum. An object that has a large angular velocity $\omega$ , such as a centrifuge, also has a rather large angular momentum.

# Making Connections

Angular momentum is completely analogous to linear momentum, first presented in Uniform Circular Motion and Gravitation. It has the same implications in terms of carrying rotation forward, and it is conserved when the net external torque is zero. Angular momentum, like linear momentum, is also a property of the atoms and subatomic particles.

# EXAMPLE 10.11

# Calculating Angular Momentum of the Earth Strategy

No information is given in the statement of the problem; so we must look up pertinent data before we can calculate $L = I { \omega }$ . First, according to Figure 10.11, the formula for the moment of inertia of a sphere is

$$
I = { \frac { 2 M R ^ { 2 } } { 5 } }
$$

so that

$$
L = I \omega = { \frac { 2 M R ^ { 2 } \omega } { 5 } } .
$$

Earth’s mass $M$ is $5 . 9 7 9 \times 1 0 ^ { 2 4 } ~ \mathrm { k g }$ and its radius $R$ is $6 . 3 7 6 \times 1 0 ^ { 6 } \mathrm { ~ m ~ }$ . The Earth’s angular velocity $\omega$ is, of course, exactly one revolution per day, but we must covert $\omega$ to radians per second to do the calculation in SI units.

# Solution

Substituting known information into the expression for $L$ and converting $\omega$ to radians per second gives

$$
{ \begin{array} { r c l } { L } & { = } & { 0 . 4 { \left( 5 . 9 7 9 \times 1 0 ^ { 2 4 } \mathrm { ~ k g } \right) } { \left( 6 . 3 7 6 \times 1 0 ^ { 6 } \mathrm { ~ m } \right) } ^ { 2 } { \left( { \frac { \mathrm { 1 ~ r e v } } { \mathrm { ~ d } } } \right) } } \\ & { = } & { 9 . 7 2 \times 1 0 ^ { 3 7 } \mathrm { ~ k g } \cdot \mathrm { m } ^ { 2 } \cdot \mathrm { r e v } / \mathrm { d } . } \end{array} }
$$

Substituting $2 \pi$ rad for rev and $8 . 6 4 \times 1 0 ^ { 4 }$ for 1 day gives

$$
{ \begin{array} { r c l } { L } & { = } & { \left( 9 . 7 2 \times 1 0 ^ { 3 7 } \ \mathrm { k g } \cdot \mathrm { m } ^ { 2 } \right) \left( { \frac { 2 \pi { \mathrm { r a d } } / \mathrm { r e v } } { 8 . 6 4 \times 1 0 ^ { 4 } \ \mathrm { s } / \mathrm { d } } } \right) \left( 1 \ \mathrm { r e v } / \mathrm { d } \right) } \\ & { = } & { 7 . 0 7 \times 1 0 ^ { 3 3 } \ \mathrm { k g } \cdot \mathrm { m } ^ { 2 } / \mathrm { s } . } \end{array} }
$$

# Discussion

This number is large, demonstrating that Earth, as expected, has a tremendous angular momentum. The answer is approximate, because we have assumed a constant density for Earth in order to estimate its moment of inertia.

When you push a merry-go-round, spin a bike wheel, or open a door, you exert a torque. If the torque you exert is greater than opposing torques, then the rotation accelerates, and angular momentum increases. The greater the net torque, the more rapid the increase in $L$ . The relationship between torque and angular momentum is

$$
{ \mathrm { n e t } } \tau = { \frac { \Delta L } { \Delta t } } .
$$

This expression is exactly analogous to the relationship between force and linear momentum, $F = \Delta p / \Delta t$ . The equation $\begin{array} { r } { \tau = \frac { \Delta L } { \Delta t } } \end{array}$ is very fundamental and broadly applicable. It is, in fact, the rotational form of Newton’s second law.

# EXAMPLE 10.12

# Calculating the Torque Putting Angular Momentum Into a Rotating Food Tray

Figure 10.19 shows a rotating food tray, often called a lazy Susan, being turned by a person in quest of sustenance. Suppose the person exerts a $2 . 5 0 \mathsf { N }$ force perpendicular to the lazy Susan’s $0 . 2 6 0 – \mathsf { m }$ radius for 0.150 s. (a) What is the final angular momentum of the lazy Susan if it starts from rest, assuming friction is negligible? (b) What is the final angular velocity of the lazy Susan, given that its mass is $4 . 0 0 \ k \ g$ and assuming its moment of inertia is that of a disk?

# Strategy

We can find the angular momentum by solving $\begin{array} { r } { \tau = \frac { \Delta L } { \Delta t } } \end{array}$ for $\Delta L$ , and using the given information to calculate the torque. The final angular momentum equals the change in angular momentum, because the lazy Susan starts from rest. That is, $\Delta L = L$ . To find the final velocity, we must calculate $\omega$ from the definition of $L$ in $L = I { \omega }$ .

# Solution for (a)

Solving $\begin{array} { r } { \tau = \frac { \Delta L } { \Delta t } } \end{array}$ for gives

$$
\Delta L = ( \mathrm { n e t } \tau ) \Delta \mathrm { t } .
$$

Because the force is perpendicular to $r$ , we see that ${ \boldsymbol { \tau } } = r { \boldsymbol { F } }$ , so that

$$
\begin{array} { l c l } { { L } } & { { = } } & { { \mathrm { r F } \Delta t = \displaystyle ( 0 . 2 6 0 ~ \mathrm { m } ) ( 2 . 5 0 ~ \mathrm { N } ) ( 0 . 1 5 0 ~ \mathrm { s } ) } } \\ { { } } & { { = } } & { { 9 . 7 5 \times 1 0 ^ { - 2 } ~ \mathrm { k g } \cdot \mathrm { m } ^ { 2 } / \mathrm { s } . } } \end{array}
$$

# Solution for (b)

The final angular velocity can be calculated from the definition of angular momentum,

$$
L = I { \boldsymbol { \omega } } .
$$

Solving for $\omega$ and substituting the formula for the moment of inertia of a disk into the resulting equation gives

$$
\omega = { \frac { L } { I } } = { \frac { L } { { \frac { 1 } { 2 } } M R ^ { 2 } } } .
$$

And substituting known values into the preceding equation yields

$$
\omega = { \frac { 9 . 7 5 \times 1 0 ^ { - 2 } \ { \mathrm { k g } } \cdot { \mathrm { m } } ^ { 2 } / { \mathrm { s } } } { ( 0 . 5 0 0 ) ( 4 . 0 0 \ { \mathrm { k g } } ) ( 0 . 2 6 0 \ { \mathrm { m } } ) ^ { 2 } } } = 0 . 7 2 1 \ { \mathrm { r a d / s } } .
$$

# Discussion

Note that the imparted angular momentum does not depend on any property of the object but only on torque and time. The final angular velocity is equivalent to one revolution in 8.71 s (determination of the time period is left as an exercise for the reader), which is about right for a lazy Susan.

# EXAMPLE 10.13

# Calculating the Torque in a Kick

The person whose leg is shown in Figure 10.20 kicks his leg by exerting a 2000-N force with his upper leg muscle. The effective perpendicular lever arm is $2 . 2 0 \mathsf { c m }$ . Given the moment of inertia of the lower leg is $1 . 2 5 \mathrm { k g } \cdot \mathrm { m } ^ { 2 }$ , (a) find the angular acceleration of the leg. (b) Neglecting the gravitational force, what is the rotational kinetic energy of the leg after it has rotated through $5 7 . 3 ^ { \circ }$ (1.00 rad)?

# Strategy

The angular acceleration can be found using the rotational analog to Newton’s second law, or $\alpha = \mathrm { n e t } \tau / I$ . The moment of inertia $I$ is given and the torque can be found easily from the given force and perpendicular lever arm. Once the angular acceleration $\alpha$ is known, the final angular velocity and rotational kinetic energy can be calculated.

# Solution to (a)

From the rotational analog to Newton’s second law, the angular acceleration $\alpha$ is

$$
\alpha = { \frac { \mathrm { n e t } \tau } { I } } .
$$

Because the force and the perpendicular lever arm are given and the leg is vertical so that its weight does not create a torque, the net torque is thus

$$
{ \begin{array} { l l l } { \operatorname { n e t } \tau } & { = } & { r _ { \perp } F } \\ & { = } & { ( 0 . 0 2 2 0 \operatorname { m } ) ( 2 0 0 0 \operatorname { N } ) } \\ & { = } & { 4 4 . 0 \operatorname { N } \cdot \operatorname { m } . } \end{array} }
$$

Substituting this value for the torque and the given value for the moment of inertia into the expression for $\alpha$ gives

$$
\alpha = { \frac { 4 4 . 0 \mathrm { N } \cdot \mathrm { m } } { 1 . 2 5 \mathrm { k g } \cdot \mathrm { m } ^ { 2 } } } = 3 5 . 2 \mathrm { r a d } / \mathrm { s } ^ { 2 } .
$$

# Solution to (b)

The final angular velocity can be calculated from the kinematic expression

$$
\omega ^ { 2 } = { \omega _ { 0 } } ^ { 2 } + 2 \alpha \theta
$$

or

$$
\omega ^ { 2 } = 2 \alpha \theta
$$

because the initial angular velocity is zero. The kinetic energy of rotation is

$$
\mathrm { K E } _ { \mathrm { r o t } } = { \frac { 1 } { 2 } } I \omega ^ { 2 }
$$

so it is most convenient to use the value of $\omega ^ { 2 }$ just found and the given value for the moment of inertia. The kinetic energy is then

$$
\begin{array} { l l l } { { \mathrm { K E } _ { \mathrm { r o t } } } } & { { = } } & { { 0 . 5 \left( 1 . 2 5 \mathrm { k g } \cdot \mathrm { m } ^ { 2 } \right) \left( 7 0 . 4 \mathrm { r a d } ^ { 2 } / \mathrm { s } ^ { 2 } \right) } } \\ { { } } & { { = } } & { { 4 4 . 0 \mathrm { J } } } \end{array} .
$$

# Discussion

These values are reasonable for a person kicking his leg starting from the position shown. The weight of the leg can be neglected in part (a) because it exerts no torque when the center of gravity of the lower leg is directly beneath the pivot in the knee. In part (b), the force exerted by the upper leg is so large that its torque is much greater than that created by the weight of the lower leg as it rotates. The rotational kinetic energy given to the lower leg is enough that it could give a ball a significant velocity by transferring some of this energy in a kick.

# Making Connections: Conservation Laws

Angular momentum, like energy and linear momentum, is conserved. This universally applicable law is another sign of underlying unity in physical laws. Angular momentum is conserved when net external torque is zero, just as linear momentum is conserved when the net external force is zero.

# Conservation of Angular Momentum

We can now understand why Earth keeps on spinning. As we saw in the previous example, $\Delta L = ( \mathrm { n e t } \ \tau ) \Delta t .$ . This equation means that, to change angular momentum, a torque must act over some period of time. Because Earth has a large angular momentum, a large torque acting over a long time is needed to change its rate of spin. So what external torques are there? Tidal friction exerts torque that is slowing Earth’s rotation, but tens of millions of years must pass before the change is very significant. Recent research indicates the length of the day was $1 8 { \mathsf { h } }$ some 900 million years ago. Only the tides exert significant retarding torques on Earth, and so it will continue to spin, although ever more slowly, for many billions of years.

What we have here is, in fact, another conservation law. If the net torque is zero, then angular momentum is constant or conserved. We can see this rigorously by considering $\begin{array} { r } { \tau = \frac { \Delta L } { \Delta t } } \end{array}$ for the situation in which the net torque is zero. In that case,

$$
\mathrm { n e t } \tau = 0
$$

implying that

$$
\frac { \Delta L } { \Delta t } = 0 .
$$

If the change in angular momentum $\Delta L$ is zero, then the angular momentum is constant; thus,

$$
L = { \mathrm { c o n s t a n t } } \left( { \mathrm { n e t } } \tau = 0 \right)
$$

or

$$
L = L ^ { \prime } ( \mathrm { n e t } \tau = 0 ) .
$$

These expressions are the law of conservation of angular momentum. Conservation laws are as scarce as they are important.

An example of conservation of angular momentum is seen in Figure 10.21, in which an ice skater is executing a spin. The net torque on her is very close to zero, because there is relatively little friction between her skates and the ice and because the friction is exerted very close to the pivot point. (Both $F$ and $r$ are small, and so $\tau$ is negligibly small.) Consequently, she can spin for quite some time. She can do something else, too. She can increase her rate of spin by pulling her arms and legs in. Why does pulling her arms and legs in increase her rate of spin? The answer is that her angular momentum is constant, so that

$$
L = L ^ { \prime } .
$$

Expressing this equation in terms of the moment of inertia,

$$
I \omega = I ^ { \prime } \omega ^ { \prime } ,
$$

where the primed quantities refer to conditions after she has pulled in her arms and reduced her moment of inertia. Because $I ^ { \prime }$ is smaller, the angular velocity $\omega ^ { \prime }$ must increase to keep the angular momentum constant. The change can be dramatic, as the following example shows.

# EXAMPLE 10.14

# Calculating the Angular Momentum of a Spinning Skater

Suppose an ice skater, such as the one in Figure 10.21, is spinning at 0.800 rev/ s with her arms extended. She has a moment of inertia of $2 . 3 4 \mathrm { k g } \cdot \mathrm { m } ^ { 2 }$ with her arms extended and of $0 . 3 6 3 \mathrm { k g } \cdot \mathrm { m } ^ { 2 }$ with her arms close to her body. (These moments of inertia are based on reasonable assumptions about a $6 0 . 0 \substack { - \ k \ g }$ skater.) (a) What is her angular velocity in revolutions per second after she pulls in her arms? (b) What is her rotational kinetic energy before and after she does this?

# Strategy

In the first part of the problem, we are looking for the skater’s angular velocity $\omega ^ { \prime }$ after she has pulled in her arms. To find this quantity, we use the conservation of angular momentum and note that the moments of inertia and initial angular velocity are given. To find the initial and final kinetic energies, we use the definition of rotational kinetic energy given by

$$
\mathrm { K E } _ { \mathrm { r o t } } = { \frac { 1 } { 2 } } I \omega ^ { 2 } .
$$

# Solution for (a)

Because torque is negligible (as discussed above), the conservation of angular momentum given in ${ \cal I } \omega = { \cal I } ^ { \prime } \omega ^ { \prime }$ is applicable. Thus,

$$
L = L ^ { \prime }
$$

or

$$
{ \cal I } \omega = { \cal I } ^ { \prime } \omega ^ { \prime }
$$

Solving for $\omega ^ { \prime }$ and substituting known values into the resulting equation gives

$$
{ \begin{array} { l l l } { { \omega ^ { \prime } } } & { = } & { { \frac { I } { I ^ { \prime } } } \omega = \left( { \frac { 2 . 3 4 \mathrm { k g } \cdot \mathrm { m } ^ { 2 } } { 0 . 3 6 3 \mathrm { k g } \cdot \mathrm { m } ^ { 2 } } } \right) \left( 0 . 8 0 0 \mathrm { r e v / s } \right) } \\ & { = } & { 5 . 1 6 \mathrm { r e v / s } . } \end{array} }
$$

# Solution for (b)

Rotational kinetic energy is given by

$$
\mathrm { K E } _ { \mathrm { r o t } } = { \frac { 1 } { 2 } } I \omega ^ { 2 } .
$$

The initial value is found by substituting known values into the equation and converting the angular velocity to $\mathsf { r a d } / \mathsf { s }$

$$
\begin{array} { l l l } { { \mathrm { K E } _ { \mathrm { r o t } } } } & { { = } } & { { ( 0 . 5 ) \bigl ( 2 . 3 4 \mathrm { k g } \cdot \mathrm { m } ^ { 2 } \bigr ) ( ( 0 . 8 0 0 \mathrm { r e v } / \mathrm { s } ) ( 2 \pi \mathrm { r a d } / \mathrm { r e v } ) ) ^ { 2 } } } \\ { { } } & { { = } } & { { 2 9 . 6 \mathrm { J } . } } \end{array}
$$

The final rotational kinetic energy is

$$
\mathrm { K E } _ { \mathrm { r o t } ^ { ' } } = \frac { 1 } { 2 } { I ^ { \prime } \omega ^ { \prime } } ^ { 2 } .
$$

Substituting known values into this equation gives

$$
\begin{array} { l l l } { { K E _ { \mathrm { r o t } } } ^ { \prime } ~ = } & { ( 0 . 5 ) \big ( 0 . 3 6 3 \mathrm { k g } \cdot \mathrm { m } ^ { 2 } \big ) [ ( 5 . 1 6 \mathrm { r e v } / \mathrm { s } ) ( 2 \pi \mathrm { r a d } / \mathrm { r e v } ) ] ^ { 2 } } \\ { ~ } & { = } & { 1 9 1 \mathrm { J } . } \end{array}
$$

# Discussion

In both parts, there is an impressive increase. First, the final angular velocity is large, although most world-class skaters can achieve spin rates about this great. Second, the final kinetic energy is much greater than the initial kinetic energy. The increase in rotational kinetic energy comes from work done by the skater in pulling in her arms. This work is internal work that depletes some of the skater’s food energy.

There are several other examples of objects that increase their rate of spin because something reduced their moment of inertia. Tornadoes are one example. Storm systems that create tornadoes are slowly rotating. When the radius of rotation narrows, even in a local region, angular velocity increases, sometimes to the furious level of a tornado. Earth is another example. Our planet was born from a huge cloud of gas and dust, the rotation of which came from turbulence in an even larger cloud. Gravitational forces caused the cloud to contract, and the rotation rate increased as a result. (See Figure 10.22.)

In case of human motion, one would not expect angular momentum to be conserved when a body interacts with the environment as its foot pushes off the ground. Astronauts floating in space aboard the International Space Station have no angular momentum relative to the inside of the ship if they are motionless. Their bodies will continue to have this zero value no matter how they twist about as long as they do not give themselves a push off the side of the vessel.

# CHECK YOUR UNDERSTANDING

Is angular momentum completely analogous to linear momentum? What, if any, are their differences?

# Solution

Yes, angular and linear momentums are completely analogous. While they are exact analogs they have different units and are not directly inter-convertible like forms of energy are.