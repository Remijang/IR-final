# 23.12 RLC Series AC Circuits

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

• Calculate the impedance, phase angle, resonant frequency, power, power factor, voltage, and/or current in a RLC series circuit.   
• Draw the circuit diagram for an RLC series circuit.   
• Explain the significance of the resonant frequency.

# Impedance

When alone in an AC circuit, inductors, capacitors, and resistors all impede current. How do they behave when all three occur together? Interestingly, their individual resistances in ohms do not simply add. Because inductors and capacitors behave in opposite ways, they partially to totally cancel each other’s effect. Figure 23.46 shows an RLC series circuit with an AC voltage source, the behavior of which is the subject of this section. The crux of the analysis of an RLCcircuit is the frequency dependence of $X _ { L }$ and $X _ { C }$ , and the effect they have on the phase of voltage versus current (established in the preceding section). These give rise to the frequency dependence of the circuit, with important “resonance” features that are the basis of many applications, such as radio tuners.

The combined effect of resistance $R$ , inductive reactance $X _ { L }$ , and capacitive reactance $X _ { C }$ is defined to be impedance, an AC analogue to resistance in a DC circuit. Current, voltage, and impedance in an $_ { R L C }$ circuit are related by an AC version of Ohm’s law:

$$
I _ { 0 } = { \frac { V _ { 0 } } { Z } } \mathrm { o r } I _ { \mathrm { r m s } } = { \frac { V _ { \mathrm { r m s } } } { Z } } .
$$

Here $I _ { 0 }$ is the peak current, $V _ { 0 }$ the peak source voltage, and $Z$ is the impedance of the circuit. The units of impedance are ohms, and its effect on the circuit is as you might expect: the greater the impedance, the smaller the current. To get an expression for $Z$ in terms of $R$ , $X _ { L }$ , and $X _ { C }$ , we will now examine how the voltages across the various components are related to the source voltage. Those voltages are labeled $V _ { R } , V _ { L }$ , and $V _ { C }$ in Figure 23.46.

Conservation of charge requires current to be the same in each part of the circuit at all times, so that we can say the currents in $R , L$ , and $C$ are equal and in phase. But we know from the preceding section that the voltage across the inductor $V _ { L }$ leads the current by one-fourth of a cycle, the voltage across the capacitor $V _ { C }$ follows the current by one-fourth of a cycle, and the voltage across the resistor $V _ { R }$ is exactly in phase with the current. Figure 23.47 shows these relationships in one graph, as well as showing the total voltage around the circuit $V = V _ { R } + V _ { L } + V _ { C }$ , where all four voltages are the instantaneous values. According to Kirchhoff’s loop rule, the total voltage around the circuit $V$ is also the voltage of the source.

You can see from Figure 23.47 that while $V _ { R }$ is in phase with the current, $V _ { L }$ leads by $9 0 ^ { \circ }$ , and $V _ { C }$ follows by $9 0 ^ { \circ }$ . Thus $V _ { L }$ and $V _ { C }$ are $1 8 0 ^ { \circ }$ out of phase (crest to trough) and tend to cancel, although not completely unless they have the same magnitude. Since the peak voltages are not aligned (not in phase), the peak voltage $V _ { 0 }$ of the source does notequal the sum of the peak voltages across $R , L$ , and $C$ . The actual relationship is

$$
V _ { 0 } = { \sqrt { { V _ { 0 R } \mathrm { \Omega } } ^ { 2 } + { ( V _ { 0 L } - V _ { 0 C } ) } ^ { 2 } } } ,
$$

where $V _ { 0 R } , V _ { 0 L }$ , and $V _ { 0 C }$ are the peak voltages across $R , L ,$ , and $C$ , respectively. Now, using Ohm’s law and definitions from Reactance, Inductive and Capacitive, we substitute $V _ { \mathrm { 0 } } = I _ { \mathrm { 0 } } Z$ into the above, as well as $V _ { 0 R } = I _ { 0 } R , V _ { 0 L } = I _ { 0 } X _ { L }$ , and $V _ { 0 C } = I _ { 0 } X _ { C }$ , yielding

$$
I _ { 0 } Z = \sqrt { { I _ { 0 } } ^ { 2 } R ^ { 2 } + ( I _ { 0 } X _ { L } - I _ { 0 } X _ { C } ) ^ { 2 } } = I _ { 0 } \sqrt { R ^ { 2 } + ( X _ { L } - X _ { C } ) ^ { 2 } } .
$$

$I _ { 0 }$ cancels to yield an expression for $Z$ :

$$
Z = \sqrt { R ^ { 2 } + ( X _ { L } - X _ { C } ) ^ { 2 } } ,
$$

which is the impedance of an $_ { R L C }$ series AC circuit. For circuits without a resistor, take $R = 0$ ; for those without an inductor, take $X _ { L } = 0$ ; and for those without a capacitor, take $X _ { C } = 0$ .

# EXAMPLE 23.12

# Calculating Impedance and Current

An RLCseries circuit has a $4 0 . 0 \Omega$ resistor, a $3 . 0 0 \mathsf { m } \mathsf { H }$ inductor, and a $5 . 0 0 \mu \mathrm { F }$ capacitor. (a) Find the circuit’s impedance at $6 0 . 0 { \mathsf { H z } }$ and $1 0 . 0 \mathsf { k H z }$ , noting that these frequencies and the values for $L$ and $C$ are the same as in Example 23.10 and Example 23.11. (b) If the voltage source has $V _ { \mathrm { r m s } } = 1 2 0 \ : \mathrm { V }$ , what is $I _ { \mathrm { r m s } }$ at each frequency?

# Strategy

For each frequency, we use $\begin{array} { r } { Z = \sqrt { R ^ { 2 } + ( X _ { L } - X _ { C } ) ^ { 2 } } } \end{array}$ to find the impedance and then Ohm’s law to find current. We can take advantage of the results of the previous two examples rather than calculate the reactances again.

# Solution for (a)

At $6 0 . 0 { \mathsf { H z } }$ , the values of the reactances were found in Example 23.10 to be $X _ { L } = 1 . 1 3 \Omega$ and in Example 23.11 to be $X _ { C } = 5 3 1 \Omega$ . Entering these and the given $4 0 . 0 \Omega$ for resistance into $\begin{array} { r } { Z = \sqrt { R ^ { 2 } + ( X _ { L } - X _ { C } ) ^ { 2 } } } \end{array}$ yields

$$
\begin{array} { r c l } { { Z } } & { { = } } & { { \sqrt { R ^ { 2 } + ( X _ { L } - X _ { C } ) ^ { 2 } \ } } } \\ { { } } & { { = } } & { { \sqrt { ( 4 0 . 0 \ \Omega ) ^ { 2 } + ( 1 . 1 3 \Omega - 5 3 1 \ \Omega ) ^ { 2 } \ } } } \\ { { } } & { { = } } & { { 5 3 1 \ \Omega \ \mathrm { a t } \ 6 0 . 0 \ \mathrm { H z } . } } \end{array}
$$

Similarly, at $1 0 . 0 \mathsf { k H z }$ , $X _ { L } = 1 8 8 \Omega$ and $X _ { C } = 3 . 1 8 \Omega$ , so that

$$
\begin{array} { l l l } { { Z } } & { { = } } & { { \sqrt { ( 4 0 . 0 \Omega ) ^ { 2 } + ( 1 8 8 \Omega - 3 . 1 8 \Omega ) ^ { 2 } } } } \\ { { } } & { { = } } & { { 1 9 0 \Omega \mathrm { a t } 1 0 . 0 \mathrm { k H z } . } } \end{array}
$$

# Discussion for (a)

In both cases, the result is nearly the same as the largest value, and the impedance is definitely not the sum of the individual values. It is clear that $X _ { L }$ dominates at high frequency and $X _ { C }$ dominates at low frequency.

# Solution for (b)

The current $I _ { \mathrm { r m s } }$ can be found using the AC version of Ohm’s law in Equation $I _ { \mathrm { r m s } } = V _ { \mathrm { r m s } } / Z$ :

$$
\begin{array} { r } { I _ { \mathrm { r m s } } = \frac { V _ { \mathrm { r m s } } } { Z } = \frac { 1 2 0 \mathrm { ~ V } } { 5 3 1 \Omega } = 0 . 2 2 6 \mathrm { ~ A ~ a t ~ } 6 0 . 0 \mathsf { H z } } \end{array}
$$

Finally, at $1 0 . 0 \mathsf { k H z }$ , we find

$$
\begin{array} { r } { I _ { \mathrm { r m s } } = \frac { V _ { \mathrm { r m s } } } { Z } = \frac { 1 2 0 ~ \mathrm { V } } { 1 9 0 ~ \Omega } = 0 . 6 3 3 ~ \mathrm { A a t } 1 0 . 0 ~ \mathrm { k H z } } \end{array}
$$

# Discussion for (a)

The current at $6 0 . 0 { \mathsf { H z } }$ is the same (to three digits) as found for the capacitor alone in Example 23.11. The capacitor dominates at low frequency. The current at $1 0 . 0 \mathsf { k H z }$ is only slightly different from that found for the inductor alone in Example 23.10. The inductor dominates at high frequency.

