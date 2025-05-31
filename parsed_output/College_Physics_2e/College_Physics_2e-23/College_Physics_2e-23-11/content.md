# 23.11 Reactance, Inductive and Capacitive

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

• Sketch voltage and current versus time in simple inductive, capacitive, and resistive circuits.   
• Calculate inductive and capacitive reactance.   
• Calculate current and/or voltage in simple inductive, capacitive, and resistive circuits.

Many circuits also contain capacitors and inductors, in addition to resistors and an AC voltage source. We have seen how capacitors and inductors respond to DC voltage when it is switched on and off. We will now explore how inductors and capacitors react to sinusoidal AC voltage.

# Inductors and Inductive Reactance

Suppose an inductor is connected directly to an AC voltage source, as shown in Figure 23.43. It is reasonable to assume negligible resistance, since in practice we can make the resistance of an inductor so small that it has a negligible effect on the circuit. Also shown is a graph of voltage and current as functions of time.

The graph in Figure 23.43(b) starts with voltage at a maximum. Note that the current starts at zero and rises to its peak afterthe voltage that drives it, just as was the case when DC voltage was switched on in the preceding section. When the voltage becomes negative at point a, the current begins to decrease; it becomes zero at point b, where voltage is its most negative. The current then becomes negative, again following the voltage. The voltage becomes positive at point c and begins to make the current less negative. At point d, the current goes through zero just as the voltage reaches its positive peak to start another cycle. This behavior is summarized as follows:

# AC Voltage in an Inductor

When a sinusoidal voltage is applied to an inductor, the voltage leads the current by one-fourth of a cycle, or by a $9 0 ^ { \circ }$ phase angle.

Current lags behind voltage, since inductors oppose change in current. Changing current induces a back emf $V = - L ( \Delta I / \Delta t )$ . This is considered to be an effective resistance of the inductor to AC. The rms current $I$ through

an inductor $L$ is given by a version of Ohm’s law:

$$
I = { \frac { V } { X _ { L } } } ,
$$

where $V$ is the rms voltage across the inductor and $X _ { L }$ is defined to be

$$
X _ { L } = 2 \pi f L ,
$$

with $f$ the frequency of the AC voltage source in hertz (An analysis of the circuit using Kirchhoff’s loop rule and calculus actually produces this expression). $X _ { L }$ is called the inductive reactance, because the inductor reacts to impede the current. $X _ { L }$ has units of ohms $\mathrm { : 1 H } = 1 \boldsymbol { \Omega } \cdot \mathbf { s } ,$ , so that frequency times inductance has units of (cycles/s) $( { \boldsymbol { \Omega } } \cdot { \mathrm { s } } ) = { \boldsymbol { \Omega } } )$ , consistent with its role as an effective resistance. It makes sense that $X _ { L }$ is proportional to $L$ , since the greater the induction the greater its resistance to change. It is also reasonable that $X _ { L }$ is proportional to frequency $f$ , since greater frequency means greater change in current. That is, $\Delta I / \Delta t$ is large for large frequencies (large $f$ ,small $\Delta t _ { \cdot }$ ). The greater the change, the greater the opposition of an inductor.

# EXAMPLE 23.10

# Calculating Inductive Reactance and then Current

(a) Calculate the inductive reactance of a $3 . 0 0 \mathsf { m } \mathsf { H }$ inductor when $6 0 . 0 { \mathsf { H z } }$ and $1 0 . 0 \mathsf { k H z }$ AC voltages are applied. (b) What is the rms current at each frequency if the applied rms voltage is 120 V?

# Strategy

The inductive reactance is found directly from the expression $X _ { L } = 2 \pi f L$ . Once $X _ { L }$ has been found at each frequency, Ohm’s law as stated in the Equation $I = V / X _ { L }$ can be used to find the current at each frequency.

# Solution for (a)

Entering the frequency and inductance into Equation $X _ { L } = 2 \pi f L$ gives

$$
X _ { L } = 2 \pi f L = 6 . 2 8 ( 6 0 . 0 / \mathrm { s } ) ( 3 . 0 0 \mathrm { m H } ) = 1 . 1 3 \Omega \mathrm { a t } 6 0 \mathrm { H z } . 
$$

