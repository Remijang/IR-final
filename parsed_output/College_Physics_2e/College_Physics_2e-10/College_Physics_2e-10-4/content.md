# 10.4 Rotational Kinetic Energy: Work and Energy Revisited

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

Derive the equation for rotational work.   
• Calculate rotational kinetic energy.   
• Demonstrate the Law of Conservation of Energy.

In this module, we will learn about work and energy associated with rotational motion. Figure 10.13 shows a worker using an electric grindstone propelled by a motor. Sparks are flying, and noise and vibration are created as layers of steel are pared from the pole. The stone continues to turn even after the motor is turned off, but it is eventually brought to a stop by friction. Clearly, the motor had to work to get the stone spinning. This work went into heat, light, sound, vibration, and considerable rotational kinetic energy.

Work must be done to rotate objects such as grindstones or merry-go-rounds. Work was defined in Uniform Circular Motion and Gravitation for translational motion, and we can build on that knowledge when considering work done in rotational motion. The simplest rotational situation is one in which the net force is exerted perpendicular to the radius of a disk (as shown in Figure 10.14) and remains perpendicular as the disk starts to rotate. The force is parallel to the displacement, and so the net work done is the product of the force times the arc length traveled:

To get torque and other rotational quantities into the equation, we multiply and divide the right-hand side of the equation by $r$ , and gather terms:

$$
\mathrm { n e t } \ : W = ( r \ : \mathrm { n e t } \ : F ) \frac { \Delta s } { r } .
$$

We recognize that $r$ net $F =$ net $\tau$ and $\Delta s / r = \theta$ , so that

This equation is the expression for rotational work. It is very similar to the familiar definition of translational work as force multiplied by distance. Here, torque is analogous to force, and angle is analogous to distance. The equation net $W = ( \mathrm { n e t } \tau ) \theta$ is valid in general, even though it was derived for a special case.

To get an expression for rotational kinetic energy, we must again perform some algebraic manipulations. The first step is to note that $\tau = I \alpha$ , so that

# Making Connections

Work and energy in rotational motion are completely analogous to work and energy in translational motion, first presented in Uniform Circular Motion and Gravitation.

Now, we solve one of the rotational kinematics equations for $\alpha \theta$ . We start with the equation

$$
\omega ^ { 2 } = { \omega _ { 0 } } ^ { 2 } + 2 \alpha \theta .
$$

Next, we solve for :

$$
\alpha \theta = \frac { \omega ^ { 2 } - { \omega _ { 0 } } ^ { 2 } } { 2 } .
$$

Substituting this into the equation for net $W$ and gathering terms yields

$$
\mathrm { n e t } W = { \frac { 1 } { 2 } } { I \omega } ^ { 2 } - { \frac { 1 } { 2 } } { I \omega _ { 0 } } ^ { 2 } .
$$

This equation is the work-energy theorem for rotational motion only. As you may recall, net work changes the kinetic energy of a system. Through an analogy with translational motion, we define the term $\scriptstyle \left( { \frac { 1 } { 2 } } \right) I \omega ^ { 2 }$ to be rotational kinetic energy ${ \mathrm { K E } } _ { \mathrm { r o t } }$ for an object with a moment of inertia $I$ and an angular velocity $\omega$ :

$$
\mathrm { K E } _ { \mathrm { r o t } } = { \frac { 1 } { 2 } } I \omega ^ { 2 } .
$$

The expression for rotational kinetic energy is exactly analogous to translational kinetic energy, with $I$ being analogous to $m$ and $\omega$ to $v$ . Rotational kinetic energy has important effects. Flywheels, for example, can be used to store large amounts of rotational kinetic energy in a vehicle, as seen in Figure 10.15.

# EXAMPLE 10.8

# Calculating the Work and Energy for Spinning a Grindstone

Consider a person who spins a large grindstone by placing her hand on its edge and exerting a force through part of a revolution as shown in Figure 10.16. In this example, we verify that the work done by the torque she exerts equals the change in rotational energy. (a) How much work is done if she exerts a force of $2 0 0 ~ \mathsf { N }$ through a rotation of $1 . 0 0 \mathrm { r a d } ( 5 7 . 3 ^ { \circ } ) \ ?$ The force is kept perpendicular to the grindstone’s $0 . 3 2 0 - \mathsf { m }$ radius at the point of application, and the effects of friction are negligible. (b) What is the final angular velocity if the grindstone has a mass of $8 5 . 0 \mathsf { k g ? }$ (c) What is the final rotational kinetic energy? (It should equal the work.)

