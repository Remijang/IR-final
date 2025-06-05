# 0.2 The Changing Slope of $y = x ^ { 2 }$ and $y = x ^ { n }$

The second of our three examples is $y = x ^ { 2 }$ : Now the slope is changing as we move up the curve. The average slope is still $\Delta y / \Delta x$ ; but that is not our final goal. We have to answer the crucial questions of differential calculus:

# What is the meaning of “slope at a point” and how can we compute it ?

My video lecture on Big Picture: Derivatives also faces those questions. Every student of calculus soon reaches this same problem. What is the meaning of “rate of change” when we are at a single moment in time, and nothing actually changes in that moment ? Good question.

The answers will come in two steps. Algebra produces $\Delta y / \Delta x$ ; and then calculus finds $d y / d x$ : Those steps $d y$ and $d x$ are infinitesimally short, so formally we are looking at $0 / 0$ : Trying to define $d y$ and $d x$ and $0 / 0$ is not wise, and I won’t do it. The successful plan is to realize that the ratio of $\Delta y$ to $\Delta x$ is clearly defined, and those two numbers can become very small. If that ratio $\Delta y / \Delta x$ approaches a limit, we have a perfect answer:

The distance across, from $x$ to $x + \Delta x$ ; is just $\Delta x$ : The distance up is from $y ( x )$ to $y ( x + \Delta x )$ : Let me show how algebra leads directly to $\Delta y / \Delta x$ when $y = x ^ { 2 }$ :

$$
{ \frac { \Delta y } { \Delta x } } = { \frac { ( x + \Delta x ) ^ { 2 } - x ^ { 2 } } { \Delta x } } = { \frac { x ^ { 2 } + 2 x \Delta x + ( \Delta x ) ^ { 2 } - x ^ { 2 } } { \Delta x } } = 2 x + \Delta x .
$$

Notice that calculation! The “leading terms” $x ^ { 2 }$ and $- x ^ { 2 }$ cancel. The important term here is $2 x \Delta x$ : This “first-order term” is responsible for most of $\Delta y$ : The “secondorder term” in this example is $( \Delta x ) ^ { 2 }$ : After we divide by $\Delta x$ ; this term is still small. That part $( \Delta x ) ^ { 2 } / \Delta x$ will disappear as the step size $\Delta x$ goes to zero.

That limiting process $\Delta x  0$ produces the slope $d y / d x$ at a point. The firstorder term survives in $d y / d x$ and higher-order terms disappear.

$$
\Bigg | \mathrm { S l o p e ~ a t ~ a ~ p o i n t } \frac { d y } { d x } = \mathrm { l i m i t } \mathrm { o f } \frac { \Delta y } { \Delta x } = \mathrm { l i m i t ~ o f } \ : 2 x + \Delta x = 2 x .
$$

Algebra produced $\Delta y / \Delta x$ : In the limit, calculus gave us $d y / d x$ : Look at the graph, to see the geometry of those steps. The ratio $\mathrm { u p } / \mathrm { a c r o s s } = \Delta y / \Delta x$ is the slope between two points on the graph. The two points come together in the limit. Then $\Delta y / \Delta x$ approaches the slope $d y / d x$ at a single point.

The color lines connecting points on the first two graphs are called “chords.” They approach the color line on the third graph, which touches at only one point. This is the “tangent line” to the curve. Here is the idea of differential calculus:

$$
\mathrm { S l o p e ~ o f ~ t a n g e n t ~ l i n e } = \mathrm { S l o p e ~ o f ~ c u r v e } = \mathrm { ~ F u n c t i o n ~ } ( 2 ) = \frac { d y } { d x } = 2 x .
$$

To find the equation for this tangent line, return to algebra. Choose any specific value $x _ { 0 }$ : Above that position on the $x$ axis, the graph isat height $y _ { 0 } = x _ { 0 } ^ { 2 }$ : The slope of the tangent line at that point of the graph is $d y / d x = 2 x _ { 0 }$ : We want the equation for the line through that point with that slope.

