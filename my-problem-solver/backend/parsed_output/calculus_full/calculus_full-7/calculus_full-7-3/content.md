# 7.3 Trigonometric Substitutions

The most power?ful tool we have, for integrating with pencil and paper and brain, is the method of substitution. To make it work, we have to think of good substitutions— which make the integral simpler. This section concentrates on the single most valuable collectionaof substitutions. They are the only ones you should memorize, and two examples aregiven imÑmediately.

To integrate $\sqrt { 1 - x ^ { 2 } }$ ; substitute $x = \sin \theta$ : Do not set $u = 1 - x ^ { 2 } \left( { \frac { d u } { d x } } { \mathrm { i s ~ m i s s i n g } } \right)$

$$
\int { \sqrt { 1 - x ^ { 2 } } } d x \to \int ( \cos \theta ) ( \cos \theta d \theta ) \qquad \int { \frac { d x } { \sqrt { 1 - x ^ { 2 } } } } \to \int { \frac { \cos \theta d \theta } { \cos \theta } }
$$

The expression $\sqrt { 1 - x ^ { 2 } }$ is awkward as a function of $x$ : It becomes graceful as a function of $\theta$ : We are practically invited to use the equation $1 - ( \sin \theta ) ^ { 2 } = ( \cos \theta ) ^ { 2 }$ : Then the square root is simply cos $\theta$ —provided this cosine is positive.

Notice the change in $d x$ . When $x$ is sin $\theta$ ; $d x$ is cos $\theta d \theta$ . Figure $7 . 4 \mathrm { a }$ shows the original area with new letters. Figure 7.4b shows an equal area, after rewriting $\int ( \cos \theta ) ( \cos \theta d \theta )$ as $\int ( \cos ^ { 2 } \theta ) d \theta$ : Changing from $x$ to $\theta$ gives a new height and a new base. There is no change in area—that is the point of substitution.

To put it bluntly: If we go from $\sqrt { 1 - x ^ { 2 } }$ to cos $\theta$ ; and forget the difference between $d x$ and $d \theta$ ; and just compute $\int \cos \theta d \theta$ ; the answer is totally wrong.

We still need the integral of $\cos ^ { 2 } \theta$ : This was Example 3 of integration by parts, and also equation 7:2:6. It is worth memorizing. The example shows this $\theta$ integral, and returns to $x$ :

EXAMPLE 1 $\textstyle \int \cos ^ { 2 } \theta d \theta = { \frac { 1 } { 2 } }$ sin $\theta$ cos $\textstyle \theta + { \frac { 1 } { 2 } } \theta$ is after substitution

We changed sin $\theta$ back to $x$ and cos $\theta$ to $\sqrt { 1 - x ^ { 2 } }$ : Notice that $\theta$ is $\sin ^ { - 1 } x$ . The answer is trickier than you might expect for the area under a circular arc. Figure 7.5 shows how the two pieces of the integral are the areas of?a pie-shaped wedge and a triangle.

# EXAMPLE 2

$$
\int { \frac { d x } { \sqrt { 1 - x ^ { 2 } } } } = \int { \frac { \cos \theta d \theta } { \cos \theta } } = \theta + C = \sin ^ { - 1 } x + C .
$$

Remember: We already know $\sin ^ { - 1 } x$ : Its derivative $1 / { \sqrt { 1 - x ^ { 2 } } }$ was computed in Section 4.4. That solves the example. But instead of matching this special problem

with a memory from Chapter 4, the substitution $x = \sin \theta$ makes the solution automatic. From $\int d \theta = \theta$ we go back to $\sin ^ { - 1 } x$ :

The rest of this section is about other substitutions. They are more complicated than $x = \sin \theta$ (but closely related). A table will display the three main choices— sin $\theta$ ; tan $\theta$ ; sec $\theta$ —and their uses.

# TRIGONOMETRIC SUBSTITUTIONS

After workingwith $\sqrt { 1 - x ^ { 2 } }$ ; the next step is $\sqrt { 4 - x ^ { 2 } }$ : The change $x = \sin \theta$ simplified the first, but it does nothing for the second: $4 - \sin ^ { 2 } \theta$ is not familiar. Nevertheless a factor of 2 makes everything work. Instead of $x = \sin \theta$ ; the idea is to substitute $x = 2 \sin \theta$ :

