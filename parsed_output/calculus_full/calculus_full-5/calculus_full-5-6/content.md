# 5.6 Properties of the Integral and Average Value

The previous section reached the definition of $\textstyle \int _ { a } ^ { b } v ( x ) d x$ : But the subject cannot stop there. The integral was defined in order to be used. Its properties are important, and its applications are even more important. The definition was chosen so that the integral has properties that make the applications possible.

One direct application is to the average value of $v ( x )$ : The average of $n$ numbers is clear, and the integral extends that idea—it produces the average of a whole continuum of numbers $v ( x )$ : This develops from the last rule in the following list (Property 7). We now collect together seven basic properties of definite integrals.

The addition rule for $\textstyle \int [ v ( x ) + w ( x ) ] d x$ will not be repeated—even though this property of linearity is the most fundamental. We start instead with a different kind of addition. There is only one function $v ( x )$ , but now there are two intervals.

The integral from a to $b$ is added to its neighbor from $b$ to $c$ : Their sum is the integral from a to $c$ . That is the first (not surprising) property in the list.

Property 1 Areas over neighboring intervals add to the area over the combined interval:

$$
\begin{array} { r } { \int _ { a } ^ { b } v ( x ) d x + \int _ { b } ^ { c } v ( x ) d x = \int _ { a } ^ { c } v ( x ) d x . } \end{array}
$$

This sum of areas is graphically obvious (Figure 5.11a). It also comes from the formal definition of the integral. Rectangular areas obey (1)—with a meshpoint at $x = b$ to make sure. When $\Delta x _ { \mathrm { m a x } }$ approaches zero, their limits also obey (1). All the normal rules for rectangular areas are obeyed in the limit by integrals.

Property 1 is worth pursuing. It indicates how to define the integral when $a = b$ : The integral “from $b$ to $b ^ { \prime \prime }$ is the area over a point, which we expect to be zero. It is.

# Property 2

$$
\begin{array} { r } { \int _ { b } ^ { b } v ( x ) d x = 0 . } \end{array}
$$

That comes from Property 1 when $c = b$ : Equation (1) has two identical integrals, so the one from $b$ to $b$ must be zero. Next we see what happens if $c = a$ —which makes the second integral go from $b$ to $a$ :

What happens when an integral goes backward? The “lower limit” is now the larger number $b$ : The “upper limit” $a$ is smaller. Going backward reverses the sign:

# Property 3

$$
\begin{array} { r } { \int _ { b } ^ { a } v ( x ) d x = - \int _ { a } ^ { b } v ( x ) d x = f ( a ) - f ( b ) . } \end{array}
$$

Proof When $c = a$ the right side of (1) is zero. Then the integrals on the left side must cancel, which is Property 3. In going from $b$ to a the steps $\Delta x$ are negative. That justifies a minus sign on the rectangular areas, and a minus sign on the integral (Figure 5.11b). Conclusion: Property 1 holds for any ordering of $a , b , c$ :

$$
\int _ { x } ^ { 0 } t ^ { 2 } d t = - { \frac { x ^ { 3 } } { 3 } } \qquad \int _ { 1 } ^ { 0 } d t = - 1 \qquad \int _ { 2 } ^ { 2 } { \frac { d t } { t } } = 0
$$

Property 4 For odd functions $\int _ { - a } ^ { a } v ( x ) d x = 0$ : “Odd” means that $v ( - x ) = - v ( x )$ : For even functions $\textstyle \int _ { - a } ^ { a } v ( x ) d x = 2 \int _ { 0 } ^ { a } v ( x ) d x$ : “Even” means that $v ( - x ) = + v ( x )$ :

The functions $x , x ^ { 3 } , x ^ { 5 } , \ldots$ are odd. If $x$ changes sign, these powers change sign. The functions sin $x$ and tan $x$ are also odd, together with their inverses. This is an

important family of functions, and the integral of an odd function from $- a$ to a equals zero. Areas cancel:

$$
\begin{array} { r } { \int _ { - a } ^ { a } 6 x ^ { 5 } d x = x ^ { 6 } \exists _ { - a } ^ { a } = a ^ { 6 } - ( - a ) ^ { 6 } = 0 . } \end{array}
$$

If $v ( x )$ is odd then $f ( x )$ is even! All powers $1 , x ^ { 2 } , x ^ { 4 }$ ; : : : are even functions. Curious fact: Odd function times even function is odd, but odd number times even number is even.

For even functions, areas add: $\int _ { - a } ^ { a }$ cos $x d x = \sin a - \sin ( - a ) = 2 \sin a .$

