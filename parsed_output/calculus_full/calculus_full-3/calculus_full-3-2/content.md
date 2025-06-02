# 3.2 Maximum and Minimum Problems

Our goal is to learn about $f ( x )$ from $d f / d x$ : We begin with two quick questions. If $d f / d x$ is positive, what does that say about $f ?$ If the slope is negative, how is that reflected in the function? Then the third question is the critical one:

How do you identify a maximum or minimum? Normal answer: The slope is zero.

This may be the most important application of calculus, to reach $d f / d x = 0$ :

Take the easy q¡uestions first. Suppose $d f / d x$ is positive for every $x$ between $a$ and $b$ : All tangent lines slope upward. The function $f ( x )$ is increasing as $x$ goes from a to $b$ .

3B If $d f / d x > 0$ then $f ( x )$ is increasing. ¡If $d f / d x < 0$ then f .x/ is decreasing.

To define increasing a nd decreasing, look at any two points $x < X$ : “Increasing” requires $f ( x ) < f ( X )$ : “Decreasing” requires $f ( x ) > f ( X ) . A$ positive slope does not mean a positive function. The function itself can be positive or negative.

EXAMPLE 1 $f ( x ) = x ^ { 2 } - 2 x$ has slope $2 x - 2$ : This slope is positive when $x > 1$ and negative when $x < 1$ : The function increases after $x = 1$ and decreases before $x = 1$ :

Wesay that without computing $f ( x )$ at any point! The parabola in Figure 3.3 goes down to its minimum at $x = 1$ and up again.

EXAMPLE 2 $x ^ { 2 } - 2 x + 5$ has the same slope. Its graph is shifted up by 5, a number that disappears in $d f / d x$ : All functions with slope $2 x - 2$ are parabolas $x ^ { 2 } - 2 x + C$ , shifted up or down according to $C$ : Some parabolas cross the $x$ axis (those crossings are solutions to $f ( x ) = 0 )$ : Other parabolas stay above the axis. The solutions to $x ^ { 2 } - 2 x + 5 = 0$ are complex numbers and we don’t see them. The special parabola $x ^ { 2 } - 2 x + 1 = ( x - 1 ) ^ { 2 }$ grazes the axis at $x = 1$ : It has a “double zero,” where $f ( x ) = d f / d x = 0$ :

EXAMPLE 3 Suppose $d f / d x = ( x - 1 ) ( x - 2 ) ( x - 3 ) ( x - 4 )$ : This slope is positive beyond $x = 4$ and up to $x = 1 \ ( d f / d x = 2 4 \$ at $x = 0$ ). And $d f / d x$ is positive again between 2 and 3: At $x = 1 , 2 , 3 , 4$ , this slope is zero and $f ( x )$ changes direction.

Here $f ( x )$ is a fifth-degree polynomial, because $f ^ { \prime } ( x )$ is fourth-degree. The graph of $f$ goes up-down-up-down-up. It might cross the $x$ axis five times. $I t$ must cross at least once (like this one). When complex numbers are allowed, every fifth-degree polynomial has five roots.

You may feel that “positive slope implies increasing function” is obvious—perhaps it is. But there is still something delicate. Starting from $d f / d x > 0$ at every single point, we have to deduce $f ( X ) > f ( x )$ at pairs of points. That is a “local to global” question, to be handled by the Mean Value Theorem. It could also wait for the Fundamental Theorem of Calculus: The difference $f ( X ) - f ( x )$ equals the area under the graph of $d f / d x$ . That area is positive, so $f ( X )$ exceeds $f ( x )$ :

# MAXIMA AND MINIMA

Which $x$ makes $f ( x )$ as large as possible? Where is the smallest $f ( x ) \ ?$ Without calculus we are reduced to computing values of $f ( x )$ and comparing. With calculus, the information is in $d f / d x$ :

Suppose the maximum or minimum is at a particular point $x$ : It is possible that the graph has a corner—and no derivative. But if $d f / d x$ exists, it must be zero. The tangent line is level. The parabolas in Figure 3.3 change from decreasing to increasing. The slope changes from negative to positive. At this crucial point the slope is zero.

3C Local Maximum or Minimum Suppose the maximum or minimum occurs at a point $x$ inside an interval where $f ( x )$ and $d f / d x$ are defined. Then $f ^ { \prime } ( x ) = 0$ :

