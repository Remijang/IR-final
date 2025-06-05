# 10.4 The Taylor Series for $e ^ { x }$ , sin $x$ , and cos $x$

This section goes back from numbers to functions. Instead of $\Sigma a _ { n } = s$ it deals with $\Sigma a _ { n } x ^ { n } = f ( x )$ : The sum is $\pmb { a }$ function of $x$ . The geometric series has all $a _ { n } = 1$ (including $\scriptstyle a _ { 0 }$ , the constant term) and its sum is $f ( x ) = 1 / ( 1 - x )$ : The derivatives of $1 + x + x ^ { 2 } + \cdots$ match the derivatives of $f .$ Now we choose the $a _ { n }$ differently, to match a different function.

The new function is $e ^ { x }$ : All its derivatives are $e ^ { x }$ : At $x = 0$ , this function and its derivatives equal 1: To match these 1’s, we move factorials into the denominators. Term by term the series is

$$
e ^ { x } = 1 + { \frac { x } { 1 ! } } + { \frac { x ^ { 2 } } { 2 ! } } + { \frac { x ^ { 3 } } { 3 ! } } + \cdots .
$$

$x ^ { n } / n !$ has the correct nth derivative $( = 1 )$ /: From the derivatives at $x = 0$ ; we have built back the function! At $x = 1$ the right side is $1 + 1 + { \textstyle { \frac { 1 } { 2 } } } + { \textstyle { \frac { 1 } { 6 } } } + \cdots$ and the left side is $e = 2 . 7 1 8 2 8 \dots$ : At $x = - 1$ the series gives $1 - 1 + { \textstyle { \frac { 1 } { 2 } } } - { \textstyle { \frac { 1 } { 6 } } } + \cdots$ , which is $e ^ { - 1 }$

The same term-by-term idea works for differential equations, as follows.

EXAMPLE 1 Solve $d y / d x = - y$ starting from $y = 1$ at $x = 0$ :

Solution The zeroth derivative at $x = 0$ is the function itself : $y = 1$ : Then the equation $y ^ { \prime } = - y$ gives $y ^ { \prime } = - 1$ and $y ^ { \prime \prime } { = } - y ^ { \prime } { = } + 1$ : The alternating derivatives $1 , - 1 , 1 , - 1 , \ldots$ are matched by the alternating series for $e ^ { - x }$ :

$y = 1 - x + { \textstyle { \frac { 1 } { 2 } } } x ^ { 2 } - { \textstyle { \frac { 1 } { 6 } } } x ^ { 3 } + \cdots = e ^ { - x }$ (the c2orrect solution to $y ^ { \prime } = - y \mathrm  \bar  \it $ ):

EXAMPLE 2 Solve $d ^ { 2 } y / d x ^ { 2 } = - y$ starting from $y = 1$ and $y ^ { \prime } = 0$ (the answer is cos $x$ ).

Solution The equationgives $y ^ { \prime \prime } { = } - 1$ (again at $x = 0$ ). The derivative of the equation gives $y ^ { \prime \prime \prime } { = } - y ^ { \prime } { = } 0$ : Then $y ^ { \prime \prime \prime } { = } - y ^ { \prime \prime } { = } + 1$ : The even derivatives are alternately $+ 1$ and $^ { - 1 }$ , the odd derivatives are zero. This is matched by a series of even powers, which constructs cos $x$ :

$$
y = 1 - { \frac { 1 } { 2 ! } } x ^ { 2 } + { \frac { 1 } { 4 ! } } x ^ { 4 } - { \frac { 1 } { 6 ! } } x ^ { 6 } + \cdots = \cos x .
$$

The first terms $1 - { \frac { 1 } { 2 } } x ^ { 2 }$ came earlier in the book. Now we have the whole alternating series. It converges absolutely for all $x$ , by comparison with the series for $e ^ { x }$ (odd powers are dropped). The partial sums in Figure 10.4 reach further and further before they lose touch with cos $x$ :