The next properties involve inequalities. If $v ( x )$ is positive, the area under its graph is positive (not surprising). Now we have a proof: The lower sums $s$ are positive and they increase toward the area integral. So the integral is positive:

A positive velocity me¤ans a po¤sitive distance¤. A p¤ositive $v$ lies above a positive area. A more general statement is true. Suppose $v ( x )$ stays between a lower function $l ( x )$ and an upper function $u ( x )$ : Then¤the rectangles f¤or $v$ stay between the rectangles for $l$ and $u$ : In the limit, the area under $v$ (Figure 5.12) is between the areas under $l$ and $u$ :

Property 6 If $l ( x ) \leqslant v ( x ) \leqslant u ( x )$ for $a \leqslant x \leqslant b$ then

$$
\begin{array} { r } { \int _ { a } ^ { b } l ( x ) d x \leqslant \int _ { a } ^ { b } v ( x ) d x \leqslant \int _ { a } ^ { b } u ( x ) d x . } \end{array}
$$

$$
{ \begin{array} { r c c c c } { \cos t \leqslant 1 } & { \Rightarrow } & { \int _ { 0 } ^ { x } \cos t d t \leqslant \int _ { 0 } ^ { x } 1 d t } & { \Rightarrow } & { \sin x \leqslant x } \\ { 1 \leqslant \sec ^ { 2 } t } & { \Rightarrow } & { \int _ { 0 } ^ { x } 1 d t \leqslant \int _ { 0 } ^ { x } \sec ^ { 2 } t d t } & { \Rightarrow } & { x \leqslant \tan x } \end{array} }
$$

EXAMPLE 3 Integrating ${ \frac { 1 } { 1 + x ^ { 2 } } } \leqslant 1$ leads to $\cdot \mathrm { a n } ^ { - 1 } x \leqslant x$ :

All those examples are for $x > 0$ : You may remember that Section 2.4 used geometry to prove sin $h < h < \tan h$ : Examples 1–2 seem to give new and shorter proofs. But I think the reasoning is doubtful. The inequalities were needed to compute the derivatives (therefore the integrals) in the first place.

Property 7 (Mean Value Theorem for Integrals) If $v ( x )$ is continuous, there is a point $c$ between $a$ and $b$ where $v ( c )$ equals the average value of $v ( x )$ :

$$
v ( c ) = \frac { 1 } { b - a } \int _ { a } ^ { b } v ( x ) d x = \ " a \nu e r a g e \nu a l u e o f v ( x ) . \mathrm { , } 
$$

This is the same as the ordinary Mean Value Theorem (for the derivative of $f ( x ) )$ :

$$
f ^ { \prime } ( c ) = { \frac { f ( b ) - f ( c ) } { b - a } } = \sp { \ast } \mathrm { a v e r a g e ~ s l o p e ~ o f ~ } f . \nonumber
$$

With $f ^ { \prime } = v$ ; (3) and (4) are the same equation. But honesty makes me admit to a flaw in the logic. We need the Fundamental Theorem of Calculus to guarantee that $\textstyle f ( x ) = \int _ { a } ^ { x } v ( t ) d t$ really gives $f ^ { \prime } = v$ :

A direct proof of (3) places one rectangle across the interval from $a$ to $b$ : Now raise the top of that rectangle, starting at $v _ { \mathrm { m i n } }$ (the bottom of the curve) and moving up to $v _ { \mathrm { m a x } }$ (the top of the curve). At some height the area will be just right—equal to the area under the curve. Then the rectangular area, which is $( b - a )$ times $v ( c )$ , equals the curved area $\textstyle \int _ { a } ^ { b } v ( x ) d x$ : This is equation (3).

$$
v _ { \mathrm { a v c } } = 0 \overbrace { \int _ { c = 0 } ^ { c } { \frac { 1 } { 1 } } \int _ { c } ^ { c } { \frac { 1 } { 1 / { \sqrt { 3 } } } } \left\{ \begin{array} { l l } { \displaystyle \sum _ { j = 1 } ^ { N - 1 } { \frac { 1 } { 2 \sqrt { 3 } } } = { \displaystyle \prod _ { i } \frac { 1 } { 3 } } v _ { \mathrm { a v c } } = \frac { 1 } { 3 } \quad } & { \displaystyle \sum _ { 0 } ^ { i } { \widehat { c - \frac { 1 } { 5 } } } v _ { \mathrm { a v c } } = \frac { 1 } { 2 } } \\ { \displaystyle v ( x ) = x } & { v ( x ) = x ^ { 2 } } \end{array} \right. } ^ { \prime } \underbrace { v _ { \mathrm { a v c } } } _ { \displaystyle c } ,
$$

That direct proof uses the intermediate value theorem: A continuous function $v ( x )$ takes on every height between $v _ { \mathrm { m i n } }$ and $v _ { \mathrm { m a x } }$ : At some point (at two points in Figure 5.12c) the function $v ( x )$ equals its own average value.

Figure 5.13 shows equal areas above and below the average height $v ( c ) =$ $v _ { \mathrm { a v e } }$ .

EXAMPLE 4 The average value of an odd function is zero (between $^ { - 1 }$ and 1):

$$
{ \frac { 1 } { 2 } } \int _ { - 1 } ^ { 1 } { x d x } = { \frac { x ^ { 2 } } { 4 } } { \Biggr ] } _ { - 1 } ^ { 1 } = { \frac { 1 } { 4 } } - { \frac { 1 } { 4 } } = 0
$$