The word¡“local” allows the possibility that in ot¤her intervals, $f ( x )$ goes hig¤her or lower. We only look near $x$ , and we use the definition of $d f / d x$ :

Start with $f ( x + \Delta x ) - f ( x )$ : If $f ( x )$ is the maximum, this difference is negative or zero. T he step $\Delta x$ can be forward or backward¥:

$$
\mathrm { i f ~ } \Delta x > 0 : \quad \frac { f ( x + \Delta x ) - f ( x ) } { \Delta x } = \frac { \mathrm { n e g a t i v e } } { \mathrm { p o s i t i v e } } \leqslant 0 \quad \mathrm { a n d ~ i n ~ t h e ~ l i m i t } \quad \frac { d f } { d x } \leqslant 0 .
$$

$$
{ \mathrm { i f ~ } } \Delta x < 0 ; \quad { \frac { f ( x + \Delta x ) - f ( x ) } { \Delta x } } = { \frac { \mathrm { n e g a t i v e } } { \mathrm { n e g a t i v e } } } \geqslant 0 \quad { \mathrm { a n d ~ i n ~ t h e ~ l i m i t } } \quad { \frac { d f } { d x } } \geqslant 0 .
$$

Both arguments apply. Both conclusions $d f / d x \leqslant 0$ and $d f / d x \geqslant 0$ are correct. Thus $d f / d x = 0$ :

Maybe Richard Feynman said it best. He showed his friends a plastic curve that was made in a special way—“no matter how you turn it, the tangent at the lowest point is horizontal.” They checked it out. It was true.

Surely You’re Joking, Mr. Feynman! is a good book (but rough on mathematicians).

EXAMPLE 3 (continued) Look back at Figure 3.3b. The points that stand out are not the “ups” or “downs” but the “turns.” Those are stationary points, where $d f / d x = 0$ : We see two maxima and two minima. None of them are absolute maxima or minima, because $f ( x )$ starts at $- \infty$ and ends at $+ \infty$ :

# 3.2 Maximum and Minimum Problems

EXAMPLE 4 $f ( x ) = 4 x ^ { 3 } - 3 x ^ { 4 }$ has slope $1 2 x ^ { 2 } - 1 2 x ^ { 3 }$ : That derivative is zero when $x ^ { 2 }$ equals $x ^ { 3 }$ , at the two points $x = 0$ and $x = 1$ : To decide between minimum and maximum (local or absolute), the first step is to evaluate $f ( x )$ at these stationary points. We find $f ( 0 ) = 0$ and $f ( 1 ) = 1$ :

Now look at large $x$ : The function goes down to $- \infty$ in both directions. (You can mentally substitute $x = 1 0 0 0$ and $x = - 1 0 0 0 )$ . For large $x , - 3 x ^ { 4 }$ dominates $4 x ^ { 3 }$ :

Conclusion $f = 1$ is an absolute maximum. $f = 0$ is not a maximum or minimum (local or absolute). We have to recognize this exceptional possibility, that a curve (or a car) can pause for an instant . $( f ^ { \prime } = 0 )$ / and continue in the same direction. The reason is the “double zero” in $1 2 x ^ { 2 } - 1 2 x ^ { 3 }$ , from its double factor $x ^ { 2 }$ :

EXAMPLE 5 Define $f ( x ) = x + x ^ { - 1 }$ for $x > 0$ : Its derivative $1 - 1 / x ^ { 2 }$ is zero at $x = 1$ : At that point $f ( 1 ) = 2$ is the minimum value. Every combination like ${ \begin{array} { l } { { \frac { 1 } { 3 } } + 3 } \end{array} }$ or ${ \frac { 2 } { 3 } } + { \frac { 3 } { 2 } }$ is larger than $f _ { \mathrm { m i n } } = 2$ : Figure 3.4 shows that the maximum of $x + x ^ { - 1 }$ is $+ \infty . \dag$

Important The maximum always occurs at a stationary point (where $d f / d x = 0 )$ 1 or a rough point (no derivative) or an endpoint of the domain. These are the three types of critical points. All maxima and minima occur at critical points! At every other point $d f / d x > 0$ or $d f / d x < 0$ : Here is the procedure:

1. Solve $d f / d x = 0$ to find the stationary points $f ( x )$ :   
2. Compute $f ( x )$ at every critical point—stationary point, rough point, endpoint.   
3. Take the maximum and minimum of those critical values of $f ( x )$ : EXAMPLE 6 (Absolute value $f ( x ) = \left| x \right| )$ The minimum is zero at a rough point.   
The maximum is at an endpoint. There are no stationary points.



The derivative of $y = \left| x \right|$ is never zero. Figure 3.4 shows the maximum and minimum on the interval $[ - 3 , 2 ]$ : This is typical of piecewise linear functions.

Question Could the minimum be zero when the function never reaches $f ( x ) = 0 ?$ Answer Yes, $f ( x ) = 1 / ( 1 + x ) ^ { 2 }$ approaches but never reaches zero as $x \to \infty$ :

Remark 1 $x \to \pm \infty$ and $f ( x )  \pm \infty$ are avoided when $f$ is continuous on a closed interval $a \leqslant x \leqslant b$ : Then $f ( x )$ reaches its maximum and its minimum (Extreme Value Theorem). But $x \to \infty$ and $f ( x )  \infty$ are too important to rule out. You test $x \to \infty$ by considering large $x$ : You recognize $f ( x )  \infty$ by going above every finite value.

Remark 2 Note the difference between critical points (specified by $x$ ) and critical values (specified by $f ( x ) )$ . The example $x + x ^ { - 1 }$ had the minimum point $x = 1$ and the minimum value $f ( 1 ) = 2$ :

# MAXIMUM AND MINIMUM IN APPLICATIONS

To find a maximum or minimum, solve $f ^ { \prime } ( x ) = 0$ : The slope is zero at the top and bottom of the graph. The idea is clear—and then check rough points and endpoints. But to be honest, that is not where the problem starts.

In a real application, the first step (often the hardest) is to choose the unknown and find the function. It is we ourselves who decide on $x$ and $f ( x )$ : The equation $d f / d x = 0$ comes in the middle of the problem, not at the beginning. I will start on a new example, with a question instead of a function.

EXAMPLE 7 Where should you get onto an expressway for minimum driving time, if the expressway speed is $6 0 \mathrm { m p h }$ and ordinary driving speed is $3 0 \mathrm { m p h } ^ { \cdot }$ ?

I know this problem well—it comes up every morning. The Mass Pike goes to MIT and I have to join it somewhere. There is an entrance near Route 128 and another entrance further in. I used to take the second one, now I take the first. Mathematics should decide which is faster—some mornings I think they are maxima.

Most models are simplified, to focus on the key idea. We will allow the expressway to be entered at any point $x$ (Figure 3.5). Instead of two entrances (a discrete problem) we have a continuous choice (a calculus problem). The trip has two parts, at speeds 30 and 60:

a distance $\sqrt { a ^ { 2 } + x ^ { 2 } }$ up to the expressway, in $\sqrt { a ^ { 2 } + x ^ { 2 } } / 3 0$ hours a distance $b - x$ on the expressway, in $( b - x ) / 6 0$ hours

Problem Minimize $f ( x ) = \mathrm { t o t a l ~ t i m e } = { \frac { 1 } { 3 0 } } \sqrt { a ^ { 2 } + x ^ { 2 } } + { \frac { 1 } { 6 0 } } ( b - x ) .$

We have the function $f ( x )$ : Now comes calculus. The first term uses the power rule: The deriva1tive of $u ^ { 1 / \bar { 2 } }$ is $\textstyle { \frac { 1 } { 2 } } u ^ { - 1 / 2 } d u / d x$ : Here $u = a ^ { 2 } + x ^ { 2 }$ has $d u / d x = 2 x$ :

$$
f ^ { \prime } ( x ) = \frac { 1 } { 3 0 } \frac { 1 } { 2 } ( a ^ { 2 } + x ^ { 2 } ) ^ { - 1 / 2 } ( 2 x ) - \frac { 1 } { 6 0 } .
$$

To solve $f ^ { \prime } ( x ) = 0$ , multiply by 60 and square both sides:

$$
( a ^ { 2 } + x ^ { 2 } ) ^ { - 1 / 2 } ( 2 x ) = 1 \quad \mathrm { g i v e s } \quad 2 x = ( a ^ { 2 } + x ^ { 2 } ) ^ { 1 / 2 } \quad \mathrm { a n d } \quad 4 x ^ { 2 } = a ^ { 2 } + x ^ { 2 } .
$$

