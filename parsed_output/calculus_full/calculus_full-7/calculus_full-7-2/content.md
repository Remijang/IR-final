# 7.2 Trigonometric Integrals

The next section will put old integrals into new forms. For example $\textstyle \int x ^ { 2 } { \sqrt { 1 - x ^ { 2 } } } d x$ will become $\textstyle \int \sin ^ { 2 } \theta \cos ^ { 2 } \theta d \theta$ . That looks simpler because the square root is gone. But still $\sin ^ { 2 } \theta \cos ^ { 2 } \theta$ has to be integrated. This brief section integrates any product of sines and cosines and secants and tangents.

There are two methods to choose from. One uses integration by parts, the other is based on trigonometric identities. Both methods try to make the integral easy (but that may take time). We follow convention by changing the letter $\theta$ back to $x$ .

Notice that $\sin ^ { 4 } x$ cos $x d x$ is easy to integrate. It is $u ^ { 4 } d u$ :This is the goal in Exam»ple 1—to separate ou»t cos $x d x$ : It becomes $d u$ ; and sin $x$ is $u$ :

EXAMPLE 1 $\textstyle \int \sin ^ { 2 } x \cos ^ { 3 } x \ d x$ (the exponent 3 is odd)

Solution Keep cos $x d x$ as $d u$ : Convert the other $\cos ^ { 2 } x$ to $1 - \sin ^ { 2 } x$ :

$$
\int \sin ^ { 2 } x \cos ^ { 3 } x d x = \int \sin ^ { 2 } x ( 1 - \sin ^ { 2 } x ) \cos x d x = { \frac { \sin ^ { 3 } x } { 3 } } - { \frac { \sin ^ { 5 } x } { 5 } } + C .
$$

EXAMPLE 2 $\textstyle \int \sin ^ { 5 } x d x$ (the exponent 5 is odd)

Solution Keep sin $x d x$ and convert everythin gelse to cosines. The conversion is always based on $\sin ^ { 2 } x + \cos ^ { 2 } x = 1$ :

$$
\begin{array} { r } { \int ( 1 - \cos ^ { 2 } x ) ^ { 2 } \sin x d x = \int ( 1 - 2 \cos ^ { 2 } x + \cos ^ { 4 } x ) \sin x d x . } \end{array}
$$

Now cos $x$ is $u$ and $- \sin x d x$ is $d u$ : We have $\textstyle \int ( - 1 + 2 u ^ { 2 } - u ^ { 4 } ) d u$ :

General method for $\textstyle \int \sin ^ { m } x \cos ^ { n } x d x$ ; when m or n is odd

If $n$ is odd, separate out a single cos $x d x$ : That leaves an even number of cosines.

Convert them to sines. Then cos $x d x$ is $d u$ and the sines are $u$ ’s.   
If $m$ is odd, separate out a single sin $x d x$ as $d u$ : Convert the rest to cosines.   
If $m$ and $n$ are both odd, use either method.   
If $m$ and $n$ are both even, a new method is needed. Here are two examples.

EXAMPLE 3 $\textstyle \int \cos ^ { 2 } x d x \quad ( m = 0 , n = 2 , { \mathrm { b o t h ~ e v e n } } )$

There are two good ways to integrate $\cos ^ { 2 } x$ ; but substitution is not one of them. If $u$ equals cos $x$ ; then $d u$ is not here. The successful methods are integration by parts and double-angle formulas. Both answers are in equation (2) below—I don’t see either one as the obvious winner.

Integrating $\cos ^ { 2 } x$ by parts was Example 3 of Section 7.1. The other approach, by double angles, is based on these formulas from trigonometry:

$$
\begin{array} { r } { \cos ^ { 2 } x = \frac { 1 } { 2 } { \big ( } 1 + \cos 2 x { \big ) } \qquad \sin ^ { 2 } x = \frac { 1 } { 2 } { \big ( } 1 - \cos 2 x { \big ) } } \end{array}
$$

The integral of cos $2 x$ is ${ \frac { 1 } { 2 } } \sin 2 x$ : So these formulas can be integrated directly. They give the only integrals you should memorize—either the integration by parts form, or the result from these double angles:

$$
\begin{array} { r l r l } { \int \cos ^ { 2 } x d x e q u a l s } & { \frac { 1 } { 2 } \big ( x + \sin x \cos x \big ) } & { o r } & { \frac { 1 } { 2 } x + \frac { 1 } { 4 } \sin 2 x \quad \mathrm { ( p l u s ~ } C ) . } \\ { \int \sin ^ { 2 } x d x e q u a l s } & { \frac { 1 } { 2 } \big ( x - \sin x \cos x \big ) } & { o r } & { \frac { 1 } { 2 } x - \frac { 1 } { 4 } \sin 2 x \quad \mathrm { ( p l u s ~ } C ) . } \end{array}
$$

