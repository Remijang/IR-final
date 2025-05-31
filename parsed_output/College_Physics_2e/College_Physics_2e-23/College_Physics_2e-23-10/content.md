# 23.10 RL Circuits

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

• Calculate the current in an RL circuit after a specified number of characteristic time steps.   
• Calculate the characteristic time of an RL circuit.   
• Sketch the current in an RL circuit over time.

We know that the current through an inductor $L$ cannot be turned on or off instantaneously. The change in current changes flux, inducing an emf opposing the change (Lenz’s law). How long does the opposition last? Current wil flow and canbe turned off, but how long does it take? Figure 23.42 shows a switching circuit that can be used to examine current through an inductor as a function of time.

When the switch is first moved to position 1 (at $t = 0$ ), the current is zero and it eventually rises to $I _ { 0 } = W R$ , where $R$ is the total resistance of the circuit. The opposition of the inductor $L$ is greatest at the beginning, because the amount of change is greatest. The opposition it poses is in the form of an induced emf, which decreases to zero as the current approaches its final value. The opposing emf is proportional to the amount of change left. This is the hallmark of an exponential behavior, and it can be shown with calculus that

$$
I = I _ { 0 } ( 1 - e ^ { - t / \tau } ) \quad ( \mathrm { t u r n i n g o n } ) ,
$$

is the current in an $R L$ circuit when switched on (Note the similarity to the exponential behavior of the voltage on a charging capacitor). The initial current is zero and approaches $I _ { 0 } = W R$ with a characteristic time constant $\tau$ for an $R L$ circuit, given by

$$
\tau = \frac { L } { R } ,
$$

where $\tau$ has units of seconds, since $1 \ \mathrm { H } = 1 \ \Omega$ . In the first period of time $\tau$ , the current rises from zero to $0 . 6 3 2 I _ { 0 }$ , since $I = I _ { 0 } ( 1 - e ^ { - 1 } ) = I _ { 0 } ( 1 - 0 . 3 6 8 ) = 0 . 6 3 2 I _ { 0 } .$ . The current will $\mathtt { g o } 0 . 6 3 2$ of the remainder in the next time $\tau$ . A well-known property of the exponential is that the final value is never exactly reached, but 0.632 of the remainder to that value is achieved in every characteristic time $\tau$ . In just a few multiples of the time $\tau$ , the final value is very nearly achieved, as the graph in Figure 23.42(b) illustrates.

The characteristic time $\tau$ depends on only two factors, the inductance $L$ and the resistance $R$ . The greater the inductance $L$ , the greater $\tau$ is, which makes sense since a large inductance is very effective in opposing change. The smaller the resistance $R$ , the greater $\tau$ is. Again this makes sense, since a small resistance means a large final current and a greater change to get there. In both cases—large $L$ and small $R$ —more energy is stored in the inductor and more time is required to get it in and out.

When the switch in Figure 23.42(a) is moved to position 2 and cuts the battery out of the circuit, the current drops because of energy dissipation by the resistor. But this is also not instantaneous, since the inductor opposes the decrease in current by inducing an emf in the same direction as the battery that drove the current. Furthermore, there is a certain amount of energy, $( 1 / 2 ) L I _ { 0 } ^ { 2 }$ , stored in the inductor, and it is dissipated at a finite rate. As the current approaches zero, the rate of decrease slows, since the energy dissipation rate is $I ^ { 2 } R .$ . Once again the behavior is exponential, and $I$ is found to be

$$
I = I _ { 0 } e ^ { - t / \tau } \quad ( \mathrm { t u r n i n g o f f } ) .
$$

(See Figure 23.42(c).) In the first period of time $\tau = L / R$ after the switch is closed, the current falls to 0.368 of its initial value, since $I = I _ { 0 } e ^ { - 1 } = 0 . 3 6 8 I _ { 0 }$ . In each successive time $\tau$ , the current falls to 0.368 of the preceding value, and in a few multiples of $\tau$ , the current becomes very close to zero, as seen in the graph in Figure 23.42(c).

# EXAMPLE 23.9

# Calculating Characteristic Time and Current in an RLCircuit

(a) What is the characteristic time constant for a $7 . 5 0 \mathsf { m H }$ inductor in series with a $3 . 0 0 \Omega$ resistor? (b) Find the current $5 . 0 0 \mathrm { m s }$ after the switch is moved to position 2 to disconnect the battery, if it is initially $\mathtt { 1 0 . 0 A }$ .

# Strategy for (a)

The time constant for an $R L$ circuit is defined by $\tau = L / R$ .

# Solution for (a)

Entering known values into the expression for $\tau$ given in $\tau = L / R$ yields

$$
\tau = { \frac { L } { R } } = { \frac { 7 . 5 0 \mathrm { m H } } { 3 . 0 0 \Omega } } = 2 . 5 0 \mathrm { m s } .
$$

# Discussion for (a)

This is a small but definitely finite time. The coil will be very close to its full current in about ten time constants, or about $2 5 { \mathsf { m s } }$ .

# Strategy for (b)

We can find the current by using $I = I _ { 0 } e ^ { - t / \tau }$ , or by considering the decline in steps. Since the time is twice the characteristic time, we consider the process in steps.

# Solution for (b)

In the first $2 . 5 0 \mathrm { m s }$ , the current declines to 0.368 of its initial value, which is

$$
\begin{array} { l c l } { { I } } & { { = } } & { { 0 . 3 6 8 I _ { 0 } = ( 0 . 3 6 8 ) ( 1 0 . 0 ~ \mathrm { A } ) } } \\ { { } } & { { = } } & { { 3 . 6 8 ~ \mathrm { A } ~ \mathrm { a t } ~ t = 2 . 5 0 ~ \mathrm { m s } . } } \end{array}
$$

After another 2.50 ms, or a total of $5 . 0 0 ~ \mathrm { m s }$ , the current declines to 0.368 of the value just found. That is,

$$
\begin{array} { r c l } { { I ^ { \prime } } } & { { = } } & { { 0 . 3 6 8 I = ( 0 . 3 6 8 ) ( 3 . 6 8 \mathrm { \AA } ) } } \\ { { } } & { { = } } & { { 1 . 3 5 \mathrm { \AA } \mathrm { a t } t = 5 . 0 0 \mathrm { m s } . } } \end{array}
$$

# Discussion for (b)

After another 5.00 ms has passed, the current will be 0.183 A (see Exercise 23.69); so, although it does die out, the current certainly does not go to zero instantaneously.

In summary, when the voltage applied to an inductor is changed, the current also changes, butthechangeincurent lagsthechangeinvoltageinanRLcircuit. In Reactance, Inductive and Capacitive, we explore how an RLcircuit behaves when a sinusoidal AC voltage is applied.