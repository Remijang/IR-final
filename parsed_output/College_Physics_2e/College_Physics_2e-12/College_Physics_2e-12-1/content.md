# 12.1 Flow Rate and Its Relation to Velocity

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

Calculate flow rate.   
Define units of volume.   
Describe incompressible fluids.   
Explain the consequences of the equation of continuity.

Flow rate $Q$ is defined to be the volume of fluid passing by some location through an area during a period of time, as seen in Figure 12.2. In symbols, this can be written as

$$
Q = { \frac { V } { t } } ,
$$

where $V$ is the volume and $t$ is the elapsed time.

The SI unit for flow rate is $\mathrm { m } ^ { 3 } / \mathrm { s }$ , but a number of other units for $Q$ are in common use. For example, the heart of a resting adult pumps blood at a rate of 5.00 liters per minute $( \mathsf { L } / \mathsf { m i n } )$ . Note that a liter (L) is 1/1000 of a cubic meter or 1000 cubic centimeters $( 1 0 ^ { - 3 } ~ \mathrm { m } ^ { 3 }$ or $1 0 ^ { 3 } ~ \mathrm { c m } ^ { 3 }$ ). In this text we shall use whatever metric units are most convenient for a given situation.

# EXAMPLE 12.1

# Calculating Volume from Flow Rate: The Heart Pumps a Lot of Blood in a Lifetime

How many cubic meters of blood does the heart pump in a 75-year lifetime, assuming the average flow rate is 5.00 L/min?

# Strategy

Time and flow rate $Q$ are given, and so the volume $V$ can be calculated from the definition of flow rate.

# Solution

Solving $Q = V / t$ for volume gives

$$
V = Q t .
$$

Substituting known values yields

$$
\begin{array} { r c l } { { V } } & { { = } } & { { \Big ( \frac { 5 . 0 0 \mathrm { ~ L } } { 1 \mathrm { ~ m i n } } \Big ) ( 7 5 \mathrm { ~ y } ) \bigg ( \frac { 1 \mathrm { ~ m } ^ { 3 } } { 1 0 ^ { 3 } \mathrm { ~ L } } \bigg ) \bigg ( 5 . 2 6 \times 1 0 ^ { 5 } \frac { \mathrm { m i n } } { \mathrm { y } } \bigg ) } } \\ { { } } & { { = } } & { { 2 . 0 \times 1 0 ^ { 5 } \mathrm { ~ m } ^ { 3 } . } } \end{array}
$$

# Discussion

This amount is about 200,000 tons of blood. For comparison, this value is equivalent to about 200 times the volume of water contained in a 6-lane $5 0 \mathrm { - } \mathsf { m }$ lap pool.

Flow rate and velocity are related, but quite different, physical quantities. To make the distinction clear, think about the flow rate of a river. The greater the velocity of the water, the greater the flow rate of the river. But flow rate also depends on the size of the river. A rapid mountain stream carries far less water than the Amazon River in Brazil, for example. The precise relationship between flow rate $Q$ and velocity $\overline { { v } }$ is

$$
Q = A { \overline { { v } } } ,
$$

where $A$ is the cross-sectional area and $\overline { { v } }$ is the average velocity. This equation seems logical enough. The relationship tells us that flow rate is directly proportional to both the magnitude of the average velocity (hereafter referred to as the speed) and the size of a river, pipe, or other conduit. The larger the conduit, the greater its crosssectional area. Figure 12.2 illustrates how this relationship is obtained. The shaded cylinder has a volume

$$
V = A d ,
$$

which flows past the point $\mathrm { \bf P }$ in a time $t$ . Dividing both sides of this relationship by $t$ gives

$$
{ \frac { V } { t } } = { \frac { A d } { t } } .
$$

We note that $Q = V / t$ and the average speed is $\overline { { v } } = d / t$ . Thus the equation becomes $Q = A { \overline { { v } } }$ .

Figure 12.3 shows an incompressible fluid flowing along a pipe of decreasing radius. Because the fluid is incompressible, the same amount of fluid must flow past any point in the tube in a given time to ensure continuity of flow. In this case, because the cross-sectional area of the pipe decreases, the velocity must necessarily increase. This logic can be extended to say that the flow rate must be the same at all points along the pipe. In particular, for points 1 and 2,

