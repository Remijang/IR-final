# 20.4 Electric Power and Energy

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

• Calculate the power dissipated by a resistor and power supplied by a power supply.   
• Calculate the cost of electricity under various circumstances.

# Power in Electric Circuits

Power is associated by many people with electricity. Knowing that power is the rate of energy use or energy conversion, what is the expression for electric power? Power transmission lines might come to mind. We also think of lightbulbs in terms of their power ratings in watts. Let us compare a 25-W bulb with a 60-W bulb. (See Figure 20.13(a).) Since both operate on the same voltage, the 60-W bulb must draw more current to have a greater power rating. Thus the 60-W bulb’s resistance must be lower than that of a 25-W bulb. If we increase voltage, we also increase power. For example, when a 25-W bulb that is designed to operate on $\boldsymbol { \mathsf { 1 2 0 } } \boldsymbol { \mathsf { V } }$ is connected to $2 4 0 \vee ,$ it briefly glows very brightly and then burns out. Precisely how are voltage, current, and resistance related to electric power?

Electric energy depends on both the voltage involved and the charge moved. This is expressed most simply as $\mathrm { P E } = q V ,$ where $q$ is the charge moved and $V$ is the voltage (or more precisely, the potential difference the charge moves through). Power is the rate at which energy is moved, and so electric power is



$$
P = { \frac { P E } { t } } = { \frac { q V } { t } } .
$$

Recognizing that current is $I = q / t$ (note that $\Delta t = t$ here), the expression for power becomes

$$
P = I V .
$$

Electric power $( P )$ is simply the product of current times voltage. Power has familiar units of watts. Since the SI unit for potential energy (PE) is the joule, power has units of joules per second, or watts. Thus, $1 \mathrm { A } \cdot \mathrm { V } = 1$ . For example, cars often have one or more auxiliary power outlets with which you can charge a cell phone or other electronic devices. These outlets may be rated at $2 0 \mathsf { A }$ , so that the circuit can deliver a maximum power $P = I V { = } ( 2 0 \mathrm { \ A } ) ( 1 2 \mathrm { V } ) = 2 4 0 \mathrm { \ W } .$ In some applications, electric power may be expressed as volt-amperes or even kilovolt-amperes ( $1 \mathrm { k A } \cdot \mathrm { V } = 1 \mathrm { k W } )$ .

To see the relationship of power to resistance, we combine Ohm’s law with $P = I V .$ Substituting $I = W R$ gives $P = ( V / R ) V = V ^ { 2 } / R$ . Similarly, substituting $V = I R$ gives $P = I ( I R ) { = } I ^ { 2 } R$ . Three expressions for electric power are listed together here for convenience:

$$
\begin{array} { c } { P = I V } \\ { P = \displaystyle \frac { V ^ { 2 } } { R } } \\ { P = I ^ { 2 } R . } \end{array}
$$

Note that the first equation is always valid, whereas the other two can be used only for resistors. In a simple circuit, with one voltage source and a single resistor, the power supplied by the voltage source and that dissipated by the resistor are identical. (In more complicated circuits, $P$ can be the power dissipated by a single device and not the total power in the circuit.)

Different insights can be gained from the three different expressions for electric power. For example, $P = V ^ { 2 } / R$ implies that the lower the resistance connected to a given voltage source, the greater the power delivered. Furthermore, since voltage is squared in $P = V ^ { 2 } / R$ , the effect of applying a higher voltage is perhaps greater than expected. Thus, when the voltage is doubled to a 25-W bulb, its power nearly quadruples to about $1 0 0 \mathsf { W }$ , burning it out. If the bulb’s resistance remained constant, its power would be exactly 100 W, but at the higher temperature its resistance is higher, too.

# EXAMPLE 20.7

# Calculating Power Dissipation and Current: Hot and Cold Power

(a) Consider the examples given in Ohm’s Law: Resistance and Simple Circuits and Resistance and Resistivity. Then find the power dissipated by the car headlight in these examples, both when it is hot and when it is cold. (b) What current does it draw when cold?

# Strategy for (a)

For the hot headlight, we know voltage and current, so we can use $P = I V$ to find the power. For the cold headlight, we know the voltage and resistance, so we can use $P = V ^ { 2 } / R$ to find the power.

# Solution for (a)

Entering the known values of current and voltage for the hot headlight, we obtain

$$
P = I V { = } ( 2 . 5 0 \mathrm { \ A } ) ( 1 2 . 0 \mathrm { \ V } ) { = } 3 0 . 0 \mathrm { \ W } .
$$

The cold resistance was $0 . 3 5 0 \Omega$ , and so the power it uses when first switched on is

$$
P = { \frac { V ^ { 2 } } { R } } = { \frac { ( 1 2 . 0 ~ \mathrm { V } ) ^ { 2 } } { 0 . 3 5 0 ~ \Omega } } = 4 1 1 ~ \mathrm { W } .
$$

# Discussion for (a)

The 30 W dissipated by the hot headlight is typical. But the 411 W when cold is surprisingly higher. The initial power quickly decreases as the bulb’s temperature increases and its resistance increases.

# Strategy and Solution for (b)

The current when the bulb is cold can be found several different ways. We rearrange one of the power equations, , and enter known values, obtaining

$$
I = { \sqrt { \frac { P } { R } } } = { \sqrt { \frac { 4 1 1 \mathrm { ~ W } } { 0 . 3 5 0 \Omega } } } = 3 4 . 3 \mathrm { ~ A } .
$$

# Discussion for (b)

