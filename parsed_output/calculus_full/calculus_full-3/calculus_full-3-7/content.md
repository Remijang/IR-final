# 3.7 Newton’s Method (and Chaos)

The equation to be solved is $f ( x ) = 0$ : Its solution $x ^ { * }$ is the point 1where the graph crosses the $x$ axis. Figure 3.22 shows $x ^ { * }$ and a starting guess $x _ { 0 }$ : Our goal is to come as close as possible to $x ^ { * }$ , based on the information $f ( x _ { 0 } )$ and $f ^ { \prime } ( x _ { 0 } )$ .

Section 3.6 reached Newton’s formula for $x _ { 1 }$ (the next guess). We now do that directly.

What do we see at $x _ { 0 }$ ? The graph has height $f ( x _ { 0 } )$ and slope $f ^ { \prime } ( x _ { 0 } )$ : We know where we are, and which direction the curv1e is going. We don’t know if the curve bends (we don’t have $f ^ { \prime \prime } )$ . The best plan is to follow the tangent line, which uses all the information we have.

Newton replaces $f ( x )$ by its linear approximation $\circeq$ tangent approximation):

$$
f ( x ) \approx f ( x _ { 0 } ) + f ^ { \prime } ( x _ { 0 } ) ( x - x _ { 0 } ) .
$$

We want the left side to be zero. The best we can do is to make the right side zero! The tangent line crosses the axis at $x _ { 1 }$ , while t1he curve crosses at $x ^ { * }$ : The new guess $x _ { 1 }$ comes from $f ( x _ { 0 } ) + f ^ { \prime } ( x _ { 0 } ) ( x _ { 1 } - x _ { 0 } ) = 0$ : Dividing by $f ^ { \prime } ( x _ { 0 } )$ and solving for $x _ { 1 }$ , this is step 1 of Newton’s method:

$$
x _ { 1 } = x _ { 0 } - { \frac { f ( x _ { 0 } ) } { f ^ { \prime } ( x _ { 0 } ) } } .
$$

At this new point, compute $f ( x _ { 1 } )$ and $f ^ { \prime } ( x _ { 1 } )$ —the height and slope at $x _ { 1 }$ : They give a new tangent line, which crosses at $x _ { 2 } . A t$ every step we want $f ( x _ { n + 1 } ) = 0$ and we settle for $f ( x _ { n } ) + f ^ { \prime } ( x _ { n } ) ( x _ { n + 1 } - x _ { n } ) = 0$ . After dividing by $f ^ { \prime } ( x _ { n } )$ , the formula for $x _ { n + 1 }$ is Newton’s method.

3L The tangent line from $x _ { n }$ crosses the axis at $x _ { n + 1 }$ : Newton’s method $x _ { n + 1 } = x _ { n } - { \frac { f ( x _ { n } ) } { f ^ { \prime } ( x _ { n } ) } } .$ (3) Usually this iteration $x _ { n + 1 } = F ( x _ { n } )$ converges quickly to $x ^ { * }$ :

Linear approximation involves three numbers. They are $\Delta x$ (across) and $\Delta f$ (up) and the slope $f ^ { \prime } ( x )$ : If we know two of those numbers, we can estimate the third. It is remarkable to realize that calculus has n1ow used all three calculations—they are the key to this subject:

$$
\begin{array} { r l } & { 1 . \ E s t i m a t e \ t h e \ s l o p e \ f ^ { \prime } ( x ) f r o m \ \Delta f / \Delta x } \\ & { 2 . \ E s t i m a t e \ t h e \ c h a n g e \Delta f f r o m \ f ^ { \prime } ( x ) \Delta x } \\ & { 3 . \ E s t i m a t e \ t h e \ c h a n g e \Delta x f r o m \Delta f / f ^ { \prime } ( x ) } \end{array}
$$

The desired $\Delta f$ is $- f ( x _ { n } )$ : Formula .3/ is exactly $\Delta x = - f ( x _ { n } ) / f ^ { \prime } ( x _ { n } )$ :

EXAMPLE 1 (Square roots) $f ( x ) = x ^ { 2 } - b$ is zero at $x ^ { * } = { \sqrt { b } }$ and also at $- { \sqrt { b } }$ : Newton’s method is a quick way to find square roots—probably built into your calculator. The slope is $f ^ { \prime } ( x _ { n } ) = 2 x _ { n }$ , and formula .3/ for the new guess becomes

