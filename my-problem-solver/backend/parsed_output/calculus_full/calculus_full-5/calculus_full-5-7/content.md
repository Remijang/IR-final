# 5.7 The Fundamental Theorem and Its Applications

When the endpoints are fixed at $a$ and $b$ , we have a definite integral. When the upper limit is a variable point $x$ , we have an indefinite integral. More generally: When the endpoints depend in any way on $x$ , the integral is a function of $x$ : Therefore we can find its derivative. This requires the Fundamental Theorem of Calculus.

The essence of the Theorem is: Derivative of integral of $v$ equals $v$ . We also compute the derivative when the integral goes from $a ( x )$ to $b ( \boldsymbol { x } )$ —both limits variable.

Part 2 of the Fundamental Theorem reverses the order: Integral of derivative of $f$ equals $f + C$ . That will follow quickly from Part 1, with help from the Mean Value Theorem. It is Part 2 that we use most, since integrals are harder than derivatives.

After the proofs we go to new applications, beyond the standard problem of area under a curve. Integrals can add up rings and triangles and shells—not just rectangles. The answer can be a volume or a probability—not just an area.

# THE FUNDAMENTAL THEOREM, PART 1

Start with a continuous function $v$ : Integrate it from a fixed point $a$ to a variable point $x$ : For each $x$ , this integral $f ( x )$ is a number. We do not require or expect a formula for $f ( x )$ —it is the area out to the point $x$ : It is a function of $x !$ ! The Fundamental Theorem says that this area function has a derivative (another limiting process). The derivative $d f / d x$ equals the original $v ( x )$ :

5C (Fundamental Theorem, Part 1) Suppose $v ( x )$ is a continuous function: $\begin{array} { r } { I f \quad f ( x ) = \int _ { a } ^ { x } v ( t ) d t \quad t h e n \quad d f / d x = v ( x ) . } \end{array}$

The dummy variable is written as $t$ , so we can concentrate on the limits. The value of the integral depends on the limits $a$ and $x$ , not on $t$ :

To find $d f / d x$ , start with $\Delta f = f ( x + \Delta x ) - f ( x ) = c$ ifference of areas:

$$
\begin{array} { r } { \Delta f = \int _ { a } ^ { x + \Delta x } v ( t ) d t - \int _ { a } ^ { x } v ( t ) d t = \int _ { x } ^ { x + \Delta x } v ( t ) d t . } \end{array}
$$

Officially, this is Property 1: The area out to $x + \Delta x$ minus the area out to $x$ equals the small part from $x$ to $x + \Delta x$ : Now divide by $\Delta x$ :

$$
\frac { \Delta f } { \Delta x } = \frac { 1 } { \Delta x } \int _ { x } ^ { x + \Delta x } { v ( t ) d t } = a \nu e r a g e \ \nu a l u e = v ( c ) .
$$

This is Property 7, the Mean Value Theorem for integrals. The average value on this short interval equals $v ( c )$ : This point $c$ is somewhere between $x$ and $x + \Delta x$ (exact position not known), and we let $\Delta x$ approach zero. That squeezes $c$ toward $x$ , so $v ( c )$ approaches $u ( x )$ —remember that $v$ is continuous. The limit of equation (2) is the Fundamental Theorem:

$$
{ \frac { \Delta f } { \Delta x } }  { \frac { d f } { d x } } \quad { \mathrm { a n d } } \quad v ( c )  v ( x ) \quad { \mathrm { s o } } \quad { \frac { d f } { d x } } = v ( x ) .
$$

If $\Delta x$ is negative the reasoning still holds. Why assume that $v ( x )$ is continuous? Because if $v$ is a step function, then $f ( x )$ has a corner where $d f / d x$ is not $v ( x )$ :

# 5 Integrals

We could skip the Mean Value Theorem and simply bound $v$ above and below:

$$
\begin{array} { r l r l } & { \mathrm { ~ f o r ~ } t \mathrm { ~ b e t w e e n ~ } x \mathrm { ~ a n d ~ } x + \Delta x \colon } & { v _ { \operatorname* { m i n } } \leqslant } & { v ( t ) } & { \leqslant v _ { \operatorname* { m a x } } } \\ & { \mathrm { i n t e g r a t e ~ o v e r ~ t h a t ~ i n t e r v a l } \colon } & { v _ { \operatorname* { m i n } } \Delta x \leqslant } & { \Delta f } & { \leqslant v _ { \operatorname* { m a x } } \Delta x } \\ & { \mathrm { d i v i d e ~ b y ~ } \Delta x \colon } & { v _ { \operatorname* { m i n } } \leqslant \Delta f / \Delta x \leqslant v _ { \operatorname* { m a x } } } \end{array}
$$

As $\Delta x \to 0$ , $v _ { \mathrm { m i n } }$ and $v _ { \mathrm { m a x } }$ approach $v ( x )$ : In the limit $d f / d x$ again equals $v ( x )$ :