# Resonance in RLCSeries AC Circuits

How does an $_ { R L C }$ circuit behave as a function of the frequency of the driving voltage source? Combining Ohm’s law, $I _ { \mathrm { r m s } } = V _ { \mathrm { r m s } } / Z$ , and the expression for impedance $Z$ from $\begin{array} { r } { Z = \sqrt { R ^ { 2 } + ( X _ { L } - X _ { C } ) ^ { 2 } } } \end{array}$ gives

$$
I _ { \mathrm { r m s } } = { \frac { V _ { \mathrm { r m s } } } { \sqrt { R ^ { 2 } + ( X _ { L } - X _ { C } ) ^ { 2 } } } } .
$$

The reactances vary with frequency, with $X _ { L }$ large at high frequencies and $X _ { C }$ large at low frequencies, as we have seen in three previous examples. At some intermediate frequency $f _ { 0 }$ , the reactances will be equal and cancel, giving $Z = R$ —this is a minimum value for impedance, and a maximum value for $I _ { \mathrm { r m s } }$ results. We can get an

expression for $f _ { 0 }$ by taking

$$
X _ { L } = X _ { C } .
$$

Substituting the definitions of $X _ { L }$ and $X _ { C }$ ,

$$
2 \pi f _ { 0 } L = { \frac { 1 } { 2 \pi f _ { 0 } C } } .
$$

Solving this expression for $f _ { 0 }$ yields

$$
f _ { 0 } = \frac { 1 } { 2 \pi \sqrt { L C } } ,
$$

where $f _ { 0 }$ is the resonant frequency of an $_ { R L C }$ series circuit. This is also the naturalfrequencyat which the circuit would oscillate if not driven by the voltage source. At $f _ { 0 }$ , the effects of the inductor and capacitor cancel, so that $Z = R$ , and $I _ { \mathrm { r m s } }$ is a maximum.

Resonance in AC circuits is analogous to mechanical resonance, where resonance is defined to be a forced oscillation—in this case, forced by the voltage source—at the natural frequency of the system. The receiver in a radio is an $_ { R L C }$ circuit that oscillates best at its $f _ { 0 }$ . A variable capacitor is often used to adjust $f _ { 0 }$ to receive a desired frequency and to reject others. Figure 23.48 is a graph of current as a function of frequency, illustrating a resonant peak in $I _ { \mathrm { r m s } }$ at $f _ { 0 }$ . The two curves are for two different circuits, which differ only in the amount of resistance in them. The peak is lower and broader for the higher-resistance circuit. Thus the higher-resistance circuit does not resonate as strongly and would not be as selective in a radio receiver, for example.

# EXAMPLE 23.13

# Calculating Resonant Frequency and Current

For the same $_ { R L C }$ series circuit having a $4 0 . 0 \Omega$ resistor, a $3 . 0 0 ~ \mathrm { m H }$ inductor, and a $5 . 0 0 \mu \mathrm { F }$ capacitor: (a) Find the resonant frequency. (b) Calculate $I _ { \mathrm { r m s } }$ at resonance if $V _ { \mathrm { r m s } }$ is $\textstyle 1 2 0 \vee .$ .

# Strategy

The resonant frequency is found by using the expression in $\begin{array} { r } { f _ { 0 } = \frac { 1 } { 2 \pi \sqrt { L C } } } \end{array}$ . The current at that frequency is the same as if the resistor alone were in the circuit.

# Solution for (a)

$L$ $C$ $f _ { 0 }$ $\begin{array} { r } { f _ { 0 } = \frac { 1 } { 2 \pi \sqrt { L C } } } \end{array}$

$$
{ \begin{array} { l l l } { f _ { 0 } } & { = } & { { \frac { 1 } { 2 \pi { \sqrt { L C } } } } } \\ & { = } & { { \frac { 1 } { 2 \pi { \sqrt { ( 3 . 0 0 \times 1 0 ^ { - 3 } ~ { \mathrm { H } } ) ( 5 . 0 0 \times 1 0 ^ { - 6 } ~ { \mathrm { F } } ) } } } } = 1 . 3 0 ~ { \mathrm { k H z } } . } \end{array} }
$$

# Discussion for (a)

We see that the resonant frequency is between $6 0 . 0 { \mathsf { H z } }$ and $1 0 . 0 \mathsf { k H z }$ , the two frequencies chosen in earlier examples. This was to be expected, since the capacitor dominated at the low frequency and the inductor dominated at the high frequency. Their effects are the same at this intermediate frequency.

# Solution for (b)

The current is given by Ohm’s law. At resonance, the two reactances are equal and cancel, so that the impedance equals the resistance alone. Thus,

$$
I _ { \mathrm { r m s } } = { \frac { V _ { \mathrm { r m s } } } { Z } } = { \frac { 1 2 0 { \mathrm { V } } } { 4 0 . 0 \Omega } } = 3 . 0 0 { \mathrm { A } } .
$$

# Discussion for (b)

At resonance, the current is greater than at the higher and lower frequencies considered for the same circuit in the preceding example.

# Power in RLCSeries AC Circuits

If current varies with frequency in an RLCcircuit, then the power delivered to it also varies with frequency. But the average power is not simply current times voltage, as it is in purely resistive circuits. As was seen in Figure 23.47, voltage and current are out of phase in an RLCcircuit. There is a phase angle $\phi$ between the source voltage $V$ and the current $I$ , which can be found from

$$
\cos \phi = { \frac { R } { Z } } .
$$

For example, at the resonant frequency or in a purely resistive circuit $Z = R$ , so that $\phi = 1$ . This implies that $\phi = 0 ^ { \circ }$ and that voltage and current are in phase, as expected for resistors. At other frequencies, average power is less than at resonance. This is both because voltage and current are out of phase and because $I _ { \mathrm { r m s } }$ is lower. The fact that source voltage and current are out of phase affects the power delivered to the circuit. It can be shown that the averagepower is

$$
P _ { \mathrm { a v e } } = I _ { \mathrm { r m s } } V _ { \mathrm { r m s } } { \cos \phi } ,
$$

Thus $\phi$ is called the power factor, which can range from 0 to 1. Power factors near 1 are desirable when designing an efficient motor, for example. At the resonant frequency, $\phi = 1$ .

# EXAMPLE 23.14

# Calculating the Power Factor and Power

For the same $_ { R L C }$ series circuit having a $4 0 . 0 \Omega$ resistor, a $3 . 0 0 ~ \mathrm { m H }$ inductor, a $5 . 0 0 \mu \mathrm { F }$ capacitor, and a voltage source with a $V _ { \mathrm { r m s } }$ of $\textstyle 1 2 0 \vee$ : (a) Calculate the power factor and phase angle for $f = 6 0 . 0 \mathrm { H z }$ . (b) What is the average power at $5 0 . 0 \mathsf { H z ? }$ (c) Find the average power at the circuit’s resonant frequency.

# Strategy and Solution for (a)

The power factor at $6 0 . 0 { \scriptstyle { \mathsf { H z } } }$ is found from

$$
\cos \phi = { \frac { R } { Z } } .
$$

We know $Z = 5 3 1 \Omega$ from Example 23.12, so that

$$
\cos \phi = { \frac { 4 0 . 0 \Omega } { 5 3 1 \Omega } } = 0 . 0 7 5 3 { \mathrm { ~ a t ~ } } 6 0 . 0 { \mathrm { ~ H z } } .
$$

This small value indicates the voltage and current are significantly out of phase. In fact, the phase angle is

# Discussion for (a)

The phase angle is close to $9 0 ^ { \circ }$ , consistent with the fact that the capacitor dominates the circuit at this low frequency (a pure RCcircuit has its voltage and current $9 0 ^ { \circ }$ out of phase).

# Strategy and Solution for (b)

The average power at $6 0 . 0 { \mathsf { H z } }$ is

$$
P _ { \mathrm { a v e } } = I _ { \mathrm { r m s } } V _ { \mathrm { r m s } } { \cos \Phi } .
$$

$I _ { \mathrm { r m s } }$ was found to be 0.226 A in Example 23.12. Entering the known values gives

$$
P _ { \mathrm { a v e } } = ( 0 . 2 2 6 \mathrm { ~ A } ) ( 1 2 0 \mathrm { ~ V } ) ( 0 . 0 7 5 3 ) = 2 . 0 4 \mathrm { ~ W }
$$

# Strategy and Solution for (c)

At the resonant frequency, we know $\phi = 1$ , and $I _ { \mathrm { r m s } }$ was found to be 6.00 A in Example 23.13. Thus, $P _ { \mathrm { a v e } } = ( 3 . 0 0 \mathrm { A } ) ( 1 2 0 \mathrm { V } ) ( 1 ) = 3 6 0 \mathrm { W }$ at resonance $( 1 . 3 0 \mathsf { k H z } )$ 1

# Discussion

Both the current and the power factor are greater at resonance, producing significantly greater power than at higher and lower frequencies.