$$
x _ { n + 1 } = x _ { n } - { \frac { x _ { n } ^ { 2 } - b } { 2 x _ { n } } } = x _ { n } - { \frac { 1 } { 2 } } x _ { n } + { \frac { b } { 2 x _ { n } } } .
$$

This simplifies to $\begin{array} { r } { x _ { n + 1 } = \frac { 1 } { 2 } ( x _ { n } + b / x _ { n } ) } \end{array}$ : Guess the square root, divide into $b$ ; and average the two numbers. The ancient Babylonians had this same idea, without knowing functions or slopes. They iterated $x _ { n + 1 } = F ( x _ { n } )$ :1

$$
F ( x ) = { \frac { 1 } { 2 } } \left( x + { \frac { b } { x } } \right) \quad { \mathrm { a n d } } \quad F ^ { \prime } ( x ) = { \frac { 1 } { 2 } } \left( 1 - { \frac { b } { x ^ { 2 } } } \right) .
$$

The Babylonians did exactly the right thing. The slope $F ^ { \prime }$ is zero at the solution, when $x ^ { 2 } = b$ : That makes Newton’s method converge at high speed. The convergence test is $\vert F ^ { \prime } ( x ^ { * } ) \vert < 1 .$ : Newton achieves $F ^ { \prime } ( x ^ { * } ) = 0 $ —which is superconvergence.

To find $\sqrt { 4 }$ , start the iteration $x _ { n + 1 } = { \textstyle { \frac { 1 } { 2 } } } ( x _ { n } + 4 / x _ { n } )$ at $x _ { 0 } = 1$ : Then $\textstyle x _ { 1 } = { \frac { 1 } { 2 } } ( 1 + 4 )$ :

$$
x _ { 1 } = 2 . 5 x _ { 2 } = 2 . 0 5 x _ { 3 } = 2 . 0 0 0 6 x _ { 4 } = 2 . 0 0 0 0 0 0 0 9 .
$$

The wrong decimal istwice as far out at each step. The error is squared. Subtracting $x ^ { * } = 2$ from both sides of $x _ { n + 1 } = F ( x _ { n } )$ gives an error equation which displays that square:

$$
x _ { n + 1 } - 2 = { \frac { 1 } { 2 } } \left( x _ { n } + { \frac { 4 } { x _ { n } } } \right) - 2 = { \frac { 1 } { 2 x _ { n } } } ( x _ { n } - 2 ) ^ { 2 } .
$$

This is $\scriptstyle ( e r r o r ) _ { n + 1 } \approx { \frac { 1 } { 4 } } ( e r r o r ) _ { n } ^ { 2 }$ : It explains the speed of Newton’s method.

Remark 1 You can’t start this iteration at $x _ { 0 } = 0$ : The first step computes $4 / 0$ and blows up. Figure 3.22a shows why—the tangent line at zero is horizontal. It will never cross the axis.

Remark 2 Starting at $x _ { 0 } = - 1$ , Newton converges to $- { \sqrt { 2 } }$ instead of $+ \sqrt { 2 }$ : That is the other $x ^ { * }$ : Often it is difficult to predict which $x ^ { * }$ Newton’s method will choose. Around every solution is a “basin of attraction,” but other parts of the basin may be far away. Numerical experiments are needed, with many starts $x _ { 0 }$ : Finding basins of attraction was one of the problems that led to fractals.

EXAMPLE 2 $S o l \nu e \ \frac { 1 } { x } - a = 0$ to find $x ^ { * } = { \frac { 1 } { a } }$ without dividing by $a$ .

Here $f ( x ) = ( 1 / x ) - a$ : Newton uses $f ^ { \prime } ( x ) = - 1 / x ^ { 2 }$ : Surprisingly, we don’t divide:

$$
x _ { n + 1 } = x _ { n } - { \frac { ( 1 / x _ { n } ) - a } { - 1 / x _ { n } ^ { 2 } } } = x _ { n } + x _ { n } - a x _ { n } ^ { 2 } .
$$

