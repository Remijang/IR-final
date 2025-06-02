# 2.7 Continuous Functions

This will be a brief section. It was originally included with limits, but the combination was too long. We are still concerned with the limit of $f ( x )$ as $x \to a$ , but a new number is involved. That number is $f ( a )$ , the value of $f$ at $x = a$ . For a “limit,” $x$ approached $a$ but never reached it—so $f ( a )$ was ignored. For a “continuous function,” this final number $f ( a )$ must be right.

May I summarize the usual (good) situation as $x$ approaches $a$ ?

1. The nu $\begin{array} { r l } & { \mathrm { ~ \ m b e r ~ } f ( a ) \mathrm { ~ e x i s t s ~ \quad } ( f \mathrm { ~ i s ~ d e f n e d ~ a t ~ } a ) } \\ & { \mathrm { ~ \ n i t ~ o f ~ } f ( x ) \mathrm { ~ e x i s t s ~ \quad } \mathrm { ( i t ~ w a s ~ c a l l e d ~ } L ) } \\ & { \mathrm { ~ \ n i t ~ } L \mathrm { ~ e q u a l s ~ } f ( a ) \quad ( f ( a ) \mathrm { ~ i s ~ t h e ~ r i g h t ~ v a l u e ) } } \end{array}$   
2. The li   
3. The li

In such a case, $f ( x )$ is continuous at $x = a$ : These requirements are often written in a single line: $f ( x ) \to f ( a )$ as $x \to a$ : By way of contrast, start with four functions that are not continuous at $x = 0$ :

In Figure 2.20, the first function would be continuous if it had $f ( 0 ) = 0$ : But it has $f ( 0 ) = 1$ : After changing $f ( 0 )$ toÑthe right value, the problem is gone. The discontinuity is removable. Examples 2; 3; 4 are mÑore important and more serious. There is no “correct” value for $f ( 0 )$ :

2. $f ( x ) =$ step function (jump from 0 to 1 at $x = 0$ )   
3. $f ( x ) = 1 / x ^ { 2 }$ (infinite limit as $x \to 0$ )   
4. $f ( x ) = \sin ( 1 / x )$ (infinite oscillation as $x \to 0$ ).

The graphs show how the limit fails to exist. The step function has a jump discontinuity. It has one-sided limits, from the left and right. It does not have an ordinary (two-sided) limit. The limit from the left $( x \to 0 ^ { - }$ ) is 0: The limit from the right $( x \to 0 ^ { + }$ ) is 1: Another step function is $x / | x |$ , which jumps from $^ { - 1 }$ to 1:

In the graph of $1 / x ^ { 2 }$ , the only reasonable limit is $L = + \infty$ : I cannot go on record as saying that this limit eÑxists. Officially, it doesn’t—but wÑe often write it anyway: $1 / x ^ { 2 }  \infty$ as $x \to 0$ : This means that $1 / x ^ { 2 }$ goes (and stays) above every $L$ as $x \to 0$ :

In the same unofficial way we write one-sided limits for $f ( x ) = 1 / x$ :

$$
{ \mathrm { F r o m ~ t h e ~ l e f t , ~ } } \operatorname* { l i m } _ { x \to 0 ^ { - } } { \frac { 1 } { x } } = - \infty . \quad { \mathrm { F r o m ~ t h e ~ r i g h t , ~ } } \operatorname* { l i m } _ { x \to 0 ^ { + } } { \frac { 1 } { x } } = + \infty .
$$

Remark $1 / x$ has a “pole” at $x = 0$ : So has $1 / x ^ { 2 }$ (a double pole). The function $1 / ( x ^ { 2 } - x )$ has poles at $x = 0$ and $x = 1$ : In each case the denominator goes to zero and the function goes to $+ \infty$ or $- \infty$ : Similarly $1 / \sin x$ has a pole at every multiple of $\pi$ (where sin $x$ is zero). Except for $1 / x ^ { 2 }$ these poles are “simple”—the functions are completely smooth at $x = 0$ when we multiply them by $x$ :



$1 / x ^ { 2 }$ has a double pole, since it needs multiplication by $x ^ { 2 }$ (not just $x$ ). A ratio of polynomials $P ( x ) / Q ( x )$ has poles where $Q = 0$ , provided any common factors like $( x + 1 ) / ( x + 1 )$ are removed first.

Jumps and poles are the most basic discontinuities, but others can occur. The fourth graph shows that $\sin ( 1 / x )$ has no limit as $x \to 0$ : This function does not blow up; the sine never exceeds 1: At $\begin{array} { r } { x = \frac { 1 } { 3 } } \end{array}$ and $\textstyle { \frac { 1 } { 4 } }$ and $\scriptstyle { \frac { 1 } { 1 0 0 0 } }$ it equals sin 3 and sin 4 and sin 1000: Those numbers are positive and negative and ( ? ). As $x$ gets small and $1 / x$ gets large, the sine oscillates faster and faster. Its graph won’t stay in a smallÑbox of heightÑ $\varepsilon$ , no matter how narrow the box.