EXAMPLE 4 $\textstyle \int \cos ^ { 4 } x d x \quad ( m = 0 , n = 4 , \mathrm { b o t h a r e e v e n } )$

Changing $\cos ^ { 2 } x$ to $1 - \sin ^ { 2 } x$ gets us nowhere. All exponents stay even. Substituting $u = \sin x$ won’t simplify $\sin ^ { 4 } x d x$ ; without $d u$ : Integrate by parts or switch to $2 x$ :

First solution Integrate by parts. Take $u = \cos ^ { 3 } x$ and $d v = \cos x d x$ :

$$
\begin{array} { r } { \int ( \cos ^ { 3 } x ) ( \cos x d x ) = u v - \int v d u = \cos ^ { 3 } x \sin x - \int ( \sin x ) ( - 3 \cos ^ { 2 } x \sin x d x ) . } \end{array}
$$

The last integral has even powers $\sin ^ { 2 } x$ and $\cos ^ { 2 } x$ : This looks like no progress. Replacing $\sin ^ { 2 } x$ by $1 - \cos ^ { \hat { 2 } } x$ produces $\cos ^ { 4 } x$ on the right-hand side also:

$$
\begin{array} { r } { \int \cos ^ { 4 } x \ d x = \cos ^ { 3 } x \sin x + 3 \int \cos ^ { 2 } x ( 1 - \cos ^ { 2 } x ) d x . } \end{array}
$$

Always even powers in the integrals. But now move 3 $\int \cos ^ { 4 } x d x$ to the left side:

$$
\begin{array} { r l r } { { R e d u c t i o n } \quad } & { { } } & { 4 \int \cos ^ { 4 } x d x = \cos ^ { 3 } x \sin x + 3 \int \cos ^ { 2 } x d x . } \end{array}
$$

Partial success—the problem is reduced from $\cos ^ { 4 } x$ to $\cos ^ { 2 } x$ : Still an even power, but a lower power. The integral of $\cos ^ { 2 } x$ is already known. Use it in equation (4):

$$
\textstyle { \int } \cos ^ { 4 } x \ d x = { \frac { 1 } { 4 } } \cos ^ { 3 } x \sin x + { \frac { 3 } { 4 } } \cdot { \frac { 1 } { 2 } } { \big ( } x + \sin x \cos x { \big ) } + C .
$$

Second solution Substitute the double-angle formula $\cos ^ { 2 } x = { \frac { 1 } { 2 } } + { \frac { 1 } { 2 } }$ cos $2 x$ :

$$
\textstyle \int \cos ^ { 4 } x \ d x = \int ( { \frac { 1 } { 2 } } + { \frac { 1 } { 2 } } \cos 2 x ) ^ { 2 } d x = { \frac { 1 } { 4 } } \int ( 1 + 2 \cos 2 x + \cos ^ { 2 } 2 x ) d x .
$$

Certainly $\int d x = x . { \mathrm { A l s o ~ } } 2 \int \cos 2 x \ d x = \sin 2 x$ : That leaves the cosine squared:

$$
\begin{array} { r } { \int \cos ^ { 2 } 2 x = \int \frac { 1 } { 2 } ( 1 + \cos 4 x ) d x = \frac { 1 } { 2 } x + \frac { 1 } { 8 } \sin 4 x + C . } \end{array}
$$

The integral of $\cos ^ { 4 } x$ using double angles is

$$
\begin{array} { r } { \frac { 1 } { 4 } \left[ x + \sin 2 x + \frac { 1 } { 2 } x + \frac { 1 } { 8 } \sin 4 x \right] + C . } \end{array}
$$

That solution looks different from equation (5), but it can’t be. There all angles were $x$ ; here we have $2 x$ and $_ { 4 x }$ : We went from $\cos ^ { 4 } x$ to $\cos ^ { 2 } 2 x$ to cos $_ { 4 x }$ ; which was integrated immediately. The powers were cut in half as the angle was doubled.

Double-angle method for $\textstyle \int \sin ^ { m } x \cos ^ { n } x \ d x$ ; when m and n are even:

Replace $\sin ^ { 2 } x$ by $\scriptstyle { \frac { 1 } { 2 } } ( 1 - \cos 2 x )$ and $\cos ^ { 2 } x$ by $\scriptstyle { \frac { 1 } { 2 } } ( 1 + \cos 2 x )$ : The exponents drop to $m / 2$ and $n / 2$ : If those are even, repeat the idea ( $2 x$ goes to $4 x$ ). If $m / 2$ or $n / 2$ is odd, switch to the “general method” using substitution. With an odd power, we have $d u$ :

EXAMPLE 5 (Double angle) $\begin{array} { r l } { \small } & { { } \int \sin ^ { 2 } x \cos ^ { 2 } x \ d x = \int \frac { 1 } { 4 } ( 1 - \cos 2 x ) ( 1 + \cos 2 x ) d x . } \end{array}$

This leaves $1 - \cos ^ { 2 } 2 x$ in the last integral. That is familiar but not necessarily easy. We can look it up (safest) or remember it (quickest) or use double angles again:

$$
{ \frac { 1 } { 4 } } \int ( 1 - \cos ^ { 2 } 2 x ) d x = { \frac { 1 } { 4 } } \int \left( 1 - { \frac { 1 } { 2 } } - { \frac { 1 } { 2 } } \cos 4 x \right) d x = { \frac { x } { 8 } } - { \frac { \sin 4 x } { 3 2 } } + C .
$$

Conclusion Every $\sin ^ { m } x \cos ^ { n } x$ can be integrated. This includes negative $m$ and $n$ — see tangents and secants below. Symbolic codes like MACSYMA or Mathematica give the answer directly. Do they use double angles or integration by parts ?

You may prefer the answer from integration by parts (I usually do). It avoids $2 x$ and $_ { 4 x }$ : But it makes no sense to go through every step every time. Either a computer does the algebra, or we use a “reduction formula” from $n$ to $n - 2$ :

$$
n \int \cos ^ { n } x \ d x = \cos ^ { n - 1 } x \ \sin x + ( n - 1 ) \int \cos ^ { n - 2 } x \ d x .
$$

For $n = 2$ this is $\int \cos ^ { 2 } x \ d x$ —the integral to learn. For $n = 4$ the reduction produces $\cos ^ { 2 } x$ : The integral of $\cos ^ { 6 } x$ goes to $\cos ^ { 4 } x$ : There are similar reduction formulas for $\sin ^ { m } x$ and also for $\sin ^ { m } x \cos ^ { n } x$ : I don’t see a good reason to memorize them.

# INTEGRALS WITH ANGLES px AND qx

Instead of $\sin ^ { 8 } x$ times $\cos ^ { 6 } x$ ; suppose you have sin $8 x$ times cos $6 x$ : How do you integrate ? Separately a sine and cosine are easy. The new question is the integral of the product:

EXAMPLE 6 Find $\int _ { 0 } ^ { 2 \pi }$ sin 8x cos 6x dx: More generally find $\int _ { 0 } ^ { 2 \pi }$ sin $p x$ cos $q x d x$

This is not for the sake of making up new problems. I believe these are the most important definite integrals in this chapter ( $p$ and $q$ are $0 , 1 , 2 , \ldots )$ . They may be the most important in all of mathematics, especially because the question has such a beautiful answer. The integrals are zero. On that fact rests the success of Fourier series, and the whole industry of signal processing.

One approach (the slow way) is to replace sin $8 x$ and cos $6 x$ by powers of cosines. That involves $\cos ^ { 1 4 } x$ : The integration is not fun. A better approach, which applies to all angles $p x$ and $q x$ ; is to use the identity

$$
\begin{array} { r } { \sin p x \cos q x = \frac { 1 } { 2 } \sin ( p + q ) x + \frac { 1 } { 2 } \sin ( p - q ) x . } \end{array}
$$

Thus sin $8 x$ cos $6 x = { \textstyle { \frac { 1 } { 2 } } } \sin 1 4 x + { \textstyle { \frac { 1 } { 2 } } } \sin 2 x$ : Separated like that, sines are easy to integrate:

$$
\int _ { 0 } ^ { 2 \pi } \sin { 8 x } \cos { 6 x } d x = \left[ - { \frac { 1 } { 2 } } { \frac { \cos { 1 4 x } } { 1 4 } } - { \frac { 1 } { 2 } } { \frac { \cos { 2 x } } { 2 } } \right] _ { 0 } ^ { 2 \pi } = 0 .
$$

Since cos $1 4 x$ is periodic, it has the same value at 0 and $2 \pi$ : Subtraction gives zero. The same is true for cos $2 x$ : The integral of sine times cosine is always zero over a complete period (like 0 to $2 \pi$ ).