Do these iterations converge ? I will take $a = 2$ and aim for $\begin{array} { r } { x ^ { * } = \frac { 1 } { 2 } } \end{array}$ : Subtracting $\frac { 1 } { 2 }$ from both sides of .7/ changes the iteration into the error equation:

$$
x _ { n + 1 } = 2 x _ { n } - 2 x _ { n } ^ { 2 } { \mathrm { b e c o m e s } } x _ { n + 1 } - { \frac { 1 } { 2 } } = - 2 \left( x _ { n } - { \frac { 1 } { 2 } } \right) ^ { 2 } .
$$

At each step the error is squared. This is terrific if (and only if) you are close to $\begin{array} { r } { x ^ { * } = \frac { 1 } { 2 } } \end{array}$ : Otherwise squaring a large error and multiplying by $- 2$ is not good:

$$
\begin{array} { l l l l l } { { x _ { 0 } = . 7 0 } } & { { x _ { 1 } = . 4 2 } } & { { x _ { 2 } = . 4 8 7 } } & { { x _ { 3 } = . 4 9 9 7 } } & { { x _ { 4 } = . 4 9 9 9 9 9 8 } } \\ { { x _ { 0 } = 1 . 2 1 } } & { { x _ { 1 } = - . 5 } } & { { x _ { 2 } = - 1 . 5 } } & { { x _ { 3 } = - 7 . 5 } } & { { x _ { 4 } = - 1 2 7 . 5 } } \end{array}
$$

The algebra in Problem 18 confirms those experiments. There is fast convergence if $0 < x _ { 0 } < 1$ : There is divergence if $x _ { 0 }$ is negative or $x _ { 0 } > 1$ : The tangent line goes to a negative $x _ { 1 }$ : After that Figure 3.22 shows a long trip backwards.

In the previous section we drew $F ( x )$ : The iteration $x _ { n + 1 } = F ( x _ { n } )$ converged to the $4 5 ^ { \circ }$ line, where $x ^ { * } = F ( x ^ { * } )$ : In this section we are drawing $f ( x )$ 1: Now $x ^ { * }$ is the point on the axis where $f ( x ^ { * } ) = 0$ :

To repeat: It is $f ( x ^ { * } ) = 0$ that we aim for. But it is the slope $F ^ { \prime } ( x ^ { * } )$ that decides whether we get there. Example 2 has $F ( x ) = 2 x - 2 x ^ { 2 }$ : The fixed points are $\begin{array} { r } { x ^ { * } = \frac { 1 } { 2 } } \end{array}$ (our solution) and $x ^ { * } = 0$ (not attr1active). The slopes $F ^ { \prime } ( x ^ { * } )$ are zero (typical Newton) and 2 (typical repeller). The key to Newton’s method is $F ^ { \prime } { = } 0$ at the solution:

The examples $x ^ { 2 } = b$ and $1 / x = a$ show fast convergence or failure. In Chapter 13, and in reality, Newton’s method solves much harder equations. Here I am going to choose a third example that came from pure curiosity about what might happen. The results are absolutely amazing. The equation is $x ^ { 2 } = - 1$ :

EXAMPLE 3 What happens to Newton’s method if you ask it to solve $f ( x ) = x ^ { 2 } + 1 = 0 ^ { . }$ ?

The only solutions are the imaginary numbers $x ^ { * } = i$ and $x ^ { * } = - i$ : There is no real square root of $^ { - 1 }$ : Newton’s method might as well give up. But it has no way to know that! The tangent line still crosses the axis at a new point $x _ { n + 1 }$ , even if the curve $y = x ^ { 2 } + 1$ never crosses. Equation (5) still gives the iteration for $b = - 1$ :

$$
x _ { n + 1 } = { \frac { 1 } { 2 } } \left( x _ { n } - { \frac { 1 } { x _ { n } } } \right) = F ( x _ { n } ) .
$$

The $x$ ’s cannot approach $i$ or $- i$ (nothing is imaginary). So what do they do ?