The cold current is remarkably higher than the steady-state value of 2.50 A, but the current will quickly decline to that value as the bulb’s temperature increases. Most fuses and circuit breakers (used to limit the current in a circuit) are designed to tolerate very high currents briefly as a device comes on. In some cases, such as with electric motors, the current remains high for several seconds, necessitating special “slow blow” fuses.

# The Cost of Electricity

The more electric appliances you use and the longer they are left on, the higher your electric bill. This familiar fact is based on the relationship between energy and power. You pay for the energy used. Since $P = E / t$ , we see that

$$
E = P t
$$

is the energy used by a device using power $P$ for a time interval $t$ . For example, the more lightbulbs burning, the greater $P$ used; the longer they are on, the greater $t$ is. The energy unit on electric bills is the kilowatt-hour $( \mathrm { k W \cdot h } )$ , consistent with the relationship $E = P t$ . It is easy to estimate the cost of operating electric appliances if you have some idea of their power consumption rate in watts or kilowatts, the time they are on in hours, and the cost per kilowatt-hour for your electric utility. Kilowatt-hours, like all other specialized energy units such as food calories, can be converted to joules. You can prove to yourself that $1 \ \mathrm { k W } \cdot \mathrm { h } = 3 . 6 { x } 1 0 ^ { 6 } \ \mathrm { J }$ .

The electrical energy $( E )$ used can be reduced either by reducing the time of use or by reducing the power consumption of that appliance or fixture. This will not only reduce the cost, but it will also result in a reduced impact on the environment. Improvements to lighting are some of the fastest ways to reduce the electrical energy used in a home or business. About $20 \%$ of a home’s use of energy goes to lighting, while the number for commercial establishments is closer to $40 \%$ . Fluorescent lights are about four times more efficient than incandescent lights—this is true for both the long tubes and the compact fluorescent lights (CFL). (See Figure 20.13(b).) Thus, a 60-W incandescent bulb can be replaced by a 15-W CFL, which has the same brightness and color. CFLs have a bent tube inside a globe or a spiral-shaped tube, all connected to a standard screw-in base that fits standard incandescent light sockets. (Original problems with color, flicker, shape, and high initial investment for CFLs have been addressed in recent years.) The heat transfer from these CFLs is less, and they last up to 10 times longer. The significance of an investment in such bulbs is addressed in the next example. New white LED lights (which are clusters of small LED bulbs) are even more efficient (twice that of CFLs) and last 5 times longer than CFLs. However, their cost is still high.

# Making Connections: Energy, Power, and Time

The relationship $E = P t$ is one that you will find useful in many different contexts. The energy your body uses in exercise is related to the power level and duration of your activity, for example. The amount of heating by a power source is related to the power level and time it is applied. Even the radiation dose of an X-ray image is related to the power and time of exposure.

# EXAMPLE 20.8

# Calculating the Cost Effectiveness of Compact Fluorescent Lights (CFL)

If the cost of electricity in your area is 12 cents per kWh, what is the total cost (capital plus operation) of using a 60-W incandescent bulb for 1000 hours (the lifetime of that bulb) if the bulb cost 25 cents? (b) If we replace this bulb with a compact fluorescent light that provides the same light output, but at one-quarter the wattage, and which costs $\$ 1.50$ but lasts 10 times longer (10,000 hours), what will that total cost be?

# Strategy

To find the operating cost, we first find the energy used in kilowatt-hours and then multiply by the cost per kilowatthour.

# Solution for (a)

The energy used in kilowatt-hours is found by entering the power and time into the expression for energy:

$$
E = P t = ( 6 0 \mathrm { ~ W } ) ( 1 0 0 0 \mathrm { ~ h } ) = 6 0 { , } 0 0 0 \mathrm { ~ W } \cdot \mathrm { h } .
$$

In kilowatt-hours, this is

$$
E = 6 0 . 0 \mathrm { k W \cdot h . }
$$

Now the electricity cost is

$$
\mathrm { c o s t } = ( 6 0 . 0 \mathrm { k W } \cdot \mathrm { h } ) ( \ S 0 . 1 2 / \mathrm { k W } \cdot \mathrm { h } ) = \ S 7 . 2 0 .
$$

The total cost, including the cost of the bulb, will be $\$ 7.45$ for 1000 hours (about one-half year at 5 hours per day).

# Solution for (b)

Since the CFL uses only 15 W and not $6 0 \mathsf { W }$ , the electricity cost will be $\$ 7.20/4=\$ 1.80$ . The CFL will last 10 times longer than the incandescent, so that the investment cost will be $ { 1 / 1 0 }$ of the bulb cost for that time period of use, or $0 . 1 ( \$ 1 . 50 ) = \$ 0. 15$ . Therefore, the total cost will be $\$ 1.95$ for 1000 hours.

# Discussion

Therefore, it is much cheaper to use the CFLs, even though the initial investment is higher. The increased cost of labor that a business must include for replacing the incandescent bulbs more often has not been figured in here.

# Making Connections: Take-Home Experiment—Electrical Energy Use Inventory

1) Make a list of the power ratings on a range of appliances in your home or room. Explain why something like a toaster has a higher rating than a digital clock. Estimate the energy consumed by these appliances in an average day (by estimating their time of use). Some appliances might only state the operating current. If the household voltage is $\boldsymbol { \mathsf { 1 2 0 V } }$ , then use $P = I V . 2$ ) Check out the total wattage used in the rest rooms of your school’s floor or building. (You might need to assume the long fluorescent lights in use are rated at 32 W.) Suppose that the building was closed all weekend and that these lights were left on from 6 p.m. Friday until 8 a.m. Monday. What would this oversight cost? How about for an entire year of weekends?