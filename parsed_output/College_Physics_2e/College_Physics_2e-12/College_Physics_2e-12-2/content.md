# 12.2 Bernoulli’s Equation

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

Explain the terms in Bernoulli’s equation. • Explain how Bernoulli’s equation is related to conservation of energy. • Explain how to derive Bernoulli’s principle from Bernoulli’s equation. • Calculate with Bernoulli’s principle. • List some applications of Bernoulli’s principle.

When a fluid flows into a narrower channel, its speed increases. That means its kinetic energy also increases. Where does that change in kinetic energy come from? The increased kinetic energy comes from the net work done on the fluid to push it into the channel and the work done on the fluid by the gravitational force, if the fluid changes vertical position. Recall the work-energy theorem,

$$
W _ { \mathrm { n e t } } = \frac { 1 } { 2 } m v ^ { 2 } - \frac { 1 } { 2 } m v _ { 0 } ^ { 2 } .
$$

There is a pressure difference when the channel narrows. This pressure difference results in a net force on the fluid: recall that pressure times area equals force. The net work done increases the fluid’s kinetic energy. As a result, the pres urewil dropinarapidly-movingfluid, whether or not the fluid is confined to a tube.

There are a number of common examples of pressure dropping in rapidly-moving fluids. Shower curtains have a disagreeable habit of bulging into the shower stall when the shower is on. The high-velocity stream of water and air creates a region of lower pressure inside the shower, and standard atmospheric pressure on the other side. The pressure difference results in a net force inward pushing the curtain in. You may also have noticed that when passing a truck on the highway, your car tends to veer toward it. The reason is the same—the high velocity of the air between the car and the truck creates a region of lower pressure, and the vehicles are pushed together by greater pressure on the outside. (See Figure 12.4.) This effect was observed as far back as the mid-1800s, when it was found that trains passing in opposite directions tipped precariously toward one another.



# Making Connections: Take-Home Investigation with a Sheet of Paper

Hold the short edge of a sheet of paper parallel to your mouth with one hand on each side of your mouth. The page should slant downward over your hands. Blow over the top of the page. Describe what happens and explain the reason for this behavior.

# Bernoulli’s Equation

The relationship between pressure and velocity in fluids is described quantitatively by Bernoulli’s equation, named after its discoverer, the Swiss scientist Daniel Bernoulli (1700–1782). Bernoulli’s equation states that for an incompressible, frictionless fluid, the following sum is constant:

$$
P + { \frac { 1 } { 2 } } \rho v ^ { 2 } + \rho g h = \mathrm { c o n s t a n t } ,
$$

where $P$ is the absolute pressure, $\rho$ is the fluid density, $v$ is the velocity of the fluid, $h$ is the height above some reference point, and $g$ is the acceleration due to gravity. If we follow a small volume of fluid along its path, various quantities in the sum may change, but the total remains constant. Let the subscripts 1 and 2 refer to any two points along the path that the bit of fluid follows; Bernoulli’s equation becomes

$$
P _ { 1 } + \frac { 1 } { 2 } \rho v _ { 1 } ^ { 2 } + \rho { g } h _ { 1 } = P _ { 2 } + \frac { 1 } { 2 } \rho v _ { 2 } ^ { 2 } + \rho { g } h _ { 2 } .
$$

Bernoulli’s equation is a form of the conservation of energy principle. Note that the second and third terms are the kinetic and potential energy with $m$ replaced by $\rho$ . In fact, each term in the equation has units of energy per unit volume. We can prove this for the second term by substituting $\rho = m / V$ into it and gathering terms:

$$
{ \frac { 1 } { 2 } } \rho v ^ { 2 } = { \frac { { \frac { 1 } { 2 } } m v ^ { 2 } } { V } } = { \frac { \mathrm { K E } } { V } } .
$$

$\mathsf { S } \mathsf { o } \frac { 1 } { 2 } \rho v ^ { 2 }$ is the kinetic energy per unit volume. Making the same substitution into the third term in the equation, we find

$$
\rho g h = \frac { m g h } { V } = \frac { \mathrm { P E } _ { \mathrm { g } } } { V } ,
$$

