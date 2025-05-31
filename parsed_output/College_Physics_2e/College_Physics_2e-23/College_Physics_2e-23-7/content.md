# 23.7 Transformers

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

Explain how a transformer works.   
• Calculate voltage, current, and/or number of turns given the other quantities.

Transformers do what their name implies—they transform voltages from one value to another (The term voltage is used rather than emf, because transformers have internal resistance). For example, many cell phones, laptops, video games, and power tools and small appliances have a transformer built into their plug-in unit (like that in Figure 23.25) that changes $\textstyle 1 2 0 \vee$ or 240 V AC into whatever voltage the device uses. Transformers are also used at several points in the power distribution systems, such as illustrated in Figure 23.26. Power is sent long distances at high voltages, because less current is required for a given amount of power, and this means less line loss, as was discussed previously. But high voltages pose greater hazards, so that transformers are employed to produce lower

voltage at the user’s location.

The type of transformer considered in this text—see Figure 23.27—is based on Faraday’s law of induction and is very similar in construction to the apparatus Faraday used to demonstrate magnetic fields could cause currents. The two coils are called the primaryand secondarycoils. In normal use, the input voltage is placed on the primary, and the secondary produces the transformed output voltage. Not only does the iron core trap the magnetic field created by the primary coil, its magnetization increases the field strength. Since the input voltage is AC, a time-varying magnetic flux is sent to the secondary, inducing its AC output voltage.

For the simple transformer shown in Figure 23.27, the output voltage $V _ { \mathrm { s } }$ depends almost entirely on the input voltage $V _ { \mathfrak { p } }$ and the ratio of the number of loops in the primary and secondary coils. Faraday’s law of induction for the secondary coil gives its induced output voltage $V _ { \mathrm { s } }$ to be

$$
V _ { \mathrm { s } } = - N _ { \mathrm { s } } \frac { \Delta \phi } { \Delta t } ,
$$

where $N _ { \mathrm { s } }$ is the number of loops in the secondary coil and $\Delta \phi / \Delta t$ is the rate of change of magnetic flux. Note that the output voltage equals the induced emf $\begin{array} { r } { \langle V _ { \mathrm { s } } = \mathrm { e m f } _ { \mathrm { s } } ^ { \ } } \end{array}$ ), provided coil resistance is small (a reasonable assumption for transformers). The cross-sectional area of the coils is the same on either side, as is the magnetic field strength, and so $\Delta \phi / \Delta t$ is the same on either side. The input primary voltage $V _ { \mathfrak { p } }$ is also related to changing flux by

$$
V _ { p } = - { N _ { \mathrm { p } } } \frac { \Delta \phi } { \Delta t } .
$$

The reason for this is a little more subtle. Lenz’s law tells us that the primary coil opposes the change in flux caused by the input voltage $V _ { \mathfrak { p } }$ , hence the minus sign (This is an example of self-inductance, a topic to be explored in some detail in later sections). Assuming negligible coil resistance, Kirchhoff’s loop rule tells us that the induced emf exactly equals the input voltage. Taking the ratio of these last two equations yields a useful relationship:

$$
{ \frac { V _ { \mathrm { s } } } { V _ { \mathrm { p } } } } = { \frac { N _ { \mathrm { s } } } { N _ { \mathrm { p } } } } .
$$

This is known as the transformer equation, and it simply states that the ratio of the secondary to primary voltages in a transformer equals the ratio of the number of loops in their coils.

The output voltage of a transformer can be less than, greater than, or equal to the input voltage, depending on the ratio of the number of loops in their coils. Some transformers even provide a variable output by allowing connection to be made at different points on the secondary coil. A step-up transformer is one that increases voltage, whereas a step-down transformer decreases voltage. Assuming, as we have, that resistance is negligible, the electrical power output of a transformer equals its input. This is nearly true in practice—transformer efficiency often exceeds $9 9 \%$ . Equating the power input and output,

$$
P _ { \mathrm { p } } = I _ { \mathrm { p } } V _ { \mathrm { p } } = I _ { \mathrm { s } } V _ { \mathrm { s } } = P _ { \mathrm { s } } .
$$

Rearranging terms gives

$$
{ \frac { V _ { \mathrm { s } } } { V _ { \mathrm { p } } } } = { \frac { I _ { \mathrm { p } } } { I _ { \mathrm { s } } } } .
$$

Combining this with $\begin{array} { r } { \frac { V _ { \mathrm { s } } } { V _ { \mathrm { p } } } = \frac { N _ { \mathrm { s } } } { N _ { \mathrm { p } } } } \end{array}$ , we find that

$$
{ \frac { I _ { \mathrm { s } } } { I _ { \mathrm { p } } } } = { \frac { N _ { \mathrm { p } } } { N _ { \mathrm { s } } } }
$$

is the relationship between the output and input currents of a transformer. So if voltage increases, current decreases. Conversely, if voltage decreases, current increases.

# EXAMPLE 23.5

# Calculating Characteristics of a Step-Up Transformer

A portable x-ray unit has a step-up transformer, the $\boldsymbol { \mathsf { 1 2 0 } } \boldsymbol { \mathsf { V } }$ input of which is transformed to the $1 0 0 \mathsf { k V }$ output needed by the $\mathsf { x }$ -ray tube. The primary has 50 loops and draws a current of 10.00 A when in use. (a) What is the number of loops in the secondary? (b) Find the current output of the secondary.

# Strategy and Solution for (a)

