# 21.6 DC Circuits Containing Resistors and Capacitors

• Explain the importance of the time constant, τ , and calculate the time constant for a given resistance and capacitance.   
• Explain why batteries in a flashlight gradually lose power and the light dims over time.   
• Describe what happens to a graph of the voltage across a capacitor over time as it charges.   
• Explain how a timing circuit works and list some applications.   
• Calculate the necessary speed of a strobe flash needed to “stop” the movement of an object over a particular length.

When you use a flash camera, it takes a few seconds to charge the capacitor that powers the flash. The light flash discharges the capacitor in a tiny fraction of a second. Why does charging take longer than discharging? This question and a number of other phenomena that involve charging and discharging capacitors are discussed in this module.

# RCCircuits

An RCcircuit is one containing a resistor $R$ and a capacitor C. The capacitor is an electrical component that stores electric charge.

Figure 21.37 shows a simple RCcircuit that employs a DC (direct current) voltage source. The capacitor is initially uncharged. As soon as the switch is closed, current flows to and from the initially uncharged capacitor. As charge increases on the capacitor plates, there is increasing opposition to the flow of charge by the repulsion of like charges on each plate.

In terms of voltage, this is because voltage across the capacitor is given by $V _ { \mathrm { c } } = Q / C$ , where $Q$ is the amount of charge stored on each plate and $C$ is the capacitance. This voltage opposes the battery, growing from zero to the maximum emf when fully charged. The current thus decreases from its initial value of $\textstyle I _ { 0 } = { \frac { \mathrm { e m f } } { R } }$ to zero as the voltage on the capacitor reaches the same value as the emf. When there is no current, there is no $I R$ drop, and so the voltage on the capacitor must then equal the emf of the voltage source. This can also be explained with Kirchhoff’s second rule (the loop rule), discussed in Kirchhoff’s Rules, which says that the algebraic sum of changes in potential around any closed loop must be zero.

The initial current is $\textstyle I _ { 0 } = { \frac { \mathrm { e m f } } { R } }$ , because all of the $I R$ drop is in the resistance. Therefore, the smaller the resistance, the faster a given capacitor will be charged. Note that the internal resistance of the voltage source is included in $R$ , as are the resistances of the capacitor and the connecting wires. In the flash camera scenario above, when the batteries powering the camera begin to wear out, their internal resistance rises, reducing the current and lengthening the time it takes to get ready for the next flash.

Voltage on the capacitor is initially zero and rises rapidly at first, since the initial current is a maximum. Figure 21.37(b) shows a graph of capacitor voltage versus time $\mathbf { \rho } ( t )$ starting when the switch is closed at $t = 0$ . The voltage approaches emf asymptotically, since the closer it gets to emf the less current flows. The equation for voltage versus time when charging a capacitor $C$ through a resistor $R$ , derived using calculus, is

$$
V = { \mathrm { e m f } } ( 1 - e ^ { - t / R C } ) { \mathrm { ( c h a r g i n g ) } } ,
$$

where $V$ is the voltage across the capacitor, emf is equal to the emf of the DC voltage source, and the exponential e $= 2 . 7 1 8$ … is the base of the natural logarithm. Note that the units of $R C$ are seconds. We define

$$
\begin{array} { r } { \tau = R C , } \end{array}
$$

where $\tau$ (the Greek letter tau) is called the time constant for an $R C$ circuit. As noted before, a small resistance $R$ allows the capacitor to charge faster. This is reasonable, since a larger current flows through a smaller resistance. It is also reasonable that the smaller the capacitor $C$ , the less time needed to charge it. Both factors are contained in $\boldsymbol { \tau } = \boldsymbol { R } \boldsymbol { C }$ .

More quantitatively, consider what happens when $t = \tau = R C$ . Then the voltage on the capacitor is

$$
V = \operatorname { e m f } \left( 1 - e ^ { - 1 } \right) = \operatorname { e m f } ( 1 - 0 . 3 6 8 ) = 0 . 6 3 2 \cdot { \mathrm { e m f } } .
$$

This means that in the time $\tau = R C$ , the voltage rises to 0.632 of its final value. The voltage will rise 0.632 of the remainder in the next time $\tau$ . It is a characteristic of the exponential function that the final value is never reached, but 0.632 of the remainder to that value is achieved in every time, $\tau$ . In just a few multiples of the time constant $\tau$ , then, the final value is very nearly achieved, as the graph in Figure 21.37(b) illustrates.

# Discharging a Capacitor

Discharging a capacitor through a resistor proceeds in a similar fashion, as Figure 21.38 illustrates. Initially, the current is $\begin{array} { r } { I _ { 0 } = \frac { V _ { 0 } } { R } } \end{array}$ , driven by the initial voltage $V _ { 0 }$ on the capacitor. As the voltage decreases, the current and

hence the rate of discharge decreases, implying another exponential formula for $V$ . Using calculus, the voltage $V$ on a capacitor $C$ being discharged through a resistor $R$ is found to be

$$
V = V _ { 0 } ~ e ^ { - t / R C } \mathrm { ( d i s c h a r g i n g ) } .
$$

The graph in Figure 21.38(b) is an example of this exponential decay. Again, the time constant is $\tau = R C$ . A small resistance $R$ allows the capacitor to discharge in a small time, since the current is larger. Similarly, a small capacitance requires less time to discharge, since less charge is stored. In the first time interval $\tau = R C$ after the switch is closed, the voltage falls to 0.368 of its initial value, since $V = V _ { 0 } \cdot e ^ { - 1 } = 0 . 3 6 8 V _ { 0 }$ .

During each successive time $\tau$ , the voltage falls to 0.368 of its preceding value. In a few multiples of $\tau$ , the voltage becomes very close to zero, as indicated by the graph in Figure 21.38(b).

Now we can explain why the flash camera in our scenario takes so much longer to charge than discharge; the resistance while charging is significantly greater than while discharging. The internal resistance of the battery accounts for most of the resistance while charging. As the battery ages, the increasing internal resistance makes the charging process even slower. (You may have noticed this.)

The flash discharge is through a low-resistance ionized gas in the flash tube and proceeds very rapidly. Flash photographs, such as in Figure 21.39, can capture a brief instant of a rapid motion because the flash can be less than a microsecond in duration. Such flashes can be made extremely intense.

During World War II, nighttime reconnaissance photographs were made from the air with a single flash illuminating more than a square kilometer of enemy territory. The brevity of the flash eliminated blurring due to the surveillance aircraft’s motion. Today, an important use of intense flash lamps is to pump energy into a laser. The short intense flash can rapidly energize a laser and allow it to reemit the energy in another form.

# EXAMPLE 21.6

# Integrated Concept Problem: Calculating Capacitor Size—Strobe Lights

High-speed flash photography was pioneered by Doc Edgerton in the 1930s, while he was a professor of electrical engineering at MIT. You might have seen examples of his work in the amazing shots of hummingbirds in motion, a drop of milk splattering on a table, or a bullet penetrating an apple (see Figure 21.39). To stop the motion and capture these pictures, one needs a high-intensity, very short pulsed flash, as mentioned earlier in this module.

