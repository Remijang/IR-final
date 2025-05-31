# 21.1 Resistors in Series and Parallel

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

• Draw a circuit with resistors in parallel and in series.   
• Calculate the voltage drop of a current across a resistor using Ohm’s law.   
• Contrast the way total resistance is calculated for resistors in series and in parallel.   
• Explain why total resistance of a parallel circuit is less than the smallest resistance of any of the resistors in that circuit.   
• Calculate total resistance of a circuit that contains a mixture of resistors connected in series and in parallel.

Most circuits have more than one component, called a resistor that limits the flow of charge in the circuit. A measure of this limit on charge flow is called resistance. The simplest combinations of resistors are the series and parallel connections illustrated in Figure 21.2. The total resistance of a combination of resistors depends on both their individual values and how they are connected.

# Resistors in Series

When are resistors in series? Resistors are in series whenever the flow of charge, called the current, must flow through devices sequentially. For example, if current flows through a person holding a screwdriver and into the Earth, then $R _ { 1 }$ in Figure 21.2(a) could be the resistance of the screwdriver’s shaft, $R _ { 2 }$ the resistance of its handle, $R _ { 3 }$ the person’s body resistance, and $R _ { 4 }$ the resistance of her shoes.

Figure 21.3 shows resistors in series connected to a voltage source. It seems reasonable that the total resistance is the sum of the individual resistances, considering that the current has to pass through each resistor in sequence. (This fact would be an advantage to a person wishing to avoid an electrical shock, who could reduce the current by wearing high-resistance rubber-soled shoes. It could be a disadvantage if one of the resistances were a faulty highresistance cord to an appliance that would reduce the operating current.)

To verify that resistances in series do indeed add, let us consider the loss of electrical power, called a voltage drop, in each resistor in Figure 21.3.

According to Ohm’s law, the voltage drop, $V$ , across a resistor when a current flows through it is calculated using the equation $V = I R$ , where $I$ equals the current in amps (A) and $R$ is the resistance in ohms $( \Omega )$ . Another way to think of this is that $V$ is the voltage necessary to make a current $I$ flow through a resistance $R$ .



So the voltage drop across $R _ { 1 }$ is $V _ { 1 } = I R _ { 1 }$ , that across $R _ { 2 }$ is $V _ { 2 } = I R _ { 2 }$ , and that across $R _ { 3 }$ is $V _ { 3 } = I R _ { 3 }$ . The sum of these voltages equals the voltage output of the source; that is,

$$
V = V _ { 1 } + V _ { 2 } + V _ { 3 } .
$$

This equation is based on the conservation of energy and conservation of charge. Electrical potential energy can be described by the equation $\begin{array} { r } { P E = q V , } \end{array}$ where $q$ is the electric charge and $V$ is the voltage. Thus the energy supplied by the source is $q V ,$ while that dissipated by the resistors is

$$
q V _ { 1 } + q V _ { 2 } + q V _ { 3 } .
$$

# Connections: Conservation Laws

The derivations of the expressions for series and parallel resistance are based on the laws of conservation of energy and conservation of charge, which state that total charge and total energy are constant in any process. These two laws are directly involved in all electrical phenomena and will be invoked repeatedly to explain both specific effects and the general behavior of electricity.

These energies must be equal, because there is no other source and no other destination for energy in the circuit. Thus, $q V = q V _ { 1 } + q V _ { 2 } + q V _ { 3 }$ . The charge $q$ cancels, yielding $V = V _ { 1 } + V _ { 2 } + V _ { 3 }$ , as stated. (Note that the same amount of charge passes through the battery and each resistor in a given amount of time, since there is no capacitance to store charge, there is no place for charge to leak, and charge is conserved.)

Now substituting the values for the individual voltages gives

$$
V = I R _ { 1 } + I R _ { 2 } + I R _ { 3 } = I ( R _ { 1 } + R _ { 2 } + R _ { 3 } ) .
$$

Note that for the equivalent single series resistance $R _ { \mathrm { s } }$ , we have

$$
V = I R _ { \mathrm { s } } .
$$

This implies that the total or equivalent series resistance $R _ { \mathrm { s } }$ of three resistors is $R _ { \mathrm { s } } = R _ { 1 } + R _ { 2 } + R _ { 3 }$ .

This logic is valid in general for any number of resistors in series; thus, the total resistance $R _ { \mathrm { s } }$ of a series connection is

$$
R _ { \mathrm { s } } = R _ { 1 } + R _ { 2 } + R _ { 3 } + . . . ,
$$

