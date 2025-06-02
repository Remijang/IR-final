# 2.5 The Product and Quotient and Power Rules

What are the derivatives of $x + \sin x$ and $x$ sin $x$ and $1 / \sin x$ and $x / \sin x$ and $\sin ^ { n } x ?$ Those are made up from the familiar pieces $x$ and sin $x$ , but we need new rules. Fortunately they are rules that apply to every function, so they can be established once and for all. If we know the separate derivatives of two functions $u$ and $v$ , then the derivatives of $u + v$ and ${ u v }$ and $1 / v$ and $u / v$ and $u ^ { n }$ are immediately available.

This is a straightforward section, with those five rules to learn. It is also an important section, containing most of the working tools of differential calculus. But I am afraid that five rules and thirteen examples (which we need—the eyes glaze over with formulas alone) make a long list. At least the easiest rule comes first. When we add functions, we add their derivatives.

# Sum Rule

$$
{ \mathrm { T h e ~ d e r i v a t i v e ~ o f ~ t h e ~ s u m ~ } } u ( x ) + v ( x ) { \mathrm { ~ i s ~ } } { \frac { d } { d x } } ( u + v ) = { \frac { d u } { d x } } + { \frac { d v } { d x } } .
$$

EXAMPLE 1 The derivative of $x + \sin x$ is $1 + \cos x$ : That is tremendously simple, but it is fundamental. The interpretation for distances may be more confusing (and more interesting) than the rule itself:

Suppose a train moves with velocity 1: The distance at time $t$ is $t$ : On the train a professor paces back and forth (in simple harmonic motion). His distance from his seat is sin t: Then the total distance from his starting point is $t + \sin t$ , and his velocity (train speed plus walking speed) is $1 + \cos t$ :

If you add distances, you add velocities. Actually that example is ridiculous, because the professor’s maximum speed equals the train speed $( = 1 )$ /: He is running like mad, not pacing. Occasionally he is standing still with respect to the ground.

The sum rule is a special case of a bigger rule called “linearity.” It applies when we add or subtract functions and multiply them by constants—as in $3 x - 4 \sin x$ : By linearity the derivative is $3 - 4 \cos x$ : The rule works for all functions $u ( x )$ and $v ( x )$ : A linear combination is $y ( x ) = a u ( x ) + b v ( x )$ , where $a$ and $b$ are any real numbers. Then $\Delta y / \Delta x$ is

$$
{ \frac { a u ( x + \Delta x ) + b v ( x + \Delta x ) - a u ( x ) - b v ( x ) } { \Delta x } } = a { \frac { u ( x + \Delta x ) - u ( x ) } { \Delta x } } + b { \frac { v ( x + \Delta x ) - v ( x ) } { \Delta x } } .
$$

The limit on the left is $d y / d x$ : The limit on the right is $a d u / d x + b d v / d x$ : We are allowed to take limits separately and add. The result is what we hope for:

# Rule of Linearity

$$
{ \mathrm { T h e ~ d e r i v a t i v e ~ o f } } a u ( x ) + b v ( x ) { \mathrm { i s } } { \frac { d } { d x } } ( a u + b v ) = a { \frac { d u } { d x } } + b { \frac { d v } { d x } } .
$$

The product rule comes next. It can’t be so simple—products are not linear. The sum rule is what you would have done anyway, but products give something new. The derivative of $u$ times $v$ is not $d u / d x$ times $d v / d x$ . Example: The derivative of $x ^ { 5 }$ is $5 x ^ { 4 }$ : Don’t multiply the derivatives of $x ^ { 3 }$ and $x ^ { 2 }$ : ( $3 x ^ { 2 }$ times $2 x$ is not $5 x ^ { 4 }$ :) For a product of two functions, the derivative has two terms.

Product Rule (the key to this section)

$$
{ \mathrm { T h e ~ d e r i v a t i v e ~ o f } } u ( x ) v ( x ) { \mathrm { ~ i s ~ } } { \frac { d } { d x } } ( u v ) = u { \frac { d v } { d x } } + v { \frac { d u } { d x } } .
$$

EXAMPLE 2 $u = x ^ { 3 }$ times $v = x ^ { 2 }$ is $u v = x ^ { 5 }$ : The product rule leads to $5 x ^ { 4 }$ :

$$
x ^ { 3 } { \frac { d v } { d x } } + x ^ { 2 } { \frac { d u } { d x } } = x ^ { 3 } ( 2 x ) + x ^ { 2 } ( 3 x ^ { 2 } ) = 2 x ^ { 4 } + 3 x ^ { 4 } = 5 x ^ { 4 } .
$$