The starting guess $x _ { 0 } = 1$ is interesting. It is followed by $x _ { 1 } = 0$ : Then $x _ { 2 }$ divides by zero and blows up. I expected other sequences to go to infinity. But the experiments showed something different (and mystifying). When $x _ { n }$ is large, $x _ { n + 1 }$ is less than half as large. After $x _ { n } = 1 0$ comes $\begin{array} { r } { x _ { n + 1 } = \frac { 1 } { 2 } ( 1 0 - \frac { 1 } { 1 0 } ) = 4 . 9 5 } \end{array}$ : After much indecision and a long wait, a number near zero eventually appears. Then the next guess divides by that small number and goes far out again. This reminded me of “chaos.”



It is temptingto retreat to ordinary examples, where Newton’s method is a big success. By trying exercises from the book or equations of your own, you will see that the fast convergence to $\sqrt { 4 }$ is very typical. The function can be much more complicated than $x ^ { 2 } - 4$ (in practice it certainly is). The iteration for $2 x = \cos x$ was in the previous section, and the error was squared at every step. If Newton’smethod starts close to $x ^ { * }$ , its convergence is overwhelming. That has to be the main point of this section: Follow the tangent line.

Instead of those good functions, may I stay with this strange example $x ^ { 2 } + 1 = 0 ?$ It is not so predictable, and maybe not so important, but somehow it is more interesting. There is no real solution $x ^ { * }$ , and Newton’s method $\begin{array} { r } { x _ { n + 1 } = \frac { 1 } { 2 } ( x _ { n } - 1 / x _ { n } ) } \end{array}$ bounces around. We will now discover $x _ { n }$ :

# A FORMULA FOR xn

The key is an exercise from trigonometry books. Most of those problems just give practice with sines and cosines, but this one exactly fits $\textstyle { \frac { 1 } { 2 } } ( x _ { n } - 1 / x _ { n } )$ :

$$
{ \frac { 1 } { 2 } } \left( { \frac { \cos \theta } { \sin \theta } } - { \frac { \sin \theta } { \cos \theta } } \right) = { \frac { \cos 2 \theta } { \sin 2 \theta } } \qquad { \mathrm { o r } } \qquad { \frac { 1 } { 2 } } \left( \cot \theta - { \frac { 1 } { \cot \theta } } \right) = \cot 2 \theta
$$

In the left equation, the common denominator is $2 \sin \theta \cos \theta$ (which is sin $2 \theta$ ). The numerator is $\cos ^ { 2 } \theta - \sin ^ { 2 } \theta$ (which is cos $2 \theta$ ). Replace cosine=sine by cotangent, and the identity says this:

$$
x _ { 0 } = \cot \theta \quad { \mathrm { t h e n } } \quad x _ { 1 } = \cot 2 \theta . \quad { \mathrm { T h e n } } \quad x _ { 2 } = \cot 4 \theta \quad { \mathrm { T h e n } } \quad x _ { n } = \cot 2 ^ { n } \theta .
$$

This is the formula. Our points are on the cotangent curve. Figure 3.23 starts from $x _ { 0 } = 2 = \cot \theta$ , and every iteration doubles the angle.

Example A The sequence $x _ { 0 } = 1 , x _ { 1 } = 0 , x _ { 2 } = \infty$ matches the cotangents of $\pi / 4 , \pi / 2$ , and $\pi$ : This sequence blows up because $x _ { 2 }$ has a division by $x _ { 1 } = 0$ :

Example $B$ The sequence $1 / \sqrt { 3 } , - 1 / \sqrt { 3 } , 1 / \sqrt { 3 }$ matches the cotangents of $\pi / 3 , 2 \pi / 3$ , and $4 \pi / 3$ : This sequence cycles forever because $x _ { 0 } = x _ { 2 } = x _ { 4 } = \dots$

Example $C$ Start with a large $x _ { 0 }$ (a small $\theta$ ). Then $x _ { 1 }$ is about half as large (at $2 \theta$ ). Eventually one of the angles $4 \theta , 8 \theta$ ; : : : hits on a large cotangent, and the $x$ ’s go far out again. This is typical. Examples $A$ and $B$ were special, when $\theta / \pi$ was $\textstyle { \frac { 1 } { 4 } }$ or $\frac 1 3$ :