# Strategy

To find the work, we can use the equation $W = ( \mathrm { n e t } \tau ) \theta$ . We have enough information to calculate the torque and are given the rotation angle. In the second part, we can find the final angular velocity using one of the kinematic relationships. In the last part, we can calculate the rotational kinetic energy from its expression in $\begin{array} { r } { \mathrm { K E } _ { \mathrm { r o t } } = \frac { 1 } { 2 } I \omega ^ { 2 } } \end{array}$ .

# Solution for (a)

The net work is expressed in the equation

$$
\operatorname { r e t } W = ( \operatorname { n e t } \tau ) \theta ,
$$

where net $\tau$ is the applied force multiplied by the radius $( r F )$ because there is no retarding friction, and the force is perpendicular to $r$ . The angle $\theta$ is given. Substituting the given values in the equation above yields

$$
\begin{array} { l l l } { { \mathrm { n e t } ~ W } } & { { = } } & { { r F \theta = ( 0 . 3 2 0 ~ \mathrm { m } ) ( 2 0 0 ~ \mathrm { N } ) ( 1 . 0 0 ~ \mathrm { r a d } ) } } \\ { { } } & { { = } } & { { 6 4 . 0 ~ \mathrm { N } \cdot \mathrm { m } . } } \end{array}
$$

Noting that $1 \mathrm { N } \cdot \mathrm { m } = 1 \mathrm { J }$ ,

# Solution for (b)

To find $\omega$ from the given information requires more than one step. We start with the kinematic relationship in the equation

$$
\omega ^ { 2 } = { \omega _ { 0 } } ^ { 2 } + 2 \alpha \theta .
$$

Note that $\omega _ { 0 } = 0$ because we start from rest. Taking the square root of the resulting equation gives

$$
\omega = ( 2 \alpha \theta ) ^ { 1 / 2 } .
$$

Now we need to find $\alpha$ . One possibility is

$$
\alpha = { \frac { \mathrm { n e t } \tau } { I } } ,
$$

where the torque is

$$
\begin{array} { r } { \operatorname { n e t } \tau = r F { = } ( 0 . 3 2 0 \mathrm { m } ) ( 2 0 0 \mathrm { N } ) { = } 6 4 . 0 \mathrm { N } \cdot \mathrm { m } . } \end{array}
$$

The formula for the moment of inertia for a disk is found in Figure 10.11:

$$
I = { \frac { 1 } { 2 } } M R ^ { 2 } = 0 . 5 ( 8 5 . 0 \mathrm { k g } ) ( 0 . 3 2 0 \mathrm { m } ) ^ { 2 } = 4 . 3 5 2 \mathrm { k g } \cdot \mathrm { m } ^ { 2 } .
$$

Substituting the values of torque and moment of inertia into the expression for $\alpha$ , we obtain

$$
\alpha = { \frac { 6 4 . 0 \mathrm { N } \cdot \mathrm { m } } { 4 . 3 5 2 \mathrm { k g } \cdot \mathrm { m } ^ { 2 } } } = 1 4 . 7 { \frac { \mathrm { r a d } } { \mathrm { s } ^ { 2 } } } .
$$

Now, substitute this value and the given value for $\theta$ into the above expression for $\omega$ :

$$
\omega = ( 2 \alpha \theta ) ^ { 1 / 2 } = \bigg [ 2 \bigg ( 1 4 . 7 \frac { \mathrm { r a d } } { \mathrm { s } ^ { 2 } } \bigg ) ( 1 . 0 0 \mathrm { r a d } ) \bigg ] ^ { 1 / 2 } = 5 . 4 2 \frac { \mathrm { r a d } } { \mathrm { s } } .
$$

# Solution for (c)

The final rotational kinetic energy is

$$
\mathrm { K E } _ { \mathrm { r o t } } = { \frac { 1 } { 2 } } I \omega ^ { 2 } .
$$

Both $I$ and $\omega$ were found above. Thus,

$$
\mathrm { K E } _ { \mathrm { r o t } } = ( 0 . 5 ) \big ( 4 . 3 5 2 \mathrm { k g } \cdot \mathrm { m } ^ { 2 } \big ) ( 5 . 4 2 \mathrm { r a d } / \mathrm { s } ) ^ { 2 } = 6 4 . 0 \mathrm { J } .
$$

# Discussion

