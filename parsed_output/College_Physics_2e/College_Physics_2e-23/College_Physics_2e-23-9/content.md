# 23.9 Inductance

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

Calculate the inductance of an inductor.   
• Calculate the energy stored in an inductor.   
• Calculate the emf generated in an inductor.

# Inductors

Induction is the process in which an emf is induced by changing magnetic flux. Many examples have been discussed so far, some more effective than others. Transformers, for example, are designed to be particularly effective at

inducing a desired voltage and current with very little loss of energy to other forms. Is there a useful physical quantity related to how “effective” a given device is? The answer is yes, and that physical quantity is called inductance.

Mutual inductance is the effect of Faraday’s law of induction for one device upon another, such as the primary coil in transmitting energy to the secondary in a transformer. See Figure 23.37, where simple coils induce emfs in one another.

In the many cases where the geometry of the devices is fixed, flux is changed by varying current. We therefore concentrate on the rate of change of current, $\Delta I / \Delta t$ , as the cause of induction. A change in the current $I _ { 1 }$ in one device, coil 1 in the figure, induces an $\mathrm { e m f } _ { 2 }$ in the other. We express this in equation form as

$$
\mathrm { e m f } _ { 2 } = - M \frac { \Delta I _ { 1 } } { \Delta t } ,
$$

where $M$ is defined to be the mutual inductance between the two devices. The minus sign is an expression of Lenz’s law. The larger the mutual inductance $M$ , the more effective the coupling. For example, the coils in Figure 23.37 have a small $M$ compared with the transformer coils in Figure 23.27. Units for $M$ are $( \mathbf { V } \cdot \mathbf { s } ) / \mathbf { A } = \Omega \cdot \mathbf { s }$ , which is named a henry (H), after Joseph Henry. That is, $1 \mathrm { H } = 1 \boldsymbol { \Omega } \cdot \mathrm { s }$ .

Nature is symmetric here. If we change the current $I _ { 2 }$ in coil 2, we induce an $\mathrm { e m f } _ { 1 }$ in coil 1, which is given by

$$
\mathrm { e m f } _ { 1 } = - M \frac { \Delta I _ { 2 } } { \Delta t } ,
$$

where $M$ is the same as for the reverse process. Transformers run backward with the same effectiveness, or mutual inductance $M$ .

A large mutual inductance $M$ may or may not be desirable. We want a transformer to have a large mutual inductance. But an appliance, such as an electric clothes dryer, can induce a dangerous emf on its case if the mutual inductance between its coils and the case is large. One way to reduce mutual inductance $M$ is to counterwind coils to cancel the magnetic field produced. (See Figure 23.38.)

Self-inductance, the effect of Faraday’s law of induction of a device on itself, also exists. When, for example, current through a coil is increased, the magnetic field and flux also increase, inducing a counter emf, as required by Lenz’s law. Conversely, if the current is decreased, an emf is induced that opposes the decrease. Most devices have a fixed geometry, and so the change in flux is due entirely to the change in current $\Delta I$ through the device. The induced emf is related to the physical geometry of the device and the rate of change of current. It is given by

$$
\mathrm { e m f } = - L { \frac { \Delta I } { \Delta t } } ,
$$

where $L$ is the self-inductance of the device. A device that exhibits significant self-inductance is called an inductor, and given the symbol in Figure 23.39.

The minus sign is an expression of Lenz’s law, indicating that emf opposes the change in current. Units of selfinductance are henries (H) just as for mutual inductance. The larger the self-inductance $L$ of a device, the greater its opposition to any change in current through it. For example, a large coil with many turns and an iron core has a large $L$ and will not allow current to change quickly. To avoid this effect, a small $L$ must be achieved, such as by counterwinding coils as in Figure 23.38.