Power delivered to an RLCseries AC circuit is dissipated by the resistance alone. The inductor and capacitor have energy input and output but do not dissipate it out of the circuit. Rather they transfer energy back and forth to one another, with the resistor dissipating exactly what the voltage source puts into the circuit. This assumes no significant electromagnetic radiation from the inductor and capacitor, such as radio waves. Such radiation can happen and may even be desired, as we will see in the next chapter on electromagnetic radiation, but it can also be suppressed as is the case in this chapter. The circuit is analogous to the wheel of a car driven over a corrugated road as shown in Figure 23.49. The regularly spaced bumps in the road are analogous to the voltage source, driving the wheel up and down. The shock absorber is analogous to the resistance damping and limiting the amplitude of the oscillation. Energy within the system goes back and forth between kinetic (analogous to maximum current, and energy stored in an inductor) and potential energy stored in the car spring (analogous to no current, and energy stored in the electric field of a capacitor). The amplitude of the wheels’ motion is a maximum if the bumps in the road are hit at the resonant frequency.

A pure LCcircuit with negligible resistance oscillates at $f _ { 0 }$ , the same resonant frequency as an RLCcircuit. It can serve as a frequency standard or clock circuit—for example, in a digital wristwatch. With a very small resistance, only a very small energy input is necessary to maintain the oscillations. The circuit is analogous to a car with no shock absorbers. Once it starts oscillating, it continues at its natural frequency for some time. Figure 23.50 shows the

analogy between an LCcircuit and a mass on a spring.

# PHET EXPLORATIONS

# Circuit Construction Kit $( A C + D C )$ , Virtual Lab

Build circuits with capacitors, inductors, resistors and AC or DC voltage sources, and inspect them using lab instruments such as voltmeters and ammeters.

Click to view content (https://openstax.org/books/college-physics-2e/pages/23-12-rlc-series-ac-circuits)

# Glossary

back emf the emf generated by a running motor, because it consists of a coil turning in a magnetic field; it opposes the voltage powering the motor   
capacitive reactance the opposition of a capacitor to a change in current; calculated by   
characteristic time constant denoted by $\tau$ , of a particular series $R L$ circuit is calculated by $\begin{array} { r } { \tau = \frac { L } { R } } \end{array}$ , where $L$ is the inductance and $R$ is the resistance   
eddy current a current loop in a conductor caused by motional emf   
electric generator a device for converting mechanical work into electric energy; it induces an emf by rotating a coil in a magnetic field   
electromagnetic induction the process of inducing an emf (voltage) with a change in magnetic flux   
emf induced in a generator coil ${ \mathrm { : m f } } = N A B \omega$ sin $\omega t$ , where $A$ is the area of an $N$ -turn coil rotated at a constant angular velocity $\omega$ in a uniform magnetic field $B$ , over a period of time $t$   
energy stored in an inductor self-explanatory; calculated by $\begin{array} { r } { E _ { \mathrm { i n d } } = \frac { 1 } { 2 } L I ^ { 2 } } \end{array}$   
Faraday’s law of induction the means of calculating the emf in a coil due to changing magnetic flux, given by   
henry the unit of inductance; $1 \ \mathrm { H } = 1 \ \Omega \cdot \mathrm { s }$   
impedance the AC analogue to resistance in a DC circuit; it is the combined effect of resistance, inductive reactance, and capacitive reactance in the form $\begin{array} { r } { Z = \sqrt { R ^ { 2 } + ( X _ { L } - X _ { C } ) ^ { 2 } } } \end{array}$   
inductance a property of a device describing how efficient it is at inducing emf in another device   
induction (magnetic induction) the creation of emfs and hence currents by magnetic fields   
inductive reactance the opposition of an inductor to a change in current; calculated by $X _ { L } = 2 \pi f L$   
inductor a device that exhibits significant selfinductance   
Lenz’s law the minus sign in Faraday’s law, signifying that the emf induced in a coil opposes the change in magnetic flux   
magnetic damping the drag produced by eddy currents   
magnetic flux the amount of magnetic field going through a particular area, calculated with ${ \pmb { \phi } } = B A$ cos $\theta$ where $B$ is the magnetic field strength over an area $A$ at an angle $\theta$ with the perpendicular to the area   
mutual inductance how effective a pair of devices are at inducing emfs in each other   
peak emf ${ \mathrm { e m f } } _ { 0 } = N A B \omega$   
phase angle denoted by $\phi$ , the amount by which the voltage and current are out of phase with each other in a circuit   
power factor the amount by which the power delivered in the circuit is less than the theoretical maximum of the circuit due to voltage and current being out of phase; calculated by $\phi$   
resonant frequency the frequency at which the impedance in a circuit is at a minimum, and also the frequency at which the circuit would oscillate if not driven by a voltage source; calculated by $\begin{array} { r } { f _ { 0 } = \frac { 1 } { 2 \pi \sqrt { L C } } } \end{array}$   
self-inductance how effective a device is at inducing emf in itself   
shock hazard the term for electrical hazards due to current passing through a human   
step-down transformer a transformer that decreases voltage   
step-up transformer a transformer that increases voltage   
thermal hazard the term for electrical hazards due to overheating   
three-wire system the wiring system used at present for safety reasons, with live, neutral, and ground wires   
transformer a device that transforms voltages from one value to another using induction   
transformer equation the equation showing that the ratio of the secondary to primary voltages in a transformer equals the ratio of the number of loops in their coils;



# Section Summary

# 23.1 Induced Emf and Magnetic Flux

• The crucial quantity in induction is magnetic flux $\boldsymbol { \phi }$ , defined to be ${ \pmb { \phi } } = B A$ cos $\theta$ , where $B$ is the magnetic field strength over an area $A$ at an angle $\theta$ with the perpendicular to the area.   
• Units of magnetic flux $\pmb { \phi }$ are $\mathrm { m } ^ { 2 }$ .   
• Any change in magnetic flux $\pmb { \phi }$ induces an

emf—the process is defined to be electromagnetic induction.

# 23.2 Faraday’s Law of Induction: Lenz’s Law

• Faraday’s law of induction states that the emfinduced by a change in magnetic flux is

$\mathrm { e m f } = - N { \frac { \Delta { \phi } } { \Delta t } }$   
when flux changes by $\Delta \phi$ in a time $\Delta t$ .   
If emf is induced in a coil, $N$ is its number of turns. The minus sign means that the emf creates a   
current $I$ and magnetic field $B$ thatop osethe changeinflux $\Delta \phi$ —this opposition is known as Lenz’s law.

# 23.3 Motional Emf

• An emf induced by motion relative to a magnetic field $B$ is called a motionalemfand is given by e $\mathbf { \nabla } \mathrm { m f } = B \ell v$ （ $[ B , \ell ]$ ,and $v$ perpendicular), where $\ell$ is the length of the object moving at speed $v$ relative to the field.

# 23.4 Eddy Currents and Magnetic Damping

• Current loops induced in moving conductors are called eddy currents.   
• They can create significant drag, called magnetic damping.

# 23.5 Electric Generators

• An electric generator rotates a coil in a magnetic field, inducing an emfgiven as a function of time by ${ \mathrm { e m f } } = N A B \omega$ sin $\omega t$ ， where $A$ is the area of an $N$ -turn coil rotated at a constant angular velocity $\omega$ in a uniform magnetic field $B$ .   
• The peak emf of a generator is ${ \mathrm { e m f } } _ { 0 } = N A B \omega .$

# 23.6 Back Emf

• Any rotating coil will have an induced emf—in motors, this is called back emf, since it opposes the emf input to the motor.

# 23.7 Transformers

Transformers use induction to transform voltages from one value to another.   
• For a transformer, the voltages across the primary and secondary coils are related by $\frac { V _ { \mathrm { s } } } { V _ { \mathrm { p } } } = \frac { N _ { \mathrm { s } } } { N _ { \mathrm { p } } } ,$ where $V _ { \mathfrak { p } }$ and $V _ { \mathrm { s } }$ are the voltages across primary and secondary coils having $N _ { \mathfrak { p } }$ and $N _ { \mathrm { s } }$ turns. The currents $I _ { \mathrm { p } }$ and $I _ { \mathrm { s } }$ in the primary and secondary coils are related by $\begin{array} { r } { \frac { I _ { \mathrm { S } } } { I _ { \mathrm { p } } } = \frac { N _ { \mathrm { p } } } { N _ { \mathrm { s } } } } \end{array}$   
• A step-up transformer increases voltage and decreases current, whereas a step-down transformer decreases voltage and increases current.

# 23.8 Electrical Safety: Systems and Devices

• Electrical safety systems and devices are employed to prevent thermal and shock hazards.   
• Circuit breakers and fuses interrupt excessive currents to prevent thermal hazards.   
• The three-wire system guards against thermal and shock hazards, utilizing live/hot, neutral, and earth/ground wires, and grounding the neutral wire and case of the appliance.   
• A ground fault interrupter (GFI) prevents shock by detecting the loss of current to unintentional paths.   
• An isolation transformer insulates the device being powered from the original source, also to prevent shock.   
• Many of these devices use induction to perform their basic function.

# 23.9 Inductance

