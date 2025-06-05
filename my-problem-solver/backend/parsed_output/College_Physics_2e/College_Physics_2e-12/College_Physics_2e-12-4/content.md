# 12.4 Viscosity and Laminar Flow; Poiseuille’s Law

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

Define laminar flow and turbulent flow. • Explain what viscosity is. • Calculate flow and resistance with Poiseuille’s law. • Explain how pressure drops due to resistance.

# Laminar Flow and Viscosity

When you pour yourself a glass of juice, the liquid flows freely and quickly. But when you pour syrup on your pancakes, that liquid flows slowly and sticks to the pitcher. The difference is fluid friction, both within the fluid itself and between the fluid and its surroundings. We call this property of fluids viscosity. Juice has low viscosity, whereas syrup has high viscosity. In the previous sections we have considered ideal fluids with little or no viscosity. In this section, we will investigate what factors, including viscosity, affect the rate of fluid flow.



The precise definition of viscosity is based on laminar, or nonturbulent, flow. Before we can define viscosity, then, we need to define laminar flow and turbulent flow. Figure 12.10 shows both types of flow. Laminar flow is characterized by the smooth flow of the fluid in layers that do not mix. Turbulent flow, or turbulence, is characterized by eddies and swirls that mix layers of fluid together.

Figure 12.11 shows schematically how laminar and turbulent flow differ. Layers flow without mixing when flow is laminar. When there is turbulence, the layers mix, and there are significant velocities in directions other than the overall direction of flow. The lines that are shown in many illustrations are the paths followed by small volumes of fluids. These are called streamlines. Streamlines are smooth and continuous when flow is laminar, but break up and mix when flow is turbulent. Turbulence has two main causes. First, any obstruction or sharp corner, such as in a faucet, creates turbulence by imparting velocities perpendicular to the flow. Second, high speeds cause turbulence. The drag both between adjacent layers of fluid and between the fluid and its surroundings forms swirls and eddies, if the speed is great enough. We shall concentrate on laminar flow for the remainder of this section, leaving certain aspects of turbulence for later sections.

# Making Connections: Take-Home Experiment: Go Down to the River

Try dropping simultaneously two sticks into a flowing river, one near the edge of the river and one near the middle. Which one travels faster? Why?

Figure 12.12 shows how viscosity is measured for a fluid. Two parallel plates have the specific fluid between them. The bottom plate is held fixed, while the top plate is moved to the right, dragging fluid with it. The layer (or lamina) of fluid in contact with either plate does not move relative to the plate, and so the top layer moves at $v$ while the bottom layer remains at rest. Each successive layer from the top down exerts a force on the one below it, trying to drag it along, producing a continuous variation in speed from $v$ to 0 as shown. Care is taken to insure that the flow is laminar; that is, the layers do not mix. The motion in Figure 12.12 is like a continuous shearing motion. Fluids have zero shear strength, but the rateat which they are sheared is related to the same geometrical factors $A$ and $L$ as is shear deformation for solids.

A force $F$ is required to keep the top plate in Figure 12.12 moving at a constant velocity $v$ , and experiments have shown that this force depends on four factors. First, $F$ is directly proportional to $v$ (until the speed is so high that turbulence occurs—then a much larger force is needed, and it has a more complicated dependence on $v$ ). Second, $F$ is proportional to the area $A$ of the plate. This relationship seems reasonable, since $A$ is directly proportional to the amount of fluid being moved. Third, $F$ is inversely proportional to the distance between the plates $L$ . This relationship is also reasonable; $L$ is like a lever arm, and the greater the lever arm, the less force that is needed. Fourth, $F$ is directly proportional to thecoeficientofviscosity, $\eta$ . The greater the viscosity, the greater the force required. These dependencies are combined into the equation

$$
F = \eta \frac { v A } { L } ,
$$

which gives us a working definition of fluid viscosity $\eta$ . Solving for $\eta$ gives

$$
\eta = \frac { F L } { v A } ,
$$

