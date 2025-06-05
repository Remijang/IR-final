# 6.7 Hyperbolic Functions

This section combines $e ^ { x }$ with $e ^ { - x }$ . Up to now those functions have gone separate ways—one increasing, the other decreasing. But two particular combinations have earned names of their own (cosh $x$ and sinh $x$ ):

$$
h y p e r b o l i c ~ c o s i n e ~ \cosh x = \frac { e ^ { x } + e ^ { - x } } 2 ~ h y p e r b o l i c ~ s i n e ~ \sinh x = \frac { e ^ { x } - e ^ { - x } } 2
$$

The first name rhymes with “gosh”. The second is usually pronounced “cinch”.

The graphs in Figure 6.18 show that cosh $x > \sinh { x }$ . For large $x$ both hyperbolic functions come extremely close to ${ \scriptstyle { \frac { 1 } { 2 } } } e ^ { x } $ . When $x$ is large and negative, it is $e ^ { - x }$ that dominates. Cosh $x$ still goes up to $+ \infty$ while sinh $x$ goes down to $- \infty$ (because sinh $x$ has a minus sign in front of $e ^ { - x }$ ).

The following facts come directly from $\scriptstyle { \frac { 1 } { 2 } } \left( e ^ { x } + e ^ { - x } \right)$ and $\scriptstyle { \frac { 1 } { 2 } } \left( e ^ { x } - e ^ { - x } \right)$ :

$$
\begin{array} { c } { { \mathrm { c o s h } ( - x ) = \cosh x \ \mathrm { a n d } \ \mathrm { c o s h } 0 = 1 } } \\ { { \mathrm { s i n h } ( - x ) = - \sinh x \ \mathrm { a n d } \ \mathrm { s i n h } 0 = 0 } } \end{array}
$$

The graph of cosh $x$ corresponds to a hanging cable (hanging under its weight). Turned upside down, it has the shape of the Gateway Arch in St. Louis. That must be the largest upside-down cosh function ever built. A cable is easier to construct than an arch, because gravity does the work. With the right axes in Problem 55; the height of the cable is a stretched-out cosh function called a catenary:

$$
y = a \cosh \left( x / a \right) \qquad { \mathrm { ( c a b l e ~ t e n s i o n / c a b l e ~ d e n s i t y = } } a ) .
$$

Busch Stadium in St. Louis has 96 catenary curves, to match the Arch.

The properties of the hyperbolic functions come directly from the definitions. There are too many properties to memorize—and no reason to do it! One rule is the most important. Every fact about sines and cosines is reflected in a corresponding fact about sinh $x$ and cosh $x$ : Often the only difference is a minus sign. Here are four properties:

1. $( \cosh x ) ^ { 2 } - ( \sinh x ) ^ { 2 } = 1 \quad \Bigl [ \mathrm { i n s t e a d o f } ( \cos x ) ^ { 2 } + ( \sin x ) ^ { 2 } = 1 \Bigr ]$   
Check: $\left[ { \frac { e ^ { x } + e ^ { - x } } { 2 } } \right] ^ { 2 } - \left[ { \frac { e ^ { x } - e ^ { - x } } { 2 } } \right] ^ { 2 } = { \frac { e ^ { 2 x } + 2 + e ^ { - 2 x } - e ^ { 2 x } + 2 - e ^ { - 2 x } } { 4 } } = 1$   
2 ${ \frac { d } { d x } } { \big ( } \cosh x { \big ) } = \sinh x \quad \left[ \operatorname { i n s t e a d o f } { \frac { d } { d x } } { \big ( } \cos x { \big ) } = - \sin x \right]$   
3. ${ \frac { d } { d x } } \left( \sinh x \right) = \cosh x \quad \left[ \operatorname { l i k e } { \frac { d } { d x } } \sin x = \cos x \right]$   
4. $\int \sinh x d x = \cosh x + C \qquad { \mathrm { a n d } } \qquad \int \cosh x d x = \sinh x + C$

Property 1 is the connection to hyperbolas. It is responsible for the “h” in cosh and sinh: Remember that $( \cos x ) ^ { 2 } + ( \sin x ) ^ { 2 } = 1$ puts the point . $( \cos x , \sin x )$ onto a unit circle. As $x$ varies, the point goes around the circle. The ordinary sine and cosine are “circular functions.”Now look at $( \cosh x , \sinh x )$ /:Property 1 is $( \cosh x ) ^ { 2 } - ( \sinh x ) ^ { 2 } = 1$ , so this point travels on the unit hyperbola in Figure 6.20.