as proposed. Since all of the current must pass through each resistor, it experiences the resistance of each, and resistances in series simply add up.

# EXAMPLE 21.1

# Calculating Resistance, Current, Voltage Drop, and Power Dissipation: Analysis of a Series Circuit

Suppose the voltage output of the battery in Figure 21.3 is $1 2 . 0 \mathrm { V }$ , and the resistances are $R _ { 1 } = 1 . 0 0 \Omega$ , $R _ { 2 } = 6 . 0 0 \Omega$ , and $R _ { 3 } = 1 3 . 0 \Omega$ . (a) What is the total resistance? (b) Find the current. (c) Calculate the voltage drop in each resistor, and show these add to equal the voltage output of the source. (d) Calculate the power dissipated by each resistor. (e) Find the power output of the source, and show that it equals the total power dissipated by the resistors.

# Strategy and Solution for (a)

The total resistance is simply the sum of the individual resistances, as given by this equation:

$$
\begin{array} { l l l } { { R _ { \mathrm { s } } } } & { { = } } & { { R _ { 1 } + R _ { 2 } + R _ { 3 } } } \\ { { } } & { { = } } & { { 1 . 0 0 \Omega + 6 . 0 0 \Omega + 1 3 . 0 \Omega } } \\ { { } } & { { = } } & { { 2 0 . 0 \Omega . } } \end{array}
$$

# Strategy and Solution for (b)

The current is found using Ohm’s law, $V = I R$ . Entering the value of the applied voltage and the total resistance yields the current for the circuit:

$$
I = { \frac { V } { R _ { \mathrm { s } } } } = { \frac { 1 2 . 0 { \mathrm { ~ V } } } { 2 0 . 0 { \Omega } } } = 0 . 6 0 0 { \mathrm { ~ A } } .
$$

# Strategy and Solution for (c)

The voltage—or $I R$ drop—in a resistor is given by Ohm’s law. Entering the current and the value of the first resistance yields

$$
V _ { 1 } = I R _ { 1 } = ( 0 . 6 0 0 \mathrm { A } ) ( 1 . 0 \Omega ) = 0 . 6 0 0 \mathrm { V } .
$$

Similarly,

$$
V _ { 2 } = I R _ { 2 } = ( 0 . 6 0 0 \mathrm { A } ) ( 6 . 0 \Omega ) = 3 . 6 0 \mathrm { V }
$$

and

$$
V _ { 3 } = I R _ { 3 } = ( 0 . 6 0 0 \mathrm { A } ) ( 1 3 . 0 \Omega ) = 7 . 8 0 \mathrm { V } .
$$

# Discussion for (c)

The three $I R$ drops add to $1 2 . 0 \mathrm { V }$ , as predicted:

$$
V _ { 1 } + V _ { 2 } + V _ { 3 } = ( 0 . 6 0 0 + 3 . 6 0 + 7 . 8 0 ) \mathrm { V } = 1 2 . 0 \mathrm { V } .
$$

# Strategy and Solution for (d)

The easiest way to calculate power in watts (W) dissipated by a resistor in a DC circuit is to use Joule’s law, $P = I V ,$ where $P$ is electric power. In this case, each resistor has the same full current flowing through it. By substituting Ohm’s law $V = I R$ into Joule’s law, we get the power dissipated by the first resistor as

$$
P _ { 1 } = I ^ { 2 } R _ { 1 } = ( 0 . 6 0 0 \mathrm { \ A } ) ^ { 2 } ( 1 . 0 0 \Omega ) = 0 . 3 6 0 \mathrm { \ W } .
$$

Similarly,

$$
P _ { 2 } = I ^ { 2 } R _ { 2 } = ( 0 . 6 0 0 \mathrm { A } ) ^ { 2 } ( 6 . 0 0 \Omega ) = 2 . 1 6 \mathrm { W }
$$

and

$$
P _ { 3 } = I ^ { 2 } R _ { 3 } = ( 0 . 6 0 0 \mathrm { A } ) ^ { 2 } ( 1 3 . 0 \Omega ) = 4 . 6 8 \mathrm { W } .
$$

# Discussion for (d)

Power can also be calculated using either or , where $V$ is the voltage drop across the resistor (not the full voltage of the source). The same values will be obtained.

# Strategy and Solution for (e)

The easiest way to calculate power output of the source is to use $P = I V ,$ where $V$ is the source voltage. This gives

