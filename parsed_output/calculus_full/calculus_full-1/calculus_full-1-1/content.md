The right way to begin a calculus book is with calculus. This chapter will jump directly into the two problems that the subject was invented to solve. You will see what the questions are, and you will see an important part of the answer. There are plenty of good things left for the other chapters, so why not get started ?

The book begins with an example that is familiar to everybody who drives a car. It is calculus in action—the driver sees it happening. The example is the relation between the speedometer and the odometer. One measures the speed (or velocity); the other measures the distance traveled. We will write $v$ for the velocity, and $f$ for how far the car has gone. The two instruments sit together on the dashboard:

Notice that the units of measurement are different for $v$ and $f .$ The distance $f$ is measured in kilometers or miles (it is easier to say miles). The velocity $v$ is measured in $\mathrm { k m / h r }$ or miles per hour. A unit of time enters the velocity but not the distance. Every formula to compute $v$ from $f$ will have $f$ divided by time.

The central question of calculus is the relation between v and $f .$

Can you find $v$ if you know $f ,$ and vice versa, and how ? If we know the velocity over the whole history of the car, we should be able to compute the total distance traveled. In other words, if the speedometer record is complete but the odometer is missing, its information could be recovered. One way to do it (without calculus) is to put in a new odometer and drive the car all over again at the right speeds. That seems like a hard way; calculus may be easier. But the point is that the information is there. If we know everything about $v$ ; there must be a method to find $f .$

What happens in the opposite direction, when $f$ is known ? If you have a complete record of distance, could you recover the complete velocity ? In principle you could drive the car, repeat the history, and read off the speed. Again there must be a better way.

The whole subject of calculus is built on the relation between v and $f .$ The question we are raising here is not some kind of joke, after which the book will get serious and the mathematics will get started. On the contrary, I am serious now—and the mathematics has already started. We need to know how to find the velocity from a record of the distance. (That is called differentiation, and it is the central idea of differential calculus.) We also want to compute the distance from a history of the velocity. (That is integration, and it is the goal of integral calculus.)

Differentiation goes from $f$ to $v$ ; integration goes from $v$ to $f .$ : We look first at examples in which these pairs can be computed and understood.

# CONSTANT VELOCITY

Suppose the velocity is fixed at $v = 6 0$ (miles per hour). Then $f$ increases at this constant rate. After two hours the distance is $f = 1 2 0$ (miles). After four hours $f = 2 4 0$ and after $t$ hours $f = 6 0 t$ : We say that $f$ increases linearly with time— its graph is a straight line.

Notice that this example starts the car at full velocity. No time is spent picking up speed. (The velocity is a “step function.”) Notice also that the distance starts at zero; the car is new. Those decisions make the graphs of $v$ and $f$ as neat as possible. One is the horizontal line $v = 6 0$ : The other is the sloping line $f = 6 0 t$ : This $v$ , $f ,$ $t$ relation needs algebra but not calculus:

The opposite is also true. When $f$ increases linearly, $v$ is constant. The division by time gives the slope. The distance is $f _ { 1 } = 1 2 0$ miles when the time is $t _ { 1 } = 2$ hours. Later $f _ { 2 } = 2 4 0$ miles at $t _ { 2 } = 4$ hours. At both points, the ratio $f / t$ is 60 miles=hour. Geometrically, the velocity is the slope of the distance graph:

$$
{ \mathrm { s l o p e } } = { \frac { { \mathrm { c h a n g e ~ i n ~ d i s t a n c e } } } { { \mathrm { c h a n g e ~ i n ~ t i m e } } } } = { \frac { v t } { t } } = v .
$$

The slope of the $f$ -graph gives the v-graph. Figure 1.3 shows two more possibilities:

1. The distance starts at 20 instead of 0: The distance formula changes from 60t to $2 0 + 6 0 t$ : The number 20 cancels when we compute change in distance—so the slope is still 60:   
2. When $v$ is negative, the graph of $f$ goes downward. The car goes backward and the slope of $f = - 3 0 t$ is $v = - 3 0$ :

I don’t think speedometers go below zero. But driving backwards, it’s not that safe to watch. If you go fast enough, Toyota says they measure “absolute values”—the speedometer reads $+ 3 0$ when the velocity is $- 3 0$ : For the odometer, as far as I know it just stops. It should go backward. $\dagger$

