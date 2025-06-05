# 4.2 Implicit Differentiation and Related Rates

We start with the equations $x y = 2$ and $y ^ { 5 } + x y = 3$ : As $x$ changes, these $y$ ’s will change—to keep $( x , y )$ on the curve. We want to know $d y / d x$ at a typical point. For $x y = 2$ that is no trouble, but the slope of $y ^ { 5 } + x y = 3$ requires a new idea.

In the first case, solve for $y = 2 / x$ and take its derivative: $d y / d x = - 2 / x ^ { 2 }$ : The curve is a hyperbola. At $x = 2$ the slope is $- 2 / 4 = - 1 / 2$ :

The problem with $y ^ { 5 } + x y = 3$ is that it can’t be solved for $y$ : Galois proved that there is no solution formula for fifth-degree equations. $\dag$ The function $y ( x )$ cannot be given explicitly. All we have is the implicit definition of $y$ , as a solution to $y ^ { 5 } + x y = 3$ : The point $x = 2$ , $y = 1$ satisfies the equation and lies on the curve, but how to find $d y / d x ?$

This section answers that question. It is a situation that often occurs. Equations like sin $y + \sin x = 1$ or $y$ sin $y = x$ (maybe even sin $y = x .$ ) are difficult or impossible to solve directly for $y$ : Nevertheless we can find $d y / d x$ at any point.

The way out is implicit differentiation. Work with the equation as it stands. Find the $x$ derivative of every term in $y ^ { 5 } + x y = 3$ . That includes the constant term 3; whose derivative is zero.

EXAMPLE 1 The power rule for $y ^ { 5 }$ and the product rule for $x y$ yield

$$
5 y ^ { 4 } { \frac { d y } { d x } } + x { \frac { d y } { d x } } + y = 0 .
$$

Now substitute the typical point $x = 2$ and $y = 1$ , and solve for $d y / d x$ :

$$
5 { \frac { d y } { d x } } + 2 { \frac { d y } { d x } } + 1 = 0 \quad { \mathrm { p r o d u c e s } } \quad { \frac { d y } { d x } } = - { \frac { 1 } { 7 } } .
$$

This is implicit differentiation $\mathbf { \left( I D \right) }$ , and you see the idea: Include $d y / d x$ from the chain rule, even if $y$ is not known explicitly as a function of $x$ :

EXAMPLE 2 s $\ln y + \sin x = 1 { \mathrm { ~ l e a d s ~ t o ~ c o s ~ } } y { \frac { d y } { d x } } + \cos x = 0$

EXAMPLE 3 $y \sin y = x \operatorname { l e a d s } \operatorname { t o } y \cos y { \frac { d y } { d x } } = \sin y { \frac { d y } { d x } } = 1$

Knowing the slope makes it easier to draw the curve. We still need points $( x , y )$ that satisfy the equation. Sometimes we can solve for $x$ : Dividing $y ^ { 5 } + x y = 3$ by $y$ gives $x = { 3 / y - \overset { \cdot } { y } ^ { 4 } }$ : Now the derivative (the $x$ derivative!) is

$$
1 = \left( - { \frac { 3 } { y ^ { 2 } } } - 4 y ^ { 3 } \right) { \frac { d y } { d x } } = - 7 { \frac { d y } { d x } } { \mathrm { a t } } y = 1 .
$$

Again $d y / d x = - 1 / 7$ : All these examples confirm the main point of the section:

4B (Implicit differentiation) An equation $F ( x , y ) = 0 $ can be differentiated directly by the chain rule, without solving for $y$ in terms of $x$ :

The example $x y = 2$ , done implicitly, gives $x d y / d x + y = 0$ : The slope $d y / d x$ is $- y / x$ : That agrees with the explicit slope $- 2 / x ^ { 2 }$ :

ID is explained better by examples than theory (maybe everything is). The essential theory can be boiled down to one idea: “Go ahead and differentiate.”

# 4 Derivatives by the Chain Rule

EXAMPLE 4 Find the tangent direction to the circle $x ^ { 2 } + y ^ { 2 } = 2 5$ :

We can solve for $y = \pm { \sqrt { 2 5 - x ^ { 2 } } }$ , or operate directly on $x ^ { 2 } + y ^ { 2 } = 2 5$ :

