# 20.5 Alternating Current versus Direct Current

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

Explain the differences and similarities between AC and DC current.   
• Calculate rms voltage, current, and average power.   
• Explain why AC current is used for power transmission.

# Alternating Current

Most of the examples dealt with so far, and particularly those utilizing batteries, have constant voltage sources. Once the current is established, it is thus also a constant. Direct current (DC) is the flow of electric charge in only one direction. It is the steady state of a constant-voltage circuit. Most well-known applications, however, use a timevarying voltage source. Alternating current (AC) is the flow of electric charge that periodically reverses direction. If the source varies periodically, particularly sinusoidally, the circuit is known as an alternating current circuit. Examples include the commercial and residential power that serves so many of our needs. Figure 20.14 shows graphs of voltage and current versus time for typical DC and AC power. The AC voltages and frequencies commonly used in homes and businesses vary around the world.

Figure 20.15 shows a schematic of a simple circuit with an AC voltage source. The voltage between the terminals fluctuates as shown, with the AC voltage given by

$$
V = V _ { 0 } \sin 2 \pi f t ,
$$

where $V$ is the voltage at time $t$ , $V _ { 0 }$ is the peak voltage, and $f$ is the frequency in hertz. For this simple resistance circuit, $I = W R$ , and so the AC current is

$$
I = I _ { 0 } \sin 2 \pi f t ,
$$

where $I$ is the current at time $t$ , and $I _ { 0 } = V _ { 0 } / R$ is the peak current. For this example, the voltage and current are said to be in phase, as seen in Figure 20.14(b).

Current in the resistor alternates back and forth just like the driving voltage, since $I = W R$ . If the resistor is a fluorescent light bulb, for example, it brightens and dims 120 times per second as the current repeatedly goes through zero. A $1 2 0 - 1 - 1 z$ flicker is too rapid for your eyes to detect, but if you wave your hand back and forth between your face and a fluorescent light, you will see a stroboscopic effect evidencing AC. The fact that the light output fluctuates means that the power is fluctuating. The power supplied is $P = I V .$ Using the expressions for $I$ and $V$ above, we see that the time dependence of power is $P = I _ { 0 } V _ { 0 } \sin ^ { 2 } 2 \pi f t$ , as shown in Figure 20.16.

# Making Connections: Take-Home Experiment—AC/DC Lights

Wave your hand back and forth between your face and a fluorescent light bulb. Do you observe the same thing with the headlights on your car? Explain what you observe. Warning:Donotlo kdirectlyatverybrightlight.

We are most often concerned with average power rather than its fluctuations—that 60-W light bulb in your desk lamp has an average power consumption of $6 0 \mathsf { W }$ , for example. As illustrated in Figure 20.16, the average power $P _ { \mathrm { a v e } }$ is

$$
P _ { \mathrm { a v e } } = { \frac { 1 } { 2 } } I _ { 0 } V _ { 0 } .
$$

This is evident from the graph, since the areas above and below the $( 1 / 2 ) I _ { 0 } V _ { 0 }$ line are equal, but it can also be proven using trigonometric identities. Similarly, we define an average or rms current $I _ { \mathrm { r m s } }$ and average or rms voltage $V _ { \mathrm { r m s } }$ to be, respectively,

$$
I _ { \mathrm { r m s } } = { \frac { I _ { 0 } } { \sqrt { 2 } } }
$$

and

$$
V _ { \mathrm { r m s } } = { \frac { V _ { 0 } } { \sqrt { 2 } } } .
$$

where rms stands for root mean square, a particular kind of average. In general, to obtain a root mean square, the particular quantity is squared, its mean (or average) is found, and the square root is taken. This is useful for AC, since the average value is zero. Now,

$$
P _ { \mathrm { a v e } } = I _ { \mathrm { r m s } } V _ { \mathrm { r m s } } ,
$$

which gives

$$
P _ { \mathrm { a v e } } = { \frac { I _ { 0 } } { \sqrt { 2 } } } \cdot { \frac { V _ { 0 } } { \sqrt { 2 } } } = { \frac { 1 } { 2 } } I _ { 0 } V _ { 0 } ,
$$

