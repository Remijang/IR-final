You remember that the derivative of $f ( x ) g ( x )$ is not $( d f / d x ) ( d g / d x )$ : The derivative of sin $x$ times $x ^ { 2 }$ is not cos $x$ times $2 x$ : The product rule gave two terms, not one term. But there is another way of combining the sine function $f$ and the squaring function $g$ into a single function. The derivative of that new function does involve the cosine times $2 x$ (but with a certain twist). We will first explain the new function, and then find the “chain rule” for its derivative.

May I say here that the chain rule is important. It is easy to learn, and you will use it often. I see it as the third basic way to find derivatives of new functions from derivatives of old functions. (So far the old functions are $x ^ { n }$ , sin $x$ , and cos $x$ : Still ahead are $e ^ { x }$ and $\log x .$ ) When $f$ and $g$ are added and multiplied, derivatives come from the sum rule and product rule. This section combines $f$ and $g$ in a third way.

The new function is $\sin ( x ^ { 2 } )$ —the sine of $x ^ { 2 }$ . It is created out of the two original functions: if $x = 3$ then $\scriptstyle x ^ { 2 } = 9$ and $\sin ( x ^ { 2 } ) = \sin 9$ : There is a “chain” of functions, combining sin $x$ and $x ^ { 2 }$ into the composite function $\sin ( x ^ { 2 } )$ : You start with $x$ , then find $g ( x )$ , then find $f ( g ( x ) )$ :

The squaring function gives $y = x ^ { 2 } .$ : This is $g ( x )$ : The sine function produces $z = \sin y = \sin ( x ^ { 2 } ) .$ : This is $f ( g ( x ) )$ :

The “inside function” $g ( x )$ gives $y$ : This is the input to the “outside function” $f ( y )$ : That is called composition. It starts with $x$ and ends with $z$ : The composite function is sometimes written $f \circ g$ (the circle shows the difference from an ordinary product $f g )$ . More often you will see $f ( g ( x ) )$ :

$$
z ( x ) = f \circ g \left( x \right) = f ( g ( x ) ) .
$$

Other examples are cos $2 x$ and $( 2 x ) ^ { 3 }$ , with $g = 2 x$ : On a calculator you input $x$ , then push the $^ { \ast } g ^ { , \prime }$ button, then push the “ $f ^ { \prime \prime }$ button:

$$
F r o m \textit { x } c o m p u t e \textit { y } = g ( x ) \qquad F r o m \textit { y } c o m p u t e \textit { z } = f ( y ) .
$$

There is not a button for every function! But the squaring function and sine function are on most calculators, and they are used in that order. Figure 4.1a shows how squaring will stretch and squeeze the sine function.

# 4.1 The Chain Rule

That graph of sin $x ^ { 2 }$ is a crazy FM signal (the Frequency is Modulated). The wave goes up and down like sin $x$ , but not at the same places. Changing to sin $g ( x )$ moves the peaks left and right. Compare with a product $g ( x )$ sin $x$ , which is an AM signal (the Amplitude is Modulated).

Remark $f ( g ( x ) )$ is usually different from $g ( f ( x ) )$ : The order of $f$ and $g$ is usually important. For $f ( x ) = \sin { x }$ and $g ( x ) = x ^ { 2 }$ , the chain in the opposite order $g ( f ( x ) )$ gives something different:

First apply the sine function: $y = \sin x$ Then apply the squaring function: $z = ( \sin x ) ^ { 2 }$ :

That result is often written $\sin ^ { 2 } x$ , to save on parentheses. It is never written sin $x ^ { 2 }$ , which is totally different. Compare them in Figure 4.1.

EXAMPLE 1 The composite function $f \circ g$ can be deceptive. If $g ( x ) = x ^ { 3 }$ and $f ( y ) = y ^ { 4 }$ , how does $f ( g ( x ) )$ differ from the ordinary product $f ( x ) g ( x ) \}$ The ordinary product is $x ^ { 7 }$ : The chain starts with $y = x ^ { 3 }$ , and then $z = y ^ { 4 } = x ^ { 1 2 }$ : The composition of x3 and y4 gives f .g.x// D x12:

EXAMPLE 2 In Newton’s method, $F ( x )$ is composed with itself. This is iteration. Every output $x _ { n }$ is fed back as input, to find $x _ { n + 1 } = F ( x _ { n } )$ : The example $\textstyle F ( x ) = { \frac { 1 } { 2 } } x + { \dot { 4 } }$ has $\begin{array} { r } { { \cal { F } } ( F ( x ) ) = \frac { 1 } { 2 } \big ( \frac { 1 } { 2 } x + 4 \big ) + 4 } \end{array}$ : That produces $\begin{array} { r } { z = \frac { 1 } { 4 } x + 6 } \end{array}$ :

