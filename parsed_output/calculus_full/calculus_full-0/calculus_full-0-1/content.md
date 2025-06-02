Calculus is about functions. I use that word “functions” in the first sentence, because we can’t go forward without it. Like all other words, we learn this one in two different ways: We define the word and we use the word.

I believe that seeing examples of functions, and using the word to explain those examples, is a fast and powerful way to learn. I will start with three examples:

Linear function $\begin{array} { l } { y \left( x \right) = 2 x } \\ { y \left( x \right) = { { x } ^ { 2 } } } \\ { y \left( x \right) = { { 2 } ^ { x } } } \end{array}$   
Squaring function   
Exponential function

The first point is that those are not the same! Their formulas involve 2 and $x$ in very different ways. When I draw their graphs (this is a good way to understand functions) you see that all three are increasing when $x$ is positive. The slopes are positive.

When the input $x$ increases (moving to the right), the output $y$ also increases (the graph goes upward). The three functions increase at different rates.

# 0 Highlights of Calculus

Near the start at $x = 0$ , the first function increases the fastest. But the others soon catch up. All three graphs reach the same height $y = 4$ when $x = 2$ : Beyond that point the second graph $y = x ^ { 2 }$ pulls ahead. At $x = 3$ the squaring function reaches $y = 3 ^ { 2 } = 9$ , while the height of the third graph is only $y = 2 ^ { 3 } = 8$ :

Don’t be deceived, the exponential will win. It pulls even at $x = 4$ , because $4 ^ { 2 }$ and $2 ^ { 4 }$ are both 16. Then $y = 2 ^ { x }$ moves ahead of $y = x ^ { 2 }$ and it stays ahead. When you reach $x = 1 0$ , the third graph will have $y = 2 ^ { 1 0 } = 1 0 2 4$ compared to $y = 1 0 ^ { 2 } = 1 0 0$ :

The graphs themselves are a straight line and a parabola and an exponential. The straight line has constant growth rate. The parabola has increasing growth rate. The exponential curve has exponentially increasing growth rate. I emphasize these because calculus is all about growth rates.

The whole point of differential calculus is to discover the growth rate of a function, and to use that information. So there are actually two functions in play at the same time—the original function and its growth rate. Before I go further down this all-important road, let¥me give a working definition of a function $y ( x )$ :

# A function has inputs $\boldsymbol { x }$ and outp¥uts $y ( x )$ . To each $\boldsymbol { x }$ it as¥signs one $y$ .

The inputs $x$ come from the “domain” of the function. In our graphs the domain contained all numbers $x \geqslant 0$ . The outputs $y$ form the “range” of the function. The ranges for the first two functions $y = 2 x$ and $y = x ^ { 2 }$ contained all numbers $y \geqslant 0$ . But the range for $y = 2 ^ { x }$ is limited to $y \geqslant 1$ when the domain is $x \geqslant 0$ .

Since these examples are so important, let me also allow $x$ to be negative. The three graphs are shown below. Strictly speaking, these are new functions! Their domains have been extended to all real numbers $x$ . Notice that the three ranges are also different:

The range of $y = 2 x$ is all real numbers $y$ The range of $y = x ^ { 2 }$ is all nonnegative numbers $y \geqslant 0$ The range of $y = 2 ^ { x }$ is all positive numbers $y > 0$

One more note about the idea of a function, and then calculus can begin. We have seen the three most popular ways to describe a function:

1. Give a formula to find $y$ from $x$ . Example: $y ( x ) = 2 x$ :   
2. Give a graph that shows $x$ (distance across) and $y$ (distance up).   
3. Give the input-output pairs ( $x$ in the domain and $y$ in the range).

In a high-level definition, the “function” is the set of all the input-output pairs. We could also say: The function is the rule that assigns an output $y$ in the range to every input $x$ in the domain.

This shows something that we see for other words too. Logically, the definition should come first. Practically, we understand the definition better after we know examples that use the word. Probably that is the way we learn other words and also the way we will learn calculus. Examples show the general idea, and the definition is more precise. Together, we get it right.

The first words in this book were Calculus is about functions. Now I have to update that.

# PAIRS OF FUNCTIONS