A 1 H inductor is a large inductor. To illustrate this, consider a device with $L = 1 . 0 \mathrm { H }$ that has a 10 A current flowing through it. What happens if we try to shut off the current rapidly, perhaps in only $\mathsf { 1 . 0 } \mathsf { m s ? }$ An emf, given by $\mathrm { e m f } = - L ( \Delta I / \Delta t )$ , will oppose the change. Thus an emf will be induced given by   
$\mathrm { e m f } = - L ( \Delta I / \Delta t ) { = } ( 1 . 0 \mathrm { H } ) [ ( 1 0 \mathrm { A } ) / ( 1 . 0 \mathrm { m s } ) ] { = } 1 0 { , } 0 0 0 \mathrm { V } .$ The positive sign means this large voltage is in the same direction as the current, opposing its decrease. Such large emfs can cause arcs, damaging switching equipment, and so it may be necessary to change current more slowly.

There are uses for such a large induced voltage. Camera flashes use a battery, two inductors that function as a transformer, and a switching system or oscillator to induce large voltages. (Remember that we need a changing magnetic field, brought about by a changing current, to induce a voltage in another coil.) The oscillator system will do this many times as the battery voltage is boosted to over one thousand volts. (You may hear the high pitched whine from the transformer as the capacitor is being charged.) A capacitor stores the high voltage for later use in powering the flash. (See Figure 23.40.)

It is possible to calculate $L$ for an inductor given its geometry (size and shape) and knowing the magnetic field that it produces. This is difficult in most cases, because of the complexity of the field created. So in this text the inductance $L$ is usually a given quantity. One exception is the solenoid, because it has a very uniform field inside, a nearly zero field outside, and a simple shape. It is instructive to derive an equation for its inductance. We start by noting that the induced emf is given by Faraday’s law of induction as $= - N ( \Delta \phi / \Delta t )$ and, by the definition of self-inductance, as $= - L ( \Delta I / \Delta t )$ . Equating these yields

$$
{ \mathrm { e m f } } = - N { \frac { \Delta \phi } { \Delta t } } = - L { \frac { \Delta I } { \Delta t } } .
$$

Solving for $L$ gives

$$
L = N { \frac { \Delta \phi } { \Delta I } } .
$$

This equation for the self-inductance $L$ of a device is always valid. It means that self-inductance $L$ depends on how effective the current is in creating flux; the more effective, the greater $\Delta \phi / \Delta I$ is.

Let us use this last equation to find an expression for the inductance of a solenoid. Since the area $A$ of a solenoid is fixed, the change in flux is $\Delta \phi = \Delta ( B A ) = A \Delta B .$ . To find $\Delta B$ , we note that the magnetic field of a solenoid is given by $\begin{array} { r } { B = \mu _ { 0 } n I = \mu _ { 0 } \frac { N I } { \ell } } \end{array}$ . (Here $n = N / \ell$ , where $N$ is the number of coils and $\ell$ is the solenoid’s length.) Only the current changes, so that $\begin{array} { r } { \Delta \Phi = A \Delta B = \mu _ { 0 } N A \frac { \Delta I } { \ell } } \end{array}$ . Substituting $\Delta \phi$ into $\begin{array} { r } { L = N \frac { \Delta \phi } { \Delta I } } \end{array}$ gives

$$
L = N { \frac { \Delta \phi } { \Delta I } } = N { \frac { \mu _ { 0 } N A { \frac { \Delta I } { \ell } } } { \Delta I } } .
$$

This simplifies to

$$
L = { \frac { \mu _ { 0 } N ^ { 2 } A } { \ell } } { \mathrm { ( s o l e n o i d ) } } .
$$

This is the self-inductance of a solenoid of cross-sectional area $A$ and length $\ell$ . Note that the inductance depends only on the physical characteristics of the solenoid, consistent with its definition.

# EXAMPLE 23.7

# Calculating the Self-inductance of a Moderate Size Solenoid

Calculate the self-inductance of a $1 0 . 0 \mathsf { c m }$ long, $4 . 0 0 \mathsf { c m }$ diameter solenoid that has 200 coils.

# Strategy

This is a straightforward application of , since all quantities in the equation except $L$ are known.

# Solution

Use the following expression for the self-inductance of a solenoid:

$$
L = { \frac { \mu _ { 0 } N ^ { 2 } A } { \ell } } .
$$

The cross-sectional area in this example is $A = \pi r ^ { 2 } = ( 3 . 1 4 . . . ) ( 0 . 0 2 0 0 ~ \mathrm { m } ) ^ { 2 } = 1 . 2 6 \times 1 0 ^ { - 3 } ~ \mathrm { m } ^ { 2 }$ , $N$ is given to be 200, and the length $\ell$ is $0 . 1 0 0 \mathsf { m }$ . We know the permeability of free space is $\mu _ { 0 } = 4 \pi \times 1 0 ^ { - 7 }$ . Substituting these into the expression for $L$ gives

$$
\begin{array} { r c l } { { { \cal L } } } & { { = } } & { { \frac { ( 4 \pi \times 1 0 ^ { - 7 } \mathrm {  ~ T } \cdot \mathrm { m } / \mathrm { A } ) ( 2 0 0 ) ^ { 2 } ( 1 . 2 6 \times 1 0 ^ { - 3 } \mathrm {  ~ m } ^ { 2 } ) } { 0 . 1 0 0 \mathrm {  ~ m } } } } \\ { { } } & { { = } } & { { 0 . 6 3 2 \mathrm {  ~ m H } . } } \end{array}
$$

# Discussion

This solenoid is moderate in size. Its inductance of nearly a millihenry is also considered moderate.

One common application of inductance is used in traffic lights that can tell when vehicles are waiting at the intersection. An electrical circuit with an inductor is placed in the road under the place a waiting car will stop over. The body of the car increases the inductance and the circuit changes sending a signal to the traffic lights to change colors. Similarly, metal detectors used for airport security employ the same technique. A coil or inductor in the metal detector frame acts as both a transmitter and a receiver. The pulsed signal in the transmitter coil induces a signal in the receiver. The self-inductance of the circuit is affected by any metal object in the path. Such detectors can be adjusted for sensitivity and also can indicate the approximate location of metal found on a person. See Figure 23.41.

# Energy Stored in an Inductor

We know from Lenz’s law that inductances oppose changes in current. There is an alternative way to look at this opposition that is based on energy. Energy is stored in a magnetic field. It takes time to build up energy, and it also takes time to deplete energy; hence, there is an opposition to rapid change. In an inductor, the magnetic field is directly proportional to current and to the inductance of the device. It can be shown that the energy stored in an inductor $E _ { \mathrm { i n d } }$ is given by

$$
E _ { \mathrm { i n d } } = { \frac { 1 } { 2 } } L I ^ { 2 } .
$$

This expression is similar to that for the energy stored in a capacitor.

# EXAMPLE 23.8

# Calculating the Energy Stored in the Field of a Solenoid

How much energy is stored in the $0 . 6 3 2 ~ \mathsf { m H }$ inductor of the preceding example when a 30.0 A current flows through it?

# Strategy

The energy is given by the equation $\begin{array} { r } { E _ { \mathrm { i n d } } = \frac { 1 } { 2 } L I ^ { 2 } } \end{array}$ , and all quantities except $E _ { \mathrm { i n d } }$ are known.

# Solution

Substituting the value for $L$ found in the previous example and the given current into $\begin{array} { r } { E _ { \mathrm { i n d } } = \frac { 1 } { 2 } L I ^ { 2 } } \end{array}$ gives

$$
\begin{array} { l l l } { { E _ { \mathrm { i n d } } } } & { { = } } & { { { \frac { 1 } { 2 } } L I ^ { 2 } } } \\ { { } } & { { = } } & { { 0 . 5 ( 0 . 6 3 2 \times 1 0 ^ { - 3 } \ \mathrm { H } ) ( 3 0 . 0 \ \mathrm { A } ) ^ { 2 } { = } 0 . 2 8 4 \ \mathrm { J } . } } \end{array}
$$

# Discussion

This amount of energy is certainly enough to cause a spark if the current is suddenly switched off. It cannot be built up instantaneously unless the power input is infinite.