Similarly, at $1 0 ~ \mathsf { k H z }$ ,

$$
X _ { L } = 2 \pi f L = 6 . 2 8 ( 1 . 0 0 \times 1 0 ^ { 4 } / \mathrm { s } ) ( 3 . 0 0 \mathrm { m H } ) = 1 8 8 \Omega \mathrm { a t } 1 0 \mathrm { k H z } .
$$

# Solution for (b)

The rms current is now found using the version of Ohm’s law in Equation $I = V / X _ { L }$ , given the applied rms voltage is $\textstyle 1 2 0 \vee .$ . For the first frequency, this yields

$$
I = { \frac { V } { X _ { L } } } = { \frac { 1 2 0 { \mathrm { ~ V } } } { 1 . 1 3 \Omega } } = 1 0 6 { \mathrm { ~ A ~ a t ~ } } 6 0 { \mathrm { ~ H z } } .
$$

Similarly, at $1 0 ~ \mathsf { k H z }$ ,

$$
I = { \frac { V } { X _ { L } } } = { \frac { 1 2 0 { \mathrm { ~ V } } } { 1 8 8 \Omega } } = 0 . 6 3 7 { \mathrm { ~ A ~ a t ~ } } 1 0 { \mathrm { ~ k H z } } .
$$

# Discussion

The inductor reacts very differently at the two different frequencies. At the higher frequency, its reactance is large and the current is small, consistent with how an inductor impedes rapid change. Thus high frequencies are impeded the most. Inductors can be used to filter out high frequencies; for example, a large inductor can be put in series with a sound reproduction system or in series with your home computer to reduce high-frequency sound output from your speakers or high-frequency power spikes into your computer.

Note that although the resistance in the circuit considered is negligible, the AC current is not extremely large because inductive reactance impedes its flow. With AC, there is no time for the current to become extremely large.

# Capacitors and Capacitive Reactance

Consider the capacitor connected directly to an AC voltage source as shown in Figure 23.44. The resistance of a circuit like this can be made so small that it has a negligible effect compared with the capacitor, and so we can assume negligible resistance. Voltage across the capacitor and current are graphed as functions of time in the figure.

The graph in Figure 23.44 starts with voltage across the capacitor at a maximum. The current is zero at this point, because the capacitor is fully charged and halts the flow. Then voltage drops and the current becomes negative as the capacitor discharges. At point a, the capacitor has fully discharged $( Q = 0$ on it) and the voltage across it is zero. The current remains negative between points a and b, causing the voltage on the capacitor to reverse. This is complete at point b, where the current is zero and the voltage has its most negative value. The current becomes positive after point b, neutralizing the charge on the capacitor and bringing the voltage to zero at point c, which allows the current to reach its maximum. Between points c and d, the current drops to zero as the voltage rises to its peak, and the process starts to repeat. Throughout the cycle, the voltage follows what the current is doing by onefourth of a cycle:

# AC Voltage in a Capacitor

When a sinusoidal voltage is applied to a capacitor, the voltage follows the current by one-fourth of a cycle, or by a $9 0 ^ { \circ }$ phase angle.

The capacitor is affecting the current, having the ability to stop it altogether when fully charged. Since an AC voltage is applied, there is an rms current, but it is limited by the capacitor. This is considered to be an effective resistance of the capacitor to AC, and so the rms current $I$ in the circuit containing only a capacitor $C$ is given by another version of Ohm’s law to be

$$
I = { \frac { V } { X _ { C } } } ,
$$

where $V$ is the rms voltage and $X _ { C }$ is defined (As with $X _ { L }$ , this expression for $X _ { C }$ results from an analysis of the circuit using Kirchhoff’s rules and calculus) to be

$$
X _ { C } = { \frac { 1 } { 2 \pi f C } } ,
$$

where $X _ { C }$ is called the capacitive reactance, because the capacitor reacts to impede the current. $X _ { C }$ has units of ohms (verification left as an exercise for the reader). $X _ { C }$ is inversely proportional to the capacitance $C$ ; the larger the capacitor, the greater the charge it can store and the greater the current that can flow. It is also inversely proportional to the frequency $f$ ; the greater the frequency, the less time there is to fully charge the capacitor, and so it impedes current less.