• Inductance is the property of a device that tells how effectively it induces an emf in another device.   
• Mutual inductance is the effect of two devices in inducing emfs in each other.   
• A change in current $\Delta I _ { 1 } / \Delta t$ in one induces an emf $\mathrm { e m f } _ { 2 }$ in the second: $\mathrm { e m f } _ { 2 } = - M \frac { \Delta I _ { 1 } } { \Delta t } ,$ where $M$ is defined to be the mutual inductance between the two devices, and the minus sign is due to Lenz’s law.   
Symmetrically, a change in current $\Delta I _ { 2 } / \Delta t$ through the second device induces an emf in the first: $\mathrm { e m f } _ { 1 } = - M \frac { \Delta I _ { 2 } } { \Delta t } ,$ where $M$ is the same mutual inductance as in the reverse process. Current changes in a device induce an emf in the device itself.   
• Self-inductance is the effect of the device inducing emf in itself. The device is called an inductor, and the emf induced in it by a change in current through it is $\mathrm { e m f } = - L { \frac { \Delta I } { \Delta t } }$ ， where $L$ is the self-inductance of the inductor, and $\Delta I / \Delta t$ is the rate of change of current through it. The minus sign indicates that emf opposes the change in current, as required by Lenz’s law.   
The unit of self- and mutual inductance is the henry $( \mathsf { H } )$ , where $1 \ \mathrm { H = } 1 \ \Omega \cdot \mathrm { s }$ .   
• The self-inductance $L$ of an inductor is proportional to how much flux changes with current. For an $N$ -turn inductor, $L = N { \frac { \Delta \phi } { \Delta I } } .$   
The self-inductance of a solenoid is $L = { \frac { \mu _ { 0 } N ^ { 2 } A } { \ell } } { \mathrm { ( s o l e n o i d ) } } ,$ where $N$ is its number of turns in the solenoid, is its cross-sectional area, $\ell$ is its length, and $\mu _ { 0 } = 4 \pi \times 1 0 ^ { - 7 } { \mathrm { ~ T ~ } } { \cdot } { \mathrm { m } } / { \mathrm { A } }$ is the permeability of free space.   
The energy stored in an inductor $E _ { \mathrm { i n d } }$ is $E _ { \mathrm { i n d } } = { \frac { 1 } { 2 } } L I ^ { 2 } .$



# 23.10 RL Circuits

• When a series connection of a resistor and an inductor—an $R L$ circuit—is connected to a voltage source, the time variation of the current is $I = I _ { 0 } ( 1 - e ^ { - t / \tau } )$ (turning on). where $I _ { 0 } = V / R$ is the final current.   
• The characteristic time constant $\tau$ is $\begin{array} { r } { \tau = \frac { L } { R } } \end{array}$ where $L$ is the inductance and $R$ is the resistance.   
• In the first time constant $\tau$ , the current rises from zero to $0 . 6 3 2 I _ { 0 }$ , and 0.632 of the remainder in every subsequent time interval $\tau$ .   
• When the inductor is shorted through a resistor, current decreases as I=Ie-tlt (turning off). Here $I _ { 0 }$ is the initial current.   
• Current falls to $0 . 3 6 8 I _ { 0 }$ in the first time interval $\tau$ , and 0.368 of the remainder toward zero in each subsequent time $\tau$ .

# 23.11 Reactance, Inductive and Capacitive

• For inductors in AC circuits, we find that when a sinusoidal voltage is applied to an inductor, the voltage leads the current by one-fourth of a cycle, or by a $9 0 ^ { \circ }$ phase angle.   
• The opposition of an inductor to a change in current is expressed as a type of AC resistance.   
• Ohm’s law for an inductor is $I = { \frac { V } { X _ { L } } } ,$ where $V$ is the rms voltage across the inductor. $X _ { L }$ is defined to be the inductive reactance, given by $X _ { L } = 2 \pi f L ,$ with $f$ the frequency of the AC voltage source in hertz.   
• Inductive reactance $X _ { L }$ has units of ohms and is greatest at high frequencies.   
• For capacitors, we find that when a sinusoidal voltage is applied to a capacitor, the voltage follows the current by one-fourth of a cycle, or by a $9 0 ^ { \circ }$ phase angle. Since a capacitor can stop current when fully charged, it limits current and offers another form of AC resistance; Ohm’s law for a capacitor is $I = { \frac { V } { X _ { C } } } ,$ where $V$ is the rms voltage across the capacitor.   
• $X _ { C }$ is defined to be the capacitive reactance, given by $\overset { \cdot } { X } _ { C } = \frac { 1 } { 2 \pi f C } .$ $X _ { C }$ has units of ohms and is greatest at low frequencies.



# 23.12 RLC Series AC Circuits

• The AC analogy to resistance is impedance $Z$ , the combined effect of resistors, inductors, and capacitors, defined by the AC version of Ohm’s law: $I _ { 0 } = { \frac { V _ { 0 } } { Z } } \ { \mathrm { o r } } \ I _ { \mathrm { r m s } } = { \frac { V _ { \mathrm { r m s } } } { Z } } ,$ where $I _ { 0 }$ is the peak current and $V _ { 0 }$ is the peak source voltage.   
• Impedance has units of ohms and is given by $\begin{array} { r } { Z = \sqrt { R ^ { 2 } + ( X _ { L } - X _ { C } ) ^ { 2 } } } \end{array}$ .   
• The resonant frequency $f _ { 0 }$ , at which $X _ { L } = X _ { C }$ , is $f _ { 0 } = \frac { 1 } { 2 \pi \sqrt { L C } } .$   
• In an AC circuit, there is a phase angle $\phi$ between source voltage $V$ and the current $I$ , which can be found from cosΦ=,   
• $\phi = 0 ^ { \circ }$ for a purely resistive circuit or an RLC circuit at resonance.   
• The average power delivered to an $_ { R L C }$ circuit is affected by the phase angle and is given by $P _ { \mathrm { a v e } } = I _ { \mathrm { r m s } } V _ { \mathrm { r m s } }$ cos $\phi$ ， cos $\phi$ is called the power factor, which ranges from 0 to 1.

# Conceptual Questions

# 23.1 Induced Emf and Magnetic Flux

1. How do the multiple-loop coils and iron ring in the version of Faraday’s apparatus shown in Figure 23.3 enhance the observation of induced emf?   
2. When a magnet is thrust into a coil as in Figure 23.4(a), what is the direction of the force exerted by the coil on the magnet? Draw a diagram showing the direction of the current induced in the coil and the magnetic field it produces, to justify your response. How does the magnitude of the force depend on the resistance of the galvanometer?   
3. Explain how magnetic flux can be zero when the magnetic field is not zero.   
4. Is an emf induced in the coil in Figure 23.51 when it is stretched? If so, state why and give the direction of the induced current.

FIGURE 23.51 A circular coil of wire is stretched in a magnetic field.

# 23.2 Faraday’s Law of Induction: Lenz’s Law

5. A person who works with large magnets sometimes places her head inside a strong field. She reports feeling dizzy as she quickly turns her head. How might this be associated with induction?   
6. A particle accelerator sends high-velocity charged particles down an evacuated pipe. Explain how a coil of wire wrapped around the pipe could detect the passage of individual particles. Sketch a graph of the voltage output of the coil as a single particle passes through it.

# 23.3 Motional Emf

7. Why must part of the circuit be moving relative to other parts, to have usable motional emf? Consider, for example, that the rails in Figure 23.10 are stationary relative to the magnetic field, while the rod moves.

8. A powerful induction cannon can be made by placing a metal cylinder inside a solenoid coil. The cylinder is forcefully expelled when solenoid current is turned on rapidly. Use Faraday’s and Lenz’s laws to explain how this works. Why might the cylinder get live/hot when the cannon is fired?   
9. An induction stove heats a pot with a coil carrying an alternating current located beneath the pot (and without a hot surface). Can the stove surface be a conductor? Why won’t a coil carrying a direct current work?   
10. Explain how you could thaw out a frozen water pipe by wrapping a coil carrying an alternating current around it. Does it matter whether or not the pipe is a conductor? Explain.

# 23.4 Eddy Currents and Magnetic Damping

11. Explain why magnetic damping might not be effective on an object made of several thin conducting layers separated by insulation.   
12. Explain how electromagnetic induction can be used to detect metals? This technique is particularly important in detecting buried landmines for disposal, geophysical prospecting and at airports.

# 23.5 Electric Generators

13. Using RHR-1, show that the emfs in the sides of the generator loop in Figure 23.22 are in the same sense and thus add.   
14. The source of a generator’s electrical energy output is the work done to turn its coils. How is the work needed to turn the generator related to Lenz’s law?

# 23.6 Back Emf

15. Suppose you find that the belt drive connecting a powerful motor to an air conditioning unit is broken and the motor is running freely. Should you be worried that the motor is consuming a great deal of energy for no useful purpose? Explain why or why not.

# 23.7 Transformers

16. Explain what causes physical vibrations in transformers at twice the frequency of the AC power involved.

# 23.8 Electrical Safety: Systems and Devices

17. Does plastic insulation on live/hot wires prevent shock hazards, thermal hazards, or both?   
18. Why are ordinary circuit breakers and fuses ineffective in preventing shocks?   
19. A GFI may trip just because the live/hot and neutral wires connected to it are significantly different in length. Explain why.

# 23.9 Inductance

