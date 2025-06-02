# 4.3 Inverse Functions and Their Derivatives

There is a remarkable special case of the chain rule. It occurs when $f ( y )$ and $g ( x )$ are “inverse functions.” That idea is expressed by a very short and powerful equation: $f ( g ( x ) ) = x$ : Here is what that means.

Inverse functions: Start with any input, say $x = 5$ : Compute $y = g ( x )$ , say $y = 3$ : Then compute $f ( y )$ , and the answer must be 5. What one function does, the inverse function undoes. If $g ( 5 ) = 3$ then $f ( 3 ) = 5$ : The inverse function $f$ takes the output $y$ back to the input $x$ .

EXAMPLE 1 $g ( x ) = x - 2$ and $f ( y ) = y + 2$ are inverse functions. Starting with $x = 5$ , the function $g$ subtracts 2: That produces $y = 3$ : Then the function $f$ adds 2: That brings back $x = 5$ . To say it directly: The inverse of $y = x - 2$ is $x = y + 2$ .

EXAMPLE 2 $\begin{array} { r } { y = g ( x ) = \frac { 5 } { 9 } ( x - 3 2 ) } \end{array}$ and $\begin{array} { r } { x = f ( y ) = \frac { 9 } { 5 } y + 3 2 } \end{array}$ are inverse functions (for temperature). Here $x$ is degrees Fahrenheit and $y$ is degrees Celsius. From $x = 3 2$ (freezing in Fahrenheit) you find $y = 0$ (freezing in Celsius). The inverse function takes $y = 0$ back to $x = 3 2$ : Figure 4.4 shows how $x = 5 0 ^ { \circ } \mathrm { F }$ matches $y = 1 0 ^ { \circ } \mathrm { C }$ .

Notice that ${ \frac { 5 } { 9 } } ( x - 3 2 )$ subtracts 32 first. The inverse $\frac { 9 } { 5 } y + 3 2$ adds 32 last. In the same way $g$ multiplies last by $\frac { 5 } { 9 }$ while $f$ multiplies first by $\frac { 9 } { 5 }$ :

The inverse function is written $f = g ^ { - 1 }$ and pronounced “ $g$ inverse.” ${ \mathbf { } } _ { I t }$ is not $1 / g ( x )$ :

If the demand $y$ is a function of the price $x$ , then the price is a function of the demand. Those are inverse functions. Their derivatives obey a fundamental rule: $d y / d x$ times $d x / d y$ equals 1. In Example 2, $d y / d x$ is $5 / 9$ and $d x / d y$ is $9 / 5$ :

There is another important point. When $f$ and $g$ are applied in the opposite order, they still come back to the start. First $f$ adds 2, then $g$ subtracts 2: The chain $g ( f ( y ) ) = ( y + 2 ) - 2$ brings back $y . H f$ is the inverse of $g$ then $g$ is the inverse of $f$ . The relation is completely symmetric, and so is the definition:

Inverse function: If $y = g ( x )$ th $e n \ x = g ^ { - 1 } ( y ) . I f x = g ^ { - 1 } ( y ) t h e n \ y = g ( x ) .$

The loop in the figure goes from $x$ to $y$ to $x$ : The composition $g ^ { - 1 } ( g ( x ) )$ i?s the “identity function.” Instead of a new point $z$ it returns to the original $x$ : This will make the chain rule particularly easy—leading to $( d y / d x ) ( d x / d y ) = 1$ :

EXAMPLE 3 $y = g ( x ) = \sqrt { x }$ and $x = f ( y ) = y ^ { 2 }$ are inverse functions.

Starting from $x = 9$ we find $y = 3$ : The inverse gives $3 ^ { 2 } = 9$ : The square of $\sqrt { x }$ is $f ( g ( x ) ) = x$ : In the opposite direction, the square root of $y ^ { 2 }$ is $g ( f ( y ) ) = y$ :