$$
P = ( 0 . 6 0 0 \mathrm { \ A } ) ( 1 2 . 0 \mathrm { \ V } ) = 7 . 2 0 \mathrm { \ W } .
$$

# Discussion for (e)

Note, coincidentally, that the total power dissipated by the resistors is also 7.20 W, the same as the power put out by the source. That is,

$$
P _ { 1 } + P _ { 2 } + P _ { 3 } = ( 0 . 3 6 0 + 2 . 1 6 + 4 . 6 8 ) \mathrm { W } = 7 . 2 0 \mathrm { W } .
$$

Power is energy per unit time (watts), and so conservation of energy requires the power output of the source to be equal to the total power dissipated by the resistors.

# Major Features of Resistors in Series

1. Series resistances add: $R _ { \mathrm { s } } = R _ { 1 } + R _ { 2 } + R _ { 3 } + . . . .$   
2. The same current flows through each resistor in series.   
3. Individual resistors in series do not get the total source voltage, but divide it.

# Resistors in Parallel

Figure 21.4 shows resistors in parallel, wired to a voltage source. Resistors are in parallel when each resistor is connected directly to the voltage source by connecting wires having negligible resistance. Each resistor thus has the full voltage of the source applied to it.

Each resistor draws the same current it would if it alone were connected to the voltage source (provided the voltage source is not overloaded). For example, an automobile’s headlights, radio, and so on, are wired in parallel, so that they utilize the full voltage of the source and can operate completely independently. The same is true in your house, or any building. (See Figure 21.4(b).)

To find an expression for the equivalent parallel resistance $R _ { \mathrm { p } }$ , let us consider the currents that flow and how they are related to resistance. Since each resistor in the circuit has the full voltage, the currents flowing through the $\begin{array} { r } { I _ { 1 } = \frac { V } { R _ { 1 } } , I _ { 2 } = \frac { V } { R _ { 2 } } } \end{array}$ , and . Conservation of charge implies that the total current produced by the source is the sum of these currents:

$$
I = I _ { 1 } + I _ { 2 } + I _ { 3 } .
$$

Substituting the expressions for the individual currents gives

$$
I = { \frac { V } { R _ { 1 } } } + { \frac { V } { R _ { 2 } } } + { \frac { V } { R _ { 3 } } } = V \Bigg ( { \frac { 1 } { R _ { 1 } } } + { \frac { 1 } { R _ { 2 } } } + { \frac { 1 } { R _ { 3 } } } \Bigg ) .
$$

Note that Ohm’s law for the equivalent single resistance gives

$$
I = { \frac { V } { R _ { \mathrm { p } } } } = V \left( { \frac { 1 } { R _ { \mathrm { p } } } } \right) .
$$

The terms inside the parentheses in the last two equations must be equal. Generalizing to any number of resistors, the total resistance $R _ { \mathrm { p } }$ of a parallel connection is related to the individual resistances by

$$
{ \frac { 1 } { R _ { \mathrm { p } } } } = { \frac { 1 } { R _ { 1 } } } + { \frac { 1 } { R _ { 2 } } } + { \frac { 1 } { R _ { . 3 } } } + \ldots
$$

This relationship results in a total resistance $R _ { \mathrm { p } }$ that is less than the smallest of the individual resistances. (This is seen in the next example.) When resistors are connected in parallel, more current flows from the source than would flow for any of them individually, and so the total resistance is lower.

# EXAMPLE 21.2

# Calculating Resistance, Current, Power Dissipation, and Power Output: Analysis of a Paralle Circuit

Let the voltage output of the battery and resistances in the parallel connection in Figure 21.4 be the same as the previously considered series connection: $V = 1 2 . 0 \ : \mathrm { V }$ , $R _ { 1 } = 1 . 0 0 \Omega$ , $R _ { 2 } = 6 . 0 0 \Omega$ , and $R _ { 3 } = 1 3 . 0 \Omega$ . (a) What is the total resistance? (b) Find the total current. (c) Calculate the currents in each resistor, and show these add to equal the total current output of the source. (d) Calculate the power dissipated by each resistor. (e) Find the power output of the source, and show that it equals the total power dissipated by the resistors.

# Strategy and Solution for (a)

The total resistance for a parallel combination of resistors is found using the equation below. Entering known values gives

$$
\frac { 1 } { R _ { \mathrm { p } } } = \frac { 1 } { R _ { 1 } } + \frac { 1 } { R _ { 2 } } + \frac { 1 } { R _ { 3 } } = \frac { 1 } { 1 . 0 0 \Omega } + \frac { 1 } { 6 . 0 0 \Omega } + \frac { 1 } { 1 3 . 0 \Omega } .
$$

