# 15.2 The First Law of Thermodynamics and Some Simple Processes

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

• Describe the processes of a simple heat engine.   
• Explain the differences among the simple thermodynamic processes—isobaric, isochoric, isothermal, and adiabatic.   
• Calculate total work done in a cyclical thermodynamic process.

One of the most important things we can do with heat transfer is to use it to do work for us. Such a device is called a heat engine. Car engines and steam turbines that generate electricity are examples of heat engines. Figure 15.7 shows schematically how the first law of thermodynamics applies to the typical heat engine.

The illustrations above show one of the ways in which heat transfer does work. Fuel combustion produces heat transfer to a gas in a cylinder, increasing the pressure of the gas and thereby the force it exerts on a movable piston. The gas does work on the outside world, as this force moves the piston through some distance. Heat transfer to the gas cylinder results in work being done. To repeat this process, the piston needs to be returned to its starting point. Heat transfer now occurs from the gas to the surroundings so that its pressure decreases, and a force is exerted by the surroundings to push the piston back through some distance. Variations of this process are employed daily in hundreds of millions of heat engines. We will examine heat engines in detail in the next section. In this section, we consider some of the simpler underlying processes on which heat engines are based.

# PVDiagrams and their Relationship to Work Done on or by a Gas

A process by which a gas does work on a piston at constant pressure is called an isobaric process. Since the pressure is constant, the force exerted is constant and the work done is given as

$$
W = F d
$$

See the symbols as shown in Figure 15.9. Now $F = P A$ , and so

$$
W = P A d .
$$

Because the volume of a cylinder is its cross-sectional area $A$ times its length $d$ , we see that $A d = \Delta V$ , the change in volume; thus,

$$
W = P \Delta V { \mathrm { ~ ( i s o b a r i c ~ p r o c e s s ) } } .
$$

Note that if $\Delta V$ is positive, then $W$ is positive, meaning that work is done bythe gas on the outside world.

(Note that the pressure involved in this work that we’ve called $P$ is the pressure of the gas insidethe tank. If we call the pressure outside the tank $P _ { \mathrm { e x t } }$ , an expanding gas would be working againstthe external pressure; the work done would therefore be $W = - P _ { \mathrm { e x t } } \Delta V$ (isobaric process). Many texts use this definition of work, and not the definition based on internal pressure, as the basis of the First Law of Thermodynamics. This definition reverses the sign conventions for work, and results in a statement of the first law that becomes $\Delta U = Q + W .$ .)

It is not surprising that $W = P \Delta V$ , since we have already noted in our treatment of fluids that pressure is a type of potential energy per unit volume and that pressure in fact has units of energy divided by volume. We also noted in our discussion of the ideal gas law that $P V$ has units of energy. In this case, some of the energy associated with pressure becomes work.