Calculus is about pairs of functions. Call them Function (1) and Function (2). Our graphs of $y = 2 x$ and $y = x ^ { 2 }$ and $y = 2 ^ { x }$ were intended to be examples of Function (1). Then we discussed the growth rates of those three examples. The growth rate of Function (1) is Function (2). This is our first task—to find the growth rate of a function. Differential calculus starts with a formula for Function .1/ and aims to produce a formula for Function .2/:

Let me say right away how calculus operates. There are two ways to compute how quickly $y$ changes when $x$ changes:

Method 1 (Limits): Write ${ \frac { { \mathrm { C h a n g e ~ i n ~ } } y } { { \mathrm { C h a n g e ~ i n ~ } } x } } = { \frac { \Delta y } { \Delta x } } ,$ . Take the limit of this ratio as $\Delta x  0$ .   
Method 2 (Rules): Follow a rule to produce new growth rates from known rates.

For each new function $y ( x )$ , look to see if it can be produced from known functions—obeying one of the rules. An important part of learning calculus is to see different ways of producing new functions from old. Then we follow the rules for the growth rate.

Suppose the new function is not produced from known functions $2 ^ { x }$ is not produced from $2 x$ or $x ^ { 2 }$ ). Then we have to find its growth rate directly. By “directly” I mean that we compute a limit which is Function (2). This book will explain what a “limit” means and how to compute it.

Here we begin with examples—almost always the best way. I will state the growth rates ${ } ^ { \ast } d y / d x ^ { \prime \prime }$ for the three functions we are working with:

The linear function $y = 2 x$ has constant growth rate $d y / d x = 2$ . This section will take that first and easiest step. It is our opportunity to connect the growth rate to the slope of the graph. The ratio of up to across is $2 x / x$ which is 2.

Section 0:2 takes the next step. The squaring function $y = x ^ { 2 }$ has linear growth rate $d y / d x = 2 x$ . (This requires the idea of a limit—so fundamental to calculus.) Then we can introduce our first two rules:

Constant factor The growth rate of $C y ( x )$ is $C$ times the growth rate of $y ( x )$ .   
Sum of functions The growth rate of $y _ { 1 } + y _ { 2 }$ is the sum of the two growth rates.

# 0 Highlights of Calculus

The first rule says that $y = 5 x ^ { 2 }$ has growth rate $1 0 x$ . The factor $C = 5$ multiplies the growth rate $2 x$ . The second rule says that $y _ { 1 } + y _ { 2 } = 5 x ^ { 2 } + 2 x$ has growth rate $1 0 x + 2$ . Notice how we immediately took $5 x ^ { 2 }$ as a function $y _ { 1 }$ with a known growth rate. Together, the two rules give the growth rate for any “linear combination”of $y _ { 1 }$ and $y _ { 2 }$ :

# The growth rate of $C _ { 1 } y _ { 1 } + C _ { 2 } y _ { 2 }$ is that same combination $C _ { 1 } \frac { d y _ { 1 } } { d x } + C _ { 2 } \frac { d y _ { 2 } } { d x }$

In words, the step from Function (1) to Function (2) is linear. The slope of $y = x ^ { 2 } - x$ is $d y / d x = 2 x - 1$ . This rule is simple but so important.

Finally, Section 0:3 will present the exponential functions $y = 2 ^ { x }$ and $y = e ^ { x }$ . Our first job is their meaning—what is $^ { 6 6 } 2$ to the power $\pi ^ { \mathfrak { N } } ?$ We understand $2 ^ { 3 } = 8$ and $2 ^ { 4 } = 1 6$ , but how can we multiply 2 by itself $\pi$ times?

When we meet $e ^ { x }$ , we are seeing the great creation of calculus. This is a function with the remarkable property that $d y / d x = y$ . The slope equals the function. This requires the amazing number $e$ , which was never seen in algebra—because it only appears when you take the right limit.

So these first sections compute growth rates for three essential functions. We are ready for $y = 2 x$ .

# THE SLOPE OF A GRAPH

