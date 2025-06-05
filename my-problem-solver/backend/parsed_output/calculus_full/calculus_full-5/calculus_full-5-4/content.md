# 5.4 Indefinite Integrals and Substitutions

This section integrates the easy way, by looking for antiderivatives. We leave aside sums of rectangular areas, and their limits as $\Delta x \to 0$ : Instead we search for an $f ( x )$ with the required derivative $v ( x )$ : In practice, this approach is more or less independent of the approach through sums—but it gives the same answer. And also, the search for an antiderivative may not succeed. We may not find $f .$ In that case we go back to rectangles, or on to something better in Section 5.8.

A computer is ready to integrate $v$ , but not by discovering $f .$ It integrates between specified limits, to obtain a number (the definite integral). Here we hope to find a function (the indefinite integral). That requires a symbolic integration code like MACSYMA or Mathematica or MAPLE, or a reasonably nice $v ( x )$ , or both. An expression for $f ( x )$ can have tremendous advantages over a list of numbers.

Thus our goal is to find antiderivatives and use them. The techniques will be further developed in Chapter 7—this section is short but good. First we write down what we know. On each line, $f ( x )$ is an antiderivative of $v ( x )$ because $d f / d x = v ( x )$ .

$$
\begin{array} { r l r } { { K n o w n p a i r s } \quad } & { { } { F u n c t i o n v ( x ) } } & { \quad A n t i d e r i \nu a t i \nu e f ( x ) } \\ { { P o w e r s ~ o f x } \quad } & { { } { x ^ { n } } } & { \quad x ^ { n + 1 } / ( n + 1 ) + C } \end{array}
$$

$n = - 1$ is not included, because $n + 1$ would be zero. $v = x ^ { - 1 }$ will lead us to $f = \ln x$ :

$$
{ \begin{array} { r l r l r l } { { n o m e t r i c . C i n n c t i o n s } } & { } & & { \cos { x } } & & { \sin { x } + C } \\ & { } & & { \sin { x } } & & { - \cos { x } + C } \\ & { } & & { \sin { x } } & & { \tan { x } + C } \\ & { } & & { \sec ^ { 2 } { x } } & & { \tan { x } + C } \\ & { } & & { \csc ^ { 2 } { x } } & & { - \cot { x } + C } \\ & { } & & { \sec { x } } & & { \sec { x } + C } \\ & { } & & { \sec { x } \cot { x } } & & { - \csc { x } + C } \\ & { } & & { \vdots \sqrt { 1 - x ^ { 2 } } } & & { \sin ^ { - 1 } { x } + C } \\ & { } & & { 1 / ( 1 + x ^ { 2 } ) } & & { \tan ^ { - 1 } { x } + C } \\ & { } & & { 1 / \left| x \right| \sqrt { x ^ { 2 } - 1 } } & & { \sec ^ { - 1 } { x } + C } \end{array} }
$$

You recognize that each integration formula came directly from a differentiation formula. The integral of the cosine is the sine, because the derivative of the sine is the cosine. For emphasis we list three derivatives above three integrals:

$$
{ \begin{array} { r l r l } { { \frac { d } { d x } } ( { \mathrm { c o n s t a n t } } ) = 0 } & { } & { { \frac { d } { d x } } ( x ) = 1 } & { } & { { \frac { d } { d x } } \left( { \frac { x ^ { n + 1 } } { n + 1 } } \right) = x ^ { n } } \\ { \int \displaylimits _ { 0 d x = C } } & { } & { { \int \displaylimits _ { 1 } ^ { 1 } d x = x + C } } & { } & { { \int x ^ { n } d x = { \frac { x ^ { n + 1 } } { n + 1 } } + C } } \end{array} }
$$

There are two ways to make this list longer. One is to find the derivative of a new $f ( x )$ : Then $f$ goes in one column and $v = d f / d x$ goes in the other co1umn. $\dagger$ The other possibility is to use rules for derivatives to find rules for integrals. That is the way to extend the list, enormously and easily.

# 5 Integrals

# RULES FOR INTEGRALS

Among the rules for derivatives, three wÑere of supreme importance. They were linearity, the product rule, and the chain rule. Everything flowed from those three. In the reverse direction (from $v$ to $f$ ) this is still true. The three basic methods of differential calculus also dominate integral cÑalculus:

$$
\begin{array} { r l } & { l i n e a r i t y ~ o f d e r i \nu a t i \nu e s \longrightarrow l i n e a r i t y ~ o f ~ i n t e g r a l s } \\ & { p r o d u c t \mathop { r u l e f o r } { d e r i \nu a t i \nu e s } \longrightarrow i n t e g r a t i o n ~ b y ~ p a r t s } \\ & { ~ c h a i n ~ r u l e f o r ~ d e r i \nu a t i \nu e s \longrightarrow i n t e g r a l s ~ b y ~ s u b s t i t u t i o n } \end{array}
$$

The easiest is linearity, which comes first. Integration by parts will be left for Section 7.1. This section starts on substitutions, reversing the chain rule to make an integral simpler.

# LINEARITY OF INTEGRALS

What is the integral of $v ( x ) + w ( x ) ?$ Add the two separate integrals. The graph of $v + w$ has two regions below it, the area under $v$ and the area from $v$ to $v + w$ : Adding areas gives the sum rule. Suppose $f$ and $g$ are antiderivatives of $v$ and $w$ :

sum rule: $\begin{array} { c c } { { f + g } } & { { \mathrm { { i s \ a n \ a n t i d e r i v a t i v e \ o f ~ } } } } & { { v + w } } \\ { { c f } } & { { \mathrm { { i s \ a n \ a n t i d e r i v a t i v e \ o f ~ } } } } & { { c v } } \\ { { a f + b g } } & { { \mathrm { { i s \ a n \ a n t i d e r i v a t i v e \ o f ~ } } } } & { { a v + b w } } \end{array}$   
constant rule:   
linearity:

This is a case of overkill. The first two rules are special cases of the third, so logically the last rule is enough. However it is so important to deal quickly with constants— just “factor them out”—that the rule $c v  c f$ is stated separately. The proofs come from the linearity of derivatives: $( a f + b g ) ^ { \prime }$ equals $a f ^ { \prime } + b g ^ { \prime }$ which equals $a v + b w$ . The rules can be restated with integral signs:

sum rule: $\begin{array} { c } { { \int \big [ { v } ( { x } ) + { w } ( { x } ) \big ] d { x } = \int { v } ( { x } ) d { x } + \int { w } ( { x } ) d { x } } } \\ { { \int c { v } ( { x } ) d { x } = c \int { v } ( { x } ) d { x } } } \\ { { \int \big [ a v ( { x } ) + b w ( { x } ) \big ] d { x } = a \int { v } ( { x } ) d { x } + b \int w ( { x } ) d { x } } } \end{array}$   
constant rule:   
linearity:

Note about the constant in $f ( x ) + C$ . All antiderivatives allow the addition of a constant. For a combination like $a v ( x ) + b w ( x )$ , the antiderivat ive is $a f ( x ) + b g ( x ) + C$ : The constants for each part combine into a single constant. To give all possible antiderivatives of a function, just remember to write $ C ^ { , , }$ after one of them. The real problem is to find that one antiderivative.

EXAMPLE 1 The antiderivative of $v = x ^ { 2 } + x ^ { - 2 }$ is $f = x ^ { 3 } / 3 + ( x ^ { - 1 } ) / ( - 1 ) + C .$ EXAMPLE 2 The antiderivative of $6 \cos t + 7 \sin t$ is $6 \sin t - 7 \cos t + C$ :

EXAMPLE 3 Rewrite $\frac { 1 } { 1 - \sin x }$ as ${ \frac { 1 - \sin x } { 1 - \sin ^ { 2 } x } } = { \frac { 1 - \sin x } { \cos ^ { 2 } x } } = \sec ^ { 2 } x - \sec x \tan x .$

The antiderivative is tan $x - \sec x + C$ : That rewriting is done by a symbolic algebra code (or by you). Differentiation is often simple, so most people check that $d f / d x = v ( x )$ :

Question How to integrate $\tan ^ { 2 } x ?$ Method Write it as $\sec ^ { 2 } x - 1$ : Answer tan $x - x + C$ :

# INTEGRALS BY SUBSTITUTION

We now present the most valuable technique in this section—substitution. To see the idea, you have to remember the chain rule:

$$
{ \begin{array} { r l r l } { f ( g ( x ) ) } & { { \mathrm { h a s ~ d e r i v a t i v e } } } & { f ^ { \prime } ( g ( x ) ) ( d g / d x ) } \\ { \sin x ^ { 2 } } & { { \mathrm { h a s ~ d e r i v a t i v e } } } & { ( \cos x ^ { 2 } ) ( 2 x ) } \\ { ( x ^ { 3 } + 1 ) ^ { 5 } } & { { \mathrm { h a s ~ d e r i v a t i v e } } } & { 5 ( x ^ { 3 } + 1 ) ^ { 4 } ( 3 x ^ { 2 } ) } \end{array} }
$$