The final rotational kinetic energy equals the work done by the torque, which confirms that the work done went into rotational kinetic energy. We could, in fact, have used an expression for energy instead of a kinematic relation to solve part (b). We will do this in later examples.

Helicopter pilots are quite familiar with rotational kinetic energy. They know, for example, that a point of no return will be reached if they allow their blades to slow below a critical angular velocity during flight. The blades lose lift, and it is impossible to immediately get the blades spinning fast enough to regain it. Rotational kinetic energy must be supplied to the blades to get them to rotate faster, and enough energy cannot be supplied in time to avoid a crash. Because of weight limitations, helicopter engines are too small to supply both the energy needed for lift and to replenish the rotational kinetic energy of the blades once they have slowed down. The rotational kinetic energy is put into them before takeoff and must not be allowed to drop below this crucial level. One possible way to avoid a crash is to use the gravitational potential energy of the helicopter to replenish the rotational kinetic energy of the blades by losing altitude and aligning the blades so that the helicopter is spun up in the descent. Of course, if the helicopter’s altitude is too low, then there is insufficient time for the blade to regain lift before reaching the ground.

# Problem-Solving Strategy for Rotational Energy

1. Determinethatenergyorworkisinvolvedintherotation.   
2. Determinethesystemofinterest. A sketch usually helps.   
3. Analyzethesituationtodeterminethetypesofworkandenergyinvolved.   
4. Forclosedsystems,mechanicalenergyisconserved. That is, $\mathrm { K E _ { i } } + \mathrm { P E _ { i } } = \mathrm { K E _ { f } } + \mathrm { P E _ { f } }$ Note that $\mathrm { K E _ { i } }$ and $\mathrm { K E _ { f } }$ may each include translational and rotational contributions.   
5. Foropensystems, mechanical energy may not be conserved, and other forms of energy (referred to previously as $O E )$ ), such as heat transfer, may enter or leave the system. Determine what they are, and calculate them as necessary.   
6. Eliminatetermswhereverpos ibletosimplifythealgebra.   
7. Checktheanswertose ifitisreasonable.

# EXAMPLE 10.9

# Calculating Helicopter Energies

A typical small rescue helicopter, similar to the one in Figure 10.17, has four blades, each is $4 . 0 0 \mathrm { m }$ long and has a mass of $5 0 . 0 \mathsf { k g }$ . The blades can be approximated as thin rods that rotate about one end of an axis perpendicular to their length. The helicopter has a total loaded mass of 1000 kg. (a) Calculate the rotational kinetic energy in the blades when they rotate at 300 rpm. (b) Calculate the translational kinetic energy of the helicopter when it flies at $2 0 . 0 \ : \mathsf { m } / \mathsf { s }$ , and compare it with the rotational energy in the blades. (c) To what height could the helicopter be raised if all of the rotational kinetic energy could be used to lift it?

# Strategy

Rotational and translational kinetic energies can be calculated from their definitions. The last part of the problem relates to the idea that energy can change form, in this case from rotational kinetic energy to gravitational potential energy.

# Solution for (a)

The rotational kinetic energy is

$$
\mathrm { K E } _ { \mathrm { r o t } } = { \frac { 1 } { 2 } } I \omega ^ { 2 } .
$$

We must convert the angular velocity to radians per second and calculate the moment of inertia before we can find $\mathrm { K E } _ { \mathrm { r o t } }$ . The angular velocity $\omega$ is

$$
\omega = \frac { 3 0 0 \mathrm { r e v } } { 1 . 0 0 \mathrm { m i n } } \cdot \frac { 2 \pi \mathrm { r a d } } { 1 \mathrm { r e v } } \cdot \frac { 1 . 0 0 \mathrm { m i n } } { 6 0 . 0 \mathrm { s } } = 3 1 . 4 \frac { \mathrm { r a d } } { \mathrm { s } } .
$$

The moment of inertia of one blade will be that of a thin rod rotated about its end, found in Figure 10.11. The total $I$ is four times this moment of inertia, because there are four blades. Thus,

$$
I = 4 { \frac { M \ell ^ { 2 } } { 3 } } = 4 \times { \frac { ( 5 0 . 0 \mathrm { k g } ) ( 4 . 0 0 \mathrm { m } ) ^ { 2 } } { 3 } } = 1 0 6 7 \mathrm { k g } \cdot \mathrm { m } ^ { 2 } .
$$

Entering $\omega$ and $I$ into the expression for rotational kinetic energy gives