Thus,

$$
\frac { 1 } { R _ { \mathrm { p } } } = \frac { 1 . 0 0 } { \Omega } + \frac { 0 . 1 6 6 7 } { \Omega } + \frac { 0 . 0 7 6 9 2 } { \Omega } = \frac { 1 . 2 4 3 6 } { \Omega } .
$$

(Note that in these calculations, each intermediate answer is shown with an extra digit.)

We must invert this to find the total resistance $R _ { \mathrm { p } }$ . This yields

$$
R _ { \mathrm { p } } = { \frac { 1 } { 1 . 2 4 3 6 } } \Omega = 0 . 8 0 4 1 \Omega .
$$

The total resistance with the correct number of significant digits is $R _ { \mathrm { p } } = 0 . 8 0 4 \Omega$ -

# Discussion for (a)

$R _ { \mathrm { p } }$ is, as predicted, less than the smallest individual resistance.

# Strategy and Solution for (b)

The total current can be found from Ohm’s law, substituting $R _ { \mathrm { p } }$ for the total resistance. This gives

$$
I = { \frac { V } { R _ { \mathrm { p } } } } = { \frac { 1 2 . 0 { \mathrm { V } } } { 0 . 8 0 4 1 \ \Omega } } = 1 4 . 9 2 \mathrm { A } .
$$

# Discussion for (b)

Current $I$ for each device is much larger than for the same devices connected in series (see the previous example). A circuit with parallel connections has a smaller total resistance than the resistors connected in series.

# Strategy and Solution for (c)

The individual currents are easily calculated from Ohm’s law, since each resistor gets the full voltage. Thus,

$$
I _ { 1 } = { \frac { V } { R _ { 1 } } } = { \frac { 1 2 . 0 ~ \mathrm { V } } { 1 . 0 0 \Omega } } = 1 2 . 0 ~ \mathrm { A } .
$$

Similarly,

$$
I _ { 2 } = { \frac { V } { R _ { 2 } } } = { \frac { 1 2 . 0 ~ \mathrm { V } } { 6 . 0 0 \Omega } } = 2 . 0 0 ~ \mathrm { A }
$$

and

$$
I _ { 3 } = { \frac { V } { R _ { 3 } } } = { \frac { 1 2 . 0 ~ \mathrm { V } } { 1 3 . 0 \Omega } } = 0 . 9 2 ~ \mathrm { A } .
$$

# Discussion for (c)

The total current is the sum of the individual currents:

$$
I _ { 1 } + I _ { 2 } + I _ { 3 } = 1 4 . 9 2 \mathrm { A } .
$$

This is consistent with conservation of charge.

# Strategy and Solution for (d)

The power dissipated by each resistor can be found using any of the equations relating power to current, voltage, and resistance, since all three are known. Let us use , since each resistor gets full voltage. Thus,

$$
P _ { 1 } = { \frac { V ^ { 2 } } { R _ { 1 } } } = { \frac { ( 1 2 . 0 ~ \mathrm { V } ) ^ { 2 } } { 1 . 0 0 ~ \Omega } } = 1 4 4 ~ \mathrm { W } .
$$

Similarly,

$$
P _ { 2 } = { \frac { V ^ { 2 } } { R _ { 2 } } } = { \frac { ( 1 2 . 0 ~ \mathrm { V } ) ^ { 2 } } { 6 . 0 0 ~ \Omega } } = 2 4 . 0 ~ \mathrm { W }
$$

and

$$
P _ { 3 } = { \frac { V ^ { 2 } } { R _ { 3 } } } = { \frac { ( 1 2 . 0 ~ \mathrm { V } ) ^ { 2 } } { 1 3 . 0 ~ \Omega } } = 1 1 . 1 ~ \mathrm { W } .
$$

# Discussion for (d)

The power dissipated by each resistor is considerably higher in parallel than when connected in series to the same voltage source.

# Strategy and Solution for (e)

The total power can also be calculated in several ways. Choosing $P = I V ,$ and entering the total current, yields

$$
P = I V = ( 1 4 . 9 2 \mathrm { ~ A } ) ( 1 2 . 0 \mathrm { ~ V } ) = 1 7 9 \mathrm { ~ W } .
$$

# Discussion for (e)

Total power dissipated by the resistors is also 179 W:

$$
P _ { 1 } + P _ { 2 } + P _ { 3 } = 1 4 4 \mathrm { W } + 2 4 . 0 \mathrm { W } + 1 1 . 1 \mathrm { W } = 1 7 9 \mathrm { W } .
$$

