# 13.5 The Chain Rule

Calculus goes back and forth between solving problems and getting ready for harder problems. The first is “application,” the second looks like “theory.” If we minimize $f$ to save time or money or energy, that is an application. If we don’t take derivatives to find the minimum—maybe because $f$ is a function of other functions, and we don’t have a chain rule—then it is time for more theory. The chain rule is a fundamental working tool, because $f ( g ( x ) )$ appears all the time in applications. So do $f ( g ( x , y ) )$ and $f ( x ( t ) , y ( t ) )$ and worse. We have to know their derivatives. Otherwise calculus can’t continue with the applicationBs.

You may instinctively say: Don’t bother with the theory, jBust t eBach me the formulas. That is not possible. You now regard the derivative of sin $2 x$ as a trivial problem, unworthy of an answer. That was not always so. Before the chain rule, the slopes of sin $2 x$ and sin $x ^ { 2 }$ and $\sin ^ { 2 } x ^ { 2 }$ were hard to compute from $\Delta f / \Delta x$ : We are now at the same point for $f ( x , y )$ : We know the meaning of $\partial f / \partial x$ ; but if $f = r$ tan $\theta$ and $x = r$ cos $\theta$ and $y = r \sin \theta$ ; we need a way to compute $\partial f / \partial x$ : A liBttle  tBheory is unavoidable, if the problem-solving part of calculus is to keep going.

To repeat: The chain rule applies to a function of a function. In one variable that was $f ( g ( x ) )$ : With two variables there are more possibilities:

$$
{ \begin{array} { r l r l } { { 1 . ~ f ( z ) } } & { { \mathrm { w i t h ~ } } z = g ( x , y ) } & & { \operatorname { F i n d } \ \partial { f / } \partial { x } { \mathrm { ~ a n d ~ } } \partial { f / } \partial { y } } \\ { { 2 . ~ f ( x , y ) } } & { { \mathrm { w i t h ~ } } x = x ( t ) , y = y ( t ) } & & { \operatorname { F i n d } \ d { f / } d t } \\ { { 3 . ~ f ( x , y ) } } & { { \mathrm { w i t h ~ } } x = x ( t , u ) , y = y ( t , u ) } & & { \operatorname { F i n d } \ \partial { f / } \partial { t } { \mathrm { ~ a n d ~ } } \partial { f / } \partial { u } } \end{array} }
$$

All derivatives are assumed continuous. More exactly, the input derivatives like $\partial g / \partial x$ and $d x / d t$ and $\partial x / \partial u$ are continuous. Then the output derivatives like $\partial f / \partial x$ and $d f / d t$ and $\partial f / \partial u$ will be continuous from the chain rule. We avoid points like $r = 0$ in polar coordinates—where $\partial r / \partial x = x / r$ has a division by zero.

A Typical Problem Start with a function of $x$ and $y$ ; for example $x$ times $y$ : Thus $f ( x , y ) = x y$ : Change $x$ to $r$ cos $\theta$ and $y$ to $r$ sin $\theta$ : The function becomes . $( r \cos \theta )$ times $( r \sin \theta )$ : We want its derivatives with respect to $r$ and $\theta$ : First we have to decide on its name.

To be correct, we should not reuse the letter $f .$ The new function can be $F$ :

$$
f ( x , y ) = x y f ( r \cos \theta , r \sin \theta ) = ( r \cos \theta ) ( r \sin \theta ) = F ( r , \theta ) .
$$

Why not call it $f ( r , \theta ) ?$ Be Bcause strictly speaking that is $r$ times $\theta !$ If we follow the rules, then $f ( x , y )$ is $x y$ and $f ( r , \theta )$ should be $r \theta$ : The new function $F$ does the right thing—it multiplies $( r \cos \theta ) ( r \sin \theta )$ : But in many cases, the rules get bent and the letter $F$ is changed back to $f .$ :

This crime has already occurred. The end of the last page ought to say $\partial F / \partial t$ : InsteadBthe prinBterBput $\partial f / \partial t$ : The purpose of the chain rule is to find derivatives in the new variables $t$ and $u$ (or $r$ and $\theta$ ). In our example we want the derivative of $F$ with respect to $r$ : Here is the chain rule:

$$
{ \frac { \partial F } { \partial r } } = { \frac { \partial f } { \partial x } } { \frac { \partial x } { \partial r } } + { \frac { \partial f } { \partial y } } { \frac { \partial y } { \partial r } } = ( y ) ( \cos \theta ) + ( x ) ( \sin \theta ) = 2 r \sin \theta \cos \theta .
$$

