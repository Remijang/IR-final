# 4.4 Inverses of Trigonometric Functions

Mathematics is built on basic functions like the sine, and on basic ideas like the inverse. Therefore $\dot { \pmb { u } }$ is totally natural to invert the sine function. The graph of $x = \sin ^ { - 1 } y$ is a mirror image of $y = \sin x$ : This is a case where we pay close attention to the domains, since the sine goes up and down infinitely often. We only want one piece of that curve, in Figure 4.9.

For the bold line the domain is restricted. The angle $x$ lies between $- \pi / 2$ and $+ \pi / 2$ . On that interval the sine is increasing, so each $y$ comes from exactly one angle $x$ . If the whole sine curve is allowed, infinitely many angles would have sin $x = 0$ : The sine function could not have an inverse. By restricting to an interval where sin $x$ is increasing, we make the function invertible.

$$
\begin{array} { r l } { \frac { \left[ \mathbf { y } = \sin x \right] } { 2 } } & { \frac { \left[ x = \sin ^ { - 1 } y \right] } { x ^ { 0 } } } \\ { \cdot \underbrace { \mathbf { y } = 1 } _ { \begin{array} { c } { \mathrm { 1 } } \\ { \mathrm { 2 } } \\ { \mathrm { 3 } } \\ { \mathrm { 4 } } \\ { \mathrm { 5 } } \\ { \mathrm { 6 } } \end{array} } \cdot \frac { \frac { d y } { d x } = 0 } { \frac { d x } { d x } } } & { \frac { \pi } { \sqrt { 6 } } \left[ \underbrace { \sum _ { i = 1 } ^ { d } \cos ^ { - 1 } \frac { 1 } { \sqrt { 1 - y ^ { 2 } } } } _ { \begin{array} { c } { \mathrm { 2 } } \\ { \mathrm { 4 } } \\ { \mathrm { 5 } } \\ { \mathrm { 6 } } \end{array} } \right] _ { \begin{array} { c } { \frac { 1 } { 6 } } \\ { \frac { \pi } { 2 } } \\ { \mathrm { 6 } } \end{array} } \times \frac { \left[ \begin{array} { c } { \frac { x } { 2 } } \\ { \frac { \pi } { 2 } } \\ { \frac { \pi } { 2 } } \end{array} \right] } { \left[ \begin{array} { c } { \frac { 1 } { 2 } } \\ { \frac { \pi } { 2 } } \end{array} \right] ^ { \frac { 1 } { 1 } } } + \sum _ { \begin{array} { c } { \mathrm { 3 } } \\ { \mathrm { 4 } } \\ { \mathrm { 5 } } \end{array} } \times \left[ \begin{array} { c } { \frac { 1 } { \sqrt { 1 - y ^ { 2 } } } } \\ { \frac { \pi } { 2 } } \\ { \frac { \pi } { 2 } } \end{array} \right] _ { \begin{array} { c } { \frac { \pi } { 2 } } \\ { \frac { \pi } { 2 } } \end{array} } } \end{array}
$$

The inverse function brings $y$ back to $x$ : It is $x = \sin ^ { - 1 } y$ (theinverse sine):

$$
x = \sin ^ { - 1 } y { \mathrm { ~ w h e n ~ } } y = \sin x { \mathrm { ~ a n d ~ } } | x | \leqslant \pi / 2 .
$$

The inverse starts with a number $y$ between $^ { - 1 }$ and 1: It produces an angle $x =$ $\sin ^ { - 1 } y$ —the angle whose sine is $y$ . The angle $x$ is between $- \pi / 2$ and $\pi / 2$ , with the required sine. Historically $x$ was called the “arc sine” of $y$ , and arcsin is used in computing. The mathematical notation is $\sin ^ { - 1 }$ : This has nothing to do with $1 / \sin x$ .