The derivative of $F ( x )$ is $\frac { 1 } { 2 }$ : The derivative of $z = F ( F ( x ) )$ is $\textstyle { \frac { 1 } { 4 } }$ , which is $\frac { 1 } { 2 }$ times $\frac { 1 } { 2 }$ : We multiply derivatives. This is a special case of the chain rule.

An extremely special case is $f ( x ) = x$ and $g ( x ) = x$ : The ordinary product is $x ^ { 2 }$ : The chain $f ( g ( x ) )$ produces only $x$ !?The output?from the “identity function” is $g ( x ) = x . \dagger$ When the second identity function operates on $x$ it produces $x$ again. The derivative is 1 times 1: I can give more composite functions in a table:

$$
{ \begin{array} { r l } { { \underline { { y = g ( x ) } } } } & { { \underline { { z = f ( y ) } } } } \\ { { x ^ { 2 } - 1 } } & { { \sqrt { y } } } \end{array} } { \begin{array} { l } { { \underline { { z = f ( g ( x ) ) } } } } \\ { { \sqrt { x ^ { 2 } - 1 } } } \end{array} }
$$

A calculator has no button for the identity function. It wouldn’t do anything.

The last one adds 5 to get $y$ : Then it subtracts 5 to reach $z$ : So $z = x$ : Here output equals input: $f ( g ( x ) ) = x$ : These “inverse functions” are in Section 4:3: The other examples create new functions $z ( x )$ and we want their derivatives.

# THE DERIVATIVE OF $f ( g ( x ) )$

What is the derivative of $z = \sin x ^ { 2 } ?$ It is the limit of $\Delta z / \Delta x$ : Therefore we look at a nearby point $x + \Delta x$ : That change in $x$ produces a change in $y = x ^ { 2 }$ —which moves to $y + \Delta y = ( x + \Delta x ) ^ { 2 }$ : From this change in $y$ , there is a change in $z = f ( y )$ : It is a “domino effect,” in which each changed input yields a changed output: $\Delta x$ produces y produces $\Delta z$ : We have to connect the final $\Delta z$ to the original $\Delta x$ :

The key is to write $\Delta z / \Delta x$ as $\Delta z / \Delta y$ times $\Delta y / \Delta x$ . Then let $\Delta x$ approach zero. In the limit, $d z / d x$ is given by the “chain rule”:

$$
{ \frac { \Delta z } { \Delta x } } = { \frac { \Delta z } { \Delta y } } { \frac { \Delta y } { \Delta x } } { \mathit { b e c o m e s t h e \ c h a i n \ r u l e \ } } { \frac { d z } { d x } } = { \frac { d z } { d y } } { \frac { d y } { d x } } .
$$

As $\Delta x$ goes to zero, the ratio $\Delta y / \Delta x$ approaches $d y / d x$ : Therefore $\Delta y$ must be going to zero, and $\Delta z / \Delta y$ approaches $d z / d y$ : The limit of a product is the product of the separate limits (end of quick proof). We multiply derivatives:

4A Chain Rule Suppose $g ( x )$ has a derivative at $x$ and $f ( y )$ has a derivative at $y = g ( x )$ : Then the derivative of $z = f ( g ( x ) )$ is

$$
{ \frac { d z } { d x } } = { \frac { d z } { d y } } { \frac { d y } { d x } } = f ^ { \prime } ( g ( x ) ) g ^ { \prime } ( x ) .
$$

The slope at $x$ is $d f / d y$ (at $y$ ) times $d g / d x$ (at $x$ ).

Caution The chain rule does not say that the derivative of sin $x ^ { 2 }$ is $( \cos x ) ( 2 x )$ : True, cos $y$ is the derivative of sin $y$ : The point is that cos $y$ must be evaluated at $y$ (not at $x$ ). We do not want $d f / d x$ at $x$ , we want $d f / d y$ at $y = x ^ { 2 }$ :

$$
T h e d e r i \nu a t i \nu e o f \sin x ^ { 2 } i s ( \cos x ^ { 2 } ) t i m e s ( 2 x ) .
$$

EXAMPLE 3 If $z = ( \sin x ) ^ { 2 }$ then $d z / d x = ( 2 \sin x ) ( \cos x )$ : Here $y = \sin x$ is inside.