You will guess the definitions of the other four hyperbolic functions:

$$
\begin{array} { l l } { \operatorname { t a n h } x = { \frac { \sinh x } { \cosh x } } = { \frac { e ^ { x } - e ^ { - x } } { e ^ { x } + e ^ { - x } } } } & { \operatorname { c o t h } x = { \frac { \cosh x } { \sinh x } } = { \frac { e ^ { x } + e ^ { - x } } { e ^ { x } - e ^ { - x } } } } \\ { \operatorname { s e c h } x = { \frac { 1 } { \cosh x } } = { \frac { 2 } { e ^ { x } + e ^ { - x } } } } & { \operatorname { c s c h } x = { \frac { 1 } { \sinh x } } = { \frac { 2 } { e ^ { x } - e ^ { - x } } } } \end{array}
$$

I think “tanh” is pronounceable, and “sech” is easy. The others are harder. Their properties come di»rectly from c $\operatorname { \mathrm { : o s h } } ^ { 2 } x - \sinh ^ { 2 } x = 1$ : Divide by $\cosh ^ { 2 } x$ and $\sinh ^ { 2 } x$ :

$$
\begin{array} { r l } { 1 - \operatorname { t a n h } ^ { 2 } x = \operatorname { s e c h } ^ { 2 } x \quad } & { \mathrm { a n d } \quad \coth ^ { 2 } x - 1 = \operatorname { c s c h } ^ { 2 } x } \\ { ( \operatorname { t a n h } x ) ^ { \prime } = \operatorname { s e c h } ^ { 2 } x \quad } & { \mathrm { a n d } \quad ( \operatorname { s e c h } x ) ^ { \prime } = - \operatorname { s e c h } x \operatorname { t a n h } x } \end{array}
$$

$$
\int \operatorname { t a n h } x \ d x = \int { \frac { \sinh x } { \cosh x } } d x = \ln ( \cosh x ) + C .
$$

# INVERSE HYPERBOLIC FUNCTIONS

You remember the angles $\sin ^ { - 1 } x$ and $\tan ^ { - 1 } x$ and $\sec ^ { - 1 } x$ : In Section 4.4 we differentiated those inverse functions by the chain rule. The main application was to integrals. If we happen to meet $\textstyle \int d x / ( 1 + x ^ { 2 } )$ ; it is $\tan ^ { - 1 } x + C$ : The situation for

$\sinh ^ { - 1 } x$ and tanh $^ { - 1 } x$ and $\operatorname { s e c h } ^ { - 1 } \boldsymbol { x }$ is the same except for sign changes—which are expected for hyperbolic functions. We write down the three new derivatives:

$$
{ \begin{array} { l } { y = \sinh ^ { - 1 } x \ ( \operatorname { m e a n i n g } x = \sinh y ) \operatorname { h a s } \ { \frac { d y } { d x } } = { \frac { 1 } { \sqrt { x ^ { 2 } + 1 } } } } \\ { y = \operatorname { t a n h } ^ { - 1 } x \ ( \operatorname { m e a n i n g } x = \operatorname { t a n h } y ) \operatorname { h a s } \ { \frac { d y } { d x } } = { \frac { 1 } { 1 - x ^ { 2 } } } } \\ { y = \operatorname { s e c h } ^ { - 1 } x \ ( \operatorname { m e a n i n g } x = \operatorname { s e c h } y ) \operatorname { h a s } \ { \frac { d y } { d x } } = { \frac { - 1 } { x { \sqrt { 1 - x ^ { 2 } } } } } } \end{array} }
$$

Problems $4 4 - 4 6$ compute $d y / d x$ from $1 / ( d x / d y )$ : The alternative is to use logarithms. Since ln $x$ is the inverse of $e ^ { x }$ ; we can express $\sinh ^ { - 1 } x$ and tanh $^ { - 1 } x$ and sech $^ { - 1 } x$ as logarithms. Here is $y = \operatorname { t a n h } ^ { - 1 } x$ :