The figure shows the $3 0 ^ { \circ }$ angl¤e $x = \pi / 6$ : Its sine is $\begin{array} { r } { y = \frac { 1 } { 2 } } \end{array}$ : The invers¤e sin¤e of $\frac { 1 } { 2 }$ is $\pi / 6$ . Again: The symbol $\sin ^ { - 1 } ( 1 )$ stands for the angle whose sine is 1 (this angle is $x = \pi / 2 )$ ). We are seeing $g ^ { - 1 } ( g ( x ) ) = x$ :

$$
\sin ^ { - 1 } ( \sin x ) = x { \mathrm { ~ f o r ~ } } - { \frac { \pi } { 2 } } \leqslant x \leqslant { \frac { \pi } { 2 } } \qquad \sin ( \sin ^ { - 1 } y ) = y { \mathrm { ~ f o r ~ } } - 1 \leqslant y \leqslant 1 .
$$

EXAMPLE 1 (important) If sin $x = y$ find a formula for cos $x$ :

Solution We are given the sine, we want the cosine. The key to this problem must be $\cos ^ { 2 } x = 1 - \sin ^ { 2 } x$ : When the sine is $y$ , the cosine is the square root of $1 - y ^ { 2 }$ :

$$
\cos x = \cos ( \sin ^ { - 1 } y ) = { \sqrt { 1 - y ^ { 2 } } } .
$$

This formula is crucial for computing derivatives. We use it immediately.

# 4 Derivatives by the Chain Rule

# THE DERIVATIVE OF THE INVERSE SINE

The calculus problem is to find the slope of the inverse functioan $f ( y ) = \sin ^ { - 1 } y$ The chain rule gives (slope of inverse function) $= 1$ =(slope of original function). Certainly the slope of sin $x$ is cos $x$ : To switch from $x$ to $y$ , use equation (2):

$$
y = \sin x \mathrm { \mathrm { ~ g i v e s ~ } } { \frac { d y } { d x } } = \cos x \mathrm { \mathrm { ~ s o ~ t h a t ~ } } { \frac { d x } { d y } } = { \frac { 1 } { \cos x } } = { \frac { 1 } { \sqrt { 1 - y ^ { 2 } } } } .
$$

This derivative $1 / \sqrt { 1 - y ^ { 2 } }$ gives a new $\scriptstyle \nu - f$ pair that is extremely valuable in calculus:

$$
\begin{array} { r l r l } { \nu e l o c i t y } & { { } v ( t ) = 1 / \sqrt { 1 - t ^ { 2 } } } & { } & { { } d i s t a n c e \quad f ( t ) = \sin ^ { - 1 } t . } \end{array}
$$

Inverse functions will soon produce two more pairs, from the derivatives of $\tan ^ { - 1 } y$ and $\sec ^ { - 1 } y$ : The table at the end lists all the essential facts.

EXAMPLE 2 The slope of $\sin ^ { - 1 } y$ at $y = 1$ is infinite: $1 / { \sqrt { 1 - y ^ { 2 } } } = 1 / 0 .$ : Explain.

At $y = 1$ the graph of $y = \sin x$ is horizontal. The slope is zero. So its mirror image is vertical. The slope $1 / 0$ is an extreme case of the chain rule.

Question What is $d / d x ( \sin ^ { - 1 } x ) ?$ Answer $1 / { \sqrt { 1 - x ^ { 2 } } }$ : I just changed letters.

# THE INVERSE COSINE AND ITS DERIVATIVE

Whatever is done for thesine can be done for the cosine. But the domain and range have to be watched. The graph cannot be allowed to go up and down. Each $y$ from $^ { - 1 }$ to 1 should be the cosine of only one angle $x$ : That puts $x$ between 0 and $\pi$ : Then the cosine is steadily decreasing and $y = \cos x $ has an inverse:

$$
\cos ^ { - 1 } ( \cos x ) = x { \mathrm { ~ a n d ~ } } \cos ( \cos ^ { - 1 } y ) = y .
$$