I substituted $r \sin \theta$ Band $r \cos \theta$ for $y$ and $x$ :BYoBu immBediaBtely check the answer: $F ( r , \theta ) = r ^ { 2 } \cos \theta \sin \theta$ does lead to ${ \partial F } / { \partial r } = 2 r$ cos $\theta \sin \theta$ : The derivative is correct. The only incorrect thing—but we do it anyway—is to write $f$ instead of $F$ :

Question Wh $\mathrm { a t ~ i s } \frac { \partial f } { \partial \theta } ? \qquad \mathsf { A n s w e r } \quad \mathrm { I t ~ i s } \frac { \partial f } { \partial x } \frac { \partial x } { \partial \theta } + \frac { \partial f } { \partial y } \frac { \partial y } { \partial \theta } .$

# THE DERIVATIVES OF $f ( g ( x , y ) )$

Here $g$ depends on $x$ and $y$ ; and $f$ depends on $g$ : Suppose $x$ moves by $d x$ ; while $y$ stays constant. Then $g$ moves by $d g = ( \partial g / \partial x ) d x$ :When $g$ changes, $f$ also changes: $d f { = } ( d f / d g ) d g$ : Now substitute for $d g$ Bto make thBe chain: $d f = ( d f / d g ) ( \partial g / \partial x ) d x$ : This is the first rule:

EXAMPLE 1 Every $f ( x + c y )$ satisfiesBthe  1B-way wave equation $\partial f / \partial y = c \partial f / \partial x$ :

TheBinside funcBtion is $g = x + c y$ : BThe outsideBfunction can be anBything, $g ^ { 2 }$ or sin $g$ or $e ^ { g }$ : The comBposite function is $( x + c y ) ^ { 2 }$ or $\sin ( x + c y )$ or $e ^ { x + c y }$ : In eacBh separate case we could check that $\partial f / \partial y = c \partial f / \partial x$ : The chain rule produces this equation in all cases at once,Bfrom B $\partial g / \partial x = 1$ and $\partial g / \partial y = c$ :

$$
{ \frac { \hat { \sigma } f } { \hat { \sigma } x } } = { \frac { d f } { d g } } { \frac { \hat { \sigma } g } { \hat { \sigma } x } } = 1 { \frac { d f } { d g } } \quad { \mathrm { a n d } } \quad { \frac { \hat { \sigma } f } { \hat { \sigma } y } } = { \frac { d f } { d g } } { \frac { \hat { \sigma } g } { \hat { \sigma } y } } = c { \frac { d f } { d g } } \quad { \mathrm { s o } } \quad { \frac { \hat { \sigma } f } { \hat { \sigma } y } } = c { \frac { \hat { \sigma } f } { \hat { \sigma } x } } .
$$

This is important: $\partial f / \partial y = c \partial f / \partial x$ is our first example of a partial differential equation. The unknown $f ( x , y )$ has two variables. Two partial derivatives enter the equation.

Up to now we have worked with $d y / d t$ and ordinary differential equations. The independent variable was time or space (and only one dimension in space). For partial differential equations the variables are time and space (possibly several dimensions in space). The great equations of mathematical physics—heat equation, wave equation, Laplace’s equation—are partial differential equations.

Notice how the chain rule applies to $f = \sin x y$ : Its $x$ derivative is $y \cos x y$ : A patient reader would check that $f$ is sin $g$ and $g$ is $x y$ and $f _ { x }$ is $f _ { g } g _ { x }$ : Probably you are not so patient—you know the derivative of sin $x y$ : Therefore we pass quickly to the next chain rule. Its outside function depends on two inside functions, and each of those depends on $t$ : We want $d f / d t$ :

# THE DERIVATIVE OF $f ( x \left( t \right) , y \left( t \right) )$

Before the formBula, hereBis the idea. Suppose $t$ changes by $\Delta t$ : That affects $x$ and $y$ ; they change by $\Delta x$ and $\Delta y$ : There is a domino effect on $f$ ; it changes by $\Delta f .$ : Tracing backwards,

$$
\Delta f \approx \frac { \partial f } { \partial x } \Delta x + \frac { \partial f } { \partial y } \Delta y \quad \mathrm { a n d } \quad \Delta x \approx \frac { d x } { d t } \Delta t \quad \mathrm { a n d } \quad \Delta y \approx \frac { d y } { d t } \Delta t .
$$

