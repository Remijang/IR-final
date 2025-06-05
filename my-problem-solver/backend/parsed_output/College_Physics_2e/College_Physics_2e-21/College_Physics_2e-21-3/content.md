# 21.3 Kirchhoff’s Rules

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

• Analyze a complex circuit using Kirchhoff’s rules, using the conventions for determining the correct signs of various terms.

Many complex circuits, such as the one in Figure 21.21, cannot be analyzed with the series-parallel techniques developed in Resistors in Series and Parallel and Electromotive Force: Terminal Voltage. There are, however, two circuit analysis rules that can be used to analyze any circuit, simple or complex. These rules are special cases of the laws of conservation of charge and conservation of energy. The rules are known as Kirchhoff’s rules, after their inventor Gustav Kirchhoff (1824–1887).

# Kirchhoff’s Rules

• Kirchhoff’s first rule—the junction rule. The sum of all currents entering a junction must equal the sum of all currents leaving the junction.   
• Kirchhoff’s second rule—the loop rule. The algebraic sum of changes in potential around any closed circuit path (loop) must be zero.

Explanations of the two rules will now be given, followed by problem-solving hints for applying Kirchhoff’s rules, and a worked example that uses them.

# Kirchhoff’s First Rule

Kirchhoff’s first rule (the junction rule) is an application of the conservation of charge to a junction; it is illustrated in Figure 21.22. Current is the flow of charge, and charge is conserved; thus, whatever charge flows into the junction must flow out. Kirchhoff’s first rule requires that $I _ { 1 } = I _ { 2 } + I _ { 3 }$ (see figure). Equations like this can and will be used to analyze circuits and to solve circuit problems.

# Making Connections: Conservation Laws

Kirchhoff’s rules for circuit analysis are applications of conservation laws to circuits. The first rule is the application of conservation of charge, while the second rule is the application of conservation of energy. Conservation laws, even used in a specific application, such as circuit analysis, are so basic as to form the foundation of that application.

$$
I _ { 1 } = I _ { 2 } + I _ { 3 }
$$

# Kirchhoff’s Second Rule

Kirchhoff’s second rule (the loop rule) is an application of conservation of energy. The loop rule is stated in terms of potential, $V$ , rather than potential energy, but the two are related since $\mathrm { P E _ { e l e c } } = q V .$ Recall that emf is the potential difference of a source when no current is flowing. In a closed loop, whatever energy is supplied by emf must be transferred into other forms by devices in the loop, since there are no other ways in which energy can be transferred into or out of the circuit. Figure 21.23 illustrates the changes in potential in a simple series circuit loop.

Kirchhoff’s second rule requires $- I r - I R _ { 1 } - I R _ { 2 } = 0$ . Rearranged, this is $= I r + I R _ { 1 } + I R _ { 2 }$ , which means the emf equals the sum of the $I R$ (voltage) drops in the loop.

across the internal resistance, and $\boldsymbol { \mathsf { 1 2 V } }$ and 5 V across the two load resistances, for a total of 18 V. (b) This perspective view represents the potential as something like a roller coaster, where charge is raised in potential by the emf and lowered by the resistances. (Note that the script E stands for emf.)

# Applying Kirchhoff’s Rules

By applying Kirchhoff’s rules, we generate equations that allow us to find the unknowns in circuits. The unknowns may be currents, emfs, or resistances. Each time a rule is applied, an equation is produced. If there are as many independent equations as unknowns, then the problem can be solved. There are two decisions you must make when applying Kirchhoff’s rules. These decisions determine the signs of various quantities in the equations you obtain from applying the rules.

1. When applying Kirchhoff’s first rule, the junction rule, you must label the current in each branch and decide in what direction it is going. For example, in Figure 21.21, Figure 21.22, and Figure 21.23, currents are labeled $I _ { 1 }$ , $I _ { 2 } , I _ { 3 }$ , and $I$ , and arrows indicate their directions. There is no risk here, for if you choose the wrong direction, the current will be of the correct magnitude but negative.   
2. When applying Kirchhoff’s second rule, the loop rule, you must identify a closed loop and decide in which direction to go around it, clockwise or counterclockwise. For example, in Figure 21.23 the loop was traversed in the same direction as the current (clockwise). Again, there is no risk; going around the circuit in the opposite direction reverses the sign of every term in the equation, which is like multiplying both sides of the equation by $^ { - 1 }$