$$
\left. \begin{array} { c } { { Q _ { 1 } = Q _ { 2 } } } \\ { { A _ { 1 } \overline { { { v } } } _ { 1 } = A _ { 2 } \overline { { { v } } } _ { 2 } } } \end{array} \right\} .
$$

This is called the equation of continuity and is valid for any incompressible fluid. The consequences of the equation of continuity can be observed when water flows from a hose into a narrow spray nozzle: it emerges with a large speed—that is the purpose of the nozzle. Conversely, when a river empties into one end of a reservoir, the water slows considerably, perhaps picking up speed again when it leaves the other end of the reservoir. In other words, speed increases when cross-sectional area decreases, and speed decreases when cross-sectional area increases.

Since liquids are essentially incompressible, the equation of continuity is valid for all liquids. However, gases are compressible, and so the equation must be applied with caution to gases if they are subjected to compression or expansion.

# EXAMPLE 12.2

# Calculating Fluid Speed: Speed Increases When a Tube Narrows

A nozzle with a radius of $0 . 2 5 0 \mathsf { c m }$ is attached to a garden hose with a radius of $0 . 9 0 0 { \mathsf { c m } }$ . The flow rate through hose and nozzle is $0 . 5 0 0 \mathsf { L } / \mathsf { s } .$ . Calculate the speed of the water (a) in the hose and (b) in the nozzle.

# Strategy

We can use the relationship between flow rate and speed to find both velocities. We will use the subscript 1 for the hose and 2 for the nozzle.

# Solution for (a)

First, we solve $Q = A { \overline { { v } } }$ for $v _ { 1 }$ and note that the cross-sectional area is $A = \pi r ^ { 2 }$ , yielding

$$
\overline { { { v } } } _ { 1 } = \frac { Q } { A _ { 1 } } = \frac { Q } { \pi r _ { 1 } ^ { 2 } } .
$$

Substituting known values and making appropriate unit conversions yields

$$
\overline { { { v } } } _ { 1 } = \frac { ( 0 . 5 0 0 \mathrm { L / s } ) ( 1 0 ^ { - 3 } \mathrm { ~ m ^ { 3 } / L } ) } { \pi ( 9 . 0 0 \times 1 0 ^ { - 3 } \mathrm { ~ m } ) ^ { 2 } } = 1 . 9 6 \mathrm { ~ m / s } .
$$

# Solution for (b)

We could repeat this calculation to find the speed in the nozzle $\overline { { v } } _ { 2 }$ , but we will use the equation of continuity to give a somewhat different insight. Using the equation which states

$$
A _ { 1 } { \overline { { v } } } _ { 1 } = A _ { 2 } { \overline { { v } } } _ { 2 } ,
$$

solving for $\overline { { v } } _ { 2 }$ and substituting $\pi r ^ { 2 }$ for the cross-sectional area yields

$$
\overline { { { v } } } _ { 2 } = \frac { A _ { 1 } } { A _ { 2 } } \overline { { { v } } } _ { 1 } = \frac { \pi r _ { 1 } ^ { 2 } } { \pi r _ { 2 } ^ { 2 } } \overline { { { v } } } _ { 1 } = \frac { r _ { 1 ^ { 2 } } } { r _ { 2 ^ { 2 } } } \overline { { { v } } } _ { 1 } .
$$

Substituting known values,

$$
\overline { { v } } _ { 2 } = \frac { ( 0 . 9 0 0 \mathrm { c m } ) ^ { 2 } } { ( 0 . 2 5 0 \mathrm { c m } ) ^ { 2 } } { 1 . 9 6 \mathrm { m / s } } = 2 5 . 5 \mathrm { m / s } .
$$

# Discussion

A speed of $1 . 9 6 ~ \mathsf { m } / \mathsf { s }$ is about right for water emerging from a nozzleless hose. The nozzle produces a considerably faster stream merely by constricting the flow to a narrower tube.

The solution to the last part of the example shows that speed is inversely proportional to the squareof the radius of the tube, making for large effects when radius varies. We can blow out a candle at quite a distance, for example, by pursing our lips, whereas blowing on a candle with our mouth wide open is quite ineffective.