$$
y = { \frac { 1 } { 2 } } \ln \left[ { \frac { 1 + x } { 1 - x } } \right] { \mathrm { h a s ~ s l o p e ~ } } { \frac { d y } { d x } } = { \frac { 1 } { 2 } } { \frac { 1 } { 1 + x } } - { \frac { 1 } { 2 } } { \frac { 1 } { 1 - x } } = { \frac { 1 } { 1 - x ^ { 2 } } } .
$$

The last step is an ordinary derivative of ${ \scriptstyle { \frac { 1 } { 2 } } } \ln ( 1 + x ) - { \frac { 1 } { 2 } } \ln ( 1 - x )$ : Nothing is new except the answer. But where did the logarithms come from ? In the middle of the following identity, multiply above and below by cosh $y$ :

$$
{ \frac { 1 + x } { 1 - x } } = { \frac { 1 + \operatorname { t a n h } y } { 1 - \operatorname { t a n h } y } } = { \frac { \cosh y + \sinh y } { \cosh y - \sinh y } } = { \frac { e ^ { y } } { e ^ { - y } } } = e ^ { 2 y } .
$$

Then $2 y$ is the logarithm of the left side. This is the first equation in (4), and it is the third formula in the following list:

$$
\begin{array} { l l } { \sinh ^ { - 1 } x = \ln \left[ x + { \sqrt { x ^ { 2 } + 1 } } \right] \quad } & { \cosh ^ { - 1 } x = \ln \left[ x + { \sqrt { x ^ { 2 } - 1 } } \right] } \\ { \operatorname { t a n h } ^ { - 1 } x = { \displaystyle { \frac { 1 } { 2 } } } \ln \left[ { \frac { 1 + x } { 1 - x } } \right] \quad } & { \operatorname { s e c h } ^ { - 1 } x = \ln \left[ { \frac { 1 + { \sqrt { 1 - x ^ { 2 } } } } { x } } \right] } \end{array}
$$

Remark 1 Those are listed only for reference. If possible do not memorize them. The derivatives in equations (1), (2), (3) offer a choice of antiderivatives—either inverse functions or logarithms (most tables prefer logarithms). The inside cover of the book has

$$
\int { \frac { d x } { 1 - x ^ { 2 } } } = { \frac { 1 } { 2 } } \ln \left[ { \frac { 1 + x } { 1 - x } } \right] + C \quad { \mathrm { ( i n ~ p l a c e ~ o f ~ t a n h } } ^ { - 1 } x + C { \mathrm { ) } } .
$$

Remark 2 Logarithms were not seen for $\sin ^ { - 1 } x$ and $\tan ^ { - 1 } x$ and $\sec ^ { - 1 } x$ : You might wonder why. How does it happen that $\operatorname { t a n h } ^ { - 1 } x$ is expressed by logarithms, when the parallel formula for $\tan ^ { - 1 } x$ was missing ? Answer: There must be a parallel formula. To display it I have to reveal a secret that has been hidden throughout this section.

The secret is one of the great equations of mathematics. What formulas for cos $x$ and sin $x$ correspond to $\begin{array} { r } { \frac { 1 } { 2 } \left( \bar { e } ^ { x } + e ^ { - x } \right) } \end{array}$ and $\scriptstyle { \frac { 1 } { 2 } } \left( e ^ { x } - e ^ { - x } \right)$ ? With so many analogies (circular vs. hyperbolic ) you would expe ct to find something. The formulas do exist, but they involve imaginary numbers. Fortunately they are very

# 6.7 Hyperbolic Functions

simple and there is no reason to withhold the truth any longer:

$$
\cos x = { \frac { 1 } { 2 } } { \big ( } e ^ { i x } + e ^ { - i x } { \big ) } \qquad { \mathrm { a n d } } \qquad \sin x = { \frac { 1 } { 2 i } } { \big ( } e ^ { i x } - e ^ { - i x } { \big ) } .
$$

It is the imaginary exponents that kept those identities hidden. Multiplying sin $x$ by $i$ and adding to cos $x$ gives Euler’s unbelievably beautiful equation

$$
\cos x + i \sin x = e ^ { i x } .
$$

That is parallel to the non-beautiful hyperbolic equation cosh $x + \sinh x = e ^ { x }$ :

I have to say that (6) is infinitely more important than anything hyperbolic will ever be. The sine and cosine are far more useful than the sinh and cosh : So we end our record of the main properties, with exercises to bring out their applications.