Substitute the last two into the first, connecting $\Delta f$ to $\Delta t$ : Then let $\Delta t \to 0$ :

$$
\boxed { 1 3 1 \ C h a i n r u l e f o r \ f ( x ( t ) , y ( t ) ) : \frac { d f } { d t } = \frac { \hat { \sigma } f } { \hat { \sigma } x } \frac { d x } { d t } + \frac { \hat { \sigma } f } { \hat { \sigma } y } \frac { d y } { d t } . }
$$

This is close to the one-variable rule $d z / d x = ( d z / d y ) ( d y / d x )$ : There we could “cancel” $d y$ : (We actually canceled $\Delta y$ in $( \Delta z / \Delta y ) ( \Delta y / \Delta x )$ , and then approached the limit.) Now $\Delta t$ affects $\Delta f$ in two ways, through $x$ and through $y$ : The chain rule has two terms. If we cancel in $( \partial f / \partial x ) ( d x / d t )$ we only get one of the terms!

We mention again that the true name for $f ( x ( t ) , y ( t ) )$ is $F ( t )$ not $f ( t )$ : For $f ( x , y , z )$ the rule has three terms: $f _ { x } x _ { t } + f _ { y } y _ { t } + f _ { z } z _ { t }$ is $f _ { t }$ (or better $d F / d t$ :)

EXAMPLE 2 How quickly does the temperature change when you drive to Florida?

Suppose the Midwest is at $3 0 ^ { \circ } \mathrm { F }$ and Florida is at $8 0 ^ { \circ } \mathrm { F } .$ Going 1000 miles south increases the temperature $f ( x , y )$ by $5 0 ^ { \circ }$ ; or .05 degrees per mile. Driving straight south at 70 miles per hour, the rate of increase is $( . 0 5 ) ( 7 0 ) = 3 . 5 \$ degrees per hour. Note how .degreesB=mile/ timBes .miles=hour/ equals .degrees=hour/. That is the ordinary chain rule $( d f / d x ) ( d x / d t ) = ( d f / d t )$ —there is no $y$ variable going south.

If the road goes southeast, the temperature is $f = 3 0 + . 0 5 x + . 0 1 y$ : Now $x ( t )$ is distance south and $y ( t )$ is distance east. What is $d f / d t$ if the speed is still 70?

$$
{ \frac { d f } { d t } } = { \frac { \partial f } { \partial x } } { \frac { d x } { d t } } + { \frac { \partial f } { \partial y } } { \frac { d y } { d t } } = . 0 5 { \frac { 7 0 } { \sqrt { 2 } } } + . 0 1 { \frac { 7 0 } { \sqrt { 2 } } } \approx 3 { \mathrm { ~ d e g r e e s } } / { \mathrm { h o u r } } .
$$

In reality there is another term. The temperature alBso dependBs directly oBn $t$ ; because of night and day. The factor $\cos ( 2 \pi t / 2 4 )$ has a period of 24 hours, and it brings an extra term into the chain rule:

$$
F o r f ( x , y , t ) t h e c h a i n r u l e i s \ \frac { d f } { d t } = \frac { \partial f } { \partial x } \frac { d x } { d t } + \frac { \partial f } { \partial y } \frac { d y } { d t } + \frac { \partial f } { \partial t } .
$$

This is the total derivative $d f / d t$ ; from all causes. Changes in $x , y , t$ all affect $f .$ The partial derivative $\partial f / \partial t$ is only one part of $d f / d t$ : (Note that $d t / d t = 1 .$ :) If night and day add $1 2 \cos ( 2 \pi t / 2 4 )$ to $f ,$ the extra term is $\partial f / \partial t = - \pi \sin ( 2 \pi t / 2 4 )$ : At nightfall that is $- \pi$ degrees per hour. You have to drive faster than $7 0 \mathrm { m p h }$ to get warm.

# SECOND DERIVATIVES

What is $d ^ { 2 } f / d t ^ { 2 } \}$ We need the derivative of (4), which is painful. It is like acceleration in Chapter 12, with many terms. So start with movement in a straight line.

Suppose $x = x _ { 0 } + t \cos \theta$ and $y = y _ { 0 } + t \sin \theta$ : We are moving at the fixed angle $\theta$ ; with speed 1: The derivatives are $x _ { t } = \cos \theta$ and $y _ { t } = \sin \theta$ and $\cos ^ { 2 } \theta + \sin ^ { 2 } \theta =$ 1: Then $d f / d t$ is immediate from the chain rule:

$$
\begin{array} { r } { f _ { t } = f _ { x } x _ { t } + f _ { y } y _ { t } = f _ { x } \cos { \theta } + f _ { y } \sin { \theta } . } \end{array}
$$

For the second derivative $f _ { t t }$ ; apply this rule to $f _ { t }$ : Then $f _ { t t }$ is

$$
( f _ { t } ) _ { x } \cos \theta + ( f _ { t } ) _ { y } \sin \theta = ( f _ { x x } \cos \theta + f _ { y x } \sin \theta ) \cos \theta + ( f _ { x y } \cos \theta + f _ { y y } \sin \theta ) \sin \theta .
$$

$$
f _ { t t } = f _ { x x } \cos ^ { 2 } \theta + 2 f _ { x y } \cos \theta \sin \theta + f _ { y y } \sin ^ { 2 } \theta .
$$

In polar coordinates change $t$ to $r$ : When we move in the $r$ direction, $\theta$ is fixed. Equation (6) gives $f _ { r r }$ from $f _ { x x } , f _ { x y } , f _ { y y }$ : Second derivatives on curved paths (with new terms from the curving) are saved for the exercises.

EXAMPLE 3 If $f _ { x x } , f _ { x y } , f _ { y y }$ are all continuous and bounded by $M$ ; find a bound on $f _ { t t }$ : This is the second derivative along any line.

Solution Equation (6) gives $\left| f _ { t t } \right| \leqslant M \cos ^ { 2 } \theta + M$ sin $2 \theta + M \sin ^ { 2 } \theta \leqslant 2 M$ : This upper bound $2 M$ was needed in equation 13.3.14, for the error in linear approximation.

# THE DERIVATIVES OF $f ( x \left( t , u \right) , y \left( t , u \right) )$

Suppose there are two inside functions $x$ and $y$ ;B eacBh depBendiBng on $t$ and $u$ : When $t$ moves, $x$ and $y$ both move: $d x = x _ { t } d t$ and $d y = y _ { t } d t$ :BTheBn $d x$ and $d y$ force a change in $f \colon d f = f _ { x } d x + f _ { y } d y$ : The chain rule for $\partial f / \partial t$ is no surprise:

$$
\left| 1 3 1 { \mathrm { C h a i n ~ r u l e ~ f o r ~ } } f ( x ( t , u ) , y ( t , u ) ) : { \frac { \partial f } { \partial t } } = { \frac { \partial f } { \partial x } } { \frac { \partial x } { \partial t } } + { \frac { \partial f } { \partial y } } { \frac { \partial y } { \partial t } } . \right.
$$

This rule has $\partial / \partial t$ instead of $d / d t$ ; because of the extra variable $u$ : The symbols remind us that $u$ is constant. Similarly $t$ is constant while $u$ moves, and there is a second cBhain rulBe foBr $\partial f / \partial u \colon f _ { u } = f _ { x } x _ { u } + f _ { y } y _ { u }$ :

EXAMPLE 4 In polar coordinates find $f _ { \theta }$ and $f _ { \theta \theta }$ : Start from $f ( x , y ) = f ( r \cos \theta , r \sin \theta )$ : The chain rule uses the $\theta$ derivatives of $x$ and $y$ :

$$
{ \frac { \partial f } { \partial \theta } } = { \frac { \partial f } { \partial x } } { \frac { \partial x } { \partial \theta } } + { \frac { \partial f } { \partial y } } { \frac { \partial y } { \partial \theta } } = \left( { \frac { \partial f } { \partial x } } \right) ( - r \sin \theta ) + \left( { \frac { \partial f } { \partial y } } \right) ( r \cos \theta ) .
$$

TBhe seBcond $\theta$ dBerivatBive isBhardeBr, becBause (B8) has four terms that depend on $\theta$ : Apply the chain rule to the first term $\partial f / \partial x$ : It is a function of $x$ and $y$ ; and $x$ and $y$ are functions of $\theta$ :

$$
{ \frac { \hat { \sigma } } { \partial \theta } } \left( { \frac { \partial f } { \partial x } } \right) = { \frac { \hat { \sigma } } { \partial x } } \left( { \frac { \partial f } { \partial x } } \right) { \frac { \partial x } { \partial \theta } } + { \frac { \hat { \sigma } } { \partial y } } \left( { \frac { \partial f } { \partial x } } \right) { \frac { \partial y } { \partial \theta } } = f _ { x x } ( - r \sin \theta ) + f _ { x y } ( r \cos \theta ) .
$$