Thus $3 x ^ { 2 } = a ^ { 2 }$ : This yields two candidates, $x = a / \sqrt { 3 }$ and $x = - a / \sqrt { 3 }$ : But a negative $x$ would mean useless driving on the expressway. In fact $f ^ { \prime }$ is not zero at $x = - a / \sqrt { 3 }$ : That false root entered when we squared $2 x$ :

I notice something surprising. The stationary point $x = a / \sqrt { 3 }$ does not depend on $b$ : The total time includes the constant $b / 6 0$ , which disappeared in $d f / d x$ : Somehow $b$ must enter the answer, and this is a warning to go carefully. The minimum might occur at a rough point or an endpoint. Those are the other critical points of $f$ , and our drawing may notabe realistic. Certainly we expect $x \leqslant b$ , or we are entering the expressway beyond MIT.

Continue with calculus. Compute the driving time $f ( x )$ for an entrance at $x ^ { * } = a / \sqrt { 3 }$ :

$$
f ( x ) = { \frac { 1 } { 3 0 } } { \sqrt { a ^ { 2 } + ( a ^ { 2 } / 3 ) } } + { \frac { 1 } { 6 0 } } \left( b - { \frac { a } { \sqrt 3 } } \right) = { \frac { \sqrt 3 a } { 6 0 } } + { \frac { b } { 6 0 } } = f ^ { * } .
$$

The square root of $4 a ^ { 2 } / 3$ is $2 a / \sqrt { 3 }$ : We combined $2 / 3 0 - 1 / 6 0 = 3 / 6 0$ and divided by $\sqrt { 3 }$ : Is this station ary value $f ^ { * }$ a minimum? You must look also at endpoints:

The comparison $f ^ { * } < f ^ { * * }$ should be automatic. Entering at $x = 0$ was a candidate and calculus didn’t choose it. The derivative is not zero at $x = 0$ : It is not smart to go perpendicular to the expressway.

The second comparison has $x = b$ : We drive directly to MIT at speed 30: T|his option has to be taken seriously. In fact it is optimal when $b$ is small or $a$ is large.

This choice $x = b$ can arise mathematically in two ways. If all entrances are between 0 and $b$ , then $b$ is an endpoint. If we can enter beyond MIT, then $b$ is a rough poin?t. The graph in Figure 3.5c has a corner at $x = b$ , where the derivative jumps. The reas¤on is that distance on the expressway is the absolute value $| b - x | -$ never negative.

Either way $x = b$ is a critical point. The optimal $x$ is the smaller of $a / \sqrt { 3 }$ and $b$ .

if $a / { \sqrt { 3 } } \leqslant b$ W stationary point wins, enter at $x = a / \sqrt { 3 }$ ; total time $f ^ { * }$ if $a / \sqrt { 3 } \geqslant b$ W no stationary point, drive directly to MIT, time $f ^ { * * * }$

The heart of this subject is in “word problems.” All the calculus is in a few lines, computing $f ^ { \prime }$ and solving $f ^ { \prime } ( x ) = 0$ : The formulation took longer. Step 1 usually does:

1. Express the quantity to be minimized or maximized as a function $f ( x )$ : The variable $x$ has to be selected.

2. Compute $f ^ { \prime } ( x )$ , solve $f ^ { \prime } ( x ) = 0$ , check critical points for $f _ { \mathrm { m i n } }$ and $f _ { \mathrm { m a x } }$

A picture of the problem (and the graph of $f ( x ) )$ makes all the difference.

EXAMPLE 7 (continued) Choose $x$ as an angle instead of a distance. Figure 3.6 shows the triangle with angle $x$ and side $a$ : The driving distance to the expressway is $a \sec x$ : The distance on the expressway is $b - a$ tan $x$ : Dividing by the speeds 30 and 60, the driving time has a nice form:

$$
f ( x ) = { \mathrm { t o t a l ~ t i m e } } = { \frac { a { \sec { x } } } { 3 0 } } + { \frac { b - a \tan { x } } { 6 0 } } .
$$

The derivatives of sec $x$ and tan $x$ go into $d f / d x$ :

$$
{ \frac { d f } { d x } } = { \frac { a } { 3 0 } } \sec x \tan x - { \frac { a } { 6 0 } } \sec ^ { 2 } x .
$$

Now set $d f / d x = 0$ , divide by $a$ , and multiply by $3 0 \mathrm { c o s } ^ { 2 } x$ :

