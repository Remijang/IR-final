# 12.3 The Most General Applications of Bernoulli’s Equation

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

Calculate using Torricelli’s theorem. • Calculate power in fluid flow.

# Torricelli’s Theorem

Figure 12.8 shows water gushing from a large tube through a dam. What is its speed as it emerges? Interestingly, if resistance is negligible, the speed is just what it would be if the water fell a distance $h$ from the surface of the reservoir; the water’s speed is independent of the size of the opening. Let us check this out. Bernoulli’s equation must be used since the depth is not constant. We consider water flowing from the surface (point 1) to the tube’s outlet (point 2). Bernoulli’s equation as stated in previously is

$$
P _ { 1 } + \frac { 1 } { 2 } \rho v _ { 1 } ^ { 2 } + \rho { g } h _ { 1 } = P _ { 2 } + \frac { 1 } { 2 } \rho v _ { 2 } ^ { 2 } + \rho { g } h _ { 2 } .
$$

Both $P _ { 1 }$ and $P _ { 2 }$ equal atmospheric pressure $\mathbf { \Omega } _ { \left. P _ { 1 } \right. }$ is atmospheric pressure because it is the pressure at the top of the reservoir. $P _ { 2 }$ must be atmospheric pressure, since the emerging water is surrounded by the atmosphere and cannot have a pressure different from atmospheric pressure.) and subtract out of the equation, leaving

$$
\frac { 1 } { 2 } \rho v _ { 1 } ^ { 2 } + \rho g h _ { 1 } = \frac { 1 } { 2 } \rho v _ { 2 } ^ { 2 } + \rho g h _ { 2 } .
$$

Solving this equation for $v _ { 2 } ^ { 2 }$ , noting that the density $\rho$ cancels (because the fluid is incompressible), yields

$$
v _ { 2 } ^ { 2 } = v _ { 1 } ^ { 2 } + 2 g ( h _ { 1 } - h _ { 2 } ) .
$$

We let $h = h _ { 1 } - h _ { 2 }$ ; the equation then becomes

$$
v _ { 2 } ^ { 2 } = v _ { 1 } ^ { 2 } + 2 g h
$$

where $h$ is the height dropped by the water. This is simply a kinematic equation for any object falling a distance $h$ with negligible resistance. In fluids, this last equation is called Toriceli’stheorem. Note that the result is independent of the velocity’s direction, just as we found when applying conservation of energy to falling objects.

All preceding applications of Bernoulli’s equation involved simplifying conditions, such as constant height or constant pressure. The next example is a more general application of Bernoulli’s equation in which pressure,

velocity, and height all change. (See Figure 12.9.)

# EXAMPLE 12.5

# Calculating Pressure: A Fire Hose Nozzle

Fire hoses used in major structure fires have inside diameters of $6 . 4 0 \mathsf { c m }$ . Suppose such a hose carries a flow of $4 0 . 0 \mathsf { L } / \mathsf { s }$ starting at a gauge pressure of $1 . 6 2 \times 1 0 ^ { 6 } \mathrm { N } / \mathrm { m } ^ { 2 }$ . The hose goes $1 0 . 0 \mathsf { m }$ up a ladder to a nozzle having an inside diameter of $3 . 0 0 \mathsf { c m }$ . Assuming negligible resistance, what is the pressure in the nozzle?

# Strategy

Here we must use Bernoulli’s equation to solve for the pressure, since depth is not constant.

# Solution

Bernoulli’s equation states

$$
P _ { 1 } + \frac { 1 } { 2 } \rho v _ { 1 } ^ { 2 } + \rho { g } h _ { 1 } = P _ { 2 } + \frac { 1 } { 2 } \rho v _ { 2 } ^ { 2 } + \rho { g } h _ { 2 } ,
$$

where the subscripts 1 and 2 refer to the initial conditions at ground level and the final conditions inside the nozzle, respectively. We must first find the speeds $v _ { 1 }$ and $v _ { 2 }$ . Since $Q = A _ { 1 } v _ { 1 }$ , we get

$$
v _ { 1 } = { \frac { Q } { A _ { 1 } } } = { \frac { 4 0 . 0 \times 1 0 ^ { - 3 } \mathrm { \ m ^ { 3 } / s } } { \pi ( 3 . 2 0 \times 1 0 ^ { - 2 } \mathrm { \ m } ) ^ { 2 } } } = 1 2 . 4 3 4 \mathrm { \ m / s } .
$$

Similarly, we find

$$
v _ { 2 } = 5 6 . 5 8 8 \mathrm { m / s } .
$$

(This rather large speed is helpful in reaching the fire.) Now, taking $h _ { 1 }$ to be zero, we solve Bernoulli’s equation for $P _ { 2 }$ :

$$
P _ { 2 } = P _ { 1 } + \frac { 1 } { 2 } \rho \bigl ( v _ { 1 } ^ { 2 } - v _ { 2 } ^ { 2 } \bigr ) - \rho g h _ { 2 } .
$$