Caution That example does not allow $x$ to be negative. The domain of $g$ —the set of numbers with square roots—is restricted to $x \geqslant 0$ : This matches the range of $g ^ { - 1 }$ : The outputs $y ^ { 2 }$ are nonnegative. With domain of $g = r a n g e$ of $g ^ { - 1 }$ , the equation $x = \hat { ( } \sqrt { x } ) ^ { 2 }$ is possible and true. The nonnegative $x$ goes into $g$ and comes out of $g ^ { - 1 }$ :

In this example $y$ is also nonnegative. You might think we could square anything, but $y$ must come back as the square root of $y ^ { 2 }$ : So $y \geqslant 0$ :

To summarize: The domain of a function matches the range of its inverse. The inputs to $g ^ { - 1 }$ are the outputs from $g$ : The i?nputs to $g$ are the outputs from $g ^ { - 1 }$ :

I $f g ( x ) = y$ then solving that equation for $x$ gives $x = g ^ { - 1 } ( y )$ :

$$
\begin{array} { l l } { { \mathrm { i f } \ y = 3 x - 6 } } & { { \ { \mathrm { t h e n } } \ x = { \frac { 1 } { 3 } } ( y + 6 ) \quad ( { \mathrm { t h i s ~ i s } } g ^ { - 1 } ( y ) ) } } \\ { { \mathrm { i f } \ y = x ^ { 3 } + 1 } } & { { \ { \mathrm { t h e n } } \ x = { \sqrt [ { 3 } ] { y - 1 } } } } \end{array}
$$

In practice that is how $g ^ { - 1 }$ is computed: Solve $g ( x ) = y$ : This is the reason inverses are important. Every time we solve an equation we are computing a value of $g ^ { - 1 }$ :

Not all equations have one solution. Not all functions have inverses. For each $y$ , the equation $g ( x ) = y$ is ¤only allowed to produce one $x$ : That solution is $x = g ^ { - 1 } ( y )$ : If there is a second solution, then $g ^ { - 1 }$ will not be a function—because a function cannot produce two $x$ ’s from the same $y$ :

EXAMPLE 4 There is more than one solution to sin $\begin{array} { r } { x = \frac { 1 } { 2 } } \end{array}$ : Many angles have the same sine. On the interval $0 \leqslant x \leqslant \pi$ , the inverse of $y = \sin x$ is not a function. Figure 4.5 shows how two $x$ ’s give the same $y$ :

Prevent $x$ from passing $\pi / 2$ and the sine has an inverse. Write $x = \sin ^ { - 1 } y$ :

The function $g$ has no inverse if two points $x _ { 1 }$ and $x _ { 2 }$ give $g ( x _ { 1 } ) = g ( x _ { 2 } )$ . Its inverse would have to bring the same $y$ back to $x _ { 1 }$ and $x _ { 2 }$ : No function can do that; $g ^ { - 1 } ( y )$ cannot equal both $x _ { l }$ and $x _ { 2 }$ : There must be only one $x$ for each $y$ :

To be invertible over an interval, $g$ must be steadily increasing or steadily decreasing.

$$
\frac { 1 - \sin ^ { - 1 } y } { 1 + \sin x } + \frac { 1 } { 1 } - \frac { \sin x } { 1 } .
$$

It is time for calculus. Forgive me for this very humble example.

EXAMPLE 5 (ordinary multiplication) The inverse of $y = g ( x ) = 3 x$ is $\begin{array} { r } { x = f ( y ) = \frac { 1 } { 3 } y } \end{array}$ :

This shows with special clarity the rule for derivatives: The slopes $d y / d x = 3$ and $\begin{array} { r } { d x / d y = \frac { 1 } { 3 } } \end{array}$ multiply to give 1: This rule holds for all inverse functions, even if their slopes are not constant. It is a crucial application of the chain rule to the derivative of $f ( g ( x ) ) = x$ :

4C (Derivative of inverse function) From $f ( g ( x ) ) = x$ the chain rule gives $f ^ { \prime } ( g ( x ) ) g ^ { \prime } ( x ) = 1 \ /$ : Writing $y = g ( x )$ and $x = f ( y )$ , this rule looks better:

$$
{ \frac { d x } { d y } } { \frac { d y } { d x } } = 1 \qquad o r \qquad { \frac { d x } { d y } } = { \frac { 1 } { d y / d x } } .
$$

The slope of $x = g ^ { - 1 } ( y )$ times the slope of $y = g ( x )$ equals one.

This is the chain rule with a special feature. Since $f ( g ( x ) ) = x$ , the derivative of both sides is 1: If we know $g ^ { \prime }$ we now know $f ^ { \prime }$ : That rule will be tested on a familiar example. In the next section it leads to totally new derivatives.

EXAMPLE 6 The inverse of $y = x ^ { 3 }$ is $x = y ^ { 1 / 3 }$ : We can find $d x / d y$ two ways:

$$
\mathsf { r e c t l y : } \frac { d x } { d y } = \frac { 1 } { 3 } y ^ { - 2 / 3 } \qquad \mathrm { i n d i r e c t l y : } \frac { d x } { d y } = \frac { 1 } { d y / d x } = \frac { 1 } { 3 x ^ { 2 } } = \frac { 1 } { 3 y ^ { 2 / 3 } } .
$$

The equation $( d x / d y ) ( d y / d x ) = 1$ is not ordinary algebra, but it is true. Those derivatives are limits of fractions. The fractions are $( \Delta x / \Delta y ) ( \Delta y / \Delta x ) = 1$ and we let $\Delta x \to 0$ :

Before going to new functions, I want todraw graphs. Figure 4.6 shows $y = { \sqrt { x } }$ and $y = 3 x$ : What is special is that the same graphs also show the inverse functions. The inverse of $y = { \sqrt { x } }$ is $x = y ^ { 2 }$ : The pair $x = 4 , y = 2$ is the same for both. That is the whole point of inverse functions—if $2 = g ( 4 )$ then $4 = g ^ { - 1 } ( 2 )$ . Notice that the graphs go steadily up.

The only problem is, the graph of $x = g ^ { - 1 } ( y )$ is on its side. To change the slope from 3 to $\frac { \bar { 1 } } { 3 }$ , you would have to turn the figure. After that turn there is another problem—the axes don’t point to the right and up. You also have to look in a mirror! (The typesetter refused to print the letters backward. He thinks it’s crazy but it’s not.) To keep thebook in position, and the typesetter in position, we need a better idea.

The graph of $\begin{array} { r } { x = \frac { 1 } { 3 } y } \end{array}$ comes from turning the picture across the $4 5 ^ { \circ }$ line. The $y$ axis becomes horizontal and $x$ goes upward. The point $( 2 , 6 )$ on the line $y = 3 x$ goes into the point $( 6 , 2 )$ on the line $\begin{array} { r } { \dot { \boldsymbol { x } } = \frac { 1 } { 3 } \boldsymbol { y } } \end{array}$ : The eyes see a reflection across the $4 5 ^ { \circ }$ line (Figure 4.6c). The mathematics sees the same pairs $x$ and $y$ : The special properties of $g$ and $g ^ { - 1 }$ allow us to know two functions—and draw two graphs—at the same time. $\dag$ The graph of $x = g ^ { - 1 } ( y )$ is the mirror image of the graph of $y = g ( x )$ .

# 4.3 Inverse Functions and Their Derivatives

# EXPONENTIALS AND LOGARITHMS

I would like to add two more examples of inverse functions, because they are so important. Both examples involve the exponential and the logarithm. One is made up of linear pieces that imitate $2 ^ { x }$ ; it appeared in Chapter 1: The other is the true function $2 ^ { x }$ , which is not yet defined—and it is not going to be defined here. The functions $b ^ { x }$ and $\log _ { b } y$ are so overwhelmingly important that they deserve and will get a whole chapter of the book (at least). But you have to see the graphs.

