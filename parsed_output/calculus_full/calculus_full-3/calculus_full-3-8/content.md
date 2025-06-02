# 3.8 The Mean Value Theorem and l’Hôpital’s Rule

Now comes one of the cornerstones of calculus: the Mean Value Theorem. It connects the local picture (slope at a point) to the global picture (average slope across an interval). In other words it relates $d f / d x$ to $\Delta f / \Delta x$ : Calculus depends on this connection, which we saw first for velocities. If the average velocity is 75, is there a moment when the instantaneous velocity is 75 ?

Without more information, the answer to that question is no. The velocity could be 100 and then 50—averaging 75 but never equal to 75: If we allow a jump in velocity, it can jump right over its average. At that moment the velocity does not exist. (The distance function in Figure 3.26a has no derivative at $x = 1 .$ :) We will take away this cheap escape by requiring a derivative at all points inside the interval.

In Figure 3.26b the distance increases by 150 when $t$ increases by 2: There is a derivative $d f / d t$ at all interior points (but an infinite slope at $t = 0$ ). The average velocity is

$$
\frac { \Delta f } { \Delta t } = \frac { f ( 2 ) - f ( 0 ) } { 2 - 0 } = \frac { 1 5 0 } { 2 } = 7 5 .
$$

The conclusion of the theorem is that $d f / d t = 7 5$ at some point inside the interval. There is at least one point where $f ^ { \prime } ( c ) = 7 5$ :

This is not a constructive theorem. The value of $c$ is not known. We don’t find $c$ , we just claim (with proof) that such a point exists.

3M Mean Value Theorem Suppose $f ( x )$ is continuous in the closed interval $a \leqslant x \leqslant b$ and has a derivative everywhere in the open interval $a < x < b$ : Then ${ \frac { f ( b ) - f ( a ) } { b - a } } = f ^ { \prime } ( c ) { \mathrm { ~ a t ~ s o m e ~ p o i n t ~ } } a < c < b .$ (1)

The left side is the average slope $\Delta f / \Delta x$ : It equals $d f / d x$ at $c$ : The notation for a closed interval [with end1points] is $[ a , b ]$ : For an open interval (without endpoints) we write $( a , b )$ : Thus $f ^ { \prime }$ is defined in $( a , b )$ , and $f$ remains continuous at $a$ and $b$ : A derivative is allowed at those endpoints too—but the theorem doesn1’t require it.

The proof is based on a special case—when $f ( a ) = 0$ and $f ( b ) = 0$ : Suppose the function starts at zero and returns to zero. The average slope or velocity is zero. We have to prove that $f ^ { \prime } ( c ) = 0$ at a point in between. This special case (keeping the assumptions on $f ( x ) )$ is called Rolle’s theorem.

Geometrically, if $f$ goes away from zero and comes back, then $f ^ { \prime } = 0$ at the turn.

3N Rolle’s theorem Suppose $f ( a ) = f ( b ) = 0$ (zero at the ends). Then $f ^ { \prime } ( c ) = 0$ at some point with $a < c < b$ :

Proof At a point inside the interval where $f ( x )$ reaches its maximum or minimum, $d f / d x$ must be zero. That is an acceptable point $c$ : Figure $3 . 2 7 \mathrm { a }$ shows the difference between $f = 0$ (assumed at $a$ and $b$ ) and $f ^ { \prime } = 0$ (proved at $c$ ).

Small problem: The maximum could be reached at the ends $a$ and $b$ , if $f ( x ) < 0$ in between. At those endpoints $d f / d x$ might not be zero. But in that case the minimum is reached at an interior point $c$ , which is equally acceptable. The key to our proof is that a continuous function on $[ a , b ]$ reaches its maximum and minimum. This is the Extreme Value Theorem.

It is ironic that Rolle himself did not believe the logic behind calculus. He may not have believed his own theorem! Probably he didn’t know what it meant—the language of “evanescent quantities” (Newton) and “infinitesimals” (Leibniz) was exciting but frustrating. Limits were close but never reached. Curves had infinitely many flat sides. Rolle didn’t accept that reasoning, and what was really serious, he didn’t accept the conclusions. The Académie des Sciences had to stop his battles (he fought against ordinary mathematicians, not Newton and Leibniz). So he went back to number theory, but his special case when $f ( a ) = f ( b ) = 0$ leads directly to the big one.

Proof of the Mean Value Theorem We are looking for a point where $d f / d x$ equals $\Delta f / \Delta x$ : The idea is to tilt the graph back to Rolle’s special case (when $\Delta f$ was zero). In Figure 3.27b, the distance $F ( x )$ between the curve and the dotted secant line comes from subtraction:

$$
F ( x ) = f ( x ) - \left[ f ( a ) + { \frac { \Delta f } { \Delta x } } ( x - a ) \right] .
$$

At $a$ and $b$ , this distance is $F ( a ) = F ( b ) = 0$ : Rolle’s the1orem applies to $F ( x )$ : There is an interior point where $F ^ { \prime } ( c ) = 0$ : At that point take the derivative of equation (2): $0 = f ^ { \prime } ( c ) - ( \Delta f / \Delta x )$ : The desired point $c$ is fo1und, proving the theorem.

EXAMPLE 1 The function $f ( x ) = { \sqrt { x } }$ goes from zero at $x = 0$ to ten at $x = 1 0 0$ : Its average slope is $\Delta f / \Delta x = 1 0 / 1 0 0$ : The derivative $f ^ { \prime } ( x ) = 1 / 2 { \sqrt { x } }$ exists in the open interval $( 0 , 1 0 0 )$ , even though it blows up at the end $x = 0$ : By the Mean Value Theorem there must be a point where $1 0 / 1 0 0 = f ^ { \prime } ( c ) = 1 / 2 { \sqrt { c } }$ : That point is $c = 2 5$ :

The truth is that nobody cares about the exact value of $c$ : Its existence is what matters. Notice how it affects the linear approximation $f ( x ) \approx f ( a ) + f ^ { \prime } ( a ) ( x -$ $a$ /, which was basic to this chapter. Close bec1omes exact ( $\approx$ becomes $\mathbf { \Psi } = \mathbf { \dot { \Psi } }$ ) when $f ^ { \prime }$ is computed at $c$ instead of $a$ :

3O The derivative at $c$ gives an exact prediction of $f ( x )$ :

$$
f ( x ) = f ( a ) + f ^ { \prime } ( c ) ( x - a ) .
$$

The Mean Value Theorem is rewritten here as $\Delta f = f ^ { \prime } ( c ) \Delta x$ : Now $a < c < x$ :

EXAMPLE 2 The function $f ( x ) = \sin { x }$ starts from $f ( 0 ) = 0$ : The linear prediction (tangent line) uses the slope cos $0 = 1$ : The exact prediction uses¤the slope cos $c$ at an unknown point between 0 and $x$ :

$$
( a p p r o x i m a t e ) \sin x \approx x \qquad ( e x a c t ) \sin x = ( \cos c ) x .
$$

The approxima1tion is useful, because everything is computed at $x = a = 0$ : The exact formula is interesting, because cos $c \leqslant 1$ proves again that sin $x \leqslant x$ : The slope is below 1, so the sine graph stays below the $4 5 ^ { \circ }$ line.

EXAMPLE 3 If $f ^ { \prime } ( c ) = 0$ at all points in an interval then $f ( x )$ is constant.

Proof When $f ^ { \prime }$ is everywhere zero, the theorem gives $\Delta f = 0$ : Every pair of points has $f ( b ) = f ( a )$ : The graph is a horizontal line. That deceptively simple case is a key to the Fundamental Theorem of Calculus.

Most applications of $\Delta f = f ^ { \prime } ( c ) \Delta x$ do not end up with a number. They end up with another theorem (like this one). The goal is to connect derivatives (local) to differences (global). But the next application—l’Hôpital’s Rule—manages to produce a number out of $0 / 0$ :

# L’HÔPITAL’S RULE

# When $f ( x )$ and $g ( x )$ both approach zero, what happens to their ratio $f ( x ) / g ( x ) \}$

$$
{ \frac { f ( x ) } { g ( x ) } } = { \frac { x ^ { 2 } } { x } } \quad { \mathrm { o r } } \quad { \frac { \sin x } { x } } \quad { \mathrm { o r } } \quad { \frac { x - \sin x } { 1 - \cos x } } \quad { \mathrm { a l l ~ b e c o m e } } \quad { \frac { 0 } { 0 } } \quad { \mathrm { a t } } \quad x = 0 .
$$

Since $0 / 0$ is meaningless, we cannot work separately with $f ( x )$ and $g ( x )$ : This is a “race toward zero,” in which two functions become small while t1heir ratio might do anything. The problem is to find the limit of $f ( x ) / g ( x )$ :

One such limit is already studied. $I t$ is the derivative! $\Delta f / \Delta x$ automatically builds in a race toward zero, whose limit is $d f / d x$ :

$$
{ \begin{array} { r l } { f ( x ) - f ( a ) \to 0 } \\ { x \ - \ a \ \to 0 } \end{array} } \quad \mathrm { b u t } \quad \quad \operatorname* { l i m } _ { x \to a } { \frac { f ( x ) - f ( a ) } { x - a } } = f ^ { \prime } ( a ) .
$$

The idea of l’Hôpital is to use $f ^ { \prime } / g ^ { \prime }$ to handle $f / g$ : The derivative is the special case $g ( x ) = x - a$ , with $g ^ { \prime } = 1$ : The Rule is followed by examples and proofs.

3P l’HôpitÑal’s Rule SÑuppo1se $f ( x )$ and $g ( x )$ both approach z1ero as $x \to a$ : Then $f ( x ) / g ( x )$ approaches the same limit as $f ^ { \prime } ( x ) / g ^ { \prime } ( x )$ , if that second limit exists:

$$
\operatorname* { l i m } _ { x \to a } { \frac { f ( x ) } { g ( x ) } } = \operatorname* { l i m } _ { x \to a } { \frac { f ^ { \prime } ( x ) } { g ^ { \prime } ( x ) } } . \qquad { \mathrm { N o r m a l l y ~ t h i s ~ l i m i t ~ i s } } \quad { \frac { f ^ { \prime } ( a ) } { g ^ { \prime } ( a ) } } .
$$

This is not the quotient rule! The derivatives of $f ( x )$ and $g ( x )$ are taken separately. Geometrically, l’Hôpital is saying that when functions go to zero their slopes control their size. An easy case is $f = 6 ( x - a )$ and $g = 2 ( x - a )$ : The ratio $f / g$ is exactly $6 / 2$ , the ratio of their slopes. F8igure3.828 shows these straight lines dropping to zero, controlled by 6 and 2:

The next figure shows the same limit $6 / 2$ , when the curves are tangent to the lines. That picture isthe key to l’Hôpital’s rule.

Generally the limit of $f / g$ can be a finite number $L$ or $+ \infty$ or $- \infty$ : (Also the limit point $x = a$ can represent a finite number or $+ \infty$ or $- \infty$ : We keep it finite.) The one absolute requirement is that $f ( x )$ and $g ( x )$ must sepa1rately approach zero—we insist on $0 / 0$ : Otherwise there is no reason why equation (6) should be true. With $f ( x ) = x$ and $g ( x ) = x - 1 , d o n ^ { \prime } t$ use l’Hôpital:

$$
{ \frac { f ( x ) } { g ( x ) } } \to { \frac { a } { a - 1 } } \qquad \mathrm { b u t } \qquad { \frac { f ^ { \prime } ( x ) } { g ^ { \prime } ( x ) } } = { \frac { 1 } { 1 } } .
$$

Ordinary ratios approach lim $f ( x )$ divided by lim $g ( x )$ : l’Hôpital enters only for $0 / 0$ :

EXAMPLE 4 (an old friend) $\operatorname* { l i m } _ { x \to 0 } { \frac { 1 - \cos x } { x } }$ equals $\operatorname* { l i m } _ { x \to 0 } { \frac { \sin x } { 1 } }$ This equals zero.   
EXAMPLE 5 ${ \frac { f } { g } } = { \frac { \tan x } { \sin x } }$ leads to ${ \frac { f ^ { \prime } } { g ^ { \prime } } } = { \frac { \sec ^ { 2 } x } { \cos x } }$ At $x = 0$ the limit is $\frac { 1 } { 1 }$   
EXAMPLEÑ6 ${ \frac { f } { g } } = { \frac { x - \sin x } { 1 - \cos x } } \ \operatorname { l e a d s } \ \mathrm { t o } \ { \frac { f ^ { \prime } } { g ^ { \prime } } } = { \frac { 1 - \cos x } { \sin x } } .$ At $x = 0$ this is still $\frac { 0 } { 0 }$ ·   
Solution Apply the Rule to $f ^ { \prime } / g ^ { \prime }$ : It has the same limit as $f ^ { \prime \prime } / g ^ { \prime \prime }$ : ${ \mathrm { i f ~ } } { \frac { f } { g } } \to { \frac { 0 } { 0 } } { \mathrm { a n d ~ } } { \frac { f ^ { \prime } } { g ^ { \prime } } } \to { \frac { 0 } { 0 } } { \mathrm { t h e n ~ c o m p u t e } } { \frac { f ^ { \prime \prime } ( x ) } { g ^ { \prime \prime } ( x ) } } = { \frac { \sin x } { \cos x } } \to { \frac { 0 } { 1 } } = 0 .$

# The reason behind l’Hôpital’s Rule is that the followingfractions are the same:

$$
{ \frac { f ( x ) } { g ( x ) } } = { \frac { f ( x ) - f ( a ) } { x - a } } \bigg / { \frac { g ( x ) - g ( a ) } { x - a } } .
$$

That is just algebra; the limit hasn’t happened yet. The factors $x - a$ cancel, and the numbers $f ( a )$ and $g ( a )$ are zero by assumption. Now take the limit on the right side of (7) as $x$ approaches $a$ :

What normally happensÑ is that one part approaches $f ^ { \prime }$ at $x = a$ : The other part approaches $g ^ { \prime } ( a )$ : We hope $g ^ { \prime } ( a )$ is not1 zero. In t1his case we can divid1e one lim1it by the other limit. That gi1ves the “normal” answer

$$
\operatorname* { l i m } _ { x \to a } { \frac { f ( x ) } { g ( x ) } } = \operatorname* { l i m i t } \operatorname { o f } \left( 7 \right) = { \frac { f ^ { \prime } ( a ) } { g ^ { \prime } ( a ) } } .
$$

This is also l’Hôpital’s answer. When $f ^ { \prime } ( x )  f ^ { \prime } ( a )$ and separately $g ^ { \prime } ( x )  g ^ { \prime } ( a )$ , his overall limit is $f ^ { \prime } ( a ) / g ^ { \prime } ( a )$ : He published this rule in the first textbook ever written on differential calculus. (That was in 1696—the limit was actually discovered by his teacher Bernoulli.) Three hundred years later we apply his name to other cases permitted in .6/; when $f ^ { \prime } / g ^ { \prime }$ might approach a8limit8even if the separate parts do not.

To prove this more general form of l’Hôpital’s Rule, we need a more general Mean Value Theorem. $I$ regard the8discussi8on below as optional in a calculus course (but required in a calculus book). T8he  i8mportant i8dea already came in equation (8).

RemarÑk The basiÑc “8indeterminate” is $\infty - \infty$ . If $f ( x )$ and $g ( x )$ approach infinity, anything is possible for $f ( x ) - g ( x )$ : We could have $x ^ { 2 } - x$ or $x - x ^ { 2 }$ or $( x + 2 ) - x$ : Their limits are $\infty$ and $- \infty$ and 2:

At the next level are $0 / 0$ and $\infty / \infty$ and $0 \cdot \infty$ : To find the limit in these cases, try l’Hôp8ital’s R8ule. See Problem 24 when $f ( x ) / g ( x )$ approaches $\infty / \infty$ : When $f ( x )  0$ and $g ( x )  \infty$ , apply the $0 / 0$ rule to $f ( x ) / ( 1 / g ( x ) )$ :

T8he next level has $0 ^ { 0 }$ and $1 ^ { \infty }$ and $\infty ^ { 0 }$ : Those come from limits of $f ( x ) ^ { g ( x ) }$ : If $f ( x )$ approaches $_ { 0 , 1 }$ ; or $\infty$ while $g ( x )$ approaches $0 , \infty$ ; or 0, we need more information. A really curious example is $x ^ { 1 / \ln x }$ , which shows all three possibilities $0 ^ { 0 }$ and $1 ^ { \infty }$ and $\infty ^ { 0 }$ : This function is actually a constant! It equals $e$ :

To go back down a level, take logarithms. Then $g ( x ) \ln f ( x )$ returns to $0 / 0$ and $0 \cdot \infty$ and l’Hôpital’s Rule. But logarithms and $e$ have to wait for Chapter 6.

# THE GENERALIZED MEAN VALUE THEOREM

The MVT can be extended to two functions. The extension is due to Cauchy, who cleared up the whole idea of limits. You will rec ognize the special case $g = x$ as the ordinary Mean Value Theorem.

3Q Generalized MVT If $f ( x )$ and $g ( x )$ are continuous on $[ a , b ]$ and differentiable on $( a , b )$ , there is a point $a < c < b$ where

$$
[ f ( b ) - f ( a ) ] g ^ { \prime } ( c ) = [ g ( b ) - g ( a ) ] f ^ { \prime } ( c ) .
$$

The proof comes by constructing a new function that has $F ( a ) = F ( b )$ :

$$
F ( x ) = [ f ( b ) - f ( a ) ] g ( x ) - [ g ( b ) - g ( a ) ] f ( x ) .
$$

The ordinary Mean Value Theorem leads to $F ^ { \prime } ( c ) = 0$ —which is equation (9).

Application 1 (Proof of l’Hôpital’s Rule) The rule deals with $f ( a ) / g ( a ) = 0 / 0$ Inserting those zeros into equation (9) leaves $f ( b ) g ^ { \prime } ( c ) = g ( b ) f ^ { \prime } ( c )$ : Therefore

$$
\frac { f ( b ) } { g ( b ) } = \frac { f ^ { \prime } ( c ) } { g ^ { \prime } ( c ) } .
$$

As $b$ approaches $a$ , so does $c$ : The point $c$ is squeezed between $a$ and $b$ : The limit of equation (10) as $b \to a$ and $c \to a$ is l’Hôpital’s Rule.

Application 2 (Error in linear approximatio2n) Section 3.2 stated that the distance between a curve and its tangent line grows like $( x - a ) ^ { 2 }$ : Now we can prove this, and find out more. Linear approximation is

$$
f ( x ) = f ( a ) + f ^ { \prime } ( a ) ( x - a ) + e r r o r e ( x ) .
$$

The pattern suggests an error involving $f ^ { \prime \prime } ( x )$ and $( x - a ) ^ { 2 }$ : The key example $f = { \bar { x } } ^ { 2 }$ shows the need for a factor $\frac { 1 } { 2 }$ (to cancel $f ^ { \prime \prime } { = } 2 $ ). The error in linear approximation is

$$
\begin{array} { r } { e ( x ) = \frac { 1 } { 2 } f ^ { \prime \prime } ( c ) ( x - a ) ^ { 2 } \quad \mathrm { w i t h } \quad a < c < x . } \end{array}
$$

Key idea Compare the error $e ( x )$ to $( x - a ) ^ { 2 }$ : Both are zero at $x = a$ :

$$
\begin{array} { l l l } { { e = f ( x ) - f ( a ) - f ^ { \prime } ( a ) ( x - a ) \quad } } & { { e ^ { \prime } = f ^ { \prime } ( x ) - f ^ { \prime } ( a ) \quad } } & { { e ^ { \prime \prime } = f ^ { \prime \prime } ( x ) } } \\ { { g = ( x - a ) ^ { 2 } \quad } } & { { g ^ { \prime } = 2 ( x - a ) \quad } } & { { g ^ { \prime \prime } = 2 } } \end{array}
$$

The Generalized Mean Value Theorem finds a point $C$ between $a$ and $x$ where $e ( x ) / g ( x ) = e ^ { \prime } ( C ) / g ^ { \prime } ( C )$ : This is equation (10) with di2fferent letters. After checking $e ^ { \prime } ( a ) = g ^ { \prime } ( a ) = 0$ , apply the same theorem to $e ^ { \prime } ( x )$ and $g ^ { \prime } ( x )$ : It produces a point $c$ between $a$ and $C$ —certainly between $a$ and $x$ —where

$$
{ \frac { e ^ { \prime } ( C ) } { g ^ { \prime } ( C ) } } = { \frac { e ^ { \prime \prime } ( c ) } { g ^ { \prime \prime } ( c ) } } \quad { \mathrm { a n d ~ t h e r e f o r e } } \quad { \frac { e ( x ) } { g ( x ) } } = { \frac { e ^ { \prime \prime } ( c ) } { g ^ { \prime \prime } ( c ) } } .
$$

With $g = ( x - a ) ^ { 2 }$ and $g ^ { \prime \prime } = 2$ and $e ^ { \prime \prime } = f ^ { \prime \prime }$ , the equation on the right is $\begin{array} { r } { e ( x ) = \frac { 1 } { 2 } f ^ { \prime \prime } ( c ) ( x - a ) ^ { 2 } } \end{array}$ : The error formula is proved. A?very good approximation is ${ \textstyle { \frac { 1 } { 2 } } } f ^ { \prime \prime } ( c ) ( x - a ) ^ { 2 }$ :

EXAMPLE 7 $f ( x ) = { \sqrt { x } } { \mathrm { ~ n e a r ~ } } a = 1 0 0 : { \sqrt { 1 0 2 } } \approx 1 0 + \left( { \frac { 1 } { 2 0 } } \right) 2 + { \frac { 1 } { 2 } } \left( { \frac { - 1 } { 4 0 0 0 } } \right) 2 ^ { 2 } .$ That last term predicts $e = - . 0 0 0 5$ : The actual error is $\sqrt { 1 0 2 } - 1 0 . 1 = - . 0 0 0 4 9 6 .$ :