What about sin $p x \sin q x$ and cos $p x$ cos $q x$ ? Their integrals are also zero, provided $p$ is different from $q$ . When $p = q$ we have a perfect square. There is no negative area to cancel the positive area. The integral of $\bar { \cos ^ { 2 } p x }$ or $\sin ^ { 2 } p x$ is $\pi$ :

# EXAMPLE 7

$$
\begin{array} { r } { \int _ { 0 } ^ { 2 \pi } \sin 8 x \sin 7 x \ d x = 0 \ \quad \mathrm { a n d } \quad \int _ { 0 } ^ { 2 \pi } \sin ^ { 2 } 8 x \ d x = \pi . } \end{array}
$$

With two sines or two cosines (instead of sine times cosine), we go back to the addition formulas of Section 1.5. Problem 24 derives these formulas:

$$
\begin{array} { r l } { \sin p x \sin q x = - \frac { 1 } { 2 } \cos ( p + q ) x + \frac { 1 } { 2 } \cos ( p - q ) x } & { } \\ { \cos p x \cos q x = } & { \frac { 1 } { 2 } \cos ( p + q ) x + \frac { 1 } { 2 } \cos ( p - q ) x . } \end{array}
$$

With $p = 8$ and $q = 7$ ; we get cos $1 5 x$ and cos $x$ : Their definite integrals are zero. With $p = 8$ and $q = 8$ ; we get cos $1 6 x$ and cos $0 x$ (which is 1). Formulas (9) and (10)

also give a factor $\frac { 1 } { 2 }$ : The integral of $\frac { 1 } { 2 }$ is $\pi$ :

$$
{ \begin{array} { r l } & { \int _ { 0 } ^ { 2 \pi } \sin 8 x \sin 7 x \ d x = - { \frac { 1 } { 2 } } \int _ { 0 } ^ { 2 \pi } \cos 1 5 x \ d x + { \frac { 1 } { 2 } } \int _ { 0 } ^ { 2 \pi } \cos \ x \ d x = 0 + 0 } \\ & { \int _ { 0 } ^ { 2 \pi } \sin 8 x \sin 8 x \ d x = - { \frac { 1 } { 2 } } \int _ { 0 } ^ { 2 \pi } \cos 1 6 x \ d x + { \frac { 1 } { 2 } } \int _ { 0 } ^ { 2 \pi } \cos 0 x \ d x = 0 + \pi } \end{array} }
$$

The answer zero is memorable. The answer $\pi$ appears constantly in Fourier series. No ordinary numbers are seen in these integrals. The case $p = q = 1$ brings back $\textstyle \int \cos ^ { 2 } x \ d \dot { x } = { \frac { 1 } { 2 } } + { \frac { 1 } { 4 } } \sin 2 x$ :

# SECANTS AND TANGENTS

When we allow negative powers $m$ |and $n$ ;|the main fact remains true. All integrals $\textstyle \int \sin ^ { m } x \cos ^ { n } x \ d x$ can be expressed by known functions. The novelty for negative powers is that logarithms appear. That happens right at the start, for sin $. { \boldsymbol { x } } / \cos { x }$ and for $1 / \cos x$ (tangent and secant):

$$
\begin{array} { r l r } { \int \tan x \ d x = - \int d u / u = - \ln { \left| \cos x \right| } } & { \mathrm { ( h e r e ~ } u = \cos x \ ) } \\ { \int \sec x \ d x = } & { \int d u / u = } & { \ln { \left| \sec x + \tan x \right| } } & { \mathrm { ( h e r e ~ } u = \sec x + \tan x \ ) . } \end{array}
$$

For higher powers there is one key identity: $1 + \tan ^ { 2 } x = \sec ^ { 2 } x$ : That is the old identity $\mathrm { \bar { c o s } } ^ { 2 } x + \mathrm { s i n } ^ { 2 } x = 1$ in disguise (just divide by $\cos ^ { 2 } x$ ). We switch tangents to secants just as we switched sines to cosines. Since $( \tan x ) ^ { \prime } { = } \sec ^ { 2 } x$ and $( \sec x ) ^ { \prime } =$ sec $x$ tan $x$ ; nothing else comes in.

$$
\begin{array} { r l } & { \int \tan ^ { 2 } x \ d x = \int ( \sec ^ { 2 } x - 1 ) d x = \tan x - x + C . } \\ & { \int \tan ^ { 3 } x \ d x = \int \tan x ( \sec ^ { 2 } x - 1 ) d x . } \end{array}
$$

