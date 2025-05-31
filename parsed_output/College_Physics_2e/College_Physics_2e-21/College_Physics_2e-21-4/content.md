# 21.4 DC Voltmeters and Ammeters

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

• Explain why a voltmeter must be connected in parallel with the circuit.   
• Draw a diagram showing an ammeter correctly connected in a circuit.   
• Describe how a galvanometer can be used as either a voltmeter or an ammeter.   
• Find the resistance that must be placed in series with a galvanometer to allow it to be used as a voltmeter with a given reading.   
• Explain why measuring the voltage or current in a circuit can never be exact.

Voltmeters measure voltage, whereas ammeters measure current. Some of the meters in automobile dashboards, digital cameras, cell phones, and tuner-amplifiers are voltmeters or ammeters. (See Figure 21.26.) The internal construction of the simplest of these meters and how they are connected to the system they monitor give further insight into applications of series and parallel connections.

Voltmeters are connected in parallel with whatever device’s voltage is to be measured. A parallel connection is used because objects in parallel experience the same potential difference. (See Figure 21.27, where the voltmeter is represented by the symbol V.)

Ammeters are connected in series with whatever device’s current is to be measured. A series connection is used because objects in series have the same current passing through them. (See Figure 21.28, where the ammeter is represented by the symbol A.)

# Analog Meters: Galvanometers

Analog meters have a needle that swivels to point at numbers on a scale, as opposed to digital meters, which have numerical readouts similar to a hand-held calculator. The heart of most analog meters is a device called a galvanometer, denoted by G. Current flow through a galvanometer, $I _ { \mathrm { G } }$ , produces a proportional needle deflection. (This deflection is due to the force of a magnetic field upon a current-carrying wire.)

The two crucial characteristics of a given galvanometer are its resistance and current sensitivity. Current sensitivity is the current that gives a full-scale deflection of the galvanometer’s needle, the maximum current that the instrument can measure. For example, a galvanometer with a current sensitivity of $5 0 \mu \mathrm { A }$ has a maximum deflection of its needle when $5 0 \mu \mathrm { A }$ flows through it, reads half-scale when $2 5 \mu \mathrm { A }$ flows through it, and so on.

If such a galvanometer has a resistance, then a voltage of only $V = I R = ( 5 0 { \mu \mathrm { A } } ) ( 2 5 \Omega ) = 1 . 2 5 { \mathrm { ~ m V } }$ produces a full-scale reading. By connecting resistors to this galvanometer in different ways, you can use it as either a voltmeter or ammeter that can measure a broad range of voltages or currents.

# Galvanometer as Voltmeter

Figure 21.29 shows how a galvanometer can be used as a voltmeter by connecting it in series with a large resistance, $R$ . The value of the resistance $R$ is determined by the maximum voltage to be measured. Suppose you want $\boldsymbol { \mathsf { 1 0 } } \boldsymbol { \mathsf { V } }$ to produce a full-scale deflection of a voltmeter containing a $2 5 \ – \Omega$ galvanometer with a $5 0 \mathrm { - } \mu \mathrm { A }$ sensitivity. Then $\boldsymbol { \mathsf { 1 0 } } \boldsymbol { \mathsf { V } }$ applied to the meter must produce a current of $5 0 \mu \mathrm { A }$ . The total resistance must be

$$
R _ { \mathrm { t o t } } = R + r = { \frac { V } { I } } = { \frac { 1 0 \mathrm { V } } { 5 0 \mu \mathrm { A } } } = 2 0 0 \mathrm { k } \Omega , \mathrm { o r }
$$

$$
R = R _ { \mathrm { t o t } } - r = 2 0 0 ~ \mathrm { k } \Omega - 2 5 \Omega \approx 2 0 0 ~ \mathrm { k } \Omega .
$$

( $R$ is so large that the galvanometer resistance, $r$ , is nearly negligible.) Note that $5 \vee$ applied to this voltmeter produces a half-scale deflection by producing a $2 5 \mathrm { - } \mu \mathrm { A }$ current through the meter, and so the voltmeter’s reading is proportional to voltage as desired.

This voltmeter would not be useful for voltages less than about half a volt, because the meter deflection would be small and difficult to read accurately. For other voltage ranges, other resistances are placed in series with the galvanometer. Many meters have a choice of scales. That choice involves switching an appropriate resistance into series with the galvanometer.

$$
- \infty - \infty \sin \theta - \infty )
$$

# Galvanometer as Ammeter

The same galvanometer can also be made into an ammeter by placing it in parallel with a small resistance $R$ , often called the shunt resistance, as shown in Figure 21.30. Since the shunt resistance is small, most of the current passes through it, allowing an ammeter to measure currents much greater than those producing a full-scale deflection of the galvanometer.