This is consistent with the law of conservation of energy.

# Overall Discussion

Note that both the currents and powers in parallel connections are greater than for the same devices in series.

# Major Features of Resistors in Parallel

1. Parallel resistance is found from $\begin{array} { r } { \frac { 1 } { R _ { \mathrm { p } } } = \frac { 1 } { R _ { 1 } } + \frac { 1 } { R _ { 2 } } + \frac { 1 } { R _ { 3 } } + . . . , } \end{array}$ and it is smaller than any individual resistance in the combination.   
2. Each resistor in parallel has the same full voltage of the source applied to it. (Power distribution systems most often use parallel connections to supply the myriad devices served with the same voltage and to allow them to operate independently.)   
3. Parallel resistors do not each get the total current; they divide it.

# Combinations of Series and Parallel

More complex connections of resistors are sometimes just combinations of series and parallel. These are commonly encountered, especially when wire resistance is considered. In that case, wire resistance is in series with other resistances that are in parallel.

Combinations of series and parallel can be reduced to a single equivalent resistance using the technique illustrated in Figure 21.5. Various parts are identified as either series or parallel, reduced to their equivalents, and further reduced until a single resistance is left. The process is more time consuming than difficult.

The simplest combination of series and parallel resistance, shown in Figure 21.6, is also the most instructive, since it is found in many applications. For example, $R _ { 1 }$ could be the resistance of wires from a car battery to its electrical devices, which are in parallel. $R _ { 2 }$ and $R _ { 3 }$ could be the starter motor and a passenger compartment light. We have previously assumed that wire resistance is negligible, but, when it is not, it has important effects, as the next example indicates.

# Calculating Resistance, $I R$ Drop, Current, and Power Dissipation: Combining Series and Parallel Circuits

Figure $2 1 . 6$ shows the resistors from the previous two examples wired in a different way—a combination of series and parallel. We can consider $R _ { 1 }$ to be the resistance of wires leading to $R _ { 2 }$ and $R _ { 3 }$ . (a) Find the total resistance. (b) What is the $I R$ drop in $R _ { 1 } ?$ (c) Find the current $I _ { 2 }$ through $R _ { 2 }$ . (d) What power is dissipated by $R _ { 2 }$ ?

# Strategy and Solution for (a)

To find the total resistance, we note that $R _ { 2 }$ and $R _ { 3 }$ are in parallel and their combination $R _ { \mathrm { p } }$ is in series with $R _ { 1 }$ . Thus the total (equivalent) resistance of this combination is

$$
\begin{array} { r } { R _ { \mathrm { t o t } } = R _ { 1 } + R _ { \mathrm { p } } . } \end{array}
$$

First, we find $R _ { \mathrm { p } }$ using the equation for resistors in parallel and entering known values:

$$
\frac { 1 } { R _ { \mathrm { p } } } = \frac { 1 } { R _ { 2 } } + \frac { 1 } { R _ { 3 } } = \frac { 1 } { 6 . 0 0 \Omega } + \frac { 1 } { 1 3 . 0 \Omega } = \frac { 0 . 2 4 3 6 } { \Omega } .
$$

Inverting gives

$$
R _ { \mathrm { p } } = { \frac { 1 } { 0 . 2 4 3 6 } } \Omega = 4 . 1 1 \Omega .
$$

So the total resistance is

$$
R _ { \mathrm { t o t } } = R _ { 1 } + R _ { \mathrm { p } } = 1 . 0 0 \Omega + 4 . 1 1 \Omega = 5 . 1 1 \Omega .
$$

# Discussion for (a)

The total resistance of this combination is intermediate between the pure series and pure parallel values $( 2 0 . 0 \Omega$ and $0 . 8 0 4 \Omega$ , respectively) found for the same resistors in the two previous examples.

# Strategy and Solution for (b)

To find the $I R$ drop in $R _ { 1 }$ , we note that the full current $I$ flows through $R _ { 1 }$ . Thus its $I R$ drop is

$$
V _ { 1 } = I R _ { 1 } .
$$

We must find $I$ before we can calculate $V _ { 1 }$ . The total current $I$ is found using Ohm’s law for the circuit. That is,

$$
I = { \frac { V } { R _ { \mathrm { t o t } } } } = { \frac { 1 2 . 0 ~ { \mathrm { V } } } { 5 . 1 1 ~ { \Omega } } } = 2 . 3 5 ~ { \mathrm { A } } .
$$

