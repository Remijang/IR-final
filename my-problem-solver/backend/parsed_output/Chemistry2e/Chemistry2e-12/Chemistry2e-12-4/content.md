# 12.4 Integrated Rate Laws

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

Explain the form and function of an integrated rate law   
Perform integrated rate law calculations for zero-, first-, and second-order reactions   
• Define half-life and carry out related calculations   
• Identify the order of a reaction from concentration/time data

The rate laws discussed thus far relate the rate and the concentrations of reactants. We can also determine a second form of each rate law that relates the concentrations of reactants and time. These are called integrated rate laws. We can use an integrated rate law to determine the amount of reactant or product present after a period of time or to estimate the time required for a reaction to proceed to a certain extent. For example, an integrated rate law is used to determine the length of time a radioactive material must be stored for its radioactivity to decay to a safe level.

Using calculus, the differential rate law for a chemical reaction can be integrated with respect to time to give an equation that relates the amount of reactant or product present in a reaction mixture to the elapsed time of the reaction. This process can either be very straightforward or very complex, depending on the complexity of the differential rate law. For purposes of discussion, we will focus on the resulting integrated rate laws for first, second-, and zero-order reactions.

# First-Order Reactions

Integration of the rate law for a simple first-order reaction (rate $= k [ A ] )$ results in an equation describing how the reactant concentration varies with time:

$$
[ A ] _ { t } = [ A ] _ { 0 } e ^ { - k t }
$$

where $[ A ] t$ is the concentration of $A$ at any time t, $[ A ] _ { 0 }$ is the initial concentration of $A$ , and $k$ is the first-order rate constant.

For mathematical convenience, this equation may be rearranged to other formats, including direct and indirect proportionalities:

$$
\ln \left( { \frac { [ A ] _ { t } } { [ A ] _ { 0 } } } \right) = - k t \qquad { \mathrm { o r } } \qquad \ln \left( { \frac { [ A ] _ { 0 } } { [ A ] _ { t } } } \right) = k t
$$

and a format showing a linear dependence of concentration in time:

$$
\ln [ A ] _ { t } = \ln [ A ] _ { 0 } - k t
$$

# EXAMPLE 12.6

# The Integrated Rate Law for a First-Order Reaction

The rate constant for the first-order decomposition of cyclobutane, $\mathrm { C _ { 4 } H _ { 8 } }$ at $5 0 0 ^ { \circ } \mathrm { C }$ is $9 . 2 \times 1 0 ^ { - 3 } \mathrm { { s ^ { - 1 } } }$ :

$$
\mathrm { C } _ { 4 } \mathrm { H } _ { 8 } \longrightarrow 2 \mathrm { C } _ { 2 } \mathrm { H } _ { 4 }
$$

How long will it take for $8 0 . 0 \%$ of a sample of $\mathrm { C _ { 4 } H _ { 8 } }$ to decompose?

# Solution

Since the relative change in reactant concentration is provided, a convenient format for the integrated rate law is:

$$
\ln \left( { \frac { [ A ] _ { 0 } } { [ A ] _ { t } } } \right) = k t
$$

The initial concentration of $\mathrm { C _ { 4 } H _ { 8 } }$ , $[ A ] _ { 0 }$ , is not provided, but the provision that $8 0 . 0 \%$ of the sample has decomposed is enough information to solve this problem. Let $\scriptstyle { \boldsymbol { X } }$ be the initial concentration, in which case the concentration after $8 0 . 0 \%$ decomposition is $2 0 . 0 \%$ of $X \operatorname { o r } 0 . 2 0 0 X .$ .Rearranging the rate law to isolate $t$ and substituting the provided quantities yields:

$$
{ \begin{array} { r l } { t } & { = \ln { \frac { [ x ] } { [ 0 . 2 0 0 x ] } } \ \times \ { \frac { 1 } { k } } } \\ & { = \ln 5 \ \times \ { \frac { 1 } { 9 . 2 \times 1 0 ^ { - 3 } \mathrm { { s ^ { - 1 } } } } } } \\ & { = 1 . 6 0 9 \ \times \ { \frac { 1 } { 9 . 2 \times 1 0 ^ { - 3 } { \mathrm { s ^ { - 1 } } } } } } \\ & { = 1 . 7 \times 1 0 ^ { 2 } \ \mathrm { { s } } } \end{array} }
$$

# Check Your Learning

