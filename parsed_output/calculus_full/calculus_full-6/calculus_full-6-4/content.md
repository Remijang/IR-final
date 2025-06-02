# 6.4 Logarithms

We have given first place to $e ^ { x }$ and a lower place to ln $x$ : In applications that is absolutely correct. But log»arithms have one important» theoretical advantage (plus many applications of their own). The advantage is that the derivative of $\ln x$ is $1 / x$ ; whereas the derivative of $e ^ { x }$ is $e ^ { x }$ : We can’t define $e ^ { x }$ as its own integral, without circular reasoning. But we can and do define $\ln x$ (the natural logarithm) as the integral of the “ $^ { \cdot } - 1$ power” which is $1 / x$ :

$$
\ln x = \int _ { 1 } ^ { x } { \frac { 1 } { x } } d x \qquad { \mathrm { o r } } \qquad \ln y = \int _ { 1 } ^ { y } { \frac { 1 } { u } } d u .
$$

Note the dummy variables, first $x$ then $u$ : Note also the live variables, first $x$ then $y$ : Especially note the lower limit of integration, which is 1 and not 0: The logarithm is the area measured from 1. Therefore ln $1 = 0$ at that starting poin¡t—as required.

Earlier chapters integrated all powers except this $^ { 6 6 } - 1$ power.” The logarithm is that missing integral. The curve in Figure 6.11 has height $y = 1 / x$ —it is a hyperbola. At $x = 0$ the height goes to infinity and the area becomes infinite: $\log 0 = - \infty$ : The minus sign is because the integral goes backward from 1 to 0: The integral does not extend past zero to negative $x$ : We are defining $\ln x$ only for $x > 0 .$ 

With this new approach, ln $x$ has a direct definition. $I t$ is an integral (or an area). Its two key properties must follo»w from thi»s definition. »That step is a beautiful application of the theory behind integrals.

Property 1: $\ln a b = \ln a + \ln b$ : The areas from 1 to $a$ and from $a$ to $a b$ combine into a single area (1 to $a b$ in the middle figure):

$$
{ \mathrm { N e i g h b o r i n g ~ a r e a s : } } \int _ { 1 } ^ { a } { \frac { 1 } { x } } d x + \int _ { a } ^ { a b } { \frac { 1 } { x } } d x = \int _ { 1 } ^ { a b } { \frac { 1 } { x } } d x .
$$

The right side is $\ln a b$ ; from definition (1). The first term on the left is $\ln { a }$ : The problem is to show that the second integral ( $a$ to $a b$ ) is $\ln b$ :

$$
\int _ { a } ^ { a b } { \frac { 1 } { x } } d x { \overset { ( ? ) } { = } } \int _ { 1 } ^ { b } { \frac { 1 } { u } } d u = \ln b .
$$

We need $u = 1$ when $x = a$ (the lower limit) and $u = b$ when $x = a b$ (the upper limit). The choice $u = x / a$ satisfies these requirements. Substituting $x = a u$ and $d x =$ a $d u$ yields $d x / x = d u / u$ : Equation (3) gives $\ln b$ ; and equation (2) is $\ln a + \ln b =$ $\ln a b$ :

# 6.4 Logarithms

Property 2: $\ln b ^ { n } = n \ln b$ : These are the left and right sides of

$$
\int _ { 1 } ^ { b ^ { n } } { \frac { 1 } { x } } d x \ { \stackrel { ( ? ) } { = } } \ n \int _ { 1 } ^ { b } { \frac { 1 } { u } } d u .
$$

This comes from the substitution $x = u ^ { n }$ : The lower limit $x = 1$ corresponds to $u = 1$ ; and $x = b ^ { n }$ corresponds to $u = b$ : The differential $d x$ is $n u ^ { n - 1 } d u$ : Dividing by $x = u ^ { n }$ leaves $d x / x = n d u / u$ : Then equation (4) becomes $\ln b ^ { n } = n \ln b$ :

Everything comes logically from the definition as an area. Also definite integrals:

EXAMPLE 1 Comp $\mathrm { u t e } \int _ { x } ^ { 3 x } { \frac { 1 } { t } } d t . \quad \mathrm  S o l u t i o n : \ln { 3 x } - \ln { { x } } = \ln { \frac { 3 x } { x } } = \ln { 3 } .$ EXAMPLE 2 Comput $\it { \Psi } = \int _ { \bf { - 1 } } ^ { 1 } \frac { 1 } { x } d x . \mathrm {  ~ \cal ~ { ~ S o l u t i o n } : \ln ~ } 1 - \ln . 1 = \ln ~  1 0 . ( { \bf { W } \ h y \cdot \nabla } )$ EXAMPLE 3 Compute $\int _ { 1 } ^ { e ^ { 2 } } { \frac { 1 } { u } } d u$ : Solution: ln $e ^ { 2 } = 2$ : The area from 1 to $e ^ { 2 }$ is 2:

Remark While working on the theory this is a chance to straighten out old debts. The book has discussed and computed (and even differentiated) the functions $e ^ { x }$ and $b ^ { x }$ and $x ^ { n }$ ; without defining them properly. When the exponent is an irrational number like $\pi$ ; how do we multiply $e$ by itself $\pi$ times ? One approach (not taken) is to come closer and closer to $\pi$ by rational exponents like $2 2 / 7$ : Another approach (taken now) is to determine the number $e ^ { \pi } = 2 3 . 1$ : : : by its logarithm. $\dagger$ Start with $e$ itself:

When the area in Figure 6.12 reaches 1; the basepoint is e. When the area reaches $\pi$ ; the basepoint is $e ^ { \pi }$ : We are constructing the inverse function (which is $e ^ { x }$ ). But how do we know that the area reaches $\pi$ or 1000 or $- 1 0 0 0$ at exactly one point ? (The area is 1000 far out at $e ^ { 1 0 0 0 }$ : The area is $- 1 0 0 0$ very near zero at $\dot { e } ^ { - 1 0 0 \hat { 0 } }$ :) To define $e$ we have to know that somewhere the area equals 1!

For a proof in two steps, go back to Figure 6.11c. The area from 1 to 2 is more than $\frac { 1 } { 2 }$ (because $1 / x$ is more than $\frac { 1 } { 2 }$ on that interval of length one). The combined area from 1 to 4 is more than 1: We come to area $= 1$ before reaching 4: (Actually at $e = 2 . 7 1 8 \dots ,$ ) Since $1 / x$ is positive, the area is increasing and never comes back to 1:

To double the area we have to square the distance. The logarithm creeps upwards:

$$
\ln x \to \infty \quad { \mathrm { b u t } } \quad { \frac { \ln x } { x } } \to 0 .
$$

The logarithm grows slowly because $e ^ { x }$ grows so fast (and vice versa—they are inverses). Remember that $e ^ { x }$ goes past every power $x ^ { n }$ : Therefore $\ln x$ is passed by every root $x ^ { 1 / n }$ : Problems 60 and 61 give two proofs that $( \ln x ) / x ^ { 1 / n }$ approaches zero.

We might compare ln $x$ with $\sqrt { x }$ : At $x = 1 0$ they are close (2:3 versus 3:2). But out at $x = e ^ { 1 0 }$ the comparison is 10 against $e ^ { 5 }$ ; and ln $x$ loses to $\sqrt { x }$ :

# APPROXIMATION OF LOGARITHMS

The limiting cases $\mathrm { ~ n ~ } 0 = - \infty$ and ln $\infty = + \infty$ are important. More important are logarithms near the starting point ln $1 = 0$ : Our question is: What is $\ln ( 1 + x )$ for $x$ near zero ? The exact answer is an area. The approximate answer is much simpler. If $x$ (positive or negative) is small, then

$$
\ln ( 1 + x ) \approx x \qquad { \mathrm { a n d } } \qquad e ^ { x } \approx 1 + x .
$$