Figure 21.24 and the following points will help you get the plus or minus signs right when applying the loop rule. Note that the resistors and emfs are traversed by going from a to b. In many circuits, it will be necessary to construct more than one loop. In traversing each loop, one needs to be consistent for the sign of the change in potential. (See Example 21.5.)

When a resistor is traversed in the same direction as the current, the change in potential is $- I R$ . (See Figure 21.24.)   
When a resistor is traversed in the direction opposite to the current, the change in potential is $+ I R$ . (See Figure 21.24.)   
• When an emf is traversed from to $^ +$ (the same direction it moves positive charge), the change in potential is +emf. (See Figure 21.24.)   
When an emf is traversed from $^ +$ to (opposite to the direction it moves positive charge), the change in potential is emf. (See Figure 21.24.)

# EXAMPLE 21.5

# Calculating Current: Using Kirchhoff’s Rules

Find the currents flowing in the circuit in Figure 21.25.

# Strategy

This circuit is sufficiently complex that the currents cannot be found using Ohm’s law and the series-parallel techniques—it is necessary to use Kirchhoff’s rules. Currents have been labeled $I _ { 1 } , I _ { 2 }$ , and $I _ { 3 }$ in the figure and assumptions have been made about their directions. Locations on the diagram have been labeled with letters a through h. In the solution we will apply the junction and loop rules, seeking three independent equations to allow us to solve for the three unknown currents.

# Solution

We begin by applying Kirchhoff’s first or junction rule at point a. This gives

$$
I _ { 1 } = I _ { 2 } + I _ { 3 } ,
$$

since $I _ { 1 }$ flows into the junction, while $I _ { 2 }$ and $I _ { 3 }$ flow out. Applying the junction rule at e produces exactly the same equation, so that no new information is obtained. This is a single equation with three unknowns—three independent equations are needed, and so the loop rule must be applied.

Now we consider the loop abcdea. Going from a to b, we traverse $R _ { 2 }$ in the same (assumed) direction of the current $I _ { 2 }$ , and so the change in potential is $- I _ { 2 } R _ { 2 }$ . Then going from b to c, we go from to $^ +$ , so that the change in potential is $+ \mathrm { e m f } _ { 1 }$ . Traversing the internal resistance $r _ { 1 }$ from c to d gives $- I _ { 2 } r _ { 1 }$ . Completing the loop by going from d to a again traverses a resistor in the same direction as its current, giving a change in potential of $- I _ { 1 } R _ { 1 }$ .

The loop rule states that the changes in potential sum to zero. Thus,

$$
\begin{array} { r } { - I _ { 2 } R _ { 2 } + \mathrm { e m f } _ { 1 } - I _ { 2 } r _ { 1 } - I _ { 1 } R _ { 1 } = - I _ { 2 } ( R _ { 2 } + r _ { 1 } ) + \mathrm { e m f } _ { 1 } - I _ { 1 } R _ { 1 } = 0 . } \end{array}
$$

Substituting values from the circuit diagram for the resistances and emf, and canceling the ampere unit gives

$$
- 3 I _ { 2 } + 1 8 - 6 I _ { 1 } = 0 .
$$

ow applying the loop rule to aefgha (we could have chosen abcdefgha as well) similarly gives

$$
+ I _ { 1 } R _ { 1 } + I _ { 3 } R _ { 3 } + I _ { 3 } r _ { 2 } - \mathrm { e m f } _ { 2 } { = } + I _ { 1 } R _ { 1 } + I _ { 3 } ( R _ { 3 } + r _ { 2 } ) \mathrm { - e m f } _ { 2 } { = } 0 .
$$

Note that the signs are reversed compared with the other loop, because elements are traversed in the opposite direction. With values entered, this becomes

$$
+ 6 I _ { 1 } + 2 I _ { 3 } - 4 5 = 0 .
$$