In this order, $z = y ^ { 2 }$ leads to $d z / d y = 2 y$ : It does not lead to $2 x$ : The inside function sin $x$ produces $d y / d x = \cos x$ : The answer is $2 y \cos x$ : We have not yet found the function whose derivative is $2 x$ cos $x$ :

EXAMPLE 4 The derivative of $z = \sin 3 x$ is ${ \frac { d z } { d x } } = { \frac { d z } { d y } } { \frac { d y } { d x } } = 3 \cos 3 x .$

# 4.1 The Chain Rule

The outside function is $z = \sin { y }$ : The inside function is $y = 3 x$ : Then $d z / d y =$ cos $y$ —this is cos $3 x$ , not cos $x$ : Remember the other factor $d y / d x = 3$ :

I can explain that factor 3; especially if $x$ is switched to $t$ : The distance is $z = \sin 3 t$ : That oscillate s like sin $t$ except three times as fast. The speeded-up function sin $3 t$ completes a wave at time $2 \pi / 3$ (instead of $2 \pi$ ). Naturally the velocity contains the e xtra factor 3 from the chain rule.

EXAMPLE 5 Let $z = f ( y ) = y ^ { n }$ : Find the derivative of $f ( g ( x ) ) = [ g ( x ) ] ^ { n }$

In this case $d z / d y$ is $n y ^ { n - 1 }$ : The chain rule multipliesby $d y / d x$

$$
{ \frac { d z } { d x } } = n y ^ { n - 1 } { \frac { d y } { d x } } \qquad { \mathrm { o r } } \qquad { \frac { d } { d x } } [ g ( x ) ] ^ { n } = n [ g ( x ) ] ^ { n - 1 } { \frac { d g } { d x } } .
$$

This is the power rule! It was already discovered in Section 2:5: Square roots (when $n = 1 / 2 )$ are frequent and important. Suppose $y = x ^ { 2 } - 1$ :

$$
{ \frac { d } { d x } } { \sqrt { x ^ { 2 } - 1 } } = { \frac { 1 } { 2 } } ( x ^ { 2 } - 1 ) ^ { - 1 / 2 } ( 2 x ) = { \frac { x } { \sqrt { x ^ { 2 } - 1 } } } .
$$

Question A Buick uses $1 / 2 0$ of a gallon of gas per mile. You drive at 60 miles per hour. How many gallons per hour?

Answer $( G a l l o n s / h o u r ) = ( g a l l o n s / m i l e ) ( m i l e s / h o u r )$ : The chain rule is $( d y / d t ) = ( d y / d x ) ( d x / d t )$ : The answer is $( 1 / 2 0 ) ( 6 0 ) = 3$ gallons=hour:

Proof of the chain rule The discussion above was correctly based on

$$
\frac { \Delta z } { \Delta x } = \frac { \Delta z } { \Delta y } \frac { \Delta y } { \Delta x } \qquad \mathrm { a n d } \qquad \frac { d z } { d x } = \frac { d z } { d y } \frac { d y } { d x } .
$$

It was here, over the chain rule, that the “battle of notation” was won by Leibniz. His notation practically 1tells you what to do: Take t1he limit o1f each term. (I have to mention that when $\Delta x$ is approaching zero, it is theoretically possible that $\Delta y$ might hit zero. If that happens, $\Delta z / \Delta y$ beco1mes $0 / 0$ : We have to assign it the correct meaning, which is $d z / d y$ :) As $\Delta x \to 0$ ,

$$
{ \frac { \Delta y } { \Delta x } } \to g ^ { \prime } ( x ) \qquad { \mathrm { a n d } } \qquad { \frac { \Delta z } { \Delta y } } \to f ^ { \prime } ( y ) = f ^ { \prime } ( g ( x ) ) .
$$

Then $\Delta z / \Delta x$ approaches $f ^ { \prime } ( y )$ times $g ^ { \prime } ( x )$ , which is the chain rule $( d z / d y ) ( d y / d x )$ : In the table below, the derivative of $( \sin x ) ^ { 3 }$ is $3 ( \sin x ) ^ { 2 } \cos x$ : That extra factor cos $x$ is easy to forget. It is even easier to forget the $^ { - 1 }$ in the last example.

