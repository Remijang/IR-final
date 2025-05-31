# 19.6 Capacitors in Series and Parallel

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

• Derive expressions for total capacitance in series and in parallel.   
• Identify series and parallel parts in the combination of connection of capacitors.   
• Calculate the effective capacitance in series and parallel given individual capacitances.

Several capacitors may be connected together in a variety of applications. Multiple connections of capacitors act like a single equivalent capacitor. The total capacitance of this equivalent single capacitor depends both on the individual capacitors and how they are connected. There are two simple and common types of connections, called seriesand paralel, for which we can easily calculate the total capacitance. Certain more complicated connections can also be related to combinations of series and parallel.

# Capacitance in Series

Figure 19.19(a) shows a series connection of three capacitors with a voltage applied. As for any capacitor, the capacitance of the combination is related to charge and voltage by .

Note in Figure 19.19 that opposite charges of magnitude $Q$ flow to either side of the originally uncharged combination of capacitors when the voltage $V$ is applied. Conservation of charge requires that equal-magnitude charges be created on the plates of the individual capacitors, since charge is only being separated in these originally neutral devices. The end result is that the combination resembles a single capacitor with an effective plate separation greater than that of the individual capacitors alone. (See Figure 19.19(b).) Larger plate separation means smaller capacitance. It is a general feature of series connections of capacitors that the total capacitance is less than any of the individual capacitances.

We can find an expression for the total capacitance by considering the voltage across the individual capacitors shown in Figure 19.19. Solving $\begin{array} { r } { C = \frac { Q } { V } } \end{array}$ for $V$ gives $\begin{array} { r } { V = \frac { Q } { C } } \end{array}$ . The voltages across the individual capacitors are thus $\begin{array} { r } { V _ { 1 } = \frac { Q } { C _ { 1 } } , V _ { 2 } = \frac { Q } { C _ { 2 } } } \end{array}$ , and $\begin{array} { r } { V _ { 3 } = \frac { Q } { C _ { 3 } } } \end{array}$ . The total voltage is the sum of the individual voltages:

$$
V = V _ { 1 } + V _ { 2 } + V _ { 3 } .
$$

Now, calling the total capacitance $C _ { \mathrm { { S } } }$ for series capacitance, consider that

$$
V = { \frac { Q } { C _ { \mathrm { { S } } } } } = V _ { 1 } + V _ { 2 } + V _ { 3 } .
$$

Entering the expressions for $V _ { 1 } , V _ { 2 }$ , and $V _ { 3 }$ , we get

$$
{ \frac { Q } { C _ { \mathrm { S } } } } = { \frac { Q } { C _ { 1 } } } + { \frac { Q } { C _ { 2 } } } + { \frac { Q } { C _ { 3 } } } .
$$

Canceling the $ { Q \mathrm { s } }$ , we obtain the equation for the total capacitance in series $C _ { \mathrm { { S } } }$ to be

$$
{ \frac { 1 } { C _ { \mathrm { S } } } } = { \frac { 1 } { C _ { 1 } } } + { \frac { 1 } { C _ { 2 } } } + { \frac { 1 } { C _ { 3 } } } + . . . ,
$$

where “...” indicates that the expression is valid for any number of capacitors connected in series. An expression of this form always results in a total capacitance $C _ { \mathrm { { S } } }$ that is less than any of the individual capacitances $C _ { 1 }$ , $C _ { 2 }$ , ..., as the next example illustrates.

# Total Capacitance in Series, $C _ { \mathrm { s } }$

Total capacitance in series: $\begin{array} { r } { \frac { 1 } { C _ { \mathrm { S } } } = \frac { 1 } { C _ { 1 } } + \frac { 1 } { C _ { 2 } } + \frac { 1 } { C _ { 3 } } + . . . } \end{array}$

# EXAMPLE 19.9

# What Is the Series Capacitance?

Find the total capacitance for three capacitors connected in series, given their individual capacitances are 1.000, 5.000, and $8 . 0 0 0 \mu \mathrm { F }$ .

# Strategy

With the given information, the total capacitance can be found using the equation for capacitance in series.

# Solution

Entering the given capacitances into the expression for $\textstyle \frac { 1 } { C _ { \mathrm { S } } }$ gives $\begin{array} { r } { \frac { 1 } { C _ { S } } = \frac { 1 } { C _ { 1 } } + \frac { 1 } { C _ { 2 } } + \frac { 1 } { C _ { 3 } } } \end{array}$

$$
\frac { 1 } { C _ { \mathrm { S } } } = \frac { 1 } { 1 . 0 0 0 \mu \mathrm { F } } + \frac { 1 } { 5 . 0 0 0 \mu \mathrm { F } } + \frac { 1 } { 8 . 0 0 0 \mu \mathrm { F } } = \frac { 1 . 3 2 5 } { \mu \mathrm { F } }
$$

Inverting to find $C _ { \mathrm { { S } } }$ yields $\begin{array} { r } { C _ { \mathrm { S } } = \frac { \mu \mathrm { F } } { 1 . 3 2 5 } = 0 . 7 5 5 \mu \mathrm { F } . } \end{array}$ ，

# Discussion

The total series capacitance $C _ { \mathrm { s } }$ is less than the smallest individual capacitance, as promised. In series connections of capacitors, the sum is less than the parts. In fact, it is less than any individual. Note that it is sometimes possible, and more convenient, to solve an equation like the above by finding the least common denominator, which in this case (showing only whole-number calculations) is 40. Thus,