EXAMPLE 3 In the slope of $x$ sin $x$ , I don’t write $d x / d x = 1$ but it’s there:

$$
{ \frac { d } { d x } } ( x \sin x ) = x \cos x + \sin x .
$$

EXAMPLE 4 If $u = \sin x$ and $v = \sin x$ then $u v = \sin ^ { 2 } x$ : We get two equal terms:

$$
\sin x { \frac { d } { d x } } ( \sin x ) + \sin x { \frac { d } { d x } } ( \sin x ) = 2 \sin x \cos x .
$$

This confirms the “square rule” $2 u \ d u / d x$ , when $u$ is the same as $v$ : Similarly the slope of $\cos ^ { 2 } x$ is $- 2$ cos $x$ sin $x$ (minus sign from the slope of the cosine).

Question Those answers for $\sin ^ { 2 } x$ and $\cos ^ { 2 } x$ have opposite signs, so the derivative of $\sin ^ { 2 } x + \cos ^ { 2 } x$ is zero (sum rule). How do you see that more quickly ?

After those examples we prove the product rule. Figure 2.13 explains it best. The area of the big rectangle is $u v$ : The important changes in area are the two strips $u \Delta v$ and $v \Delta u$ . The corner area $\Delta u \Delta v$ is much smaller. When we divide by $\Delta x$ , the strips give $u \Delta v / \Delta x$ and $v \Delta u / \Delta x$ : The corner gives $\Delta u \Delta v / \Delta x$ , which approaches zero.

Notice how the sum rule is in one dimension and the product rule is in two dimensionsÑ. The rule for uvw would be in three dimensions.

The extra area comes from the whole top strip plus the side strip. By algebra, $u ( x + h ) v ( x + h ) - u ( x ) v ( x ) = u ( x + h ) [ v ( x + h ) - v ( x ) ] + v ( x ) [ u ( x + h ) - u ( x ) ] .$ (

This increase is $u ( x + h ) \Delta v + v ( x ) \Delta u$ —top plus side. Now divide by $h$ (or $\Delta x$ ) and let $h  0$ . The left side of equation (4) becomes the derivative of $u ( x ) v ( x )$ : The right side becomes $u ( x )$ times $d v / d x$ —we can multiply the two limits—plus $v ( x )$ times $d u / d x$ : That proves the product rule—definitely useful.

We could go immediately to the quotient rule for $u ( x ) / v ( x )$ : But start with $u = 1$ : The derivative of $1 / x$ is $- 1 / x ^ { 2 }$ (known). What is the derivative of $1 / v ( x ) \}$

# Reciprocal Rule

$$
{ \mathrm { T h e ~ d e r i v a t i v e ~ o f ~ } } \ { \frac { 1 } { v ( x ) } } { \mathrm { ~ i s ~ } } { \frac { - d v / d x } { v ^ { 2 } } } .
$$

The proof starts with $( v ) ( 1 / v ) = 1$ : The derivative of 1 is 0: Apply the product rule:

$$
v { \frac { d } { d x } } \left( { \frac { 1 } { v } } \right) + { \frac { 1 } { v } } { \frac { d v } { d x } } = 0 \quad { \mathrm { s o ~ t h a t } } \quad { \frac { d } { d x } } \left( { \frac { 1 } { v } } \right) = { \frac { - d v / d x } { v ^ { 2 } } } .
$$

It is worth checking the units—in the reciprocal rule and others. A test of dimensions is automatic in science and engineering, and a good idea in mathematics. The test ignores constants and plus or minus signs, but it prevents bad errors. If $v$ is in dollars and $x$ is in hours, $d v / d x$ is in dollars per hour. Then dimensions agree:

$$
\frac { d } { d x } \left( \frac { 1 } { v } \right) \approx \frac { \left( 1 / \mathrm { d o l l a r s } \right) } { \mathrm { h o u r } } \quad \mathrm { a n d ~ a l s o } \quad \frac { - d v / d x } { v ^ { 2 } } \approx \frac { \mathrm { d o l l a r s / h o u r } } { \left( \mathrm { d o l l a r s } \right) ^ { 2 } } .
$$

From this test, the derivative of $1 / v$ cannot be $1 / ( d v / d x )$ :A similar test show sthat Einstein’s formula $e = m c ^ { 2 }$ is dimensionally possible. The theory of relativity might be correct! Both sides have the dimension of (mass)(distance) $^ 2 / ( \mathrm { t i m e } ) ^ { 2 }$ , when mass is converted to energy.

