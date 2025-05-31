# 16.5 Energy and the Simple Harmonic Oscillator

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

Determine the maximum speed of an oscillating system.

To study the energy of a simple harmonic oscillator, we first consider all the forms of energy it can have We know from Hooke’s Law: Stress and Strain Revisited that the energy stored in the deformation of a simple harmonic oscillator is a form of potential energy given by:

$$
\mathrm { P E _ { \mathrm { e l } } } = { \frac { 1 } { 2 } } k x ^ { 2 } .
$$

Because a simple harmonic oscillator has no dissipative forces, the other important form of energy is kinetic energy . Conservation of energy for these two forms is:

$$
\mathrm { K E + P E _ { \mathrm { e l } } = \mathrm { c o n s t a n t } }
$$

or

$$
{ \frac { 1 } { 2 } } m v ^ { 2 } + { \frac { 1 } { 2 } } k x ^ { 2 } = \mathrm { c o n s t a n t } .
$$

This statement of conservation of energy is valid for al simple harmonic oscillators, including ones where the gravitational force plays a role

Namely, for a simple pendulum we replace the velocity with $v = L \omega$ , the spring constant with $k = m g / L$ , and the displacement term with $x = L \theta$ . Thus

$$
{ \frac { 1 } { 2 } } m L ^ { 2 } \omega ^ { 2 } + { \frac { 1 } { 2 } } m g L \theta ^ { 2 } = \mathrm { c o n s t a n t } .
$$

In the case of undamped simple harmonic motion, the energy oscillates back and forth between kinetic and potential, going completely from one to the other as the system oscillates. So for the simple example of an object on a frictionless surface attached to a spring, as shown again in Figure 16.14, the motion starts with all of the energy stored in the spring. As the object starts to move, the elastic potential energy is converted to kinetic energy, becoming entirely kinetic energy at the equilibrium position. It is then converted back into elastic potential energy by the spring, the velocity becomes zero when the kinetic energy is completely converted, and so on. This concept provides extra insight here and in later applications of simple harmonic motion, such as alternating current circuits.

The conservation of energy principle can be used to derive an expression for velocity $v$ . If we start our simple harmonic motion with zero velocity and maximum displacement $( x = X )$ , then the total energy is

$$
{ \frac { 1 } { 2 } } k X ^ { 2 } .
$$

This total energy is constant and is shifted back and forth between kinetic energy and potential energy, at most

times being shared by each. The conservation of energy for this system in equation form is thus:

$$
{ \frac { 1 } { 2 } } m v ^ { 2 } + { \frac { 1 } { 2 } } k x ^ { 2 } = { \frac { 1 } { 2 } } k X ^ { 2 } .
$$

Solving this equation for $v$ yields:

$$
v = \pm { \sqrt { { \frac { k } { m } } \left( X ^ { 2 } - x ^ { 2 } \right) } } .
$$

Manipulating this expression algebraically gives:

$$
v = \pm \sqrt { \frac { k } { m } } X \sqrt { 1 - \frac { x ^ { 2 } } { X ^ { 2 } } }
$$

and so

$$
v = \pm v _ { \mathrm { m a x } } \sqrt { 1 - { \frac { x ^ { 2 } } { X ^ { 2 } } } } ,
$$

where

$$
v _ { \mathrm { m a x } } = \sqrt { \frac { k } { m } } X .
$$

From this expression, we see that the velocity is a maximum $( v _ { \mathrm { m a x } } )$ at $x = 0$ , as stated earlier in $v ( t ) = - v _ { \operatorname* { m a x } }$ sin $\textstyle { \frac { 2 \pi t } { T } }$ .Notice that the maximum velocity depends on three factors. Maximum velocity is directly proportional to amplitude. As you might guess, the greater the maximum displacement the greater the maximum velocity. Maximum velocity is also greater for stiffer systems, because they exert greater force for the same displacement. This observation is seen in the expression for $v _ { \mathrm { m a x } }$ it is proportional to the square root of the force constant $k$ . Finally, the maximum velocity is smaller for objects that have larger masses, because the maximum velocity is inversely proportional to the square root of $m$ . For a given force, objects that have large masses accelerate more slowly.

A similar calculation for the simple pendulum produces a similar result, namely:

$$
\omega _ { \mathrm { m a x } } = \sqrt { \frac { g } { L } } \theta _ { \mathrm { m a x } } .
$$

# EXAMPLE 16.6

# Determine the Maximum Speed of an Oscillating System: A Bumpy Road

Suppose that a car is $9 0 0 ~ \mathsf { k g }$ and has a suspension system that has a force constant $k = 6 . 5 3 \times 1 0 ^ { 4 } ~ \mathrm { N / m }$ . The car hits a bump and bounces with an amplitude of $0 . 1 0 0 \mathsf { m }$ . What is its maximum vertical velocity if you assume no damping occurs?

# Strategy

We can use the expression for $v _ { \mathrm { m a x } }$ given in $\begin{array} { r } { v _ { \operatorname* { m a x } } = \sqrt { \frac { k } { m } } X } \end{array}$ to determine the maximum vertical velocity. The variables $m$ and $k$ are given in the problem statement, and the maximum displacement $X$ is $0 . 1 0 0 \mathsf { m }$ .

# Solution

1. Identify known.   
2. Substitute known values into $\begin{array} { r } { v _ { \mathrm { m a x } } = \sqrt { \frac { k } { m } } X } \end{array}$

$$
v _ { \mathrm { m a x } } = { \sqrt { \frac { 6 . 5 3 \times 1 0 ^ { 4 } \ \mathrm { N / m } } { 9 0 0 \ \mathrm { k g } } } } ( 0 . 1 0 0 \ \mathrm { m } ) .
$$

3. Calculate to find $v _ { \mathrm { m a x } } { = } 0 . 8 5 2 \mathrm { m / s }$ ·

# Discussion

This answer seems reasonable for a bouncing car. There are other ways to use conservation of energy to find $v _ { \mathrm { m a x } }$ .   
We could use it directly, as was done in the example featured in Hooke’s Law: Stress and Strain Revisited.

The small vertical displacement $y$ of an oscillating simple pendulum, starting from its equilibrium position, is given as

$$
y ( t ) = a \sin \omega t ,
$$

where $a$ is the amplitude, $\omega$ is the angular velocity and $t$ is the time taken. Substituting $\begin{array} { r } { \omega = \frac { 2 \pi } { T } } \end{array}$ , we have

$$
y ( t ) = a \sin \biggl ( \frac { 2 \pi t } { T } \biggr ) .
$$

Thus, the displacement of pendulum is a function of time as shown above.

Also the velocity of the pendulum is given by

$$
v ( t ) { = } \frac { 2 a \pi } { T } \cos { \left( \frac { 2 \pi t } { T } \right) } ,
$$

so the motion of the pendulum is a function of time.

# CHECK YOUR UNDERSTANDING

Why does it hurt more if your hand is snapped with a ruler than with a loose spring, even if the displacement of each system is equal?

# Solution

The ruler is a stiffer system, which carries greater force for the same amount of displacement. The ruler snaps your hand with greater force, which hurts more.

# CHECK YOUR UNDERSTANDING

You are observing a simple harmonic oscillator. Identify one way you could decrease the maximum velocity of the system.

# Solution

You could increase the mass of the object that is oscillating.