$$
1 \underbrace { \left[ \begin{array} { c c c } { 1 - \frac { 1 } { 2 } x ^ { 2 } + \frac { 1 } { 2 4 } x ^ { 4 } } & { \cdots } & { \int } \\ { \displaystyle \sum _ { i = 1 } ^ { \infty } \displaystyle \sum _ { 1 \leq i \leq j } 3 \int _ { i } ^ { \infty } \log _ { i } ^ { 1 } \log _ { i } ^ { 1 / 2 } } & { \cdots } \\ { 1 } & { \ddots } & { \displaystyle \sum _ { i = 1 } ^ { \infty } \sum _ { 1 = i \leq i \leq n } 3 \int _ { i } ^ { \infty } \log _ { i } ^ { 1 / 2 } } \end{array} \right] } _ { 1 } \underbrace { \left[ \begin{array} { c c c } { 1 ^ { 1 2 } } & { \cdots } & { \cdots } \\ { \vdots } & { \vdots } & { \ddots } \\ { \ddots } & { \vdots } & { \ddots } \\ { 1 } & { \ddots } & { \vdots } \end{array} \right] } _ { \left( \begin{array} { c c c } { 1 } & { \cdots } & { \displaystyle } \\ { 1 } & { \cdots } & { \displaystyle } \\ { 1 } & { \cdots } & { \displaystyle } \\ { 1 } & { \cdots } & { \displaystyle } \end{array} \right) }
$$

If we wanted plus signs instead of plus-minus, we could average $e ^ { x }$ and $e ^ { - x }$ : The differential equation for cosh $x$ is $d ^ { 2 } \bar { y } / d x ^ { 2 } = + y$ , to give plus signs:

$$
{ \frac { 1 } { 2 } } ( e ^ { x } + e ^ { - x } ) = 1 + { \frac { 1 } { 2 ! } } x ^ { 2 } + { \frac { 1 } { 4 ! } } x ^ { 4 } + { \frac { 1 } { 6 ! } } x ^ { 6 } + \cdots { \mathrm { ~ ( w h i c h ~ i s ~ c o s h ~ } } x { ) } .
$$

# TAYLOR SERIES

The idea of matching derivatives by powers is becoming central to this chapter. The derivatives are given at a basepoint (say $x = 0$ ). They are numbers $f ( 0 ) , f ^ { \prime } ( 0 ) , \ldots .$ The derivative ${ \bf \bar { \boldsymbol { f } } } ^ { ( n ) } ( 0 )$ will be the $n$ th derivative of $a _ { n } x ^ { n }$ , i8f we choose $a _ { n }$ to be $f ^ { ( n ) } ( 0 ) / n !$ Then the series $\Sigma a _ { n } x ^ { n }$ has the same derivatives at the basepoint as $f ( x )$ :

$$
f ( 0 ) + f ^ { \prime } ( 0 ) x + { \frac { 1 } { 2 } } f ^ { \prime \prime } ( 0 ) x ^ { 2 } + { \frac { 1 } { 6 } } f ^ { \prime \prime \prime } ( 0 ) x ^ { 3 } + \cdots = \sum _ { n = 0 } ^ { \infty } { \frac { f ^ { ( n ) } ( 0 ) } { n ! } } x ^ { n } .
$$

The first terms give the linear and quadratic approximations that we know well. The $x ^ { 3 }$ term was mentioned earlier (but not used). Now we have all the terms—an “infinite approximation” that is intended to equal $f ( x )$ :

Two things are needed. First, the series must converge. Second, the function must do what the series predicts, away from $x = 0$ : Those are true for $e ^ { x }$ and cos $x$ and sin $x$ ; the series equals the function. We proceed on that basis.

The Taylor series with special basepoint $x = 0$ is also called the “Maclaurin series.”

EXAMPLE 3 Find the Taylor series for $f ( x ) = \sin { x }$ around $x = 0$ :

