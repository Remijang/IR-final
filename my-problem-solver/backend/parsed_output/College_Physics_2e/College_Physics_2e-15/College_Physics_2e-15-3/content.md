# 15.3 Introduction to the Second Law of Thermodynamics: Heat Engines and Their Efficiency

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

• State the expressions of the second law of thermodynamics.   
• Calculate the efficiency and carbon dioxide emission of a coal-fired electricity plant, using second law characteristics.   
• Describe and define the Otto cycle.

The second law of thermodynamics deals with the direction taken by spontaneous processes. Many processes occur spontaneously in one direction only—that is, they are irreversible, under a given set of conditions. Although irreversibility is seen in day-to-day life—a broken glass does not resume its original state, for instance—complete irreversibility is a statistical statement that cannot be seen during the lifetime of the universe. More precisely, an irreversible process is one that depends on path. If the process can go in only one direction, then the reverse path differs fundamentally and the process cannot be reversible. For example, as noted in the previous section, heat involves the transfer of energy from higher to lower temperature. A cold object in contact with a hot one never gets colder, transferring heat to the hot object and making it hotter. Furthermore, mechanical energy, such as kinetic energy, can be completely converted to thermal energy by friction, but the reverse is impossible. A hot stationary object never spontaneously cools off and starts moving. Yet another example is the expansion of a puff of gas introduced into one corner of a vacuum chamber. The gas expands to fill the chamber, but it never regroups in the corner. The random motion of the gas molecules could take them all back to the corner, but this is never observed to happen. (See Figure 15.15.)

The fact that certain processes never occur suggests that there is a law forbidding them to occur. The first law of thermodynamics would allow them to occur—none of those processes violate conservation of energy. The law that forbids these processes is called the second law of thermodynamics. We shall see that the second law can be stated in many ways that may seem different, but which in fact are equivalent. Like all natural laws, the second law of thermodynamics gives insights into nature, and its several statements imply that it is broadly applicable, fundamentally affecting many apparently disparate processes.

The already familiar direction of heat transfer from hot to cold is the basis of our first version of the second law of thermodynamics.

# The Second Law of Thermodynamics (first expression)

Heat transfer occurs spontaneously from higher- to lower-temperature bodies but never spontaneously in the reverse direction.

Another way of stating this: It is impossible for any process to have as its sole result heat transfer from a cooler to a hotter object.

# Heat Engines

Now let us consider a device that uses heat transfer to do work. As noted in the previous section, such a device is called a heat engine, and one is shown schematically in Figure 15.16(b). Gasoline and diesel engines, jet engines, and steam turbines are all heat engines that do work by using part of the heat transfer from some source. Heat transfer from the hot object (or hot reservoir) is denoted as $Q _ { \mathrm { h } }$ , while heat transfer into the cold object (or cold reservoir) is $Q _ { \mathrm { c } }$ , and the work done by the engine is $W$ . The temperatures of the hot and cold reservoirs are $T _ { \mathrm { h } }$ and $T _ { \mathrm { c } }$ , respectively.

Because the hot reservoir is heated externally, which is energy intensive, it is important that the work is done as efficiently as possible. In fact, we would like $W$ to equal $Q _ { \mathrm { h } }$ , and for there to be no heat transfer to the environment $\left( Q _ { \mathrm { c } } = 0 \right)$ ). Unfortunately, this is impossible. The second law of thermodynamics also states, with regard to using heat transfer to do work (the second expression of the second law):

# The Second Law of Thermodynamics (second expression)

It is impossible in any system for heat transfer from a reservoir to completely convert to work in a cyclical process in which the system returns to its initial state.

A cyclical process brings a system, such as the gas in a cylinder, back to its original state at the end of every cycle. Most heat engines, such as reciprocating piston engines and rotating turbines, use cyclical processes. The second law, just stated in its second form, clearly states that such engines cannot have perfect conversion of heat transfer into work done. Before going into the underlying reasons for the limits on converting heat transfer into work, we need to explore the relationships among $W$ , $Q _ { \mathrm { h } }$ , and $Q _ { \mathrm { c } }$ , and to define the efficiency of a cyclical heat engine. As noted, a cyclical process brings the system back to its original condition at the end of every cycle. Such a system’s internal energy $U$ is the same at the beginning and end of every cycle—that is, $\Delta U = 0$ . The first law of thermodynamics states that

$$
\Delta U = Q - W ,
$$

where $Q$ is the netheat transfer during the cycle $( Q = Q _ { \mathrm { h } } - Q _ { \mathrm { c } } )$ and $W$ is the net work done by the system. Since $\Delta U = 0$ for a complete cycle, we have

$$
0 = Q - W ,
$$

so that

$$
W = Q .
$$

Thus the net work done by the system equals the net heat transfer into the system, or