which defines viscosity in terms of how it is measured. The SI unit of viscosity is $\mathbf { N } \cdot \mathbf { m } / [ ( \mathbf { m } / \mathrm { s } ) \mathbf { m } ^ { 2 } ] { = } ( \mathbf { N } / \mathbf { m } ^ { 2 } ) \mathrm { s }$ or $\mathrm { \ P a \cdot s . }$ Table 12.1 lists the coefficients of viscosity for various fluids.

Viscosity varies from one fluid to another by several orders of magnitude. As you might expect, the viscosities of gases are much less than those of liquids, and these viscosities are often temperature dependent. The viscosity of blood can be reduced by aspirin consumption, allowing it to flow more easily around the body. (When used over the long term in low doses, aspirin can help prevent heart attacks, and reduce the risk of blood clotting.)

# Laminar Flow Confined to Tubes—Poiseuille’s Law

What causes flow? The answer, not surprisingly, is pressure difference. In fact, there is a very simple relationship between horizontal flow and pressure. Flow rate $Q$ is in the direction from high to low pressure. The greater the pressure differential between two points, the greater the flow rate. This relationship can be stated as

$$
Q = \frac { P _ { 2 } - P _ { 1 } } { R } ,
$$

where $P _ { 1 }$ and $P _ { 2 }$ are the pressures at two points, such as at either end of a tube, and $R$ is the resistance to flow. The resistance $R$ includes everything, except pressure, that affects flow rate. For example, $R$ is greater for a long tube than for a short one. The greater the viscosity of a fluid, the greater the value of $R$ . Turbulence greatly increases $R$ , whereas increasing the diameter of a tube decreases $R$ .

If viscosity is zero, the fluid is frictionless and the resistance to flow is also zero. Comparing frictionless flow in a tube to viscous flow, as in Figure 12.13, we see that for a viscous fluid, speed is greatest at midstream because of drag at the boundaries. We can see the effect of viscosity in a Bunsen burner flame, even though the viscosity of natural gas is small.

The resistance $R$ to laminar flow of an incompressible fluid having viscosity $\eta$ through a horizontal tube of uniform radius $r$ and length $l$ , such as the one in Figure 12.14, is given by

$$
R = \frac { 8 \eta l } { \pi r ^ { 4 } } .
$$

This equation is called Poiseuille’s law for resistance after the French scientist J. L. Poiseuille (1799–1869), who derived it in an attempt to understand the flow of blood, an often turbulent fluid.

Let us examine Poiseuille’s expression for $R$ to see if it makes good intuitive sense. We see that resistance is directly proportional to both fluid viscosity $\eta$ and the length $l$ of a tube. After all, both of these directly affect the amount of friction encountered—the greater either is, the greater the resistance and the smaller the flow. The radius $r$ of a tube affects the resistance, which again makes sense, because the greater the radius, the greater the flow (all other factors remaining the same). But it is surprising that $r$ is raised to the fourthpower in Poiseuille’s law. This exponent means that any change in the radius of a tube has a very large effect on resistance. For example, doubling the radius of a tube decreases resistance by a factor of $2 ^ { 4 } = 1 6$ .

Taken together, $Q = \frac { P _ { 2 } - P _ { 1 } } { R }$ and $\begin{array} { r } { R = \frac { 8 \eta l } { \pi r ^ { 4 } } } \end{array}$ give the following expression for flow rate:

$$
Q = \frac { ( P _ { 2 } - P _ { 1 } ) \pi r ^ { 4 } } { 8 \eta l } .
$$

This equation describes laminar flow through a tube. It is sometimes called Poiseuille’s law for laminar flow, or simply Poiseuille’s law.

# EXAMPLE 12.7

# Using Flow Rate: Plaque Deposits Reduce Blood Flow

Suppose the flow rate of blood in a coronary artery has been reduced to half its normal value by plaque deposits. By what factor has the radius of the artery been reduced, assuming no turbulence occurs?

# Strategy

Assuming laminar flow, Poiseuille’s law states that

$$
Q = \frac { ( P _ { 2 } - P _ { 1 } ) \pi r ^ { 4 } } { 8 \eta l } .
$$

We need to compare the artery radius before and after the flow rate reduction.

# Solution

With a constant pressure difference assumed and the same length and viscosity, along the artery we have

$$
\frac { Q _ { 1 } } { r _ { 1 } ^ { 4 } } = \frac { Q _ { 2 } } { r _ { 2 } ^ { 4 } } .
$$