At the point where $x = x _ { 0 }$ and $y = y _ { 0 }$ ; this equation becomes $0 = 0$ : The equation is satisfied and the point is on the line. Furthermore the slope of the line matches the slope $2 { x } _ { 0 }$ of the curve. You see that directly if you divide both sides by $x - x _ { 0 }$ :

# Tangent line

$$
{ \frac { \mathrm { u p } } { \mathrm { a c r o s s } } } = { \frac { y - y _ { 0 } } { x - x _ { 0 } } } = 2 x _ { 0 } { \mathrm { i s ~ t h e ~ c o r r e c t ~ s l o p e } } { \frac { d y } { d x } } .
$$

Let me say this again. The curve $y = x ^ { 2 }$ is bending, the tangent line is straight. This line stays as close to the curve as possible, near the point where they touch. The tangent line gives a linear approximation to the nonlinear function $y = x ^ { 2 }$ :

I only moved $y _ { 0 }$ to the right side of equation (1). Then I used the symbol $\approx$ for “approximately equal” because the symbol $\mathbf { \Sigma } =$ would be wrong: The curve bends. Important for the future: This bending comes from the second derivative of $y = x ^ { 2 }$ :

# THE SECOND DERIVATIVE

The first derivative is the slope $d y / d x = 2 x$ : The second derivative is the slope of the slope. By good luck we found the slope of $2 x$ in the previous section (easy to do, it is just the constant 2). Notice the symbol $d ^ { 2 } y / d x ^ { 2 }$ for the slope of the slope:

In ordinary language, the first derivative $d y / d x$ tells how fast the function $y ( x )$ is changing. The second derivative tells whether we are speeding up or slowing down. The example $y = x ^ { 2 }$ is certainly speeding up, since the graph is getting steeper. The curve is bending and the tangent line is steepening.

Think also about $y = x ^ { 2 }$ on the left side (the negative side) of $x = 0$ : The graph is coming down to zero. Its slope is certainly negative. But the curve is still bending upwards! The algebra agrees with this picture: The slope $d y / d x = 2 x$ is negative on the left side of $x = 0$ ; but the second derivative $d ^ { 2 } y / d x ^ { 2 } = 2$ is still positive.

An economist or an investor watches all three of those numbers: $y ( x )$ tells where the economy is, and $d y / d x$ tells which way it is going (short term, close to the tangent line). But it is $d ^ { 2 } y / d x ^ { 2 }$ that reveals the longer term prediction. I am writing these words near the end of the economic downturn (I hope). I am sorry that $d y / d x$ has been negative but happy that $d ^ { 2 } y / d x ^ { 2 }$ has recently been positive.

# DISTANCE AND SPEED AND ACCELERATION

An excellent example of $y ( x )$ and $d y / d x$ and $d ^ { 2 } y / d x ^ { 2 }$ comes from driving a car. The function $y$ is the distance traveled. Its rate of change (first derivative) is the speed. The rate of change of the speed (second derivative) is the acceleration. If you are pressing on the gas pedal, all three will be positive. If you are pressing on the brake, the distance and speed are probably still positive but the acceleration is negative: The speed is dropping. If the car is in reverse and you are braking, what then ?

The speed is negative (going backwards) The speed is increasing (less negative) The acceleration is positive (increasing speed).

The video lecture mentions that car makers don’t know calculus. The distance meter on the dashboard does not go back toward zero (in reverse gear it should). The speedometer does not go below zero (it should). There is no meter at all (on my car) for acceleration. Spaceships do have accelerometers, and probably aircraft too.

We often hear that an astronaut or a test pilot is subjected to a high number of $g$ ’s. The ordinary acceleration in free fall is one $g$ ; from the gravity of the Earth. An airplane in a dive and a rocket at takeoff will have a high second derivative—the rocket may be hardly moving but it is accelerating like mad.

