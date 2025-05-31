# 16.7 Damped Harmonic Motion

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

Compare and discuss underdamped and overdamped oscillating systems.   
• Explain critically damped system.

A guitar string stops oscillating a few seconds after being plucked. To keep a child happy on a swing, you must keep pushing. Although we can often make friction and other non-conservative forces negligibly small, completely undamped motion is rare. In fact, we may even want to damp oscillations, such as with car shock absorbers.

For a system that has a small amount of damping, the period and frequency are nearly the same as for simple harmonic motion, but the amplitude gradually decreases as shown in Figure 16.20. This occurs because the nonconservative damping force removes energy from the system, usually in the form of thermal energy. In general, energy removal by non-conservative forces is described as

$$
W _ { \mathrm { n c } } = \Delta ( \mathrm { K E + P E } ) ,
$$

where $W _ { \mathrm { n c } }$ is work done by a non-conservative force (here the damping force). For a damped harmonic oscillator, $W _ { \mathrm { n c } }$ is negative because it removes mechanical energy $( \mathsf { K E } + \mathsf { P E } )$ from the system.

If you gradually increasethe amount of damping in a system, the period and frequency begin to be affected, because damping opposes and hence slows the back and forth motion. (The net force is smaller in both directions.) If there is very large damping, the system does not even oscillate—it slowly moves toward equilibrium. Figure 16.21 shows the displacement of a harmonic oscillator for different amounts of damping. When we want to damp out oscillations, such as in the suspension of a car, we may want the system to return to equilibrium as quickly as possible Critical damping is defined as the condition in which the damping of an oscillator results in it returning as quickly as possible to its equilibrium position The critically damped system may overshoot the equilibrium position, but if it does, it will do so only once. Critical damping is represented by Curve A in Figure 16.21. With less-than critical damping, the system will return to equilibrium faster but will overshoot and cross over one or more times. Such a system is underdamped; its displacement is represented by the curve in Figure 16.20. Curve B in Figure 16.21 represents an overdamped system. As with critical damping, it too may overshoot the equilibrium position, but will reach equilibrium over a longer period of time.

Critical damping is often desired, because such a system returns to equilibrium rapidly and remains at equilibrium as well. In addition, a constant force applied to a critically damped system moves the system to a new equilibrium position in the shortest time possible without overshooting or oscillating about the new position. For example, when you stand on bathroom scales that have a needle gauge, the needle moves to its equilibrium position without oscillating. It would be quite inconvenient if the needle oscillated about the new equilibrium position for a long time before settling. Damping forces can vary greatly in character. Friction, for example, is sometimes independent of velocity (as assumed in most places in this text). But many damping forces depend on velocity—sometimes in complex ways, sometimes simply being proportional to velocity.

# EXAMPLE 16.7

# Damping an Oscillatory Motion: Friction on an Object Connected to a Spring

Damping oscillatory motion is important in many systems, and the ability to control the damping is even more so. This is generally attained using non-conservative forces such as the friction between surfaces, and viscosity for objects moving through fluids. The following example considers friction. Suppose a $0 . 2 0 0 \mathrm { - } \mathrm { k g }$ object is connected to a spring as shown in Figure 16.22, but there is simple friction between the object and the surface, and the coefficient of friction $\mu _ { k }$ is equal to 0.0800. (a) What is the frictional force between the surfaces? (b) What total distance does the object travel if it is released $0 . 1 0 0 \mathsf { m }$ from equilibrium, starting at $v = 0 ?$ The force constant of the spring is $k = 5 0 . 0 \mathrm { N } / \mathrm { m }$ .

# Strategy

This problem requires you to integrate your knowledge of various concepts regarding waves, oscillations, and damping. To solve an integrated concept problem, you must first identify the physical principles involved. Part (a) is about the frictional force. This is a topic involving the application of Newton’s Laws. Part (b) requires an understanding of work and conservation of energy, as well as some understanding of horizontal oscillatory systems.

Now that we have identified the principles we must apply in order to solve the problems, we need to identify the knowns and unknowns for each part of the question, as well as the quantity that is constant in Part (a) and Part (b) of the question.

# Solution a

1. Choose the proper equation: Friction is $f = \mu _ { \mathrm { k } } m g$ .   
2. Identify the known values.   
3. Enter the known values into the equation:   
$f = ( 0 . 0 8 0 0 ) ( 0 . 2 0 0 \mathrm { k g } ) ( 9 . 8 0 \mathrm { m / s ^ { 2 } } ) .$   
4. Calculate and convert units: $f = 0 . 1 5 7 \ : \mathrm { N }$ ·

# Discussion a

The force here is small because the system and the coefficients are small.

# Solution b

Identify the known:

• The system involves elastic potential energy as the spring compresses and expands, friction that is related to the work done, and the kinetic energy as the body speeds up and slows down.   
• Energy is not conserved as the mass oscillates because friction is a non-conservative force.   
• The motion is horizontal, so gravitational potential energy does not need to be considered.   
• Because the motion starts from rest, the energy in the system is initially $\mathrm { P E _ { e l , i } } = ( 1 / 2 ) k X ^ { 2 }$ . This energy is removed by work done by friction $W _ { \mathrm { n c } } = - \mathop { f d }$ , where $d$ is the total distance traveled and $f = \mu _ { \mathrm { k } } m g$ is the force of friction. When the system stops moving, the friction force will balance the force exerted by the spring, so $\mathrm { P E _ { e l , f } } = ( 1 / 2 ) k x ^ { 2 }$ where $x$ is the final position and is given by