as stated above. It is standard practice to quote $I _ { \mathrm { r m s } } , V _ { \mathrm { r m s } }$ , and $P _ { \mathrm { a v e } }$ rather than the peak values. For example, most household electricity is $\boldsymbol { \mathsf { 1 2 0 } } \boldsymbol { \mathsf { V } }$ AC, which means that $V _ { \mathrm { r m s } }$ is $\textstyle 1 2 0 \vee .$ . The common 10-A circuit breaker will interrupt a sustained $I _ { \mathrm { r m s } }$ greater than 10 A. Your $\mathsf { 1 . 0 \mathrm { - } k W }$ microwave oven consumes $P _ { \mathrm { a v e } } = 1 . 0 \mathrm { k W }$ , and so on. You can think of these rms and average values as the equivalent DC values for a simple resistive circuit.

To summarize, when dealing with AC, Ohm’s law and the equations for power are completely analogous to those for DC, but rms and average values are used for AC. Thus, for AC, Ohm’s law is written

$$
I _ { \mathrm { r m s } } = { \frac { V _ { \mathrm { r m s } } } { R } } .
$$

The various expressions for AC power $P _ { \mathrm { a v e } }$ are

$$
\begin{array} { r l r } { \mathrm { ~ } } & { { } } & { P _ { \mathrm { a v e } } = I _ { \mathrm { r m s } } V _ { \mathrm { r m s } } , } \\ { \mathrm { ~ } } & { { } } & { P _ { \mathrm { a v e } } = \cfrac { V _ { \mathrm { r m s } } ^ { 2 } } { R } , } \end{array}
$$

and

$$
P _ { \mathrm { a v e } } = I _ { \mathrm { r m s } } ^ { 2 } R .
$$

# EXAMPLE 20.9

# Peak Voltage and Power for AC

(a) What is the value of the peak voltage for 120-V AC power? (b) What is the peak power consumption rate of a 60.0-W AC light bulb?

# Strategy

We are told that $V _ { \mathrm { r m s } }$ is $\textstyle 1 2 0 \vee$ and $P _ { \mathrm { a v e } }$ is 60.0 W. We can use $V _ { \mathrm { r m s } } = { \frac { V _ { 0 } } { \sqrt { 2 } } }$ to find the peak voltage, and we can manipulate the definition of power to find the peak power from the given average power.

# Solution for (a)

Solving the equation $V _ { \mathrm { r m s } } = { \frac { V _ { 0 } } { \sqrt { 2 } } }$ for the peak voltage $V _ { 0 }$ and substituting the known value for $V _ { \mathrm { r m s } }$ gives

$$
V _ { 0 } = \sqrt { 2 } V _ { \mathrm { r m s } } = 1 . 4 1 4 ( 1 2 0 \mathrm { V } ) { = } 1 7 0 \mathrm { V } .
$$

# Discussion for (a)

This means that the AC voltage swings from $\boldsymbol { \mathsf { 1 7 0 } } \boldsymbol { \mathsf { V } }$ to $- 1 7 0 \mathrm { V }$ and back 60 times every second. An equivalent DC voltage is a constant $\textstyle 1 2 0 \vee .$ .

# Solution for (b)

Peak power is peak current times peak voltage. Thus,

$$
P _ { 0 } = I _ { 0 } V _ { 0 } = 2 \bigg ( \frac { 1 } { 2 } I _ { 0 } V _ { 0 } \bigg ) = 2 P _ { \mathrm { a v e } } .
$$

We know the average power is 60.0 W, and so

$$
P _ { 0 } = 2 ( 6 0 . 0 \mathrm { W } ) { = } 1 2 0 \mathrm { W } .
$$

# Discussion

So the power swings from zero to 120 W one hundred twenty times per second (twice each cycle), and the power averages 60 W.

# Why Use AC for Power Distribution?

Most large power-distribution systems are AC. Moreover, the power is transmitted at much higher voltages than the 120-V AC $2 4 0 \vee$ in most parts of the world) we use in homes and on the job. Economies of scale make it cheaper to build a few very large electric power-generation plants than to build numerous small ones. This necessitates sending power long distances, and it is obviously important that energy losses en route be minimized. High voltages can be transmitted with much smaller power losses than low voltages, as we shall see. (See Figure 20.17.) For safety reasons, the voltage at the user is reduced to familiar values. The crucial factor is that it is much easier to increase and decrease AC voltages than DC, so AC is used in most large power distribution systems.