One more very useful point about this example of motion. The natural letter to use is not $x$ but t. The distance is a function of time. The slope of a graph is up=across, but now the right ratio is (change of distance) divided by (change in time):

Average speed between $t \ \mathbf { a n d } \ t + \Delta t \quad { \frac { \Delta y } { \Delta t } } = { \frac { y ( t + \Delta t ) - y ( t ) } { \Delta t } }$ Speed at t itself (instant speed) ${ \frac { d y } { d t } } = \operatorname* { l i m i t } \operatorname* { o f } { \frac { \Delta y } { \Delta t } } \ \mathrm { a s } \ \Delta t \to 0$

The words “rate of change” and “rate of growth” suggest $t$ . The word “slope” suggests $x$ : But calculus doesn’t worry much about the letters we use. If we graph the distance traveled as a function of time, then the $x$ axis (across) becomes the $t$ axis. And the slope of that graph becomes the speed (velocity is the best word).

Here is something not often seen in calculus books—the second difference. We know the first difference $\Delta y = y ( t + \Delta t ) - y ( t )$ . It is the change in $y$ : The second difference $\Delta ^ { 2 } y$ is the change in $\Delta y$ :

$$
\Delta ^ { 2 } y = \left( y ( t + \Delta t ) - y ( t ) \right) - \left( y ( t ) - y ( t - \Delta t ) \right) \quad { \frac { \Delta ^ { 2 } y } { ( \Delta t ) ^ { 2 } } } \to { \frac { d ^ { 2 } y } { d t ^ { 2 } } }
$$

$\Delta ^ { 2 } y$ simplifies to $y ( t + \Delta t ) - 2 y ( t ) + y ( t - \Delta t )$ : We divide by $( \Delta t ) ^ { 2 }$ to approximate the acceleration. In the limit as $\Delta t \to 0$ , this ratio $\Delta ^ { 2 } y / ( \Delta t ) ^ { 2 }$ becomes the second derivative $d ^ { 2 } y / d t ^ { 2 }$ .

The slope of $y = x ^ { 2 }$ is $d y / d x = 2 x$ : Now I want to compute the slopes of $y = x ^ { 3 }$ and $y = x ^ { 4 }$ and all succeeding powers $y = x ^ { n }$ : The rate of increase of $x ^ { n }$ will be found again in Section 2:2: But there are two reasons to discover these special derivatives early:

1.Their pattern is simple: The slope of each power $y = x ^ { n }$ is ${ \frac { d y } { d x } } = n x ^ { n - 1 }$   
2. The next section can then introduce $y = e ^ { x }$ : This amazing function has ${ \frac { d y } { d x } } = y$

Of course $y = x ^ { 2 }$ fits into this pattern for $x ^ { n }$ : The exponent drops by 1 from $n = 2$ to $n - 1 = 1$ . Also $n = 2$ multiplies that lower power to give $n x ^ { n - 1 } = 2 x$ :

The slope of $y = x ^ { 3 }$ is $d y / d x = 3 x ^ { 2 }$ . Watch how $3 x ^ { 2 }$ appears in $\Delta y / \Delta x$ :

$$
{ \frac { \Delta y } { \Delta x } } = { \frac { ( x + \Delta x ) ^ { 3 } - x ^ { 3 } } { \Delta x } } = { \frac { x ^ { 3 } + 3 x ^ { 2 } \Delta x + 3 x ( \Delta x ) ^ { 2 } + ( \Delta x ) ^ { 3 } - x ^ { 3 } } { \Delta x } } .
$$

Cancel $x ^ { 3 }$ with $- x ^ { 3 }$ : Then divide by $\Delta x$ :

# Average slope

$$
\frac { \Delta y } { \Delta x } = 3 x ^ { 2 } + 3 x \Delta x + ( \Delta x ) ^ { 2 } .
$$

When the step length $\Delta x$ goes to zero, the limit value $d y / d x$ is $3 x ^ { 2 }$ : This is $n x ^ { n - 1 }$