So, given that $Q _ { 2 } = 0 . 5 Q _ { 1 }$ , we find that $r _ { 2 } ^ { 4 } = 0 . 5 r _ { 1 } ^ { 4 }$ .

Therefore, $r _ { 2 } = ( 0 . 5 ) ^ { 0 . 2 5 } r _ { 1 } = 0 . 8 4 1 r _ { 1 }$ , a decrease in the artery radius of $1 6 \%$

# Discussion

This decrease in radius is surprisingly small for this situation. To restore the blood flow in spite of this buildup would require an increase in the pressure difference $( P _ { 2 } - P _ { 1 } )$ of a factor of two, with subsequent strain on the heart.

The circulatory system provides many examples of Poiseuille’s law in action—with blood flow regulated by changes in vessel size and blood pressure. Blood vessels are not rigid but elastic. Adjustments to blood flow are primarily made by varying the size of the vessels, since the resistance is so sensitive to the radius. During vigorous exercise, blood vessels are selectively dilated to important muscles and organs and blood pressure increases. This creates both greater overall blood flow and increased flow to specific areas. Conversely, decreases in vessel radii, perhaps from plaques in the arteries, can greatly reduce blood flow. If a vessel’s radius is reduced by only $5 \%$ (to 0.95 of its original value), the flow rate is reduced to about $( 0 . 9 5 ) ^ { 4 } { = } 0 . 8 1$ of its original value. A $1 9 \%$ decrease in flow is caused by a $5 \%$ decrease in radius. The body may compensate by increasing blood pressure by $1 9 \%$ , but this presents hazards to the heart and any vessel that has weakened walls. Another example comes from automobile engine oil. If you have a car with an oil pressure gauge, you may notice that oil pressure is high when the engine is cold. Motor oil has greater viscosity when cold than when warm, and so pressure must be greater to pump the same amount of cold oil.



# EXAMPLE 12.8

# What Pressure Produces This Flow Rate?

An intravenous (IV) system is supplying saline solution to a patient at the rate of $0 . 1 2 0 \mathrm { c m } ^ { 3 } / \mathrm { s }$ through a needle of radius $0 . 1 5 0 \mathrm { m m }$ and length $2 . 5 0 \mathsf { c m }$ . What pressure is needed at the entrance of the needle to cause this flow, assuming the viscosity of the saline solution to be the same as that of water? The gauge pressure of the blood in the patient’s vein is $8 . 0 0 \mathsf { m m } \mathsf { H g }$ . (Assume that the temperature is $2 0 ^ { \circ } \mathrm { C }$ .)

# Strategy

Assuming laminar flow, Poiseuille’s law applies. This is given by

$$
Q = \frac { ( P _ { 2 } - P _ { 1 } ) \pi r ^ { 4 } } { 8 \eta l } ,
$$

where $P _ { 2 }$ is the pressure at the entrance of the needle and $P _ { 1 }$ is the pressure in the vein. The only unknown is $P _ { 2 }$ .

# Solution

Solving for $P _ { 2 }$ yields

$$
{ \cal P } _ { 2 } = \frac { 8 \eta l } { \pi r ^ { 4 } } Q + { \cal P } _ { 1 . }
$$

$P _ { 1 }$ is given as $8 . 0 0 \mathsf { m m } \mathsf { H g }$ , which converts to $1 . 0 6 6 \times 1 0 ^ { 3 } \ \mathrm { N } / \mathrm { m } ^ { 2 }$ . Substituting this and the other known values yields

$$
\begin{array} { r c l } { P _ { 2 } } & { = } & { \left[ { \frac { 8 ( 1 . 0 0 \times 1 0 ^ { - 3 } ~ \mathrm { N } \cdot \mathrm { s } / \mathrm { m } ^ { 2 } ) ( 2 . 5 0 \times 1 0 ^ { - 2 } ~ \mathrm { m } ) } { \pi ( 0 . 1 5 0 \times 1 0 ^ { - 3 } ~ \mathrm { m } ) ^ { 4 } } } \right] ( 1 . 2 0 \times 1 0 ^ { - 7 } ~ \mathrm { m } ^ { 3 } / \mathrm { s } ) + 1 . 0 6 6 \times 1 0 ^ { 3 } ~ \mathrm { N } / \mathrm { m } ^ { 2 } } \\ & { = } & { 1 . 6 2 \times 1 0 ^ { 4 } ~ \mathrm { N } / \mathrm { m } ^ { 2 } . } \end{array}
$$