20. How would you place two identical flat coils in contact so that they had the greatest mutual inductance? The least?   
21. How would you shape a given length of wire to give it the greatest self-inductance? The least?   
22. Verify, as was concluded without proof in Example 23.7, that units of $\cdot \mathrm { m } ^ { 2 } / A = \Omega \cdot \mathrm { s } = \mathrm { H }$ .

# 23.11 Reactance, Inductive and Capacitive

23. Presbycusis is a hearing loss due to age that progressively affects higher frequencies. A hearing aid amplifier is designed to amplify all frequencies equally. To adjust its output for presbycusis, would you put a capacitor in series or parallel with the hearing aid’s speaker? Explain.   
24. Would you use a large inductance or a large capacitance in series with a system to filter out low frequencies, such as the $1 0 0 { \mathsf { H z } }$ hum in a sound system? Explain.   
25. High-frequency noise in AC power can damage computers. Does the plug-in unit designed to prevent this damage use a large inductance or a large capacitance (in series with the computer) to filter out such high frequencies? Explain.   
26. Does inductance depend on current, frequency, or both? What about inductive reactance?

27. Explain why the capacitor in Figure 23.52(a) acts as a low-frequency filter between the two circuits, whereas that in Figure 23.52(b) acts as a highfrequency filter.

28. If the capacitors in Figure 23.52 are replaced by inductors, which acts as a low-frequency filter and which as a high-frequency filter?

# 23.12 RLC Series AC Circuits

29. Does the resonant frequency of an AC circuit depend on the peak voltage of the AC source? Explain why or why not.   
30. Suppose you have a motor with a power factor significantly less than 1. Explain why it would be better to improve the power factor as a method of improving the motor’s output, rather than to increase the voltage input.

# Problems & Exercises

# 23.1 Induced Emf and Magnetic Flux

1. What is the value of the magnetic flux at coil 2 in Figure 23.53 due to coil 1?

2. What is the value of the magnetic flux through the coil in Figure 23.53(b) due to the wire?

# 23.2 Faraday’s Law of Induction: Lenz’s Law

3. Referring to Figure 23.54(a), what is the direction of the current induced in coil 2: (a) If the current in coil 1 increases? (b) If the current in coil 1 decreases? (c) If the current in coil 1 is constant? Explicitly show how you follow the steps in the Problem-Solving Strategy for Lenz's Law.

4. Referring to Figure 23.54(b), what is the direction of the current induced in the coil: (a) If the current in the wire increases? (b) If the current in the wire decreases? (c) If the current in the wire suddenly changes direction? Explicitly show how you follow the steps in the Problem-Solving Strategy for Lenz’s Law.

5. Referring to Figure 23.55, what are the directions of the currents in coils 1, 2, and 3 (assume that the coils are lying in the plane of the circuit): (a) When the switch is first closed? (b) When the switch has been closed for a long time? (c) Just after the switch is opened?

6. Repeat the previous problem with the battery reversed.   
7. Verify that the units of $\Delta \phi / \Delta t$ are volts. That is, show that $1 { \mathrm { T } } \cdot { \mathrm { m } } ^ { 2 } / { \mathrm { s } } = 1 { \mathrm { V } } .$ .   
8. Suppose a 50-turn coil lies in the plane of the page in a uniform magnetic field that is directed into the page. The coil originally has an area of $0 . 2 5 0 \mathrm { m } ^ { 2 }$ . It is stretched to have no area in $0 . 1 0 0 \mathsf s$ . What is the direction and magnitude of the induced emf if the uniform magnetic field has a strength of 1.50 T?   
9. (a) An MRI technician moves his hand from a region of very low magnetic field strength into an MRI scanner’s $2 . 0 0 \intercal$ field with his fingers pointing in the direction of the field. Find the average emf induced in his wedding ring, given its diameter is $2 . 2 0 \mathsf { c m }$ and assuming it takes 0.250 s to move it into the field. (b) Discuss whether this current would significantly change the temperature of the ring.   
10. Integrated Concepts Referring to the situation in the previous problem: (a) What current is induced in the ring if its resistance is $0 . 0 1 0 0 \Omega ?$ (b) What average power is dissipated? (c) What magnetic field is induced at the center of the ring? (d) What is the direction of the induced magnetic field relative to the MRI’s field?   
11. An emf is induced by rotating a 1000-turn, 20.0 cm diameter coil in the Earth’s $5 . 0 0 \times 1 0 ^ { - 5 }$ T magnetic field. What average emf is induced, given the plane of the coil is originally perpendicular to the Earth’s field and is rotated to be parallel to the field in $\mathsf { 1 0 . 0 ~ m s ? }$   
12. A 0.250 m radius, 500-turn coil is rotated onefourth of a revolution in 4.17 ms, originally having its plane perpendicular to a uniform magnetic field. (This is 60 rev/s.) Find the magnetic field strength needed to induce an average emf of 10,000 V.   
13. Integrated Concepts Approximately how does the emf induced in the loop in Figure 23.54(b) depend on the distance of the center of the loop from the wire?   
14. Integrated Concepts (a) A lightning bolt produces a rapidly varying magnetic field. If the bolt strikes the earth vertically and acts like a current in a long straight wire, it will induce a voltage in a loop aligned like that in Figure 23.54(b). What voltage is induced in a $. 1 . 0 0 \mathrm { m }$ diameter loop $5 0 . 0 \mathsf { m }$ from a $2 . 0 0 \times 1 0 ^ { 6 }$ lightning strike, if the current falls to zero in $2 5 . 0 \mu \mathrm { s } ?$ (b) Discuss circumstances under which such a voltage would produce noticeable consequences.



# 23.3 Motional Emf

15. Use Faraday’s law, Lenz’s law, and RHR-1 to show that the magnetic force on the current in the moving rod in Figure 23.10 is in the opposite direction of its velocity.   
16. If a current flows in the Satellite Tether shown in Figure 23.11, use Faraday’s law, Lenz’s law, and RHR-1 to show that there is a magnetic force on the tether in the direction opposite to its velocity.   
17. (a) A jet airplane with a $7 5 . 0 \mathrm { m }$ wingspan is flying at $2 8 0 ~ \mathrm { m / s }$ . What emf is induced between wing tips if the vertical component of the Earth’s field is $3 . 0 0 \times 1 0 ^ { - 5 }$ ? (b) Is an emf of this magnitude likely to have any consequences? Explain.   
18. (a) A nonferrous screwdriver is being used in a $2 . 0 0 \intercal$ magnetic field. What maximum emf can be induced along its $1 2 . 0 \mathsf { c m }$ length when it moves at $6 . 0 0 \mathsf { m } / \mathsf { s } ?$ (b) Is it likely that this emf will have any consequences or even be noticed?   
19. At what speed must the sliding rod in Figure 23.10 move to produce an emf of $\mathtt { 1 . 0 0 V }$ in a 1.50 T field, given the rod’s length is $3 0 . 0 \mathsf { c m ? }$   
20. The $1 2 . 0 \mathsf { c m }$ long rod in Figure 23.10 moves at $4 . 0 0 \ : \mathrm { m } / \mathsf { s }$ . What is the strength of the magnetic field if a $9 5 . 0 \vee$ emf is induced?   
21. Prove that when $B , \ell$ , and $v$ are not mutually perpendicular, motional emf is given by $\operatorname { e m f } = B \ell v$ sin $\theta$ . If $v$ is perpendicular to $B$ , then $\theta$ is the angle between $\ell$ and $B$ . If $\ell$ is perpendicular to $B$ , then $\theta$ is the angle between $v$ and $B$ .

22. In the August 1992 space shuttle flight, only 250 m of the conducting tether considered in Example 23.2 could be let out. A $4 0 . 0 \mathrm { V }$ motional emf was generated in the Earth’s $5 . 0 0 \times 1 0 ^ { - 5 }$ field, while moving at $7 . 8 0 \times 1 0 ^ { 3 } ~ \mathrm { m / s }$ . What was the angle between the shuttle’s velocity and the Earth’s field, assuming the conductor was perpendicular to the field?

23. Integrated Concepts Derive an expression for the current in a system like that in Figure 23.10, under the following conditions. The resistance between the rails is $R$ , the rails and the moving rod are identical in cross section $A$ and have the same resistivity $\rho$ . The distance between the rails is l, and the rod moves at constant speed $v$ perpendicular to the uniform field $B$ . At time zero, the moving rod is next to the resistance $R$ .

24. Integrated Concepts The Tethered Satellite in Figure 23.11 has a mass of $5 2 5 \mathsf { k g }$ and is at the end of a $2 0 . 0 { \mathsf { k m } }$ long, 2.50 mm diameter cable with the tensile strength of steel. (a) How much does the cable stretch if a $\textstyle 1 0 0 { \mathsf { N } }$ force is exerted to pull the satellite in? (Assume the satellite and shuttle are at the same altitude above the Earth.) (b) What is the effective force constant of the cable? (c) How much energy is stored in it when stretched by the $\textstyle 1 0 0 \mathsf { N }$ force?