The calculator gives ln $1 . 0 1 = . 0 0 9 9 5 0 3$ : This is close to $x = . 0 1$ : Between 1 and $1 + x$ the ar2ea under the graph of $1 / x$ is nearly a rectangle. Its base is $x$ and its height is 1: So the curved area $\ln ( 1 + x )$ is close to the rectangular area $x$ : Figure 6.14 shows how a small triangle is chopped off at the top.

The difference between .0099503 (actual) and .01 (linear approximation) is :0000497: That is predicted almost exactly by the second derivative: $\frac { 1 } { 2 }$ times $( \Delta x ) ^ { 2 }$ times $( \ln x ) ^ { \prime \prime }$ is $\textstyle { \frac { 1 } { 2 } } { \bigl ( } . 0 1 { \bigr ) } ^ { 2 } { \bigl ( } - 1 { \bigr ) } = - . 0 0 0 0 5$ : This is the area of the small triangle!

$$
\begin{array} { r } { \ln ( 1 + x ) \approx r e c t a n g u l a r a r e a m i n u s t r i a n g u l a r a r e a = x - \frac { 1 } { 2 } x ^ { 2 } . } \end{array}
$$

The remaining mistake of :0000003 is close to ${ \scriptstyle { \frac { 1 } { 3 } } } x ^ { 3 }$ (Problem 65).

May I switch to $e ^ { x }$ ? Its slope starts at $e ^ { 0 } = 1$ ; so its linear approximation is $1 + x$ : Then $\ln ( e ^ { x } ) \approx \ln ( 1 + x ) \approx x$ : Twowrongs do make a right: $\ln ( e ^ { x } ) = x $ exactly.

The calculator gives $e ^ { . 0 1 }$ as 1:0100502 (actual) instead of 1:01 (approximation). The second-order correction is again a small triangle: ${ \frac { 1 } { 2 } } x ^ { 2 } = . 0 0 0 0 5$ : The complete series for $\ln ( 1 + x )$ and $e ^ { x }$ are in Sections 10:1 and 6:6 W

$$
\ln ( 1 + x ) = x - x ^ { 2 } / 2 + x ^ { 3 } / 3 - \ldots \qquad e ^ { x } = 1 + x + x ^ { 2 } / 2 + x ^ { 3 } / 6 + \ldots
$$

# DERIVATIVES BASED ON LOGARITHMS

Logarithms turn up as antiderivatives very often. To build up a collection of integrals, we now differentiate ln $u ( x )$ by the chain rule.

# 6.4 Logarithms

The slope of ln $x$ was hard work in Section 6:2: With its new definition (the integral of $1 / x \mathrm { \ i }$ ) the work is gone. By the Fundamental Theorem, the slope must be $1 / x$ :

For ln $u ( x )$ the derivative comes from the chain rule. The inside function is $u$ ; the outside function is ln : (Keep $u > 0$ to define ln $u$ :) The chain rule gives

$$
{ \begin{array} { r l r l } & { { \frac { d } { d x } } \ln c x = { \frac { 1 } { c x } } c = { \frac { 1 } { x } } ( ! ) } & & { { \frac { d } { d x } } \ln x ^ { 3 } = 3 x ^ { 2 } / x ^ { 3 } = { \frac { 3 } { x } } } \\ & { { \frac { d } { d x } } \ln ( x ^ { 2 } + 1 ) = 2 x / ( x ^ { 2 } + 1 ) } & & { { \frac { d } { d x } } \ln \cos x = { \frac { - \sin x } { \cos x } } = - \tan x } \\ & { { \frac { d } { d x } } \ln e ^ { x } = e ^ { x } / e ^ { x } = 1 } & & { { \frac { d } { d x } } \ln ( \ln x ) = { \frac { 1 } { \ln x } } { \frac { 1 } { x } } . } \end{array} }
$$

Those are worth another look, especially the first. Any reasonable person would expect the slope of $\ln { 3 x }$ to be $3 / x$ : Not so. The 3 cancels, and $\ln { 3 x }$ has the same slope as $\ln x$ : (The real reason is that ln $3 x = \ln 3 + \ln x .$ ) The antiderivative of $3 / x$ is not ln $3 x$ but $3 \ln x$ ; which is $\ln x ^ { 3 }$ :