$$
\begin{array} { l l l } { { F _ { \mathrm { { e l } } } } } & { { = } } & { { f } } \\ { { k x } } & { { = } } & { { { \mu _ { \mathrm { { k } } } } m g } } \\ { { x } } & { { = } } & { { { \frac { { \mu _ { \mathrm { { k } } } } m g } { k } } } } \end{array} .
$$

1. By equating the work done to the energy removed, solve for the distance $d$ .

2. The work done by the non-conservative forces equals the initial, stored elastic potential energy. Identify the correct equation to use:

$$
\mathrm { W _ { n c } } = A ( \mathrm { K E + P E } ) \mathrm { = P E _ { \mathrm { e l , f } } - P E _ { \mathrm { e l , i } } } = { \frac { 1 } { 2 } } k \Biggl ( \Bigl ( { \frac { \mu _ { \mathrm { k } } m g } { k } } \Bigr ) ^ { 2 } - X ^ { 2 } \Biggr ) .
$$

3. Recall that $W _ { \mathrm { n c } } = - \mathop { f d }$ .

4. Enter the friction as $f = \mu _ { \mathrm { k } } m g$ into $W _ { \mathrm { n c } } = - \mathop { f d } $ , thus

$$
W _ { \mathrm { n c } } = - \mu _ { \mathrm { k } } m g d .
$$

5. Combine these two equations to find

$$
\frac { 1 } { 2 } k \bigg ( \bigg ( \frac { \mu _ { k } m g } { k } \bigg ) ^ { 2 } - X ^ { 2 } \bigg ) = - \mu _ { \mathrm { k } } m g d .
$$

6. Solve the equation for $d$ :

$$
d = { \frac { k } { 2 \mu _ { \mathrm { k } } m g } } \Biggl ( X ^ { 2 } - \left( { \frac { \mu _ { \mathrm { k } } m g } { k } } \right) ^ { 2 } \Biggr ) .
$$

7. Enter the known values into the resulting equation:

$$
\begin{array} { r } { d = } \\ { \frac { \langle 0 . 0 8 0 0 \rangle \langle 0 . 2 0 0 \mathrm { ~ k g } \rangle \left( 9 . 8 0 \mathrm { ~ m } / \mathrm { s } ^ { 2 } \right) } { 2 \left( 0 . 0 8 0 0 \right) \left( 0 . 2 0 0 \mathrm { ~ k g } \right) \left( 9 . 8 0 \mathrm { ~ m } / \mathrm { s } ^ { 2 } \right) } \left( \left( 0 . 1 0 0 \mathrm { ~ m } \right) ^ { 2 } - \left( \frac { \left( 0 . 0 8 0 0 \right) \left( 0 . 2 0 0 \mathrm { ~ k g } \right) \left( 9 . 8 0 \mathrm { ~ m } / \mathrm { s } ^ { 2 } \right) } { 5 0 . 0 \mathrm { ~ N } / \mathrm { m } } \right) ^ { 2 } \right) . } \end{array}
$$

8. Calculate $d$ and convert units:

$$
d = 1 . 5 9 \mathrm { m } .
$$

# Discussion b

This is the total distance traveled back and forth across $x = 0$ , which is the undamped equilibrium position. The number of oscillations about the equilibrium position will be more than $d / X = ( 1 . 5 9 \mathrm { m } ) / ( 0 . 1 0 0 \mathrm { m } ) = 1 5 . 9$ because the amplitude of the oscillations is decreasing with time. At the end of the motion, this system will not return to $x = 0$ for this type of damping force, because static friction will exceed the restoring force. This system is underdamped. In contrast, an overdamped system with a simple constant damping force would not cross the equilibrium position $x = 0$ a single time. For example, if this system had a damping force 20 times greater, it would only move $0 . 0 4 8 4 \mathrm { m }$ toward the equilibrium position from its original 0.100-m position.

This worked example illustrates how to apply problem-solving strategies to situations that integrate the different concepts you have learned. The first step is to identify the physical principles involved in the problem. The second step is to solve for the unknowns using familiar problem-solving strategies. These are found throughout the text, and many worked examples show how to use them for single topics. In this integrated concepts example, you can see how to apply them across several topics. You will find these techniques useful in applications of physics outside a physics course, such as in your profession, in other science disciplines, and in everyday life.

# CHECK YOUR UNDERSTANDING

Why are completely undamped harmonic oscillators so rare?

# Solution

Friction often comes into play whenever an object is moving. Friction causes damping in a harmonic oscillator.

# CHECK YOUR UNDERSTANDING

Describe the difference between overdamping, underdamping, and critical damping.

# Solution

An overdamped system moves slowly toward equilibrium. An underdamped system moves quickly to equilibrium, but will oscillate about the equilibrium point as it does so. A critically damped system moves as quickly as possible toward equilibrium without oscillating about the equilibrium.