We solve for , the number of loops in the secondary, and enter the known values. This gives

$$
\begin{array} { l l l } { N _ { \mathrm { s } } } & { = } & { N _ { \mathrm { p } } \frac { V _ { \mathrm { s } } } { V _ { \mathrm { p } } } } \\ & { = } & { ( 5 0 ) \frac { 1 0 0 , 0 0 0 \mathrm { \ V } } { 1 2 0 \mathrm { \ V } } = 4 . 1 7 \times 1 0 ^ { 4 } \mathrm { . } } \end{array}
$$

# Discussion for (a)

A large number of loops in the secondary (compared with the primary) is required to produce such a large voltage.   
This would be true for neon sign transformers and those supplying high voltage inside TVs and CRTs.

# Strategy and Solution for (b)

We can similarly find the output current of the secondary by solving f or and entering known values. This gives

$$
\begin{array}{c} { \begin{array} { l } { I _ { \mathrm { s } } } \\ { \ = \ } \end{array} } = { I _ { \mathrm { p } } } { \frac { N _ { \mathrm { p } } } { N _ { \mathrm { s } } } }  \\ { \ = \ ( 1 0 . 0 0 \mathrm { \ A } ) { \frac { 5 0 } { 4 . 1 7 \times 1 0 ^ { 4 } } } = 1 2 . 0 \mathrm { m A } . } \end{array} 
$$

# Discussion for (b)

As expected, the current output is significantly less than the input. In certain spectacular demonstrations, very large voltages are used to produce long arcs, but they are relatively safe because the transformer output does not supply a large current. Note that the power input here is $P _ { \mathrm { p } } = I _ { \mathrm { p } } V _ { \mathrm { p } } = ( 1 0 . 0 0 \mathrm { A } ) ( 1 2 0 \mathrm { V } ) = 1 . 2 0 \mathrm { k W } .$ This equals the power output $P _ { \mathrm { p } } = I _ { \mathrm { s } } V _ { \mathrm { s } } = ( 1 2 . 0 \mathrm { m A } ) ( 1 0 0 \mathrm { k V } ) = 1 . 2 0 \mathrm { k W }$ , as we assumed in the derivation of the equations used.

The fact that transformers are based on Faraday’s law of induction makes it clear why we cannot use transformers to change DC voltages. If there is no change in primary voltage, there is no voltage induced in the secondary. One possibility is to connect DC to the primary coil through a switch. As the switch is opened and closed, the secondary produces a voltage like that in Figure 23.28. This is not really a practical alternative, and AC is in common use wherever it is necessary to increase or decrease voltages.

# EXAMPLE 23.6

# Calculating Characteristics of a Step-Down Transformer

A battery charger meant for a series connection of ten nickel-cadmium batteries (total emf of 12.5 V DC) needs to have a 15.0 V output to charge the batteries. It uses a step-down transformer with a 200-loop primary and a $\textstyle 1 2 0 \vee$ input. (a) How many loops should there be in the secondary coil? (b) If the charging current is 16.0 A, what is the input current?

# Strategy and Solution for (a)

You would expect the secondary to have a small number of loops. Solving for and entering known values gives

$$
\begin{array} { l l l } { N _ { \mathrm { s } } } & { = } & { N _ { \mathrm { p } } \frac { V _ { \mathrm { s } } } { V _ { \mathrm { p } } } } \\ & { = } & { ( 2 0 0 ) \frac { 1 5 . 0 \mathrm { \ : V } } { 1 2 0 \mathrm { \ : V } } = 2 5 . } \end{array}
$$

# Strategy and Solution for (b)

$\begin{array} { r } { \frac { I _ { \mathrm { S } } } { I _ { \mathrm { p } } } = \frac { N _ { \mathrm { p } } } { N _ { \mathrm { S } } } } \end{array}$ $I _ { \mathrm { p } }$

$$
\begin{array} { l l l } { { I _ { \mathrm { p } } } } & { { = } } & { { I _ { \mathrm { s } } { \frac { N _ { \mathrm { s } } } { N _ { \mathrm { p } } } } } } \\ { { } } & { { = } } & { { ( 1 6 . 0 \mathrm { A } ) { \frac { 2 5 } { 2 0 0 } } = 2 . 0 0 \mathrm { A } . } } \end{array}
$$

# Discussion

The number of loops in the secondary is small, as expected for a step-down transformer. We also see that a small input current produces a larger output current in a step-down transformer. When transformers are used to operate large magnets, they sometimes have a small number of very heavy loops in the secondary. This allows the secondary to have low internal resistance and produce large currents. Note again that this solution is based on the assumption of $100 \%$ efficiency—or power out equals power in $\begin{array} { r } { ( P _ { \mathrm { p } } = P _ { \mathrm { s } } ) } \end{array}$ )—reasonable for good transformers. In this case the primary and secondary power is 240 W. (Verify this for yourself as a consistency check.) Note that the NiCd batteries need to be charged from a DC power source (as would a $\boldsymbol { \mathsf { 1 2 V } }$ battery). So the AC output of the

secondary coil needs to be converted into DC. This is done using something called a rectifier, which uses devices called diodes that allow only a one-way flow of current.

Transformers have many applications in electrical safety systems, which are discussed in Electrical Safety: Systems and Devices.

# PHET EXPLORATIONS

# Generator

Generate electricity with a bar magnet! Discover the physics behind the phenomena by exploring magnets and how you can use them to make a bulb light.

Click to view content (https://openstax.org/l/28gen).

#