# 21.2 Electromotive Force: Terminal Voltage

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

• Compare and contrast the voltage and the electromagnetic force of an electric power source. • Describe what happens to the terminal voltage, current, and power delivered to a load as internal resistance of the voltage source increases (due to aging of batteries, for example). • Explain why it is beneficial to use more than one voltage source connected in parallel.

When you forget to turn off your car lights, they slowly dim as the battery runs down. Why don’t they simply blink off when the battery’s energy is gone? Their gradual dimming implies that battery output voltage decreases as the battery is depleted.

Furthermore, if you connect an excessive number of 12-V lights in parallel to a car battery, they will be dim even when the battery is fresh and even if the wires to the lights have very low resistance. This implies that the battery’s output voltage is reduced by the overload.

The reason for the decrease in output voltage for depleted or overloaded batteries is that all voltage sources have two fundamental parts—a source of electrical energy and an internal resistance. Let us examine both.

# Electromotive Force

You can think of many different types of voltage sources. Batteries themselves come in many varieties. There are many types of mechanical/electrical generators, driven by many different energy sources, ranging from nuclear to wind. Solar cells create voltages directly from light, while thermoelectric devices create voltage from temperature differences.

A few voltage sources are shown in Figure 21.8. All such devices create a potential difference and can supply current if connected to a resistance. On the small scale, the potential difference creates an electric field that exerts force on charges, causing current. We thus use the name electromotive force, abbreviated emf.

Emf is not a force at all; it is a special type of potential difference. To be precise, the electromotive force (emf) is the potential difference of a source when no current is flowing. Units of emf are volts.

Electromotive force is directly related to the source of potential difference, such as the particular combination of chemicals in a battery. However, emf differs from the voltage output of the device when current flows. The voltage across the terminals of a battery, for example, is less than the emf when the battery supplies current, and it declines further as the battery is depleted or loaded down. However, if the device’s output voltage can be measured without drawing current, then output voltage will equal emf (even for a very depleted battery).

# Internal Resistance

As noted before, a 12-V truck battery is physically larger, contains more charge and energy, and can deliver a larger current than a $1 2 - \mathsf { V }$ motorcycle battery. Both are lead-acid batteries with identical emf, but, because of its size, the truck battery has a smaller internal resistance $r$ . Internal resistance is the inherent resistance to the flow of current within the source itself.

Figure 21.9 is a schematic representation of the two fundamental parts of any voltage source. The emf (represented by a script E in the figure) and internal resistance $r$ are in series. The smaller the internal resistance for a given emf, the more current and the more power the source can supply.

The internal resistance $r$ can behave in complex ways. As noted, $r$ increases as a battery is depleted. But internal resistance may also depend on the magnitude and direction of the current through a voltage source, its temperature, and even its history. The internal resistance of rechargeable nickel-cadmium cells, for example, depends on how many times and how deeply they have been depleted.

# Things Great and Small: The Submicroscopic Origin of Battery Potential

Various types of batteries are available, with emfs determined by the combination of chemicals involved. We can view this as a molecular reaction (what much of chemistry is about) that separates charge.

The lead-acid battery used in cars and other vehicles is one of the most common types. A single cell (one of six) of this battery is seen in Figure 21.10. The cathode (positive) terminal of the cell is connected to a lead oxide plate, while the anode (negative) terminal is connected to a lead plate. Both plates are immersed in sulfuric acid, the electrolyte for the system.

The details of the chemical reaction are left to the reader to pursue in a chemistry text, but their results at the molecular level help explain the potential created by the battery. Figure 21.11 shows the result of a single chemical reaction. Two electrons are placed on the anode, making it negative, provided that the cathode supplied two electrons. This leaves the cathode positively charged, because it has lost two electrons. In short, a separation of charge has been driven by a chemical reaction.

Note that the reaction will not take place unless there is a complete circuit to allow two electrons to be supplied to the cathode. Under many circumstances, these electrons come from the anode, flow through a resistance, and return to the cathode. Note also that since the chemical reactions involve substances with resistance, it is not possible to create the emf without an internal resistance.

Why are the chemicals able to produce a unique potential difference? Quantum mechanical descriptions of molecules, which take into account the types of atoms and numbers of electrons in them, are able to predict the energy states they can have and the energies of reactions between them.

