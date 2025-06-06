# 3.3 Second Derivatives: Bending and Acceleration

When $f ^ { \prime } ( x )$ is positive, $f ( x )$ is increasing. When $d y / d x$ is negative, $y ( x )$ is decreasing. That is clear2, but what about the second derivative? From looking at the curve, can you decide the sign of $f ^ { \prime \prime } ( x )$ or $d ^ { 2 } y / d x ^ { 2 } ?$ The answer is yes and the key is in the bending.

A straight line doesn’t bend. The slope of $y = m x + b$ is $m$ (a constant). The second derivative is zero. We have to go to curves, to see a changing slope. Changes in the derivative show up in $f ^ { \prime \prime } ( x )$ :

The slope $2 x$ gets larger even when the parabola is fallin2g. The sign of $f$ or $f ^ { \prime }$ is not revealed by $f ^ { \prime \prime }$ : The second derivative tells about change in slope.

A function with $f ^ { \prime \prime } ( x ) > 0$ is concave up. It bends upward as the slope increases. It is also called convex. A function with decreasing slope—this means $f ^ { \prime \prime } ( x ) < 0$ —is concave down. Note how cos $x$ and $1 + \cos x$ and even $1 + { \frac { 1 } { 2 } } x + \cos { \cdot }$ change from concave down to concave up at $x = \pi / 2$ : At that point $f ^ { \prime \prime } { = } - \cos x$ changes from negative to positive. The extra $1 + { \frac { 1 } { 2 } } x$ tilts the graph but the bending is the same.

Here is another way to2see the sign of $f ^ { \prime \prime }$ : Watch the tangent lines.When the curve is concave up, the tangent stays below it. A linear approximation is too low. This section computes a quadratic approximation—which includes the term with $f ^ { \prime \prime } { > } 0$ : When the curve bends down $( f ^ { \prime \prime } < 0 )$ , the opposite happens—the tangent lin2es¡are above the curve. The linear approximation is too high, and $f ^ { \prime \prime }$ lowers it.

In physical motion, $f ^ { \prime \prime } ( t )$ is the acceleration—in units of distance= $( \mathrm { t i m e } ) ^ { 2 }$ : Acceleration is rate of change of velocity. The oscillation $\sin 2 t$ has $v = 2 \cos 2 t$ (maximum speed 2) and $a = - 4 \sin 2 t$ (maximum acceleration 4).

An increasing p1opulation means $f ^ { \prime } > 0$ : An increasing growth rate means $f ^ { \prime \prime } > 0$ . Those are different. The rate can slow down while the growth continues.

# MAXIMUM VS. MINIMUM

Remember that $f ^ { \prime } ( x ) = 0$ locates a stationary point. That may be a minimum or a maximum. The second derivative decides! Instead of computing $f ( x )$ at many points, we compute $f ^ { \prime \prime } ( x )$ at one point—the stationary point. It is a minimum if $f ^ { \prime \prime } ( x ) > 0$ :

To the left of a minimum, the curve is falling. After the minimum, the curve rises. The slope has changed from negative to positive. Th1e graph ben2ds upward and $f ^ { \prime \prime } ( x ) > 0$ :

At a maximum the slope drops from positive to negative. In the exceptional case, when $f ^ { \prime } ( x ) = 0$ and also $f ^ { \prime \prime } ( x ) = 0$ , anything can happen. An example is $x ^ { 3 }$ , which pauses at $x = 0$ and continues up (its slope is $3 x ^ { 2 } \geqslant 0$ ). However $x ^ { 4 }$ pauses and goes down (with a very flat graph).

We emphasize that the information from $f ^ { \prime } ( x )$ and $f ^ { \prime \prime } ( x )$ is only “local.” To be certain of an absolute minimum or maximum, we need information over2the whole domain.

$$
f ^ { \prime } ( x ) = 3 x ^ { 2 } - 2 x \quad { \mathrm { a n d } } \quad f ^ { \prime \prime } ( x ) = 6 x - 2 .
$$

