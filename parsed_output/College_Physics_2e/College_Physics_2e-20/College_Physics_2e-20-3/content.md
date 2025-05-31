# 20.3 Resistance and Resistivity

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

• Explain the concept of resistivity.   
• Use resistivity to calculate the resistance of specified configurations of material.   
• Use the thermal coefficient of resistivity to calculate the change of resistance with temperature.

# Material and Shape Dependence of Resistance

The resistance of an object depends on its shape and the material of which it is composed. The cylindrical resistor in Figure 20.10 is easy to analyze, and, by so doing, we can gain insight into the resistance of more complicated shapes. As you might expect, the cylinder’s electric resistance $R$ is directly proportional to its length $L$ , similar to the resistance of a pipe to fluid flow. The longer the cylinder, the more collisions charges will make with its atoms. The greater the diameter of the cylinder, the more current it can carry (again similar to the flow of fluid through a pipe). In fact, $R$ is inversely proportional to the cylinder’s cross-sectional area $A$ .

For a given shape, the resistance depends on the material of which the object is composed. Different materials offer different resistance to the flow of charge. We define the resistivity $\rho$ of a substance so that the resistance $R$ of an object is directly proportional to $\rho$ . Resistivity $\rho$ is an intrinsicproperty of a material, independent of its shape or size. The resistance $R$ of a uniform cylinder of length $L$ , of cross-sectional area $A$ , and made of a material with resistivity $\rho$ , is

$$
R = { \frac { \rho L } { A } } .
$$

Table 20.1 gives representative values of $\rho$ . The materials listed in the table are separated into categories of conductors, semiconductors, and insulators, based on broad groupings of resistivities. Conductors have the smallest resistivities, and insulators have the largest; semiconductors have intermediate resistivities. Conductors have varying but large free charge densities, whereas most charges in insulators are bound to atoms and are not free to move. Semiconductors are intermediate, having far fewer free charges than conductors, but having properties that make the number of free charges depend strongly on the type and amount of impurities in the semiconductor. These unique properties of semiconductors are put to use in modern electronics, as will be explored in later chapters.

# EXAMPLE 20.5

# Calculating Resistor Diameter: A Headlight Filament

A car headlight filament is made of tungsten and has a cold resistance of $0 . 3 5 0 \Omega$ . If the filament is a cylinder 4.00

cm long (it may be coiled to save space), what is its diameter?

# Strategy

We can rearrange the equation $\textstyle R = { \frac { \rho L } { A } }$ to find the cross-sectional area $A$ of the filament from the given information. Then its diameter can be found by assuming it has a circular cross-section.

# Solution

$\textstyle R = { \frac { \rho L } { A } }$

$$
A = { \frac { \rho L } { R } } .
$$

Substituting the given values, and taking $\rho$ from Table 20.1, yields

$$
\begin{array} { r c l } { { A } } & { { = } } & { { \frac { ( 5 . 6 \times 1 0 ^ { - 8 } \ \Omega \cdot \mathrm { m } ) ( 4 . 0 0 \times 1 0 ^ { - 2 } \ \mathrm { m } ) } { 0 . 3 5 0 \ \Omega } } } \\ { { } } & { { = } } & { { 6 . 4 0 \times 1 0 ^ { - 9 } \ \mathrm { m } ^ { 2 } . } } \end{array}
$$

The area of a circle is related to its diameter $D$ by

$$
A = { \frac { \pi D ^ { 2 } } { 4 } } .
$$

Solving for the diameter $D$ , and substituting the value found for $A$ , gives

$$
\begin{array} { r c l } { { D } } & { { = } } & { { 2 \Big ( { \frac { A } { p } } \Big ) ^ { \frac { 1 } { 2 } } = 2 \Bigg ( { \frac { 6 . 4 0 \times 1 0 ^ { - 9 } \ \mathrm { m } ^ { 2 } } { 3 . 1 4 } } \Bigg ) ^ { \frac { 1 } { 2 } } } } \\ { { } } & { { = } } & { { 9 . 0 \times 1 0 ^ { - 5 } \ \mathrm { m } . } } \end{array}
$$

# Discussion

The diameter is just under a tenth of a millimeter. It is quoted to only two digits, because $\rho$ is known to only two digits.

# Temperature Variation of Resistance