EXAMPLE 9

The first integral on the right is $\textstyle \int u \ d u = { \frac { 1 } { 2 } } u ^ { 2 }$ ; with $u = \tan x$ : The last integral is $- \int \tan x d x$ : The complete answer is $\scriptstyle { \frac { 1 } { 2 } } ( \tan x ) ^ { 2 } + \ln | \cos x | + C$ : By taking absolute values, a negative cosine is also allowed. Avoid cos $x = 0$ :

$$
\int ( \tan x ) ^ { m } d x = { \frac { ( \tan x ) ^ { m - 1 } } { m - 1 } } - \int ( \tan x ) ^ { m - 2 } d x
$$

Same idea—separate off .tan $x ) ^ { 2 }$ as $\sec ^ { 2 } x - 1$ : Then integrate $( \tan x ) ^ { m - 2 } \sec ^ { 2 } x \ d x$ ; which is ${ u ^ { m - 2 } d u }$ : This leaves the integral on the right, with the exponent lowered by 2: Every power .tan $x ) ^ { m }$ is eventually reduced to Example 8 or 9.

EXAMPLE 11 $\textstyle \int \sec ^ { 3 } x \ d x = u v - \int v d u = \sec x \tan x - \int \tan ^ { 2 } x \sec x \ d x$

This was integration by parts, with $u = \sec x$ and $v = \tan x$ : In the integral on the right, replace tan $^ 2 x$ by $\sec ^ { 2 } x - 1$ (this identity is basic):

$$
\textstyle \int \sec ^ { 3 } x \ d x = \sec x \tan x - \int \sec ^ { 3 } x \ d x + \int \sec x \ d x .
$$

Bring $\int \sec ^ { 3 } x \ d x$ to the left side. That reduces theproblem from $\sec ^ { 3 } x$ to sec $x$ :

I believe those examples make the point—trigonometric integrals are computable. Every product t $\mathfrak { u } ^ { m } x \sec ^ { n } x$ can be reduced to one of these examples. If $n$ is even we substitute $u = \tan x$ : If $m$ is odd we set $u = \sec x$ : If $m$ is even and $n$ is odd, use a reduction formula (and always use $\tan ^ { 2 } x = \sec ^ { 2 } x - 1 .$ )

# 7 Techniques of Integration

I mention very briefly a completely different substitution $\begin{array} { r } { u = \tan { \frac { 1 } { 2 } } x } \end{array}$ : This seems to all students and instructors (quite correctly) to come out of the blue:

$$
\sin x = { \frac { 2 u } { 1 + u ^ { 2 } } } \qquad { \mathrm { a n d } } \qquad \cos x = { \frac { 1 - u ^ { 2 } } { 1 + u ^ { 2 } } } \qquad { \mathrm { a n d } } \qquad d x = { \frac { 2 d u } { 1 + u ^ { 2 } } } .
$$

The $x$ -integral can involve sums as well as products—not only $\sin ^ { m } x \cos ^ { n } x$ but also $1 / ( 5 + \sin x - \tan x )$ : (No square roots.) The $u$ -integral is a ratio of ordinary polynomials. It is done by partial fractions.

# Application of r sec x dx to distance on a map (Mercator projection)

The strange integral $\ln ( \sec x + \tan x )$ has an everyday application. It measures the distance from the equator to latitude $x$ ; on a Mercator map of the world.

All mapmakers face the impossibility of putting part of a sphere onto a flat page. You can’t preserve distances, when an orange peel is flattened. But angles can be preserved, and Mercator found a way to do it. His map came before Newton and Leibniz. Amazingly, and accidentally, somebody matched distances on the map with a table of logarithms—and discovered $\int \sec { x } d x$ before calculus. You would not be surprised to meet sin $x$ ; but who would recognize $\ln ( \sec x + \tan x )$ ?

The map starts with strips at all latitudes $x$ : The heights are $d x$ ; the lengths are proportional to $\cos x$ : We stretch the strips by $1 / \cos x$ —then Figure 7.3c lines up evenly on the page. When $d x$ is also divided by cos $x$ ; angles are preserved—a small square becomes a bigger square. The distance north adds up the strip heights $d x / \cos x$ : This gives $\int \sec { x } d x$ :



The distance to the North Pole is infinite! Close to the Pole, maps are stretched totally out of shape. When sailors wanted to go from $A$ to $B$ at a constant angle with the North Star, they looked on Mercator’s map to find the angle.