Suppose one wished to capture the picture of a bullet (moving at $5 . 0 \times 1 0 ^ { 2 } ~ \mathrm { m / s } ,$ that was passing through an apple. The duration of the flash is related to the $R C$ time constant, $\tau$ . What size capacitor would one need in the $R C$ circuit to succeed, if the resistance of the flash tube was $1 0 . 0 \Omega ?$ Assume the apple is a sphere with a diameter of $8 . 0 \times 1 0 ^ { - 2 } \mathrm { ~ m ~ }$

# Strategy

We begin by identifying the physical principles involved. This example deals with the strobe light, as discussed above. Figure 21.38 shows the circuit for this probe. The characteristic time $\tau$ of the strobe is given as $\tau = R C$

# Solution

We wish to find $C$ , but we don’t know $\tau$ . We want the flash to be on only while the bullet traverses the apple. So we need to use the kinematic equations that describe the relationship between distance $x$ , velocity $v$ , and time $t$ :

$$
x = v t \ { \mathrm { o r } } t = { \frac { x } { v } } .
$$

The bullet’s velocity is given as $5 . 0 \times 1 0 ^ { 2 } ~ \mathrm { m / s }$ , and the distance $x$ is $8 . 0 \times 1 0 ^ { - 2 } \mathrm { ~ m ~ }$ The traverse time, then, is

$$
t = { \frac { x } { v } } = { \frac { 8 . 0 \times 1 0 ^ { - 2 } \ { \mathrm { m } } } { 5 . 0 \times 1 0 ^ { 2 } \ { \mathrm { m / s } } } } = 1 . 6 \times 1 0 ^ { - 4 } \ { \mathrm { s } } .
$$

We set this value for the crossing time $t$ equal to $\tau$ . Therefore,

$$
C = \frac { t } { R } = \frac { 1 . 6 { \times 1 0 ^ { - 4 } } { \mathrm { ~ s } } } { 1 0 . 0 \Omega } = 1 6 { \mu \mathrm { F } } .
$$

(Note: Capacitance $C$ is typically measured in farads, $F$ , defined as Coulombs per volt. From the equation, we see that $C$ can also be stated in units of seconds per ohm.)

# Discussion

The flash interval of $1 6 0 ~ \mu \mathrm { s }$ (the traverse time of the bullet) is relatively easy to obtain today. Strobe lights have opened up new worlds from science to entertainment. The information from the picture of the apple and bullet was used in the Warren Commission Report on the assassination of President John F. Kennedy in 1963 to confirm that only one bullet was fired.

# RCCircuits for Timing

$R C$ circuits are commonly used for timing purposes. A mundane example of this is found in the ubiquitous intermittent wiper systems of modern cars. The time between wipes is varied by adjusting the resistance in an circuit. Another example of an $R C$ circuit is found in novelty jewelry, Halloween costumes, and various toys that have battery-powered flashing lights. (See Figure 21.40 for a timing circuit.)

A more crucial use of $R C$ circuits for timing purposes is in the artificial pacemaker, used to control heart rate. The heart rate is normally controlled by electrical signals generated by the sino-atrial (SA) node, which is on the wall of the right atrium chamber. This causes the muscles to contract and pump blood. Sometimes the heart rhythm is abnormal and the heartbeat is too high or too low.

The artificial pacemaker is inserted near the heart to provide electrical signals to the heart when needed with the appropriate time constant. Pacemakers have sensors that detect body motion and breathing to increase the heart rate during exercise to meet the body’s increased needs for blood and oxygen.



# EXAMPLE 21.7

# Calculating Time: RCCircuit in a Heart Defibrillator

A heart defibrillator is used to resuscitate an accident victim by discharging a capacitor through the trunk of her body. A simplified version of the circuit is seen in Figure 21.38. (a) What is the time constant if an $8 . 0 0 \mathrm { - } \mu \mathrm { F }$ capacitor is used and the path resistance through her body is $1 . 0 0 \times 1 0 ^ { 3 } ~ \Omega ?$ (b) If the initial voltage is $1 0 . 0 \mathsf { k V }$ , how long does it take to decline to $5 . 0 0 \times 1 0 ^ { 2 }$ ?

# Strategy

Since the resistance and capacitance are given, it is straightforward to multiply them to give the time constant asked for in part (a). To find the time for the voltage to decline to $5 . 0 0 \times 1 0 ^ { 2 } \mathrm { ~ V ~ }$ , we repeatedly multiply the initial voltage by 0.368 until a voltage less than or equal to $5 . 0 0 \times 1 0 ^ { 2 }$ is obtained. Each multiplication corresponds to a time of $\tau$ seconds.

# Solution for (a)

The time constant $\tau$ is given by the equation $\tau = R C$ . Entering the given values for resistance and capacitance (and remembering that units for a farad can be expressed as $\mathrm { s } / \Omega$ ) gives

$$
\tau = R C = ( 1 . 0 0 \times 1 0 ^ { 3 } \Omega ) ( 8 . 0 0 \mu F ) = 8 . 0 0 \mathrm { m s } .
$$

# Solution for (b)

In the first $8 . 0 0 \mathrm { m s }$ , the voltage $( 1 0 . 0 \mathsf { k V } )$ declines to 0.368 of its initial value. That is:

$$
V = 0 . 3 6 8 V _ { 0 } = 3 . 6 8 0 \times 1 0 ^ { 3 } \mathrm { ~ V ~ a t } t = 8 . 0 0 \mathrm { m s } .
$$

(Notice that we carry an extra digit for each intermediate calculation.) After another $8 . 0 0 \mathrm { m s }$ , we multiply by 0.368 again, and the voltage is

$$
{ \begin{array} { l l l } { V ^ { \prime } } & { = } & { 0 . 3 6 8 V } \\ & { = } & { ( 0 . 3 6 8 ) { \bigl ( } 3 . 6 8 0 \times 1 0 ^ { 3 } \ \mathrm { V } { \bigr ) } } \\ & { = } & { 1 . 3 5 4 \times 1 0 ^ { 3 } \ \mathrm { V } \ { \mathrm { a t } } \ t = 1 6 . 0 \ { \mathrm { m s } } . } \end{array} }
$$

Similarly, after another $8 . 0 0 \mathrm { m s }$ , the voltage is

$$
{ \begin{array} { r c l } { V ^ { \prime \prime } } & { = } & { 0 . 3 6 8 V \ ^ { \prime } = ( 0 . 3 6 8 ) ( 1 . 3 5 4 \times 1 0 ^ { 3 } \ \mathrm { V } ) } \\ & { = } & { 4 9 8 \ \mathrm { V } \ \mathrm { a t } \ t = 2 4 . 0 \ \mathrm { m s } . } \end{array} }
$$

# Discussion

So after only $2 4 . 0 \mathsf { m s }$ , the voltage is down to $4 9 8 { \sf V } ,$ , or $4 . 9 8 \%$ of its original value.Such brief times are useful in heart defibrillation, because the brief but intense current causes a brief but effective contraction of the heart. The actual circuit in a heart defibrillator is slightly more complex than the one in Figure 21.38, to compensate for magnetic and AC effects that will be covered in Magnetism.

# CHECK YOUR UNDERSTANDING

When is the potential difference across a capacitor an emf?

# Solution

Only when the current being drawn from or put into the capacitor is zero. Capacitors, like batteries, have internal resistance, so their output voltage is not an emf unless current is zero. This is difficult to measure in practice so we refer to a capacitor’s voltage rather than its emf. But the source of potential difference in a capacitor is fundamental and it is an emf.

# PHET EXPLORATIONS

# Circuit Construction Kit (DC only)

An electronics kit in your computer! Build circuits with resistors, light bulbs, batteries, and switches. Take measurements with the realistic ammeter and voltmeter. View the circuit as a schematic diagram, or switch to a lifelike view.

Click to view content (https://openstax.org/books/college-physics-2e/pages/21-6-dc-circuits-containing-resistorsand-capacitors)

Glossary   
ammeter an instrument that measures current   
analog meter a measuring instrument that gives a readout in the form of a needle movement over a marked gauge   
bridge device a device that forms a bridge between two branches of a circuit; some bridge devices are used to make null measurements in circuits   
capacitance the maximum amount of electric potential energy that can be stored (or separated) for a given electric potential   
capacitor an electrical component used to store energy by separating electric charge on two opposing plates   
conservation laws require that energy and charge be conserved in a system   
current the flow of charge through an electric circuit past a given point of measurement   
current sensitivity the maximum current that a galvanometer can read   
digital meter a measuring instrument that gives a readout in a digital form   
electromotive force (emf) the potential difference of a source of electricity when no current is flowing; measured in volts   
full-scale deflection the maximum deflection of a galvanometer needle, also known as current sensitivity; a galvanometer with a full-scale deflection of $5 0 \mu \mathrm { A }$ has a maximum deflection of its needle when $5 0 \mu \mathrm { A }$ flows through it   
galvanometer an analog measuring device, denoted by G, that measures current flow using a needle deflection caused by a magnetic field force acting upon a current-carrying wire   
internal resistance the amount of resistance within the voltage source   
Joule’s law the relationship between potential electrical power, voltage, and resistance in an electrical circuit, given by: $P _ { e } = I V$   
junction rule Kirchhoff’s first rule, which applies the conservation of charge to a junction; current is the flow of charge; thus, whatever charge flows into the junction must flow out; the rule can be stated $I _ { 1 } = I _ { 2 } + I _ { 3 }$   
Kirchhoff’s rules a set of two rules, based on conservation of charge and energy, governing current and changes in potential in an electric circuit   
loop rule Kirchhoff’s second rule, which states that in a closed loop, whatever energy is supplied by emf must be transferred into other forms by devices in the loop, since there are no other ways in which energy can be transferred into or out of the circuit. Thus, the emf equals the sum of the $I R$ (voltage) drops in the loop and can be stated: $\mathrm { e m f } = I r + I R _ { 1 } + I R _ { 2 } $   
null measurements methods of measuring current and voltage more accurately by balancing the circuit so that no current flows through the measurement device   
Ohm’s law the relationship between current, voltage, and resistance within an electrical circuit: $V = I R$   
ohmmeter an instrument that applies a voltage to a resistance, measures the current, calculates the resistance using Ohm’s law, and provides a readout of this calculated resistance   
parallel the wiring of resistors or other components in an electrical circuit such that each component receives an equal voltage from the power source; often pictured in a ladder-shaped diagram, with each component on a rung of the ladder   
potential difference the difference in electric potential between two points in an electric circuit, measured in volts   
potentiometer a null measurement device for measuring potentials (voltages)   
RC circuit a circuit that contains both a resistor and a capacitor   
resistance causing a loss of electrical power in a circuit   
resistor a component that provides resistance to the current flowing through an electrical circuit   
series a sequence of resistors or other components wired into a circuit one after the other   
shunt resistance a small resistance $R$ placed in parallel with a galvanometer G to produce an ammeter; the larger the current to be measured, the smaller $R$ must be; most of the current flowing through the meter is shunted through $R$ to protect the galvanometer   
terminal voltage the voltage measured across the terminals of a source of potential difference   
voltage the electrical potential energy per unit charge; electric pressure created by a power source, such as a battery   
voltage drop the loss of electrical power as a current travels through a resistor, wire or other component   
voltmeter an instrument that measures voltage   
Wheatstone bridge a null measurement device for calculating resistance by balancing potential drops in a circuit



# Section Summary

# 21.1 Resistors in Series and Parallel

• The total resistance of an electrical circuit with resistors wired in a series is the sum of the individual resistances: $R _ { \mathrm { s } } = R _ { 1 } + R _ { 2 } + R _ { 3 } + \ldots$   
• Each resistor in a series circuit has the same amount of current flowing through it.   
• The voltage drop, or power dissipation, across each individual resistor in a series is different, and their combined total adds up to the power source input. The total resistance of an electrical circuit with resistors wired in parallel is less than the lowest resistance of any of the components and can be determined using the formula: ${ \frac { 1 } { R _ { \mathrm { p } } } } = { \frac { 1 } { R _ { 1 } } } + { \frac { \stackrel { \smile } { 1 } } { R _ { 2 } } } + { \frac { 1 } { R _ { 3 } } } + \ldots$   
• Each resistor in a parallel circuit has the same full voltage of the source applied to it.   
• The current flowing through each resistor in a parallel circuit is different, depending on the resistance.   
• If a more complex connection of resistors is a combination of series and parallel, it can be reduced to a single equivalent resistance by identifying its various parts as series or parallel, reducing each to its equivalent, and continuing until a single resistance is eventually reached.

# 21.2 Electromotive Force: Terminal Voltage

• All voltage sources have two fundamental parts—a source of electrical energy that has a characteristic electromotive force (emf), and an internal resistance $r$ . The emf is the potential difference of a source when no current is flowing.   
• The numerical value of the emf depends on the source of potential difference.   
• The internal resistance $r$ of a voltage source affects the output voltage when a current flows.   
• The voltage output of a device is called its terminal voltage $V$ and is given by $V = \mathrm { e m f } - I r$ , where $I$ is the electric current and is positive when flowing away from the positive terminal of the voltage source.   
• When multiple voltage sources are in series, their internal resistances add and their emfs add algebraically.   
• Solar cells can be wired in series or parallel to provide increased voltage or current, respectively.

# 21.3 Kirchhoff’s Rules

• Kirchhoff’s rules can be used to analyze any circuit, simple or complex.   
• Kirchhoff’s first rule—the junction rule: The sum of all currents entering a junction must equal the sum of all currents leaving the junction.   
• Kirchhoff’s second rule—the loop rule: The algebraic sum of changes in potential around any closed circuit path (loop) must be zero.   
• The two rules are based, respectively, on the laws of conservation of charge and energy.   
• When calculating potential and current using Kirchhoff’s rules, a set of conventions must be followed for determining the correct signs of various terms.   
• The simpler series and parallel rules are special cases of Kirchhoff’s rules.

# 21.4 DC Voltmeters and Ammeters

• Voltmeters measure voltage, and ammeters measure current.   
• A voltmeter is placed in parallel with the voltage source to receive full voltage and must have a large resistance to limit its effect on the circuit.   
• An ammeter is placed in series to get the full current flowing through a branch and must have a small resistance to limit its effect on the circuit.   
• Both can be based on the combination of a resistor and a galvanometer, a device that gives an analog reading of current.   
Standard voltmeters and ammeters alter the circuit being measured and are thus limited in accuracy.

# 21.5 Null Measurements

• Null measurement techniques achieve greater accuracy by balancing a circuit so that no current flows through the measuring device.   
• One such device, for determining voltage, is a potentiometer.   
• Another null measurement device, for determining resistance, is the Wheatstone bridge.   
• Other physical quantities can also be measured with null measurement techniques.

# 21.6 DC Circuits Containing Resistors and Capacitors

• An $R C$ circuit is one that has both a resistor and a capacitor. • The time constant $\tau$ for an $R C$ circuit is $\tau = R C$ . • When an initially uncharged ( $\mathrm { \Delta } V _ { 0 } = 0$ at $t = 0$ )

capacitor in series with a resistor is charged by a DC voltage source, the voltage rises, asymptotically approaching the emf of the voltage source; as a function of time, $V = \operatorname { e m f } ( 1 - e ^ { - t / R C } )$ (charging). • Within the span of each time constant $\tau$ , the voltage rises by 0.632 of the remaining value, approaching the final voltage asymptotically.

# Conceptual Questions

# 21.1 Resistors in Series and Parallel

1. A switch has a variable resistance that is nearly zero when closed and extremely large when open, and it is placed in series with the device it controls. Explain the effect the switch in Figure 21.41 has on current when open and when closed.

2. What is the voltage across the open switch in Figure 21.41?

3. There is a voltage across an open switch, such as in Figure 21.41. Why, then, is the power dissipated by the open switch small?

4. Why is the power dissipated by a closed switch, such as in Figure 21.41, small?

• If a capacitor with an initial voltage $V _ { 0 }$ is discharged through a resistor starting at $t = 0$ , then its voltage decreases exponentially as given by $V = V _ { 0 } e ^ { - t / R C }$ (discharging).   
• In each time constant $\tau$ , the voltage falls by 0.368 of its remaining initial value, approaching zero asymptotically.

5. A student in a physics lab mistakenly wired a light bulb, battery, and switch as shown in Figure 21.42. Explain why the bulb is on when the switch is open, and off when the switch is closed. (Do not try this—it is hard on the battery!)

6. Knowing that the severity of a shock depends on the magnitude of the current through your body, would you prefer to be in series or parallel with a resistance, such as the heating element of a toaster, if shocked by it? Explain.   
7. Would your headlights dim when you start your car’s engine if the wires in your automobile were superconductors? (Do not neglect the battery’s internal resistance.) Explain.   
8. Some strings of holiday lights are wired in series to save wiring costs. An old version utilized bulbs that break the electrical connection, like an open switch, when they burn out. If one such bulb burns out, what happens to the others? If such a string operates on $\boldsymbol { \mathsf { 1 2 0 } } \boldsymbol { \mathsf { V } }$ and has 40 identical bulbs, what is the normal operating voltage of each? Newer versions use bulbs that short circuit, like a closed switch, when they burn out. If one such bulb burns out, what happens to the others? If such a string operates on $\boldsymbol { \mathsf { 1 2 0 } } \boldsymbol { \mathsf { V } }$ and has 39 remaining identical bulbs, what is then the operating voltage of each?   
9. If two household lightbulbs rated 60 W and 100 W are connected in series to household power, which

will be brighter? Explain.

10. Suppose you are doing a physics lab that asks you to put a resistor into a circuit, but all the resistors supplied have a larger resistance than the requested value. How would you connect the available resistances to attempt to get the smaller value asked for?   
11. Before World War II, some radios got power through a “resistance cord” that had a significant resistance. Such a resistance cord reduces the voltage to a desired level for the radio’s tubes and the like, and it saves the expense of a transformer. Explain why resistance cords become warm and waste energy when the radio is on.   
12. Some light bulbs have three power settings (not including zero), obtained from multiple filaments that are individually switched and wired in parallel. What is the minimum number of filaments needed for three power settings?

# 21.2 Electromotive Force: Terminal Voltage

13. Is every emf a potential difference? Is every potential difference an emf? Explain.   
14. Explain which battery is doing the charging and which is being charged in Figure 21.43.   
15. Given a battery, an assortment of resistors, and a variety of voltage and current measuring devices, describe how you would determine the internal resistance of the battery.   
16. Two different $1 2 - \mathsf { V }$ automobile batteries on a store shelf are rated at 600 and 850 “cold cranking amps.” Which has the smallest internal resistance?   
17. What are the advantages and disadvantages of connecting batteries in series? In parallel?   
18. Semitractor trucks use four large 12-V batteries. The starter system requires $2 4 \vee$ , while normal operation of the truck’s other electrical components utilizes $\displaystyle { 1 2 \vee }$ . How could the four batteries be connected to produce 24 V? To produce 12 V? Why is $2 4 \vee$ better than $\boldsymbol { \mathsf { 1 2 V } }$ for starting the truck’s engine (a very heavy load)?



# 21.3 Kirchhoff’s Rules

19. Can all of the currents going into the junction in Figure 21.44 be positive? Explain.

20. Apply the junction rule to junction b in Figure 21.45. Is any new information gained by applying the junction rule at e? (In the figure, each emf is represented by script E.)

21. (a) What is the potential difference going from point a to point b in Figure 21.45? (b) What is the potential difference going from c to b? (c) From e to $\ S ?$ (d) From e to d?   
22. Apply the loop rule to loop afedcba in Figure 21.45.   
23. Apply the loop rule to loops abgefa and cbgedc in Figure 21.45.

# 21.4 DC Voltmeters and Ammeters

24. Why should you not connect an ammeter directly across a voltage source as shown in Figure 21.46? (Note that script E in the figure stands for emf.)

25. Suppose you are using a multimeter (one designed to measure a range of voltages, currents, and resistances) to measure current in a circuit and you inadvertently leave it in a voltmeter mode. What effect will the meter have on the circuit? What would happen if you were measuring voltage but accidentally put the meter in the ammeter mode?

26. Specify the points to which you could connect a voltmeter to measure the following potential differences in Figure 21.47: (a) the potential difference of the voltage source; (b) the potential difference across $R _ { 1 }$ ; (c) across $R _ { 2 }$ ; (d) across $R _ { 3 }$ ; (e) across $R _ { 2 }$ and $R _ { 3 }$ . Note that there may be more than one answer to each part.

27. To measure currents in Figure 21.47, you would replace a wire between two points with an ammeter. Specify the points between which you would place an ammeter to measure the following: (a) the total current; (b) the current flowing through $R _ { 1 }$ ; (c) through $R _ { 2 }$ ; (d) through $R _ { 3 }$ . Note that there may be more than one answer to each part.

# 21.5 Null Measurements

28. Why can a null measurement be more accurate than one using standard voltmeters and ammeters? What factors limit the accuracy of null measurements?   
29. If a potentiometer is used to measure cell emfs on the order of a few volts, why is it most accurate for the standard to be the same order of magnitude and the resistances to be in the range of a few ohms?

# 21.6 DC Circuits Containing Resistors and Capacitors

30. Regarding the units involved in the relationship $\boldsymbol { \tau } = \boldsymbol { R } \boldsymbol { C }$ , verify that the units of resistance times capacitance are time, that is, $\boldsymbol { \Omega } \cdot \boldsymbol { \mathrm { F } } = \boldsymbol { \mathrm { s } }$ .

31. The $R C$ time constant in heart defibrillation is crucial to limiting the time the current flows. If the capacitance in the defibrillation unit is fixed, how would you manipulate resistance in the circuit to adjust the $R C$ constant $\boldsymbol { \tau } ?$ Would an adjustment of the applied voltage also be needed to ensure that the current delivered has an appropriate value?

32. When making an ECG measurement, it is important to measure voltage variations over small time intervals. The time is limited by the $R C$ constant of the circuit—it is not possible to measure time variations shorter than . How would you manipulate $R$ and $C$ in the circuit to allow the necessary measurements?   
33. Draw two graphs of charge versus time on a capacitor. Draw one for charging an initially uncharged capacitor in series with a resistor, as in the circuit in Figure 21.37, starting from $\mathbf { t } = 0$ . Draw the other for discharging a capacitor through a resistor, as in the circuit in Figure 21.38, starting at $\mathbf { t } = 0$ , with an initial charge $Q _ { 0 }$ . Show at least two intervals of $\tau$ .   
34. When charging a capacitor, as discussed in conjunction with Figure 21.37, how long does it take for the voltage on the capacitor to reach emf? Is this a problem?   
35. When discharging a capacitor, as discussed in conjunction with Figure 21.38, how long does it take for the voltage on the capacitor to reach zero? Is this a problem?   
36. Referring to Figure 21.37, draw a graph of potential difference across the resistor versus time, showing at least two intervals of . Also draw a graph of current versus time for this situation.   
37. A long, inexpensive extension cord is connected from inside the house to a refrigerator outside. The refrigerator doesn’t run as it should. What might be the problem?   
38. In Figure 21.40, does the graph indicate the time constant is shorter for discharging than for charging? Would you expect ionized gas to have low resistance? How would you adjust $R$ to get a longer time between flashes? Would adjusting $R$ affect the discharge time?

39. An electronic apparatus may have large capacitors at high voltage in the power supply section, presenting a shock hazard even when the apparatus is switched off. A “bleeder resistor” is therefore placed across such a capacitor, as shown schematically in Figure 21.48, to bleed the charge from it after the apparatus is off. Why must the bleeder resistance be much greater than the effective resistance of the rest of the circuit? How does this affect the time constant for discharging the capacitor?

# Problems & Exercises

# 21.1 Resistors in Series and Parallel

# Note: Data taken from figures can be assumed to be accurate to three significant digits.

1. (a) What is the resistance of ten resistors connected in series? (b) In parallel?   
2. (a) What is the resistance of a $1 . 0 0 \times 1 0 ^ { 2 } \ : - \Omega ,$ , a $2 . 5 0 – \mathbf { k } \Omega$ , and a $4 . 0 0 \mathrm { - k } \Omega$ resistor connected in series? (b) In parallel?   
3. What are the largest and smallest resistances you can obtain by connecting a $3 6 . 0 – \Omega$ , a , and a resistor together?   
4. An 1800-W toaster, a 1400-W electric frying pan, and a 75-W lamp are plugged into the same outlet in a 15-A, 120-V circuit. (The three devices are in parallel when plugged into the same socket.). (a) What current is drawn by each device? (b) Will this combination blow the 15-A fuse?   
5. Your car’s 30.0-W headlight and 2.40-kW starter are ordinarily connected in parallel in a 12.0-V system. What power would one headlight and the starter consume if connected in series to a $\mathsf { 1 2 . 0 – V }$ battery? (Neglect any other resistance in the circuit and any change in resistance in the two devices.)   
6. (a) Given a 48.0-V battery and $2 4 . 0 { \cdot } \Omega$ and $9 6 . 0 \ – \Omega$ resistors, find the current and power for each when connected in series. (b) Repeat when the resistances are in parallel.   
7. Referring to the example combining series and parallel circuits and Figure $2 1 . 6$ , calculate $I _ { 3 }$ in the following two different ways: (a) from the known values of $I$ and $I _ { 2 }$ ; (b) using Ohm’s law for $R _ { 3 }$ . In both parts explicitly show how you follow the steps in the Problem-Solving Strategies for Series and Parallel Resistors.   
8. Referring to Figure 21.6: (a) Calculate $P _ { 3 }$ and note how it compares with $P _ { 3 }$ found in the first two example problems in this module. (b) Find the total power supplied by the source and compare it with the sum of the powers dissipated by the resistors.   
9. Refer to Figure 21.7 and the discussion of lights dimming when a heavy appliance comes on. (a) Given the voltage source is $\textstyle 1 2 0 \vee ,$ , the wire resistance is $0 . 4 0 0 \Omega$ , and the bulb is nominally 75.0 W, what power will the bulb dissipate if a total of 15.0 A passes through the wires when the motor comes on? Assume negligible change in bulb resistance. (b) What power is consumed by the motor?



10. A 240-kV power transmission line carrying $5 . 0 0 \times 1 0 ^ { 2 }$ is hung from grounded metal towers by ceramic insulators, each having a $1 . 0 0 \times 1 0 ^ { 9 } \ - \Omega$ resistance. Figure 21.49. (a) What is the resistance to ground of 100 of these insulators? (b) Calculate the power dissipated by 100 of them. (c) What fraction of the power carried by the line is this? Explicitly show how you follow the steps in the Problem-Solving Strategies for Series and Parallel Resistors.

11. Show that if two resistors $R _ { 1 }$ and $R _ { 2 }$ are combined and one is much greater than the other $( R _ { 1 } > > R _ { 2 } )$ : (a) Their series resistance is very nearly equal to the greater resistance $R _ { 1 }$ . (b) Their parallel resistance is very nearly equal to smaller resistance $R _ { 2 }$ .

12. Unreasonable Results Two resistors, one having a resistance of $1 4 5 \Omega$ , are connected in parallel to produce a total resistance of $1 5 0 \Omega$ . (a) What is the value of the second resistance? (b) What is unreasonable about this result? (c) Which assumptions are unreasonable or inconsistent?

13. Unreasonable Results Two resistors, one having a resistance of $9 0 0 \mathrm { k } \Omega$ , are connected in series to produce a total resistance of $0 . 5 0 0 { \bf M } \Omega$ . (a) What is the value of the second resistance? (b) What is unreasonable about this result? (c) Which assumptions are unreasonable or inconsistent?

# 21.2 Electromotive Force: Terminal Voltage

14. Standard automobile batteries have six lead-acid cells in series, creating a total emf of 12.0 V. What is the emf of an individual lead-acid cell?

15. Carbon-zinc dry cells (sometimes referred to as non-alkaline cells) have an emf of $\mathtt { 1 . 5 4 V } ,$ , and they are produced as single cells or in various combinations to form other voltages. (a) How many 1.54-V cells are needed to make the common 9-V battery used in many small electronic devices? (b) What is the actual emf of the approximately 9-V battery? (c) Discuss how internal resistance in the series connection of cells will affect the terminal voltage of this approximately 9-V battery.

16. What is the output voltage of a 3.0000-V lithium cell in a digital wristwatch that draws $0 . 3 0 0 ~ \mathsf { m A }$ , if the cell’s internal resistance is $2 . 0 0 \Omega ?$

17. (a) What is the terminal voltage of a large 1.54-V carbon-zinc dry cell used in a physics lab to supply 2.00 A to a circuit, if the cell’s internal resistance is $0 . 1 0 0 \Omega ?$ (b) How much electrical power does the cell produce? (c) What power goes to its load?

18. What is the internal resistance of an automobile battery that has an emf of $\boldsymbol { \mathsf { 1 2 . 0 V } }$ and a terminal voltage of $\boldsymbol { \mathsf { 1 5 . 0 \vee } }$ while a current of 8.00 A is charging it?

19. (a) Find the terminal voltage of a $\mathsf { 1 2 . 0 – V }$ motorcycle battery having a $0 . 6 0 0 – \Omega$ internal resistance, if it is being charged by a current of 10.0 A. (b) What is the output voltage of the battery charger?

20. A car battery with a 12-V emf and an internal resistance of $0 . 0 5 0 \Omega$ is being charged with a current of 60 A. Note that in this process the battery is being charged. (a) What is the potential difference across its terminals? (b) At what rate is thermal energy being dissipated in the battery? (c) At what rate is electric energy being converted to chemical energy? (d) What are the answers to (a) and (b) when the battery is used to supply 60 A to the starter motor?

21. The hot resistance of a flashlight bulb is $2 . 3 0 \Omega$ , and it is run by a 1.58-V alkaline cell having a $0 . 1 0 0 – \Omega$ internal resistance. (a) What current flows? (b) Calculate the power supplied to the bulb using $I ^ { 2 } R _ { \mathrm { { b u l b } } }$ . (c) Is this power the same as calculated using ?

22. The label on a portable radio recommends the use of rechargeable nickel-cadmium cells (nicads), although they have a 1.25-V emf while alkaline cells have a 1.58-V emf. The radio has a $3 . 2 0 – \Omega$ resistance. (a) Draw a circuit diagram of the radio and its batteries. Now, calculate the power delivered to the radio. (b) When using Nicad cells each having an internal resistance of $0 . 0 4 0 0 \Omega$ . (c) When using alkaline cells each having an internal resistance of $0 . 2 0 0 \Omega$ . (d) Does this difference seem significant, considering that the radio’s effective resistance is lowered when its volume is turned up?

23. An automobile starter motor has an equivalent resistance of $0 . 0 5 0 0 \Omega$ and is supplied by a $\mathsf { 1 2 . 0 – V }$ battery with a internal resistance. (a) What is the current to the motor? (b) What voltage is applied to it? (c) What power is supplied to the motor? (d) Repeat these calculations for when the battery connections are corroded and add $0 . 0 9 0 0 \Omega$ to the circuit. (Significant problems are caused by even small amounts of unwanted resistance in low-voltage, high-current applications.)

24. A child’s electronic toy is supplied by three 1.58-V alkaline cells having internal resistances of $0 . 0 2 0 0 \Omega$ in series with a 1.53-V carbon-zinc dry cell having a internal resistance. The load resistance is $1 0 . 0 \Omega$ . (a) Draw a circuit diagram of the toy and its batteries. (b) What current flows? (c) How much power is supplied to the load? (d) What is the internal resistance of the dry cell if it goes bad, resulting in only 0.500 W being supplied to the load?

25. (a) What is the internal resistance of a voltage source if its terminal voltage drops by $2 . 0 0 \mathrm { V }$ when the current supplied increases by 5.00 A? (b) Can the emf of the voltage source be found with the information supplied?

26. A person with body resistance between his hands of $1 0 . 0 \mathrm { k } \Omega$ accidentally grasps the terminals of a $2 0 . 0 \substack { - \mathsf { k V } }$ power supply. (Do NOT do this!) (a) Draw a circuit diagram to represent the situation. (b) If the internal resistance of the power supply is $2 0 0 0 \Omega$ , what is the current through his body? (c) What is the power dissipated in his body? (d) If the power supply is to be made safe by increasing its internal resistance, what should the internal resistance be for the maximum current in this situation to be $\mathsf { 1 . 0 0 } \mathsf { m } \mathsf { A }$ or less? (e) Will this modification compromise the effectiveness of the power supply for driving low-resistance devices? Explain your reasoning.

27. Electric fish generate current with biological cells called electroplaques, which are physiological emf devices. The electroplaques in the South American eel are arranged in 140 rows, each row stretching horizontally along the body and each containing 5000 electroplaques. Each electroplaque has an emf of $0 . 1 5 \vee$ and internal resistance of $0 . 2 5 \Omega$ . If the water surrounding the fish has resistance of $8 0 0 \Omega$ , how much current can the eel produce in water from near its head to near its tail?

28. Integrated Concepts A 12.0-V emf automobile battery has a terminal voltage of $\boldsymbol { 1 6 . 0 \vee }$ when being charged by a current of 10.0 A. (a) What is the battery’s internal resistance? (b) What power is dissipated inside the battery? (c) At what rate (in ${ } ^ { \mathrm { { o } } } \mathrm { { C } } / \mathrm { { m i n } } \mathrm { { \dot { \Omega } } }$ ) will its temperature increase if its mass is $2 0 . 0 \mathsf { k g }$ and it has a specific heat of $0 . 3 0 0 \mathrm { k c a l / k g \cdot ^ { \circ } C } ,$ assuming no heat escapes?

29. Unreasonable Results A 1.58-V alkaline cell with a $0 . 2 0 0 – \Omega$ internal resistance is supplying 8.50 A to a load. (a) What is its terminal voltage? (b) What is the value of the load resistance? (c) What is unreasonable about these results? (d) Which assumptions are unreasonable or inconsistent?

30. Unreasonable Results (a) What is the internal resistance of a 1.54-V dry cell that supplies 1.00 W of power to a bulb? (b) What is unreasonable about this result? (c) Which assumptions are unreasonable or inconsistent?

# 21.3 Kirchhoff’s Rules

31. Apply the loop rule to loop abcdefgha in Figure 21.25.   
32. Apply the loop rule to loop aedcba in Figure 21.25.   
33. Verify the second equation in Example 21.5 by substituting the values found for the currents $I _ { 1 }$ and $I _ { 2 }$ .   
34. Verify the third equation in Example 21.5 by substituting the values found for the currents $I _ { 1 }$ and $I _ { 3 }$ .

35. Apply the junction rule at point a in Figure 21.50.

36. Apply the loop rule to loop abcdefghija in Figure 21.50.   
37. Apply the loop rule to loop akledcba in Figure 21.50.   
38. Find the currents flowing in the circuit in Figure 21.50. Explicitly show how you follow the steps in the Problem-Solving Strategies for Series and Parallel Resistors.   
39. Solve Example 21.5, but use loop abcdefgha instead of loop akledcba. Explicitly show how you follow the steps in the Problem-Solving Strategies for Series and Parallel Resistors.   
40. Find the currents flowing in the circuit in Figure 21.45.   
41. Unreasonable Results Consider the circuit in Figure 21.51, and suppose that the emfs are unknown and the currents are given to be $I _ { 1 } = 5 . 0 0 \mathrm { A }$ , $I _ { 2 } = 3 . 0 \mathrm { A }$ , and $I _ { 3 } = - 2 . 0 0$ . (a) Could you find the emfs? (b) What is wrong with the assumptions?

# 21.4 DC Voltmeters and Ammeters

42. What is the sensitivity of the galvanometer (that is, what current gives a full-scale deflection) inside a voltmeter that has a resistance on its 30.0-V scale?   
43. What is the sensitivity of the galvanometer (that is, what current gives a full-scale deflection) inside a voltmeter that has a $2 5 . 0 \mathrm { - k } \Omega$ resistance on its 100-V scale?   
44. Find the resistance that must be placed in series with ${ \sf a 2 5 . 0 { - } \Omega }$ galvanometer having a $5 0 . 0 \mathrm { - \mu A }$ sensitivity (the same as the one discussed in the text) to allow it to be used as a voltmeter with a 0.100-V full-scale reading.   
45. Find the resistance that must be placed in series with $\mathsf { a 2 5 . 0 { - } } \Omega$ galvanometer having a ${ 5 0 . 0 - \mu \mathrm { A } }$ sensitivity (the same as the one discussed in the text) to allow it to be used as a voltmeter with a 3000-V full-scale reading. Include a circuit diagram with your solution.   
46. Find the resistance that must be placed in parallel with a $2 5 . 0 – \Omega$ galvanometer having a $5 0 . 0 { \cdot } \mu \mathrm { A }$ sensitivity (the same as the one discussed in the text) to allow it to be used as an ammeter with a 10.0-A full-scale reading. Include a circuit diagram with your solution.   
47. Find the resistance that must be placed in parallel with a $2 5 . 0 { - } \Omega$ galvanometer having a $5 0 . 0 { \cdot } \mu \mathrm { A }$ sensitivity (the same as the one discussed in the text) to allow it to be used as an ammeter with a $3 0 0 - \mathsf { m A }$ full-scale reading.   
48. Find the resistance that must be placed in series with a $1 0 . 0 { - } \Omega$ galvanometer having a $1 0 0 { \cdot } \mu \mathrm { A }$ sensitivity to allow it to be used as a voltmeter with: (a) a 300-V full-scale reading, and (b) a 0.300-V full-scale reading.   
49. Find the resistance that must be placed in parallel with a $1 0 . 0 { - } \Omega$ galvanometer having a $1 0 0 { \cdot } \mu \mathrm { A }$ sensitivity to allow it to be used as an ammeter with: (a) a 20.0-A full-scale reading, and (b) a $\mathsf { 1 0 0 - m A }$ full-scale reading.

50. Suppose you measure the terminal voltage of a 1.585-V alkaline cell having an internal resistance of $0 . 1 0 0 \Omega$ by placing a $1 . 0 0 \mathrm { - k } \Omega$ voltmeter across its terminals. (See Figure 21.52.) (a) What current flows? (b) Find the terminal voltage. (c) To see how close the measured terminal voltage is to the emf, calculate their ratio.

51. Suppose you measure the terminal voltage of a 3.200-V lithium cell having an internal resistance of $5 . 0 0 \Omega$ by placing a $1 . 0 0 \mathrm { - k } \Omega$ voltmeter across its terminals. (a) What current flows? (b) Find the terminal voltage. (c) To see how close the measured terminal voltage is to the emf, calculate their ratio.

52. A certain ammeter has a resistance of $5 . 0 0 \times 1 0 ^ { - 5 } \Omega$ on its 3.00-A scale and contains a $1 0 . 0 – \Omega$ galvanometer. What is the sensitivity of the galvanometer?

53. A voltmeter is placed in parallel with a $7 5 . 0 \mathrm { - k } \Omega$ resistor in a circuit. (a) Draw a circuit diagram of the connection. (b) What is the resistance of the combination? (c) If the voltage across the combination is kept the same as it was across the $7 5 . 0 \mathrm { - k } \Omega$ resistor alone, what is the percent increase in current? (d) If the current through the combination is kept the same as it was through the $7 5 . 0 \mathrm { - k } \Omega$ resistor alone, what is the percentage decrease in voltage? (e) Are the changes found in parts (c) and (d) significant? Discuss.

54. A ammeter is placed in series with a resistor in a circuit. (a) Draw a circuit diagram of the connection. (b) Calculate the resistance of the combination. (c) If the voltage is kept the same across the combination as it was through the resistor alone, what is the percent decrease in current? (d) If the current is kept the same through the combination as it was through the resistor alone, what is the percent increase in voltage? (e) Are the changes found in parts (c) and (d) significant? Discuss.

55. Unreasonable Results Suppose you have a $4 0 . 0 \ – \Omega$ galvanometer with a $2 5 . 0 { \cdot } \mu \mathrm { A }$ sensitivity. (a) What resistance would you put in series with it to allow it to be used as a voltmeter that has a full-scale deflection for 0.500 mV? (b) What is unreasonable about this result? (c) Which assumptions are responsible?

56. Unreasonable Results (a) What resistance would you put in parallel with a $4 0 . 0 – \Omega$ galvanometer having a $2 5 . 0 { \cdot } \mu \mathrm { A }$ sensitivity to allow it to be used as an ammeter that has a full-scale deflection for $1 0 . 0 { \cdot } \mu \ A \ ?$ (b) What is unreasonable about this result? (c) Which assumptions are responsible?

# 21.5 Null Measurements

57. What is the $\mathrm { e m f _ { x } }$ of a cell being measured in a potentiometer, if the standard cell’s emf is $\boldsymbol { \mathsf { 1 2 . 0 \vee } }$ and the potentiometer balances for $R _ { \mathrm { x } } = 5 . 0 0 0 \Omega$ and $R _ { \mathrm { s } } = 2 . 5 0 0 \Omega ?$   
58. Calculate the $\mathrm { e m f _ { x } }$ of a dry cell for which a potentiometer is balanced when $R _ { \mathrm { x } } = 1 . 2 0 0 \Omega$ , while an alkaline standard cell with an emf of 1.600 V requires $R _ { \mathrm { s } } = 1 . 2 4 7 \Omega$ to balance the potentiometer.   
59. When an unknown resistance $R _ { \mathrm { X } }$ is placed in a Wheatstone bridge, it is possible to balance the bridge by adjusting $R _ { 3 }$ to be $2 5 0 0 \Omega$ . What is $R _ { \mathrm { X } }$ if $\frac { R _ { 2 } } { R _ { 1 } } = 0 . 6 2 5 ?$   
60. To what value must you adjust $R _ { 3 }$ to balance a Wheatstone bridge, if the unknown resistance $R _ { \mathrm { x } }$ is $1 0 0 \Omega , R _ { 1 }$ is $5 0 . 0 \Omega$ , and $R _ { 2 }$ is $1 7 5 \Omega ?$   
61. (a) What is the unknown $\mathrm { e m f _ { x } }$ in a potentiometer that balances when $R _ { \mathrm { x } }$ is $1 0 . 0 \Omega$ , and balances when $R _ { \mathrm { s } }$ is $1 5 . 0 \Omega$ for a standard 3.000-V emf? (b) The same $\mathrm { e m f _ { x } }$ is placed in the same potentiometer, which now balances when $R _ { \mathrm { s } }$ is $1 5 . 0 \Omega$ for a standard emf of 3.100 V. At what resistance $R _ { \mathrm { x } }$ will the potentiometer balance?   
62. Suppose you want to measure resistances in the range from $1 0 . 0 \Omega$ to $1 0 . 0 \mathrm { k } \Omega$ using a Wheatstone bridge that has . Over what range should $R _ { 3 }$ be adjustable?

# 21.6 DC Circuits Containing Resistors and Capacitors

63. The timing device in an automobile’s intermittent wiper system is based on an $R C$ time constant and utilizes a $0 . 5 0 0 \mathrm { - } \mu \mathrm { F }$ capacitor and a variable resistor. Over what range must $R$ be made to vary to achieve time constants from 2.00 to $\boldsymbol { 1 5 . 0 \mathsf { s ? } }$

64. A heart pacemaker fires 72 times a minute, each time a 25.0-nF capacitor is charged (by a battery in series with a resistor) to 0.632 of its full voltage. What is the value of the resistance?

65. The duration of a photographic flash is related to an $R C$ time constant, which is $0 . 1 0 0 ~ \mu \mathrm { s }$ for a certain camera. (a) If the resistance of the flash lamp is $0 . 0 4 0 0 \Omega$ during discharge, what is the size of the capacitor supplying its energy? (b) What is the time constant for charging the capacitor, if the charging resistance is $8 0 0 \mathrm { k } \Omega ?$

66. A 2.00- and a $7 . 5 0 \mathrm { - } \mu \mathrm { F }$ capacitor can be connected in series or parallel, as can a 25.0- and a $1 0 0 \mathrm { - k } \Omega$ resistor. Calculate the four $R C$ time constants possible from connecting the resulting capacitance and resistance in series.

67. After two time constants, what percentage of the final voltage, emf, is on an initially uncharged capacitor $C$ , charged through a resistance $R ?$

68. A resistor, an uncharged $1 . 5 0 \mathrm { - \mu F }$ capacitor, and a 6.16-V emf are connected in series. (a) What is the initial current? (b) What is the $R C$ time constant? (c) What is the current after one time constant? (d) What is the voltage on the capacitor after one time constant?

69. A heart defibrillator being used on a patient has an $R C$ time constant of 10.0 ms due to the resistance of the patient and the capacitance of the defibrillator. (a) If the defibrillator has an $8 . 0 0 \mathrm { - } \mu \mathrm { F }$ capacitance, what is the resistance of the path through the patient? (You may neglect the capacitance of the patient and the resistance of the defibrillator.) (b) If the initial voltage is 12.0 ${ \sf k V } _ { \ }$ , how long does it take to decline to $6 . 0 0 \times 1 0 ^ { 2 }$ ?

70. An ECG monitor must have an $R C$ time constant less than $1 . 0 0 \times 1 0 ^ { 2 } ~ \mu \mathrm { s }$ to be able to measure variations in voltage over small time intervals. (a) If the resistance of the circuit (due mostly to that of the patient’s chest) is $1 . 0 0 \mathrm { k } \Omega$ , what is the maximum capacitance of the circuit? (b) Would it be difficult in practice to limit the capacitance to less than the value found in (a)?

71. Figure 21.53 shows how a bleeder resistor is used to discharge a capacitor after an electronic device is shut off, allowing a person to work on the electronics with less risk of shock. (a) What is the time constant? (b) How long will it take to reduce the voltage on the capacitor to $0 . 2 5 0 \%$ $5 \%$ of $5 \%$ ) of its full value once discharge begins? (c) If the capacitor is charged to a voltage $V _ { 0 }$ through a $1 0 0  – \Omega$ resistance, calculate the time it takes to rise to $0 . 8 6 5 V _ { 0 }$ (This is about two time constants.)

72. Using the exact exponential treatment, find how much time is required to discharge a $2 5 0 \mathrm { - } \mu \mathrm { F }$ capacitor through a $\boldsymbol { \Omega }$ resistor down to $1 . 0 0 \%$ of its original voltage.

73. Using the exact exponential treatment, find how much time is required to charge an initially uncharged 100-pF capacitor through a resistor to $9 0 . 0 \%$ of its final voltage.

74. Integrated Concepts If you wish to take a picture of a bullet traveling at $5 0 0 ~ \mathrm { m / s }$ , then a very brief flash of light produced by an $R C$ discharge through a flash tube can limit blurring. Assuming $\pm . 0 0 \mathsf { m m }$ of motion during one $R C$ constant is acceptable, and given that the flash is driven by a $6 0 0 \mathrm { - } \mu \mathrm { F }$ capacitor, what is the resistance in the flash tube?

75. Integrated Concepts A flashing lamp in a Christmas earring is based on an $R C$ discharge of a capacitor through its resistance. The effective duration of the flash is 0.250 s, during which it produces an average 0.500 W from an average $3 . 0 0 { \mathsf { V } } .$ (a) What energy does it dissipate? (b) How much charge moves through the lamp? (c) Find the capacitance. (d) What is the resistance of the lamp?

76. Integrated Concepts

A $1 6 0 \mathrm { - } \mu \mathrm { F }$ capacitor charged to $4 5 0 \vee$ is discharged through a $3 1 . 2 – \mathrm { k } \Omega$ resistor. (a) Find the time constant. (b) Calculate the temperature increase of the resistor, given that its mass is 2.50 g and its specific heat is , noting that most of the thermal energy is retained in the short time of the discharge. (c) Calculate the new resistance, assuming it is pure carbon. (d) Does this change in resistance seem significant?

77. Unreasonable Results (a) Calculate the capacitance needed to get an $R C$ time constant of $1 . 0 0 \times 1 0 ^ { 3 }$ with a $0 . 1 0 0 – \Omega$ resistor. (b) What is unreasonable about this result? (c) Which assumptions are responsible?

78. Construct Your Own Problem Consider a camera’s flash unit. Construct a problem in which you calculate the size of the capacitor that stores energy for the flash lamp. Among the things to be considered are the voltage applied to the capacitor, the energy needed in the flash and the associated charge needed on the capacitor, the resistance of the flash lamp during discharge, and the desired $R C$ time constant.

79. Construct Your Own Problem

Consider a rechargeable lithium cell that is to be used to power a camcorder. Construct a problem in which you calculate the internal resistance of the cell during normal operation. Also, calculate the minimum voltage output of a battery charger to be used to recharge your lithium cell. Among the things to be considered are the emf and useful terminal voltage of a lithium cell and the current it should be able to supply to a camcorder.

80. Critical Thinking A circuit has a voltage source producing $1 . 0 0 \times 1 0 ^ { 2 } \mathrm { V }$ and a $2 . 5 0 \times 1 0 ^ { 3 } \Omega$ resistor. (a) If the circuit contains nothing else, how much power is dissipated by the resistor? (b) A second $2 . 5 0 \times 1 0 ^ { 3 } \Omega$ resistor is added in parallel to the first resistor. Now how much power is dissipated by the resistors? (c) Now place the two resistors in series. How much power is dissipated by the resistors? (d) Why would a parallel arrangement of resistors dissipate more power than a series arrangement of resistors of the same value? (e) Which delivers more energy in a given time period, the parallel combination of resistors, the series combination of resistors, or is the energy delivered in a given time period the same?