The resistivity of all materials depends on temperature. Some even become superconductors (zero resistivity) at very low temperatures. (See Figure 20.11.) Conversely, the resistivity of conductors increases with increasing temperature. Since the atoms vibrate more rapidly and over larger distances at higher temperatures, the electrons moving through a metal make more collisions, effectively making the resistivity higher. Over relatively small temperature changes (about $1 0 0 ^ { \circ } \mathrm { C }$ or less), resistivity $\rho$ varies with temperature change $\Delta T$ as expressed in the following equation

$$
\rho = \rho _ { 0 } ( 1 + \alpha \Delta T ) ,
$$

where $\rho _ { 0 }$ is the original resistivity and $\alpha$ is the temperature coefficient of resistivity. (See the values of $\alpha$ in Table $\underline { { 2 0 . 2 } }$ below.) For larger temperature changes, $\alpha$ may vary or a nonlinear equation may be needed to find $\rho$ . Note that $\alpha$ is positive for metals, meaning their resistivity increases with temperature. Some alloys have been developed specifically to have a small temperature dependence. Manganin (which is made of copper, manganese and nickel), for example, has $\alpha$ close to zero (to three digits on the scale in Table 20.2), and so its resistivity varies only slightly with temperature. This is useful for making a temperature-independent resistance standard, for example.

Note also that $\alpha$ is negative for the semiconductors listed in Table 20.2, meaning that their resistivity decreases with increasing temperature. They become better conductors at higher temperature, because increased thermal agitation increases the number of free charges available to carry current. This property of decreasing $\rho$ with temperature is also related to the type and amount of impurities present in the semiconductors.

The resistance of an object also depends on temperature, since $R _ { 0 }$ is directly proportional to $\rho$ . For a cylinder we know $R = \rho L / A$ , and so, if $L$ and $A$ do not change greatly with temperature, $R$ will have the same temperature dependence as $\rho$ . (Examination of the coefficients of linear expansion shows them to be about two orders of magnitude less than typical temperature coefficients of resistivity, and so the effect of temperature on $L$ and $A$ is about two orders of magnitude less than on $\rho$ .) Thus,

$$
R = R _ { 0 } ( 1 + \alpha \Delta T )
$$

is the temperature dependence of the resistance of an object, where $R _ { 0 }$ is the original resistance and $R$ is the resistance after a temperature change $\Delta T$ . Numerous thermometers are based on the effect of temperature on resistance. (See Figure 20.12.) One of the most common is the thermistor, a semiconductor crystal with a strong temperature dependence, the resistance of which is measured to obtain its temperature. The device is small, so that it quickly comes into thermal equilibrium with the part of a person it touches.

# EXAMPLE 20.6

# Calculating Resistance: Hot-Filament Resistance

Although caution must be used in applying $\rho = \rho _ { 0 } ( 1 + \alpha \Delta T )$ and $R = R _ { 0 } ( 1 + \alpha \Delta T )$ for temperature changes greater than $1 0 0 ^ { \circ } \mathrm { C }$ , for tungsten the equations work reasonably well for very large temperature changes. What, then, is the resistance of the tungsten filament in the previous example if its temperature is increased from room temperature $( 2 0 ^ { \circ } \mathrm { C } )$ to a typical operating temperature of $2 8 5 0 ^ { \circ } \mathrm { C } ?$

# Strategy

This is a straightforward application of $R = R _ { 0 } ( 1 + \alpha \Delta T )$ , since the original resistance of the filament was given to be $R _ { 0 } = 0 . 3 5 0 \Omega$ , and the temperature change is $\Delta T = 2 8 3 0 ^ { \circ } \mathrm { C }$ .

# Solution

The hot resistance $R$ is obtained by entering known values into the above equation:

$$
\begin{array} { l l l } { { R } } & { { = } } & { { R _ { 0 } ( 1 + \alpha \Delta T ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { ( 0 . 3 5 0 \ \Omega ) [ 1 + ( 4 . 5 \times 1 0 ^ { - 3 } / ^ { \circ } \mathrm { C } ) ( 2 8 3 0 ^ { \circ } \mathrm { C } ) ] } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { 4 . 8 \ \Omega . } } \end{array}
$$

# Discussion

This value is consistent with the headlight resistance example in Ohm’s Law: Resistance and Simple Circuits.

# PHET EXPLORATIONS

# Resistance in a Wire

Learn about the physics of resistance in a wire. Change its resistivity, length, and area to see how they affect the wire's resistance. The sizes of the symbols in the equation change along with the diagram of a wire.

Click to view content (https://openstax.org/books/college-physics-2e/pages/20-3-resistance-and-resistivity)