Solution The numbers $f ^ { ( n ) } ( 0 )$ are the values of $f = \sin x$ , $f ^ { \prime } { = } \cos { x }$ , $f ^ { \prime \prime } =$ $- \sin x , \ldots$ at $x = 0$ : Those values are $0 , 1 , 0 , - 1 , 0 , 1 , \ldots$ : All even derivatives are zero. To find the coefficients in the Taylor series, divide by the factorials:

$$
\sin x = x - { \textstyle \frac { 1 } { 6 } } x ^ { 3 } + { \textstyle \frac { 1 } { 1 2 0 } } x ^ { 5 } - \cdots .
$$

EXAMPLE 4 Find the Taylor series for $f ( x ) = ( 1 + x ) ^ { 5 }$ around $x = 0$ :

Solution This function starts at $f ( 0 ) = 1$ : Its derivative is $5 ( 1 + x ) ^ { 4 }$ , so $f ^ { \prime } ( 0 ) =$ 5: The second derivative is $5 \cdot 4 \cdot ( 1 + x ) ^ { 3 }$ , so $f ^ { \prime \prime } ( 0 ) = 5 \cdot 4$ : The next three derivatives are $5 \cdot 4 \cdot 3 , 5 \cdot 4 \cdot 3 \cdot 2 , 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 . .$ After that all derivatives are zero. Therefore the Taylor series stops after the $x ^ { 5 }$ term:

$$
1 + 5 x + \frac { 5 \cdot 4 } { 2 ! } x ^ { 2 } + \frac { 5 \cdot 4 \cdot 3 } { 3 ! } x ^ { 3 } + \frac { 5 \cdot 4 \cdot 3 \cdot 2 } { 4 ! } x ^ { 4 } + \frac { 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 } { 5 ! } x ^ { 5 } .
$$

You may recognize 1, 5, 10, 10, 5, 1: They are the binomial coefficients, which appear in Pascal’s triangle (Section 2.2). By matching derivatives, we see why 0Š; 1Š; 2Š; : are needed in the denominators.

There is no doubt that $x = 0$ is the nicest basepoint. But Taylor series can be constructed around other points $x = a$ : The principle is the same—match derivatives by powers—but now the powers to use are $( x - a ) ^ { n }$ : The derivatives $f ^ { ( n ) } ( a )$ are computed at the new basepoint $x = a$ :

The Taylor series begins with $f ( a ) + f ^ { \prime } ( a ) ( x - a )$ : This is the tangent approximation at $x = a$ : The whole “2infinite approximation” is centered at a— at that point it has the same derivatives as $f ( x )$ :

$$
f ( x ) = f ( a ) + f ^ { \prime } ( a ) ( x - a ) + { \frac { 1 } { 2 } } f ^ { \prime \prime } ( a ) ( x - a ) ^ { 2 } + \cdots = \sum _ { n = 0 } ^ { \infty } { \frac { f ^ { ( n ) } ( a ) } { n ! } } ( x - a ) ^ { n } { \Bigg \} }
$$

EXAMPLE 5 Find the Taylor series for $f ( x ) = ( 1 + x ) ^ { 5 }$ around $x = a = 1$ :

Solution At $x = 1$ , the function is $( 1 + 1 ) ^ { 5 } = 3 2$ : Its first derivative $5 ( 1 + x ) ^ { 4 }$ is $5 \cdot 1 6 = 8 0$ : We compute the $n$ th derivative, divide by $n !$ , and multiply by $( x - 1 ) ^ { n }$ :

$$
3 2 + 8 0 ( x - 1 ) + 8 0 ( x - 1 ) ^ { 2 } + 4 0 ( x - 1 ) ^ { 3 } + 1 0 ( x - 1 ) ^ { 4 } + ( x - 1 ) ^ { 5 } .
$$

That Taylor series (which stops at $n = 5$ ) should agree with $( 1 + x ) ^ { 5 }$ : It does. We could rewrite $1 + x$ as $2 + ( x - 1 )$ , and take its fifth power directly. Then 32; 16; 8; 4; 2; 1 will multiply the usual coefficients $1 , 5 , 1 0 , 1 0 , 5 , 1$ to give our Taylor coefficients 32; 80; 80; 40; 10; 1: The series stops as it will stop for any polynomial—because the high derivatives are zero.