Before moving to integrals, here is a new method for derivatives: logarithmic differentiation or LD. It applies to produ?cts and powers. The product and power rules are always available, but sometimes there is an easier way.

Main idea: The logarithm of a product $p ( x )$ is a sum of logarithms. Switching to $\ln { p }$ ; the sum rule just adds up the derivatives. But there is a catch at the end, as you see in the example.

EXAMPLE 4 Find $d p / d x$ if $p ( x ) = x ^ { x } { \sqrt { x - 1 } }$ : Here ln $p ( x ) = x$ ln $\begin{array} { r } { x + \frac { 1 } { 2 } \ln ( x - 1 ) } \end{array}$ :

$$
\begin{array} { r l } { \mathrm { T a k e ~ t h e ~ d e r i v a t i v e ~ o f ~ l n ~ } p { : } } & { \displaystyle \frac { 1 } { p } \frac { d p } { d x } = x \cdot \frac { 1 } { x } + \ln x + \frac { 1 } { 2 ( x - 1 ) } \cdot } \\ { \mathrm { N o w ~ m u l t i p l y ~ b y ~ } p ( x ) { : } } & { \displaystyle \frac { d p } { d x } = p \left( 1 + \ln x + \frac { 1 } { 2 ( x - 1 ) } \right) . } \end{array}
$$

The catch is that last step. Multiplying by $p$ complicates the answer. This can’t be helped—logarithmic differentiation contains no magic. The derivative of $p = f g$ is the same as from the product rule: ln $p = \ln f + \ln g$ gives

$$
\frac { p ^ { \prime } } { p } = \frac { f ^ { \prime } } { f } + \frac { g ^ { \prime } } { g } \quad \mathrm { a n d } \quad p ^ { \prime } = p \left( \frac { f ^ { \prime } } { f } + \frac { g ^ { \prime } } { g } \right) = f ^ { \prime } g + f g ^ { \prime } .
$$

For $p = x e ^ { x } \sin x$ ; with three factors, the sum has three terms:

$$
\ln p = \ln x + x + \ln \sin x \mathrm { a n d } p ^ { \prime } = p \left[ { \frac { 1 } { x } } + 1 + { \frac { \cos x } { \sin x } } \right] .
$$

We multiply $p$ times $p ^ { \prime } / p$ (the derivative of ln $p$ ). Do the same for powers:

$$
p = x ^ { 1 / x } \Rightarrow \ln p = { \frac { 1 } { x } } \ln x \Rightarrow { \frac { d p } { d x } } = p \left[ { \frac { 1 } { x ^ { 2 } } } - { \frac { \ln x } { x ^ { 2 } } } \right] .
$$

$$
p = x ^ { \ln x } \Rightarrow \ln p = ( \ln x ) ^ { 2 } \Rightarrow { \frac { d p } { d x } } = p \left[ { \frac { 2 \ln x } { x } } \right] .
$$

$$
p = x ^ { 1 / \ln x } \Rightarrow \ln p = { \frac { 1 } { \ln x } } \ln x = 1 \Rightarrow { \frac { d p } { d x } } = 0
$$

# INTEGRALS BASED ON LOGARITHMS

Now comes an important step. Many integrals produce logarithms. The foremost example is $1 / x$ ; whose integral is ln $x$ : In a certain way that is the only example, but its range is enormously extended by the chain rule. The derivative of $\ln u ( x )$ is $u ^ { \prime } / u$ ; so the integral goes from $u ^ { \prime } / u$ back to ln $u$ :

$$
\int \frac { d u / d x } { u ( x ) } d x = \ln u ( x ) \quad \mathrm { o r ~ e q u i v a l e n t l y } \quad \int \frac { d u } { u } = \ln u .
$$

# Try to choose $u ( x )$ so that the integral contains $d u / d x$ divided by $u$ :

# EXAMPLES

