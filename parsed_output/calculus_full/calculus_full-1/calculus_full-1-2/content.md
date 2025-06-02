# 1.2 Calculus Without Limits

The next page is going to reveal one of the key ideas behind calculus. The discussion is just about numbers—functions and slopes can wait. The numbers are not even special, they can be any numbers. The crucial point is to look at their differences:

The differences are printed in between, to show $2 - 0 = 2$ and $6 - 2 = 4$ and $7 - 6 = 1$ : Notice how $4 - 7$ gives a negative answer $^ { - 3 }$ : The numbers in $f$ can go up or down, the differences in $v$ can be positive or negative. The idea behind calculus comes when you add up those differences:

$$
\pmb { 2 + 4 + 1 - 3 + 5 } = \pmb { 9 }
$$

The sum of differences is 9: This is the last number on the top line (in $f ^ { \cdot }$ ). Is this an accident, or is this always true ? If we stop earlier, after $2 + 4 + 1$ , we get the 7 in $f .$ Test any prediction on a second example:

$$
{ \begin{array} { l } { { \mathrm { S u p p o s e ~ t h e ~ n u m b e r s ~ a r e ~ } } f = 1 \quad 3 \quad 7 \quad 8 \quad 5 \quad 1 0 } \\ { { \mathrm { T h e i r ~ d i f f e r e n c e s ~ a r e ~ } } v = \qquad 2 \quad 4 \quad 1 \quad - 3 \quad 5 } \end{array} }
$$

The $f$ ’s are increased by 1: The differences are exactly the same—no change. The sum of differences is still 9: But the last $f$ is now 10: That prediction is not right, we don’t always get the last $f .$ :

The first $f$ is now 1: Theanswer 9 (the sum of differences) is $^ { 1 0 - 1 }$ , the last $f$ minus the first $f .$ What happens when we change the $f$ ’s in the middle ?

The differences add to $4 + 7 - 5 + 3 = 9$ : This is still 10 1: No matter what $f$ ’s we choose or how many, the sum of differences is controlled by the first $f$ and last $f .$ If this is always true, there must be a clear reason why the middle $f ^ { \prime } s$ cancel out.

The sum of differences is $( 5 - 1 ) + ( 1 2 - 5 ) + ( 7 - 1 2 ) + ( 1 0 - 7 ) = 1 0 - 1 .$

The 5’s cancel, the 12’s cancel, and the 7’s cancel. It is only $1 0 - 1$ that doesn’t cancel. This is the key to calculus!

1B The differences of the $f$ ’s add up to $( f _ { \mathrm { l a s t } } - f _ { \mathrm { f i r s t } } )$ .

EXAMPLE 1 The numbers grow linearly: $\begin{array} { l } { { \begin{array} { l l l l l l l } { { \epsilon = } } & { { 2 } } & { { 3 } } & { { 4 } } & { { 5 } } & { { 6 } } & { { 7 } } \\ { { \it { \cdot \ v = } } } & { { 1 } } & { { 1 } } & { { 1 } } & { { 1 } } & { { 1 } } \end{array} } } \end{array}$ Their differences are constant:

The sum of differences is certainly 5: This agrees with $7 - 2 = f _ { \mathrm { l a s t } } - f _ { \mathrm { f i r s t } }$ : The numbers in $v$ remind us of constant velocity. The numbers in $f$ remind us of a straight line $f = v t + C$ : This example has $v = 1$ and the $f$ ’s start at 2: The straight line would come from $f = t + 2$ :

EXAMPLE 2 The numbers are squares: $\begin{array} { r l r l } { f = } & { { } } & { 0 } \end{array}$ 1 4 9 16 Their differences grow linearly: $\boldsymbol { v } = \mathrm { ~ \scriptsize ~ 1 ~ \ 3 ~ \ 5 ~ \ 7 ~ }$

$1 + 3 + 5 + 7$ agrees with $4 ^ { 2 } = 1 6$ : It is a beautiful fact that the first $j$ odd numbers always add up to $j ^ { 2 }$ : The $v$ ’s are the odd numbers, the $f$ ’s are perfect squares.