Suppose, for example, an ammeter is needed that gives a full-scale deflection for $\pm . 0 \mathsf { A }$ , and contains the same $2 5 - \Omega$ galvanometer with its $5 0 { \mathrm { - } } \mu \mathrm { A }$ sensitivity. Since $R$ and $r$ are in parallel, the voltage across them is the same.

These $I R$ drops are $I R = I _ { \mathrm { G } } r$ so that $\begin{array} { r } { I R = \frac { I _ { \mathrm { G } } } { I } = \frac { R } { r } } \end{array}$ . Solving for $R$ , and noting that $I _ { \mathrm { G } }$ is $5 0 \mu \mathrm { A }$ and $I$ is 0.999950 A, we have

$$
R = r { \frac { I _ { \mathrm { G } } } { I } } = ( 2 5 \Omega ) { \frac { 5 0 \mu \mathrm { A } } { 0 . 9 9 9 9 5 0 \mathrm { A } } } = 1 . 2 5 \times 1 0 ^ { - 3 } \Omega .
$$

# Taking Measurements Alters the Circuit

When you use a voltmeter or ammeter, you are connecting another resistor to an existing circuit and, thus, altering the circuit. Ideally, voltmeters and ammeters do not appreciably affect the circuit, but it is instructive to examine the circumstances under which they do or do not interfere.



First, consider the voltmeter, which is always placed in parallel with the device being measured. Very little current flows through the voltmeter if its resistance is a few orders of magnitude greater than the device, and so the circuit is not appreciably affected. (See Figure 21.31(a).) (A large resistance in parallel with a small one has a combined resistance essentially equal to the small one.) If, however, the voltmeter’s resistance is comparable to that of the device being measured, then the two in parallel have a smaller resistance, appreciably affecting the circuit. (See Figure 21.31(b).) The voltage across the device is not the same as when the voltmeter is out of the circuit.

An ammeter is placed in series in the branch of the circuit being measured, so that its resistance adds to that branch. Normally, the ammeter’s resistance is very small compared with the resistances of the devices in the circuit, and so the extra resistance is negligible. (See Figure 21.32(a).) However, if very small load resistances are involved, or if the ammeter is not as low in resistance as it should be, then the total series resistance is significantly greater, and the current in the branch being measured is reduced. (See Figure 21.32(b).)

A practical problem can occur if the ammeter is connected incorrectly. If it was put in parallel with the resistor to measure the current in it, you could possibly damage the meter; the low resistance of the ammeter would allow most of the current in the circuit to go through the galvanometer, and this current would be larger since the effective resistance is smaller.

One solution to the problem of voltmeters and ammeters interfering with the circuits being measured is to use galvanometers with greater sensitivity. This allows construction of voltmeters with greater resistance and ammeters with smaller resistance than when less sensitive galvanometers are used.

There are practical limits to galvanometer sensitivity, but it is possible to get analog meters that make measurements accurate to a few percent. Note that the inaccuracy comes from altering the circuit, not from a fault in the meter.

# Connections: Limits to Knowledge

Making a measurement alters the system being measured in a manner that produces uncertainty in the measurement. For macroscopic systems, such as the circuits discussed in this module, the alteration can usually be made negligibly small, but it cannot be eliminated entirely. For submicroscopic systems, such as atoms, nuclei, and smaller particles, measurement alters the system in a manner that cannot be made arbitrarily small. This actually limits knowledge of the system—even limiting what nature can know about itself. We shall see profound implications of this when the Heisenberg uncertainty principle is discussed in the modules on quantum mechanics.



There is another measurement technique based on drawing no current at all and, hence, not altering the circuit at all. These are called null measurements and are the topic of Null Measurements. Digital meters that employ solid-state electronics and null measurements can attain accuracies of one part in $1 0 ^ { 6 }$ .

# CHECK YOUR UNDERSTANDING

Digital meters are able to detect smaller currents than analog meters employing galvanometers. How does this explain their ability to measure voltage and current more accurately than analog meters?

# Solution

Since digital meters require less current than analog meters, they alter the circuit less than analog meters. Their resistance as a voltmeter can be far greater than an analog meter, and their resistance as an ammeter can be far less than an analog meter. Consult Figure 21.27 and Figure 21.28 and their discussion in the text.

# PHET EXPLORATIONS

# Circuit Construction Kit (DC Only), Virtual Lab

Stimulate a neuron and monitor what happens. Pause, rewind, and move forward in time in order to observe the ions as they move across the neuron membrane.

Click to view content (https://openstax.org/books/college-physics-2e/pages/21-4-dc-voltmeters-and-ammeters)