Graphical meaning The $f$ -graph gives the area under the $v$ -graph. The thin strip in Figure 5.14 has area $\Delta f .$ That area is approximately $v ( x )$ times $\Delta x$ . Dividing by its base, $\Delta f / \Delta x$ is close to the height $v ( x )$ : When $\Delta x \to 0$ and the strip becomes infinitely thin, the expression “close to” converges to “equals.” Then $d f / d x$ is the height at $v ( x )$ :

# DERIVATIVES WITH VARIABLE ENDPOINTS

When the upper limit is $x$ , the derivative is $v ( x )$ : Suppose the lower limit is $x$ : The integral goes from $x$ to $b$ , instead of $a$ to $x$ : When $x$ moves, the lower limit moves. The change in area is on the left side of Figure 5.15. As $x$ goes forward, area is removed. So there is a minus sign in the derivative of area:

$$
T h e d e r i v a t i v e o f g ( x ) = \int _ { x } ^ { b } v ( t ) d t i s \frac { d g } { d x } = - v ( x ) .
$$

The quickest proof is to reverse $b$ and $x$ , which reverses the sign (Property 3):

$$
g ( x ) = - \int _ { b } ^ { x } v ( t ) d t \quad { \mathrm { s o ~ b y ~ P a r t } } 1 \quad { \frac { d g } { d x } } = - v ( x ) .
$$

The general case is messier but not much harder (it is quite useful). Suppose both limits are changing. The upper limit $b ( \boldsymbol { x } )$ is not necessarily $x$ , but it depends on $x$ :

The lower limit $a ( x )$ can also depend on $x$ (Figure 5.15b). The area $A$ between those limits changes as $x$ changes, and we want $d A / d x$ :

$$
I f \quad A = \int _ { a ( x ) } ^ { b ( x ) } v ( t ) d t \quad t h e n \quad { \frac { d A } { d x } } = v ( b ( x ) ) { \frac { d b } { d x } } - v ( a ( x ) ) { \frac { d a } { d x } } .
$$

The figure shows two thin strips, one added to the area and one subtracted.

First check the two cases we know. When $a = 0$ and $b = x$ , we have $d a / d x = 0$ and $d b / d x = 1$ : The derivative according to (6) is $v ( x )$ times 1—the Fundamental Theorem. The other case has $a = x$ and $b =$ constant. Then the lower limit in (6) produces $- v ( x )$ : When the integral goes from $a = 2 x$ to $b = x ^ { 3 }$ , its derivative is new:

# EXAMPLE 1

$$
\begin{array} { r } { A = \int _ { 2 x } ^ { x ^ { 3 } } \cos t d t = \sin x ^ { 3 } - \sin 2 x } \\ { d A / d x = ( \cos x ^ { 3 } ) ( 3 x ^ { 2 } ) - ( \cos 2 x ) ( 2 ) . } \end{array}
$$

That fits with (6), because $d b / d x$ is $3 x ^ { 2 }$ and $d a / d x$ is 2 (with minus sign). It also looks like the ch1ain rule—which1 it is! To prove (6) we use the letters $v$ and $f$ :

$$
{ \begin{array} { r l r l } & { { \boldsymbol { A } } = \displaystyle \int _ { a ( x ) } ^ { b ( x ) } { \boldsymbol { v } } ( t ) d t = f ( b ( x ) ) - f ( a ( x ) ) } & & & { { \mathrm { ( b y ~ P a r t ~ 2 ~ b e l o w ) } } } \\ & { { \cfrac { d { \boldsymbol { A } } } { d x } } = f ^ { \prime } ( b ( x ) ) { \cfrac { d b } { d x } } - f ^ { \prime } ( a ( x ) ) { \cfrac { d a } { d x } } } & & { { \mathrm { ( b y ~ t h e ~ c h a i n ~ r u l e ) } } } \end{array} }
$$

Since $f ^ { \prime } = v$ , eq»uation (6) is proved. In the next example the area turns out to be constant, although it seems to depend on $x$ : Note that $v ( t ) = 1 / t$ so $v ( 3 x ) = 1 / 3 x$ :

EXAMPLE 2 $A = \int _ { 2 x } ^ { 3 x } { \frac { 1 } { t } } d t \ \mathrm { h a s } \ { \frac { d A } { d x } } = \left( { \frac { 1 } { 3 x } } \right) ( 3 ) - \left( { \frac { 1 } { 2 x } } \right) ( 2 ) = 0 .$ Question $A = \int _ { - x } ^ { x } v ( t ) d t$ has ${ \frac { d A } { d x } } = v ( x ) + v ( - x )$ : Why does $v ( - x )$ have a plus sign?

# THE» FUNDAMEN»TAL THEOREM, PART 2