Iodine-131 is a radioactive isotope that is used to diagnose and treat some forms of thyroid cancer. Iodine-131 decays to xenon-131 according to the equation:

$$
\mathrm { I } { - } 1 3 1 \longrightarrow \mathrm { X e } { - } 1 3 1 + \mathrm { e l e c t r o n }
$$

The decay is first-order with a rate constant of $0 . 1 3 8 { \mathrm { d } } ^ { - 1 }$ . How many days will it take for $90 \%$ of the iodine−131 in a 0.500 Msolution of this substance to decay to Xe-131?

Answer: 16.7 days

In the next example exercise, a linear format for the integrated rate law will be convenient:

$$
\begin{array} { r c l } { \ln [ A ] _ { t } } & { = } & { ( - k ) ( t ) + \ln [ A ] _ { 0 } } \\ { y } & { = } & { m x + b } \end{array}
$$

A plot of $\ln [ A ] _ { t }$ versus $t$ for a first-order reaction is a straight line with a slope of $- k$ and a $y$ -intercept of $\mathrm { l n } [ A ] _ { 0 }$ . If a set of rate data are plotted in this fashion but do notresult in a straight line, the reaction is not first order in $A$ .

# EXAMPLE 12.7

# Graphical Determination of Reaction Order and Rate Constant

Show that the data in Figure 12.2 can be represented by a first-order rate law by graphing $\mathrm { { l n } [ \mathrm { { H _ { 2 } } \mathrm { { O _ { 2 } } ] } } }$ versus time Determine the rate constant for the decomposition of $\mathrm { H } _ { 2 } \mathrm { O } _ { 2 }$ from these data.

# Solution

The plot of $\mathrm { { l n } [ \mathrm { { H _ { 2 } } \mathrm { { O _ { 2 } } ] } } }$ versus time is linear, indicating that the reaction may be described by a first-order rate law.

According to the linear format of the first-order integrated rate law, the rate constant is given by the negative of this plot’s slope.

$$
{ \mathrm { s l o p e } } = { \frac { { \mathrm { c h a n g e ~ i n ~ } } y } { { \mathrm { c h a n g e ~ i n ~ } } x } } = { \frac { \Delta y } { \Delta x } } = { \frac { \Delta \ln \left[ { \mathrm { H } } _ { 2 } { \mathrm { O } } _ { 2 } \right] } { \Delta t } }
$$

The slope of this line may be derived from two values of $\mathrm { { l n } [ \mathrm { { H _ { 2 } } \mathrm { { O _ { 2 } } ] } } }$ at different values of $t$ (one near each end of the line is preferable). For example, the value of $\mathrm { { l n } [ \mathrm { { H _ { 2 } } \mathrm { { O _ { 2 } } ] } } }$ when $t$ is $0 . 0 0 \mathrm { { h } }$ is 0.000; the value when $t = 2 4 . 0 0 \mathrm { h }$ is −2.772

$$
{ \begin{array} { r c l } { { \mathrm { s l o p e } } } & { = } & { { \frac { - 2 . 7 7 2 - 0 . 0 0 0 } { 2 4 . 0 0 - 0 . 0 0 ~ \mathrm { h } } } } \\ & { = } & { { \frac { - 2 . 7 7 2 } { 2 4 . 0 0 ~ \mathrm { h } } } } \\ & { = } & { - 0 . 1 1 6 { \mathrm { h } } ^ { - 1 } } \\ { k } & { = } & { { \mathrm { - s l o p e } } = - \left( - 0 . 1 1 6 { \mathrm { h } } ^ { - 1 } \right) = 0 . 1 1 6 { \mathrm { h } } ^ { - 1 } } \end{array} }
$$

# Check Your Learning

Graph the following data to determine whether the reaction $A \longrightarrow B + C$ is first order.

# Answer:

The plot of $\mathrm { l n } [ A ] _ { t }$ vs. tis not linear, indicating the reaction is not first order:

# Second-Order Reactions

The equations that relate the concentrations of reactants and the rate constant of second-order reactions can be fairly complicated. To illustrate the point with minimal complexity, only the simplest second-order reactions will be described here, namely, those whose rates depend on the concentration of just one reactant. For these types of reactions, the differential rate law is written as:

$$
\mathrm { r a t e } = k [ A ] ^ { 2 }
$$

For these second-order reactions, the integrated rate law is:

$$
{ \frac { 1 } { [ A ] _ { t } } } = k t + { \frac { 1 } { [ A ] _ { 0 } } }
$$