To2find the maximum and=or minimum, solve $3 x ^ { 2 } - 2 x = 0$ : The stationary points are $x = 0$ and $\textstyle x = { \frac { 2 } { 3 } }$ . At those points we need the second derivative. It is $f ^ { \prime \prime } ( 0 ) = - 2$ (local maximum) and $f ^ { \prime \prime } \left( { \frac { 2 } { 3 } } \right) = + 2$ (local minimum).

Between the maximum  and minimum is the inflection point. That is where $f ^ { \prime \prime } ( x ) = 0$ . The curve changes from concave down to concave up. This example has $f ^ { \prime \prime } { = } 6 x - 2$ , so the inflection point is at $\begin{array} { r } { x = \frac { 1 } { 3 } } \end{array}$ :

# INFLECTION POINTS

In mathematics it is a special event when a function passes through zero. When the function is $f$ , its gr3aph crosses4the axis. When the function is $f ^ { \prime }$ , the tangent line is horizontal. When $f ^ { \prime \prime }$ goes through zero, we have an infl1ection point.

The direction of bending changes at a2n inflection point. Your eye picks that out in a graph. For an instant the graph is straight (straight lines have $f ^ { \prime \prime } { = } 0 \rangle$ ). It is easy to see crossing points and stationary points and inflection points. Very few people can recognize where $f ^ { \prime \prime \prime } = 0$ or $f ^ { \prime \prime \prime } = 0 .$ I am not sure if those points have names.

There is a genuine maximum or minimum when $f ^ { \prime } ( x )$ changes sig2n. Similarly, there is a genuine inflection point when $f ^ { \prime \prime } ( x )$ cha2nges sign. The graph is concave down on one side of an inflection point and concave 2up on the other side. $\dagger$ The tangents are above the curve on one side and below it on the other side. At an inflection point, the tangent line crosses the curve (Figure 3.7b).

Notice that a parabola $y = a x ^ { 2 } + b x + c$ has no inflection points: $y ^ { \prime \prime }$ is constant. A cubic curve has one inflection point, because $f ^ { \prime \prime }$ is linear. A fourth-degree curve might or might not have i?nflection points—?the quadratic? $f ^ { \prime \prime } ( x )$ mi?ght or might not cross the axis.

Between zeros of $f ( x )$ come zeros of $f ^ { \prime } ( x )$ (stationary points). Between zeros of $f ^ { \prime } ( x )$ come zeros of $f ^ { \prime \prime } ( x )$ (inflection points). In this example $f ( x )$ has a double zero at the origin, so a single zero of $f ^ { \prime }$ is caught there. It is a local maximum, since $f ^ { \prime \prime } ( 0 ) < 0$ :

Inflection points are important—not just for mathematics. We know the world population will keep rising. We don’t know if the rate of growth will slow down. Remember: The rate of growth stops growing at the inflection point. Here is the 1990 report of the UN Population Fund.

The next ten years will decide whether the world population trebles or merely doubles before it finally stops growing. This may decide the future of the earth as a habitation for humans. The population, now 5:3 billion, is increasing by a quarter of a million every day. Between 90 and 100 million people will be added every year during the 1990s; a billion people—a whole China—over the decade. The fastest growth will come in the poorest countries.

A few years ago it seemed as if the rate of population growth was slowing everywhere except in Africa and parts of South Asia. The world’s population seemed set to stabilize around 10:2 billion towards the end of the next century.

Today, the situation looks less promising. The world has overshot the marker points of the 1984 “most likely” medium projection. It is now on course for an eventual total that will be closer to 11 billion than to 10 billion.

If fertility reductions continue to be slower than projected, the mark could be missed again. In that case the world could be headed towards a total of up to 14 billion people.

Starting with a census, the UN follows each age group in each country. They estimate the death rate and fertility rate2—the medium estimates are published. This report is saying that we are not on track with the estimate.