If the function on the right is given, the function on the left is its antiderivative! There are two points to emphasize right away:

# 1. Constants are no problem—they can always be fixed. Divide by 2 or 15:

$$
\int x \cos ( x ) ^ { 2 } d x = { \frac { 1 } { 2 } } \sin ( x ^ { 2 } ) + C \qquad \int x ^ { 2 } ( x ^ { 3 } + 1 ) ^ { 4 } d x = { \frac { 1 } { 1 5 } } ( x ^ { 3 } + 1 ) ^ { 5 } + C
$$

Notice the 2 from $x ^ { 2 }$ , the 5 from the fifth power, and the 3 from $x ^ { 3 }$ :

2. Choosing the inside function $g$ (or $u$ ) commits us to its derivative:

$$
\begin{array} { l l } { { \mathrm { t e g r a l ~ o f ~ } 2 x \cos x ^ { 2 } \mathrm { ~ i s ~ } \sin x ^ { 2 } + C } } & { { ( g = x ^ { 2 } , d g / d x = 2 x ) } } \\ { { \mathrm { t e g r a l ~ o f ~ c o s ~ } x ^ { 2 } \mathrm { ~ i s ~ } ( f a i l u r e ) } } & { { ( \mathrm { n o ~ } d g / d x ) } } \\ { { \mathrm { t e g r a l ~ o f ~ } x ^ { 2 } \cos x ^ { 2 } \mathrm { ~ i s ~ } ( f a i l u r e ) } } & { { ( \mathrm { w r o n g ~ } d g / d x ) } } \end{array}
$$

To substitute $g$ for $x ^ { 2 }$ , we need its derivative. The trick is to spot an inside function whose derivative is present. We can fix constants like 2 or 15; but otherwise $d g / d x$ has to be there. Very often the inside function $g$ is written $u$ . We use that letter to state the substitution rule, when $f$ is the integral of $v$ :

$$
\int v ( u ( x ) ) { \frac { d u } { d x } } d x = f ( u ( x ) ) + C .
$$

EXAMPLE 4 $\begin{array} { r } { \int \sin x \cos x d x = { \frac { 1 } { 2 } } ( \sin x ) ^ { 2 } + C \qquad u = \sin x } \end{array}$ (compare Example 6)

EXAMPLE 5 $\begin{array} { r } { \int \sin ^ { 2 } x \cos x d x = { \frac { 1 } { 3 } } ( \sin x ) ^ { 3 } + C \qquad u = \sin x } \end{array}$

EXAMPLE 6 $\begin{array} { r } { \int \cos x \sin x d x = - \frac 1 2 ( \cos x ) ^ { 2 } + C } \end{array}$ $u = \cos x$ (compare Example 4)

EXAMPLE 7 $\int \tan ^ { 4 } x \sec ^ { 2 } x d x = { \frac { 1 } { 5 } } ( \tan x ) ^ { 5 } + C \qquad u = \tan x$

The next example has $u = x ^ { 2 } - 1$ and $d u / d x = 2 x$ : The key step is choosing $u$ :

EXAMPLE 8 $\textstyle \int x d x / { \sqrt { x ^ { 2 } - 1 } } = { \sqrt { x ^ { 2 } - 1 } } + C \quad \quad \int x { \sqrt { x ^ { 2 } - 1 } } d x = { \frac { 1 } { 3 } } ( x ^ { 2 } - 1 ) ^ { 3 / 2 } + C$ A shift of $x$ (to $x + 2$ ) or a multiple of $x$ (rescaling to $2 x$ ) is particularly easy:

$$
\begin{array} { r l } { \int { ( x + 2 ) ^ { 3 } d x } = \frac { 1 } { 4 } ( x + 2 ) ^ { 4 } + C } & { { } \int { \cos { 2 x } d x } = \frac { 1 } { 2 } \sin { 2 x } + C } \end{array}
$$

You will soon be able to do those in your sleep. Officially the derivative of $( x + 2 ) ^ { 4 }$ uses the chain rule. But the inside function $u = x + 2$ has $d u / d x = 1$ : The “1” is there automatically, and the graph shifts over—as in Figure 5.8b.

For Example 10 the inside function is $u = 2 x$ : Its derivative is $d u / d x = 2$ : This

