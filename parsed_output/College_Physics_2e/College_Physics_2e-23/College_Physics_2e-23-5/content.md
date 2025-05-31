# 23.5 Electric Generators

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

• Calculate the emf induced in a generator.   
• Calculate the peak emf which can be induced in a particular generator system.

Electric generators induce an emf by rotating a coil in a magnetic field, as briefly discussed in Induced Emf and Magnetic Flux. We will now explore generators in more detail. Consider the following example.

# EXAMPLE 23.3

# Calculating the Emf Induced in a Generator Coil

The generator coil shown in Figure 23.19 is rotated through one-fourth of a revolution (from $\theta = 0 ^ { \circ }$ to $\theta = 9 0 ^ { \circ }$ ) in $1 5 . 0 \mathsf { m s }$ . The 200-turn circular coil has a $5 . 0 0 \mathsf { c m }$ radius and is in a uniform $\pm . 2 5 \intercal$ magnetic field. What is the average emf induced?

# Strategy

We use Faraday’s law of induction to find the average emf induced over a time $\Delta t$ :

$$
\mathrm { e m f } = - N \frac { \Delta \phi } { \Delta t } .
$$

We know that $N = 2 0 0$ and $\Delta t = 1 5 . 0 \mathrm { m s }$ , and so we must determine the change in flux $\Delta \phi$ to find emf.

# Solution

Since the area of the loop and the magnetic field strength are constant, we see that

$$
\Delta \phi = \Delta ( B A \cos \theta ) = A B \Delta ( \cos \theta ) .
$$

Now, $\Delta ( \cos \theta ) { = - 1 . 0 }$ , since it was given that $\theta$ goes from $0 ^ { \circ }$ to $9 0 ^ { \circ }$ . Thus $\Delta \phi = - A B$ , and

$$
{ \mathrm { e m f } } = N { \frac { A B } { \Delta t } } .
$$

The area of the loop is $A = \pi r ^ { 2 } = ( 3 . 1 4 . . . ) ( 0 . 0 5 0 0 ~ \mathrm { m } ) ^ { 2 } = 7 . 8 5 \times 1 0 ^ { - 3 } ~ \mathrm { m } ^ { 2 } .$ . Entering this value gives

$$
\mathrm { e m f } = 2 0 0 { \frac { ( 7 . 8 5 \times 1 0 ^ { - 3 } \ \mathrm { m } ^ { 2 } ) ( 1 . 2 5 \ \mathrm { T } ) } { 1 5 . 0 \times 1 0 ^ { - 3 } \ \mathrm { s } } } = 1 3 1 \ \mathrm { V } .
$$

# Discussion

This is a practical average value, similar to the $\textstyle 1 2 0 \vee$ used in household power.

The emf calculated in Example 23.3 is the average over one-fourth of a revolution. What is the emf at any given instant? It varies with the angle between the magnetic field and a perpendicular to the coil. We can get an expression for emf as a function of time by considering the motional emf on a rotating rectangular coil of width $w$ and height $\ell$ in a uniform magnetic field, as illustrated in Figure 23.20.

Charges in the wires of the loop experience the magnetic force, because they are moving in a magnetic field. Charges in the vertical wires experience forces parallel to the wire, causing currents. But those in the top and bottom segments feel a force perpendicular to the wire, which does not cause a current. We can thus find the induced emf by considering only the side wires. Motional emf is given to be $\mathbf { \nabla } = B \ell \boldsymbol { v }$ , where the velocity vis perpendicular to the magnetic field $B$ . Here the velocity is at an angle $\theta$ with $B$ , so that its component perpendicular to $B$ is $v$ sin $\theta$ (see Figure 23.20). Thus in this case the emf induced on each side is $\mathbf { \nabla } = B \ell \boldsymbol { v }$ sin $\theta$ , and they are in the same direction. The total emf around the loop is then

$$
\operatorname { e m f } = 2 B \ell v \sin \theta .
$$

This expression is valid, but it does not give emf as a function of time. To find the time dependence of emf, we assume the coil rotates at a constant angular velocity $\omega$ . The angle $\theta$ is related to angular velocity by $\theta = \omega t$ , so that

$$
\mathrm { e m f } = 2 B \ell v \sin \omega t .
$$

Now, linear velocity $v$ is related to angular velocity $\omega$ by $v = r \omega$ . Here $r = w / 2$ , so that $\scriptstyle v = ( w / 2 ) \omega$ , and