25. Integrated Concepts The Tethered Satellite discussed in this module is producing $5 . 0 0 { \sf k V } ,$ , and a current of 10.0 A flows. (a) What magnetic drag force does this produce if the system is moving at $7 . 8 0 ~ \mathsf { k m } / \mathsf { s ? }$ (b) How much kinetic energy is removed from the system in 1.00 h, neglecting any change in altitude or velocity during that time? (c) What is the change in velocity if the mass of the system is ${ 1 0 0 , 0 0 0 \mathsf { k g } \colon }$ (d) Discuss the long term consequences (say, a weeklong mission) on the space shuttle’s orbit, noting what effect a decrease in velocity has and assessing the magnitude of the effect.

# 23.4 Eddy Currents and Magnetic Damping

26. Make a drawing similar to Figure 23.13, but with the pendulum moving in the opposite direction. Then use Faraday’s law, Lenz’s law, and RHR-1 to show that magnetic force opposes motion.

27.

A coil is moved through a magnetic field as shown in Figure 23.56. The field is uniform inside the rectangle and zero outside. What is the direction of the induced current and what is the direction of the magnetic force on the coil at each position shown?

# 23.5 Electric Generators

28. Calculate the peak voltage of a generator that rotates its 200-turn, $0 . 1 0 0 \mathrm { m }$ diameter coil at 3600 rpm in a 0.800 T field.   
29. At what angular velocity in rpm will the peak voltage of a generator be $4 8 0 \vee ,$ if its 500-turn, $8 . 0 0 \mathsf { c m }$ diameter coil rotates in a $0 . 2 5 0 \intercal$ field?   
30. What is the peak emf generated by rotating a 1000-turn, 20.0 cm diameter coil in the Earth’s $5 . 0 0 \times 1 0 ^ { - 5 }$ magnetic field, given the plane of the coil is originally perpendicular to the Earth’s field and is rotated to be parallel to the field in $\textstyle 1 0 . 0 \operatorname { m s ? }$   
31. What is the peak emf generated by a $0 . 2 5 0 \mathrm { m }$ radius, 500-turn coil is rotated one-fourth of a revolution in $4 . 1 7 \mathrm { m s }$ , originally having its plane perpendicular to a uniform magnetic field. (This is 60 rev/s.)   
32. (a) A bicycle generator rotates at 1875 rad/s, producing an $\boldsymbol { 1 8 . 0 \vee }$ peak emf. It has a 1.00 by $3 . 0 0 \mathsf { c m }$ rectangular coil in a 0.640 T field. How many turns are in the coil? (b) Is this number of turns of wire practical for a 1.00 by 3.00 cm coil?

33. Integrated Concepts This problem refers to the bicycle generator considered in the previous problem. It is driven by a $1 . 6 0 \mathsf { c m }$ diameter wheel that rolls on the outside rim of the bicycle tire. (a) What is the velocity of the bicycle if the generator’s angular velocity is $1 8 7 5 ~ \mathrm { r a d } / \mathsf { s } ?$ (b) What is the maximum emf of the generator when the bicycle moves at $1 0 . 0 ~ \mathsf { m } / \mathsf { s }$ , noting that it was $\boldsymbol { 1 8 . 0 \vee }$ under the original conditions? (c) If the sophisticated generator can vary its own magnetic field, what field strength will it need at $5 . 0 0 \mathrm { m } / \mathrm { s }$ to produce a $9 . 0 0 \mathrm { V }$ maximum emf?

34. (a) A car generator turns at 400 rpm when the engine is idling. Its 300-turn, 5.00 by $8 . 0 0 \mathsf { c m }$ rectangular coil rotates in an adjustable magnetic field so that it can produce sufficient voltage even at low rpms. What is the field strength needed to produce a $2 4 . 0 \ : \vee$ peak emf? (b) Discuss how this required field strength compares to those available in permanent and electromagnets.

35. Show that if a coil rotates at an angular velocity $\omega$ , the period of its AC output is $2 \pi / \omega$ .

36. A 75-turn, $1 0 . 0 \mathsf { c m }$ diameter coil rotates at an angular velocity of $8 . 0 0 ~ \mathrm { r a d / s }$ in a $\boldsymbol { \mathsf { 1 . 2 5 7 } }$ field, starting with the plane of the coil parallel to the field. (a) What is the peak emf? (b) At what time is the peak emf first reached? (c) At what time is the emf first at its most negative? (d) What is the period of the AC voltage output?

37. (a) If the emf of a coil rotating in a magnetic field is zero at $t = 0$ , and increases to its first peak at $t = 0 . 1 0 0 \mathrm { m s }$ , what is the angular velocity of the coil? (b) At what time will its next maximum occur? (c) What is the period of the output? (d) When is the output first one-fourth of its maximum? (e) When is it next one-fourth of its maximum?

38. Unreasonable Results A 500-turn coil with a $\phantom { - } 1 0 . 2 5 0 \mathrm { m } ^ { 2 }$ area is spun in the Earth’s $5 . 0 0 \times 1 0 ^ { - 5 }$ field, producing a 12.0 kV maximum emf. (a) At what angular velocity must the coil be spun? (b) What is unreasonable about this result? (c) Which assumption or premise is responsible?

# 23.6 Back Emf

39. Suppose a motor connected to a $\boldsymbol { \mathsf { 1 2 0 } } \boldsymbol { \mathsf { V } }$ source draws 10.0 A when it first starts. (a) What is its resistance? (b) What current does it draw at its normal operating speed when it develops a 100 V back emf?   
40. A motor operating on 240 V electricity has a 180 V back emf at operating speed and draws a 12.0 A current. (a) What is its resistance? (b) What current does it draw when it is first started?   
41. What is the back emf of a $\textstyle 1 2 0 \vee$ motor that draws 8.00 A at its normal speed and 20.0 A when first starting?   
42. The motor in a toy car operates on $6 . 0 0 \mathsf { V } _ { ; }$ , developing a 4.50 V back emf at normal speed. If it draws 3.00 A at normal speed, what current does it draw when starting?

43. Integrated Concepts

The motor in a toy car is powered by four batteries in series, which produce a total emf of 6.00 V. The motor draws 3.00 A and develops a $4 . 5 0 \mathrm { V }$ back emf at normal speed. Each battery has a $0 . 1 0 0 \Omega$ internal resistance. What is the resistance of the motor?

# 23.7 Transformers

44. A plug-in transformer, like that in Figure 23.25, supplies $9 . 0 0 \mathrm { \ : V }$ to a video game system. (a) How many turns are in its secondary coil, if its input voltage is $\boldsymbol { \mathsf { 1 2 0 } } \boldsymbol { \mathsf { V } }$ and the primary coil has 400 turns? (b) What is its input current when its output is 1.30 A?

45. An American traveler in New Zealand carries a transformer to convert New Zealand’s standard $2 4 0 \vee$ to $\textstyle 1 2 0 \vee$ so that she can use some small appliances on her trip. (a) What is the ratio of turns in the primary and secondary coils of her transformer? (b) What is the ratio of input to output current? (c) How could a New Zealander traveling in the United States use this same transformer to power her $2 4 0 \vee$ appliances from 120 V?

46. A cassette recorder uses a plug-in transformer to convert $\boldsymbol { \mathsf { 1 2 0 \vee } }$ to $\Omega . 0 \vee _ { \ O _ { 3 } }$ , with a maximum current output of $2 0 0 ~ \mathsf { m A }$ . (a) What is the current input? (b) What is the power input? (c) Is this amount of power reasonable for a small appliance?

47. (a) What is the voltage output of a transformer used for rechargeable flashlight batteries, if its primary has 500 turns, its secondary 4 turns, and the input voltage is 120 V? (b) What input current is required to produce a 4.00 A output? (c) What is the power input?

48. (a) The plug-in transformer for a laptop computer puts out $7 . 5 0 \mathrm { V }$ and can supply a maximum current of 2.00 A. What is the maximum input current if the input voltage is 240 V? Assume $100 \%$ efficiency. (b) If the actual efficiency is less than $100 \%$ , would the input current need to be greater or smaller? Explain.

49. A multipurpose transformer has a secondary coil with several points at which a voltage can be extracted, giving outputs of 5.60, 12.0, and $4 8 0 \vee .$ (a) The input voltage is $2 4 0 \vee$ to a primary coil of 280 turns. What are the numbers of turns in the parts of the secondary used to produce the output voltages? (b) If the maximum input current is 5.00 A, what are the maximum output currents (each used alone)?

50. A large power plant generates electricity at 12.0 kV. Its old transformer once converted the voltage to $3 3 5 { \mathsf { k V } } .$ . The secondary of this transformer is being replaced so that its output can be $7 5 0 \mathsf { k V }$ for more efficient cross-country transmission on upgraded transmission lines. (a) What is the ratio of turns in the new secondary compared with the old secondary? (b) What is the ratio of new current output to old output (at $3 3 5 \mathsf { k V } )$ ) for the same power? (c) If the upgraded transmission lines have the same resistance, what is the ratio of new line power loss to old?

51. If the power output in the previous problem is 1000 MW and line resistance is $2 . 0 0 \Omega$ , what were the old and new line losses?

52. Unreasonable Results The $3 3 5 \mathsf { k V }$ AC electricity from a power transmission line is fed into the primary coil of a transformer. The ratio of the number of turns in the secondary to the number in the primary is $N _ { \mathrm { s } } / N _ { \mathrm { p } } = 1 0 0 0$ . (a) What voltage is induced in the secondary? (b) What is unreasonable about this result? (c) Which assumption or premise is responsible?