Note The letter $j$ is sometimes useful to tell which number in $f$ we are looking at. For this example the zeroth number is $f _ { 0 } = 0$ and the $j$ th number is $f _ { j } = j ^ { 2 }$ : This is a part of algebra, to give a formula for the $f$ ’s instead of a list of numbers. We can also use $j$ to tell which difference we are looking at. The first $v$ is the first odd number $v _ { 1 } = 1$ : The $j$ th difference is the $j$ th odd number $v _ { j } = 2 j - 1$ : (Thus $v _ { 4 }$ is $8 - 1 = 7 .$ ) It is better to start the differences with $j = 1$ , since there is no zeroth odd number $v _ { 0 }$ :

With this notation the $j$ th difference is $v _ { j } = f _ { j } - f _ { j - 1 }$ : Sooner or later you will get comfortable with subscripts like $j$ and $j - 1$ , but it can be later. The important point is that the sum of the $v$ ’s equals $f _ { \mathrm { l a s t } } - f _ { \mathrm { f i r s t } }$ : We now connect the $v$ ’s to slopes and the $f$ ’s to areas.

Figure 1.7 shows a natural way to graph Example 2, with the odd numbers in $v$ and the squares in $f .$ Notice an important difference between the $v$ -graph and the $f$ -graph. The graph of $f$ is “piecewise linear.” We plotted the numbers in $f$ and connected them by straight lines. The graph of $v$ is “piecewise constant.” We plotted the differences as constant over each piece. This reminds us of the distance-velocity graphs, when the distance $f ( t )$ is a straight line and the velocity $v ( t )$ is a horizontal line.

Now make the connection to slopes:

$$
{ \frac { { \mathrm { d i s t a n c e ~ u p } } } { { \mathrm { d i s t a n c e ~ a c r o s s } } } } = { \frac { \mathrm { c h a n g e ~ i n ~ } f } { \mathrm { c h a n g e ~ i n ~ } t } } = v .
$$

Over each piece, the change in $t$ (across) is 1: The change in $f$ (upward) is the difference that we are calling $v$ : The ratio is the slope $v / 1$ or just $v$ : The slope makes a sudden change at the breakpoints $t = 1 , 2 , 3$ ; : : :. At thosespecial points the slope of the $f .$ -graph is not defined—we connected the $v$ ’s by vertical lines but this is very debatable. The main idea is that between the breakpoints, the slope of $f ( t )$ is $v ( t )$ .

Now make the connection to areas:

# The total area under the $v$ -graph is $f _ { \mathrm { l a s t } } - f _ { \mathrm { f i r s t } }$ :

This area, underneath the staircase in Figure 1.7, is composed of rectangles. The base of every rectangle is 1: The heights of the rectangles are the v’s. So the areas also equal the $v$ ’s, and the total area is the sum of the $v$ ’s. This area is $f _ { \mathrm { l a s t } } - f _ { \mathrm { f i r s t } }$ :

Even more is true. We could start at any time and end at any later time— not necessarily at the special times $t = 0 , 1 , 2 , 3 , 4$ : Suppose we stop at $t = 3 . 5$ : Only half of the last rectangular area (under $v = 7$ ) will be counted. The total area is $1 + 3 + 5 + { \textstyle { \frac { 1 } { 2 } } } ( 7 ) = 1 2 . 5$ : This still agrees with $f _ { \mathrm { l a s t } } - f _ { \mathrm { f i r s t } } = 1 2 . 5 - 0$ : At this new ending time $t = 3 . 5$ , we are only halfway up the last step in the $f$ -graph. Halfway between 9 and 16 is 12:5:

1C The v’s are slopes of $f ( t )$ : The area under the $v$ -graph is $f ( t _ { \mathrm { e n d } } ) - f ( t _ { \mathrm { s t a r t } } )$ :

This is nothing less than the Fundamental Theorem of Calculus. But we have only used algebra (no curved graphs and no calculations involving limits). For now the Theorem is restricted to piecewise linear $f ( t )$ and piecewise constant $v ( t )$ : In Chapter 5 that restriction will be overcome.