Entering this into the expression above, we get

$$
V _ { 1 } = I R _ { 1 } = ( 2 . 3 5 \mathrm { ~ A } ) ( 1 . 0 0 \Omega ) = 2 . 3 5 \mathrm { ~ V } .
$$

# Discussion for (b)

The voltage applied to $R _ { 2 }$ and $R _ { 3 }$ is less than the total voltage by an amount $V _ { 1 }$ . When wire resistance is large, it can significantly affect the operation of the devices represented by $R _ { 2 }$ and $R _ { 3 }$ .

# Strategy and Solution for (c)

To find the current through $R _ { 2 }$ , we must first find the voltage applied to it. We call this voltage $V _ { \mathfrak { p } }$ , because it is applied to a parallel combination of resistors. The voltage applied to both $R _ { 2 }$ and $R _ { 3 }$ is reduced by the amount $V _ { 1 }$ , and so it is

$$
V _ { \mathrm { p } } = V - V _ { \mathrm { 1 } } = 1 2 . 0 \mathrm { V } - 2 . 3 5 \mathrm { V } = 9 . 6 5 \mathrm { V } .
$$

Now the current $I _ { 2 }$ through resistance $R _ { 2 }$ is found using Ohm’s law:

$$
I _ { 2 } = { \frac { V _ { \mathrm { p } } } { R _ { 2 } } } = { \frac { 9 . 6 5 \mathrm { \ V } } { 6 . 0 0 \Omega } } = 1 . 6 1 \mathrm { \ A } .
$$

# Discussion for (c)

The current is less than the 2.00 A that flowed through $R _ { 2 }$ when it was connected in parallel to the battery in the previous parallel circuit example.

# Strategy and Solution for (d)

The power dissipated by $R _ { 2 }$ is given by

$$
P _ { 2 } = ( I _ { 2 } ) ^ { 2 } R _ { 2 } = ( 1 . 6 1 \mathrm { \ A } ) ^ { 2 } ( 6 . 0 0 \Omega ) = 1 5 . 5 \mathrm { \ W } .
$$

# Discussion for (d)

The power is less than the 24.0 W this resistor dissipated when connected in parallel to the 12.0-V source.

# Practical Implications

One implication of this last example is that resistance in wires reduces the current and power delivered to a resistor. If wire resistance is relatively large, as in a worn (or a very long) extension cord, then this loss can be significant. If a large current is drawn, the $I R$ drop in the wires can also be significant.

For example, when you are rummaging in the refrigerator and the motor comes on, the refrigerator light dims momentarily. Similarly, you can see the passenger compartment light dim when you start the engine of your car (although this may be due to resistance inside the battery itself).

What is happening in these high-current situations is illustrated in Figure 21.7. The device represented by $R _ { 3 }$ has a very low resistance, and so when it is switched on, a large current flows. This increased current causes a larger $I R$ drop in the wires represented by $R _ { 1 }$ , reducing the voltage across the light bulb (which is $R _ { 2 }$ ), which then dims noticeably.

# CHECK YOUR UNDERSTANDING

Can any arbitrary combination of resistors be broken down into series and parallel combinations? See if you can draw a circuit diagram of resistors that cannot be broken down into combinations of series and parallel.

# Solution

No, there are many ways to connect resistors that are not combinations of series and parallel, including loops and unctions. In such cases Kirchhoff’s rules, to be introduced in Kirchhoff’s Rules, will allow you to analyze the circuit.

# Problem-Solving Strategies for Series and Parallel Resistors

1. Draw a clear circuit diagram, labeling all resistors and voltage sources. This step includes a list of the knowns for the problem, since they are labeled in your circuit diagram.   
2. Identify exactly what needs to be determined in the problem (identify the unknowns). A written list is useful.   
3. Determine whether resistors are in series, parallel, or a combination of both series and parallel. Examine the circuit diagram to make this assessment. Resistors are in series if the same current must pass sequentially through them.   
4. Use the appropriate list of major features for series or parallel connections to solve for the unknowns. There is one list for series and another for parallel. If your problem has a combination of series and parallel, reduce it in steps by considering individual groups of series or parallel connections, as done in this module and the examples. Special note: When finding $R _ { \mathrm { p } }$ , the reciprocal must be taken with care.   
5. Check to see whether the answers are reasonable and consistent. Units and numerical results must be reasonable. Total series resistance should be greater, whereas total parallel resistance should be smaller, for example. Power should be greater for the same devices in parallel compared with series, and so on.