# EXAMPLE 23.11

# Calculating Capacitive Reactance and then Current

(a) Calculate the capacitive reactance of a $5 . 0 0 \mu \mathsf { F }$ capacitor when $6 0 . 0 { \mathsf { H z } }$ and 10.0 kHz AC voltages are applied. (b) What is the rms current if the applied rms voltage is 120 V?

# Strategy

The capacitive reactance is found directly from the expression in $\begin{array} { r } { X _ { C } = \frac { 1 } { 2 \pi f C } } \end{array}$ . Once $X _ { C }$ has been found at each frequency, Ohm’s law stated as $I = V / X _ { C }$ can be used to find the current at each frequency.

# Solution for (a)

Entering the frequency and capacitance into $\begin{array} { r } { X _ { C } = \frac { 1 } { 2 \pi f C } } \end{array}$ gives

$$
\begin{array} { l l l } { { X _ { C } } } & { { = } } & { { { \frac { 1 } { 2 \pi f C } } } } \\ { { } } & { { = } } & { { { \frac { 1 } { 6 . 2 8 ( 6 0 . 0 / \mathrm { s } ) ( 5 . 0 0 \mu \mathrm { F } ) } } = 5 3 1 \Omega \mathrm { a t } 6 0 \mathrm { H z } . } } \end{array}
$$

Similarly, at $1 0 ~ \mathsf { k H z }$ ,

$$
\begin{array} { r c l } { { X _ { C } } } & { { = } } & { { { \frac { 1 } { 2 \pi f C } } = { \frac { 1 } { 6 . 2 8 ( 1 . 0 0 \times 1 0 ^ { 4 } / \mathrm { s } ) ( 5 . 0 0 ~ \mu \mathrm { F } ) } } } } \\ { { } } & { { = } } & { { 3 . 1 8 \ \Omega \ \mathrm { a t \ 1 0 \ k H z } } } \end{array} .
$$

# Solution for (b)

The rms current is now found using the version of Ohm’s law in $I = V / X _ { C }$ , given the applied rms voltage is $\displaystyle { 1 2 0 \vee . }$ For the first frequency, this yields

$$
I = { \frac { V } { X _ { C } } } = { \frac { 1 2 0 { \mathrm { V } } } { 5 3 1 \Omega } } = 0 . 2 2 6 { \mathrm { A a t } } 6 0 { \mathrm { H z } } .
$$

Similarly, at $1 0 ~ \mathsf { k H z }$ ,

$$
I = { \frac { V } { X _ { C } } } = { \frac { 1 2 0 { \mathrm { V } } } { 3 . 1 8 \Omega } } = 3 7 . 7 { \mathrm { A a t ~ l 0 ~ k H z } } .
$$

# Discussion

The capacitor reacts very differently at the two different frequencies, and in exactly the opposite way an inductor reacts. At the higher frequency, its reactance is small and the current is large. Capacitors favor change, whereas inductors oppose change. Capacitors impede low frequencies the most, since low frequency allows them time to become charged and stop the current. Capacitors can be used to filter out low frequencies. For example, a capacitor in series with a sound reproduction system rids it of the $6 0 \mathsf { H z }$ hum.

Although a capacitor is basically an open circuit, there is an rms current in a circuit with an AC voltage applied to a capacitor. This is because the voltage is continually reversing, charging and discharging the capacitor. If the frequency goes to zero (DC), $X _ { C }$ tends to infinity, and the current is zero once the capacitor is charged. At very high frequencies, the capacitor’s reactance tends to zero—it has a negligible reactance and does not impede the current (it acts like a simple wire). Capacitorshavetheop ositeefectonACcircuitsthatinductorshave.

# Resistors in an AC Circuit

Just as a reminder, consider Figure 23.45, which shows an AC voltage applied to a resistor and a graph of voltage and current versus time. The voltage and current are exactly inphasein a resistor. There is no frequency dependence to the behavior of plain resistance in a circuit:

# AC Voltage in a Resistor

When a sinusoidal voltage is applied to a resistor, the voltage is exactly in phase with the current—they have a $0 ^ { \circ }$ phase angle.