Substituting known values yields

$$
{ \begin{array} { c } { P _ { 2 } = } \\ { { \mathrm { } } } \\ { { \mathrm { } } { \mathrm { } } { \mathrm { } } < 1 0 ^ { 6 } \ { \mathrm { N } } / { \mathrm { m } } ^ { 2 } + { \frac { 1 } { 2 } } ( 1 0 0 0 \mathrm { { k g } } / { \mathrm { m } } ^ { 3 } ) { \bigl [ } ( 1 2 . 4 3 4 \mathrm { { m } } / { \mathrm { s } } ) ^ { 2 } - ( 5 6 . 5 8 8 \mathrm { { m } } / { \mathrm { s } } ) ^ { 2 } { \bigr ] } - ( 1 0 0 0 \mathrm { { k g } } / { \mathrm { m } } ^ { 3 } ) ( 9 . 8 0 \mathrm { { m } } / { \mathrm { s } } ^ { 2 } ) ( 1 0 . 0 1 \mathrm { { m } } / { \mathrm { s } } ) } \\ { \approx 1 8 0 0 \mathrm { { N } } / { \mathrm { m } } ^ { 2 } . } \end{array} }
$$

# Discussion

This value is a gauge pressure, since the initial pressure was given as a gauge pressure. Thus the nozzle pressure is very close to atmospheric pressure, as it must because the water exits into the atmosphere without changes in its conditions.

# Power in Fluid Flow

Power is the rateat which work is done or energy in any form is used or supplied. To see the relationship of power to fluid flow, consider Bernoulli’s equation:

$$
P + { \frac { 1 } { 2 } } \rho v ^ { 2 } + \rho g h = \mathrm { c o n s t a n t } .
$$

All three terms have units of energy per unit volume, as discussed in the previous section. Now, considering units, if we multiply energy per unit volume by flow rate (volume per unit time), we get units of power. That is, $( E / V ) ( V / t ) { = } E / t$ . This means that if we multiply Bernoulli’s equation by flow rate $Q$ , we get power. In equation form, this is

$$
\Bigg ( P + \frac { 1 } { 2 } \rho v ^ { 2 } + \rho g h \Bigg ) Q = \mathrm { p o w e r } .
$$

Each term has a clear physical meaning. For example, $P Q$ is the power supplied to a fluid, perhaps by a pump, to give it its pressure $P$ . Similarly, ${ \scriptstyle { \frac { 1 } { 2 } } } \rho v ^ { 2 } Q$ is the power supplied to a fluid to give it its kinetic energy. And $\rho g h Q$ is the power going to gravitational potential energy.

# Making Connections: Power

Power is defined as the rate of energy transferred, or $E / t$ . Fluid flow involves several types of power. Each type of power is identified with a specific type of energy being expended or changed in form.

# EXAMPLE 12.6

# Calculating Power in a Moving Fluid

Suppose the fire hose in the previous example is fed by a pump that receives water through a hose with a $6 . 4 0 \mathsf { - c m }$ diameter coming from a hydrant with a pressure of $0 . 7 0 0 \times 1 0 ^ { 6 } \ \mathrm { N } / \mathrm { m } ^ { 2 }$ . What power does the pump supply to the water?

# Strategy

Here we must consider energy forms as well as how they relate to fluid flow. Since the input and output hoses have the same diameters and are at the same height, the pump does not change the speed of the water nor its height, and so the water’s kinetic energy and gravitational potential energy are unchanged. That means the pump only supplies power to increase water pressure by $0 . 9 2 \times 1 0 ^ { 6 } ~ \mathrm { N } / \mathrm { m } ^ { 2 }$ (from $0 . 7 0 0 \times 1 0 ^ { 6 } \ \mathrm { N } / \mathrm { m } ^ { 2 }$ to $1 . 6 2 \times 1 0 ^ { 6 } \mathrm { \ : N / m } ^ { 2 } ;$ ).

# Solution

As discussed above, the power associated with pressure is

$$
{ \begin{array} { l l l } { \operatorname { p o w e r } } & { = } & { P Q } \\ & { = } & { \left( 0 . 9 2 0 \times 1 0 ^ { 6 } \ \mathrm { N } / \mathrm { m } ^ { 2 } \right) \left( 4 0 . 0 \times 1 0 ^ { - 3 } \ \mathrm { m } ^ { 3 } / \mathrm { s } \right) . . } \\ & { = } & { 3 . 6 8 \times 1 0 ^ { 4 } \ \mathrm { W } = 3 6 . 8 \ \mathrm { k W } } \end{array} }
$$

# Discussion

Such a substantial amount of power requires a large pump, such as is found on some fire trucks. (This kilowatt value converts to about 50 hp.) The pump in this example increases only the water’s pressure. If a pump—such as the heart—directly increases velocity and height as well as pressure, we would have to calculate all three terms to find the power it supplies.