The cosine of the angle $x = 0$ is the number $y = 1$ : The inverse cosine of $y = 1$ is the angle $x = 0$ : Those both expressthe same fact, that cos $0 = 1$ :

For the slope of $\cos ^ { - 1 } y$ , we could copy the calculation that succeeded for $\sin ^ { - 1 } y$ : The chain rule could be applied as in (3). But there is a faster way, because of a special relation between cos $^ { - 1 } y$ and $\sin ^ { - 1 } y$ : Those angles always add to a right angle:

$$
\cos ^ { - 1 } y + \sin ^ { - 1 } y = \pi / 2 .
$$

Figure $4 . 9 \mathrm { c }$ shows the angles and Figure 4.10c shows the graphs. The sum is $\pi / 2$ (the dotted line), and its derivative is zero. So the derivatives of $\cos ^ { - 1 } \boldsymbol { y }$ and $\sin ^ { - 1 } y$ must add to zero. Those derivatives have opposite sign. There is a minus for the inverse cosine, and its graph goes downward:

$$
\textit { \textbf { f } } x = \cos ^ { - 1 } y \quad i s \quad d x / d y = - 1 / \sqrt { 1 - y ^ { 2 } } .
$$

Question How can two functions $x = \sin ^ { - 1 } y$ and $x = - \cos ^ { - 1 } y$ have the same derivative? Answer $\sin ^ { - 1 } y$ must be the same as $- \mathrm { c o s } ^ { - 1 } y + C$ : Equation (5) gives $C = \pi / 2$ :

# THEINVER SE TANGENT AND ITS DERIVATIVE

The tangent is sin $x / \cos x$ : The inverse tangent is not $\sin ^ { - 1 } y / \cos ^ { - 1 } y$ : The inverse function produces the angle whose tangent is $y$ : Figure 4.11 shows that angle, which is between $- \pi / 2$ and $\pi / 2$ : The tangent can be any number, but the inverse tangent is in the open interval $- \pi / 2 < x < \pi / 2$ : (The interval is “open” because its endpoints are not included.) The tangents of $\pi / 2$ and $- \pi / 2$ are not defined.

The slope of $y = \tan x$ is $d y / d x = \sec ^ { 2 } x$ : What is the slope of $x = \tan ^ { - 1 } y \ i$ $\pi / 4$ the secant squared equals 2: The slopes $\begin{array} { r } { d x / d y = \frac { 1 } { 2 } } \end{array}$ and $d y / d x = 2$ multiply to give 1:



Important Soon will come the following question. What function has the derivative $1 / ( 1 + x ^ { 2 } ) \ ?$ One reason for reading this section is to learn the answer. The function is in equation (8)—if we change letters. It is $f ( x ) = \tan ^ { - 1 } x$ that has slope $1 / ( 1 + x ^ { 2 } )$ .

# INVERSE COTANGENT, INVERSE SECANT, INVERSE COSECANT

There is no way we can avoid completing this miserable list! But it can be painless. The idea is to use $1 / ( d y / d x )$ for $y = \cot x$ and $y = \sec x$ and $y = \csc x$ :

$$
{ \frac { d x } { d y } } = { \frac { - 1 } { \csc ^ { 2 } x } } \quad { \mathrm { a n d } } \quad { \frac { d x } { d y } } = { \frac { 1 } { \sec x \tan x } } \quad { \mathrm { a n d } } \quad { \frac { d x } { d y } } = { \frac { - 1 } { \csc x \cot x } } .
$$

In the middle equation, replace sec $x$ bay $y$ and tan $x$ by $\pm { \sqrt { y ^ { 2 } - 1 } }$ : Cahoose the sign for positive slope (compare Figure| 4|.11). That gives the middle eq|ua|tion in(10):

The derivatives of $\cot ^ { - 1 } y$ and $\sec ^ { - 1 } y$ and $\csc ^ { - 1 } { y }$ are

