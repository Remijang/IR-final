# 12.6 Motion of an Object in a Viscous Fluid

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

Calculate the Reynolds number for an object moving through a fluid. • Explain whether the Reynolds number indicates laminar or turbulent flow. • Describe the conditions under which an object has a terminal speed.

A moving object in a viscous fluid is equivalent to a stationary object in a flowing fluid stream. (For example, when you ride a bicycle at $1 0 ~ \mathrm { m / s }$ in still air, you feel the air in your face exactly as if you were stationary in a $\mathsf { 1 0 - m } / \mathsf { s }$ wind.) Flow of the stationary fluid around a moving object may be laminar, turbulent, or a combination of the two. Just as with flow in tubes, it is possible to predict when a moving object creates turbulence. We use another form of the Reynolds number $N _ { \mathrm { R } } ^ { \prime }$ , defined for an object moving in a fluid to be

$$
N _ { \mathrm { R } } ^ { \prime } = \frac { \rho v L } { \eta } ( \mathrm { o b j e c t i n f l u i d } ) ,
$$

where $L$ is a characteristic length of the object (a sphere’s diameter, for example), $\rho$ the fluid density, $\eta$ its viscosity, and $v$ the object’s speed in the fluid. If $N _ { \mathrm { R } } ^ { \prime }$ is less than about 1, flow around the object can be laminar, particularly if the object has a smooth shape. The transition to turbulent flow occurs for $N _ { \mathrm { R } } ^ { \prime }$ between 1 and about 10, depending on surface roughness and so on. Depending on the surface, there can be a turbulentwakebehind the object with some laminar flow over its surface. For an $N _ { \mathrm { R } } ^ { \prime }$ between 10 and $1 0 ^ { 6 }$ , the flow may be either laminar or turbulent and may oscillate between the two. For $N _ { \mathrm { R } } ^ { \prime }$ greater than about $1 0 ^ { 6 }$ , the flow is entirely turbulent, even at the surface of the object. (See Figure 12.18.) Laminar flow occurs mostly when the objects in the fluid are small, such as raindrops, pollen, and blood cells in plasma.

# EXAMPLE 12.10

# Does a Ball Have a Turbulent Wake?

Calculate the Reynolds number $N _ { \mathrm { R } } ^ { \prime }$ for a ball with a 7.40-cm diameter thrown at $4 0 . 0 \ : \mathrm { m / s }$ .

# Strategy

We can use $\begin{array} { r } { N _ { \mathrm { R } } ^ { \prime } = \frac { \rho v L } { \eta } } \end{array}$ to calculate $N _ { \mathrm { R } } ^ { \prime }$ , since all values in it are either given or can be found in tables of density and viscosity.

# Solution

Substituting values into the equation for $N _ { \mathrm { R } } ^ { \prime }$ yields

$$
\begin{array} { r c l } { { N _ { R } ^ { \prime } } } & { { = } } & { { \frac { \rho v L } { \eta } = \frac { ( 1 . 2 9 \mathrm { { k g } } / \mathrm { { m } } ^ { 3 } ) ( 4 0 . 0 \mathrm { { m } } / \mathrm { { s } } ) ( 0 . 0 7 4 0 \mathrm { { m } } ) } { 1 . 8 1 \times 1 0 ^ { - 5 } \ 1 . 0 0 \mathrm { { P a } } \cdot \mathrm { { s } } } } } \\ { { } } & { { = } } & { { 2 . 1 1 \times 1 0 ^ { 5 } . } } \end{array}
$$

# Discussion

This value is sufficiently high to imply a turbulent wake. Most large objects, such as airplanes and sailboats, create significant turbulence as they move. As noted before, the Bernoulli principle gives only qualitatively-correct results in such situations.

One of the consequences of viscosity is a resistance force called viscous drag $F _ { \mathrm { V } }$ that is exerted on a moving object. This force typically depends on the object’s speed (in contrast with simple friction). Experiments have shown that for laminar flow ( $N _ { \mathrm { R } } ^ { \prime }$ less than about one) viscous drag is proportional to speed, whereas for $N _ { \mathrm { R } } ^ { \prime }$ between about 10 and $1 0 ^ { 6 }$ , viscous drag is proportional to speed squared. (This relationship is a strong dependence and is pertinent to bicycle racing, where even a small headwind causes significantly increased drag on the racer. Cyclists take turns being the leader in the pack for this reason.) For $N _ { \mathrm { R } } ^ { \prime }$ greater than $1 0 ^ { 6 }$ , drag increases dramatically and behaves with greater complexity. For laminar flow around a sphere, $F _ { \mathrm { V } }$ is proportional to fluid viscosity $\eta ,$ , the object’s characteristic size $L$ , and its speed $v$ . All of which makes sense—the more viscous the fluid and the larger the object, the more drag we expect. Recall Stoke’s law $F _ { \mathrm { S } } = 6 \pi r \eta v$ . For the special case of a small sphere of radius $R$ moving slowly in a fluid of viscosity $\eta ,$ , the drag force $F _ { \mathrm { S } }$ is given by

$$
F _ { \mathrm { S } } = 6 \pi R \eta v .
$$

An interesting consequence of the increase in $F _ { \mathrm { V } }$ with speed is that an object falling through a fluid will not continue to accelerate indefinitely (as it would if we neglect air resistance, for example). Instead, viscous drag increases, slowing acceleration, until a critical speed, called the terminal speed, is reached and the acceleration of the object becomes zero. Once this happens, the object continues to fall at constant speed (the terminal speed). This is the case for particles of sand falling in the ocean, cells falling in a centrifuge, and sky divers falling through the air. Figure 12.19 shows some of the factors that affect terminal speed. There is a viscous drag on the object that depends on the viscosity of the fluid and the size of the object. But there is also a buoyant force that depends on the density of the object relative to the fluid. Terminal speed will be greatest for low-viscosity fluids and objects with high densities and small sizes. Thus a skydiver falls more slowly with outspread limbs than when they are in a pike position—head first with hands at their side and legs together.

# Take-Home Experiment: Don’t Lose Your Marbles

By measuring the terminal speed of a slowly moving sphere in a viscous fluid, one can find the viscosity of that fluid (at that temperature). It can be difficult to find small ball bearings around the house, but a small marble will do. Gather two or three fluids (syrup, motor oil, honey, olive oil, etc.) and a thick, tall clear glass or vase. Drop the marble into the center of the fluid and time its fall (after letting it drop a little to reach its terminal speed).

Compare your values for the terminal speed and see if they are inversely proportional to the viscosities as listed in Table 12.1. Does it make a difference if the marble is dropped near the side of the glass?

Knowledge of terminal speed is useful for estimating sedimentation rates of small particles. We know from watching mud settle out of dirty water that sedimentation is usually a slow process. Centrifuges are used to speed sedimentation by creating accelerated frames in which gravitational acceleration is replaced by centripetal acceleration, which can be much greater, increasing the terminal speed.