so $\rho g h$ is the gravitational potential energy per unit volume. Note that pressure $P$ has units of energy per unit volume, too. Since $P = F / A$ , its units are $\mathrm { N } / \mathrm { m } ^ { 2 }$ . If we multiply these by $\mathsf { m } / \mathsf { m }$ , we obtain $\mathbf { N } \cdot \mathbf { m } / \mathbf { m } ^ { 3 } = \mathbf { J } / \mathbf { m } ^ { 3 }$ , or energy per unit volume. Bernoulli’s equation is, in fact, just a convenient statement of conservation of energy for an incompressible fluid in the absence of friction.

# Making Connections: Conservation of Energy

Conservation of energy applied to fluid flow produces Bernoulli’s equation. The net work done by the fluid’s pressure results in changes in the fluid’s and $\mathrm { P E _ { g } }$ per unit volume. If other forms of energy are involved in fluid flow, Bernoulli’s equation can be modified to take these forms into account. Such forms of energy include thermal energy dissipated because of fluid viscosity.

The general form of Bernoulli’s equation has three terms in it, and it is broadly applicable. To understand it better, we will look at a number of specific situations that simplify and illustrate its use and meaning.

# Bernoulli’s Equation for Static Fluids

Let us first consider the very simple situation where the fluid is static—that is, $v _ { 1 } = v _ { 2 } = 0$ . Bernoulli’s equation in that case is

$$
P _ { 1 } + \rho g h _ { 1 } = P _ { 2 } + \rho g h _ { 2 } .
$$

We can further simplify the equation by taking $h _ { 2 } = 0$ (we can always choose some height to be zero, just as we often have done for other situations involving the gravitational force, and take all other heights to be relative to this). In that case, we get

$$
P _ { 2 } = P _ { 1 } + \rho g h _ { 1 } .
$$

This equation tells us that, in static fluids, pressure increases with depth. As we go from point 1 to point 2 in the fluid, the depth increases by $h _ { 1 }$ , and consequently, $P _ { 2 }$ is greater than $P _ { 1 }$ by an amount $\rho g h _ { 1 }$ . In the very simplest case, $P _ { 1 }$ is zero at the top of the fluid, and we get the familiar relationship $P = \rho g h$ . (Recall that $P = \rho g h$ and $\Delta \mathrm { P E _ { g } } = m g h . )$ Bernoulli’s equation includes the fact that the pressure due to the weight of a fluid is $\rho g h$ . Although we introduce Bernoulli’s equation for fluid flow, it includes much of what we studied for static fluids in the preceding chapter.

# Bernoulli’s Principle—Bernoulli’s Equation at Constant Depth

Another important situation is one in which the fluid moves but its depth is constant—that is, $h _ { 1 } = h _ { 2 }$ . Under that condition, Bernoulli’s equation becomes

$$
P _ { 1 } + \frac { 1 } { 2 } \rho v _ { 1 } ^ { 2 } = P _ { 2 } + \frac { 1 } { 2 } \rho v _ { 2 } ^ { 2 } .
$$

Situations in which fluid flows at a constant depth are so important that this equation is often called Bernoulli’s principle. It is Bernoulli’s equation for fluids at constant depth. (Note again that this applies to a small volume of fluid as we follow it along its path.) As we have just discussed, pressure drops as speed increases in a moving fluid. We can see this from Bernoulli’s principle. For example, if $v _ { 2 }$ is greater than $\scriptstyle v _ { 1 }$ in the equation, then $P _ { 2 }$ must be less than $P _ { 1 }$ for the equality to hold.

# EXAMPLE 12.4

# Calculating Pressure: Pressure Drops as a Fluid Speeds Up

In Example 12.2, we found that the speed of water in a hose increased from $1 . 9 6 ~ \mathsf { m } / \mathsf { s }$ to $2 5 . 5 \mathsf { m } / \mathsf { s }$ going from the hose to the nozzle. Calculate the pressure in the hose, given that the absolute pressure in the nozzle is $1 . 0 1 \times 1 0 ^ { 5 } \ \mathrm { N } / \mathrm { m } ^ { 2 }$ (atmospheric, as it must be) and assuming level, frictionless flow.

# Strategy

Level flow means constant depth, so Bernoulli’s principle applies. We use the subscript 1 for values in the hose and 2 for those in the nozzle. We are thus asked to find $P _ { 1 }$ .

# Solution

Solving Bernoulli’s principle for $P _ { 1 }$ yields

$$
P _ { 1 } = P _ { 2 } + \frac { 1 } { 2 } \rho v _ { 2 } ^ { 2 } - \frac { 1 } { 2 } \rho v _ { 1 } ^ { 2 } = P _ { 2 } + \frac { 1 } { 2 } \rho ( v _ { 2 } ^ { 2 } - v _ { 1 } ^ { 2 } ) .
$$