For once we know $c$ : It is the center point $x = 0$ ; where $v ( c ) = v _ { \mathrm { a v e } } = 0$ :

EXAMPLE 5 The average value of $x ^ { 2 }$ is $\frac 1 3$ (between 1 and $^ { - 1 }$ ):

$$
{ \frac { 1 } { 2 } } \int _ { - 1 } ^ { 1 } { x ^ { 2 } d x } = { \frac { x ^ { 3 } } { 6 } } { \Bigg ] } _ { - 1 } ^ { 1 } = { \frac { 1 } { 6 } } - \left( - { \frac { 1 } { 6 } } \right) = { \frac { 1 } { 3 } }
$$

Where does this function $x ^ { 2 }$ equal its average value ${ \frac { 1 } { 3 } } \ ?$ That happens when $\begin{array} { r } { c ^ { 2 } = { \frac { 1 } { 3 } } } \end{array}$ , so $c$ can be either of the points $1 / \sqrt { 3 }$ and $- 1 / \sqrt { 3 }$ in Figure 5.13b. Those are the Gauss points, which are terrific for numerical integration as Section 5.8 will show.

EXAMPLE 6 The average value of $\sin ^ { 2 } x$ over a period (zero to $\pi$ ) is $\frac { 1 } { 2 }$

$$
{ \frac { 1 } { \pi } } \int _ { 0 } ^ { \pi } \sin { x ^ { 2 } } d x = { \frac { x - \sin x \cos x } { 2 \pi } } { \bmod { \frac { \pi } { 2 } } } = { \frac { 1 } { 2 } } \qquad \left( \operatorname { n o t e } { \frac { 1 } { b - a } } = { \frac { 1 } { \pi } } \right)
$$

The point $c$ is $\pi / 4$ or $3 \pi / 4$ , where $\begin{array} { r } { \sin ^ { 2 } c = \frac { 1 } { 2 } } \end{array}$ : The graph of $\sin ^ { 2 } x$ oscillates around its average value $\frac { 1 } { 2 }$ . See the figure or the formula:

$$
\begin{array} { r } { \sin ^ { 2 } x = \frac { 1 } { 2 } - \frac { 1 } { 2 } \cos 2 x . } \end{array}
$$

The steady term is $\frac { 1 } { 2 }$ , the oscillation is $\begin{array} { r } { - \frac { 1 } { 2 } \cos 2 x } \end{array}$ : The integral is $\begin{array} { r } { f ( x ) = \frac { 1 } { 2 } x - } \end{array}$ $\textstyle { \frac { 1 } { 4 } }$ sin $2 x$ , which is the same as ${ \frac { 1 } { 2 } } x - { \frac { 1 } { 2 } } \sin x$ cos $x$ : This integral of $\sin ^ { 2 } x$ will be seen again. Please verify that $d f / d x = \sin ^ { 2 } x$ :

# THE AVERAGE VALUE AND EXPECTED VALUE

The “average value” from $a$ to $b$ is the integral divided by the length $b - a$ : This was computed for $x$ and $x ^ { 2 }$ and $\sin ^ { 2 } x$ , but not explained. It is a major application of the integral, and it is guided by the ordinary average of $n$ numbers:

$$
v _ { \mathrm { a v e } } = { \frac { 1 } { b - a } } \int _ { a } ^ { b } v ( x ) d x \qquad { \mathrm { c o m e s ~ f r o m } } \qquad v _ { \mathrm { a v e } } = { \frac { 1 } { n } } ( v _ { 1 } + v _ { 2 } + \cdots + v _ { n } ) .
$$

