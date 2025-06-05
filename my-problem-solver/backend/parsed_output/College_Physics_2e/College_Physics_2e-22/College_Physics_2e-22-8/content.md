# 22.8 Torque on a Current Loop: Motors and Meters

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

Describe how motors and meters work in terms of torque on a current loop.   
• Calculate the torque on a current-carrying loop in a magnetic field.

Motors are the most common application of magnetic force on current-carrying wires. Motors have loops of wire in a magnetic field. When current is passed through the loops, the magnetic field exerts torque on the loops, which rotates a shaft. Electrical energy is converted to mechanical work in the process. (See Figure 22.33.)

Let us examine the force on each segment of the loop in Figure 22.33 to find the torques produced about the axis of the vertical shaft. (This will lead to a useful equation for the torque on the loop.) We take the magnetic field to be uniform over the rectangular loop, which has width $w$ and height . First, we note that the forces on the top and bottom segments are vertical and, therefore, parallel to the shaft, producing no torque. Those vertical forces are equal in magnitude and opposite in direction, so that they also produce no net force on the loop. Figure 22.34 shows views of the loop from above. Torque is defined as $\boldsymbol { \tau } = \boldsymbol { r } \boldsymbol { F }$ sin $\theta$ , where $F$ is the force, $r$ is the distance from the pivot that the force is applied, and $\theta$ is the angle between $r$ and $F$ . As seen in Figure 22.34(a), right hand rule 1 gives the forces on the sides to be equal in magnitude and opposite in direction, so that the net force is again zero. However, each force produces a clockwise torque. Since $r = w / 2$ , the torque on each vertical segment is $( w / 2 ) F$ sin $\theta$ , and the two add to give a total torque.

$$
\tau = { \frac { w } { 2 } } F \sin \theta + { \frac { w } { 2 } } F \sin \theta = w F \sin \theta
$$

Now, each vertical segment has a length $l$ that is perpendicular to $B$ , so that the force on each is $F = I l B$ . Entering $F$ into the expression for torque yields

$$
\tau = w I l B \sin \theta .
$$

If we have a multiple loop of $N$ turns, we get $N$ times the torque of one loop. Finally, note that the area of the loop is $A = w l$ ; the expression for the torque becomes

$$
\tau = N I A B \sin \theta .
$$

This is the torque on a current-carrying loop in a uniform magnetic field. This equation can be shown to be valid for a loop of any shape. The loop carries a current $I$ , has $N$ turns, each of area $A$ , and the perpendicular to the loop makes an angle $\theta$ with the field $B$ . The net force on the loop is zero.

# EXAMPLE 22.5

# Calculating Torque on a Current-Carrying Loop in a Strong Magnetic Field

Find the maximum torque on a 100-turn square loop of a wire of $1 0 . 0 \mathsf { c m }$ on a side that carries 15.0 A of current in a 2.00-T field.

# Strategy

Torque on the loop can be found using $\tau = N I A B$ sin $\theta$ . Maximum torque occurs when $\theta = 9 0 ^ { \circ }$ and $\theta = 1$ .

# Solution

For $\theta = 1$ , the maximum torque is

$$
\tau _ { \operatorname* { m a x } } = N I A B .
$$

Entering known values yields

$$
{ \begin{array} { l c l } { \tau _ { \operatorname* { m a x } } } & { = } & { ( 1 0 0 ) ( 1 5 . 0 \mathrm { \ A } ) { \bigl ( } 0 . 1 0 0 \mathrm { \ m } ^ { 2 } { \bigr ) } ( 2 . 0 0 \mathrm { \ T } ) } \\ & { = } & { 3 0 . 0 \mathrm { \ N } \cdot \mathrm { m } . } \end{array} }
$$

# Discussion

This torque is large enough to be useful in a motor.

The torque found in the preceding example is the maximum. As the coil rotates, the torque decreases to zero at $\theta = 0$ . The torque then reversesits direction once the coil rotates past $\theta = 0$ . (See Figure 22.34(d).) This means that, unless we do something, the coil will oscillate back and forth about equilibrium at $\theta = 0$ . To get the coil to continue rotating in the same direction, we can reverse the current as it passes through $\theta = 0$ with automatic switches called brushes. (See Figure 22.35.)

Meters, such as those in analog fuel gauges on a car, are another common application of magnetic torque on a current-carrying loop. Figure 22.36 shows that a meter is very similar in construction to a motor. The meter in the figure has its magnets shaped to limit the effect of $\theta$ by making $B$ perpendicular to the loop over a large angular range. Thus the torque is proportional to $I$ and not $\theta _ { \cdot }$ . A linear spring exerts a counter-torque that balances the current-produced torque. This makes the needle deflection proportional to $I$ . If an exact proportionality cannot be achieved, the gauge reading can be calibrated. To produce a galvanometer for use in analog voltmeters and ammeters that have a low resistance and respond to small currents, we use a large loop area $A$ , high magnetic field $B$ , and low-resistance coils.