# Discussion

This pressure could be supplied by an IV bottle with the surface of the saline solution $\mathtt { 1 . 6 1 m }$ above the entrance to the needle (this is left for you to solve in this chapter’s Problems and Exercises), assuming that there is negligible pressure drop in the tubing leading to the needle.

# Flow and Resistance as Causes of Pressure Drops

You may have noticed that water pressure in your home might be lower than normal on hot summer days when there is more use. This pressure drop occurs in the water main before it reaches your home. Let us consider flow through the water main as illustrated in Figure 12.15. We can understand why the pressure $P _ { 1 }$ to the home drops during times of heavy use by rearranging

$$
Q = \frac { P _ { 2 } - P _ { 1 } } { R }
$$

to

$$
P _ { 2 } - P _ { 1 } = R Q ,
$$

where, in this case, $P _ { 2 }$ is the pressure at the water works and $R$ is the resistance of the water main. During times of heavy use, the flow rate $Q$ is large. This means that $P _ { 2 } - P _ { 1 }$ must also be large. Thus $P _ { 1 }$ must decrease. It is correct to think of flow and resistance as causing the pressure to drop from $P _ { 2 }$ to $P _ { 1 } . P _ { 2 } - P _ { 1 } = R Q$ is valid for both laminar and turbulent flows.

We can use $P _ { 2 } - P _ { 1 } = R Q$ to analyze pressure drops occurring in more complex systems in which the tube radius is not the same everywhere. Resistance will be much greater in narrow places, such as an obstructed coronary artery. For a given flow rate $Q$ , the pressure drop will be greatest where the tube is most narrow. This is how water faucets control flow. Additionally, $R$ is greatly increased by turbulence, and a constriction that creates turbulence greatly reduces the pressure downstream. Plaque in an artery reduces pressure and hence flow, both by its resistance and by the turbulence it creates.

Figure 12.16 is a schematic of the human circulatory system, showing average blood pressures in its major parts for an adult at rest. Pressure created by the heart’s two pumps, the right and left ventricles, is reduced by the resistance of the blood vessels as the blood flows through them. The left ventricle increases arterial blood pressure that drives the flow of blood through all parts of the body except the lungs. The right ventricle receives the lower pressure blood from two major veins and pumps it through the lungs for gas exchange with atmospheric gases – the disposal of carbon dioxide from the blood and the replenishment of oxygen. Only one major organ is shown schematically, with typical branching of arteries to ever smaller vessels, the smallest of which are the capillaries, and rejoining of small veins into larger ones. Similar branching takes place in a variety of organs in the body, and the circulatory system has considerable flexibility in flow regulation to these organs by the dilation and constriction of the arteries leading to them and the capillaries within them. The sensitivity of flow to tube radius makes this flexibility possible over a large range of flow rates.

Each branching of larger vessels into smaller vessels increases the total cross-sectional area of the tubes through which the blood flows. For example, an artery with a cross section of $1 \mathrm { c m } ^ { 2 }$ may branch into 20 smaller arteries, each with cross sections of $0 . 5 \mathrm { c m } ^ { 2 }$ , with a total of $1 0 \mathrm { c m } ^ { 2 }$ . In that manner, the resistance of the branchings is reduced so that pressure is not entirely lost. Moreover, because $Q = A { \overline { { v } } }$ and $A$ increases through branching, the average velocity of the blood in the smaller vessels is reduced. The blood velocity in the aorta ( $= 1$ ) is about $2 5 \mathsf { c m } / \mathsf { s }$ , while in the capillaries $2 0 \mu \mathrm { m }$ in diameter) the velocity is about $\mathsf { 1 } \mathsf { m m } / \mathsf { s }$ . This reduced velocity allows the blood to exchange substances with the cells in the capillaries and alveoli in particular.