# VELOCITY vs. DISTANCE: SLOPE vs. AREA

How do you compute $f$ from $v$ ? The point of the question is to see $f = v t$ on the graphs. We want to start with the graph of $v$ and discover the graph of $f .$ Amazingly, the opposite of slope is area.

The distance $f$ is the area under the $v$ -graph. When $v$ is constant, the region under the graph is a rectangle. Its height is $v$ , its width is $t$ , and its area is $v$ times $t$ : This is integration, to go from $v$ to $f$ by computing the area. We are glimpsing two of the central facts of calculus.

# 1A The slope of the $f$ -graph gives the velocity v. The area under the v-graph gives the distance $f .$

That is certainly not obvious, and I hesitated a long time before I wrote it down in this first section. The best way to understand it is to look first at more examples. The whole point of calculus is to deal with velocities that arenot constant, and from now on $v$ has several values.

EXAMPLE (Forward and back) There is a motion that you will understand right away. The car goes forward with velocity $V$ ; and comes back at the same speed. To say it more correctly, the velocity in the second part is $- V .$ If the forward part lasts until $t = 3$ , and the backward part continues to $t = 6$ , the car will come back where it started. The total distance after both parts will be $f = 0$ :

The $v$ -graph shows velocities $+ V$ and $- V .$ The distance starts up with slope $+ V$ and reaches $f = 3 V .$ : Then the car starts backward. The distance goes down with slope $- V$ and returns to $f = 0$ at $t = 6$ :

Notice what that means. The total area “under” the $v$ -graph is zero! A negative velocity makes the distance graph go downward (negative slope). The car is moving backward. Area below the axis in the $v$ -graph is counted as negative.

# FUNCTIONS

This forward-back example gives practice with a crucially important idea—the concept of a “function.” We seize this golden opportunity to explain functions:

The number $v ( t )$ is the value of the function v at the time t .

The time $t$ is the input to the function. The velocity $v ( t )$ at that time is the output. Most people say $^ { 6 6 } v$ of $t ^ { \prime \prime }$ when t'hey read $v ( t )$ : T he number $^ { * * } v$ of $2 ^ { , , }$ is the velocity when $t = 2$ : The forward-back example has $v ( 2 ) = + V$ and $v ( 4 ) = - V .$ : The function contains the whole history, li'%ke a memory bank that has a record of $v$ at each $t$ :

It is simple to convert forward-back motion into a formula. Here is $v ( t )$ :