$$
\begin{array} { l l l } { { z = ( x ^ { 3 } + 1 ) ^ { 5 } } } & { { d z / d x = 5 ( x ^ { 3 } + 1 ) ^ { 4 } } } & { { \mathrm { t i m e s ~ } 3 x ^ { 2 } } } \\ { { z = ( \sin x ) ^ { 3 } } } & { { d z / d x = 3 \sin ^ { 2 } x } } & { { \mathrm { t i m e s ~ } \cos x } } \\ { { z = ( 1 - x ) ^ { 2 } } } & { { d z / d x = 2 ( 1 - x ) } } & { { \mathrm { t i m e s ~ } - 1 } } \end{array}
$$

Important All kinds of letters are used for the chain rule. We named the output $z$ : Very often it is called $y$ , and the inside function is called $u$ :

$$
T h e \ d e r i \nu a t i \nu e \ o f \ y = \sin u ( x ) \ i s \ { \frac { d y } { d x } } = \cos u { \frac { d u } { d x } } .
$$

Examples with $d u / d x$ are extremely common. I have to ask you to accept whatever letters may come. What never changes is the key idea—derivative of outside function times derivative of inside function.

# 4 Derivatives by the Chain Rule

EXAMPLE 6 The chain rule is barely needed for $\sin ( x - 1 )$ : Strictly speaking the inside function is $u = x - 1$ : Then $d u / d x$ is just 1 (not 1). If $y = \sin ( x - 1 )$ then $d y / d x = \cos ( x - 1 )$ : The graph is shifted and the slope shifts too.

Notice especially: The cosine is computed at $x - 1$ and not at the unshifted $x$ :

# REC?OGNIZING f.?y/ AND $g ( x )$

A big part of the chain rule is recognizing the chain. The table started with $( x ^ { 3 } + 1 ) ^ { 5 }$ : You look at it for a second. Then you see it as $u ^ { 5 }$ : The inside function is $u = x ^ { 3 } + 1$ : With practice this decomposition (the opposite of composition) gets easy:

$$
\cos ( 2 x + 1 ) { \mathrm { ~ i s ~ } } \cos u \qquad { \sqrt { 1 + \sin t } } { \mathrm { ~ i s ~ } } { \sqrt { u } } \qquad x \sin x { \mathrm { ~ i s ~ } } \dots ( { \mathrm { p r o d u c t ~ r u l e ! } } )
$$

In calculations, the careful way is to write down all the functions:

$$
z = \cos u \quad u = 2 x + 1 \quad d z / d x = ( - \sin u ) ( 2 ) = - 2 \sin ( 2 x + 1 ) .
$$

The quick way is to keep in your mind “the derivative of what’s inside.” The slope of $\cos ( 2 x + 1 )$ is $- \sin ( 2 x + 1 )$ , times 2 from the chain rule. The derivative of $2 x + 1$ is remembered—with?out $z$ or $u$ or $f$ ?or $g$ :

EXAMPLE 7 sin $\sqrt { 1 - x }$ is a chain of $z = \sin { y }$ ; $y = \sqrt { u } , u = 1 - x$ (three functions). With that triple chain you will have the hang of the chain rule:

$$
\mathrm { T h e ~ d e r i v a t i v e ~ o f ~ } \sin \sqrt { 1 - x } \mathrm { ~ i s ~ } ( \cos \sqrt { 1 - x } ) \left( \frac { 1 } { 2 \sqrt { 1 - x } } \right) ( - 1 ) .
$$

This is $( d z / d y ) ( d y / d u ) ( d u / d x )$ : Evaluate them at the right places $y , u , x$ :

Finally there is the question of second derivatives. The chain rule gives $d z / d x$ as a product, so $d ^ { 2 } z / d x ^ { \bar { 2 } }$ needs the product rule:

$$
\frac { d z } { d x } = \frac { d z } { d y } \frac { d y } { d x } \frac { d z } { d x } = \frac { d ^ { 2 } z } { d x ^ { 2 } } = \frac { d z } { d y } \frac { d ^ { 2 } y } { d x ^ { 2 } } + \frac { d } { d x } \left( \frac { d z } { d y } \right) \frac { d y } { d x } .
$$

That last term needs the chain rule again. It becomes $d ^ { 2 } z / d y ^ { 2 }$ times $( d y / d x ) ^ { 2 }$ :

EXAMPLE 8 The derivative of sin $x ^ { 2 }$ is $2 x \cos x ^ { 2 }$ : Then the product rule gives $d ^ { 2 } z / d x ^ { 2 } = 2 \cos x ^ { 2 } - 4 x ^ { 2 } \sin x ^ { 2 }$ : In this case $y ^ { \prime \prime } { = } 2$ and $( y ^ { \prime } ) ^ { 2 } = 4 x ^ { 2 }$ :