$$
\begin{array} { l l l } { { \mathrm { K E } _ { \mathrm { r o t } } } } & { { = } } & { { 0 . 5 ( 1 0 6 7 \mathrm { k g } \cdot \mathrm { m } ^ { 2 } ) ( 3 1 . 4 \mathrm { r a d } / \mathrm { s } ) ^ { 2 } } } \\ { { } } & { { = } } & { { 5 . 2 6 \times 1 0 ^ { 5 } \mathrm { J } } } \end{array}
$$

# Solution for (b)

Translational kinetic energy was defined in Uniform Circular Motion and Gravitation. Entering the given values of mass and velocity, we obtain

$$
{ \mathrm { K E } } _ { \mathrm { t r a n s } } = { \frac { 1 } { 2 } } m v ^ { 2 } = ( 0 . 5 ) ( 1 0 0 0 { \mathrm { k g } } ) ( 2 0 . 0 { \mathrm { m } } / { \mathrm { s } } ) ^ { 2 } = 2 . 0 0 \times 1 0 ^ { 5 } { \mathrm { J } } .
$$

To compare kinetic energies, we take the ratio of translational kinetic energy to rotational kinetic energy. This ratio is

$$
\frac { 2 . 0 0 \times 1 0 ^ { 5 } \mathrm { ~ J } } { 5 . 2 6 \times 1 0 ^ { 5 } \mathrm { ~ J } } = 0 . 3 8 0 .
$$

# Solution for (c)

At the maximum height, all rotational kinetic energy will have been converted to gravitational energy. To find this height, we equate those two energies:

$$
\mathrm { K E } _ { \mathrm { r o t } } = \mathrm { P E } _ { \mathrm { g r a v } }
$$

or

$$
{ \frac { 1 } { 2 } } I \omega ^ { 2 } = m g h .
$$

We now solve for $h$ and substitute known values into the resulting equation

$$
h = { \frac { { \frac { 1 } { 2 } } I { \omega } ^ { 2 } } { m g } } = { \frac { 5 . 2 6 \times 1 0 ^ { 5 } { \mathrm { ~ J } } } { ( 1 0 0 0 { \mathrm { ~ k g } } ) { \left( 9 . 8 0 { \mathrm { ~ m / s } } ^ { 2 } \right) } } } = 5 3 . 7 { \mathrm { ~ m } } .
$$

# Discussion

The ratio of translational energy to rotational kinetic energy is only 0.380. This ratio tells us that most of the kinetic energy of the helicopter is in its spinning blades—something you probably would not suspect. The $5 3 . 7 \mathrm { m }$ height to which the helicopter could be raised with the rotational kinetic energy is also impressive, again emphasizing the amount of rotational kinetic energy in the blades.

# Making Connections

Conservation of energy includes rotational motion, because rotational kinetic energy is another form of .   
Uniform Circular Motion and Gravitation has a detailed treatment of conservation of energy.

# How Thick Is the Soup? Or Why Don’t All Objects Roll Downhill at the Same Rate?

One of the quality controls in a tomato soup factory consists of rolling filled cans down a ramp. If they roll too fast, the soup is too thin. Why should cans of identical size and mass roll down an incline at different rates? And why should the thickest soup roll the slowest?

The easiest way to answer these questions is to consider energy. Suppose each can starts down the ramp from rest. Each can starting from rest means each starts with the same gravitational potential energy , which is converted entirely to , provided each rolls without slipping. , however, can take the form of ${ \mathrm { K E } } _ { \mathrm { t r a n s } }$ or $\mathrm { K E } _ { \mathrm { r o t } }$ , and total is the sum of the two. If a can rolls down a ramp, it puts part of its energy into rotation, leaving less for translation. Thus, the can goes slower than it would if it slid down. Furthermore, the thin soup does not rotate, whereas the thick soup does, because it sticks to the can. The thick soup thus puts more of the can’s original gravitational potential energy into rotation than the thin soup, and the can rolls more slowly, as seen in Figure 10.18.

Assuming no losses due to friction, there is only one force doing work—gravity. Therefore the total work done is the change in kinetic energy. As the cans start moving, the potential energy is changing into kinetic energy. Conservation of energy gives

$$
\mathrm { P E _ { i } = K E _ { f } } .
$$

More specifically,

$$
\mathrm { P E } _ { \mathrm { g r a v } } = \mathrm { K E } _ { \mathrm { t r a n s } } + \mathrm { K E } _ { \mathrm { r o t } }
$$