$$
\begin{array} { r } { \sin x = \frac { 1 } { 2 } . } \end{array}
$$

This answer is beautiful. The angle $x$ is $3 0 ^ { \circ } !$ That optimal angle $_ { \cdot \pi / 6 }$ radians) has sin $\begin{array} { r } { x = \frac { 1 } { 2 } } \end{array}$ : The triangle with side $a$ and hypotenuse $a / \sqrt { 3 }$ is a 30–60–90 right triangle.

I don’t know whether you prefer $\sqrt { a ^ { 2 } + x ^ { 2 } }$ or trigonometry. The minimum is exactly as before—either at $3 0 ^ { \circ }$ or going directly to MIT.

EXAMPLE 8 In mechanics, nat¡ure chooses minimum energy. A spring is pulled dow n by a mass, the energy is $f ( x )$ , and $d f / d x = 0$ gives equilibrium. It is a philosophical question why so many laws of physics involve minimum energy or minimum time—which makes the mathematics easy.

The energy has two terms—for the spring and the mass. The spring energy is ${ \scriptstyle { \frac { 1 } { 2 } } } k x ^ { 2 }$ —positive in stretching $\ b { x } > 0$ is downward) and also positive in compression $( x < 0 )$ : The potential energy of the mass is taken as $- m x$ —decreasing as the mass goes down. The balance is at the minimum of $\begin{array} { r } { f ( x ) = \frac { 1 } { 2 } k x ^ { 2 } - m x } \end{array}$ :

I apologize for giving you such a small problem, but it makes a crucial point. When $f ( x )$ is quadratic, the equilibrium equation $d f / d x = 0$ is linear.

$$
d f / d x = k x - m = 0 .
$$

Graphically, $x = m / k$ is at the bottom of the parabola. Physically, $k x = m$ is a balance of forces—the spring force against the weight. Hooke’s law for the spring force is elastic constant $k$ times displacement $x$ :

EXAMPLE 9 Derivative of cost $\mathbf { \tau } =$ marginal cost (our first management example).

The paper to print $x$ copies of this book might cost $C = 1 0 0 0 + 3 x$ dollars. The derivative is $d C / d x = 3$ : This is the marginal cost of paper for each additional book. If $x$ increases by one book, the cost $C$ increases by $\$ 3$ : The marginal cost is like the velocity and the total cost is like the distance.

Marginal cost is in doll ars per book. Total cost is in dollars. On the plus side, the income is $I ( x )$ and the marginal income is $d I / d x$ : To apply calculus, we overlook the restriction to whole numbers.

Suppose the number of books increases by $d x . \dagger$ The cost goes up by $( d C / d x ) d x$ : The income goes up by $( d I / d x ) d x$ : If we skip all other costs, then profit $P ( x ) =$ income $I ( x ) -$ cost $C ( x )$ . In most cases $P$ increases to a maximum and falls back.

At the high point on the profit curve, the marginal profit is zero:

$$
d P / d x = 0 \quad { \mathrm { o r } } \quad d I / d x = d C / d x .
$$

Profit is maximized when marginal income $I ^ { \prime }$ equals marginal cost $C ^ { \prime }$ .

This basic rule of economics comes directly from calculus, and we give an example:

$C ( x ) = c o s t o f x a d \nu e r t i s e m e n t s = 9 0 0 + 4 0 0 x - x ^ { 2 }$ setup cost 900, print cost $4 0 0 x$ ; volume savings $x ^ { 2 }$   
$I ( x ) = i n c o m e d u e t o \ x a d \nu e r t i s e m e n t s = 6 0 0 x - 6 x ^ { 2 }$ sales 600 per advertisement, subtract $6 x ^ { 2 }$ for diminishing returns

optimal decis $\begin{array} { r l } & { \textit { n d C } / d x = d I / d x \quad \mathrm { o r } \quad 4 0 0 - 2 x = 6 0 0 - 1 2 x \quad \mathrm { o r } \quad x = 2 0 } \\ & { \textit { p r o f t } = i n c o m e - c o s t = 9 6 0 0 - 8 5 0 0 = 1 1 0 0 . } \end{array}$

The next section shows how to verify that this profit is a maximum not a minimum. The first exercises ask you to solve $d f / d x = 0$ : Later exercises also look for $f ( x )$ :