$$
{ \frac { d } { d y } } ( \cot ^ { - 1 } y ) = { \frac { - 1 } { 1 + y ^ { 2 } } } \quad { \frac { d } { d y } } ( \sec ^ { - 1 } y ) = { \frac { 1 } { | y | \sqrt { y ^ { 2 } - 1 } } } \quad { \frac { d } { d y } } ( \csc ^ { - 1 } y ) = { \frac { - 1 } { | y | \sqrt { y ^ { 2 } - 1 } } } .
$$

Note about the inverse secant When $y$ is negative there is a choice for $\boldsymbol { x } = \sec ^ { - 1 } \boldsymbol { y }$ : We selected the angle inthe second quadrant (between $\pi / 2$ and $\pi$ ). Its cosine is negative, so its secant is negative. This choice makes $\sec ^ { - 1 } y = \cos ^ { - 1 } ( 1 / y )$ , which matches sec $x = 1 / \cos x$ : It also makes $\sec ^ { - 1 } y$ an increasing function, where $\cos ^ { - 1 } y$ is a decreasing function. So we needed the absolute value $| y |$ in the derivative.

Some mathematical tables make a different choice. The angle $x$ could be in the third quadrant (between $- \pi$ and $- \pi / 2 )$ ). Then the slope omits the absolute value.

Summary For the six inverse functions it is only necessary to learn three derivatives. The other three just have minus signs, as we saw for $\sin ^ { - 1 } y$ and $\cos ^ { - 1 } y$ : Each inverse function and its “cofunction” add to $\pi / 2$ , so their derivatives add to zero. Here are the six functio|ns| f¤or quick reference, with the threeanew derivatives.

$$
\begin{array} { r l r l r } & { f u n c t i o n f ( y ) } & { i n p u t s ~ y } & { o u t p u t s ~ x } & { s l o p e d x / d y ~ } \\ & { \sin ^ { - 1 } y , \cos ^ { - 1 } y } & { \left| y \right| \leqslant 1 } & { \left[ - \displaystyle \frac { \pi } { 2 } , \displaystyle \frac { \pi } { 2 } \right] , \left[ 0 , \pi \right] } & { \pm \displaystyle \frac { 1 } { \sqrt { 1 - y ^ { 2 } } } } \\ & { \tan ^ { - 1 } y , \cot ^ { - 1 } y } & { \mathrm { a l l ~ } y } & { \left( - \displaystyle \frac { \pi } { 2 } , \displaystyle \frac { \pi } { 2 } \right) , \left( 0 , \pi \right) } & { \pm \displaystyle \frac { 1 } { 1 + y ^ { 2 } } } \\ & { \sec ^ { - 1 } y , \csc ^ { - 1 } y } & { \left| y \right| \geqslant 1 } & { \left[ 0 , \pi \right] ^ { * } , \left[ - \displaystyle \frac { \pi } { 2 } , \displaystyle \frac { \pi } { 2 } \right] ^ { * } } & { \pm \displaystyle \frac { 1 } { \left| y \right| \sqrt { y ^ { 2 } - 1 } } } \end{array}
$$

# 4.4 Inverses of Trigonometric Functions

If $y = \cos x $ or $y = \sin x$ then $\left| y \right| \leqslant 1$ : For $y = \sec x$ and $y = \csc x$ the opposite is true; we must have $\left| y \right| \geqslant 1$ : The graph of $\sec ^ { - 1 } y$ misses all the points $- 1 < y < 1$ : Also, that graph misses $x = \pi / 2$ —where the cosine is zero. The secant of $\pi / 2$ would be $1 / 0$ (impossible). Similarly $\mathbf { c s c } ^ { - 1 } \boldsymbol { y }$ misses $x = 0$ , because $y = \csc 0$ cannot be $1 / \sin 0$ : The asterisks in the table are to remove those points $x = \pi / 2$ and $x = 0$ :

The column of derivatives is what we need and use in calculus.