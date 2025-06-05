# 6.5 Separable Equations Including the Logistic Equation

This section begins with the integrals that solve two basic differential equations:

$$
{ \frac { d y } { d t } } = c y \qquad { \mathrm { a n d } } \qquad { \frac { d y } { d t } } = c y + s .
$$

We already know the solutions. What we don’t know is how to discover those solutions, when a suggestion “try $e ^  c t \cdot \}$ has not been made. Many important equations, including these, separate into a $y$ -integral and a $t$ -integral. The answer comes directly from the two separate integrations. When a differential equation is reduced that far—to integrals that we know or can look up—it is solved.

One particular equation will be emphasized. The logistic equation describes the speedup and slowdown of growth. Its solution is an S-curve, which starts slowly, rises quickly, and levels off. (The 1990’s are near the middle of the S, if the prediction is correct for the world population.) S-curves are solutions to nonlinear equations, and we will be solving our first nonlinear model. It is highly important in biology and all life sciences.

# SEPARABLE EQUATIONS

The equations $d y / d t = c y$ and $d y / d t = c y + s$ (with constant source $s$ ) can be solved by a direct method. The idea is to separate $y$ from $t$ :

$$
{ \frac { d y } { y } } = c ~ d t \qquad { \mathrm { a n d } } \qquad { \frac { d y } { y + ( s / c ) } } = c ~ d t .
$$

All $y$ ’s are on the left side. All $t$ ’s are on the right side (and $c$ can be on either side). This separation would not be possible for $d y / d t = y + t$ :

Equation (2) contains differentials. They suggest integrals. The $t$ -integrals give $c t$ and the $y$ -integrals give logarithms:

$$
\ln y = c t + \mathrm { c o n s t a n t } \qquad \mathrm { a n d } \qquad \ln \left( y + { \frac { s } { c } } \right) = c t + \mathrm { c o n s t a n t } .
$$

The constant is determined by the initial condition. At $t = 0$ we require $y = y _ { 0 }$ ; and the right constant will make that happen:

$$
\ln y = c t + \ln y _ { 0 } \qquad { \mathrm { a n d } } \qquad \ln \left( y + { \frac { s } { c } } \right) = c t + \ln \left( y _ { 0 } + { \frac { s } { c } } \right) .
$$

Then the final step isolates $y$ : The goal is a formula for $y$ itself, not its logarithm, so take the exponential of both sides ( $e ^ { \ln y }$ is $y$ ):

$$
y = y _ { 0 } e ^ { c t } \qquad { \mathrm { a n d } } \qquad y + { \frac { s } { c } } = \left( y _ { 0 } + { \frac { s } { c } } \right) e ^ { c t } .
$$

It is wise to substitute $y$ back into the differential equation, as a check.

This is our fourth method for $y ^ { \prime } = c y + s$ : Method 1 assumed from the start that $y = A e ^ { c t } + B$ : Method 2 multiplied all inputs by their growth factors $e ^ { c ( t - T ) }$ and added up outputs. Method 3 solved for $y - y _ { \infty }$ : Method 4 is separation of variables (and all methods give the same answer). This separation method is so useful that we repeat its main idea, and then explain it by using it.

To solve $d y / d t = u ( y ) v ( t )$ ; separate $d y / u ( y )$ from $v ( t ) d t$ and integrate both sides:

$$
\int d y / u ( y ) = \int v ( t ) d t + C .
$$

Then substitute the initial condition to determine $C$ ; and solve for $y ( t )$ :

EXAMPLE 1 $d y / d t = y ^ { 2 }$ separates into $d y / y ^ { 2 } = d t$ : Integrate to reach $- 1 / y = t + C$ : Substitute $t = 0$ and $y = y _ { 0 }$ to find $C = - 1 / y _ { 0 }$ : Now solve for $y$ :

$$
- { \frac { 1 } { y } } = t - { \frac { 1 } { y _ { 0 } } } \qquad { \mathrm { a n d } } \qquad y = { \frac { y _ { 0 } } { 1 - t y _ { 0 } } } .
$$

This solution blows up (Figure 6.15a) when $t$ reaches $1 / y _ { 0 }$ : If the bank pays interest on your deposit squared $( y ^ { \prime } = y ^ { 2 } )$ ), you soon have all the money in the world.

EXAMPLE 2 $d y / d t = t y$ separates into $d y / y = t \ d t$ : Then by integration ln $y = \textstyle { \frac { 1 } { 2 } } t ^ { 2 } + C$ : Substitute $t = 0$ and $y = y _ { 0 }$ to find $C = \ln y _ { 0 }$ : The exponential of $\scriptstyle { \frac { 1 } { 2 } } t ^ { 2 } + \ln y _ { 0 }$ gives $y = y _ { 0 } e ^ { t ^ { 2 } / 2 }$ : When the interest rate is $c = t$ ; the exponent is $t ^ { 2 } / 2$ :