Substituting known values,

$$
{ \begin{array} { l l l } { P _ { 1 } } & { = } & { 1 . 0 1 \times 1 0 ^ { 5 } \ \mathrm { N / m ^ { 2 } } } \\ & & { \ + \ { \frac { 1 } { 2 } } ( 1 0 ^ { 3 } \ \mathrm { k g / m ^ { 3 } } ) \big [ ( 2 5 . 5 \ \mathrm { m / s } ) ^ { 2 } - ( 1 . 9 6 \ \mathrm { m / s } ) ^ { 2 } \big ] } \\ & { = } & { 4 . 2 4 \times 1 0 ^ { 5 } \ \mathrm { N / m ^ { 2 } } . } \end{array} }
$$

# Discussion

This absolute pressure in the hose is greater than in the nozzle, as expected since $v$ is greater in the nozzle. The pressure $P _ { 2 }$ in the nozzle must be atmospheric since it emerges into the atmosphere without other changes in conditions.

# Applications of Bernoulli’s Principle

There are a number of devices and situations in which fluid flows at a constant height and, thus, can be analyzed with Bernoulli’s principle.

# Entrainment

People have long put the Bernoulli principle to work by using reduced pressure in high-velocity fluids to move things about. With a higher pressure on the outside, the high-velocity fluid forces other fluids into the stream. This process is called entrainment. Entrainment devices have been in use since ancient times, particularly as pumps to raise water small heights, as in draining swamps, fields, or other low-lying areas. Some other devices that use the concept of entrainment are shown in Figure 12.5.

# Wings and Sails

The airplane wing is a beautiful example of Bernoulli’s principle in action. Figure 12.6(a) shows the characteristic shape of a wing. The wing is tilted upward at a small angle and the upper surface is longer, causing air to flow faster over it. The pressure on top of the wing is therefore reduced, creating a net upward force or lift. (Wings can also gain lift by pushing air downward, utilizing the conservation of momentum principle. The deflected air molecules result in an upward force on the wing — Newton’s third law.) Sails also have the characteristic shape of a wing. (See Figure 12.6(b).) The pressure on the front side of the sail, $P _ { \mathrm { f r o n t } }$ , is lower than the pressure on the back of the sail, $P _ { \mathrm { b a c k } }$ .

This results in a forward force and even allows you to sail into the wind.

# Making Connections: Take-Home Investigation with Two Strips of Paper

For a good illustration of Bernoulli’s principle, make two strips of paper, each about $1 5 \mathsf { c m }$ long and 4 cm wide. Hold the small end of one strip up to your lips and let it drape over your finger. Blow across the paper. What happens? Now hold two strips of paper up to your lips, separated by your fingers. Blow between the strips. What happens?

# Velocity measurement

Figure 12.7 shows two devices that measure fluid velocity based on Bernoulli’s principle. The manometer in Figure 12.7(a) is connected to two tubes that are small enough not to appreciably disturb the flow. The tube facing the oncoming fluid creates a dead spot having zero velocity $( v _ { 1 } = 0 )$ ) in front of it, while fluid passing the other tube has velocity $v _ { 2 }$ . This means that Bernoulli’s principle as stated in $\begin{array} { r } { P _ { 1 } + \frac { 1 } { 2 } \rho v _ { 1 } ^ { 2 } = P _ { 2 } + \frac { 1 } { 2 } \rho v _ { 2 } ^ { 2 } } \end{array}$ becomes

$$
P _ { 1 } = P _ { 2 } + \frac { 1 } { 2 } \rho v _ { 2 } ^ { 2 } .
$$

Thus pressure $P _ { 2 }$ over the second opening is reduced by $\scriptstyle { \frac { 1 } { 2 } } \rho v _ { 2 } ^ { 2 }$ , and so the fluid in the manometer rises by $h$ on the side connected to the second opening, where

$$
h \propto \frac { 1 } { 2 } \rho v _ { 2 } ^ { 2 } .
$$

(Recall that the symbol means “proportional to.”) Solving for $v _ { 2 }$ , we see that

$$
v _ { 2 } \propto { \sqrt { h } } .
$$

Figure 12.7(b) shows a version of this device that is in common use for measuring various fluid velocities; such devices are frequently used as air speed indicators in aircraft.