The slopes in the linear model are powers of 2: So are the heights $y$ at the start of each piece. The slopes 1; 2; 4; : : : equal the heights 1; 2; 4; : : : at those special points.

The inverse is a discrete model for the logarithm (to base 2). The logarithm of 1 is 0, because $2 ^ { 0 } = 1$ : The logarithm of 2 is 1, because $2 ^ { 1 } = 2$ : The logarithm of $2 ^ { j }$ is the exponent $j$ : Thus the model gives the correct $x = \log _ { 2 } y$ at the breakpoints $y = 1 , 2 , 4 , 8 , \dots$ The slopes are $1 , { \frac { \overline { { 1 } } } { 2 } } , { \frac { 1 } { 4 } } , { \frac { 1 } { 8 } } , \dots$ because $d x / d y = 1 / ( d y / d x )$ :

The model is good, but the real thing is better. The figure on the right shows the true exponential $y = 2 ^ { x }$ : At $x = 0 , 1 , 2 .$ : : : the heights $y$ are the same as before. But now the height at $\begin{array} { r } { x = \frac { 1 } { 2 } } \end{array}$ is the number $2 ^ { 1 / 2 }$ , which is $\sqrt { 2 }$ : The height at $x = . 1 0$ is the tenth root $2 ^ { 1 / 1 0 } = 1 . 0 7$ : : : : The slope at $x = 0$ is no longer 1—it is closer to $\Delta y / \Delta x = . 0 7 / . 1 0$ : The exact slope is a number $c$ (near .7) that we are not yet prepared to reveal.

The special property of $y = 2 ^ { x }$ is that the slope at all points is $c y$ : The slope is proportional to the function. The exponential solves $d y / d x = c y$ :

Now look at the inverse function—the logarithm. Its graph is the mirror image:

$$
\textit { I f y } = 2 ^ { x } \mathit { t h e n } x = \log _ { 2 } y . \mathit { I f } \ 2 ^ { 1 / 1 0 } \approx 1 . 0 7 \mathit { t h e n } \ \log _ { 2 } 1 . 0 7 \approx 1 / 1 0 .
$$

What the exponential does, the logarithm undoes—and vice versa. The logarithm of $2 ^ { x }$ is the exponent $x$ . Since the exponential starts with slope $c$ , the logarithm must start with slope $1 / c$ : Check that numerically. The logarithm of 1:07 is near $1 / 1 0$ : The slope is near . $1 0 / . 0 7$ : The beautiful property is that $d x / d y = 1 / c y$ :

I have to mention that calculus avoids logarithms to base 2: The reason lies in that mysterious number $c$ : It is the “natural logarithm” of 2, which is .693147 : : —and who wants that? Also $1 / . 6 9 3 1 4 7 \ldots$ enters the slope of $\log _ { 2 } y$ : Then $( d x / d y ) ( d y / d x ) = 1$ : The right choice is to use “natural logarithms” throughout. In place of 2, they are based on the special number $e$ :

$$
y = e ^ { x } \ i s \ t h e \ i n v e r s e \ o f \ x = \ln y .
$$

The derivatives of those functions are sensational—they are saved for Chapter 6.   
Together with $x ^ { n }$ and sin $x$ and cos $x$ , they are the backbone of calculus.

Note It is almost possible to go directly to Chapter 6: The inverse functions $x = \sin ^ { - 1 } y$ and $x = \tan ^ { - 1 } y$ can be done quickly. The reason for including integrals first (Chapter 5) is that they solve differential equations with no guesswork:

$$
{ \frac { d y } { d x } } = y \quad { \mathrm { o r } } \quad { \frac { d x } { d y } } = { \frac { 1 } { y } } \quad { \mathrm { l e a d s ~ t o } } \quad \int d x = \int { \frac { d y } { y } } \quad { \mathrm { o r } } \quad x = \ln y + C .
$$

Integrals have applications of all kinds, spread through the rest of the book. But do not lose sight of $2 ^ { x }$ and $e ^ { x }$ : They solve $d y / d x = c y$ —the key to applied calculus.