In the case of a lead-acid battery, an energy of $2 \mathsf { e V }$ is given to each electron sent to the anode. Voltage is defined as the electrical potential energy divided by charge: $V = { \frac { P _ { \mathrm { E } } } { q } } $ . An electron volt is the energy given to a single electron by a voltage of 1 V. So the voltage here is $2 \mathsf { V }$ , since $2 \mathsf { e V }$ is given to each electron. It is the energy produced in each molecular reaction that produces the voltage. A different reaction produces a different energy and, hence, a different voltage.

# Terminal Voltage

The voltage output of a device is measured across its terminals and, thus, is called its terminal voltage . Terminal voltage is given by

$$
V = \mathrm { e m f } - I r ,
$$

where $r$ is the internal resistance and $I$ is the current flowing at the time of the measurement.

$I$ is positive if current flows away from the positive terminal, as shown in Figure 21.9. You can see that the larger the current, the smaller the terminal voltage. And it is likewise true that the larger the internal resistance, the smaller the terminal voltage.

Suppose a load resistance $R _ { \mathrm { l o a d } }$ is connected to a voltage source, as in Figure 21.12. Since the resistances are in series, the total resistance in the circuit is $R _ { \mathrm { l o a d } } + r$ . Thus the current is given by Ohm’s law to be

$$
I = \frac { \mathrm { e m f } } { R _ { \mathrm { l o a d } } + r } .
$$

We see from this expression that the smaller the internal resistance $r$ , the greater the current the voltage source supplies to its load $R _ { \mathrm { l o a d } }$ . As batteries are depleted, $r$ increases. If $r$ becomes a significant fraction of the load resistance, then the current is significantly reduced, as the following example illustrates.

# Calculating Terminal Voltage, Power Dissipation, Current, and Resistance: Terminal Voltage and Load

A certain battery has a 12.0-V emf and an internal resistance of $0 . 1 0 0 \Omega$ . (a) Calculate its terminal voltage when connected to a load. (b) What is the terminal voltage when connected to a load? (c) What power does the $0 . 5 0 0 – \Omega$ load dissipate? (d) If the internal resistance grows to $0 . 5 0 0 \Omega$ , find the current, terminal voltage, and power dissipated by a load.

# Strategy

The analysis above gave an expression for current when internal resistance is taken into account. Once the current is found, the terminal voltage can be calculated using the equation $V = \mathrm { e m f } - I r$ . Once current is found, the power dissipated by a resistor can also be found.

# Solution for (a)

Entering the given values for the emf, load resistance, and internal resistance into the expression above yields

$$
I = { \frac { \mathrm { e m f } } { R _ { \mathrm { l o a d } } + r } } = { \frac { 1 2 . 0 \mathrm { V } } { 1 0 . 1 \Omega } } = 1 . 1 8 8 \mathrm { A } .
$$

Enter the known values into the equation $V = \mathrm { e m f } - I r$ to get the terminal voltage:

$$
\begin{array} { l l l } { { V } } & { { = } } & { { \mathrm { e m f } - I r = 1 2 . 0 \mathrm { V } - ( 1 . 1 8 8 \mathrm { A } ) ( 0 . 1 0 0 \Omega ) } } \\ { { } } & { { = } } & { { 1 1 . 9 \mathrm { V } . } } \end{array}
$$

# Discussion for (a)

The terminal voltage here is only slightly lower than the emf, implying that $1 0 . 0 \Omega$ is a light load for this particular battery.

# Solution for (b)

Similarly, with $R _ { \mathrm { l o a d } } = 0 . 5 0 0 \Omega$ , the current is

$$
I = { \frac { \mathrm { e m f } } { R _ { \mathrm { l o a d } } + r } } = { \frac { 1 2 . 0 ~ { \mathrm { V } } } { 0 . 6 0 0 \Omega } } = 2 0 . 0 ~ { \mathrm { A } } .
$$

The terminal voltage is now

$$
{ \begin{array} { l l l } { V } & { = } & { \operatorname { e m f } - I r = 1 2 . 0 \mathrm { V } - ( 2 0 . 0 \mathrm { A } ) ( 0 . 1 0 0 \Omega ) } \\ & { = } & { 1 0 . 0 \mathrm { V } . } \end{array} }
$$

# Discussion for (b)