where the terms in the equation have their usual meanings as defined earlier.

# EXAMPLE 12.8

# The Integrated Rate Law for a Second-Order Reaction

The reaction of butadiene gas $( \mathrm { C } _ { 4 } \mathrm { H } _ { 6 } )$ to yield $\mathrm { C } _ { 8 } \mathrm { H } _ { 1 2 }$ gas is described by the equation:

$$
2 \mathrm { C } _ { 4 } \mathrm { H } _ { 6 } ( g ) \longrightarrow \mathrm { C } _ { 8 } \mathrm { H } _ { 1 2 } ( g )
$$

This “dimerization” reaction is second order with a rate constant equal to $5 . 7 6 \times 1 0 ^ { - 2 } \mathrm { L } \mathrm { m o l } ^ { - 1 } \mathrm { m i n } ^ { - 1 }$ under certain conditions. If the initial concentration of butadiene is $0 . 2 0 0 M ,$ , what is the concentration after 10.0 min?

# Solution

For a second-order reaction, the integrated rate law is written

$$
{ \frac { 1 } { [ A ] _ { t } } } = k t + { \frac { 1 } { [ A ] _ { 0 } } }
$$

We know three variables in this equation: $[ A ] _ { 0 } = 0 . 2 0 0 \mathrm { m o l / L } , k = 5 . 7 6 \times 1 0 ^ { - 2 } \mathrm { L / m o l / m i n }$ , and $t = 1 0 . 0$ min. Therefore, we can solve for [A], the fourth variable:

$$
{ \begin{array} { l c l } { { \frac { 1 } { \left[ A \right] _ { t } } } } & { = } & { \left( 5 . 7 6 \times 1 0 ^ { - 2 } { \mathrm { L } } { \mathrm { m o l } } ^ { - 1 } { \mathrm { m i n } } ^ { - 1 } \right) ( 1 0 { \mathrm { m i n } } ) + { \frac { 1 } { 0 . 2 0 0 { \mathrm { m o l } } ^ { - 1 } } } } \\ { { \frac { 1 } { \left[ A \right] _ { t } } } } & { = } & { \left( 5 . 7 6 \times 1 0 ^ { - 1 } { \mathrm { L } } { \mathrm { m o l } } ^ { - 1 } \right) + 5 . 0 0 { \mathrm { L } } { \mathrm { m o l } } ^ { - 1 } } \\ { { \frac { 1 } { \left[ A \right] _ { t } } } } & { = } & { 5 . 5 8 { \mathrm { L } } { \mathrm { m o l } } ^ { - 1 } } \\ { { \left[ A \right] _ { t } } } & { = } & { 1 . 7 9 \times 1 0 ^ { - 1 } { \mathrm { m o l } } { \mathrm { L } } ^ { - 1 } } \end{array} }
$$

Therefore $0 . 1 7 9 \mathrm { m o l / L }$ of butadiene remain at the end of $1 0 . 0 \mathrm { m i n }$ , compared to the $0 . 2 0 0 \mathrm { m o l / L }$ that was originally present.

# Check Your Learning

If the initial concentration of butadiene is $0 . 0 2 0 0 M ,$ , what is the concentration remaining after 20.0 min?

Answer: 0.0195 mol/L

The integrated rate law for second-order reactions has the form of the equation of a straight line:

$$
{ \begin{array} { r c l } { { \frac { 1 } { \left[ A \right] _ { t } } } } & { = } & { k t + { \frac { 1 } { \left[ A \right] _ { 0 } } } } \\ { y } & { = } & { m x + b } \end{array} }
$$

A plot of $\textstyle { \frac { 1 } { \left[ A \right] _ { t } } }$ versus tfor a second-order reaction is a straight line with a slope of kand a y-intercept of the plot is not a straight line, then the reaction is not second order.

# EXAMPLE 12.9

# Graphical Determination of Reaction Order and Rate Constant

The data below are for the same reaction described in Example 12.8. Prepare and compare two appropriate data plots to identify the reaction as being either first or second order. After identifying the reaction order, estimate a value for the rate constant.

# Solution

In order to distinguish a first-order reaction from a second-order reaction, prepare a plot of $\mathrm { \ l n { [ C _ { 4 } H _ { 6 } ] } } _ { t }$ versus t and compare it to a plot of $\frac { 1 } { \left[ \mathrm { C } _ { 4 } \mathrm { H } _ { 6 } \right] _ { t } }$ versus $t .$ The values needed for these plots follow.