We have used a hundred times the Theorem that is now to be proved. It is the key to integration. “The integral of $d f / d x$ is $f ( x ) + C$ .” The application starts with $v ( x )$ : We search for an $f ( x )$ with this derivative. If $d f / d x = v ( x )$ , the Theorem says that

$$
\int v ( x ) d x = \int { \frac { d f } { d x } } d x = f ( x ) + C .
$$

We can’t rely on knowing formulas for $v$ and $f$ —only the definitions of $\scriptstyle \int$ and $d / d x$ : The proof rests on one extremely special case: $d f / d x$ is the zero function. We easily find $f ( x ) = c o n s t a n t$ . The problem is to prove that there are no other possibilities:1 $f$ must beconstant. When the slope is zero, the graph must be flat. Everybody knows this is true, but intuition is not the same as proof.

Ass1ume that $d f / d x = 0$ in an interval. If $f ( x )$ is not constant, there are points where $f ( a ) \neq f ( b )$ : By the Mean Value Theorem, there is a point $c$ where

$$
f ^ { \prime } ( c ) = { \frac { f ( b ) - f ( a ) } { b - a } } \quad { \mathrm { ( t h i s ~ i s ~ n o t ~ z e r o ~ b e c a u s e } } f ( a ) \neq f ( b ) { \mathrm { ) } } .
$$

But $f ^ { \prime } ( c ) \neq 0$ directly contradicts $d f / d x = 0$ : Therefore $f ( x )$ must be constant.

Note the crucial role of the Mean Value Theorem. A local hypothesis $( d f / d x = 0$ at each point) yields a global conclusion ( $\cdot f =$ constant in the whole interval). The derivative narrows the field of view, the integral widens it. The Mean Value Theorem connects instantaneous to average, local to global, pointsto intervals. This special case (the zero function) applies when $A ( x )$ and $f ( x )$ have the same derivative:

$$
\textit { f } d A / d x = d f / d x \ o n \ a n i n t e r { \nu } a l , t h e n \ A ( x ) = f ( x ) + C .
$$

Reason: The derivative of $A ( x ) - f ( x )$ is zero. So $A ( x ) - f ( x )$ must be constant. Now comes the big theorem. It assumes that $v ( x )$ is continuous, andintegrates using $f ( x )$ :

$$
\boxed { \begin{array} { r l } { \mathrm { 5 D } } & { ( F u n d a m e n t a l T h e o r e m , P a r t 2 ) { \mathrm { I f } } v ( x ) = \cfrac { d f } { d x } \operatorname { t h e n } \int _ { a } ^ { b } v ( x ) d x = f ( b ) - f ( a ) . } \end{array} }
$$

Proof The antiderivative is $f ( x )$ : But Part 1 gave another antiderivative for the same $v ( x )$ : It was the inte1gral—constructed from rectangles and now called $A ( x )$ :

$$
A ( x ) = \int _ { a } ^ { x } v ( t ) d t a l s o h a s \frac { d A } { d x } = v ( x ) .
$$

Since $A ^ { \prime } = v$ and $f ^ { \prime } = v$ , the special case in equation (7) states that $A ( x ) = f ( x ) +$ $C$ : That is the essential point: The integral from rectangles equals $f ( x ) + C$ .

At the lower limit the area integral is $A = 0$ : So $f ( a ) + C = 0$ : At the upper limit $f ( b ) + C = A ( b )$ : Subtract to find $A ( b )$ , the definite integral:

$$
\begin{array} { r } { A ( b ) = \int _ { a } ^ { b } v ( x ) d x = f ( b ) - f ( a ) . } \end{array}
$$

Calculus is beautiful—its Fundamental Theorem is also its most useful theorem.

Another proof of Part 2 starts with $f ^ { \prime } = v$ and looks at subintervals:

$$
\begin{array} { r l r l } { f ( x _ { 1 } ) - f ( a ) = v ( x _ { 1 } ^ { * } ) ( x _ { 1 } - a ) } & { } & & { \mathrm { ( b y ~ t h e ~ M e a n ~ V a l u e ~ T h e o r e m ) } } \\ { f ( x _ { 2 } ) - f ( x _ { 1 } ) = v ( x _ { 2 } ^ { * } ) ( x _ { 2 } - x _ { 1 } ) } & { } & & { \mathrm { ( b y ~ t h e ~ M e a n ~ V a l u e ~ T h e o r e m ) } } \\ { \therefore \dots = \dots } \\ { f ( b ) - f ( x _ { n - 1 } ) = v ( x _ { n } ^ { * } ) ( b - x _ { n - 1 } ) } & { } & & { \mathrm { ( b y ~ t h e ~ M e a n ~ V a l u e ~ T h e o r e m ) } . } \end{array}
$$