$$
v ( t ) = \left\{ \begin{array} { c l l } { { + V } } & { { \mathrm { i f } } } & { { 0 < t < 3 } } \\ { { \mathrm { ? } } } & { { \mathrm { i f } } } & { { t = 3 } } \\ { { - V } } & { { \mathrm { i f } } } & { { 3 < t < 6 } } \end{array} \right.
$$

The right side contains the instructions for finding $v ( t )$ : The input $t$ is converted into the output $+ V$ or $- V .$ : The velocity $v ( t )$ depends on $t$ : In this case the function is “discontinuous,” because the needle jumps at $t = 3$ : The velocity is not defined at that instant. There is no $v ( 3 )$ : (You might argue that $v$ is zero at the jump, but that leads to trouble.) The graph of $f$ has a corner, and we can’t give its slope.

The problem also involves a second function, n¤ame¤ly the distance. The principle behind $f ( t )$ is the same: $f ( t )$ is the distance at time $t$ : It is the net distance forward, and again the instructions change at $t = 3$ : In the forward motion, $f ( t )$ equals $V t$ as before. In the backward half, a calculation is built into the formula for $f ( t )$ :

$$
f ( t ) = \left\{ \begin{array} { l l } { V t } & { { \mathrm { i f } \quad 0 \leqslant t \leqslant 3 } } \\ { V ( 6 - t ) } & { { \mathrm { i f } \quad 3 \leqslant t \leqslant 6 } } \end{array} \right.
$$

At the switching time the right side gives two instructions (one on each line). This would be bad except that they agree: $f ( 3 ) = 3 V . \dagger$ The distance function is “continuous.” There is no jump in $f ,$ ; even when there is a jump in $v$ : After $t = 3$ the distance decreases because of $- V t$ : At $t = 6$ the second instruction correctly gives $f ( 6 ) = 0$ :

# 1.1 Velocity and Distance

Notice something more. The functions were given by graphs before they were given by formulas. The graphs tell you $f$ and $v$ at every time t—sometimes more clearly than the formulas. The values $f ( t )$ and $v ( t )$ can also be given by tables or equations or a set of instructions. (In some way all functions are instructions—the function tells how to find $f$ at time $t$ :) Part of knowing $f$ is knowing all its inputs and outputs—its domain and range:

The domain of a function is the set of inputs. The range is the set of outputs.

The domain of $f$ consists of all times $0 \leqslant t \leqslant 6$ : The range consists of all distances $0 \leqslant f ( t ) \leqslant 3 V .$ (The range of $v$ contains only the two velocities $+ V$ and $- V . )$ We mention now, and repeat later, that every “linear” function has a formula $\begin{array} { r } { f ( t ) = v t + C } \end{array}$ : Its graph is a line and $v$ is the slope. The constant $C$ moves the line up and down. It adjusts the line to go through any desired starting point.

# SUMMARY: MORE ABOUT FUNCTIONS

May I collect together the ideas brought out by this example ? We had two functions $v$ and $f .$ One was velocity, the other was distance. Each function had a domain, and a range, and m&ost importantÑa graph. For the $f$ -grÑaph we studied the.slope (which agreed with $v$ ). For the $v$ -grapÑh we studied the areaÑ(which agreed with $f$ ). Calculus produces functions in pairs, aÑnd the best thing a bÑook can do early is to show you more of them.

$$
\begin{array} { r }  i n ( \begin{array} { l } { i n } \\ { t h e } \\ { d o m a i n } \end{array} \{ \begin{array} { l l } { i n p u t \ t \  } & { f u n c t i o n \ f \quad  \quad o u t p u t \ f ( t ) } \\ { i n p u t \ 2 } \\ { i n p u t \ 7 } \end{array}  \  \quad f u n c t i o n \ v \quad  \quad o u t p u t \ v ( 2 ) \ \} \begin{array} { l } { i n } \\ { t h e } \end{array} \end{array}
$$

Note about the definition of a function. The idea behind the symbol $f ( t )$ is absolutely crucial to mathematics. Words don’t do it justice! By definition, a function is a “rule” that assigns one member of the range to each member of the domain. Or, a function is a set of pairs $( t , f ( t ) )$ with no $t$ appearing twice. (These are “ordered pairs” because we write $t$ before $f ( t )$ :) Both of those definitions are correct—but somehow they are too passive.

In practice what matters is the active part. The number $f ( t )$ is produced from the number $t$ : We read a graph, plug into a formula, solve an equation, run a computer program. The input $t$ is “mapped” to the output $f ( t )$ , which changes as $t$ changes. Calculus is about the rate of change. This rate is our other function $v$ :

It is quite hard at the beginning, and not automatic, to see the difference between $f ( t ) - 2$ and $f ( t - 2 )$ : Those are both new functions, created out of the original $f ( t )$ : In $f ( t ) - 2$ , we subtract 2 from all the distances. That moves the whole graph down. In $f ( t - 2 )$ , we subtract 2 fro¤m th¤e time.¤That m¤oves the graph over to the right. Figure 1.5 shows both movements, starting from $f ( t ) = 2 t + 1$ : The formula to find $f ( t - 2 )$ is $2 ( t - 2 ) + 1$ , which is $2 t - 3$ :

A graphing calculator also moves the graph, when you change the viewing window. You can pick any rectangle $A \leqslant t \leqslant B , C \leqslant f ( t ) \leqslant D$ : The screen shows that part of the graph. But on the calculator, the function $f ( t )$ remains the same. It is the axes that get renumbered. In our figures the axes stay the same and the function is changed.

There are two more basic ways to change a function. (We are always creating new functions—that is what mathematics is all about.) Instead of subtracting or adding, we can multiply the distance by 2: Figure 1.6 shows $2 f ( t )$ : And instead of shifting the time, we can speed it up. The function becomes $f ( 2 t )$ : Everything happens twice as fast (and takes half as long). On the calculator those changes correspond to a “zoom” —on the $f$ axis or the $t$ axis. We soon come back to zooms.