$$
\mathrm { e m f } = 2 B \ell \frac { w } { 2 } \omega \sin \omega t = ( \ell w ) B \omega \sin \omega t .
$$

Noting that the area of the loop is $A = \ell w$ , and allowing for $N$ loops, we find that

$$
{ \mathrm { e m f } } = N A B \omega \sin \omega t
$$

is the emf induced in a generator coil of $N$ turns and area $A$ rotating at a constant angular velocity $\omega$ in a uniform magnetic field $B$ . This can also be expressed as

$$
\mathrm { e m f } = \mathrm { e m f _ { 0 } } \ \sin \omega t ,
$$

where

$$
{ \mathrm { e m f } } _ { 0 } = N A B \omega
$$

is the maximum (peak) emf. Note that the frequency of the oscillation is $f = \omega / 2 \pi$ , and the period is $T = 1 / f = 2 \pi / \omega .$ .Figure 23.21 shows a graph of emf as a function of time, and it now seems reasonable that AC voltage is sinusoidal.

The fact that the peak emf, ${ \mathrm { e m f } } _ { 0 } = N A B \omega$ , makes good sense. The greater the number of coils, the larger their area, and the stronger the field, the greater the output voltage. It is interesting that the faster the generator is spun (greater $\omega ,$ ), the greater the emf. This is noticeable on bicycle generators—at least the cheaper varieties. One of the authors as a juvenile found it amusing to ride his bicycle fast enough to burn out his lights, until he had to ride home lightless one dark night.

Figure 23.22 shows a scheme by which a generator can be made to produce pulsed DC. More elaborate arrangements of multiple coils and split rings can produce smoother DC, although electronic rather than mechanical means are usually used to make ripple-free DC.

# EXAMPLE 23.4

# Calculating the Maximum Emf of a Generator

Calculate the maximum emf, $\mathrm { e m f _ { 0 } }$ , of the generator that was the subject of Example 23.3.

# Strategy

Once $\omega$ , the angular velocity, is determined, ${ \mathrm { e m f } } _ { 0 } = N A B \omega$ can be used to find $\mathrm { e m f } _ { 0 }$ . All other quantities are

known.

# Solution

Angular velocity is defined to be the change in angle per unit time:

$$
\omega = { \frac { \Delta \theta } { \Delta t } } .
$$

One-fourth of a revolution is $\pi / 2$ radians, and the time is $0 . 0 1 5 0 \mathsf s$ ; thus,

$$
\begin{array} { l l l } { \omega } & { = } & { \frac { \pi / 2 \ \mathrm { r a d } } { 0 . 0 1 5 0 \ \mathrm { s } } } \\ & { = } & { 1 0 4 . 7 \ \mathrm { r a d / s } . } \end{array}
$$

$1 0 4 . 7 \ r { \mathsf { a d } } / { \mathsf { s } }$ is exactly 1000 rpm. We substitute this value for $\omega$ and the information from the previous example into ${ \mathrm { e m f } } _ { 0 } = N A B \omega$ , yielding

$$
{ \begin{array} { l l l } { \operatorname { e m f } _ { 0 } } & { = } & { N A B \omega } \\ & { = } & { 2 0 0 ( 7 . 8 5 \times 1 0 ^ { - 3 } \ \mathrm { m } ^ { 2 } ) ( 1 . 2 5 \ \mathrm { T } ) ( 1 0 4 . 7 \ \mathrm { r a d } / \mathrm { s } ) . } \\ & { = } & { 2 0 6 \ \mathrm { V } } \end{array} }
$$

# Discussion

The maximum emf is greater than the average emf of $\boldsymbol { \mathsf { 1 3 1 V } }$ found in the previous example, as it should be.

In real life, electric generators look a lot different than the figures in this section, but the principles are the same. The source of mechanical energy that turns the coil can be falling water (hydropower), steam produced by the burning of fossil fuels, or the kinetic energy of wind. Figure 23.23 shows a cutaway view of a steam turbine; steam moves over the blades connected to the shaft, which rotates the coil within the generator.

Generators illustrated in this section look very much like the motors illustrated previously. This is not coincidental. In fact, a motor becomes a generator when its shaft rotates. Certain early automobiles used their starter motor as a generator. In Back Emf, we shall further explore the action of a motor as a generator.