$$
{ \sqrt { 4 - x ^ { 2 } } } = { \sqrt { 4 - 4 \sin ^ { 2 } \theta } } = 2 \cos \theta \quad { \mathrm { a n d } } \quad d x = 2 \cos \theta d \theta .
$$

Notice both 2’s.The integral is $\scriptstyle { \mathfrak { t } } \int \cos ^ { 2 } \theta d \theta = 2 \sin \theta$ cos $\theta + 2 \theta$ : But watch closely.   
This is not 4 times the previous $\int \cos ^ { 2 } \theta d \theta ! \ : S i n c e \ : x \ : i s 2 \sin \theta , \theta$ is now $\sin ^ { - 1 } ( x / 2 )$ .

$$
\textstyle \int { \sqrt { 4 - x ^ { 2 } } } d x = 4 \int \cos ^ { 2 } \theta d \theta = x { \sqrt { 1 - ( x / 2 ) ^ { 2 } } } + 2 \sin ^ { - 1 } ( x / 2 ) .
$$

Based on $\sqrt { 1 - x ^ { 2 } }$ and $\sqrt { 4 - x ^ { 2 } }$ ; here is the general rule for $\sqrt { a ^ { 2 } - x ^ { 2 } }$ : Substitute $x = a$ sin $\theta$ : Then the $a$ ’s separate out:

$$
{ \sqrt { a ^ { 2 } - x ^ { 2 } } } = { \sqrt { a ^ { 2 } - a ^ { 2 } \sin ^ { 2 } \theta } } = a \cos \theta \quad { \mathrm { a n d } } \quad d x = a \cos \theta d \theta .
$$

That is the automatic substitution to try, whenever the square root appears.

# EXAMPLE 4

$$
\int _ { x = 0 } ^ { 4 } { \frac { d x } { \sqrt { 1 6 - x ^ { 2 } } } } = \int _ { \theta = 0 } ^ { \pi / 2 } { \frac { 4 \cos \theta d \theta } { \sqrt { 4 ^ { 2 } - 4 ^ { 2 } ( \sin \theta ) ^ { 2 } } } } = \int _ { \theta = 0 } ^ { \pi / 2 } d \theta = { \frac { \pi } { 2 } } .
$$

Here $a ^ { 2 } = 1 6$ : Then $a = 4$ and $x = 4 \sin \theta$ : The integral has $4 \cos \theta$ above and below, so it is $\textstyle \int d \theta$ : The antiderivative is just $\theta$ : For the definite integral notice that $x = 4$ means sin $\theta = 1$ ; and this means $\theta = \pi / 2$ :

A table of integrals would hide that substitution. The table only gives $\sin ^ { - 1 } ( x / 4 )$ : There is no mention of $\int d \theta = \theta$ : But what if $1 6 - x ^ { 2 }$ changes to $x ^ { 2 } - 1 6 ?$

# EXAMPLE 5

$$
\int _ { x = 4 } ^ { 8 } { \frac { d x } { \sqrt { x ^ { 2 } - 1 6 } } } = ?
$$

Notice the two changes—the sign in the square root and the limits on $x$ : Example 4 stayed inside the interval $\vert x \vert \leqslant 4$ ; where $1 6 - x ^ { 2 }$ has a square root. Example 5 stays

outside, where $x ^ { 2 } - 1 6$ has a square root. The new problem cannot use $x = 4$ sin $\theta$ ; because we don’t want the square root of $- \mathrm { c o s } ^ { 2 } \theta$ :

The new substitution is $x = 4 \sec \theta$ . This turns the square root into 4 ta?n $\theta$ :

$x = 4 \sec \theta$ gives $d x = 4$ sec  tan  d and $x ^ { 2 } - 1 6 = 1 6 \sec ^ { 2 } \theta - 1 6 = 1 6 \tan ^ { 2 } \theta .$

This substitution solves the example, when the limits are changed to $\theta$ :

$$
\int _ { 0 } ^ { \pi / 3 } { \frac { 4 \sec \theta \tan d \theta } { 4 \tan \theta } } = \int _ { 0 } ^ { \pi / 3 } \sec \theta d \theta = \ln ( \sec \theta + \tan \theta ) { \bigg ] } _ { 0 } ^ { \pi / 3 } = \ln ( 2 + { \sqrt { 3 } } ) .
$$