Integration is parallel to summation! Su ms approach integrals. Discrete averages approach continuous averages. The average of $\frac { 1 } { 3 } , \frac { 2 } { 3 } , \frac { 3 } { 3 }$ is $\frac { 2 } { 3 }$ : The average of $\textstyle { \frac { 1 } { 5 } } , { \frac { 2 } { 5 } } , { \frac { 3 } { 5 } } , { \frac { 4 } { 5 } } , { \frac { 5 } { 5 } }$ is $\frac { 3 } { 5 }$ : The average of $n$ numbers from $1 / n$ to $n / n$ is

$$
v _ { \mathrm { a v e } } = { \frac { 1 } { n } } \left( { \frac { 1 } { n } } + { \frac { 2 } { n } } + \cdots + { \frac { n } { n } } \right) = { \frac { n + 1 } { 2 n } } .
$$

The middle term givÑes the average, when $n$ is odd. Or we can do the addition. As $n \to \infty$ the sum approaches an integral (do you see the rectangles?). The ordinary average of numbers becomes the continuous average of $v ( x ) = x$ :

$$
{ \frac { n + 1 } { 2 n } } \to { \frac { 1 } { 2 } } \quad { \mathrm { ~ a n d ~ } } \quad \int _ { 0 } ^ { 1 } x d x = { \frac { 1 } { 2 } } \quad { \bigg ( } { \mathrm { n o t e } } { \frac { 1 } { b - a } } = 1 { \bigg ) } \quad
$$

In ordinary language: “The average value of the numbers between 0 and 1 is $\frac { 1 } { 2 }$ :” Since a whole continuum of numbers lies between 0 and 1, that statement is meaningless until we have integration.

The average value of the squares of those numbers is $\begin{array} { r } { ( x ^ { 2 } ) _ { \mathrm { a v e } } = \int x ^ { 2 } d x / ( b - a ) = \frac { 1 } { 3 } } \end{array}$ If you pick a number randomly between 0 and 1; its expected value is $\frac { 1 } { 2 }$ and its expected square is $\frac 1 3$ .

To me that sentence is a puzzle. First, we don’t expect the number to be exactly $\frac { 1 } { 2 }$ —so we need to define “expected value.” Second, if the expected value is $\frac { 1 } { 2 }$ , why is the expected square equal to $\frac 1 3$ instead of $\textstyle { \frac { 1 } { 4 } } ?$ The ideas come from probability theory, and calculus is leading us to continuous probability. We introduce it briefly here, and come back to it in Chapter 8.

# PREDICTABLE AVERAGES FROM RANDOM EVENTS

Suppose you throw a pair of dice. The outcome is not predictable. Otherwise why throw them? But the average over more and more throws is totally predictable. We don’t know what will happen, but we know its probability.

For dice, we are adding two numbers between 1 and 6: The outcome is between 2 and 12: The probability of 2 is the chance of two ones: $( 1 / 6 ) ( 1 / 6 ) = 1 / 3 6 .$ : Beside each outcome we can write its probability:

$$
2 \left( { \frac { 1 } { 3 6 } } \right) 3 \left( { \frac { 2 } { 3 6 } } \right) 4 \left( { \frac { 3 } { 3 6 } } \right) 5 \left( { \frac { 4 } { 3 6 } } \right) 6 \left( { \frac { 5 } { 3 6 } } \right) 7 \left( { \frac { 6 } { 3 6 } } \right) 8 \left( { \frac { 5 } { 3 6 } } \right) 9 \left( { \frac { 4 } { 3 6 } } \right) 1 0 \left( { \frac { 3 } { 3 6 } } \right) 1 1 \left( { \frac { 2 } { 3 6 } } \right) 1 2 \left( { \frac { 1 } { 3 6 } } \right)
$$

To repeat, one roll is unpredictable. Only the probabilities are known, and they add to 1: (Those fractions add to $3 6 / 3 6$ ; all possibilities are covered.) The total from a million rolls is even more unpredictable—it can be anywhere between 2; 000; 000 and 12; 000; 000: Nevertheless the average of those million outcomes is almost completely predictable. This expected value is found by adding the products in that line above:

Expected value: multiply (outcome) times (probability of outcome) and add:

$$
{ \frac { 2 } { 3 6 } } + { \frac { 6 } { 3 6 } } + { \frac { 1 2 } { 3 6 } } + { \frac { 2 0 } { 3 6 } } + { \frac { 3 0 } { 3 6 } } + { \frac { 4 2 } { 3 6 } } + { \frac { 4 0 } { 3 6 } } + { \frac { 3 6 } { 3 6 } } + { \frac { 3 0 } { 3 6 } } + { \frac { 2 2 } { 3 6 } } + { \frac { 1 2 } { 3 6 } } = 7 .
$$

If you throw the dice 1000 times, and the average is not between 6:9 and 7:1, you get an A. Use the random number generator on a computer and round off to integers.