Notice that a proof of $1 + 3 + 5 + 7 = 4 ^ { 2 }$ is suggested by Figure 1.7a. The triangle under the dotted line has the same area as the four rectangles under the staircase. The area of the triangle is $\begin{array} { r } { \frac { 1 } { 2 } \cdot { \mathrm { b a s e } } \cdot { \mathrm { h e i g h t } } = \frac { 1 } { 2 } \cdot 4 \cdot 8 } \end{array}$ , which is the perfect square $4 ^ { 2 }$ : When there are $j$ rectangles instead of 4, we get ${ \frac { 1 } { 2 } } \cdot j \cdot 2 j = j ^ { 2 }$ for the area.

The next examples show other patterns, where $f$ and $v$ increase exponentially or   
oscillate around zero. I hope you like them but I don’t think you have to learn them.   
They are like the special functions $2 ^ { t }$ and sin $t$ and cos t—except they go in steps.   
You get a first look at the important functions of calculus, but you only need algebra.   
Calculus is needed for a steadily changing velocity, when the graph of $f$ is curved.

The last example will be income tax—which really does go in steps. Then Section 1:3 will introduce the slope of a curve. The crucial step for curves is working with limits. That will take us from algebra to calculus.

# EXPONENTIAL VELOCITY AND DISTANCE

Start with the numbers $f = 1 , 2 , 4 , 8 , 1 6$ : These are “powers of 2:” They start with the zeroth power, which is $2 ^ { 0 } = 1$ : The exponential starts at 1 and not 0. After $j$ steps there are $j$ factors of 2, and $f _ { j }$ equals $2 ^ { j }$ : Please recognize the difference between $2 j$ and $j ^ { 2 }$ and $2 ^ { j }$ . The numbers $2 j$ grow linearly, the numbers $j ^ { 2 }$ grow quadratically, the numbers $2 ^ { j }$ grow exponentially. At $j = 1 0$ these are 20 and 100 and 1024: The exponential $2 ^ { j }$ quickly becomes much larger than the others.

The differences of $f = 1 , 2 , 4 , 8 , 1 6$ are exactly $v = 1 , 2 , 4 , 8$ : We get the same beautiful numbers. When the $f$ ’s are powers of 2; so are the $v$ ’s. The formula $v _ { j } = 2 ^ { j - 1 }$ is slightly different from $f _ { j } = 2 ^ { j }$ , because the first $v$ is numbered $v _ { 1 }$ : (Then $v _ { 1 } = 2 ^ { 0 } = 1$ : The zeroth power of every number is 1, except that $0 ^ { 0 }$ is meaningless.) The two graphs in Figure 1.8 use the same numbers but they look different, because $f$ is piecewise linear and $v$ is piecewise constant.

Where will calculus come in ? It works with the smooth curve $f ( t ) = 2 ^ { t }$ : This exponential growth is critically important for population and money in a bank and the national debt. You can spot it by the following test: $v ( t )$ is proportional to $f ( t )$ :

# 1 Introduction to Calculus

Remark The function $2 ^ { t }$ is trickier than $t ^ { 2 }$ : For $f = t ^ { 2 }$ the slope is $v = 2 t$ : It is proportional to $t$ and not $t ^ { 2 }$ : For $f = 2 ^ { t }$ the slope is $v = c 2 ^ { t }$ , and we won’t find the constant $c = . 6 9 3 \ldots$ until Chapter 6: (The number $c$ is the natural logarithm of 2:) Problem 37 estimates $c$ with a calculator—the important thingis that it’s constant.

# OSCILLATING VELOCITY AND DISTANCE

We have seen a forward-back motion, velocity $V$ followed by $- V .$ That is oscillation of the simplest kind. The graph of $f$ goes linearly up and linearly down. Figure 1.9 shows another oscillation that returns to zero, but the path is more interesting.