The plots are shown in Figure 12.10, which clearly shows the plot of $\mathrm { l n } [ \mathrm { C } _ { 4 } \mathrm { H } _ { 6 } ] _ { t }$ versus tis not linear, therefore the reaction is not first order. The plot of $\frac { 1 } { \left[ \mathrm { C } _ { 4 } \mathrm { H } _ { 6 } \right] _ { t } }$ versus $t$ is linear, indicating that the reaction is second order.

According to the second-order integrated rate law, the rate constant is equal to the slope of the $\frac { 1 } { \left[ A \right] _ { t } }$ versus $t$ plot. Using the data for $t = 0 ~ s$ and $t = 6 2 0 0 s ,$ the rate constant is estimated as follows:

$$
k = \mathrm { s l o p e } = { \frac { ( 4 8 1 M ^ { - 1 } - 1 0 0 M ^ { - 1 } ) } { ( 6 2 0 0 \mathrm { s } - 0 \mathrm { s } ) } } = 0 . 0 6 1 4 \mathbf { M } ^ { - 1 } \mathrm { s } ^ { - 1 }
$$

# Check Your Learning

Do the following data fit a second-order rate law?

# Answer:

Yes. The plot of $\frac { 1 } { \left[ A \right] _ { t } }$ vs. $t$ is linear:

# Zero-Order Reactions

For zero-order reactions, the differential rate law is:

$$
{ \mathrm { r a t e } } = k
$$

A zero-order reaction thus exhibits a constant reaction rate, regardless of the concentration of its reactant(s). This may seem counterintuitive, since the reaction rate certainly can’t be finite when the reactant concentration is zero. For purposes of this introductory text, it will suffice to note that zero-order kinetics are observed for some reactions only under certain specific conditions. These same reactions exhibit different kinetic behaviors when the specific conditions aren’t met, and for this reason the more prudent term pseudozero-orderis sometimes used.

The integrated rate law for a zero-order reaction is a linear function:

$$
\begin{array} { r c l } { { [ A ] _ { t } } } & { { = } } & { { - k t + [ A ] _ { 0 } } } \\ { { y } } & { { = } } & { { m x + b } } \end{array}
$$

A plot of [A] versus $t$ for a zero-order reaction is a straight line with a slope of $- k$ and a $y$ -intercept of $[ A ] _ { 0 }$ . Figure 12.11 shows a plot of $\left[ \mathrm { N H } _ { 3 } \right]$ versus $t$ for the thermal decomposition of ammonia at the surface of two different heated solids. The decomposition reaction exhibits first-order behavior at a quartz $\mathrm { ( S i O _ { 2 } ) }$ ) surface, as suggested by the exponentially decaying plot of concentration versus time. On a tungsten surface, however, the plot is linear, indicating zero-order kinetics.

# EXAMPLE 12.10

# Graphical Determination of Zero-Order Rate Constant

Use the data plot in Figure 12.11 to graphically estimate the zero-order rate constant for ammonia decomposition at a tungsten surface.

# Solution

The integrated rate law for zero-order kinetics describes a linear plot of reactant concentration, $[ A ] _ { t } ,$ versus time, $t ,$ , with a slope equal to the negative of the rate constant, $- k$ . Following the mathematical approach of previous examples, the slope of the linear data plot (for decomposition on W) is estimated from the graph. Using the ammonia concentrations at $t = 0$ and $t = 1 0 0 0 \mathrm { s }$ :

$$
k = - { \mathrm { s l o p e } } = - { \frac { ( 0 . 0 0 1 5 { \mathrm { m o l } } \mathrm { L } ^ { - 1 } - 0 . 0 0 2 8 { \mathrm { m o l } } \mathrm { L } ^ { - 1 } ) } { ( 1 0 0 0 \mathrm { s } - 0 \mathrm { s } ) } } = 1 . 3 \times 1 0 ^ { - 6 } { \mathrm { m o l } } { \mathrm { L } } ^ { - 1 } { \mathrm { s } } ^ { - 1 }
$$

# Check Your Learning

The zero-order plot in Figure 12.11 shows an initial ammonia concentration of $0 . 0 0 2 8 \mathrm { m o l } \mathrm { L } ^ { - 1 }$ decreasing linearly with time for 1000 s. Assuming no change in this zero-order behavior, at what time (min) will the concentration reach $0 . 0 0 0 1 \mathrm { m o l } \mathrm { L } ^ { - 1 } \ ?$