53. Construct Your Own Problem Consider a double transformer to be used to create very large voltages. The device consists of two stages. The first is a transformer that produces a much larger output voltage than its input. The output of the first transformer is used as input to a second transformer that further increases the voltage. Construct a problem in which you calculate the output voltage of the final stage based on the input voltage of the first stage and the number of turns or loops in both parts of both transformers (four coils in all). Also calculate the maximum output current of the final stage based on the input current. Discuss the possibility of power losses in the devices and the effect on the output current and power.

# 23.8 Electrical Safety: Systems and Devices

# 54. Integrated Concepts

A short circuit to the grounded metal case of an appliance occurs as shown in Figure 23.57. The person touching the case is wet and only has a $3 . 0 0 \mathrm { k } \Omega$ resistance to earth/ground. (a) What is the voltage on the case if $5 . 0 0 \mathsf { m A }$ flows through the person? (b) What is the current in the short circuit if the resistance of the earth/ground wire is $0 . 2 0 0 \Omega ?$ (c) Will this trigger the 20.0 A circuit breaker supplying the appliance?

# 23.9 Inductance

55. Two coils are placed close together in a physics lab to demonstrate Faraday’s law of induction. A current of 5.00 A in one is switched off in $1 . 0 0 \mathsf { m s } _ { \cdot }$ , inducing a $9 . 0 0 \mathrm { \ : V }$ emf in the other. What is their mutual inductance?

56. If two coils placed next to one another have a mutual inductance of $5 . 0 0 ~ \mathrm { m H }$ , what voltage is induced in one when the 2.00 A current in the other is switched off in $3 0 . 0 ~ \mathsf { m s ? }$

57. The 4.00 A current through a $7 . 5 0 \ : \mathrm { m H }$ inductor is switched off in $8 . 3 3 ~ \mathrm { m s }$ . What is the emf induced opposing this?

58. A device is turned on and 3.00 A flows through it 0.100 ms later. What is the self-inductance of the device if an induced 150 V emf opposes this?

59. Starting with , show that the units of inductance are $( \mathrm { V \cdot s ) / A = \Omega \cdot s . }$ .

60. Camera flashes charge a capacitor to high voltage by switching the current through an inductor on and off rapidly. In what time must the 0.100 A current through a $2 . 0 0 \mathsf { m } \mathsf { H }$ inductor be switched on or off to induce a $5 0 0 \vee$ emf?

61. A large research solenoid has a self-inductance of 25.0 H. (a) What induced emf opposes shutting it off when 100 A of current through it is switched off in $8 0 . 0 \ \mathsf { m s ? }$ (b) How much energy is stored in the inductor at full current? (c) At what rate in watts must energy be dissipated to switch the current off in $8 0 . 0 \mathsf { m s ? }$ (d) In view of the answer to the last part, is it surprising that shutting it down this quickly is difficult?

62. (a) Calculate the self-inductance of a 50.0 cm long, $1 0 . 0 \mathsf { c m }$ diameter solenoid having 1000 loops. (b) How much energy is stored in this inductor when 20.0 A of current flows through it? (c) How fast can it be turned off if the induced emf cannot exceed 3.00 V?

63. A precision laboratory resistor is made of a coil of wire $\mathtt { 1 . 5 0 \mathtt { c m } }$ in diameter and $4 . 0 0 \mathsf { c m }$ long, and it has 500 turns. (a) What is its self-inductance? (b) What average emf is induced if the 12.0 A current through it is turned on in 5.00 ms (one-fourth of a cycle for $5 0 \mathsf { H z } \mathsf { A C } ) \hat { \colon }$ (c) What is its inductance if it is shortened to half its length and counter-wound (two layers of 250 turns in opposite directions)?

64. The heating coils in a hair dryer are $0 . 8 0 0 { \mathsf { c m } }$ in diameter, have a combined length of $1 . 0 0 \mathrm { m }$ , and a total of 400 turns. (a) What is their total selfinductance assuming they act like a single solenoid? (b) How much energy is stored in them when 6.00 A flows? (c) What average emf opposes shutting them off if this is done in $5 . 0 0 ~ \mathsf { m s }$ (onefourth of a cycle for 50 Hz AC)?

65. When the 20.0 A current through an inductor is turned off in $\mathsf { 1 . 5 0 } \mathsf { m s }$ , an $8 0 0 \vee$ emf is induced, opposing the change. What is the value of the selfinductance?

66. How fast can the 150 A current through a 0.250 H inductor be shut off if the induced emf cannot exceed 75.0 V?

67. Integrated Concepts

A very large, superconducting solenoid such as one used in MRI scans, stores 1.00 MJ of energy in its magnetic field when 100 A flows. (a) Find its self-inductance. (b) If the coils “go normal,” they gain resistance and start to dissipate thermal energy. What temperature increase is produced if all the stored energy goes into heating the 1000 kg magnet, given its average specific heat is $2 0 0 { \mathrm { J / k g } } { \cdot } { ^ { \circ } } { \mathrm { C } } ?$

68. Unreasonable Results A $2 5 . 0 \mathsf { H }$ inductor has 100 A of current turned off in $1 . 0 0 \mathrm { m s }$ . (a) What voltage is induced to oppose this? (b) What is unreasonable about this result? (c) Which assumption or premise is responsible?

# 23.10 RL Circuits

69. If you want a characteristic RLtime constant of $\mathsf { 1 . 0 0 s }$ , and you have a $5 0 0 \Omega$ resistor, what value of self-inductance is needed?   
70. Your RLcircuit has a characteristic time constant of 20.0 ns, and a resistance of $5 . 0 0 \mathrm { M } \Omega$ . (a) What is the inductance of the circuit? (b) What resistance would give you a 1.00 ns time constant, perhaps needed for quick response in an oscilloscope?   
71. A large superconducting magnet, used for magnetic resonance imaging, has a $5 0 . 0 \mathsf { H }$ inductance. If you want current through it to be adjustable with a 1.00 s characteristic time constant, what is the minimum resistance of system?   
72. Verify that after a time of $1 0 . 0 \mathsf { m s }$ , the current for the situation considered in Example 23.9 will be 0.183 A as stated.   
73. Suppose you have a supply of inductors ranging from $ { \mathsf { 1 . 0 0 } }  { \mathsf { n H } }$ to ${ \mathsf { 1 0 . 0 \mathsf { H } } }$ , and resistors ranging from $0 . 1 0 0 \Omega$ to $1 . 0 0 \mathbf { M } \Omega$ . What is the range of characteristic $R L$ time constants you can produce by connecting a single resistor to a single inductor?   
74. (a) What is the characteristic time constant of a $2 5 . 0 \mathsf { m H }$ inductor that has a resistance of $4 . 0 0 \Omega ?$ (b) If it is connected to a $\boldsymbol { \mathsf { 1 2 . 0 V } }$ battery, what is the current after $1 2 . 5 \mathsf { m s ? }$   
75. What percentage of the final current $I _ { 0 }$ flows through an inductor $L$ in series with a resistor $R$ , three time constants after the circuit is completed?   
76. The 5.00 A current through a $\pm 1 . 5 0 \mathsf { H }$ inductor is dissipated by a $2 . 0 0 \Omega$ resistor in a circuit like that in Figure 23.42 with the switch in position 2. (a) What is the initial energy in the inductor? (b) How long will it take the current to decline to $5 . 0 0 \%$ of its initial value? (c) Calculate the average power dissipated, and compare it with the initial power dissipated by the resistor.   
77. (a) Use the exact exponential treatment to find how much time is required to bring the current through an $8 0 . 0 \mathsf { m H }$ inductor in series with a $1 5 . 0 \Omega$ resistor to $9 9 . 0 \%$ of its final value, starting from zero. (b) Compare your answer to the approximate treatment using integral numbers of . (c) Discuss how significant the difference is.   
78. (a) Using the exact exponential treatment, find the time required for the current through a $2 . 0 0 \mathsf { H }$ inductor in series with a $0 . 5 0 0 \Omega$ resistor to be reduced to $0 . 1 0 0 \%$ of its original value. (b) Compare your answer to the approximate treatment using integral numbers of $\tau$ . (c) Discuss how significant the difference is.



# 23.11 Reactance, Inductive and Capacitive