The $\theta$ derivative of $\partial f / \partial y$ is similar. So apply the product rule to (8):

$$
\begin{array} { c } { { f _ { \theta \theta } = [ f _ { x x } ( - r \sin \theta ) + f _ { x y } ( r \cos \theta ) ] ( - r \sin \theta ) + f _ { x } ( - r \cos \theta ) \nonumber } } \\ { { + [ f _ { y x } ( - r \sin \theta ) + f _ { y y } ( r \cos \theta ) ] ( r \cos \theta ) + f _ { y } ( - r \sin \theta ) . } } \end{array}
$$

This formula is not attractive. In mathematics, a messy formula is almost always a signal of asking the wrong question. In fact the combination $f _ { x x } + f _ { y y }$ is much more special than the separate derivatives. We might hope the same for $f _ { r r } + f _ { \theta \theta }$ ; but dimensionally that is impossible—since $r$ is a length and $\theta$ is an angle. The dimensions of $f _ { x x }$ and $f _ { y y }$ are matched by $f _ { r r }$ and $f _ { r } / r$ and $f _ { \theta \theta } / r ^ { 2 }$ : We could even hope that

$$
f _ { x x } + f _ { y y } = f _ { r r } + \frac { 1 } { r } f _ { r } + \frac { 1 } { r ^ { 2 } } f _ { \theta \theta } .
$$

This equation is true. Add $( 5 ) + ( 6 ) + ( 9 )$ with $t$ changed to $r$ : Laplace’s eqBuat iBon $f _ { x x } + f _ { y y } = 0$ is now expressed in polar coordinates: $f _ { r r } + f _ { r } / r + f _ { \theta \theta } / r ^ { 2 } = 0$ :

# A PARADOX

Before leaving polar coordinates there is one more question. It goes back to $\partial r / \partial x$ ; which was practically the first example of partial derivatives:

$$
{ \frac { \partial r } { \partial x } } = { \frac { \partial } { \partial x } } { \sqrt { x ^ { 2 } + y ^ { 2 } } } = x / { \sqrt { x ^ { 2 } + y ^ { 2 } } } = x / r .
$$

My problem is this. We know that $x$ is $r$ cos $\theta$ : So $x / r$ on the right side is cos $\theta$ : On the other hand $r$ is $x / \cos \theta$ : So $\partial r / \partial x$ is also $1 / \cos \theta$ : How can $\partial r / \partial x$ lead to cos $\theta$ one way and $1 / \cos \theta$ the other way?

# 13.5 The Chain Rule

I will admit that this cost me a sleepless night. There must be an explanation— we cannot end with cos $\theta = 1 / \cos \theta$ : This paradox brings a new respect for partial derivatives. May I tell you what I finally noticed? You could cover up the next paragraph and think about the puzzle first.

The key to partial derivatives is to ask: Which variable is held constant? In equation (11), $y$ is constant. But when $r = x / \cos \theta$ gave $\partial r / \partial x = 1 / \cos \theta , \theta$ was constant. In both cases we change $x$ and look at the effect on $r$ . The movement is on a horizontal line (constant $y$ ) or on a radial line (constant $\theta$ ). Figure 13.15 shows the difference.

Remark This example shows that $\partial r / \partial x$ is different from $1 / ( \partial x / \partial r )$ : The neat formula $( \partial r / \partial x ) ( \partial x / \partial r ) = 1$ is not generally true. May I tell you what takes its place? We have toB in cBlude $( \partial r / \partial y ) ( \partial y / \partial r )$ : WBithB two variables $x y$ and two variables $r \theta$ ; we need 2 by 2 matrices! Section 14.4 gives the details:

$$
\left[ \begin{array} { l l } { \partial r / \partial x } & { \partial r / \partial y } \\ { \partial \theta / \partial x } & { \partial \theta / \partial y } \end{array} \right] \left[ \begin{array} { l l } { \partial x / \partial r } & { \partial x / \partial \theta } \\ { \partial y / \partial r } & { \partial y \partial \theta } \end{array} \right] = \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] .
$$

# NON-INDEPENDENT VARIABLES

This paradox points to a serious problem. In computing partial derivatives of $f ( x , y , z )$ ; we assumed that $x , y , z$ were independent. Up to now, $x$ could move while $y$ and $z$ wer Be fix eBd. In physics and chemistry and economics that may not be possible. If there is a relation between $x , y , z$ ; then $x$ can’t move by itself.