Section 6.5 will come bac2k to population, with an equation that predicts 10 billion. It assumes 2we are now at the inflection point. But China’s second census just started on July 1, 1990: When it’s finished we will know if the inflection point is still ahead.

You now understand the meaning of $f ^ { \prime \prime } ( x )$ :Its sign gives the direction of bending— the change in the slope. The rest of this section computes how much the curve bends—using the size of $f ^ { \prime \prime }$ and not just its sign. We find quadratic approximations based on $f ^ { \prime \prime } ( x )$ : In some courses they are optional—the main points are highlighted.

# CENTERED DIFFERENCES AND SECOND DIFFERENCES

Calculus begins with average velocities, computed on either side of $x$ :

$$
{ \frac { f ( x + \Delta x ) - f ( x ) } { \Delta x } } \quad { \mathrm { a n d } } \quad { \frac { f ( x ) - f ( x - \Delta x ) } { \Delta x } } \quad { \mathrm { a r e ~ c l o s e ~ t o ~ } } f ^ { \prime } ( x )
$$

We never mentioned it, but a better approximation to $f ^ { \prime } ( x )$ comes from averaging those two averages. This produces a centered difference, which is based on $x + \Delta x$ and $x - \Delta x$ : It divides by $2 \Delta x$ :

$$
f ^ { \prime } ( x ) \approx { \frac { 1 } { 2 } } \left[ { \frac { f ( x + \Delta x ) - f ( x ) } { \Delta x } } + { \frac { f ( x ) - f ( x - \Delta x ) } { \Delta x } } \right] = { \frac { f ( x + \Delta x ) - f ( x - \Delta x ) } { 2 \Delta x } } .
$$

We claim this is better. The test is to try it on powers of $x$

For $f ( x ) = x$ these ratios all give $f ^ { \prime } = 1$ (exactly). For $f ( x ) = x ^ { 2 }$ , only the centered difference correctly gives $f ^ { \prime } = 2 x$ : The one-sided ratio gave $2 x + \Delta x$ (in Chapter 1 it was $2 t + h )$ . It is only “first-order accurate.” But centering leaves no error. We are averaging $2 x + \Delta x$ with $2 x - \Delta x$ : Thus the centered difference is “second-order accurate.”

I ask now: What ratio converges to the second derivative? One answer is to take differences of the first derivative. Certainly $\Delta f ^ { \prime } / \Delta x$ approaches $f ^ { \prime \prime }$ : But we want a ratio involving $f$ itself. A natural idea is to take differences of differÑences, which brings us to “second differences”:

$$
{ \frac { { f ( x + \Delta x ) - f ( x ) } } { \Delta x } } - { \frac { f ( x ) - f ( x - \Delta x ) } { \Delta x } } = { \frac { f ( x + \Delta x ) - 2 f ( x ) + f ( x - \Delta x ) } { ( \Delta x ) ^ { 2 } } } \to { \frac { d ^ { 2 } f } { d { x ^ { 2 } } } } .
$$

On the top, the difference of the d2ifference is $\Delta ( \Delta f ) = \Delta ^ { 2 } f .$ It corresponds to $d ^ { 2 } f .$ On the bottom, $( \Delta x ) ^ { 2 }$ corresponds to $d x ^ { 2 }$ . This explains the way we place the 2’s in $d ^ { 2 } f / d x ^ { 2 }$ : To say it differently: $d x$ is squared, $d f$ is not squared—as in distance= $( \mathrm { t i m e } ) ^ { 2 }$

Note that $( \Delta x ) ^ { 2 }$ becomes much smaller than $\Delta x$ : If we divide $\Delta f$ by $( \Delta x ) ^ { 2 }$ , the ratio blows up. It is the extra cancellation in the second difference $\Delta ^ { 2 } f$ that allows the limit to exist. That limit is $f ^ { \prime \prime } ( x )$ :