$$
\frac { 1 } { C _ { \mathrm { S } } } = \frac { 4 0 } { 4 0 \mu \mathrm { F } } + \frac { 8 } { 4 0 \mu \mathrm { F } } + \frac { 5 } { 4 0 \mu \mathrm { F } } = \frac { 5 3 } { 4 0 \mu \mathrm { F } } ,
$$

so that

$$
C _ { \mathrm { S } } = { \frac { 4 0 \mu \mathrm { F } } { 5 3 } } = 0 . 7 5 5 \mu \mathrm { F } .
$$

# Capacitors in Parallel

Figure 19.20(a) shows a parallel connection of three capacitors with a voltage applied. Here the total capacitance is easier to find than in the series case. To find the equivalent total capacitance $C _ { \mathfrak { p } }$ , we first note that the voltage across each capacitor is $V$ , the same as that of the source, since they are connected directly to it through a conductor. (Conductors are equipotentials, and so the voltage across the capacitors is the same as that across the voltage source.) Thus the capacitors have the same charges on them as they would have if connected individually to the voltage source. The total charge $Q$ is the sum of the individual charges:

$$
Q = Q _ { 1 } + Q _ { 2 } + Q _ { 3 } .
$$

Using the relationship $Q = C V ,$ we see that the total charge is $Q = C _ { \mathrm { p } } V$ , and the individual charges are $Q _ { 1 } = C _ { 1 } V , Q _ { 2 } = C _ { 2 } V$ ,and $Q _ { 3 } = C _ { 3 } V$ . Entering these into the previous equation gives

$$
C _ { \mathrm { p } } V = C _ { 1 } V + C _ { 2 } V + C _ { 3 } V .
$$

Canceling $V$ from the equation, we obtain the equation for the total capacitance in parallel $C _ { \mathfrak { p } }$ :

$$
C _ { \mathfrak { p } } = C _ { 1 } + C _ { 2 } + C _ { 3 } + \dots
$$

Total capacitance in parallel is simply the sum of the individual capacitances. (Again the “..” indicates the expression is valid for any number of capacitors connected in parallel.) So, for example, if the capacitors in the example above were connected in parallel, their capacitance would be

$$
C _ { \mathfrak { p } } = 1 . 0 0 0 \mu \mathrm { F } + 5 . 0 0 0 \mu \mathrm { F } + 8 . 0 0 0 \mu \mathrm { F } = 1 4 . 0 0 0 \mu \mathrm { F } .
$$

The equivalent capacitor for a parallel connection has an effectively larger plate area and, thus, a larger capacitance, as illustrated in Figure 19.20(b).

# Total Capacitance in Parallel, $C _ { \mathrm { p } }$

Total capacitance in parallel $C _ { \mathrm { p } } = C _ { \mathrm { l } } + C _ { 2 } + C _ { 3 } + . . .$

More complicated connections of capacitors can sometimes be combinations of series and parallel. (See Figure 19.21.) To find the total capacitance of such combinations, we identify series and parallel parts, compute their capacitances, and then find the total.

# EXAMPLE 19.10

# A Mixture of Series and Parallel Capacitance

Find the total capacitance of the combination of capacitors shown in Figure 19.21. Assume the capacitances in Figure 19.21 are known to three decimal places ( $C _ { 1 } = 1 . 0 0 0 \mu \mathrm { F }$ , $C _ { 2 } = 5 . 0 0 0 \mu \mathrm { F }$ , and $C _ { 3 } = 8 . 0 0 0 \mu \mathrm { F } )$ , and round your answer to three decimal places.

# Strategy

To find the total capacitance, we first identify which capacitors are in series and which are in parallel. Capacitors $C _ { 1 }$ and $C _ { 2 }$ are in series. Their combination, labeled $C _ { \mathrm { { S } } }$ in the figure, is in parallel with $C _ { 3 }$ .

# Solution

Since $C _ { 1 }$ and $C _ { 2 }$ are in series, their total capacitance is given by $\begin{array} { r } { \frac { 1 } { C _ { \mathrm { S } } } = \frac { 1 } { C _ { 1 } } + \frac { 1 } { C _ { 2 } } + \frac { 1 } { C _ { 3 } } } \end{array}$ . Entering their values into the equation gives

$$
{ \frac { 1 } { C _ { \mathrm { { S } } } } } = { \frac { 1 } { C _ { 1 } } } + { \frac { 1 } { C _ { 2 } } } = { \frac { 1 } { 1 . 0 0 0 \mu \mathrm { { F } } } } + { \frac { 1 } { 5 . 0 0 0 \mu \mathrm { { F } } } } = { \frac { 1 . 2 0 0 } { \mu \mathrm { { F } } } } .
$$

Inverting gives

$$
C _ { \mathrm { S } } = 0 . 8 3 3 \mu \mathrm { F } .
$$

This equivalent series capacitance is in parallel with the third capacitor; thus, the total is the sum

$$
{ \begin{array} { l l l } { C _ { \mathrm { t o t } } } & { = } & { C _ { \mathrm { S } } + C _ { \mathrm { S } } } \\ & { = } & { 0 . 8 3 3 \mu \mathrm { F } + 8 . 0 0 0 \mu \mathrm { F } } \\ & { = } & { 8 . 8 3 3 \mu \mathrm { F } . } \end{array} }
$$

# Discussion

This technique of analyzing the combinations of capacitors piece by piece until a total is obtained can be applied to larger combinations of capacitors.