$$
2 x + 2 y { \frac { d y } { d x } } = 0 \qquad { \mathrm { o r } } \qquad { \frac { d y } { d x } } = - { \frac { x } { y } } .
$$

Compare with the radius, which has slope $y / x$ : The radius goes across $x$ and up $y$ : The tangent goesacross $- y$ and up $x$ : The slopes multiply to give $( - x / y ) ( y / x ) = - 1$ :

To emphasize implicit differentiation, go on to the second derivative. The top of the circle is concave down, so $d ^ { 2 } y / d x ^ { 2 }$ is negative. Use the quotient rule on $- x / y$ :

$$
{ \frac { d y } { d x } } = - { \frac { x } { y } } \quad { \mathrm { s o } } \quad { \frac { d ^ { 2 } y } { d x ^ { 2 } } } = - { \frac { y d x / d x - x d y / d x } { y ^ { 2 } } } = - { \frac { y + ( x ^ { 2 } / y ) } { y ^ { 2 } } } = - { \frac { y ^ { 2 } + x ^ { 2 } } { y ^ { 3 } } } .
$$

# RELATED RATES

There is a group of problems that has never found a perfect place in calculus. They seem to fit here—as applications of the chain rule. The problem is to compute $d f / d t$ , but the odd thing is that we are given another derivative $d g / d t$ : To find $d f / d t$ , we need a relation between $f$ and $g$ :

The chain rule is $d f / d t = ( d f / d g ) ( d g / d t )$ : Here the variable is $t$ because that is typical in applications. From the rate of change of $g$ we find the rate of change of $f .$ This is the problem of related rates, and examples will make the point.

EXAMPLE 5 The radius of a circle is growing by $d r / d t = 7$ : How fast is the circumference growing? Remember that $C = 2 \pi r$ (this relates $C$ to $r$ ).

Solution

$$
\frac { d C } { d t } = \frac { d C } { d r } \frac { d r } { d t } = ( 2 \pi ) ( 7 ) = 1 4 \pi .
$$

That is pretty basic, but its implications are amazing. Suppose you want to put a rope around the earth that any 7-footer can walk under. If the distance is 24; 000 miles, what is the additional length of the rope? Answer: Only $1 4 \pi$ feet.

More realistically, if two lanes on a circular track are separated by 5 feet, how much head start should the outside runner get? Only $1 0 \pi$ feet. If your speed around a turn is 55 and the car in the next lane goes 56; who wins? See Problem 14:

Examples 6–8 are from the 1988 Advanced Placement Exams (copyright 1989 by the College Entrance Examination Board). Their questions are carefully prepared.

EXAMPLE 6 The sides of the rectangle increase in such a way that $d z / d t = 1$ and $d x / d t = 3 d y / d t$ : At the instant when $x = 4$ and $y = 3$ , what is the value of $d x / d t ?$

Solution The key relation is $x ^ { 2 } + y ^ { 2 } = z ^ { 2 }$ : Take its derivative (implicitly):

$$
2 x { \frac { d x } { d t } } + 2 y { \frac { d y } { d t } } = 2 z { \frac { d z } { d t } } \quad { \mathrm { p r o d u c e s } } \quad 8 { \frac { d x } { d t } } + 6 { \frac { d y } { d t } } = 1 0 .
$$

We used all information, including $z = 5$ , except for $d x / d t = 3 d y / d t$ : The term $6 d y / d t$ equals $2 d x / d t$ , so we have $1 0 d x / d t = 1 0$ : Answer: $d x / d t = 1$ :

EXAMPLE 7 A person 2 meters tall walks directly away from a streetlight that is 8 meters above the ground. If the person’s shadow is lengthening at the rate of $4 / 9$ meters per second, at what rate in meters per second is the person walking?

Solution Draw a figure! You must relate the shadow length $s$ to the distance $x$ from the streetlight. The problem gives $d s / d t = 4 / 9$ and asks for $d x / d t$ :

$$
{ \mathrm { B y ~ s i m i l a r ~ t r i a n g l e s ~ } } { \frac { x } { 6 } } = { \frac { s } { 2 } } \quad { \mathrm { s o } } \quad { \frac { d x } { d t } } = { \frac { 6 } { 2 } } { \frac { d s } { d t } } = ( 3 ) \left( { \frac { 4 } { 9 } } \right) = { \frac { 4 } { 3 } } .
$$