EXAMPLE 6 The derivatives of $x ^ { - 1 } , x ^ { - 2 } , x ^ { - n }$ are $- 1 x ^ { - 2 } , - 2 x ^ { - 3 } , - n x ^ { - n - 1 } .$

Those come from the reciprocal rule with $v = x$ and $x ^ { 2 }$ and any $x ^ { n }$ :

$$
{ \frac { d } { d x } } ( x ^ { - n } ) = { \frac { d } { d x } } \left( { \frac { 1 } { x ^ { n } } } \right) = - { \frac { n x ^ { n - 1 } } { ( x ^ { n } ) ^ { 2 } } } = - n x ^ { - n - 1 } .
$$

The beautiful thing is that this answer $- n x ^ { - n - 1 }$ fits into the same pattern as $x ^ { n }$ : Multiply by the exponent and reduce it by one.

For negative and positive exponents the derivative of $x ^ { n }$ is $n x ^ { n - 1 } .$

EXAMPLE 7 The derivatives of $\frac { 1 } { \cos x }$ and $\frac { 1 } { \sin x }$ are $\frac { + \sin x } { \cos ^ { 2 } x }$ and ${ \frac { - \cos x } { \sin ^ { 2 } x } } .$

Those come directly from the reciprocal rule. In trigonometry, $1 / \cos x$ is the secant of the angle $x$ , and $1 / \sin x$ isthe cosecant of $x$ : Now wehave their derivatives:

$$
{ \begin{array} { l } { { \frac { d } { d x } } ( \sec x ) = { \frac { \sin x } { \cos ^ { 2 } x } } = { \frac { 1 } { \cos x } } { \frac { \sin x } { \cos x } } = \sec x \tan x . } \\ { { \frac { d } { d x } } ( \csc x ) = - { \frac { \cos x } { \sin ^ { 2 } x } } = - { \frac { 1 } { \sin x } } { \frac { \cos x } { \sin x } } = - \csc x \cot x . } \end{array} }
$$

# 2.5 The Product and Quotient and Power Rules

Those formulas are often seen in calculus. If you have a good memory they are worth storing. Like most mathematicians, I have to check them every time before using them (maybe once a year). It is really the rules that are basic, not the formulas.

The next rule applies to the quotient $u ( x ) / v ( x )$ : That is $u$ times $1 / v$ : Combining the product rule and reciprocal rule gives something new and important:

# Quotient Rule

$$
\mathrm { T h e ~ d e r i v a t i v e ~ o f } \quad \frac { u ( x ) } { v ( x ) } \quad \mathrm { i s } \quad \frac { 1 } { v } \frac { d u } { d x } - u \frac { d v / d x } { v ^ { 2 } } = \frac { v d u / d x - u d v / d x } { v ^ { 2 } } .
$$

You must memorize that last formula. The $v ^ { 2 }$ is familiar. The rest is new, but not very new. If $v = 1$ the result is $d u / d x$ (of course). For $u = 1$ we have the reciprocal rule. Figure $2 . 1 4 \mathrm { b }$ shows thedifference $( u + \Delta u ) / ( v + \Delta v ) - ( u / v )$ : The denominator $v ( v + \Delta v )$ is responsible for $v ^ { 2 }$ :

EXAMPLE 8 (only practice) If $u / v = x ^ { 5 } / x ^ { 3 }$ (which is $x ^ { 2 }$ ) the quotient rule gives $2 x$

$$
{ \frac { d } { d x } } \left( { \frac { x ^ { 5 } } { x ^ { 3 } } } \right) = { \frac { x ^ { 3 } ( 5 x ^ { 4 } ) - x ^ { 5 } ( 3 x ^ { 2 } ) } { x ^ { 6 } } } = { \frac { 5 x ^ { 7 } - 3 x ^ { 7 } } { x ^ { 6 } } } = 2 x .
$$

EXAMPLE 9 (important) For $u = \sin x$ and $v = \cos x$ , the quotient is sin $x / \cos x =$ tan $x$ : The derivative of tan1 $x$ is $\sec ^ { 2 } x$ . Use the quotient rule and $\cos ^ { 2 } x + \sin ^ { 2 } x = 1$ W