In many situations, including in the cardiovascular system, branching of the flow occurs. The blood is pumped from the heart into arteries that subdivide into smaller arteries (arterioles) which branch into very fine vessels called capillaries. In this situation, continuity of flow is maintained but it is the sumof the flow rates in each of the branches in any portion along the tube that is maintained. The equation of continuity in a more general form becomes

$$
n _ { 1 } A _ { 1 } \overline { { { v } } } _ { 1 } = n _ { 2 } A _ { 2 } \overline { { { v } } } _ { 2 } ,
$$

where $n _ { 1 }$ and $n _ { 2 }$ are the number of branches in each of the sections along the tube.

# EXAMPLE 12.3

# Calculating Flow Speed and Vessel Diameter: Branching in the Cardiovascular System

The aorta is the principal blood vessel through which blood leaves the heart in order to circulate around the body. (a) Calculate the average speed of the blood in the aorta if the flow rate is $5 . 0 \ L / \mathsf { m i n }$ . The aorta has a radius of $1 0 \mathsf { m m }$ . (b) Blood also flows through smaller blood vessels known as capillaries. When the rate of blood flow in the aorta is

$5 . 0 \ L / \mathsf { m i n }$ , the speed of blood in the capillaries is about $0 . 3 3 ~ \mathrm { m m / s }$ . Given that the average diameter of a capillary is $8 . 0 \mu \mathrm { m }$ , calculate the number of capillaries in the blood circulatory system.

# Strategy

We can use $Q = A { \overline { { v } } }$ to calculate the speed of flow in the aorta and then use the general form of the equation of continuity to calculate the number of capillaries as all of the other variables are known.

# Solution for (a)

The flow rate is given by $Q = A { \overline { { v } } }$ or $\begin{array} { r } { \overline { { v } } = \frac { Q } { \pi r ^ { 2 } } } \end{array}$ for a cylindrical vessel.

Substituting the known values (converted to units of meters and seconds) gives

$$
\overline { { v } } = \frac { ( 5 . 0 \mathrm { L } / \mathrm { m i n } ) \left( 1 0 ^ { - 3 } \mathrm { ~ m } ^ { 3 } / \mathrm { L } \right) ( 1 \mathrm { ~ m i n } / 6 0 \mathrm { ~ s } ) } { \pi ( 0 . 0 1 0 \mathrm { ~ m } ) ^ { 2 } } = 0 . 2 7 \mathrm { ~ m } / \mathrm { s } .
$$

# Solution for (b)

Using $n _ { 1 } A _ { 1 } \overline { { v } } _ { 1 } = n _ { 2 } A _ { 2 } \overline { { v } } _ { 1 }$ , assigning the subscript 1 to the aorta and 2 to the capillaries, and solving for $n _ { 2 }$ (the number of capillaries) gives . Converting all quantities to units of meters and seconds and substituting into the equation above gives

$$
n _ { 2 } = { \frac { ( 1 ) ( \pi ) { \bigl ( } 1 0 \times 1 0 ^ { - 3 } ~ \mathrm { m } { \bigr ) } ^ { 2 } ( 0 . 2 7 ~ \mathrm { m / s } ) } { ( \pi ) { \bigl ( } 4 . 0 \times 1 0 ^ { - 6 } ~ \mathrm { m } { \bigr ) } ^ { 2 } { \bigl ( } 0 . 3 3 \times 1 0 ^ { - 3 } ~ \mathrm { m / s } { \bigr ) } } } = 5 . 0 \times 1 0 ^ { 9 } ~ \mathrm { c a p i l l a r i e s } .
$$

# Discussion

Note that the speed of flow in the capillaries is considerably reduced relative to the speed in the aorta due to the significant increase in the total cross-sectional area at the capillaries. This low speed is to allow sufficient time for effective exchange to occur although it is equally important for the flow not to become stationary in order to avoid the possibility of clotting. Does this large number of capillaries in the body seem reasonable? In active muscle, one finds about 200 capillaries per $\mathrm { m m } ^ { 3 }$ , or about $2 0 0 \times 1 0 ^ { 6 }$ per $1 \kappa \theta$ of muscle. For $2 0 ~ \mathsf { k g }$ of muscle, this amounts to about $4 \times 1 0 ^ { 9 }$ capillaries.