# THE INVERSE OF A CHAIN $h ( g ( x ) )$

The functions $g ( x ) = x - 2$ and $h ( y ) = 3 y$ were easy to invert. For $g ^ { - 1 }$ we added 2, and for $h ^ { - 1 }$ we divided by 3: Now the question is: If we create the composite function $z = h ( g ( x ) )$ , or $z = 3 ( x - 2 )$ , what is its inverse?

Virtually all known functions are created in this way, from chains of simpler functions. The problem is to invert achain using the inverse of each piece. The answer is one of the fundamental rules of mathematics:

4D The inverse of $z = h ( g ( x ) )$ is a chain of inverses in the opposite order:

$$
x = g ^ { - 1 } ( h ^ { - 1 } ( z ) ) .
$$

$h ^ { - 1 }$ is applied first because $h$ was applied last: $g ^ { - 1 } ( h ^ { - 1 } ( h ( g ( x ) ) ) ) = x$ :

That last equation looks like a mess, but it holds the key. In the middle you see $h ^ { - 1 }$ and $h$ : That part of the chain does nothing! The inverse functions cancel, to leave $g ^ { - 1 } ( g ( x ) )$ : But that is $x$ . The whole chain collapses, when $g ^ { - 1 }$ and $h ^ { - 1 }$ are in the correct order—which is opposite to the order of $h ( g ( x ) )$ :

EXAMPLE 7 $z = h ( g ( x ) ) = 3 ( x - 2 ) { \mathrm { ~ a n d ~ } } x = g ^ { - 1 } ( h ^ { - 1 } ( z ) ) = { \frac { 1 } { 3 } } z + 2 .$

First $h ^ { - 1 }$ divides by 3: Then $g ^ { - 1 }$ adds 2: The inverse of $h \circ g$ is $g ^ { - 1 } \circ h ^ { - 1 }$ : $I t$ can be found directly by solving $z = 3 ( x - 2 )$ . A chain of inverses is like writing in prose—we do it without knowing it.

EXAMPLE 8 Invert $z = { \sqrt { x - 2 } }$ by writing $z ^ { 2 } = x - 2$ and¥then $x = z ^ { 2 } + 2$ :

The inverse adds 2 and takes the square—but not in that order. That would give $( z + 2 ) ^ { 2 }$ , which is wrong. The correct order is $z ^ { 2 } + 2$ :

The domains and ranges are explained by Figure 4.8. We start with $x \geqslant 2$ : Subtracting 2 gives $y \geqslant 0$ : Taking the square root gives $z \geqslant 0$ : Taking the square brings back $y \geqslant 0$ : Adding 2 brings back $x \geqslant 2$ —which is in the original domain of $g$ :

EXAMPLE 9 Inverse matrices $( A B ) ^ { - 1 } = B ^ { - 1 } A ^ { - 1 }$ (this linear algebra is optional).

Suppose a vector $x$ is multiplied by a square matrix $B \colon y = g ( x ) = B x .$ : The inverse function multiplies by the inverse matrix: $x = g ^ { - 1 } ( y ) = B ^ { - 1 } y$ : It is like multiplication by $B = 3$ and $B ^ { - 1 } = 1 / 3$ , except that $x$ and $y$ are vectors.

Now suppose a second function multiplies by another matrix $A \colon z = h ( g ( x ) ) = A B x$ The problem is to recover $x$ from $z$ : The first step is to invert $A$ , because that came last: $B x = A ^ { - 1 } z$ : Then the second step multiplies by $B ^ { - 1 }$ and brings back $x = B ^ { - 1 } A ^ { - 1 } z$ : The product $B ^ { - 1 } A ^ { - 1 }$ inverts the product $A B$ . The rule for matrix inverses is like the rule for function inverses—in fact it is a special case.

I had better not wander too far from calculus. The next section introduces the inverses of the sine and cosine and tangent, and finds their derivatives. Remember that the ultimate source is the chain rule.