$$
{ \frac { d } { d x } } \left( { \frac { \sin x } { \cos x } } \right) = { \frac { \cos x \left( \cos x \right) - \sin x \left( - \sin x \right) } { \cos ^ { 2 } x } } = { \frac { 1 } { \cos ^ { 2 } x } } = \sec ^ { 2 } x .
$$

Again to memorize: $( \tan x ) ^ { \prime } { = } \sec ^ { 2 } x$ : At $x = 0$ , this slope is 1. The graphs of sin $x$ and $x$ and tan $x$ all start with this slope (then they separate). At $x = \pi / 2$ the sine curve is flat .cos $x = 0$ / and the tangent curve is vertical . $( \sec ^ { 2 } x = \infty$ /:

The slope generally blows up faster than the function. We divide by cos $x$ , once for the tangent and twice for its slope. The slope of $1 / x$ is $- 1 / x ^ { 2 }$ : The slope is more sensitive than the function, because of the square in the denominator.

# EXAMPLE 10

$$
{ \frac { d } { d x } } \left( { \frac { \sin x } { x } } \right) = { \frac { x \cos x - \sin x } { x ^ { 2 } } } .
$$

That one I hesitate to touch at $x = 0$ : Formally it becomes $0 / 0$ : In reality it is more like $0 ^ { 3 } / 0 ^ { 2 }$ , and the true derivative is zero. Figure 2.10 showed graphically that $( \sin x ) / x$ is flat at the center point. The function is even (symmetric across the $y$ axis) so its derivative can only be zero.

This section is full of rules, and I hope you will allow one more. It goes beyond $x ^ { n }$ to $( u ( x ) ) ^ { n }$ : A power of $x$ changes to a power of $u ( x )$ —as in $( \sin x ) ^ { 6 }$ or $( \tan x ) ^ { 7 }$ or $( x ^ { 2 } + 1 ) ^ { 8 }$ : The derivative contains $n u ^ { n - 1 }$ (copying $n x ^ { n - 1 }$ ) ,but there is an extra factor $d u / d x$ : Watch that factor in $6 ( \sin x ) ^ { 5 } \cos x$ and $7 ( \tan x ) ^ { 6 } \sec ^ { 2 } x$ and $8 ( x ^ { 2 } + 1 ) ^ { 7 } ( 2 x )$ :

# Power Rule

$$
{ \mathrm { T h e ~ d e r i v a t i v e ~ o f ~ } } \quad \left[ u ( x ) \right] ^ { n } \quad { \mathrm { ~ i s ~ } } \quad n \left[ u ( x ) \right] ^ { n - 1 } { \frac { d u } { d x } } .
$$

For $n = 1$ this reduces to $d u / d x = d u / d x$ : For $n = 2$ we get the square rule $2 u d u / d x$ : Next comes $u ^ { 3 }$ : The best approach is to use mathematical induction,

# 2 Derivatives

which goes from each $n$ to the next power $n + 1$ by the product rule:

$$
{ \frac { d } { d x } } \left( u ^ { n + 1 } \right) = { \frac { d } { d x } } \left( u ^ { n } u \right) = u ^ { n } { \frac { d u } { d x } } + u \left( n u ^ { n - 1 } { \frac { d u } { d x } } \right) = ( n + 1 ) u ^ { n } { \frac { d u } { d x } } .
$$

That is exactly equation (12) for the power $n + 1$ : We get all positive powers this way, going up from $n = 1$ —then the negative powers come from the reciprocal rule.

Figure 2.15 shows the power rule for $n = 1 , 2 , 3$ : The cube makes the point best. The three thin slabs are $u$ by $u$ by $\Delta u$ : The change in volume is essentially $3 u ^ { 2 } \Delta u$ : From multiplying out $( u + \Delta u ) ^ { 3 }$ , the exact change in volume is $3 u ^ { 2 } \Delta u + 3 u ( \Delta u ) ^ { 2 } + ( \Delta u ) ^ { 3 }$ —which also accounts for three narrow boxes and a midget cube in the corner. This is the binomial formula in a picture.

EXAMPLE 11 ${ \frac { d } { d x } } ( \sin x ) ^ { n } = n ( \sin x ) ^ { n - 1 }$ cos $x$ : The extra factor cos $x$ is $d u / d x$ :

Our last step finally escapes from a very undesirable restriction—that $n$ must be a whole number. We want to allow fractional powers $n = p / q$ , and keep the same formula. The derivative of $x ^ { n }$ is still $n x ^ { n - 1 }$ .

To deal with square roots I can write $( { \sqrt { x } } ) ^ { 2 } = x$ : Its derivative is $2 { \sqrt { x } } ( { \sqrt { x } } ) ^ { \prime } = 1$ : Therefore $( \sqrt { x } ) ^ { \prime }$ is $1 / 2 { \sqrt { x } }$ , which fits the formula when $\begin{array} { r } { n = \frac { 1 } { 2 } } \end{array}$ : Now try $n = p / q$ :

Fractional powers Write $u = x ^ { p / q }$ as $u ^ { q } = x ^ { p }$ : Take derivatives, assuming they exist:

$$
{ \begin{array} { r l r l } { q u ^ { q - 1 } } & { { \frac { d u } { d x } } = p x ^ { p - 1 } } & & { { \mathrm { ( p o w e r ~ r u l e ~ o n ~ b o t h ~ s i d e s ) } } } \\ & { } & & { { \frac { d u } { d x } } = { \frac { p x ^ { - 1 } } { q u ^ { - 1 } } } } \\ & { } & & { { \mathrm { ( c a n c e l ~ } } x ^ { p } { \mathrm { ~ w i t h ~ } } u ^ { q } { \mathrm { ) } } } \\ & { } & & { { \frac { d u } { d x } } = n x ^ { n - 1 } } & & { { \mathrm { ( r e p l a c e ~ } } p / q { \mathrm { ~ b y ~ } } n { \mathrm { ~ a n d ~ } } u { \mathrm { ~ b y ~ } } x ^ { n } { \mathrm { ) } } } \end{array} }
$$

EXAMPLE 12 The slope of $x ^ { 1 / 3 }$ is ${ \frac { 1 } { 3 } } x ^ { - 2 / 3 }$ : The slope is infinite at $x = 0$ and zero at $x = \infty$ : But the curve in Figure 2.16 keeps climbing. It doesn’t stay below an “asymptote.”

EXAMPLE 13 The slope of $x ^ { 4 / 3 }$ is ${ \frac { 4 } { 3 } } x ^ { 1 / 3 }$ : The slope is zero at $x = 0$ and infinite at $x = \infty$ : The graph climbs faster than a line and slower than a parabola ( $\frac { 4 } { 3 }$ is between 1 and 2). Its slope follows the cube root curve (times $\frac { 4 } { 3 }$ ).

WE STOP NOW! I am sorry there were so ma1ny rule1s. A c1omputer can memorize them all, but it doesn’t know what they mean and you do. Together with the chain rule that dominates Chapter 4; they achieve virtually all the derivatives ever computed by mankind. We list them in one place for convenien1ce.

$$
{ \left[ \begin{array} { l l l } { { \mathrm { R u l e ~ o f ~ L i n e a r i t y } } } & { } & { ( a u + b v ) ^ { \prime } = a u ^ { \prime } + b v ^ { \prime } } \\ { { \mathrm { P r o d u c t ~ R u l e } } } & { } & { ( u v ) ^ { \prime } = u v ^ { \prime } + v u ^ { \prime } } \\ { { \mathrm { R e c i p r o c a l ~ R u l e } } } & { } & { ( 1 / v ) ^ { \prime } = - v ^ { \prime } / v ^ { 2 } } \\ { { \mathrm { Q u o t i e n t ~ R u l e } } } & { } & { ( u / v ) ^ { \prime } = ( v u ^ { \prime } - u v ^ { \prime } ) / v ^ { 2 } } \\ { { \mathrm { P o w e r ~ R u l e } } } & { } & { ( u ^ { n } ) ^ { \prime } = n u ^ { n - 1 } u ^ { \prime } } \end{array} \right] }
$$

The power 1rule applies when $n$ is n1egative, or a fraction, o1r any real number. The derivative of $x ^ { \pi }$ is $\pi x ^ { \pi - 1 }$ , accordingto Chapter 6: The derivative of $( \sin x ) ^ { \pi }$ is : And the derivatives of all six trigonometric functions are now established:

$$
( \sin x ) ^ { \prime } = \quad \cos x \qquad ( \tan x ) ^ { \prime } = \quad \sec ^ { 2 } x \qquad ( \sec x ) ^ { \prime } = \quad \sec x \tan x
$$

$$
( \cos x ) ^ { \prime } = - \sin x \qquad { \mathrm { ( c o t ~ } } x { \mathrm { ) ^ { \prime } = - c s c ^ { 2 } } } x \qquad { \mathrm { ( c s c ~ } } x { \mathrm { ) ^ { \prime } = - c s c ~ } } x { \mathrm { \cot ~ } } x .
$$