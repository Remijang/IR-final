# 21.5 Null Measurements

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

• Explain why a null measurement device is more accurate than a standard voltmeter or ammeter.   
• Demonstrate how a Wheatstone bridge can be used to accurately calculate the resistance in a circuit.

Standard measurements of voltage and current alter the circuit being measured, introducing uncertainties in the measurements. Voltmeters draw some extra current, whereas ammeters reduce current flow. Null measurements balance voltages so that there is no current flowing through the measuring device and, therefore, no alteration of the circuit being measured.

Null measurements are generally more accurate but are also more complex than the use of standard voltmeters and ammeters, and they still have limits to their precision. In this module, we shall consider a few specific types of null measurements, because they are common and interesting, and they further illuminate principles of electric circuits.

# The Potentiometer

Suppose you wish to measure the emf of a battery. Consider what happens if you connect the battery directly to a standard voltmeter as shown in Figure 21.33. (Once we note the problems with this measurement, we will examine a null measurement that improves accuracy.) As discussed before, the actual quantity measured is the terminal voltage $V$ , which is related to the emf of the battery by $V = \mathrm { e m f } - I r$ , where $I$ is the current that flows and $r$ is the internal resistance of the battery.

The emf could be accurately calculated if $r$ were very accurately known, but it is usually not. If the current $I$ could be made zero, then $V =$ , and so emf could be directly measured. However, standard voltmeters need a current to operate; thus, another technique is needed.

A potentiometer is a null measurement device for measuring potentials (voltages). (See Figure 21.34.) A voltage source is connected to a resistor say, a long wire, and passes a constant current through it. There is a steady drop in potential (an $I R$ drop) along the wire, so that a variable potential can be obtained by making contact at varying locations along the wire.

Figure 21.34(b) shows an unknown $\mathrm { e m f _ { x } }$ (represented by script $E _ { \mathrm { x } }$ in the figure) connected in series with a galvanometer. Note that $\mathrm { e m f _ { x } }$ opposes the other voltage source. The location of the contact point (see the arrow on the drawing) is adjusted until the galvanometer reads zero. When the galvanometer reads zero, $\mathrm { e m f _ { x } } = I R _ { \mathrm { x } }$ , where $R _ { \mathrm { X } }$ is the resistance of the section of wire up to the contact point. Since no current flows through the galvanometer, none flows through the unknown emf, and so $\mathrm { e m f _ { x } }$ is directly sensed.

Now, a very precisely known standard is substituted for $\mathrm { e m f _ { x } }$ , and the contact point is adjusted until the galvanometer again reads zero, so that $\mathrm { e m f _ { s } } = I R _ { \mathrm { s } }$ . In both cases, no current passes through the galvanometer, and so the current $I$ through the long wire is the same. Upon taking the ratio $\frac { \mathrm { e m f _ { X } } } { \mathrm { e m f _ { S } } }$ , $I$ cancels, giving

$$
{ \frac { \mathrm { e m f _ { x } } } { \mathrm { e m f _ { s } } } } = { \frac { I R _ { \mathrm { x } } } { I R _ { \mathrm { s } } } } = { \frac { R _ { \mathrm { x } } } { R _ { \mathrm { s } } } } .
$$

Solving for $\mathrm { e m f _ { x } }$ gives

$$
\mathrm { e m f _ { x } } = \mathrm { e m f _ { s } } \frac { R _ { \mathrm { x } } } { R _ { \mathrm { s } } } .
$$

Because a long uniform wire is used for $R$ , the ratio of resistances $R _ { \mathrm { x } } / R _ { \mathrm { s } }$ is the same as the ratio of the lengths of wire that zero the galvanometer for each emf. The three quantities on the right-hand side of the equation are now known or measured, and $\mathrm { e m f _ { x } }$ can be calculated. The uncertainty in this calculation can be considerably smaller than when using a voltmeter directly, but it is not zero. There is always some uncertainty in the ratio of resistances $R _ { \mathrm { x } } / R _ { \mathrm { s } }$ and in the standard $\mathrm { e m f _ { s } }$ . Furthermore, it is not possible to tell when the galvanometer reads exactly zero, which introduces error into both $R _ { \mathrm { x } }$ and $R _ { \mathrm { s } }$ , and may also affect the current $I$ .



# Resistance Measurements and the Wheatstone Bridge

There is a variety of so-called ohmmeters that purport to measure resistance. What the most common ohmmeters actually do is to apply a voltage to a resistance, measure the current, and calculate the resistance using Ohm’s law. Their readout is this calculated resistance. Two configurations for ohmmeters using standard voltmeters and ammeters are shown in Figure 21.35. Such configurations are limited in accuracy, because the meters alter both the voltage applied to the resistor and the current that flows through it.

The Wheatstone bridge is a null measurement device for calculating resistance by balancing potential drops in a circuit. (See Figure 21.36.) The device is called a bridge because the galvanometer forms a bridge between two branches. A variety of bridge devices are used to make null measurements in circuits.

Resistors $R _ { 1 }$ and $R _ { 2 }$ are precisely known, while the arrow through $R _ { 3 }$ indicates that it is a variable resistance. The value of $R _ { 3 }$ can be precisely read. With the unknown resistance $R _ { \mathrm { X } }$ in the circuit, $R _ { 3 }$ is adjusted until the galvanometer reads zero. The potential difference between points b and ${ \mathsf d }$ is then zero, meaning that b and d are at the same potential. With no current running through the galvanometer, it has no effect on the rest of the circuit. So the branches abc and adc are in parallel, and each branch has the full voltage of the source. That is, the $I R$ drops along abc and adc are the same. Since b and d are at the same potential, the $I R$ drop along ad must equal the $I R$ drop along ab. Thus,

$$
I _ { 1 } R _ { 1 } = I _ { 2 } R _ { 3 } .
$$

Again, since b and d are at the same potential, the $I R$ drop along dc must equal the $I R$ drop along bc. Thus,

$$
I _ { 1 } R _ { 2 } = I _ { 2 } R _ { \mathrm { x } } .
$$

Taking the ratio of these last two expressions gives

$$
\frac { I _ { 1 } R _ { 1 } } { I _ { 1 } R _ { 2 } } = \frac { I _ { 2 } R _ { 3 } } { I _ { 2 } R _ { \mathrm { x } } } .
$$

Canceling the currents and solving for $\mathsf { R } _ { \mathsf { x } }$ yields

$$
R _ { \mathrm { x } } = R _ { 3 } { \frac { R _ { 2 } } { R _ { 1 } } } .
$$

This equation is used to calculate the unknown resistance when current through the galvanometer is zero. This method can be very accurate (often to four significant digits), but it is limited by two factors. First, it is not possible to get the current through the galvanometer to be exactly zero. Second, there are always uncertainties in $R _ { 1 } , R _ { 2 }$ , and $R _ { 3 }$ , which contribute to the uncertainty in $R _ { \mathrm { x } }$ .

# CHECK YOUR UNDERSTANDING

Identify other factors that might limit the accuracy of null measurements. Would the use of a digital device that is more sensitive than a galvanometer improve the accuracy of null measurements?

# Solution

One factor would be resistance in the wires and connections in a null measurement. These are impossible to make zero, and they can change over time. Another factor would be temperature variations in resistance, which can be reduced but not completely eliminated by choice of material. Digital devices sensitive to smaller currents than analog devices do improve the accuracy of null measurements because they allow you to get the current closer to zero.