EXAMPLE 6 Find the Taylor series for $f ( x ) = e ^ { x }$ around the basepoint $x = 1$ :

Solution At $x = 1$ the function and all its derivatives equal $e$ : Therefore the Taylor series has that constant factor (note the powers of $x - 1$ , not $x$ ):

$$
e ^ { x } = e + e ( x - 1 ) + \frac { e } { 2 ! } ( x - 1 ) ^ { 2 } + \frac { e } { 3 ! } ( x - 1 ) ^ { 3 } + \cdots .
$$

# DEFINING THE FUNCTION BY ITS SERIES

Usually, we define sin $x$ and cos $x$ from the sides of a triangle. But we could start instead with the series. Define sin $x$ by equation (2). The logic goes backward, but it is still correct:

First, prove that the series converges. Second, prove properties like $( \sin x ) ^ { \prime } = \cos x .$ : Third, connect the definitions by series to the sides of a triangle.

We don’t plan to do all this. The usual definition was good enough. But note first: There is no problem with convergence. The series for sin $x$ and cos $x$ and $e ^ { x }$ all have terms $\pm x ^ { n } / n !$ : The factorials make the series converge for all $x$ : The general rule for $e ^ { x }$ times $e ^ { y }$ can be based on the series. Equation (6) is typical: $e$ is multiplied by powers of $( x - 1 )$ : Those powers add to $e ^ { x - 1 }$ : So the series proves that $e ^ { x } = e e ^ { x - 1 }$ : That is just one example of the multiplication $( e ^ { x } ) ( e ^ { y } ) = e ^ { x + y }$ :

$$
\left( 1 + x + { \frac { x ^ { 2 } } { 2 } } + . . . \right) \left( 1 + y + { \frac { y ^ { 2 } } { 2 } } + . . . \right) = 1 + x + y + { \frac { x ^ { 2 } } { 2 } } + x y + { \frac { y ^ { 2 } } { 2 } } + . . . . .
$$

Term by term, multiplication gives the series for $e ^ { x + y }$ : Term by term, differentiating the series for $e ^ { x }$ gives $e ^ { x }$ : Term by term, the derivative of sin $x$ is cos $x$ :

$$
{ \frac { d } { d x } } \left( x - { \frac { x ^ { 3 } } { 3 ! } } + { \frac { x ^ { 5 } } { 5 ! } } - \ldots \right) = 1 - { \frac { x ^ { 2 } } { 2 ! } } + { \frac { x ^ { 4 } } { 4 ! } } - \ldots .
$$

We don’t need the famous limit $( \sin x ) / x \to 1$ , by which geometry gave us the derivative. The identities of trigonometry becom?e identities of infinite series. We could even define $\pi$ as the first positive $x$ at which $x - { \textstyle \frac { 1 } { 6 } } x ^ { 3 } + \cdots$ equals zero. But it is certainly not obvious that this sine series returns to zero—much less that the point of return is near 3:14:

The function that will be defined by infinite series is $e ^ { i \theta }$ . This is the exponential of the imaginary number $i \theta$ (a multiple of $i = \sqrt { - 1 } ,$ . The result $e ^ { i \theta }$ is a complex number, and our goal is to identify it. (We will be confirming Section 9.4.) The technique is to treat $i \theta$ like all other numbers, real or complex, and simply put it into the series:

$$
e ^ { i \theta } { \mathrm { ~ i s ~ t h e ~ s u m ~ o f ~ } } 1 + ( i \theta ) + { \frac { 1 } { 2 ! } } ( i \theta ) ^ { 2 } + { \frac { 1 } { 3 ! } } ( i \theta ) ^ { 3 } + \cdots .
$$

Now use $i ^ { 2 } = - 1$ :The even powers are $i ^ { 4 } = + 1$ , $i ^ { 6 } = - 1$ , $i ^ { 8 } = + 1 , \dots$ We are just multiplying $^ { - 1 }$ by $^ { - 1 }$ to get 1: The odd powers are $i ^ { 3 } = - i$ , $i ^ { 5 } = + i , \dots$ Therefore $e ^ { i \theta }$ splits into a real part (with no $i$ ’s) and an imaginary part (multiplying $i \backslash$ ):

$$
e ^ { i \theta } = \left( 1 - \frac { 1 } { 2 ! } \theta ^ { 2 } + \frac { 1 } { 4 ! } \theta ^ { 4 } - \cdots \right) + i \left( \theta - \frac { 1 } { 3 ! } \theta ^ { 3 } + \frac { 1 } { 5 ! } \theta ^ { 5 } - \cdots \right) .
$$

You recognize those series. They are cos $\theta$ and sin $\theta$ : Therefore:

The real part is $x = \cos \theta$ and the imaginary part is $y = \sin \theta$ : Those coordinates pick out the point $e ^ { i \theta }$ in the “complex plane.” Its distance from the origin $( 0 , 0 )$ is $r = 1$ , because $( \cos \theta ) ^ { 2 } + ( \sin \theta ) ^ { \bar { 2 } } = 1$ : Its angle is $\theta$ , as shown in Figure 10.5. The number $^ { - 1 }$ is $e ^ { i \pi }$ ; at the distance $r = 1$ and the angle $\pi$ : It is on the real axis to the left of zero. If $e ^ { i \theta }$ is multiplied by $r = 2$ or $\begin{array} { r } { r = \dot { \frac { 1 } { 2 } } } \end{array}$ or any $r \geqslant 0$ , the result is a complex number at a distance $r$ from the origin:

$$
\begin{array} { r } { \begin{array} { c c c } { \ast s ; } & { r e ^ { i \theta } = r ( \cos \theta + i \sin \theta ) = r \cos \theta + i r \sin \theta = x + i y . } \end{array} } \end{array}
$$

With ei , a negative number has a logarithm. The logarithm of 1 is imaginary (it is $i \pi$ , since $e ^ { i \pi } = - 1 \$ ). A negative number also has fractional powers. The fourth root of $^ { - 1 }$ is $( - 1 ) ^ { 1 / 4 } = e ^ { i \pi / 4 }$ : More important for calculus: The derivative of $x ^ { 5 / 4 }$ is ${ \frac { 5 } { 4 } } x ^ { 1 / 4 }$ . That sounds old and familiar, but at $x = - 1$ it was never allowed.

Complex numbers tie up the loose ends left by the limitations of real numbers.

The formula $e ^ { i \theta } = \cos \theta + i$ sin $\theta$ has been called “one of the greatest mysteries of undergraduate mathematics.” Writers have used desperate methods to avoid infinite series. That proof in (10) may b e the clearest (I remember sending it to a prisoner studying calculus) but here is a way to start from $d / d x ( e ^ { i x } ) = i e ^ { i \bar { x } }$ :

$A$ different proof of Euler’s formula Any complex number is $e ^ { i x } = r ( \cos \theta +$ $i$ sin $\theta$ / for some $r$ and $\theta$ : Take the $x$ derivative of both sides, and substitute for $i e ^ { i x }$ :

$$
( \cos \theta + i \sin \theta ) d r / d x + r ( - \sin \theta + i \cos \theta ) d \theta / d x = i r ( \cos \theta + i \sin \theta ) .
$$

Comparing the real parts and also the imaginary parts, we need $d r / d x = 0$ and $d \theta / d x = 1$ : The starting values $r = 1$ and $\theta = 0$ are known from $e ^ { i 0 } = 1$ : Therefore $r$ is always 1 and $\theta$ is $x$ : Substituting into the first sentence of the proof, we have Euler’s formula $e ^ { i \theta } = 1 ( \cos \theta + i \sin \theta )$ :