Answer: 35 min

# The Half-Life of a Reaction

The half-life of a reaction $( t _ { 1 / 2 } )$ is the time required for one-half of a given amount of reactant to be consumed. In each succeeding half-life, half of the remaining concentration of the reactant is consumed. Using the decomposition of hydrogen peroxide (Figure 12.2) as an example, we find that during the first half-life (from 0.00 hours to 6.00 hours), the concentration of $\mathrm { H } _ { 2 } \mathrm { O } _ { 2 }$ decreases from 1.000 $M$ to $0 . 5 0 0 M .$ During the second half-life (from 6.00 hours to 12.00 hours), it decreases from $0 . 5 0 0 M$ to $0 . 2 5 0 M ;$ during the third half-life, it decreases from $0 . 2 5 0 M$ to $0 . 1 2 5 M .$ The concentration of $\mathrm { H } _ { 2 } \mathrm { O } _ { 2 }$ decreases by half during each successive period of 6.00 hours. The decomposition of hydrogen peroxide is a first-order reaction, and, as can be shown, the half-life of a first-order reaction is independent of the concentration of the reactant. However, half-lives of reactions with other orders depend on the concentrations of the reactants.

# First-Order Reactions

An equation relating the half-life of a first-order reaction to its rate constant may be derived from the integrated rate law as follows:

$$
\begin{array} { r c l } { { \ln { \frac { [ A ] _ { 0 } } { \left[ A \right] _ { t } } } } } & { { = } } & { { k t } } \\ { { t } } & { { = } } & { { \ln { \frac { [ A ] _ { 0 } } { \left[ A \right] _ { t } } } \ \times \ { \frac { 1 } { k } } } } \end{array}
$$

Invoking the definition of half-life, symbolized $t _ { 1 / 2 }$ requires that the concentration of $A$ at this point is one-half its initial concentration: $\begin{array} { r } { t = t _ { 1 / 2 } , [ A ] _ { t } = \frac { 1 } { 2 } [ A ] _ { 0 } } \end{array}$

Substituting these terms into the rearranged integrated rate law and simplifying yields the equation for halflife:

$$
\begin{array}{c} { \begin{array} { l } { { \displaystyle t _ { 1 / 2 } } } \\ { { \mathrm {  ~ \ell ~ } } } \\ { { \mathrm {  ~ \ell ~ } } } \\ { { \displaystyle t _ { 1 / 2 } } } \end{array} } = \ln { \frac { [ A ] _ { 0 } } { { \frac { 1 } { 2 } } [ A ] _ { 0 } } } \ \times \ { \frac { 1 } { k } }  \\ { ~ } \\ { { \mathrm {  ~ \ell ~ } } } \\ { { \displaystyle t _ { 1 / 2 } } } \end{array} 
$$

This equation describes an expected inverse relation between the half-life of the reaction and its rate constant, $k .$ . Faster reactions exhibit larger rate constants and correspondingly shorter half-lives. Slower reactions exhibit smaller rate constants and longer half-lives.

# EXAMPLE 12.11

# Calculation of a First-order Rate Constant using Half-Life

Calculate the rate constant for the first-order decomposition of hydrogen peroxide in water at $4 0 ^ { \circ } \mathrm { C }$ , using the data given in Figure 12.12.

# Solution

Inspecting the concentration/time data in Figure 12.12 shows the half-life for the decomposition of $\mathrm { H } _ { 2 } \mathrm { O } _ { 2 }$ is $2 . 1 6 \times 1 0 ^ { 4 } \mathrm { s } ;$ :

$$
{ \begin{array} { r c l } { t _ { 1 / 2 } } & { = } & { { \frac { 0 . 6 9 3 } { k } } } \\ { k } & { = } & { { \frac { 0 . 6 9 3 } { t _ { 1 / 2 } } } = { \frac { 0 . 6 9 3 } { 2 . 1 6 \times 1 0 ^ { 4 } { \mathrm { s } } } } = 3 . 2 1 \times 1 0 ^ { - 5 } { \mathrm { s } } ^ { - 1 } } \end{array} }
$$

# Check Your Learning

The first-order radioactive decay of iodine-131 exhibits a rate constant of $0 . 1 3 8 { \mathrm { d } } ^ { - 1 }$ . What is the half-life for this decay?

Answer: 5.02 d.