EXAMPLE 3 $d y / d t = y + t$ is not separable. Method 1 survives by assuming $y = A e ^ { t } + B + D t$ —with an extra coefficient $D$ in Problem 23: Method 2 also succeeds—but not the separation method.

EXAMPLE 4 Separate $d y / d t = n y / t$ into $d y / y = n \ d t / t$ : By integration ln $y =$ $n \ln t + C$ : Substituting $t = 0$ produces $\ln { 0 }$ and disaster. This equation cannot start from time zero (it divides by $t$ ). However $y$ can start from $y _ { 1 }$ at $t = 1$ ; which gives $C = \ln y _ { 1 }$ : The solution is a power function $y = y _ { 1 } t ^ { n }$ .

This was the first differential equation in the book (Section 2:2). The ratio of $d y / y$ to $d t / t$ is the “elasticity” in economics. These relative changes have units like dollars=dollars—they are dimensionless, and $y = t ^ { n }$ has constant elasticity $n$ :

On log–log paper the graph of ln $y = n$ ln $t + C$ is a straight line with slope $n$ :

# THE LOGISTIC EQUATION

The simplest model of population growth is $d y / d t = c y$ : The growth rate $c$ is the birth rate minus the death rate. If $c$ is constant the growth goes on forever—beyond the point where the model is reasonable. A population can’t grow all the way to infinity! Eventually there is competition for food and space, and $y = e ^ { c t }$ must slow down.

The true rate c depends on the population size $y$ : It is a function $c ( y )$ not a constant. The choice of the model is at least half the problem:

$$
\begin{array} { r l r } & { } & { P r o b l e m \ i n \ b i o l o g y \ o r \ e c o l o g y ; \mathrm { D i s c o v e r \ } c ( y ) . } \\ & { } & { P r o b l e m \ i n \ m a t h e m a t i c s ; \mathrm { S o l v e \ } d y / d t = c ( y ) y . } \end{array}
$$

Every model looks linear over a small range of $y$ ’s—but not forever. When the rate drops off, two models are of the greatest importance. The Michaelis-Menten equation has $c ( y ) = c / ( y + K )$ : The logistic equation has $c ( y ) = c - b y$ : It comes first.

The nonlinear effect is from “interaction.” For two populations of size $y$ and $z$ ; the number of interactions is proportional to $y$ times $z$ : The Law of Mass Action produces a quadratic term $b y z$ : It is the basic model for interactions and competition. Here we have one population competing within itself, so $z$ is the same as $y$ : This competition slows down the growth, because $- b y ^ { 2 }$ goes into the equation.

The basic model of growth versus competition is known as the logistic equation:

$$
d y / d t = c y - b y ^ { 2 } .
$$

Normally $b$ is very small compared to $c$ : The growth begins as usual (close to $e ^ { c t }$ ). The competition term $b y ^ { 2 }$ is much smaller than $_ { c y }$ ; until $y$ itself gets large. Then $b y ^ { 2 }$ (with its minus sign) slows the growth down. The solution follows an S-curve that we can compute exactly.

What are the numbers $b$ and $c$ for human population ? Ecologists estimate the natural growth rate as $c = . 0 2 9 ,$ =year. That is not the actual rate, because of $b$ : About 1930; the world population was 3 billion. The $c y$ term predicts a yearly increase of $( . 0 2 9 ) ( 3 \mathrm { b i l l i o n } ) = 8 7$ million: The actual growth was more like $d y / d t = 6 0$ million=year: That difference of 27 million=year was $b y ^ { 2 }$ :

$$
2 7 \mathrm { m i l l i o n / y e a r } = b ( 3 \mathrm { b i l l i o n } ) ^ { 2 } \mathrm { l e a d s t o } b = 3 \cdot 1 0 ^ { - 1 2 } / \mathrm { y e a r } .
$$

Certainly $b$ is a small number (three trillionths) but its effect is not small. It reduces 87 to 60: What is fascinating is to calculate the steady state, when the new term $b y ^ { 2 }$ equals the old term $c y$ :8When these terms cancel each other, $d y / d t = c y - b y ^ { 2 }$ is zero. The loss from competition balances the gain from new growth: $c y = b y ^ { 2 }$ and $y = c / b$ : The growth stops at this equilibrium point—the top of the S-curve:

$$
y _ { \infty } = { \frac { c } { b } } = { \frac { . 0 2 9 } { 3 } } 1 0 ^ { 1 2 } \approx 1 0 { \mathrm { b i l l i o n ~ p e o p l e } } .
$$

According to Verhulst’s logistic equation, t8he world population is converging to 10 billion. That is from the model. From present indications we are growing much faster. We will very probably go beyond 10 billion. The United Nations report in Section 3:3 predicts 11 billion to 14 billion.

Notice a specia2l point halfwa1y to $y _ { \infty } = c / b$ 1. (In the model this point is at 5 billion.) It is the inflection point where the S-curve begins to bend down. The second derivative $d ^ { 2 } y / d t ^ { 2 }$ is zero. The slope $d y / d t$ is a maximum. It is easier to find this point from the differential equation (which gives $d y / d t )$ ) than from $y$ : Take one more derivative:

$$
y ^ { \prime \prime } = ( c y - b y ^ { 2 } ) ^ { \prime } = c y ^ { \prime } - 2 b y y ^ { \prime } = ( c - 2 b y ) y ^ { \prime } .
$$

The factor $c - 2 b y$ is zero at the inflection point $y = c / 2 b$ ; halfway up the S-curve.

# THE S-CURVE

# The logistic equation is solved by separating variables $y$ and $t$ :

$$
d y / d t = c y - b y ^ { 2 } { \mathrm { ~ b e c o m e s } } \int d y / ( c y - b y ^ { 2 } ) = \int d t .
$$

The first question is whether we recognize this $y$ -integral. $N o$ . The second question is whether it is listed in the cover of the book. $N o$ . The nearest is $\int d x / ( a ^ { 2 } - \bar { x ^ { 2 } } )$ ; which can be reached with considerable manipulation (Problem21). The third question is whether a general method is available. Yes. “Partial fractions” is perfectly suited to $1 / ( c y - b \bar { y } ^ { 2 } )$ ; and Section 7:4 gives the following integral of equation (9):

$$
\ln { \frac { y } { c - b y } } = c t + C \qquad { \mathrm { a n d ~ t h e n } } \qquad \ln { \frac { y _ { 0 } } { c - b y _ { 0 } } } = C .
$$

That constant $C$ makes the solution correct at $t = 0$ : The logistic equation is integrated, but the solution can be improved. Take exponentials of both sides to remove the logarithms:

$$
\frac { y } { c - b y } = e ^ { c t } \frac { y _ { 0 } } { c - b y _ { 0 } } .
$$

This contains the same growth factor $e ^ { c t }$ as in linear equations. But the logistic equation is not linear—it is8not $y$ that increases so fast. According to (11),8it is $y / ( c - b y )$ that grows to infinity. This happens when $c - b y$ approaches zero.

The growth stops at $y = c / b$ : That is the final population of the world (10 billion ? ).