This terminal voltage exhibits a more significant reduction compared with emf, implying $0 . 5 0 0 \Omega$ is a heavy load for this battery.

# Solution for (c)

The power dissipated by the $0 . 5 0 0 \textrm { - } \Omega$ load can be found using the formula $P = I ^ { 2 } R$ . Entering the known values gives

$$
P _ { \mathrm { l o a d } } = I ^ { 2 } R _ { \mathrm { l o a d } } = ( 2 0 . 0 ~ \mathrm { A } ) ^ { 2 } ( 0 . 5 0 0 ~ \Omega ) = 2 . 0 0 \times 1 0 ^ { 2 } ~ \mathrm { W } .
$$

# Discussion for (c)

Note that this power can also be obtained using the expressions $\textstyle { \frac { V ^ { 2 } } { R } }$ or $I V ,$ where $V$ is the terminal voltage (10.0 V in this case).

# Solution for (d)

Here the internal resistance has increased, perhaps due to the depletion of the battery, to the point where it is as great as the load resistance. As before, we first find the current by entering the known values into the expression, yielding

$$
I = { \frac { \mathrm { e m f } } { R _ { \mathrm { l o a d } } + r } } = { \frac { 1 2 . 0 ~ \mathrm { V } } { 1 . 0 0 ~ \Omega } } = 1 2 . 0 ~ \mathrm { A } .
$$

Now the terminal voltage is

$$
\begin{array} { l l l } { { V } } & { { = } } & { { \mathrm { e m f } - I r = 1 2 . 0 \mathrm { V } \mathrm { - } ( 1 2 . 0 \mathrm { A } ) ( 0 . 5 0 0 \Omega ) } } \\ { { } } & { { = } } & { { 6 . 0 0 \mathrm { V } , } } \end{array}
$$

and the power dissipated by the load is

$$
P _ { \mathrm { l o a d } } = I ^ { 2 } R _ { \mathrm { l o a d } } = ( 1 2 . 0 \mathrm { \ A } ) ^ { 2 } ( 0 . 5 0 0 \Omega ) = 7 2 . 0 \mathrm { \ W } .
$$

# Discussion for (d)

We see that the increased internal resistance has significantly decreased terminal voltage, current, and power delivered to a load.

Battery testers, such as those in Figure 21.13, use small load resistors to intentionally draw current to determine whether the terminal voltage drops below an acceptable level. They really test the internal resistance of the battery. If internal resistance is high, the battery is weak, as evidenced by its low terminal voltage.

Some batteries can be recharged by passing a current through them in the direction opposite to the current they supply to a resistance. This is done routinely in cars and batteries for small electrical appliances and electronic devices, and is represented pictorially in Figure 21.14. The voltage output of the battery charger must be greater than the emf of the battery to reverse current through it. This will cause the terminal voltage of the battery to be greater than the emf, since $V = \mathrm { e m f } - I r$ , and $I$ is now negative.

# Multiple Voltage Sources

There are two voltage sources when a battery charger is used. Voltage sources connected in series are relatively simple. When voltage sources are in series, their internal resistances add and their emfs add algebraically. (See

Figure 21.15.) Series connections of voltage sources are common—for example, in flashlights, toys, and other appliances. Usually, the cells are in series in order to produce a larger total emf.

But if the cells oppose one another, such as when one is put into an appliance backward, the total emf is less, since it is the algebraic sum of the individual emfs.

A battery is a multiple connection of voltaic cells, as shown in Figure 21.16. The disadvantage of series connections of cells is that their internal resistances add. One of the authors once owned a 1957 MGA that had two 6-V batteries in series, rather than a single 12-V battery. This arrangement produced a large internal resistance that caused him many problems in starting the engine.

If the seriesconnection of two voltage sources is made into a complete circuit with the emfs in opposition, then a current of magnitude flows. See Figure 21.17, for example, which shows a circuit exactly analogous to the battery charger discussed above. If two voltage sources in series with emfs in the same sense are connected to a load $R _ { \mathrm { l o a d } }$ , as in Figure 21.18, then $I = \frac { ( \mathrm { e m f } _ { 1 } + \mathrm { e m f } _ { 2 } ) } { r _ { 1 } + r _ { 2 } + R _ { \mathrm { l o a d } } }$ flows.

# Take-Home Experiment: Flashlight Batteries