# Second-Order Reactions

Following the same approach as used for first-order reactions, an equation relating the half-life of a secondorder reaction to its rate constant and initial concentration may be derived from its integrated rate law:

$$
{ \frac { 1 } { [ A ] _ { t } } } = k t + { \frac { 1 } { [ A ] _ { 0 } } }
$$

$$
{ \frac { 1 } { [ A ] } } - { \frac { 1 } { [ A ] _ { 0 } } } = k t
$$

Restrict tto t1/2

$$
t = t _ { 1 / 2 }
$$

define $[ A ] _ { t }$ as one-half $[ A ] _ { 0 }$

$$
[ A ] _ { t } = { \frac { 1 } { 2 } } [ A ] _ { 0 }
$$

and then substitute into the integrated rate law and simplify:

$$
\begin{array} { r c l } { { \frac { 1 } { \frac { 1 } { 2 } [ A ] _ { 0 } } ~ - ~ \frac { 1 } { [ A ] _ { 0 } } } } & { { = } } & { { k t _ { 1 / 2 } } } \\ { { } } & { { } } & { { } } \\ { { \frac { 2 } { [ A ] _ { 0 } } ~ - ~ \frac { 1 } { [ A ] _ { 0 } } } } & { { = } } & { { k t _ { 1 / 2 } } } \\ { { } } & { { } } & { { } } \\ { { \frac { 1 } { [ A ] _ { 0 } } ~ = } } & { { k t _ { 1 / 2 } } } \\ { { } } & { { } } & { { } } \\ { { t _ { 1 / 2 } ~ = } } & { { \frac { 1 } { k [ A ] _ { 0 } } } } \end{array}
$$

For a second-order reaction, $t _ { 1 / 2 }$ is inversely proportional to the concentration of the reactant, and the half-life increases as the reaction proceeds because the concentration of reactant decreases. Unlike with first-order reactions, the rate constant of a second-order reaction cannot be calculated directly from the half-life unless the initial concentration is known.

# Zero-Order Reactions

As for other reaction orders, an equation for zero-order half-life may be derived from the integrated rate law:

$$
[ A ] = - k t + [ A ] _ { 0 }
$$

Restricting the time and concentrations to those defined by half-life: $t = t _ { 1 / 2 }$ and $[ A ] = { \frac { [ A ] _ { 0 } } { 2 } }$ Substituting these terms into the zero-order integrated rate law yields:

$$
\begin{array} { r c l } { { \frac { [ \mathrm { A } ] _ { 0 } } { 2 } } } & { { = } } & { { - k t _ { 1 / 2 } + [ \mathrm { A } ] _ { 0 } } } \\ { { k t _ { 1 / 2 } } } & { { = } } & { { \frac { [ \mathrm { A } ] _ { 0 } } { 2 } } } \\ { { t _ { 1 / 2 } } } & { { = } } & { { \frac { [ \mathrm { A } ] _ { 0 } } { 2 k } } } \end{array}
$$

As for all reaction orders, the half-life for a zero-order reaction is inversely proportional to its rate constant.   
However, the half-life of a zero-order reaction increases as the initial concentration increases.

Equations for both differential and integrated rate laws and the corresponding half-lives for zero-, first-, and second-order reactions are summarized in Table 12.2.

# EXAMPLE 12.12

# Half-Life for Zero-Order and Second-Order Reactions

What is the half-life for the butadiene dimerization reaction described in Example 12.8?

# Solution

The reaction in question is second order, is initiated with a $0 . 2 0 0 \mathrm { m o l } \mathrm { L } ^ { - 1 }$ reactant solution, and exhibits a rate constant of $0 . 0 5 7 6 \mathrm { L } \mathrm { m o l } ^ { - 1 } \mathrm { m i n } ^ { - 1 }$ . Substituting these quantities into the second-order half-life equation:

$$
\begin{array} { r c l } { t _ { 1 / 2 } } & { = } & { \frac { 1 } { [ ( 0 . 0 5 7 6 \mathrm { L } \mathrm { m o l } ^ { - 1 } \mathrm { m i n } ^ { - 1 } ) ( 0 . 2 0 0 \mathrm { m o l } \mathrm { L } ^ { - 1 } ) ] } = 1 8 \mathrm { m i n } } \end{array}
$$

# Check Your Learning

What is the half-life (min) for the thermal decomposition of ammonia on tungsten (see Figure 12.11)?

Answer: 87 min