I want to emphasize the three steps. First came the substitution $x = 4 \sec \theta$ : An unrecognizable integral became $\int \sec \theta d \theta$ : Second came the new limits ( $\overset { \cdot } { \theta } = 0$ when $x = 4 , \theta = \pi / 3$ when $x = 8 \mathrm { \cdot }$ ). Then I integrated sec $\theta$ :

Example 6 has the same $x ^ { 2 } - 1 6$ : So the substitution is again $x = 4$ sec $\theta$ :

# EXAMPLE 6

$$
\int _ { x = 8 } ^ { \infty } { \frac { 1 6 d x } { ( x ^ { 2 } - 1 6 ) ^ { 3 / 2 } } } = \int _ { \theta = \pi / 3 } ^ { \pi / 2 } { \frac { 6 4 \sec \theta \tan \theta d \theta } { ( 4 \tan \theta ) ^ { 3 } } } = \int _ { \pi / 3 } ^ { \pi / 2 } { \frac { \cos \theta d \theta } { \sin ^ { 2 } \theta } } .
$$

Step one substitutes $x = 4 \sec \theta$ : Step two changes the limits to $\theta$ : The upper limit $x = \infty$ becomes $\theta = \pi / 2$ ; where the secant is infinite. The limit $x = 8$ again means $\theta = \pi / 3$ : To get a grip on the integral, I also changed to sines and cosines.

The integral of cos $\theta / \sin ^ { 2 } \theta$ needs another substitution! $\mathrm { \Delta O r }$ else recognize cot $\theta$ csc $\theta$ :) With $u = \sin \theta$ we have $\textstyle \int d u / u ^ { 2 } = - 1 / u = - 1 / \sin \theta$ :

Solution

$$
\int _ { \pi / 3 } ^ { \pi / 2 } { \frac { \cos \theta d \theta } { \sin ^ { 2 } \theta } } = { \frac { - 1 } { \sin \theta } } \Biggr ] _ { \pi / 3 } ^ { \pi / 2 } = - 1 + { \frac { 2 } { \sqrt { 3 } } } .
$$

Warning With lower limit $\theta = 0$ (or $x = 4$ ) this integral would be a disaster. It divides by sin»0; which is zero. This area is in»finite.

.Warning/2 Example 5 also blew up at $x = 4$ ; but the area was not infinite. To make the point directly, compare $x ^ { - 1 / 2 }$ to $x ^ { - 3 / 2 }$ : Both blow?up at $x = 0$ ; but the first one has finite area:

$$
\int _ { 0 } ^ { 1 } { \frac { 1 } { \sqrt { x } } } d x = 2 { \sqrt { x } } \int _ { 0 } ^ { 1 } = 2 \qquad \int _ { 0 } ^ { 1 } { \frac { 1 } { x ^ { 3 / 2 } } } d x = { \frac { - 2 } { \sqrt { x } } } \int _ { 0 } ^ { 1 } = \infty .
$$

Section 7.5 separates finite areas (slow growth of $1 / { \sqrt { x } } )$ from infinite areas (fast growth of x 3=2).

Last substitution Toge»the8r with $1 6 - x ^ { 2 }$ »and $x ^ { 2 } - 1 6$ comes the possibility $1 6 + x ^ { 2 }$ : (You might ask about $- 1 6 - x ^ { 2 }$ ; but for obvious reasons we don’t take its square root.) This third form $1 6 + x ^ { 2 }$ requires a third substitution $x = 4$ tan $\theta$ : Then $1 6 + x ^ { 2 } = 1 6 + 1 6 \tan ^ { 2 } \theta = 1 6 \sec ^ { 2 } \theta$ : Here is an example:

EXAMPLE 7

$$
\int _ { x = 0 } ^ { \infty } { \frac { d x } { 1 6 + x ^ { 2 } } } = \int _ { \theta = 0 } ^ { \pi / 2 } { \frac { 4 \sec ^ { 2 } \theta d \theta } { 1 6 \sec ^ { 2 } \theta } } = { \frac { 1 } { 4 } } \theta \Biggr ] _ { 0 } ^ { \pi / 2 } = { \frac { \pi } { 8 } } .
$$

Note There is a subtle difference between changing $x$ to sin $\theta$ and changing sin $\theta$ to $u$ :

in Example 1, $d x$ was replaced by cos $\theta d \theta$ (new method)

in Example 6, cos $\theta d \theta$ was already there and became $d u$ (old method):

The combination cos $\theta d \theta$ was put into the first and pulled out of the second.