or

$$
m g h = { \frac { 1 } { 2 } } m v ^ { 2 } + { \frac { 1 } { 2 } } I \omega ^ { 2 } .
$$

So, the initial is divided between translational kinetic energy and rotational kinetic energy; and the greater $I$ is, the less energy goes into translation. If the can slides down without friction, then $\omega = 0$ and all the energy goes into translation; thus, the can goes faster.

# Take-Home Experiment

Locate several cans each containing different types of food. First, predict which can will win the race down an inclined plane and explain why. See if your prediction is correct. You could also do this experiment by collecting several empty cylindrical containers of the same size and filling them with different materials such as wet or dry sand.

# EXAMPLE 10.10

# Calculating the Speed of a Cylinder Rolling Down an Incline

Calculate the final speed of a solid cylinder that rolls down a $2 . 0 0 \cdot \mathsf { m }$ -high incline. The cylinder starts from rest, has a mass of $0 . 7 5 0 \ k \ g ,$ , and has a radius of $4 . 0 0 ~ \mathsf { c m }$ .

# Strategy

We can solve for the final velocity using conservation of energy, but we must first express rotational quantities in terms of translational quantities to end up with $v$ as the only unknown.

# Solution

Conservation of energy for this situation is written as described above:

$$
m g h = { \frac { 1 } { 2 } } m v ^ { 2 } + { \frac { 1 } { 2 } } I \omega ^ { 2 } .
$$

Before we can solve for $v$ , we must get an expression for $I$ from Figure 10.11. Because $v$ and $\omega$ are related (note here that the cylinder is rolling without slipping), we must also substitute the relationship $\omega = v / R$ into the expression. These substitutions yield

$$
m g h = \frac { 1 } { 2 } m v ^ { 2 } + \frac { 1 } { 2 } \left( \frac { 1 } { 2 } m R ^ { 2 } \right) \left( \frac { v ^ { 2 } } { R ^ { 2 } } \right) .
$$

Interestingly, the cylinder’s radius $R$ and mass $m$ cancel, yielding

$$
g h = { \frac { 1 } { 2 } } v ^ { 2 } + { \frac { 1 } { 4 } } v ^ { 2 } = { \frac { 3 } { 4 } } v ^ { 2 } .
$$

Solving algebraically, the equation for the final velocity $v$ gives

$$
v = \left( \frac { 4 g h } { 3 } \right) ^ { 1 / 2 } .
$$

Substituting known values into the resulting expression yields

$$
v = \left[ { \frac { 4 \left( 9 . 8 0 \mathrm { m / s ^ { 2 } } \right) \left( 2 . 0 0 \mathrm { m } \right) } { 3 } } \right] ^ { 1 / 2 } = 5 . 1 1 \mathrm { m / s } .
$$

# Discussion

Because $m$ and $R$ cancel, the result $v = \left( { \textstyle { \frac { 4 } { 3 } } g h } \right) ^ { 1 / 2 }$ is valid for any solid cylinder, implying that all solid cylinders will roll down an incline at the same rate independent of their masses and sizes. (Rolling cylinders down inclines is what Galileo actually did to show that objects fall at the same rate independent of mass.) Note that if the cylinder slid without friction down the incline without rolling, then the entire gravitational potential energy would go into translational kinetic energy. Thus, ${ \frac { 1 } { 2 } } m v ^ { 2 } = m g h$ and $v = ( 2 g h ) ^ { 1 / 2 }$ , which is $2 2 \%$ greater than $( 4 g h / 3 ) ^ { 1 / 2 }$ . That is, the cylinder would go faster at the bottom.

# CHECK YOUR UNDERSTANDING

Analogy of Rotational and Translational Kinetic Energy Is rotational kinetic energy completely analogous to translational kinetic energy? What, if any, are their differences? Give an example of each type of kinetic energy.

# Solution

Yes, rotational and translational kinetic energy are exact analogs. They both are the energy of motion involved with the coordinated (non-random) movement of mass relative to some reference frame. The only difference between rotational and translational kinetic energy is that translational is straight line motion while rotational is not. An

example of both kinetic and translational kinetic energy is found in a bike tire while being ridden down a bike path. The rotational motion of the tire means it has rotational kinetic energy while the movement of the bike along the path means the tire also has translational kinetic energy. If you were to lift the front wheel of the bike and spin it while the bike is stationary, then the wheel would have only rotational kinetic energy relative to the Earth.