Now comes continuous probability. Suppose all numbers between 2 and 12 are equally probable. This means all numbers—not just integers. What is the probability of hitting the particular number $x = \pi ? I t$ is zero! By any reasonable measure, $\pi$ has no chance to occur. In the continuous case, every $x$ has probability zero. But an interval of $x$ ’s has a nonzero probability:

the probability of an outcome between 2 and 3 is $1 / 1 0$ the probability of an outcome between $x$ and $x + \Delta x$ is $\Delta x / 1 0$

To find the average, add up each outcome times the probability of that outcome. First divide 2 to 12 into intervals of length $\Delta x = 1$ and probability $p = 1 / 1 0$ : If we round off $x$ , the average is $6 \textstyle { \frac { 1 } { 2 } }$ :

$$
2 \left( { \frac { 1 } { 1 0 } } \right) + 3 \left( { \frac { 1 } { 1 0 } } \right) + \cdots + 1 1 \left( { \frac { 1 } { 1 0 } } \right) = 6 . 5 .
$$

Here all outcomes are integers (as with dice). It is more accurate to use 20 intervals of length $1 / 2$ and probability $1 / 2 0$ : The average is $6 { \frac { 3 } { 4 } }$ , and you see what is coming. These are rectangular areas (Riemann sums). As $\Delta x \to 0$ they approach an integral. The probability of an outcome between $x$ and $x + d x$ is $p ( x ) d x$ , and this problem has $p ( x ) = 1 / 1 0$ : The average outcome in the continuous case is not a sum but an integral:

$$
e x p e c t e d \nu a l u e E ( x ) = \int _ { 2 } ^ { 1 2 } x p ( x ) d x = \int _ { 2 } ^ { 1 2 } x { \frac { d x } { 1 0 } } = { \frac { x ^ { 2 } } { 2 0 } } \int _ { 2 } ^ { 1 2 } = 7 .
$$

That is a big jump. From the point of view of integration, it is a limit of sums. From the point of view of probability, the chance of each outcome is zero but the probability density at $x$ is $p ( x ) = 1 / 1 0$ : The integral of $p ( x )$ is 1, because so?me outcome must happen. The integral of $x p ( x )$ is $x _ { \mathrm { a v e } } = 7$ , the expected value. Each choice of $x$ is random, but the average is predictable.



This completes a first step in probability theory. The second step comes after more calculus. Decaying probabilities use $e ^ { - x }$ and $e ^ { - x ^ { 2 } }$ ?—then the chance of a large $x$ is very small. Here we end with the expected values of $x ^ { n }$ and $1 / { \sqrt { x } }$ and $1 / x$ , for a random choice between 0 and 1 (so $p ( x ) = 1 \backslash$ :

$$
E ( x ^ { n } ) = \int _ { 0 } ^ { 1 } x ^ { n } d x = { \frac { 1 } { n + 1 } } \qquad E \left( { \frac { 1 } { \sqrt { x } } } \right) = \int _ { 0 } ^ { 1 } { \frac { d x } { \sqrt { x } } } = 2 \qquad E \left( { \frac { 1 } { x } } \right) = \int _ { 0 } ^ { 1 } { \frac { d x } { x } } = \infty ( 1 )
$$

# A CONFUSION ABOUT “EXPECTED” CLASS SIZE

A college can advertise an average class size of 29; while most students are in large classes most of the time. I will show quickly how that happens.

Suppose there are 95 classes of 20 students and 5 classes of 200 students. The total enrollment in 100 classes is $1 9 0 0 + 1 0 0 0 = 2 9 0 0$ : A random professor has expected class size 29: But a random student sees it differently. The probability is 1900=2900 of being in a small class and $1 0 0 0 / 2 9 0 0$ of being in a large class. Adding class size times probability gives the expected class size for the student:

$$
\left( { \frac { 1 9 0 0 } { 2 9 0 0 } } \right) + ( 2 0 0 ) \left( { \frac { 1 0 0 0 } { 2 9 0 0 } } \right) = 8 2
$$

Similarly, the average waiting time at a restaurant seems like 40 minutes (to the customer). To the hostess, who averages over the whole day, it is 10 minutes. If you came at a random time it would be10, but if you are a random customer it is 40:

Traffic problems could be eliminated by raising the average number of people per car to 2:5, or even 2: But that is virtually impossible. Part of the problem is the difference between (a) the percentage of cars with one person and (b) the percentage of people alone in a car. Percentage (b) is smaller. In practice, most people would be in crowded cars. See Problems $^ { 3 7 - 3 8 }$ :