The slope is distance up divided by distance across. I am thinking now about the graph of a function $y ( x )$ . The “distance across” is the change $x _ { 2 } - x _ { 1 }$ in the inputs, from $x _ { 1 }$ to $x _ { 2 }$ . The “distance up” is the change $y _ { 2 } - y _ { 1 }$ in the outputs, from $y _ { 1 }$ to $y _ { 2 }$ . The slope is large and the graph is steep when $y _ { 2 } - y _ { 1 }$ is much larger than $x _ { 2 } - x _ { 1 }$ . Change in y divided by change in $x$ matches our ordinary meaning of the word slope:

$$
{ \mathrm { A v e r a g e ~ s l o p e ~ } } = { \frac { \mathrm { c h a n g e ~ i n ~ } y } { \mathrm { c h a n g e ~ i n ~ } x } } = { \frac { y _ { 2 } - y _ { 1 } } { x _ { 2 } - x _ { 1 } } } = { \frac { \Delta y } { \Delta x } } .
$$

I introduced the very useful Greek letter $\Delta$ (delta), as a symbol for change. We take a step of length $\Delta x$ to go from $x _ { 1 }$ to $x _ { 2 }$ . For the height $y ( x )$ on the graph, that produces a step $\Delta y = y _ { 2 } - y _ { 1 }$ . The ratio of $\Delta y$ to $\Delta x$ , up divided by across, is the average slope between $x _ { 1 }$ and $x _ { 2 }$ . The slope is the steepness.

Important point: I had to say “average” because the slope could be changing as we go. The graph of $y = x ^ { 2 }$ shows an increasing slope. Between $x _ { 1 } = 1$ and $x _ { 2 } = 2$ , what is the average slope for $y = x ^ { 2 }$ ? Divide $\Delta y$ by $\Delta x$ :

$$
\begin{array}{c} y _ { 1 } = 1 { \mathrm { ~ a t ~ } } x _ { 1 } = 1  \\ { y _ { 2 } = 4 { \mathrm { ~ a t ~ } } x _ { 2 } = 2 } \end{array} \qquad { \mathrm { A v e r a g e ~ s l o p e } } = { \frac { 4 - 1 } { 2 - 1 } } = { \frac { \Delta y } { \Delta x } } = 3 .
$$

Between $x _ { 1 } = 0$ and $x _ { 2 } = 2$ , we get a different answer (not 3). This graph of $x ^ { 2 }$ shows the problem of calculus, to deal with changes in slope and changes in speed.

The graph of $y = 2 x$ has constant slope. The ratio of $\Delta y$ to $\Delta x$ , distance up to distance across, is always 2:

# Constant slope

$$
{ \frac { \Delta y } { \Delta x } } = { \frac { y _ { 2 } - y _ { 1 } } { x _ { 2 } - x _ { 1 } } } = { \frac { 2 x _ { 2 } - 2 x _ { 1 } } { x _ { 2 } - x _ { 1 } } } = 2 .
$$

The mathematics is easy, which gives me a chance to emphasize the words and the ideas:

Function $( 1 ) =$ Height of the graph Function $( 2 ) =$ Slope of the graph

When Function (1) is $y = C x$ , the ratio $\Delta y / \Delta x$ is always $C$ . A linear function has a constant slope. And those same functions can come from driving a car at constant speed:

Function $( 1 ) =$ Distance traveled $\mathbf { \Psi } = C \mathbf { \Psi } \mathbf { t }$ Function $( 2 ) =$ Speed of the car $= C$

For a graph of Function (1), its rate of change is the slope. When Function (1) measures distance traveled, its rate of change is the speed (or velocity). When Function .1/ measures our height, its rate of change is our growth rate.

The first point is that functions are everywhere. For calculus, those functions come in pairs. Function .2/ is the rate of change of Function .1/:

The second point is that Function (1) and Function (2) are measured in different units. That is natural:

$$
\begin{array} { r l } & { \left( \mathrm { S p e e d ~ i n ~ } \displaystyle \frac { \mathrm { m i l e s } } { \mathrm { h o u r } } \right) \mathrm { ~ m u l t i p l i e s ~ } \left( \mathrm { T i m e ~ i n ~ h o u r s } \right) \mathrm { t o ~ g i v e ~ } \Big ( \mathrm { D i s t a n c e ~ i n ~ m i l e s } \Big ) } \\ & { \left( \mathrm { G r o w t h ~ r a t e ~ i n ~ } \displaystyle \frac { \mathrm { i n c h e s } } { \mathrm { y e a r } } \right) \mathrm { ~ m u l t i p l i e s ~ } \left( \mathrm { T i m e ~ i n ~ y e a r s } \right) \mathrm { t o ~ g i v e ~ } \Big ( \mathrm { H e i g h t ~ i n ~ i n c h e s } \Big ) } \end{array}
$$

When time is in seconds and distance is in meters, then speed is automatically in meters per second. We can choose two units, and they decide the third. Function (2) always involves a division: $\Delta y$ is divided by $\Delta x$ or distance is divided by time.

The delicate and tricky part of calculus is coming next. We want the slope at one point and the speed at one instant. What is the rate of change in zero time ?

The distance across is $\Delta x = 0$ at a point. The distance up is $\Delta y = 0$ . Formally, their ratio is $\frac { 0 } { 0 }$ . It is the inspiration of calculus to give this a useful meaning.

# 0 Highlights of Calculus

Big Picture

Calculus connects Function (1) with Function $( 2 ) =$ rate of change of (1) Function (1) Distance traveled $f ( t )$ Function (2) Speed $s ( t ) = d f / d t$ Function (1) Height of graph $y ( x )$ Function (2) Slope $s ( x ) = d y / d x$ Function (2) tells how quickly Function (1) is changing

$s = { \frac { \operatorname { D i s t a n c e } f } { \operatorname { T i m e } t } }$ Distance up KEY Constant speed Constant slope s D Distance across

Graphs of (1) and (2) $f =$ increasing distance $s =$ constant speed

Slope of $f \mathrm { - g r a p h } = { \frac { \mathrm { u p } } { \mathrm { a c r o s s } } } = { \frac { s t } { t } } = s$ Area under $s$ -graph $\ b =$ area of rectangle ${ } = s t = f$

Now run the car backwards. Speed is negative Distance goes down to 0 Area “under” $s ( t )$ is zero

When speed is changing, algebra is not enough $s = { \frac { f } { t } }$ is wrong Still true that area under $s = { \mathrm { t r i a n g l e ~ a r e a } } = { \frac { 1 } { 2 } } ( t ) ( 2 0 t ) = 1 0 t ^ { 2 } = f$ Still true that $s = { \mathrm { s l o p e } }$ of $f = { \frac { d f } { d t } } =$ “derivative” of $f$

When $f$ is increasing, the slope $s$ is positive   
When $f$ is decreasing, the slope $s$ is negative   
When $f$ is at its maximum or minimum, the slope $s$ is zero   
The graphs of any $f ( t )$ and $f ( t ) + 1 0$ have the same slope at every t   
To recover $f =$ Function (1) from dft ; good to know a starting height f .0/

# 0 Highlights of Calculus

# Practice Questions

1. Draw a graph of $f ( t )$ that goes up and down and up again.

Then draw a reasonable graph of its slope.

2. The world population $f ( t )$ increased slowly at first, now quickly, then slowly again (we hope and expect). Maybe a limit $\approx 1 2$ or 14 billion.

Draw a graph for $f ( t )$ and its slope $s ( t ) = \frac { d f } { d t }$

3. Suppose $f ( t ) = 2 t$ for $t \leq 1$ and then $f ( t ) = 3 t + 2$ for $t \geq 1$ Describe the slope graph $s ( t )$ : Compare its area out to $t = 3$ with $f ( 3 )$

4. Draw a graph of $f ( t ) = \cos t$ : Then sketch a graph of its slope. At what angles $t$ is the slope zero (slope $= 0$ when $f ( t )$ is “flat”).   
5. Suppose the graph of $f ( t )$ is shaped like the capital letter W. Describe the graph of its slope $s ( t ) = \frac { d f } { d t }$ : What is the total area under the graph of $s$ ? -   
6. A train goes a distance $f$ at constant speed $s$ : Inside the train, a passenger walks forward a distance $F$ at walking speed $S$ : What distance does the passenger go ? At what speed ? (Measure distance from the train station)