What we have here is chaos. The $x$ ’s can’t converge. They are strongly repelled by all points. They are also extremely sensitive to the value of $\theta$ : After ten steps $\theta$ is multiplied by $2 ^ { 1 0 } = 1 0 2 4$ : The starting angles $6 0 ^ { \circ }$ and $6 1 ^ { \circ }$ look close, but now they are different by $1 0 2 4 ^ { \circ }$ . If that were a multiple of $1 8 0 ^ { \circ }$ , the cotangents would still be close. In fact the $x _ { 1 0 }$ ’s are 0:6 and 14:

This chaos in mathematics is also seen in nature. The most familiar example is the weather, which is much more delicate than you might think. The headline “Forecasting Pushed Too Far” appeared in Science .1989/. The article said that the snowballing of small errors destroys the forecast after six days. We can’t follow the weather equations for a month—the flight of a plane can change everything. This is a revolutionary idea, that a simple rule can lead to answers that are too sensitive to compute.

We are accustomed to complicated formulas (or no formulas). We are not accustomed to innocent-looking formulas like cot $2 ^ { n } \theta$ , which are absolutely hopeless after 100 steps.

# CHAOS FROM A PARABOLA

Now I get to tell you about new mathematics. First I will change the iteration $x _ { n + 1 } =$ ${ \frac { 1 } { 2 } } ( x _ { n } - 1 / x _ { n } )$ into one that is even simpler. By switching from $x$ to $z = 1 / ( 1 + x ^ { 2 } )$ , each new $z$ turns out to involve only the old $z$ and $z ^ { 2 }$ :

$$
z _ { n + 1 } = 4 z _ { n } - 4 z _ { n } ^ { 2 } .
$$

This is the most famous quadratic iteration in the world. There are books about it, and Problem 28 shows where it comes from. Our formula for $x _ { n }$ leads to $z _ { n }$ :

$$
z _ { n } = { \frac { 1 } { 1 + x _ { n } ^ { 2 } } } = { \frac { 1 } { 1 + ( \cot 2 ^ { n } \theta ) ^ { 2 } } } = ( \sin 2 ^ { n } \theta ) ^ { 2 } .
$$

The sine is just as unpredictable as the cotangent, when $2 ^ { n } \theta$ gets large. The new thing is to locate this quadratic as the last member (when $a = 4$ ) of the family

$$
z _ { n + 1 } = a z _ { n } - a z _ { n } ^ { 2 } , \quad 0 \leqslant a \leqslant 4 .
$$

Example 2 happened to be the middle member $a = 2$ , converging to $\frac { 1 } { 2 }$ : I would like to give a brief and very optional report on this iteration, for different $\boldsymbol { a } ^ { \prime } \mathrm { { s } }$ .

The general principle i¤s to¤start with a number $z _ { 0 }$ between 0 and 1, and compute $z _ { 1 } , z _ { 2 } , z _ { 3 } , \ldots$ It is fascin¤ating¤to watch the behavior change as $a$ increases. You can see it on your own computer. Here we describe some things to look for. All numbers stay between 0 and 1 and they may approach a limit. That happens when $a$ is small:

Those limit points are the solutions of $z = F ( z )$ :T |h¡ey are the fixed points where $z ^ { * } = a z ^ { * } - a ( z ^ { * } ) ^ { 2 }$ : But remember the test for approaching a limit: The slope at $z ^ { * }$ cannot be larger than one. Here $F = a z - a z ^ { 2 }$ has $F ^ { \prime } { = } a - 2 a z$ : It is easy to check $\left| F ^ { \prime } \right| \leqslant 1$ at the limits predicted above. The hard problem—sometimes impossible— is to predict what happens above $a = 3$ : Our case is $a = 4$ :

The $z$ ’s cannot approach a limit when $\left| F ^ { \prime } ( z ^ { * } ) \right| > 1$ . Something has to happen, and there are at least three possibilities:

The $z _ { n }$ ’s can cycle or fill the whole interval $( 0 , 1 )$ or approach a Cantor set.

I start with a random number $z _ { 0 }$ , take 100 steps, and write down steps 101 to 105:

The first column is converging to a “2-cycle.” It alternates between $x = . 8 4 2$ and $y = . 4 5 2$ : Those satisfy $y = F ( x )$ and $x = F ( y ) = F ( F ( x ) ) .$ : If we look at a double step when $a = 3 . 4 , x$ and $y$ are fixed points of the double iteration $z _ { n + 2 } = F ( F ( z _ { n } ) )$ : When $a$ increases past 3:45, this cycle becomes unstable.