Note This problem was hard. I drew three figures before catching on to $x$ and $s$ : It is interesting that we never knew $x$ or s or the angle.

EXAMPLE 8 An observer at point $A$ is watching balloon $B$ as it rises from point $C$ : (The figure is given.) The balloon is rising at a constant rate of 3 meters per second (this means ${ d y } / { d t } = 3 \$ ) and the observer is 100 meters from point $C$ :

(a) Find the rate of change in $z$ at the in?stant when $y = 5 0$ :(They want $d z / d t .$ .)

$$
z ^ { 2 } = y ^ { 2 } + 1 0 0 ^ { 2 } \Rightarrow 2 z { \frac { d z } { d t } } = 2 y { \frac { d y } { d t } }
$$

$$
z = { \sqrt { 5 0 ^ { 2 } + 1 0 0 ^ { 2 } } } = 5 0 { \sqrt { 5 } } \Rightarrow { \frac { d z } { d t } } = { \frac { 2 \cdot 5 0 \cdot 3 } { 2 \cdot 5 0 { \sqrt { 5 } } } } = { \frac { 3 { \sqrt { 5 } } } { 5 } } .
$$

(b) Find the rate of change in the area of right triangle $B C A$ when $y = 5 0$ :

$$
A = { \frac { 1 } { 2 } } ( 1 0 0 ) ( y ) = 5 0 y \qquad { \frac { d A } { d t } } = 5 0 { \frac { d y } { d t } } = 5 0 \cdot 3 = 1 5 0 .
$$

(c) Find the rate of change in $\theta$ when $y = 5 0$ : (They want d=dt:)

$$
y = 5 0 \Rightarrow \cos \theta = { \frac { 1 0 0 } { 5 0 { \sqrt { 5 } } } } = { \frac { 2 } { \sqrt { 5 } } }
$$

$$
\mathfrak { n } \theta = { \frac { y } { 1 0 0 } } \Rightarrow \sec ^ { 2 } \theta { \frac { d \theta } { d t } } = { \frac { 1 } { 1 0 0 } } { \frac { d y } { d t } } \Rightarrow { \frac { d \theta } { d t } } = \left( { \frac { 2 } { \sqrt { 5 } } } \right) ^ { 2 } { \frac { 3 } { 1 0 0 } } = { \frac { 3 } { 1 2 5 } }
$$

In all problems I first wrote down a relation from the figure: Then $\pmb { I }$ took its derivative: Then I substituted known information: (The substitution is after taking the derivative of tan $\theta = y / 1 0 0$ : If we substitute $y = 5 0$ too soon; the derivative of $5 0 / 1 0 0$ is useless:)

“Candidates are advised to show their work in order to minimize the risk of not receiving credit for it.” $50 \%$ solved Example 6 and $21 \%$ solved Example 7. From 12; 000 candidates, the average on Example 8 (free response) was 6:1 out of 9:

# 4 Derivatives by the Chain Rule

EXAMPLE 9 $A$ is a lighthouse and $B C$ is the shoreline (same figure as the balloon). The light at $A$ turns once a second . $( d \theta / d t = 2 \pi$ radians =second/: How quickly does the receiving point $B$ move up the shoreline?

Solution The figure shows $y = 1 0 0$ tan $\theta$ : The speed $d y / d t$ is $1 0 0 \sec ^ { 2 } \theta d \theta / d t$ : This is $2 0 0 \pi \sec ^ { 2 } \theta$ , so $B$ speeds up as sec $\theta$ increases.

Paradox When $\theta$ approaches a right angle, sec $\theta$ approaches infinity. So does $d y / d t$ : $B$ moves faster than light! This contradicts Einstein’s theory of relativity. The paradox is resolved (I hope) in Problem 18:

If you walk around a light at $A$ , your shadow at $B$ seems to go faster than light. Same problem. This speed is impossible—something has been forgotten.

Smaller paradox (not destroying the theory of relativity). The figure shows $y = z \sin \theta$ Apparently $d y / d t = ( d z / d t ) \sin \theta$ : This is totally wrong. Not only is it wrong, the exact opposite is true: $d z / d t = ( d y / d t ) \sin \theta$ : If you can explain that (Problem 15), then ${ \bf I D }$ and related rates hold no terrors.