79. At what frequency will a $3 0 . 0 \mathsf { m } \mathsf { H }$ inductor have a reactance of $1 0 0 \Omega ?$   
80. What value of inductance should be used if a $2 0 . 0 \mathrm { k } \Omega$ reactance is needed at a frequency of $5 0 0 ~ { \mathsf { H z ? } }$   
81. What capacitance should be used to produce a $2 . 0 0 \mathbf { M } \Omega$ reactance at $6 0 . 0 \mathsf { H z ? }$   
82. At what frequency will an $8 0 . 0 ~ \mathsf { m } \mathsf { F }$ capacitor have a reactance of $0 . 2 5 0 \Omega ?$   
83. (a) Find the current through a 0.500 H inductor connected to a $6 0 . 0 { \mathsf { H z } }$ , 480 V AC source. (b) What would the current be at $\scriptstyle 1 0 0 \models 1 \neq ?$   
84. (a) What current flows when a $6 0 . 0 { \mathsf { H z } }$ , 480 V AC source is connected to a $0 . 2 5 0 \mu \mathrm { F }$ capacitor? (b) What would the current be at $2 5 . 0 \mathsf { k H z ? }$   
85. A $2 0 . 0 \mathsf { k H z }$ , 16.0 V source connected to an inductor produces a 2.00 A current. What is the inductance?   
86. A $2 0 . 0 { \mathsf { H } } z$ , $\boldsymbol { 1 6 . 0 \ V }$ source produces a $2 . 0 0 \mathsf { m A }$ current when connected to a capacitor. What is the capacitance?   
87. (a) An inductor designed to filter high-frequency noise from power supplied to a personal computer is placed in series with the computer. What minimum inductance should it have to produce a $2 . 0 0 \mathrm { k } \Omega$ reactance for $1 5 . 0 \mathsf { k H z }$ noise? (b) What is its reactance at $6 0 . 0 \mathsf { H z ? }$   
88. The capacitor in Figure 23.52(a) is designed to filter low-frequency signals, impeding their transmission between circuits. (a) What capacitance is needed to produce a $1 0 0 \mathrm { k } \Omega$ reactance at a frequency of $\textstyle { 1 2 0 } \ H z ?$ (b) What

would its reactance be at $\pm . 0 0 \mathsf { M H z ? }$ (c) Discuss the implications of your answers to (a) and (b).

89. The capacitor in Figure 23.52(b) will filter highfrequency signals by shorting them to earth/ ground. (a) What capacitance is needed to produce a reactance of $1 0 . 0 \mathrm { m } \Omega$ for a $5 . 0 0 ~ { \mathsf { k H z } }$ signal? (b) What would its reactance be at 3.00 $H Z ?$ (c) Discuss the implications of your answers to (a) and (b).

90. Unreasonable Results In a recording of voltages due to brain activity (an EEG), a $1 0 . 0 \mathsf { m V }$ signal with a $0 . 5 0 0 { \sf H z }$ frequency is applied to a capacitor, producing a current of $\mathsf { 1 0 0 } \mathsf { m } \mathsf { A }$ . Resistance is negligible. (a) What is the capacitance? (b) What is unreasonable about this result? (c) Which assumption or premise is responsible?

91. Construct Your Own Problem Consider the use of an inductor in series with a computer operating on $6 0 \mathsf { H z }$ electricity. Construct a problem in which you calculate the relative reduction in voltage of incoming high frequency noise compared to $6 0 \mathsf { H z }$ voltage. Among the things to consider are the acceptable series reactance of the inductor for $6 0 \mathsf { H z }$ power and the likely frequencies of noise coming through the power lines.

# 23.12 RLC Series AC Circuits

92. An $R L$ circuit consists of a $4 0 . 0 \Omega$ resistor and a $3 . 0 0 \mathsf { m } \mathsf { H }$ inductor. (a) Find its impedance $Z$ at $6 0 . 0 { \scriptstyle { \mathsf { H z } } }$ and $1 0 . 0 \mathsf { k H z }$ . (b) Compare these values of $Z$ with those found in Example 23.12 in which there was also a capacitor.   
93. An RCcircuit consists of a $4 0 . 0 \Omega$ resistor and a $5 . 0 0 \mu \mathrm { F }$ capacitor. (a) Find its impedance at 60.0 $H z$ and $1 0 . 0 \mathsf { k H z }$ . (b) Compare these values of $Z$ with those found in Example 23.12, in which there was also an inductor.   
94. An LCcircuit consists of a $3 . 0 0 \mathrm { m H }$ inductor and a $5 . 0 0 \mu F$ capacitor. (a) Find its impedance at 60.0 Hz and $1 0 . 0 \mathsf { k H z }$ . (b) Compare these values of $Z$ with those found in Example 23.12 in which there was also a resistor.   
95. What is the resonant frequency of a $0 . 5 0 0 ~ \mathrm { m H }$ inductor connected to a $4 0 . 0 \mu \mathrm { F }$ capacitor?   
96. To receive AM radio, you want an RLCcircuit that can be made to resonate at any frequency between 500 and $1 6 5 0 ~ \mathsf { k H z }$ . This is accomplished with a fixed $1 . 0 0 \mu \mathrm { H }$ inductor connected to a variable capacitor. What range of capacitance is needed?

97. Suppose you have a supply of inductors ranging from $1 . 0 0 \mathsf { n H }$ to ${ \mathsf { 1 0 . 0 \mathsf { H } } }$ , and capacitors ranging from 1.00 pF to 0.100 F. What is the range of resonant frequencies that can be achieved from combinations of a single inductor and a single capacitor?

98. What capacitance do you need to produce a resonant frequency of $1 . 0 0 \mathsf { G H z }$ , when using an $8 . 0 0 \mathsf { n H }$ inductor?   
99. What inductance do you need to produce a resonant frequency of $6 0 . 0 { \mathsf { H z } }$ , when using a $2 . 0 0 \mu \mathrm { F }$ capacitor?   
100. The lowest frequency in the FM radio band is $8 8 . 0 \mathsf { M H z }$ . (a) What inductance is needed to produce this resonant frequency if it is connected to a 2.50 pF capacitor? (b) The capacitor is variable, to allow the resonant frequency to be adjusted to as high as $1 0 8 M H z$ . What must the capacitance be at this frequency?   
101. An RLCseries circuit has a $2 . 5 0 \Omega$ resistor, a $1 0 0 \mu \mathrm { H }$ inductor, and an $8 0 . 0 \mu \mathrm { F }$ capacitor.(a) Find the circuit’s impedance at ${ \mathsf { 1 2 0 } } { \mathsf { H z } }$ . (b) Find the circuit’s impedance at $5 . 0 0 ~ { \sf k H z }$ . (c) If the voltage source has $V _ { \mathrm { r m s } } = 5 . 6 0 \ : \mathrm { V }$ , what is $I _ { \mathrm { r m s } }$ at each frequency? (d) What is the resonant frequency of the circuit? (e) What is $I _ { \mathrm { r m s } }$ at resonance?   
102. An RLCseries circuit has a $1 . 0 0 \mathrm { k } \Omega$ resistor, a $1 5 0 \mu \mathrm { H }$ inductor, and a 25.0 nF capacitor. (a) Find the circuit’s impedance at $5 0 0 ~ { \mathsf { H z } }$ . (b) Find the circuit’s impedance at $7 . 5 0 \mathsf { k H z }$ . (c) If the voltage source has $V _ { \mathrm { r m s } } = 4 0 8 \mathrm { V }$ , what is $I _ { \mathrm { r m s } }$ at each frequency? (d) What is the resonant frequency of the circuit? (e) What is $I _ { \mathrm { r m s } }$ at resonance?   
103. An RLCseries circuit has a $2 . 5 0 \Omega$ resistor, a $1 0 0 \mu \mathrm { H }$ inductor, and an $8 0 . 0 \mu \mathrm { F }$ capacitor. (a) Find the power factor at $f = 1 2 0 \mathrm { H z }$ . (b) What is the phase angle at $\textstyle { 1 2 0 } \ H z ?$ (c) What is the average power at $\textstyle { 1 2 0 } \ H z ?$ (d) Find the average power at the circuit’s resonant frequency.   
104. An RLCseries circuit has a $1 . 0 0 \mathrm { k } \Omega$ resistor, a $1 5 0 \mu \mathrm { H }$ inductor, and a 25.0 nF capacitor. (a) Find the power factor at $f = 7 . 5 0 \ : \mathrm { H z }$ . (b) What is the phase angle at this frequency? (c) What is the average power at this frequency? (d) Find the average power at the circuit’s resonant frequency.   
105. An $_ { R L C }$ series circuit has a $2 0 0 \Omega$ resistor and a $2 5 . 0 \mathsf { m H }$ inductor. At $8 0 0 0 { \mathsf { H z } }$ , the phase angle is $4 5 . 0 ^ { \circ }$ . (a) What is the impedance? (b) Find the circuit’s capacitance. (c) If $V _ { \mathrm { r m s } } = 4 0 8 \mathrm { V }$ is applied, what is the average power supplied?

106. Referring to Example 23.14, find the average power at $1 0 . 0 \mathsf { k H z }$ .

07. Critical Thinking A length of $4 . 0 0 0 \mathrm { m }$ of wire is to be used to detect a magnetic field. The wire is made into a single square loop and rotated at a rate of 400 cycles per second. (a) If the magnetic field is 0.02000 T, what is the magnitude of the average emf that can be generated in the first quarter cycle, provided the loop is initially oriented in a plane perpendicular to the magnetic field? (b) Is there a difference in the magnitude of the average emf generated if the wire is made into two square loops and rotated at the same rate, starting with the same orientation of the loops as that of the loop in part a? If so, what is the average emf possible for the first quarter cycle for two loops being rotated at 400 cycles per second in the magnetic field? (c) If the wire is made into a figure eight, what is the average emf for the first quarter cycle that can be generated by rotating it at 400 cycles per second in the magnetic field, again starting with the same orientation of the oops with respect to the magnetic field? The wire crosses itself in this arrangement. (d) Does the shape of the loop matter?