My point is that Chapter 5 needed $d u / d x$ inside the integral. Then $( d u / d x ) d x$ became $d u$ : Now it is not necessary to see so far ahead. We can try any substitution. If it works, we win. In this section, $x = \sin \theta$ or sec $\theta$ or tan $\theta$ is bound to succeed.

$$
\int { \frac { d x } { 1 + x ^ { 2 } } } = \int d \theta \ \mathrm { b y } \mathrm { t r y i n g } \ x = \tan \theta \qquad \mathrm { O L D } \int { \frac { x \ d x } { 1 + x ^ { 2 } } } = \int { \frac { d u } { 2 u } } \ \mathrm { b y } \mathrm { s e e i n g } \ d u
$$

We mention the hyperbolic substitutions tanh $\theta , \sinh \theta$ ; and cosh $\theta$ : The table below shows their use. They give new forms for the same integrals. If you are familiar with hyperbolic functions the new form might look simpler—as it does in Example 8.

$$
{ \begin{array} { r l l l l l l } { x = a \operatorname { t a n h } \theta } & { { \mathrm { r e p l a c e s ~ } } } & { a ^ { 2 } - x ^ { 2 } } & { { \mathrm { b y } } } & { a ^ { 2 } { \mathrm { s e c h } } ^ { 2 } \theta } & { { \mathrm { a n d } } } & { d x } & { { \mathrm { b y } } } & { a { \mathrm { s e c h } } ^ { 2 } \theta d \theta } \\ { x = a \sinh \theta } & { { \mathrm { r e p l a c e s ~ } } } & { a ^ { 2 } + x ^ { 2 } } & { { \mathrm { b y } } } & { a ^ { 2 } { \mathrm { c o s h } } ^ { 2 } \theta } & { { \mathrm { a n d } } } & { d x } & { { \mathrm { b y } } } & { a { \mathrm { c o s h } } \theta d \theta } \\ { x = a \cosh \theta } & { { \mathrm { r e p l a c e s ~ } } } & { x ^ { 2 } - a ^ { 2 } } & { { \mathrm { b y } } } & { a ^ { 2 } { \mathrm { s i n h } } ^ { 2 } \theta } & { { \mathrm { a n d } } } & { d x } & { { \mathrm { b y } } } & { a { \mathrm { s i n h } } \theta d \theta } \end{array} }
$$

# EX?AMPLE 8

$$
\int { \frac { d x } { \sqrt { x ^ { 2 } - 1 } } } = \int { \frac { \sinh \theta d \theta } { \sinh \theta } } = \theta + C = \cosh ^ { - 1 } x + C .
$$

$\int d \theta$ is simple. The bad part is $\cosh ^ { - 1 } x$ at the end. Compare with $x = \sec \theta$ :

$$
\int { \frac { d x } { \sqrt { x ^ { 2 } - 1 } } } = \int { \frac { \sec \theta \tan \theta d \theta } { \tan \theta } } = \ln ( \sec \theta + \tan \theta ) + C = \ln ( x + { \sqrt { x ^ { 2 } - 1 } } ) + C .
$$

This way looks harder, but most tables prefer that final logarithm. It is clearer than $\cosh ^ { - 1 } { \dot { x } }$ ; even if it takes more space. All answers agree if Problem 35 is correct.

# COMPLETING THE SQUARE

We have not said what to do for $\sqrt { x ^ { 2 } - 2 x + 2 }$ or $\sqrt { - x ^ { 2 } + 2 x }$ : Those square roots contain a linear term—a multiple of $x$ : The device for removing linear terms is worth knowing. It is called completing the square, and two examples will begin to explain it:

$$
\begin{array} { c } { { x ^ { 2 } - 2 x + 2 = ( x - 1 ) ^ { 2 } + 1 = u ^ { 2 } + 1 } } \\ { { - x ^ { 2 } + 2 x = - ( x - 1 ) ^ { 2 } + 1 = 1 - u ^ { 2 } . } } \end{array}
$$

The idea has three steps. First, get the $x ^ { 2 }$ and $x$ terms into one square. Here that square was $( x - 1 ) ^ { 2 } = x ^ { 2 } - 2 x + 1$ : Sec?ond, fix up the c?onstant term. He?re we recover the original functions by adding 1: Third, set $u = x - 1$ to leave no linear term. Then the integral goes forward based on the substitutions of this section:

$$
\int { \frac { d x } { \sqrt { x ^ { 2 } - 2 x + 1 } } } = \int { \frac { d u } { \sqrt { u ^ { 2 } + 1 } } } \qquad \int { \frac { d x } { \sqrt { 2 x - x ^ { 2 } } } } = \int { \frac { d u } { \sqrt { 1 - u ^ { 2 } } } }
$$

# 7.3 Trigonometric Substitutions

The same idea applies to any quadratic that contains a linear term $2 b x$ :

$$
\begin{array} { r l r } { \mathrm { r e w r i t e } } & { } & { x ^ { 2 } + 2 b x + c \quad \mathrm { a s } \qquad ( x + b ) ^ { 2 } + C , \mathrm { w i t h } C = c - b ^ { 2 } } \\ { \mathrm { r e w r i t e } } & { } & { - x ^ { 2 } + 2 b x + c \quad \mathrm { a s } \quad - ( x - b ) ^ { 2 } + C , \mathrm { w i t h } C = c + b ^ { 2 } } \end{array}
$$

To match the quadratic with» the square, we fix u»p the constant:

$$
\begin{array} { r l } { x ^ { 2 } + 1 0 x + 1 6 = } & { { } ( x + 5 ) ^ { 2 } + C { \mathrm { ~ l e a d s ~ t o ~ } } C = 1 6 - 2 5 = - 9 } \end{array}
$$

# EXAMPLE 9

$$
\int { \frac { d x } { x ^ { 2 } + 1 0 x + 1 6 } } = \int { \frac { d x } { ( x + 5 ) ^ { 2 } - 9 } } = \int { \frac { d u } { u ^ { 2 } - 9 } } .
$$

Here $u = x + 5$ and $d u = d x$ : Now comes a choice—struggle on with $u = 3$ sec $\theta$ or look for $\textstyle \int d u / ( u ^ { 2 } - a ^ { 2 } )$ inside the front cover. Then set $a = 3$ :

$$
\int { \frac { d u } { u ^ { 2 } - 9 } } = { \frac { 1 } { 6 } } \ln \left| { \frac { u - 3 } { u + 3 } } \right| = { \frac { 1 } { 6 } } \ln \left| { \frac { x + 2 } { x + 8 } } \right| .
$$

Note If the quadrati»c starts with $5 x ^ { 2 }$ or $- 5 x ^ { 2 }$ ; factor out»the 5 first:

$$
5 x ^ { 2 } - 1 0 x + 2 5 = 5 ( x ^ { 2 } - 2 x + 5 ) = ( { \mathrm { c o m p l e t e ~ t h e ~ s q u a r e } } ) = 5 [ ( x - 1 ) ^ { 2 } + 4 ] .
$$

Now $u = x - 1$ produces $5 [ u ^ { 2 } + 4 ]$ : This is ready for table lookup or $u = 2$ tan $\theta$ :

# EXAMPLE 10

$$
\int \frac { d x } { 5 x ^ { 2 } - 1 0 x + 2 5 } = \int \frac { d u } { 5 [ u ^ { 2 } + 4 ] } = \int \frac { 2 \sec ^ { 2 } \theta d \theta } { 5 [ 4 \sec ^ { 2 } \theta ] } = \frac { 1 } { 1 0 } \int d \theta .
$$

This answer is $\theta / 1 0 + C$ : Now go backwards: $\theta / 1 0 = ( \tan ^ { - 1 } { \frac { 1 } { 2 } } u ) / 1 0 = ( \tan ^ { - 1 } { \frac { 1 } { 2 } } ( x -$ $1 ) ) / 1 0$ : Nobody could see that from the start. A double substitution takes practice, from $x$ to $u$ to $\theta$ : Then go backwards from $\theta$ to $u$ to $x$ :

Final remark For $u ^ { 2 } + a ^ { 2 }$ we substitute $u = a$ tan $\theta . \operatorname { F o r } u ^ { 2 } - a ^ { 2 }$ we substitute $u =$ $a$ sec $\theta$ : This big dividing line depends on whether the constant $C$ (after completing the square) is positive or negative. We either have $C = a ^ { 2 }$ or $C = - a ^ { 2 }$ : The same dividing line in the original $x ^ { 2 } + 2 b x + c$ is between $c > b ^ { 2 }$ and $c < b ^ { 2 }$ : In between, $c = b ^ { 2 }$ yields the perfect square $( x + b ) ^ { 2 } .$ — and no trigonometric substitution at all.