required factor 2 is missing in $\int \cos 2 x d x$ , but we put it there by multiplying and dividing by 2: Check the derivative of ${ \frac { 1 } { 2 } } \sin 2 x$ : the 2 from the chain rule cancels the $\frac { 1 } { 2 }$ : The rule for any nonzero constant is similar:

$$
\int v ( x + c ) d x = f ( x + c ) \quad { \mathrm { a n d } } \quad \int v ( c x ) d x = { \frac { 1 } { c } } f ( c x ) .
$$

Squeezing the graph by $c$ divides the area by $c . \operatorname { N o w } 3 x + 7$ rescales and shifts:

EXAMPLE 11 $\begin{array} { r l } { \int \cos ( 3 x + 7 ) d x = { \frac { 1 } { 3 } } \sin ( 3 x + 7 ) + C } & { { } \int ( 3 x + 7 ) ^ { 2 } d x = { \frac { 1 } { 3 } } \cdot { \frac { 1 } { 3 } } ( 3 x + 7 ) ^ { 3 } + C } \end{array}$ Remark on writing down the steps When the substitution is complicated, it is a good idea to get $d u / d x$ where you need it. Here $3 x ^ { 2 } + 1$ needs $6 x$ :

$$
\int \gamma x ( 3 x ^ { 2 } + 1 ) ^ { 4 } d x = { \frac { 7 } { 6 } } \int ( 3 x ^ { 2 } + 1 ) ^ { 4 } 6 x d x = { \frac { 7 } { 6 } } \int u ^ { 4 } { \frac { d u } { d x } } d x
$$

Now integrate: $\frac { 7 } { 6 } \frac { u ^ { 5 } } { 5 } + C = \frac { 7 } { 6 } \frac { ( 3 x ^ { 2 } + 1 ) ^ { 5 } } { 5 } + C .$

Check the derivative at the end. The exponent 5 cancels 5 in the denominator, $6 x$ from the chain rule cancels 6, and $7 x$ is what we started with.

Remark on differentials In place of $( d u / d x ) d x$ , many people just write $d u$ :

$$
\begin{array} { r } { \int { ( 3 x ^ { 2 } + 1 ) ^ { 4 } } 6 x d x = \int u ^ { 4 } d u = \frac { 1 } { 5 } u ^ { 5 } + C . } \end{array}
$$

This really shows how substitution works. We switch from $x$ to $u$ , and we also switch from $d x$ to $d u$ . The most common mistake is to confuse $d x$ with $d u$ : The factor $d u / d x$ from the chain rule is absolutely needed, to reach $d u$ : The change of variables (dummy variables anyway!) leaves an easy integral, and then $u$ turns back into $3 x ^ { 2 } + 1$ : Here are the four steps to substitute $u$ for $x$ :

1. Choose $u ( x )$ and co?mpute $d u / d x$   
2. Locate $v ( u )$ times $d u / d x$ times $d x$ , or $v ( u )$ times $d u$   
3. Integrate $\int v ( u ) d u$ to find $f ( u ) + C$   
4. Substitute $u ( x )$ back into this antiderivative $f$

$$
\begin{array} { r } { \int \left( \cos { \sqrt { x } } \right) d x / 2 \sqrt { x } = \int \cos { u } d u = \sin { u } + C = \sin { \sqrt { x } } + C } \\ { ( p u t i n ~ u ) \quad \quad ( i n t e g r a t e ) \quad ( p u t b a c k x ) } \end{array}
$$

The choice of $u$ must be right, to change everything from $x$ to $u$ : With ingenuity, some remarkable integrals are possible. But most will remain impossible forever. The functions cos $x ^ { 2 }$ and $1 / { \sqrt { 4 - \sin ^ { 2 } x } }$ have no “elementary” antiderivative. Those integrals are well defined and they come up in applications—the latter gives the distance around an ellipse. That can be computed to tremendous accuracy, but not to perfect»accuracy.



The exercises concentrate on substitutions, which needand deserve practice. We give a nonexample— $\int { ( x ^ { 2 } + 1 ) ^ { 2 } d x }$ does not equal ${ \scriptstyle { \frac { 1 } { 3 } } } ( x ^ { 2 } + 1 ) ^ { 3 }$ —to emphasize the need for $d u / d x$ : Since $2 x$ is missing, $u = x ^ { 2 } + 1$ does not work. But we can fix up $\pi$ :

$$
\int \sin { \pi x } d x = \int \sin { u { \frac { d u } { \pi } } } = - { \frac { 1 } { \pi } } \cos { u } + C = - { \frac { 1 } { \pi } } \cos { \pi x } + C .
$$