The numbers in $f$ are now $0 , 1 , 1 , 0 , - 1 , - 1 , 0$ : Since $f _ { 6 } = 0$ the motion brings us back to the start. The whole oscillation can be repeated.

The differences in $v$ are $1 , 0 , - 1 , - 1 , 0 , 1$ : They add up to zero, which agrees with $f _ { \mathrm { l a s t } } - f _ { \mathrm { f i r s t } }$ : It is the same oscillation as in $f$ (and also repeatable), but shifted in time.

The $f$ -graph resembles (roughly) a sine curve. The $v$ -graph resembles (even more roughly) a cosine curve. The waveforms in nature are smooth curves, while these are “digitized”—the way a digital watch goes forward in jumps. You recognize that the change from analog to digital brought the computer revolution. The same revolution is coming in CD players. Digital signals (off or on, 0 or 1) seem to win every time.

The piecewise $v$ and $f$ start again at $t = 6$ : The ordinary sine and cosine repeat at $t = 2 \pi$ : A repeating motion is periodic—here the “period” is 6 or $2 \pi$ : (With $t$ in degrees the period is 360—a full circle. The period becomes $2 \pi$ when angles are measured in radians. We virtually always use radians—which are degrees times $2 \pi / 3 6 0 . )$ 1 A watch has a period of 12 hours. If the dial shows AM and PM, the period is

# A SHORT BURST OF SPEED

The next example is a car that is driven fast for a short time. The speed is $V$ until the distance reaches $f = 1$ , when the car suddenly stops. The graph of $f$ goes up linearly with slope $V$ , and then across with slope zero:

$$
v ( t ) = \{ { \begin{array} { c l } { V } & { { \mathrm { ~ u p ~ t o ~ } } t = T } \\ { 0 } & { { \mathrm { ~ a f t e r ~ } } t = T } \end{array} } \qquad f ( t ) = \{ { \begin{array} { c l } { V t } & { { \mathrm { ~ u p ~ t o ~ } } t = T } \\ { 1 } & { { \mathrm { ~ a f t e r ~ } } t = T } \end{array} } 
$$

This is another example of “function notation.” Notice the general time $t$ and the particular stopping time $T _ { \mathbf { \delta } }$ : The distance is $f ( t )$ : The domain of $f$ (the inputs) includes all times $t \geqslant 0$ : The range of $f$ (the outputs) includes all distances $0 \leqslant f \leqslant 1$ :

Figure 1.10 allows us to compare three cars—a Jeep and a Corvette and a Maserati. They have different speeds but they all reach $f = 1$ : So the areas under the $v$ -graphs are all 1: The rectangles have height $V$ and base $T = 1 / V .$

Optional remark It is natural to think about faster and faster speeds, which means steeper slopes. The $f$ -graph reaches 1 in shorter times. The extreme case is a step function, when the graph of $f$ goes straight up. This is the unit step $U ( t )$ , which is zero up to $t = 0$ and jumps immediately to $U = 1$ for $t > 0$ :

What is the slope of the step function ? It is zero except at the jump. At that moment, which is $t = 0$ , the slope is infinite. We don’t have an ordinary velocity $v ( t )$ —instead we have an impulse that makes the car jump. The graph is a spike over the single point $t = 0$ , and it is often denoted by $\delta$ —so the slope of the step function is called a “delta function.” The area under the infinite spike is 1:

You are absolutely not responsible for the theory of delta functions! Calculus is about curves, not jumps.

Our last example is a real-world application of slopes ands rates—to explain “how taxes work.” Note especially the difference between tax rates and tax brackets and total tax. The rates are $v$ , the brackets are on $x$ , the total tax is $f .$

# EXAMPLE 3 Income tax is piecewise linear. The slopes are the tax rates :15; :28; :31:

Suppose you¤are¤single with taxable income of $x$ dollars (Form 1040; line 37—after all deductions). These are the 1991 instructions from the Internal Revenue Service:

If $x$ is not over $\$ 20,350$ ; the tax is $1 5 \%$ of $x$ :

If $\$ 20,350 \leqslant x \leqslant \$ 49,300$ ; the tax is $\$ 3052.50+28 \%$ of the amount¤ove¤r $\$ 20,350$ :

If $x$ is over $\$ 49,300$ ; the tax is $\$ 123,458.50+31\%$ of the amount over $\$ 49,300$ :

The first bracket is $0 \leqslant x \leqslant \Phi 2 0 , 3 5 0$ : (The IRS never uses this symbol $\leqslant$ , but I think it is OK here.We know what it means.)Thesecond bracket is $\$ 20,350 \leqslant x \leqslant \$ 49,300$ : The top bracket $x \geqslant \$ 49,300$ pays tax at the top rate of $31 \%$ : But only the income in that bracket is taxed at that rate.

Figure 1.11 shows the rates and the brackets and the tax due. Those are not average rates, they are marginal rates. Total tax divided by total income would be the average rate. The marginal rate of .28 or :31 gives the tax on each additional dollar of income— it is the slope at the point $x$ : Tax is like area or distance—it adds up. Tax rate is like slope or velocity—it depends where you are. This is often unclear in the news media.

Question What is the equation for the straight line in the top bracket ?

Answer The bracket begins at $x = \mathfrak { F } 4 9 , 3 0 0$ when the tax is $f ( x ) = \mathbb { S } 1 1 , 1 5 8 . 5 0$ : The slope of the line is the tax rate :31: When we know a point on the line and the slope, we know the equation. This is important enough to be highlighted.

1D For $x$ in the top bracket the tax is $f ( x ) = \$ 123,456.50+.31( x -\mathbb { S } 4 9 , 30 0 )$ : This is the tax on $\$ 49,300$ plus the extra tax on extra income.

Section 2:3 presents this “point-slope equation” for any straight line. Here you see it for one specific example. Where does the number $\$ 11$ ;158:50 come from ? It is the tax at the end of the middle bracket, so it is the tax at the start of thetop bracket.

Figure 1.11 also shows a distance-velocity example. The distance at $t = 2$ is $f ( 2 ) = 4 0$ miles. After that time the velocity is 60 miles per hour. So the line with slope 60 on the $f$ -graph has the equation

$$
f ( t ) = { \mathrm { s t a r t i n g ~ d i s t a n c e } } + { \mathrm { e x t r a ~ d i s t a n c e } } = 4 0 + 6 0 ( t - 2 ) .
$$

The starting point is .2; 40/: The new speed 60 multiplies the extra time $t - 2$ : The point-slope equation makes sense. We now review this section, with comments.

Central idea Start with any numbers in $f .$ Their differences go in $v$ : Then the sum of those differences is flast ffirst:

Subscript notation The numbers are $f _ { 0 } , f _ { 1 } , \ldots$ and the first difference is $v _ { 1 } = f _ { 1 } - f _ { 0 }$ : A typical number is $f _ { j }$ and the $j$ th difference is $v _ { j } = f _ { j } - f _ { j - 1 }$ : When those differences are added, all $f$ ’s in the middle (like $f _ { 1 }$ ) cancel out:

$$
v _ { 1 } + v _ { 2 } + \cdots + v _ { j } = ( f _ { 1 } - f _ { 0 } ) + ( f _ { 2 } - f _ { 1 } ) + \cdots + ( f _ { j } - f _ { j - 1 } ) = f _ { j } - f _ { 0 } .
$$

Examples $f _ { j } = j$ or $j ^ { 2 }$ or $2 ^ { j }$ : Then $v _ { j } = 1$ (constant) or $2 j - 1$ (odd numbers) or 2j 1:

Functions Connect the $f$ ’s to be piecewise linear. Then the slope $v$ is piecewise constant. The area under the $v$ -graph from any $t _ { \mathrm { s t a r t } }$ to any $t _ { \mathrm { e n d } }$ equals $f ( t _ { \mathrm { e n d } } ) - f ( t _ { \mathrm { s t a r t } } )$ :

Units Distance in miles and velocity in miles per hour. Tax in dollars and tax rate in (dollars paid)=(dollars earned). Tax rate is a percentage like :28, with no units.