Application The great majority of equations can’t be solved exactly. A typical case is $f ^ { \prime \prime } ( x ) = - \sin f ( x )$ (the pendulum equation). To compute a solution, I would replace $f ^ { \prime \prime } ( x )$ by the second difference in equation (3). Approximations at points spaced by $\Delta x$ are a very large part of scientific computing.

To test the accuracy of these differences, here is an experiment on $f ( x ) =$ sin $x + \cos x$ : The table shows the errors at $x = 0$ from formulas .1/, .2/, .3/:

The one-sided errors are cut in half when $\Delta x$ is cut in half. The other columns decrease like $( \Delta x ) ^ { 2 }$ : Each reduction divides those errors by 4. The errors from one-sided differences are $O ( \Delta x )$ and the errors from centered differences are $O ( \Delta x ) ^ { 2 }$ .

The “big $\mathit { O } ^ { \prime \prime }$ notation When the errors are of order $\Delta x$ , we write $E = O ( \Delta x )$ : This means that $E \leqslant C \Delta x$ for some constant $C$ : We don’t compute $C$ —in fact we don’t want to deal with it. The statement “one-sided errors are Oh of delta $x ^ { \prime \prime }$ captures what is im1 portant. The main point of the other columns is $E = O ( \Delta x ) ^ { 2 }$ .

# LINEAR APPROXIMATION VS. QUADRATIC APPROXIMATION

The second derivative gives a tremendous improvement over linear approximation $f ( a ) + f ^ { \prime } ( a ) ( x - a )$ : A tangent line starts out close to the curve, but the line has no way to bend. After a while it overshoots or undershoots the true function (see Figure 3.8). That is especially clear for the model $f ( x ) = x ^ { 2 }$ , when the tangent is the $x$ axis and the parabola curves upward.

You can almost guess the term with bending. It should involve $f ^ { \prime \prime }$ , and also $( \Delta x ) ^ { 2 }$ : It might be exactly $f ^ { \prime \prime } ( x )$ times $( \Delta x ) ^ { 2 }$ but it is not. The model function $x ^ { 2 }$ has $f ^ { \prime \prime } { = } 2$ : There must bea factor $\frac { 1 } { 2 }$ to cancelthat 2:

3E The quadratic approximation to a smooth function $f ( x )$ near $x = a$ is $\begin{array} { r } { f ( x ) \approx f ( a ) + f ^ { \prime } ( a ) ( x - a ) + \frac { 1 } { 2 } f ^ { \prime \prime } ( a ) ( x - a ) ^ { 2 } . } \end{array}$

At th4e basepoint this is $f ( a ) = f ( a )$ : The derivatives also agree at $x = a$ : Furthermore the second derivatives agree. On both sides of .4/, the second derivative at $x = a$ is $f ^ { \prime \prime } ( a )$ :

The quadratic approximation bends with the function. It is not the absolutely final word, because there is a cubic term ${ \scriptstyle { \frac { 1 } { 6 } } } f ^ { \prime \prime \prime } ( a ) ( x - a ) ^ { 3 }$ and a fourth-degree term $\textstyle { \frac { 1 } { 2 4 } } f ^ { \prime \prime \prime } ( a ) ( x - a ) ^ { 4 }$ and so on. The whole infinite sum is a “Taylor series.” Equation (4) carries that series through the quadratic term—which for practical purposes gives a terrific approximation. You will see that in numerical experiments.

Two things to mention. First, equation (4) shows 1why $f ^ { \prime \prime } > 0$ brings the curve above the tangent line. The linear part gives the line, while the quadratic part is positive and bends upward. Second, equation (4)comes from2 .2/ and .3/: Where one-sided differences give $f ( x + \Delta x ) \approx f ( x ) + f ^ { \prime } ( x ) \Delta x$ , centered 2differences give the quadratic:

$$
\begin{array} { r l } { \mathrm { f r o m } ( 2 ) : } & { f ( x + \Delta x ) \approx f ( x - \Delta x ) + 2 f ^ { \prime } ( x ) \Delta x } \\ { \mathrm { f r o m } ( 3 ) : } & { f ( x + \Delta x ) \approx 2 f ( x ) - f ( x - \Delta x ) + f ^ { \prime \prime } ( x ) ( \Delta x ) ^ { 2 } . } \end{array}
$$

Add and divide by 2: The result is $\begin{array} { r } { f ( x + \Delta x ) \approx f ( x ) + f ^ { \prime } ( x ) \Delta x + \frac { 1 } { 2 } f ^ { \prime \prime } ( x ) ( \Delta x ) ^ { 2 } . } \end{array}$ This is correct through $( \Delta x ) ^ { 2 }$ and misses by $( \Delta x ) ^ { 3 }$ , as examples show:

$$
\begin{array} { l } { { ( x + \Delta x ) ^ { 3 } \approx ( x ^ { 3 } ) + ( 3 x ^ { 2 } ) ( \Delta x ) + \frac { 1 } { 2 } ( 6 x ) ( \Delta x ) ^ { 2 } + \mathrm { e r r o r } ( \Delta x ) ^ { 3 } . } } \\ { { \nonumber } } \\ { { ( 1 + x ) ^ { n } \approx 1 + n x + \frac { 1 } { 2 } n ( n - 1 ) x ^ { 2 } . } } \end{array}
$$

EXAMPLE 4

The first derivative at $x = 0$ is $n$ : The second derivative is $n ( n - 1 )$ : The cubic term would be ${ \scriptstyle { \frac { 1 } { 6 } } } n ( n - l ) ( n - 2 ) x ^ { 3 }$ : We are just producing the binomial expansion!

EXAMPLE 5 ${ \frac { 1 } { 1 - x } } \approx 1 + x + x ^ { 2 } = { \mathrm { s t a r t ~ o f ~ a ~ g e o m e t r i c ~ s e r i e s } } .$

$1 / ( 1 - x )$ has derivative $1 / ( 1 - x ) ^ { 2 }$ : Itssecond derivative is $2 / ( 1 - x ) ^ { 3 }$ : At $x = 0$ those equal 1; 1; 2: The factor $\frac { 1 } { 2 }$ cancels the 2, which leaves 1; 1; 1: This explains $1 + x + x ^ { 2 }$ :

The next terms are $x ^ { 3 }$ and $x ^ { 4 }$ : The whole series is $1 / ( 1 - x ) = 1 + x + x ^ { 2 } + x ^ { 3 } + \cdots$

Numerical experiment $1 / { \sqrt { 1 + x } } \approx 1 - { \frac { 1 } { 2 } } x + { \frac { 3 } { 8 } } x ^ { 2 }$ is tested for accuracy. Dividing $x$ by 2 almost divides the error by 8: If we only keep the linear part $1 - { \frac { 1 } { 2 } } x$ the error is only divided by 4: Hereare the errors at $\begin{array} { r } { x = \frac { 1 } { 4 } , \frac { 1 } { 8 } } \end{array}$ and $\scriptstyle { \frac { 1 } { 1 6 } }$ :

$$
{ \begin{array} { r l } { { \mathrm { l i n e a r ~ a p p r o x i m a t i o n } } \left( \operatorname { e r r o r } \approx { \frac { 3 } { 8 } } x ^ { 2 } \right) : } & { . 0 1 9 4 \quad . 0 0 5 3 \quad . 0 0 1 4 } \\ { { \mathrm { q u a d r a t i c ~ a p p r o x i m a t i o n } } \left( \operatorname { e r r o r } \approx { \frac { - 5 } { 1 6 } } x ^ { 3 } \right) : - . 0 0 4 0 1 } & { - . 0 0 0 5 5 \quad - . 0 0 0 0 7 } \end{array} }
$$