BEX ABMPLE 5 The gas law $P V = n R T$ relates pressure to volume and temperature. $P , V , T$ are not independent. What is the meaning of ${ \partial V } / { \partial P ? }$ Does it equal $1 / ( \partial P / \partial V )$ ?

Those questions have no answers, until we say what is held constant. In the paradox, $\partial r / \partial x$ had one meaning for fixed $y$ aBnd  aBnother meaning for fixed $\theta$ : To indicate Bwha tBis held constant, use an extra subscript (not denoting a derivative):

$$
( \partial r / \partial x ) _ { y } = \cos \theta \qquad ( \partial r / \partial x ) _ { \theta } = 1 / \cos \theta .
$$

$( \partial f / \partial P ) _ { V }$ has constant volume and $( \partial f / \partial P ) _ { T }$ has constant temperature. The usual $\partial f / \partial P$ has both $V$ and $T$ constant. But then the gas law won’t let us change $P$ :

EXAMPLE 6 Let $f = 3 x + 2 y + z$ : Compute $\partial f / \partial x$ on the plane $z = 4 x + y$ :

# 13 Partial Derivatives

Solution 1 Think of $x$ and $y$ as independent. Replace $z$ by $4 x + y$ :

$$
f = 3 x + 2 y + ( 4 x + y ) \quad \mathrm { s o } \quad ( \partial f / \partial x ) _ { y } = 7 .
$$

Solution 2 Keep $x$ and $y$ independent. Deal with $z$ by the chain rule:

$$
(  { \hat { \sigma } } f /  { \hat { \sigma } } x ) _ { y } =  { \hat { \sigma } } f /  { \hat { \sigma } } x + (  { \hat { \sigma } } f /  { \hat { \sigma } } z ) (  { \hat { \sigma } } z /  { \hat { \sigma } } x ) = 3 + ( 1 ) ( 4 ) = 7 .
$$

SoBlutio Bn 3 (different) Make $x$ and $z$ independent. Then $y = z - 4 x$ :

$$
( \partial f / \partial x ) _ { z } = \partial f / \partial x + ( \partial f / \partial y ) ( \partial y / \partial x ) = 3 + ( 2 ) ( - 4 ) = - 5 .
$$

WBitho But a subscript, $\partial f / \partial x$ means: Take the $x$ derivative the usual way. The answer is $\partial f / \partial x = 3$ ; when $y$ and $z$ don’t move. But on the plane $z = 4 x + y$ ; one of them must move! 3 is only part of the total answer, which is $( \partial f / \partial x ) _ { y } = 7$ or $( \partial f / \partial x ) _ { z } =$ $- 5$ :

Here is the geometrical meaning. We are on the plane $z = 4 x + y$ : The derivative $( \partial ^ { } f / \partial x ) _ { y }$ moves $x$ but not $y$ : To stay on the plane, $d z$ is $4 d x$ : The change in $f =$ $3 x + 2 y + z$ is $d f = 3 d x + 0 + d z = 7 d x$ :

EXA BMP LBE 7 OnBthe  wBorld l iBne $x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = t ^ { 2 }$ find $( \hat { o } f / \hat { o } y ) _ { x , z }$ for $f = x y z t$ :

The subscripts $x , z$ mean that $x$ and $z$ are fixed. The chain Brule  Bskips $\partial f / \partial x$ and $\partial f / \partial z$ :

$$
( \partial f / \partial y ) _ { x , z } = \partial f / \partial y + ( \partial f / \partial t ) ( \partial t / \partial y ) = x z t + ( x y z ) ( y / t ) . W h y y / t \uparrow
$$

EXAMPLE 8 From the law $P V = T$ ; compute the product $( \partial P / \partial V ) _ { T } ( \partial V / \partial T ) _ { P } ( \partial T / \partial P ) _ { V } .$

Any intelligentperson cancels $\partial V$ ’s, $\partial T$ ’s, and $\partial P$ ’s to get 1: The right answer is $^ { - 1 }$ :

$$
( \partial P / \partial V ) _ { T } = - T / V ^ { 2 } \qquad ( \partial V / \partial T ) _ { P } = 1 / P \qquad ( \partial T / \partial P ) _ { V } = V .
$$

The product is $- T / P V .$ This is $- 1 n o t + 1 !$ The chain rule is tricky (Problem 42).

EXAMPLE 9 Implicit differentiation was used in Chapter 4. The chain rule explains it:

$$
( x , y ) = 0 t h e n ~ F _ { x } + F _ { y } y _ { x } = 0 s o ~ d y / d x = - F _ { x } / F _ { y } .
$$