To establish this pattern for $n = 4 , 5 , 6 , \ldots$ the only hard part is $( x + \Delta x ) ^ { n }$ : When $n$ was 3; we multiplied this out in equation (5) above. The result will always start with $x ^ { n }$ : We claim that the next term (the “first-order term” in $\Delta y$ ) will be $n x ^ { n - 1 } \Delta x$ : When we divide this part of $\Delta y$ by $\Delta x$ ; we have the answer we want—the correct derivative $n x ^ { n - 1 }$ of $y ( x ) = x ^ { n }$ :

How to see that term $n x ^ { n - 1 } \Delta x ?$ Our multiplications showed that $2 x \Delta x$ and $3 x ^ { 2 } \Delta x$ are correct for $n = 2$ and 3. Then we can reach $n = 4$ from $n = 3$ :

$$
\begin{array} { c } { { ( x + \Delta x ) ^ { 4 } = ( x + \Delta x ) ^ { 3 } \mathrm { ~ t i m e s ~ } ( x + \Delta x ) } } \\ { { = ( x ^ { 3 } + 3 x ^ { 2 } \Delta x + \cdots ) \mathrm { ~ t i m e s ~ } ( x + \Delta x ) } } \end{array}
$$

That multiplication produces $x ^ { 4 }$ and $4 x ^ { 3 } \Delta x$ , exactly what we want. We can go from each $n$ to the next one in the same way (this is called “induction”). The derivatives of all the powers $x ^ { 4 } , x ^ { 5 } , . . . , x ^ { n }$ are $4 x ^ { 3 }$ $\mathfrak { c } ^ { 3 } , 5 x ^ { 4 } , . . . , n x ^ { n - 1 }$ .

Section 2:2 of the book shows you a slightly different proof of this formula. And the video lecture on the Product Rule explains one more way. Look at $x ^ { n + 1 }$ as the product of $x ^ { n }$ times $x$ , and use the rule for the slope of $y _ { 1 }$ times $y _ { 2 }$ :

With $y _ { 1 } = x ^ { n }$ and $y _ { 2 } = x$ , the slope of $y _ { 1 } y _ { 2 } = x ^ { n + 1 }$ comes out right:

$$
x ( \mathrm { s l o p e ~ o f ~ } x ^ { n } ) + x ^ { n } ( \mathrm { s l o p e ~ o f ~ } x ) = x ( n x ^ { n - 1 } ) + x ^ { n } ( 1 ) = ( n + 1 ) x ^ { n } .
$$

Again we can increase $n$ one step at a time. Soon comes the truly valuable fact that this derivative formula is correct for all powers $y = x ^ { n }$ . The exponent $n$ can be negative, or a fraction, or any number at all. The slope $d y / d x$ is always $n x ^ { n - 1 }$ .

By combining different powers of $x$ , you know the slope of every “polynomial.” An example is $y = x + x ^ { 2 } / 2 + x ^ { 3 } / 3$ . Compute $d y / d x$ one term at a time, as the Sum Rule allows:

$$
{ \frac { d } { d x } } \Bigl ( x + { \frac { x ^ { 2 } } { 2 } } + { \frac { x ^ { 3 } } { 3 } } \Bigr ) = 1 + x + x ^ { 2 } .
$$

The slope of the slope is $d ^ { 2 } y / d x ^ { 2 } = 1 + 2 x$ . The fourth derivative is zero!

Function (1) tells us the height $y$ above each point $x$ The problem is to find the “instant slope” at $x$ This slope $s ( x )$ is written $\frac { d y } { d x }$ It is Function (2) KEY: ${ \frac { \Delta y } { \Delta x } } = { \frac { y ( x + \Delta x ) - y ( x ) } { \Delta x } } = { \frac { \mathrm { u p } } { \mathrm { a c r o s s } } }$ approaches $\frac { d y } { d x }$ as $\Delta x  0$