At that point the period doubles from 2 to 4. With $a = 3 . 5$ you see a “4-cycle” in the table—it repeats after four steps. The sequence bounces from :875 to :383 to :827 to :501 and back to :875. This cycle must be attractive or we would not see it. But it also becomes unstable as $a$ increases. Next comes an 8-cycle, which is stable in a little window (you could compute it) around $a = 3 . 5 5$ : The cycles are stable for shorter and shorter intervals of $a$ ’s. Those stability windows are reduced by the Feigenbaum shrinking factor 4:6692. . . . Cycles of length 16 and 32 and 64 can be seen in physical experiments, but they are all unstable before $a = 3 . 5 7 .$ : What happens then ?

The new and unexpected behavior is between 3:57 and 4: Down each line of Figure 3.24, the computer has plotted the valuesof $z _ { 1 0 0 1 }$ to $z _ { 2 0 0 0 }$ —omitting the first thousand points to let a stable period (or chaos) become established. No points appeared in the big white wedge. I don’t know why. In the window for period 3, you see only three $z$ ’s. Period 3 is followed by 6; 12; 24; . . . . There is period doubling at the end of every window (including all the windows that are too small to see). You can reproduce this figure by iterating $z _ { n + 1 } = a z _ { n } - a z _ { n } ^ { 2 }$ from any $z _ { 0 }$ and plotting the results.

# CANTOR SETS AND FRACTALS

I can’t tell what happens at $a = 3 . 8$ : There may be a stable cycle of some long period. The $z$ ’s may come close to every point between 0 and 1: A third possibility is to approach a very thin limit set, which looks like the famous Cantor set:

To construct the Cantor set, divide $[ 0 , 1 ]$ into three pieces and remove the open interval $\scriptstyle \left( { \frac { 1 } { 3 } } , { \frac { 2 } { 3 } } \right)$ : Then remove $\textstyle \left( { \frac { 1 } { 9 } } , { \frac { \bar { 2 } } { 9 } } \right)$ and $\left( { \frac { 7 } { 9 } } , { \frac { 8 } { 9 } } \right)$ from what remains. At each step take out the middle thirds . Thepoints  thatare left form the Cantor set.

tAhlel tehnegtehnsdopfoitnhtes ${ \frac { 1 } { 3 } } , { \frac { 2 } { 3 } } , { \frac { 1 } { 9 } } , { \frac { 2 } { 9 } } , \dots$ varles ianddthteo seta.nSdothies $\frac { 4 } { 3 }$ (ntPorrobsletmha4s2“).meNaesvuerrethzelreos.”s What is especially striking is its self-similarity: Between 0 and $\frac 1 3$ you see the same Cantor set three times smaller. From 0 to $\textstyle { \frac { 1 } { 9 } }$ the Cantor set is there again, scaled down by 9: Every section, when blown up, copies the larger picture.

Fractals That self-similarity is typical of a fractal. There is an infinite sequence of scales. A mathematical snowflake starts with a triangle and adds a bump in the middle of each side. At every step the bumps lengthen the sides by $4 / 3$ : The final boundary is self-similar, like an infinitely long coastline.

The period $2 , 4 , \ldots$ is the number of $z$ ’s in a cycle.

a=4

The word “fractal” comes from fractional dimension. The snowflake boundary has dimension larger than 1 and smaller than 2: The Cantor set has dimension larger than 0 and smaller than 1: Covering an ordinary line segment with circles of radius $r$ would take $c / r$ circles. For fractals it takes $c / \dot { r } ^ { D }$ circles—and $D$ is the dimension.

Our iteration $z _ { n + 1 } = 4 z _ { n } - 4 z _ { n } ^ { 2 }$ has $a = 4$ , at the end of Figure 3.24. The sequence $z _ { 0 } , z _ { 1 } , \ldots . { \mathrm { g o e s } }$ everywhere and nowhere. Its behavior is chaotic, and statistical tests find no pattern. For all practical purposes the numbers are random.

Think what this means in an experiment (or the stock market). If simple rules produce chaos, there is absolutely no way to predict the results. No measurement can ever be sufficiently accurate. The newspapers report that Pluto’s orbit is chaotic— even though it obeys the law of gravity. The motion is totally unpredictable over long times. I don’t know what that does for astronomy (or astrology).