We still need a formula for $y$ : The perfect S-curve is the graph of $y = 1 / ( 1 +$ $e ^ { - t }$ /: It equals 1 when $t = \infty$ ;it equals $\frac { 1 } { 2 }$ when $t = 0$ ; it equals 0when $t = - \infty$ : It satisfies $y ^ { \prime } { = } y - y ^ { 2 }$ ; with $c = b = 1$ : The general formula cannot be so beautiful, because it allows any $\mathbf { \Psi } _ { c , b }$ ; and $y _ { 0 }$ : To find the S-curve, multiply equation (11) by $c - b y$ and solve for :

$$
\begin{array} { l } { \displaystyle { \mathrm {  ~ \mu ~ } } ^ { \mathrm { \scriptsize { \mathrm { \scriptsize { ~ \scriptstyle ~ 1 ~ v ~ c ~ 1 0 ~ } ~ } } } y . } \qquad \displaystyle { \mathrm {  ~ \Lambda ~ } } ^ { c } \qquad \mathrm { \ o r } \qquad y = \frac { c } { b + d e ^ { - c t } } . } \end{array}
$$

When $t$ approaches infinity , $e ^ { - c t }$ approaches zero. The complicated part of the formula disappears. Then $y$ approaches its steady state $c / b$ ; the asymptote in Figure 6.16. The S-shape comes from the inflection point halfway up.

Surprising observation: $z = 1 / y$ satisfies a linear equation. By calculus $z ^ { \prime } = - y ^ { \prime } / y ^ { 2 }$ : So

$$
z ^ { \prime } = \frac { - c y + b y ^ { 2 } } { y ^ { 2 } } = - \frac { c } { y } + b = - c z + b .
$$

This equation $z ^ { \prime } = - c z + b$ is solved by an exponential $e ^ { - c t }$ plus a constant:

$$
z = A e ^ { - c t } + \frac { a } { b } = \left( \frac { 1 } { y _ { 0 } } - \frac { b } { c } \right) e ^ { - c t } + \frac { b } { c } .
$$

Turned upside down, $y = 1 / z$ is the S-curve (12). As $z$ approaches $b / c$ ; the S-curve approaches $c / b$ : Notice that $z$ starts at $1 / y _ { 0 }$ :

EXAMPLE 1 (United States population) The table shows the actual population and the model. Pearl and Reed used cen1sus figures for 1790; 1850; and 1910 to compute $c$ and $b$ : In between, the fit is good but not fantastic. One reason is war—another is depression. Probably more important is immigration. $^ \dagger$ In fact the Pearl-Reed steady state $c / b$ is below 200 million, which the US has already passed. Certainly their model can be and has been improved. The 1990 census predicted a stop before 300 million. For constant immigration $s$ we could still solve $y ^ { \prime } { = } c y - b y ^ { 2 } + s$ by partial fractions—but in practice the computer has taken over. The table comes from Braun’s book Differential Equations (Springer 1975).

Remark For good science the $y ^ { 2 }$ term should be explained and justified. It gave a nonlinear model that could be completely solved, but simplicity is not necessarily truth. The basic justification is this: In a population of size $y$ ; the number of encounters is proportional to $y ^ { 2 }$ : If those encounters are fights, the term is $- b y ^ { 2 }$ : If those encounters increase the population, as some like to think, the sign is changed. There is a cooperation term $+ b y ^ { 2 }$ ; and the population increases very fast.

EXAMPLE 5 $y ^ { \prime } = c y + b y ^ { 2 }$ : y goes to infinity in a finite time.

EXAMPLE 6 $y ^ { \prime } = - d y + b y ^ { 2 }$ : y dies to zero if y0 d=b:

In Example 6 death wins. A small population dies out before the cooperation $b y ^ { 2 }$ can save it. A population below $d / b$ is an endangered species.

The logistic equation can’t predict oscillations—those go beyond $d y / d t = f ( y )$

The $y$ line Here is a way to understand every nonlinear equation $y ^ { \prime } = f ( y )$ : Draw a “ $y$ line.” Add arrows to show the sign of $f ( y )$ : When $y ^ { \prime } = f ( y )$ is positive, $y$ is increasing (it follows the arrow to the right). When $f$ is negative, $y$ goes to the left. When $f$ is zero, the equation is $y ^ { \prime } = 0$ and $y$ is stationary:

The arrows take you left or right, to the steady state or to infinity. Arrows go toward stable steady states. The arrows go away, when the stationary point is unstable. The $y$ line shows which way $y$ moves and where it stops.

The terminal velocity of a falling body is $v _ { \infty } = { \sqrt { g } }$ in Problem 6:7:54: For $f ( y ) = \sin y$ there are several steady states:

The reaction combines $m$ molecules of $A$ with $n$ molecules of $B$ to produce $p$ molecules of $C$ : The numbers $m , n , p$ are $1 , 1 , 2$ for hydrogen chloride: $\mathrm { H } _ { 2 } + \mathrm { C l } _ { 2 } =$ $2 \mathrm { H C l }$ : The Law of Mass Action says that the reaction rate is proportional to the product of the concentrations ŒA and $[ B ]$ : Then $[ A ]$ decays as $[ C ]$ grows:

$$
d [ A ] / d t = - r [ A ] [ B ] \qquad { \mathrm { a n d } } \qquad d [ C ] / d t = + k [ A ] [ B ] .
$$

Chemistry measures $r$ and $k$ : Mathematics solves for $[ A ]$ and $[ C ]$ : Write $y$ for the concentration $[ C ]$ ; the number of molecules in aunit volume. Forming those $y$ molecules drops the concentration $[ A ]$ from $a _ { 0 }$ to $a _ { 0 } - ( m / p ) y$ : Similarly $[ B ]$ drops from $b _ { 0 }$ to $b _ { 0 } - ( n / p ) y$ : The mass action law (15) contains $y ^ { 2 }$ :

$$
\frac { d y } { d t } = k \left( a _ { 0 } - \frac { m } { p } y \right) \left( b _ { 0 } - \frac { n } { p } y \right) .
$$

This fits our nonlinear model (Problem 33 34). We now find this same mass action in biology. You recognize it whenever there is a product of two concentrations.

$$
{ \mathsf { T H E } } \ { \mathsf { M M } } \ { \mathsf { E G U A T I O N } } \ d y / d t = - c y / ( y + K )
$$

Biochemical reactions are the keys to life. They take place continually in every living organism. Their mathematical description is not easy! Engineering and physics go far with linear models, while biology is quickly nonlinear. It is true that $y ^ { \prime } = c y$ is extremely effective in first-order kinetics (Section 6:3), but nature builds in a nonlinear regulator.

It is enzymes that speed up a reaction. Without them, your life would be in slow motion. Blood would take years to clot. Steaks would take decades to digest. Calculus would take centuries to learn. The whole system is awesomely beautiful—DNA tells amino acids how to combine into useful proteins, and we get enzymes and elephants and Isaac Newton.

Briefly, the enzyme enters the reaction and comes out again. It is the catalyst. Its combination with the substrate is an unstable intermediate, which breaks up into a new product and the enzyme (which is ready to start over).

Here are examples of catalysts, some good and some bad.

1. The platinum in a catalytic converter reacts with pollutants from the car engine. (But platinum also reacts with lead—ten gallons of leaded gasoline and you can forget the platinum.)   
2. Spray propellants (CFC’s) catalyze the change from ozone $\left( \mathbf { O } _ { 3 } \right)$ into ordinary oxygen $( \mathbf { O } _ { 2 } )$ . This wipes out the ozone layer—our shield in the atmosphere.   
3. Milk becomes yoghurt and grape juice becomes wine.   
4. Blood clotting needs a whole cascade of enzymes, amplifying the reaction at every step. In hemophilia—the “Czar’s disease”—the enzyme called Factor VIII is missing. A small accident is disaster; the bleeding won’t stop.   
5. Adolph’s Meat Tenderizer is a protein from papayas. It predigests the steak. The same enzyme (chymopapain) is injected to soften herniated disks.   
6. Yeast makes bread rise. Enzymes put the sour in sourdough.



Of course, it takes enzymes to make enzymes. The maternal egg contains the material for a cell, and also half of the DNA. The fertilized egg contains the full instructions.

We now look at the Michaelis–Menten (MM) equation, to describe these reactions. It is based on the Law of Mass Action. An enzyme in concentration $z$ converts a substrate in concentration $y$ by $d y / d t = - b y z$ : The rate constant is $b$ ; and you see the product of “enzyme times substrate.” A similar law governs the other reactions (some go backwards). The equations are nonlinear, with no exact solution. It is typical of applied mathematics (and nature) that a pattern can still be found.

What happens is that the enzyme concentration $z ( t )$ quickly drops to $z _ { 0 } K / ( y +$ $K$ /: The Michaelis constant $K$ depends on the rates (like $b$ ) in the mass action laws. Later the enzyme reappears $\dot { z } _ { \infty } = z _ { 0 }$ ). But by then the first reaction is over. Its law of mass action is effectively

$$
{ \frac { d y } { d t } } = - b y z = - { \frac { c y } { y + K } }
$$

with $c = b z _ { 0 } K$ : This is the Michaelis–Menten equation—basic to biochemistry. The rate $d y / d t$ is all-important in biology. Look at the function $c y / ( y + K )$ :

$$
\mathrm { w h e n } y \mathrm { ~ i s ~ l a r g e } , d y / d t \approx - c \qquad \mathrm { w h e n } y \mathrm { ~ i s ~ s m a l l } , d y / d t \approx - c y / K .
$$

The start and the finish operate at different rates, depending whether $y$ dominates $K$ or $K$ dominates $y$ : The fastest rate is $c$ :

A biochemist solves the MM equation by separating variables:

$$
\int { \frac { y + K } { y } } d y = - \int c d t \quad { \mathrm { g i v e s } } \quad y + K \ln y = - c t + C .
$$

Set $t = 0$ as usual. Then $C = y _ { 0 } + K$ ln $y _ { 0 }$ : The exponentials of the two sides are

$$
e ^ { y } y ^ { K } = e ^ { - c t } e ^ { y _ { 0 } } y _ { 0 } ^ { K } .
$$

We don’t have a simple formula for $y$ : We are lucky to get this close. A computer can quickly graph $y ( t )$ —and we see the dynamics of enzymes.

Problems $2 7 - 3 2$ follow up the Michaelis–Menten theory. In science, concentrations and rate constants come with units. In mathematics, variables can be made dimensionless and constants become 1: We solve $d Y / d T = Y / ( Y + 1 )$ and then switch back to $y , t , c , K$ : This idea applies to other equations too.

Essential point: Most applications of calculus come through differential equations. That is the language of mathematics—with populations and chemicals and epidemics obeying the same equation. Running parallel to $d y / d t = c y$ are the difference equations that come next.