These three equations are sufficient to solve for the three unknown currents. First, solve the second equation for $I _ { 2 }$

$$
I _ { 2 } = 6 - 2 I _ { 1 } .
$$

Now solve the third equation for $I _ { 3 }$ :

$$
I _ { 3 } = 2 2 . 5 - 3 I _ { 1 } .
$$

Substituting these two new equations into the first one allows us to find a value for $I _ { 1 }$ :

$$
I _ { 1 } = I _ { 2 } + I _ { 3 } = ( 6 - 2 I _ { 1 } ) + ( 2 2 . 5 - 3 I _ { 1 } ) = 2 8 . 5 - 5 I _ { 1 } .
$$

Combining terms gives

$$
\begin{array} { c } { 6 { I _ { 1 } } = 2 8 . 5 , \mathrm { a n d } } \\ { { { I _ { 1 } } = 4 . 7 5 \mathrm { A } . } } \end{array}
$$

Substituting this value for $I _ { 1 }$ back into the fourth equation gives

$$
\begin{array} { c } { { I _ { 2 } = 6 - 2 I _ { 1 } = 6 - 9 . 5 0 } } \\ { { I _ { 2 } = - 3 . 5 0 \mathrm { A } . } } \end{array}
$$

The minus sign means $I _ { 2 }$ flows in the direction opposite to that assumed in Figure 21.25.

Finally, substituting the value for $I _ { 1 }$ into the fifth equation gives

$$
I _ { 3 } = 2 2 . 5 - 3 I _ { 1 } = 2 2 . 5 - 1 4 . 2 5
$$

$$
I _ { 3 } = 8 . 2 5 \mathrm { A } .
$$

# Discussion

Just as a check, we note that indeed $I _ { 1 } = I _ { 2 } + I _ { 3 }$ . The results could also have been checked by entering all of the values into the equation for the abcdefgha loop.

# Problem-Solving Strategies for Kirchhoff’s Rules

1. Make certain there is a clear circuit diagram on which you can label all known and unknown resistances, emfs, and currents. If a current is unknown, you must assign it a direction. This is necessary for determining the signs of potential changes. If you assign the direction incorrectly, the current will be found to have a negative value—no harm done.   
2. Apply the junction rule to any junction in the circuit. Each time the junction rule is applied, you should get an equation with a current that does not appear in a previous application—if not, then the equation is redundant.   
3. Apply the loop rule to as many loops as needed to solve for the unknowns in the problem. (There must be as many independent equations as unknowns.) To apply the loop rule, you must choose a direction to go around the loop. Then carefully and consistently determine the signs of the potential changes for each element using the four bulleted points discussed above in conjunction with Figure 21.24.   
4. Solve the simultaneous equations for the unknowns. This may involve many algebraic steps, requiring careful checking and rechecking.   
5. Check to see whether the answers are reasonable and consistent. The numbers should be of the correct order of magnitude, neither exceedingly large nor vanishingly small. The signs should be reasonable—for example, no resistance should be negative. Check to see that the values obtained satisfy the various equations obtained from applying the rules. The currents should satisfy the junction rule, for example.

The material in this section is correct in theory. We should be able to verify it by making measurements of current and voltage. In fact, some of the devices used to make such measurements are straightforward applications of the principles covered so far and are explored in the next modules. As we shall see, a very basic, even profound, fact results—making a measurement alters the quantity being measured.

# CHECK YOUR UNDERSTANDING

Can Kirchhoff’s rules be applied to simple series and parallel circuits or are they restricted for use in more complicated circuits that are not combinations of series and parallel?

# Solution

Kirchhoff's rules can be applied to any circuit since they are applications to circuits of two conservation laws. Conservation laws are the most broadly applicable principles in physics. It is usually mathematically simpler to use the rules for series and parallel in simpler circuits so we emphasize Kirchhoff’s rules for use in more complicated situations. But the rules for series and parallel can be derived from Kirchhoff’s rules. Moreover, Kirchhoff’s rules can be expanded to devices other than resistors and emfs, such as capacitors, and are one of the basic analysis devices in circuit analysis.