Find a flashlight that uses several batteries and find new and old batteries. Based on the discussions in this module, predict the brightness of the flashlight when different combinations of batteries are used. Do your predictions match what you observe? Now place new batteries in the flashlight and leave the flashlight switched on for several hours. Is the flashlight still quite bright? Do the same with the old batteries. Is the flashlight as bright when left on for the same length of time with old and new batteries? What does this say for the case when you are limited in the number of available new batteries?

Figure 21.19 shows two voltage sources with identical emfs in parallel and connected to a load resistance. In this simple case, the total emf is the same as the individual emfs. But the total internal resistance is reduced, since the internal resistances are in parallel. The parallel connection thus can produce a larger current.

Here, $I = \frac { \mathrm { e m f } } { \left( r _ { \mathrm { t o t } } + R _ { \mathrm { l o a d } } \right) }$ flows through the load, and $r _ { \mathrm { t o t } }$ is less than those of the individual batteries. For example, some diesel-powered cars use two $1 2 - \mathsf { V }$ batteries in parallel; they produce a total emf of $\boldsymbol { \mathsf { 1 2 V } }$ but can deliver the larger current needed to start a diesel engine.

# Animals as Electrical Detectors

A number of animals both produce and detect electrical signals. Fish, sharks, platypuses, and echidnas (spiny anteaters) all detect electric fields generated by nerve activity in prey. Electric eels produce their own emf through biological cells (electric organs) called electroplaques, which are arranged in both series and parallel as a set of batteries.

Electroplaques are flat, disk-like cells; those of the electric eel have a voltage of 0.15 V across each one. These cells are usually located toward the head or tail of the animal, although in the case of the electric eel, they are found along the entire body. The electroplaques in the South American eel are arranged in 140 rows, with each row stretching horizontally along the body and containing 5,000 electroplaques. This can yield an emf of approximately $6 0 0 \mathsf { V } ,$ , and a current of 1 A—deadly.



The mechanism for detection of external electric fields is similar to that for producing nerve signals in the cell through depolarization and repolarization—the movement of ions across the cell membrane. Within the fish, weak electric fields in the water produce a current in a gel-filled canal that runs from the skin to sensing cells, producing a nerve signal. The Australian platypus, one of the very few mammals that lay eggs, can detect fields of $3 0 \ \frac { \mathrm { m V } } { \mathrm { m } }$ , while sharks have been found to be able to sense a field in their snouts as small as 100 $\textstyle \frac { \mathrm { m V } } { \mathrm { m } }$ (Figure 21.20). Electric eels use their own electric fields produced by the electroplaques to stun their prey or enemies.

# Solar Cell Arrays

Another example dealing with multiple voltage sources is that of combinations of solar cells—wired in both series and parallel combinations to yield a desired voltage and current. Photovoltaic generation (PV), the conversion of sunlight directly into electricity, is based upon the photoelectric effect, in which photons hitting the surface of a solar cell create an electric current in the cell.

Most solar cells are made from pure silicon—either as single-crystal silicon, or as a thin film of silicon deposited upon a glass or metal backing. Most single cells have a voltage output of about 0.5 V, while the current output is a function of the amount of sunlight upon the cell (the incident solar radiation—the insolation). Under bright noon sunlight, a current of about $1 0 0 \mathrm { m A } / \mathrm { c m } ^ { 2 }$ of cell surface area is produced by typical single-crystal cells.

Individual solar cells are connected electrically in modules to meet electrical-energy needs. They can be wired together in series or in parallel—connected like the batteries discussed earlier. A solar-cell array or module usually consists of between 36 and 72 cells, with a power output of 50 W to 140 W.

The output of the solar cells is direct current. For most uses in a home, AC is required, so a device called an inverter must be used to convert the DC to AC. Any extra output can then be passed on to the outside electrical grid for sale to the utility.

# Take-Home Experiment: Virtual Solar Cells

One can assemble a “virtual” solar cell array by using playing cards, or business or index cards, to represent a solar cell. Combinations of these cards in series and/or parallel can model the required array output. Assume each card has an output of $0 . 5 \ : \forall$ and a current (under bright light) of 2 A. Using your cards, how would you

arrange them to produce an output of 6 A at 3 V (18 W)?

Suppose you were told that you needed only 18 W (but no required voltage). Would you need more cards to make this arrangement?