Compute the instant slope $\frac { d y } { d x }$ for the function $y = x ^ { 3 }$   
First find the average slope between $x$ and $x + \Delta x$   
Average ${ \mathrm { s l o p e } } = { \frac { \Delta y } { \Delta x } } = { \frac { ( x + \Delta x ) ^ { 3 } - x ^ { 3 } } { \Delta x } }$   
Write $( x + \Delta x ) ^ { 3 } = x ^ { 3 } + 3 x ^ { 2 } \Delta x + 3 x ( \Delta x ) ^ { 2 } + ( \Delta x ) ^ { 3 }$   
Subtract $x ^ { 3 }$ and divide by $\Delta x$   
$\begin{array} { r l } & { \frac { \Delta y } { \Delta x } { = } \frac { 3 { \mathbf x } ^ { 2 } \Delta x + 3 x ( \Delta x ) ^ { 2 } + ( \Delta x ) ^ { 3 } } { \Delta x } { = } 3 { \mathbf x } ^ { 2 } + 3 x \Delta x + ( \Delta x ) ^ { 2 } } \\ & { \mathrm { W h e n } ~ \Delta x {  } 0 , \mathrm { t h i s ~ b e c o m e s } \ \frac { d y } { d x } { = } 3 { \mathbf x } ^ { 2 } \quad \displaystyle \frac { d } { d x } ( x ^ { n } ) = n x ^ { n - 1 } } \\ & { y { = } C x ^ { n } \mathrm { ~ h a s ~ s l o p e ~ } C n x ^ { n - 1 } \quad \mathrm { ~ T h e ~ s l o p e ~ o f ~ } y { = } 7 x ^ { 2 } \mathrm { ~ i s ~ } \frac { d y } { d x } { = } 1 4 x } \\ & { \mathrm { M u l t i p l y ~ } y \mathrm { ~ b y ~ } C {  } \mathrm { M u l t i p l y ~ } \Delta y \mathrm { ~ b y ~ } C  \mathrm { M u l t i p l y ~ } \frac { d y } { d x } \mathrm { ~ b y ~ } C } \end{array}$

# 0 Highlights of Calculus

Neat Fact: The slope of $y = \sin x$ is ${ \frac { d y } { d x } } = \cos x $ The graphs show this is reasonable Slope at the start is 1 (to find later)

Sine curve climbing $$ Cosine curve $> 0$ Top of sine curve (flat) $$ Cosine is zero at the first bullet Sine curve falling $$ Cosine curve $< 0$ between bullets Bottom of sine curve (flat) $$ Cosine back to zero at the second bullet

# Practice Questions

1. For $y = 2 x ^ { 3 }$ ; what is t he average ${ \mathrm { s l o p e } } = { \frac { \Delta y } { \Delta x } }$ from $x = 1$ to $x = 2$ ?   
2. What is the instant slope of $y = 2 x ^ { 3 }$ at $x = 1 \ : 2$ What is $\frac { d ^ { 2 } y } { d x ^ { 2 } }$   
3. $y = x ^ { n }$ has ${ \frac { d y } { d x } } = n x ^ { n - 1 }$ : What is $\frac { d y } { d x }$ when $y ( x ) = { \frac { 1 } { x } } = x ^ { - 1 } ?$   
4. For $y = x ^ { - 1 }$ , what is the average slope $\frac { \Delta y } { \Delta x }$ from x $x = \frac { 1 } { 2 }$ to $x = 1 ^ { \cdot }$ ?   
5. What is the instant slope of $y = x ^ { - 1 }$ at $x = \frac { 1 } { 2 } ?$

6. Suppose the graph of $y ( x )$ climbs up to its maximum at $x = 1$   
Then it goes downward for $x > 1$   
6A. What is the sign of $\frac { d y } { d x }$ for $x < 1$ and then for $x > 1$ ?   
6B. What is the instant slope at $x = 1$ ?   
7 If $y = \sin x$ , write an expression for $\frac { \Delta y } { \Delta x }$ at any point $x$ :   
We see later that this $\frac { \Delta y } { \Delta x }$ approaches cos $x$