# CONTINUOUS FUNCTIONS

DEFINITION $f$ is “continuous at $x = a ^ { , , }$ if $f ( a )$ is defined and $f ( x ) \to f ( a )$ as $x \to a$ : If $f$ is continuous at every point where it is defined, it is a continuous function.

Objection The definition makes $f ( x ) = 1 / x$ a continuous function! It is not defined at $x = 0$ , so its continuity can’t fail. The logic requires us to accept this, but we don’t have to like it. Certainly there is no $f ( 0 )$ that would make $1 / x$ continuous at $x = 0$ :

It is amazing but true that the definition of “continuous function” is still debated (Mathematics Teacher, May 1989). You see the reason—we speak about a discontinuity of $1 / x$ , and at the same time call it a continuous function. The definition misses the difference between $1 / x$ and $( \sin x ) / x$ : The function $f ( x ) = ( \sin x ) / x$ can be made continuous at all $x$ . Just set $f ( 0 ) = 1$ :

We call a function “continuable” if its definition can be extended to all $x$ in a way that makes it continuous. Thus $( \sin x ) / x$ and $\sqrt { x }$ are continuable. The functions $1 / x$ and tan $x$ are not continuable. This suggestion may not end the debate, but I hope it is helpful.

EXAMPLE 1 sin $x$ and cos $x$ and all polynomials $P ( x )$ are continuous functions.

EXAMPLE 2 The absolute value $| x |$ is continuous. Its slope jumps (not continuable).

EXAMPLE 3 Any rational function $P ( x ) / Q ( x )$ is continuous except where $Q = 0$ :

EXAMPLE 4 The function that jumps between 1 at fractions and 0 at non-fractions is discontinuous everywhere. There is a fraction between every pair of non-fractions and vice versa. (Somehow there are many more non-fractions.)

EXAMPLE 5 The function $0 ^ { x ^ { 2 } }$ is zero for every $x$ , except that $0 ^ { 0 }$ is not defined. So define it as zero and this function is continuous. But see the next paragraph where $0 ^ { 0 }$ has to be 1:

We could fill the book with proofs of continuity, but usually the situation is clear. “A function is continuous if you can draw its graph without lifting up your pen.” At a jump, or an infinite limit, or an infinite oscillation, there is no way across the discontinuity except to start again on the other side. The function $x ^ { \prime \prime }$ is continuous for $n > 0$ : It is not continuable for $n < 0$ : The function $x ^ { 0 }$ equals 1 for every $x$ , except that $0 ^ { 0 }$ is not defined. This time continuity requires $0 ^ { 0 } = \bar { 1 }$ :

The interesting examples are the close ones—we have seen two of them:

EXAMPLE 6 ${ \frac { \sin x } { x } } \quad { \mathrm { a n d } } \quad { \frac { 1 - \cos x } { x } } \quad { \mathrm { a r e ~ b o t h ~ c o n t i n u a b l e ~ a t ~ } } x = 0 .$

Those were crucial for the slope of sin $x$ : The first approaches 1 and the second approaches 0: Strictly speaking we must give these functions the correct values (1 and 0) at the limiting point $x = 0$ —which of course we do.

It is important to know what happens when the denominators change to $x ^ { 2 }$ :

$$
{ \frac { \sin x } { x ^ { 2 } } } \quad { \mathrm { b l o w s ~ u p ~ b u t ~ } } { \frac { 1 - \cos x } { x ^ { 2 } } } { \mathrm { ~ h a s ~ t h e ~ l i m i t ~ } } { \frac { 1 } { 2 } } { \mathrm { ~ a t ~ } } x = 0 .
$$

Since $( \sin x ) / x$ approaches 1, dividing by another $x$ gives a function like $1 / x$ : There is a simple pole. It is anexample of $0 / 0$ , in which the zero from $x ^ { 2 }$ is reached more quickly than the zero from sin $x$ : The “race to zero” proÑduces almost all iÑnteresting problems about limits.

For $1 - \cos x$ and $x ^ { 2 }$ the race is almost even. Their ratio is 1 to 2:

$$
{ \frac { 1 - \cos x } { x ^ { 2 } } } = { \frac { 1 - \cos ^ { 2 } x } { x ^ { 2 } ( 1 + \cos x ) } } = { \frac { \sin ^ { 2 } x } { x ^ { 2 } } } \cdot { \frac { 1 } { 1 + \cos x } }  { \frac { 1 } { 1 + 1 } } \quad { \mathrm { a s } } \quad x  0 .
$$

This answer $\frac { 1 } { 2 }$ will be found again (m1ore easily) by “l’Hôpital’s rule.” Here I emphasize not the answer but the problem. A central question of differential calculus is to know how fast the limit is approached. The speed of approach is exactly the information in the derivative.

