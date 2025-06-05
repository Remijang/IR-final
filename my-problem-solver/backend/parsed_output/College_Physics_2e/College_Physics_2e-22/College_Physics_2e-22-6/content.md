# 22.6 The Hall Effect

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

Describe the Hall effect. • Calculate the Hall emf across a current-carrying conductor.

We have seen effects of a magnetic field on free-moving charges. The magnetic field also affects charges moving in a conductor. One result is the Hall effect, which has important implications and applications.

Figure 22.26 shows what happens to charges moving through a conductor in a magnetic field. The field is perpendicular to the electron drift velocity and to the width of the conductor. Note that conventional current is to the right in both parts of the figure. In part (a), electrons carry the current and move to the left. In part (b), positive charges carry the current and move to the right. Moving electrons feel a magnetic force toward one side of the conductor, leaving a net positive charge on the other side. This separation of charge createsavoltage $\varepsilon$ , known as the Hall emf, acros the conductor. The creation of a voltage acros a current-carrying conductor by a magnetic field is known as the Hall effect, after Edwin Hall, the American physicist who discovered it in 1879.

One very important use of the Hall effect is to determine whether positive or negative charges carries the current. Note that in Figure 22.26(b), where positive charges carry the current, the Hall emf has the sign opposite to when negative charges carry the current. Historically, the Hall effect was used to show that electrons carry current in metals and it also shows that positive charges carry current in some semiconductors. The Hall effect is used today as a research tool to probe the movement of charges, their drift velocities and densities, and so on, in materials. In 1980, it was discovered that the Hall effect is quantized, an example of quantum behavior in a macroscopic object.

The Hall effect has other uses that range from the determination of blood flow rate to precision measurement of magnetic field strength. To examine these quantitatively, we need an expression for the Hall emf, $\varepsilon$ , across a conductor. Consider the balance of forces on a moving charge in a situation where $B , v$ , and $l$ are mutually perpendicular, such as shown in Figure 22.27. Although the magnetic force moves negative charges to one side, they cannot build up without limit. The electric field caused by their separation opposes the magnetic force, ${ \boldsymbol { F } } = q v { \boldsymbol { B } }$ , and the electric force, $F _ { \mathrm { e } } = q E$ , eventually grows to equal it. That is,

$$
q E = q v B
$$

or

$$
E = v B .
$$

Note that the electric field $E$ is uniform across the conductor because the magnetic field $B$ is uniform, as is the conductor. For a uniform electric field, the relationship between electric field and voltage is $E = \varepsilon / l$ , where $l$ is the width of the conductor and $\varepsilon$ is the Hall emf. Entering this into the last expression gives

$$
\frac { \varepsilon } { l } = v B .
$$

Solving this for the Hall emf yields

$$
\varepsilon = B l v ( B , v , \mathrm { a n d } l , \mathrm { m u t u a l l y p e r p e n d i c u l a r } ) ,
$$

where $\varepsilon$ is the Hall effect voltage across a conductor of width $l$ through which charges move at a speed $v$ .

One of the most common uses of the Hall effect is in the measurement of magnetic field strength $B$ . Such devices, called Hal probes, can be made very small, allowing fine position mapping. Hall probes can also be made very accurate, usually accomplished by careful calibration. Another application of the Hall effect is to measure fluid flow in any fluid that has free charges (most do). (See Figure 22.28.) A magnetic field applied perpendicular to the flow direction produces a Hall emf $\varepsilon$ as shown. Note that the sign of $\varepsilon$ depends not on the sign of the charges, but only on the directions of $B$ and $v$ . The magnitude of the Hall emf is ${ \varepsilon } = B l v$ , where $l$ is the pipe diameter, so that the average velocity $v$ can be determined from $\varepsilon$ providing the other factors are known.

# EXAMPLE 22.3

# Calculating the Hall emf: Hall Effect for Blood Flow

A Hall effect flow probe is placed on an artery, applying a $0 . 1 0 0 \mathrm { - } \mathsf { T }$ magnetic field across it, in a setup similar to that in Figure 22.28. What is the Hall emf, given the vessel’s inside diameter is $4 . 0 0 \ : \mathrm { m m }$ and the average blood velocity is $2 0 . 0 \mathsf { c m } / \mathsf { s } ?$

# Strategy

Because , $v$ , and $l$ are mutually perpendicular, the equation ${ \varepsilon = B l v }$ can be used to find $\varepsilon$ .

# Solution

Entering the given values for $B , v$ , and $l$ gives

$$
\begin{array} { l l l } { \varepsilon } & { = } & { B l v = ( 0 . 1 0 0 \mathrm { \ T } ) \bigl ( 4 . 0 0 \times 1 0 ^ { - 3 } \mathrm { \ m } \bigr ) ( 0 . 2 0 0 \mathrm { \ m / s } ) } \\ & { = } & { 8 0 . 0 \mu \mathrm { V } } \end{array}
$$

# Discussion

This is the average voltage output. Instantaneous voltage varies with pulsating blood flow. The voltage is small in this type of measurement. $\varepsilon$ is particularly difficult to measure, because there are voltages associated with heart action (ECG voltages) that are on the order of millivolts. In practice, this difficulty is overcome by applying an AC magnetic field, so that the Hall emf is AC with the same frequency. An amplifier can be very selective in picking out only the appropriate frequency, eliminating signals and noise at other frequencies.