# EXAMPLE 20.10

# Power Losses Are Less for High-Voltage Transmission

(a) What current is needed to transmit 100 MW of power at $2 0 0 \mathsf { k } \mathsf { V ? }$ (b) What is the power dissipated by the transmission lines if they have a resistance of $1 . 0 0 \Omega ?$ (c) What percentage of the power is lost in the transmission lines?

# Strategy

We are given $P _ { \mathrm { a v e } } = 1 0 0 \ : \mathrm { M W } _ { \mathrm { ; } }$ , $V _ { \mathrm { r m s } } = 2 0 0 \mathrm { k V }$ , and the resistance of the lines is $R = 1 . 0 0 \Omega$ . Using these givens, we can find the current flowing (from $P = I V$ and then the power dissipated in the lines $( P = I ^ { 2 } R )$ , and we take the ratio to the total power transmitted.

# Solution

To find the current, we rearrange the relationship $P _ { \mathrm { a v e } } = I _ { \mathrm { r m s } } V _ { \mathrm { r m s } }$ and substitute known values. This gives

$$
I _ { \mathrm { r m s } } = { \frac { P _ { \mathrm { a v e } } } { V _ { \mathrm { r m s } } } } = { \frac { 1 0 0 \times 1 0 ^ { 6 } ~ { \mathrm { W } } } { 2 0 0 \times 1 0 ^ { 3 } ~ { \mathrm { V } } } } = 5 0 0 ~ { \mathrm { A } } .
$$

# Solution

Knowing the current and given the resistance of the lines, the power dissipated in them is found from $P _ { \mathrm { a v e } } = I _ { \mathrm { r m s } } ^ { 2 } R$ . Substituting the known values gives

$$
P _ { \mathrm { a v e } } = I _ { \mathrm { r m s } } ^ { 2 } R = ( 5 0 0 \mathrm { A } ) ^ { 2 } ( 1 . 0 0 \Omega ) = 2 5 0 \mathrm { k W } .
$$

# Solution

The percent loss is the ratio of this lost power to the total or input power, multiplied by 100:

$$
\mathcal { I } _ { 0 } \mathrm { { l o s s } = } \frac { 2 5 0 \mathrm { { k W } } } { 1 0 0 \mathrm { { M W } } } \times 1 0 0 = 0 . 2 5 0 \mathrm { { \% } } .
$$

# Discussion

One-fourth of a percent is an acceptable loss. Note that if 100 MW of power had been transmitted at $2 5 \mathsf { k V } _ { : }$ , then a current of 4000 A would have been needed. This would result in a power loss in the lines of ${ 1 6 . 0 \mathsf { M } } { \mathsf { W } }$ , or $1 6 . 0 \%$ rather than $0 . 2 5 0 \%$ . The lower the voltage, the more current is needed, and the greater the power loss in the fixedresistance transmission lines. Of course, lower-resistance lines can be built, but this requires larger and more expensive wires. If superconducting lines could be economically produced, there would be no loss in the

transmission lines at all. But, as we shall see in a later chapter, there is a limit to current in superconductors, too. In short, high voltages are more economical for transmitting power, and AC voltage is much easier to raise and lower, so that AC is used in most large-scale power distribution systems.

It is widely recognized that high voltages pose greater hazards than low voltages. But, in fact, some high voltages, such as those associated with common static electricity, can be harmless. So it is not voltage alone that determines a hazard. It is not so widely recognized that AC shocks are often more harmful than similar DC shocks. Thomas Edison thought that AC shocks were more harmful and set up a DC power-distribution system in New York City in the late 1800s. There were bitter fights, in particular between Edison and George Westinghouse and Nikola Tesla, who were advocating the use of AC in early power-distribution systems. AC has prevailed largely due to transformers and lower power losses with high-voltage transmission.

# PHET EXPLORATIONS

# Generator

Generate electricity with a bar magnet! Discover the physics behind the phenomena by exploring magnets and how you can use them to make a bulb light.

Click to view content (https://openstax.org/l/28gen).