These three examples are all continuous at $x = 0$ : The race is controlled by the slope—because $f ( x ) - f ( 0 )$ i8s neaØrly $f ^ { \prime } ( 0 )$ times $x$ :

derivative of sin $x$ is 1 $$ sin $x$ decreases like $x$ derivative of $\sin ^ { 2 } x$ is 0 $$ $\sin ^ { 2 } x$ decreases faster than $x$ derivative o|f $x ^ { 1 / 3 }$ is $\begin{array} { r l r } { \infty } & { { }  } & { x ^ { 1 / 3 } } \end{array}$ x1=3 decreases more slowly than x:

# DIFFERENTIABLE FUNCTIONS

The absolute value $| x |$ is continuous at $x = 0$ but has no derivative. The same is true for $x ^ { 1 / 3 }$ : Asking for a derivative is more than askÑing for continuÑity. The reason is fundamental, and carries us back to the key definitions:

$C o n t i n u o u s { \mathrm { ~ a t ~ x : ~ } } f ( x + \Delta x ) - f ( x ) { \longrightarrow } 0 { \mathrm { ~ a s ~ } } \Delta x {  } 0$ $D e r i \nu a t i \nu e { \mathrm { ~ a t ~ x : ~ } } \quad { \xrightarrow { f ( x + \Delta x ) - f ( x ) } } f ^ { \prime } ( x ) { \mathrm { ~ a s ~ } } \Delta x \to 0 .$

# 2 Derivatives

In the first case, $\Delta f$ goes to zero (maybe slowly). In the second case, $\Delta f$ goes to zero as fast as $\Delta x$ (because $\Delta f / \Delta x$ has a limit). That requirement is stronger:

2I AtÑa point where $f ( x )$ has a derivative, the function must be continuous.   
But $f ( x )$ can be continuous with no derivative.

Proof The limit of $\Delta f = ( \Delta x ) ( \Delta f / \Delta x )$ is $( 0 ) ( d f / d x ) = 0$ : So $f ( x + \Delta x ) -$ $f ( x )  0$ :

The continuous function $x ^ { 1 / 3 }$ has no derivative at $x = 0$ , because ${ \frac { 1 } { 3 } } x ^ { - 2 / 3 }$ blows up. The absolute value $\left| x \right|$ has no derivative because its slope jumps. The remarkable function $\textstyle { \frac { 1 } { 2 } } \cos 3 x + { \frac { 1 } { 4 } } \cos 9 x + \cdots$ is continuous at all points and has a derivative at no points. You can draw its graph without lifting your pen (but not easily—it turns at every point). To most people, it belongs with space-filling curves and unmeasurable areas—in a box of curiosities. Fractals used to go into the same box! They are beauÑtif8ul shapesÑ, with boundaries that have no tangents. The theory of fractals is very alive, for good mathematical reasons, and we touch on it in Section 3:7:

I hope you have a clear idea of these basic definitions of calculus:

1 Limit . $\textstyle n \to \infty$ or $x \to a$ / 2 Continuity (at $x = a$ ) 3 Derivative (at $x = a$ ).

Those go back to $\varepsilon$ and $\delta$ , but it is seldom necessary to follow them so far. In the same way that economics describes many transactions, or history describes many events, a function comes from many values $f ( x )$ : A few points may be special, like market crashes or wars or discontinuities. At other points $d f / d x$ is the best guide to the function.

This chapter ends with two essential facts about a continuous function on a closed interval. The interval is $a \leqslant x \leqslant b$ , written simply as $[ a , b ] . \dagger$ At the endpoints $a$ and $b$ we require $f ( x )$ to approach $f ( a )$ and $f ( b )$ :

Extreme Value Property A continuous function on the finite interval $[ a , b ]$ has a maximum value $M$ and a minimum value $m$ : There are points $x _ { \mathrm { m a x } }$ and $x _ { \mathrm { m i n } }$ in $[ a , b ]$ where it reaches those values:

$$
f ( x _ { \mathrm { m a x } } ) = M \geqslant f ( x ) \geqslant f ( x _ { \mathrm { m i n } } ) = m \mathrm { ~ f o r ~ a l l ~ } x \mathrm { ~ i n ~ } [ a , b ] .
$$

Int erm¤ediate Value Property If the number $F$ is between $f ( a )$ and $f ( b )$ , there is a point $c$ between $a$ and $b$ where $f ( c ) = F$ : Thus if $F$ is between the minimum $m$ and the maximum $M$ , there is a point $c$ between $x _ { \mathrm { m i n } }$ and $x _ { \mathrm { m a x } }$ where $f ( c ) = F$ :

Examples show why we require closed intervals and continuous functions. For $0 < x \leqslant 1$ the function $f ( x ) = x$ never reaches its minimum (zero). If we close the interval by defining $f ( 0 ) = 3$ (discontinu¥ous) the minimum is still not reached. Because of the jump, the intermediate value $F = 2$ is also not reached. The idea of continuity was inescapable, after Cauchy defined the idea of a limit.