$$
W = Q _ { \mathrm { h } } - Q _ { \mathrm { c } } { \mathrm { ~ ( c y c l i c a l ~ p r o c e s s ) , } }
$$

just as shown schematically in Figure 15.16(b). The problem is that in all processes, there is some heat transfer $Q _ { \mathrm { c } }$ to the environment—and usually a very significant amount at that.

In the conversion of energy to work, we are always faced with the problem of getting less out than we put in. We defineconversioneficiency $E f f$ to be the ratio of useful work output to the energy input (or, in other words, the

ratio of what we get to what we spend). In that spirit, we define the efficiency of a heat engine to be its net work output $W$ divided by heat transfer to the engine $Q _ { \mathrm { h } }$ ; that is,

$$
E f f = { \frac { W } { Q _ { \mathrm { h } } } } .
$$

Since $W = Q _ { \mathrm { h } } - Q _ { \mathrm { c } }$ in a cyclical process, we can also express this as

$$
E f f = { \frac { Q _ { \mathrm { h } } - Q _ { \mathrm { c } } } { Q _ { \mathrm { h } } } } = 1 - { \frac { Q _ { \mathrm { c } } } { Q _ { \mathrm { h } } } } \mathrm { ( c y c l i c a l p r o c e s s ) } ,
$$

making it clear that an efficiency of 1, or $100 \%$ , is possible only if there is no heat transfer to the environment $( Q _ { \mathrm { c } } = 0 )$ . Note that all $Q \mathsf { s }$ are positive. The direction of heat transfer is indicated by a plus or minus sign. For example, $Q _ { \mathrm { c } }$ is out of the system and so is preceded by a minus sign.

# EXAMPLE 15.3

# Daily Work Done by a Coal-Fired Power Station, Its Efficiency and Carbon Dioxide Emissions

A coal-fired power station is a huge heat engine. It uses heat transfer from burning coal to do work to turn turbines, which are used to generate electricity. In a single day, a large coal power station has $2 . 5 0 \times 1 0 ^ { 1 4 }$ of heat transfer from coal and $1 . 4 8 \times 1 0 ^ { 1 4 }$ of heat transfer into the environment. (a) What is the work done by the power station? (b) What is the efficiency of the power station? (c) In the combustion process, the following chemical reaction occurs: $\mathrm { C } + \mathrm { O } _ { 2 } \to \mathrm { C O } _ { 2 }$ . This implies that every $1 2 \ k \varrho$ of coal puts $1 2 \mathrm { k g } + 1 6 \mathrm { k g } + 1 6 \mathrm { k g } = 4 4 \mathrm { k g }$ of carbon dioxide into the atmosphere. Assuming that $1 \kappa \theta$ of coal can provide $2 . 5 \times 1 0 ^ { 6 }$ of heat transfer upon combustion, how much $\mathrm { C O } _ { 2 }$ is emitted per day by this power plant?

# Strategy for (a)

We can use $W = Q _ { \mathrm { h } } - Q _ { \mathrm { c } }$ to find the work output $W$ , assuming a cyclical process is used in the power station. In this process, water is boiled under pressure to form high-temperature steam, which is used to run steam turbinegenerators, and then condensed back to water to start the cycle again.

# Solution for (a)

Work output is given by:

$$
{ \cal W } = { \cal Q } _ { \mathrm { h } } - { \cal Q } _ { \mathrm { c } } .
$$

Substituting the given values:

$$
\begin{array} { r c l } { { W } } & { { = } } & { { 2 . 5 0 { \times } 1 0 ^ { 1 4 } \mathrm { J } - 1 . 4 8 { \times } 1 0 ^ { 1 4 } \mathrm { J } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { 1 . 0 2 \times 1 0 ^ { 1 4 } \mathrm { J } . } } \end{array}
$$

# Strategy for (b)

The efficiency can be calculated with $\begin{array} { r } { E f f = \frac { W } { Q _ { \mathrm { h } } } } \end{array}$ since $Q _ { \mathrm { h } }$ is given and work $W$ was found in the first part of this example.

# Solution for (b)

Efficiency is given by: $\begin{array} { r } { E f f = \frac { W } { Q _ { \mathrm { h } } } } \end{array}$ . The work $W$ was just found to be $1 . 0 2 \times 1 0 ^ { 1 4 } \mathrm { ~ J }$ , and $Q _ { \mathrm { h } }$ is given, so the efficiency is

$$
\begin{array} { r c l } { E f f } & { = } & { \frac { 1 . 0 2 \times 1 0 ^ { 1 4 } \mathrm { ~ J } } { 2 . 5 0 \times 1 0 ^ { 1 4 } \mathrm { ~ J } } } \\ & { = } & { 0 . 4 0 8 , \mathrm { o r } 4 0 . 8 \% } \end{array}
$$

# Strategy for (c)

The daily consumption of coal is calculated using the information that each day there is $2 . 5 0 x 1 0 ^ { 1 4 }$ of heat transfer from coal. In the combustion process, we have $\mathrm { C } + \mathrm { O } _ { 2 } \to \mathrm { C O } _ { 2 }$ . So every $1 2 \ k \varrho$ of coal puts $1 2 ~ \mathsf { k g } + 1 6 ~ \mathsf { k g } + 1 6$ ${ \mathsf { k g } } = 4 4 { \mathsf { k g } }$ of $\mathrm { C O } _ { 2 }$ into the atmosphere.

# Solution for (c)

The daily coal consumption is

$$
{ \frac { 2 . 5 0 \times 1 0 ^ { 1 4 } ~ { \mathrm { J } } } { 2 . 5 0 \times 1 0 ^ { 6 } ~ { \mathrm { J / k g } } } } = 1 . 0 \times 1 0 ^ { 8 } ~ { \mathrm { k g } } .
$$

Assuming that the coal is pure and that all the coal goes toward producing carbon dioxide, the carbon dioxide produced per day is

$$
1 . 0 \times 1 0 ^ { 8 } \ \mathrm { k g } \ \mathrm { c o a l } \times \frac { 4 4 \ \mathrm { k g } \mathrm { C O } _ { 2 } } { 1 2 \ \mathrm { k g } \ \mathrm { c o a l } } = 3 . 7 \times 1 0 ^ { 8 } \ \mathrm { k g } \ \mathrm { C O } _ { 2 } .
$$

This is 370,000 metric tons of $\mathrm { C O } _ { 2 }$ produced every day.

# Discussion

If all the work output is converted to electricity in a period of one day, the average power output is 1180 MW (this is left to you as an end-of-chapter problem). This value is about the size of a large-scale conventional power plant. The efficiency found is acceptably close to the value of $4 2 \%$ given for coal power stations. It means that fully $5 9 . 2 \%$ of the energy is heat transfer to the environment, which usually results in warming lakes, rivers, or the ocean near the power station, and is implicated in a warming planet generally. While the laws of thermodynamics limit the efficiency of such plants—including plants fired by nuclear fuel, oil, and natural gas—the heat transfer to the environment could be, and sometimes is, used for heating homes or for industrial processes. The generally low cost of energy has not made it economical to make better use of the waste heat transfer from most heat engines. Coalfired power plants produce the greatest amount of $\mathrm { C O } _ { 2 }$ per unit energy output (compared to natural gas or oil), making coal the least efficient fossil fuel.

With the information given in Example $\underline { { 1 5 . 3 } }$ , we can find characteristics such as the efficiency of a heat engine without any knowledge of how the heat engine operates, but looking further into the mechanism of the engine will give us greater insight. Figure 15.17 illustrates the operation of the common four-stroke gasoline engine. The four steps shown complete this heat engine’s cycle, bringing the gasoline-air mixture back to its original condition.

The Otto cycle shown in Figure 15.18(a) is used in four-stroke internal combustion engines, although in fact the true Otto cycle paths do not correspond exactly to the strokes of the engine.

The adiabatic process AB corresponds to the nearly adiabatic compression stroke of the gasoline engine. In both cases, work is done on the system (the gas mixture in the cylinder), increasing its temperature and pressure. Along path BC of the Otto cycle, heat transfer $Q _ { \mathrm { h } }$ into the gas occurs at constant volume, causing a further increase in pressure and temperature. This process corresponds to burning fuel in an internal combustion engine, and takes place so rapidly that the volume is nearly constant. Path CD in the Otto cycle is an adiabatic expansion that does work on the outside world, just as the power stroke of an internal combustion engine does in its nearly adiabatic expansion. The work done by the system along path CD is greater than the work done on the system along path AB, because the pressure is greater, and so there is a net work output. Along path DA in the Otto cycle, heat transfer $Q _ { \mathrm { c } }$ from the gas at constant volume reduces its temperature and pressure, returning it to its original state. In an internal combustion engine, this process corresponds to the exhaust of hot gases and the intake of an air-gasoline mixture at a considerably lower temperature. In both cases, heat transfer into the environment occurs along this final path.

The net work done by a cyclical process is the area inside the closed path on a diagram, such as that inside path ABCDA in Figure 15.18. Note that in every imaginable cyclical process, it is absolutely necessary for heat transfer from the system to occur in order to get a net work output. In the Otto cycle, heat transfer occurs along path DA. If no heat transfer occurs, then the return path is the same, and the net work output is zero. The lower the temperature on the path AB, the less work has to be done to compress the gas. The area inside the closed path is then greater, and so the engine does more work and is thus more efficient. Similarly, the higher the temperature along path CD, the more work output there is. (See Figure 15.19.) So efficiency is related to the temperatures of the hot and cold reservoirs. In the next section, we shall see what the absolute limit to the efficiency of a heat engine is, and how it is related to temperature.