The most readable book on this subject is Gleick’s best-seller Chaos: Making a New Science. The most dazzling books are The Beauty of Fractals and The Science

# 3 Applications of the Derivative

of Fractal Images, in which Peitgen and Richter and Saupe show photographs that have been in art museums around the world. The most original books are Mandelbrot’s Fractals and Fractal Geometry. Our cover has a fractal from Figure 13.11.

We return to friendlier problems in which calculus is not helpless.

# NEWTON’S METHOD VS. SECANT METHOD: CALCULATOR PROGRAMS

The hard part of Newton’s method is to find $d f / d x$ : We need itfor th eslope of the tangent line. But calculus can approximate by $\Delta f / \Delta x$ —usingthe values of $f ( x )$ already computed at $x _ { n }$ and $x _ { n - 1 }$ :

The secant method follows the secant line instead of the tangent line:

$$
x _ { n + 1 } = x _ { n } - { \frac { f ( x _ { n } ) } { \left( \Delta f / \Delta x \right) _ { n } } } { \mathrm { ~ w h e r e ~ } } \left( { \frac { \Delta f } { \Delta x } } \right) _ { n } = { \frac { f ( x _ { n } ) - f ( x _ { n - 1 } ) } { x _ { n } - x _ { n - 1 } } } .
$$

The secant line connects the two latest points on the graph of $f ( x )$ : Its equation is $y - f ( x _ { n } ) = ( \Delta f / \Delta x ) ( x - x _ { n } )$ : Set $y = 0$ to find equation (13) for the new $x = x _ { n + 1 }$ , where the line crosses t1he axis.

Prediction: Three secant steps are about as good as two Newton steps. Both should give four times as many correct decimals: $( e r r o r ) \to ( e r r o r ) ^ { 4 }$ : Probably the secant method is also chaotic for $x ^ { 2 } + 1 = 0$ :

These Newton and secant programs are for the TI-81. Place the formula for $f ( x )$ in slot $\textsf { Y } _ { 1 }$ and the formula for $f ^ { \prime } ( x )$ in slot $\textsf { Y } _ { 2 }$ on the $\curlyvee =$ function edit screen. NAn:sDweirsthpe'prEoNmpTtEwRithFOthRe iMniOtiRalE $x _ { 0 } = \mathsf { X } \theta$ .gTmheS:prSogErCamAsNpTause to:dYisÑplTay each ap:prDoxismpati'o'n $x _ { n }$ ,2thTeOvaBluRe $f ( x _ { n } )$ ', and th:eDdiffserpe'n'ceX $x _ { n } - x _ { n - 1 }$ : Pr:esYs1ÑY to:coDnitinsupe'o'r pr'e'ss $0 \mathsf { N }$ and select item $2 : \mathsf { Q u i t }$ toXbreak. If $f ( x _ { n } ) = 0$ ,stphe'prEo-N gra:mDsidispl'a'yXN FXN XN-anXdNthMe1ro'o't $x _ { n }$ :

PrgmN:NEWTON :Disp''ENTER FOR MORE" PrgmS:SECANT :Y→T  
: Disp" $x \theta = 1 1$ :Disp"'ON 2 TO BREAK' : Disp'xΩ= :Y1→Y  
:Input X :Disp" - : Input X : Disp''ENTERFORMORE'  
： $x \to 5$ : Disp''XNFXN XN-XNM1'' ： $x  5$ : Disp''XN FXN XN-XNM1 '\`  
$\mathsf { \Omega } : \mathsf { Y } _ { 1 } \to \mathsf { Y }$ : Disp X :Y1→T : Disp X  
:Lbl1 : DispY : Disp'X1=" : DispY  
:X-Y/Y2→X : Disp D : Input X : Disp D  
:X-S→D : Pause :Y1→Y : Pause  
:x→S :If $\forall \neq \emptyset$ :Lbl1 :If $\forall \neq \emptyset$   
:Y1→Y :Goto 1 : X-S→D : Goto1: Disp ''ROOT AT' : X→S : Disp "'ROOT AT':Disp X :X-YD/(Y-T)→X : Disp X