Figure 15.10 shows a graph of pressure versus volume (that is, a $P V$ diagram for an isobaric process. You can see in the figure that the work done is the area under the graph. This property of $P V$ diagrams is very useful and broadly applicable:theworkdoneonorbyasystemingoingfromonestatetoanotherequalstheareaunderthecurveona diagram.

We can see where this leads by considering Figure 15.11(a), which shows a more general process in which both pressure and volume change. The area under the curve is closely approximated by dividing it into strips, each having an average constant pressure $P _ { i \mathrm { ( a v e ) } }$ . The work done is $W _ { i } = P _ { i ( \mathrm { a v e } ) } \Delta V _ { i }$ for each strip, and the total work done is the sum of the $W _ { i }$ . Thus the total work done is the total area under the curve. If the path is reversed, as in Figure 15.11(b), then work is done on the system. The area under the curve in that case is negative, because $\Delta V$ is negative.

$P V$ diagrams clearly illustrate that theworkdonedependsonthepathtakenandnotjusttheendpoints. This path dependence is seen in Figure 15.12(a), where more work is done in going from A to C by the path via point B than by the path via point D. The vertical paths, where volume is constant, are called isochoric processes. Since volume is constant, $\Delta V = 0$ , and no work is done in an isochoric process. Now, if the system follows the cyclical path ABCDA, as in Figure 15.12(b), then the total work done is the area inside the loop. The negative area below path CD subtracts, leaving only the area inside the rectangle. In fact, the work done in any cyclical process (one that returns to its starting point) is the area inside the loop it forms on a diagram, as Figure 15.12(c) illustrates for a general cyclical process. Note that the loop must be traversed in the clockwise direction for work to be positive—that is, for

there to be a net work output.

# EXAMPLE 15.2

# Total Work Done in a Cyclical Process Equals the Area Inside the Closed Loop on a PV Diagram

Calculate the total work done in the cyclical process ABCDA shown in Figure 15.12(b) by the following two methods to verify that work equals the area inside the closed loop on the diagram. (Take the data in the figure to be precise to three significant figures.) (a) Calculate the work done along each segment of the path and add these values to get the total work. (b) Calculate the area inside the rectangle ABCDA.

# Strategy

To find the work along any path on a $P V$ diagram, you use the fact that work is pressure times change in volume, or $W = P \Delta V$ . So in part (a), this value is calculated for each leg of the path around the closed loop.

# Solution for (a)

The work along path AB is

$$
\begin{array} { l c l } { { W _ { \mathrm { A B } } } } & { { = } } & { { P _ { \mathrm { A B } } \Delta V _ { \mathrm { A B } } } } \\ { { } } & { { = } } & { { ( 1 . 5 0 \times 1 0 ^ { 6 } ~ \mathrm { N / m ^ { 2 } } ) ( 5 . 0 0 \times 1 0 ^ { - 4 } ~ \mathrm { m ^ { 3 } } ) = 7 5 0 ~ \mathrm { J } . } } \end{array}
$$

Since the path BC is isochoric, $\Delta V _ { \mathrm { B C } } = 0$ , and so $W _ { \mathrm { B C } } = 0$ . The work along path CD is negative, since $\Delta V _ { \mathrm { C D } }$ is negative (the volume decreases). The work is

$$
\begin{array} { l l l } { { W _ { \mathrm { C D } } } } & { { = } } & { { P _ { \mathrm { C D } } \Delta V _ { \mathrm { C D } } } } \\ { { } } & { { = } } & { { ( 2 . 0 0 \times 1 0 ^ { 5 } ~ \mathrm { N / m ^ { 2 } } ) ( - 5 . 0 0 \times 1 0 ^ { - 4 } ~ \mathrm { m ^ { 3 } } ) = - 1 0 0 ~ \mathrm { J } . } } \end{array}
$$

Again, since the path DA is isochoric, $\Delta V _ { \mathrm { D A } } = 0$ , and so $W _ { \mathrm { D A } } = 0$ . Now the total work is

$$
\begin{array} { r c l } { { W } } & { { = } } & { { W _ { \mathrm { A B } } + W _ { \mathrm { B C } } + W _ { \mathrm { C D } } + W _ { \mathrm { D A } } } } \\ { { } } & { { = } } & { { 7 5 0 \mathrm { J } + 0 + ( - 1 0 0 \mathrm { J } ) + 0 = 6 5 0 \mathrm { J } . } } \end{array}
$$

# Solution for (b)

The area inside the rectangle is its height times its width, or

$$
\begin{array} { l l l } { { \mathrm { a r e a } } } & { { = } } & { { ( P _ { \mathrm { A B } } - P _ { \mathrm { C D } } ) \Delta V } } \\ { { } } & { { = } } & { { \Bigl [ ( 1 . 5 0 \times 1 0 ^ { 6 } \ \mathrm { N / m ^ { 2 } } \ ) - ( 2 . 0 0 \times 1 0 ^ { 5 } \ \mathrm { N / m ^ { 2 } } ) \Bigl ] ( 5 . 0 0 \times 1 0 ^ { - 4 } \ \mathrm { m ^ { 3 } } ) } } \\ { { } } & { { = } } & { { 6 5 0 \mathrm { J } . } } \end{array}
$$

Thus,

$$
\mathrm { a r e a } = 6 5 0 { \mathrm { J } } = W .
$$

# Discussion

The result, as anticipated, is that the area inside the closed loop equals the work done. The area is often easier to calculate than is the work done along each path. It is also convenient to visualize the area inside different curves on $P V$ diagrams in order to see which processes might produce the most work. Recall that work can be done to the system, or by the system, depending on the sign of $W$ . A positive $W$ is work that is done by the system on the outside environment; a negative $W$ represents work done by the environment on the system.

Figure 15.13(a) shows two other important processes on a diagram. For comparison, both are shown starting from the same point A. The upper curve ending at point B is an isothermal process—that is, one in which temperature is kept constant. If the gas behaves like an ideal gas, as is often the case, and if no phase change occurs, then $P V = n R T .$ Since $T$ is constant, $P V$ is a constant for an isothermal process. We ordinarily expect the temperature of a gas to decrease as it expands, and so we correctly suspect that heat transfer must occur from the surroundings to the gas to keep the temperature constant during an isothermal expansion. To show this more rigorously for the special case of a monatomic ideal gas, we note that the average kinetic energy of an atom in such a gas is given by

$$
\frac { 1 } { 2 } m \overline { { { v } } } ^ { 2 } = \frac { 3 } { 2 } k T .
$$

The kinetic energy of the atoms in a monatomic ideal gas is its only form of internal energy, and so its total internal energy $U$ is

$$
U = N { \frac { 1 } { 2 } } m { \overline { { v } } } ^ { 2 } = { \frac { 3 } { 2 } } N k T , { \mathrm { ( m o n a t o m i c ~ i d e a l ~ g a s ) } } ,
$$

where $N$ is the number of atoms in the gas. This relationship means that the internal energy of an ideal monatomic gas is constant during an isothermal process—that is, $\Delta U = 0$ . If the internal energy does not change, then the net heat transfer into the gas must equal the net work done by the gas. That is, because $\Delta U = Q - W = 0$ here, $Q = W$ . We must have just enough heat transfer to replace the work done. An isothermal process is inherently slow, because heat transfer occurs continuously to keep the gas temperature constant at all times and must be allowed to spread through the gas so that there are no hot or cold regions.

Note that diatomic gases, such as those in air, have different formulas for average kinetic energy of an atom and total internal energy.

Also shown in Figure 15.13(a) is a curve AC for an adiabatic process, defined to be one in which there is no heat transfer—that is, $Q = 0$ . Processes that are nearly adiabatic can be achieved either by using very effective insulation or by performing the process so fast that there is little time for heat transfer. Temperature must decrease during an adiabatic expansion process, since work is done at the expense of internal energy:

$$
U = { \frac { 3 } { 2 } } N k T .
$$

(You might have noted that a gas released into atmospheric pressure from a pressurized cylinder is substantially colder than the gas in the cylinder.) In fact, because $Q = 0$ ， $\Delta U = - W$ for an adiabatic process. Lower temperature results in lower pressure along the way, so that curve AC is lower than curve AB, and less work is done. If the path ABCA could be followed by cooling the gas from B to C at constant volume (isochorically), Figure 15.13(b), there would be a net work output.

# Reversible Processes

Both isothermal and adiabatic processes such as shown in Figure 15.13 are reversible in principle. A reversible process is one in which both the system and its environment can return to exactly the states they were in by following the reverse path. The reverse isothermal and adiabatic paths are BA and CA, respectively. Real

macroscopic processes are never exactly reversible. In the previous examples, our system is a gas (like that in Figure 15.9), and its environment is the piston, cylinder, and the rest of the universe. If there are any energydissipating mechanisms, such as friction or turbulence, then heat transfer to the environment occurs for either direction of the piston. So, for example, if the path BA is followed and there is friction, then the gas will be returned to its original state but the environment will not—it will have been heated in both directions. Reversibility requires the direction of heat transfer to reverse for the reverse path. Since dissipative mechanisms cannot be completely eliminated, real processes cannot be reversible.

There must be reasons that real macroscopic processes cannot be reversible. We can imagine them going in reverse. For example, heat transfer occurs spontaneously from hot to cold and never spontaneously the reverse. Yet it would not violate the first law of thermodynamics for this to happen. In fact, all spontaneous processes, such as bubbles bursting, never go in reverse. There is a second thermodynamic law that forbids them from going in reverse. When we study this law, we will learn something about nature and also find that such a law limits the efficiency of heat engines. We will find that heat engines with the greatest possible theoretical efficiency would have to use reversible processes, and even they cannot convert all heat transfer into doing work. Table 15.2 summarizes the simpler thermodynamic processes and their definitions.

# PHET EXPLORATIONS

# States of Matter

Watch different types of molecules form a solid, liquid, or gas. Add or remove heat and watch the phase change.   
Change the temperature or volume of a container and see a pressure-temperature diagram respond in real time.   
Relate the interaction potential to the forces between molecules.

Click to view content (https://openstax.org/books/college-physics-2e/pages/15-2-the-first-law-ofthermodynamics-and-some-simple-processes)

#