The left sides add to $f ( b ) - f ( a )$ : The sum on the right, as $\Delta x  0$ , is $\textstyle \int _ { a } ^ { b } v ( x ) d x$ :

# APPLICATIONS OF INTEGRATION

Up to now the integral has been the area under a curve. There are many other applications, quite different from areas. Whenever addition becomes “continuous,” we have integrals instead of sums. Chapter 8 has space to develop more applications, but four examples can be given immediately—which will make the point.

We stay with geometric problems, rather than launching into physics or engineering or biology or economics. All those will come. The goal here is to take a first step away from rectangles.

EXAMPLE 3 (for circles) The area A and circumference $C$ are related by $d A / d r = C$ .

The question is why. The area is $\pi r ^ { 2 }$ : Its derivative $2 \pi r$ is the circumference. By the Fundamental Theorem, the integral of $C$ is $A$ : What is missing is the geometrical reason. Certainly $\pi r ^ { 2 }$ is the integral of $2 \pi r$ , but what is the real explanation for $\begin{array} { r } { \boldsymbol { A } = \int \boldsymbol { C } ( \boldsymbol { r } ) d \boldsymbol { r } ? } \end{array}$

My point is that the pieces are not rectangles. We could squeeze rectangles under a circular curve, but their heights would have nothing to do with $C$ : Our intuition has to take a completely different direction, and add up the thin rings in Figure 5.16.

Suppose the ring thickness is $\Delta r$ : Then the ring area is close to $C$ times $\Delta r$ : This is precisely the kind of approximation we need, because its error is of higher order $( \Delta r ) ^ { 2 }$ : The integral adds ring areas just as it added rectangular areas:

$$
A = \int _ { 0 } ^ { r } C d r = \int _ { 0 } ^ { r } 2 \pi r \ d r = \pi r ^ { 2 } .
$$

That is our first step toward freedom, away from rectanglesÑto rings.

The ring area $\Delta A$ can be checked exactly—it is the difference of circles:

$$
\Delta A = \pi ( r + \Delta r ) ^ { 2 } - \pi r ^ { 2 } = 2 \pi r \Delta r + \pi ( \Delta r ) ^ { 2 } .
$$

This is $C \Delta r$ plus a correction. Dividing both sides by $\Delta r  0$ leaves $d A / d r = C$ :

Finally there is a geometrical reason. The ring unwinds into a thin strip. Its width is $\Delta r$ and its length is close to $C$ : The inside and outside circles have different perimeters, so this is not a true rectangle—but the area is near $C \Delta r$ :

EXAMPLE 4 For a sphere, surface area and volume satisfy $A = d V / d r$ :

What worked for circles will work for spheres. The thin rings become thin shells. A shell goes from radius $r$ to radius $r + \Delta r$ , so its thickness is $\Delta r$ : We want the volume of the shell, but we don’t need it exactly. The surface area is $4 \pi r ^ { 2 }$ , so the volume is about $4 \pi r ^ { 2 } \Delta r$ : That is close enough!

Again we are correct except for $( \Delta r ) ^ { 2 }$ : Infinitesimally speaking $d V = A d r$ :

$$
V = \int _ { 0 } ^ { r } A \ d r = \int _ { 0 } ^ { r } 4 \pi r ^ { 2 } \ d r = { \frac { 4 } { 3 } } \pi r ^ { 3 } .
$$

This is the volume of a sphere. The derivative of $V$ is $A$ , and the shells explain why.   
Main point: Integration is not restricted to rectangles.

EXAMPLE 5 The distance around a square is $4 s$ : Why does the area have $d A / d s = 2 s \mathrm { ? }$

The side is $s$ and the area is $s ^ { 2 }$ : Its derivative $2 s$ goes only half way around the square. I tried to understand that by drawing a figure. Normally this works, but in the figure $d A / d s$ looks like $4 s$ : Something is wrong. The bell is ringing so I leave this as an exercise.

EXAMPLE 6 Find the area under $v ( x ) = \cos ^ { - 1 } x$ from $x = 0$ to $x = 1$ :

That is a conventional problem, but we have no antiderivative for $\cos ^ { - 1 } x$ : We could look harder, and find one. However there is another solution—unconventional but correct. The region can be filled with horizontal rectangles (not vertical rectangles). Figure 5.17b shows a typical strip of length $x = \cos v$ (the curve has $v = \cos ^ { - 1 } \bar { x }$ ). As the thickness $\Delta v$ approaches zero, the total area becomes $\int x d v$ : We are integrating upward, so the limits are on $v$ not on $x$ :

$$
\begin{array} { r } { \mathrm { a r e a } = \int _ { 0 } ^ { \pi / 2 } \cos v d v = \sin v \bigg ] _ { 0 } ^ { \pi / 2 } = 1 . } \end{array}
$$

The exercises ask you to set up other integrals—not always with rectangles.   
Archimedes used triangles instead of rings to find the area of a circle.