$$
\int { \frac { d x } { x + 7 } } = \ln | x + 7 | \qquad \int { \frac { d x } { c x + 7 } } = { \frac { 1 } { c } } \ln | c x + 7 |
$$

Final remark When $u$ is negative, ln $u$ cannot be the integral of $1 / u$ : The logarithm is not defi ned when $u < 0$ : But the integral can go forward by switching to $- u$ :

$$
\int { \frac { d u / d x } { u } } d x = \int { \frac { - d u / d x } { - u } } d x = \ln ( - u ) .
$$

Thus $\ln ( - u )$ succeeds when $\ln u$ fails. The forbidden case is $u = 0$ . The integrals $\ln u$ and $\ln ( - u )$ ; on the plus and minus sides of zero, can be combined as $\ln \left| u \right|$ : Every integral that gives a logarithm allows $u < 0$ by changing to the absolute value $\left| u \right|$ :

$$
\int _ { - e } ^ { - 1 } { \frac { d x } { x } } = \Big [ \ln | x | \Big ] _ { - e } ^ { - 1 } = \ln 1 - \ln e \quad \int _ { 2 } ^ { 4 } { \frac { d x } { x - 5 } } = \Big [ \ln | x - 5 | \Big ] _ { 2 } ^ { 4 } = \ln 1 - \ln 3 .
$$

The areas are $^ { - 1 }$ and $- \ln 3$ : The graphs of $1 / x$ and $1 / ( x - 5 )$ are below t he $x$ axis. We do not have l|og|arithms of negative numbers, and we will not integrate $1 / ( x - 5 )$ from 2»to 6: That cro»sses the forbidden point $x = 5$ ; »with infinite area on both sides.

The ratio $d u / u$ leads to important integrals. When $u = \cos x$ or $u = \sin x$ ; we are integra»ting the tange»nt and cotangent. When there i»s a possibility that $u < 0$ ; write the integral as ln $\left| u \right|$ :

$$
\begin{array} { l l } { \displaystyle { \int \tan x d x = \int \frac { \sin x } { \cos x } d x = - \ln \left| \cos x \right| } } & { \quad \displaystyle { \int \frac { x d x } { x ^ { 2 } + 7 } = \frac { 1 } { 2 } \ln ( x ^ { 2 } + 7 ) } } \\ { \displaystyle { \int \cot x d x = \int \frac { \cos x } { \sin x } d x = \ln \left| \sin x \right| } } & { \quad \displaystyle { \int \frac { d x } { x \ln x } = \ln \left| \ln x \right| } } \end{array}
$$

Now w»e report on the»secant and cosecant. The integrals of $1 / \cos x$ and $1 / \sin x$ also surrender to an attack by logarithms—based on a crazy|trick:

$$
\begin{array} { l } { \int \sec x \ d x = \displaystyle \int \sec x \left( \frac { \sec x + \tan x } { \sec x + \tan x } \right) d x = \ln | \sec x + \tan x | . } \\ { \displaystyle \int \csc x \ d x = \displaystyle \int \csc x \left( \frac { \csc x - \cot x } { \csc x - \cot x } \right) d x = \ln | \csc x + \cot x | . } \end{array}
$$

Here $u = \sec x + \tan x$ is in the denominator; $d u / d x = \sec x$ tan $x + \sec ^ { 2 } x$ is above it. The integral is ln $\left| u \right|$ : Similarly (10) contains $d u / d x$ over $u = \csc x - \cot x$ :

# 6.4 Logarithms

In closing we integrate ln $x$ itself. The derivative of $x$ ln $x$ is ln $x + 1$ : To remove the extra 1; subtract $x$ from the integral: $\textstyle \int \ln x d x = x$ ln $x - x$ :

In contrast, the area under $1 / ( \ln x )$ has no elementary formula. Nevertheless it is the key to the greatest approximation in mathematics—the prime number theorem. The area $\textstyle \int _ { a } ^ { b } d x / \ln x$ is approximately the number of primes between a and $b$ . Near $e ^ { 1 0 0 0 }$ ; about $1 / 1 0 0 0$ of the integers are prime.