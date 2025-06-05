# 0.3 The Exponential $y = e ^ { x }$

The great function that calculus creates is the exponential $y = e ^ { x }$ : There are different ways to reach this function, and Section 6.2 of this textbook mentions five ways. Here I will describe the approach to $e ^ { x }$ that I now like best. It uses the derivative of $x ^ { n }$ ; the first thing we learn.

In all approaches, a “limiting step” will be involved. So the amazing number $e = 2 . 7 \dots$ is not seen in algebra ( $\mathbf { \boldsymbol { \mathscr { e } } }$ is not a fraction). The question is where to take that limiting step, and my answer starts with this truly remarkable fact: When $y = e ^ { x }$ is Function .1/, it is also Function .2/.

# The exponential function $y = e ^ { x }$ solves the equation ${ \frac { d y } { d x } } = y$ :

The function equals its slope. This is a first example of a differential equation— connecting an unknown function $y$ with its own derivatives. Fortunately $d y / d x = y$ is the most important differential equation—a model that other equations try to follow.

I will add one more requirement, to eliminate solutions like $y = 2 e ^ { x }$ and $y = 8 e ^ { x }$ : When $y = e ^ { x }$ solves our equation, all other functions $C e ^ { x }$ solve it too. $C = 2$ and $C = 8$ will appear on both sides of $d y / d x = y$ , and they cancel.) At $x = 0$ , $e ^ { 0 }$ will be the “zeroth power” of the positive number $e$ : All zeroth powers are 1. So we want $y = e ^ { x }$ to equal 1 when $x = 0$ :

Before solving $d y / d x = y$ , look at what this equation means. When $y$ starts from 1 at $x = 0$ , its slope is also 1. So $y$ increases. Therefore $d y / d x$ also increases, staying equal to $y$ : So $y$ increases faster. The graph gets steeper as the function climbs higher. This is what “growing exponentially” means.

# INTRODUCING $e ^ { x }$

Exponential growth is quite ordinary and reasonable. When a bank pays interest on your money, the interest is proportional to the amount you have. After the interest is added, you have more. The new interest is based on the higher amount. Your wealth is growing “geometrically,” one step at a time.

At the end of this section on $e ^ { x }$ ; I will come back to continuous compounding— interest is added at every instant instead of every year. That word “continuous” signals that we need calculus. There is a limiting step, from every year or month or day or second to every instant. You don’t get infinite interest, you do get exponentially increasing interest.

I will also describe other ways to introduce $e ^ { x }$ : This is an important question with many answers! I like equation (1) below, because we know the derivative of each power $x ^ { n }$ . If you take their derivatives in equation (1), you get back the same $e ^ { x }$ : amazing. So that sum solves $d y / d x = y$ ; starting from $y = 1$ as we wanted.

The difficulty is that the sum involves every power $x ^ { n }$ : an infinite series. When I go step by step, you will see that those powers are all needed. For this infinite series, I am asking you to believe that everything works. We can add the series to get $e ^ { x }$ ; and we can add all derivatives to see that the slope of $e ^ { x }$ is $e ^ { x }$ :

For me, the advantage of using only the powers $x ^ { n }$ is overwhelming.

I will solve $d y / d x = y$ a step at a time. At the start, $y = 1$ means that $d y / d x = 1$ :

$$
\begin{array} { r } { \begin{array} { c c c c c c } { y = 1 } \\ { d y / d x = 1 } \end{array} } & { \mathrm { ~ \mathbf { C h a n g e } ~ } y } & { d y / d x = 1 } & { \mathrm { ~ \mathbf { C h a n g e } ~ } \frac { d y } { d x } } & { y = 1 + x } \end{array}
$$

After the first change, $y = 1 + x$ has the correct derivative $d y / d x = 1$ : But then I had to change $d y / d x$ to keep it equal to $y$ : And I can’t stop there:

$$
{ \begin{array} { r c l } { y = 1 + x } & { } & { { \mathrm { U p d a t e ~ } } y { \mathrm { ~ t o ~ } } 1 + x + { \frac { 1 } { 2 } } x ^ { 2 } } & { { \mathrm { T h e n ~ u p d a t e ~ } } { \frac { d y } { d x } } { \mathrm { ~ t o ~ } } 1 + x + { \frac { 1 } { 2 } } x ^ { 2 } } \end{array} }
$$

The extra ${ \scriptstyle { \frac { 1 } { 2 } } } x ^ { 2 }$ gave the correct $x$ in the slope. Then ${ \scriptstyle { \frac { 1 } { 2 } } } x ^ { 2 }$ also had to go into $d y / d x$ , to keep it equal to $y$ : Now we need a new term with this derivative ${ \scriptstyle { \frac { 1 } { 2 } } } x ^ { 2 }$ :

The term that gives ${ \scriptstyle { \frac { 1 } { 2 } } } x ^ { 2 }$ has $x ^ { 3 }$ divided by 6: The derivative of $x ^ { n }$ is $n x ^ { n - 1 }$ , so I must divide by $n$ (to cancel correctly). Then the derivative of $x ^ { 3 } / 6$ is $3 x ^ { 2 } / 6 = \textstyle { \frac { 1 } { 2 } } x ^ { 2 }$ as we wanted. After that comes $x ^ { 4 }$ divided by 24:

$$
{ \begin{array} { r l r l } & { { \frac { x ^ { 3 } } { 6 } } = { \frac { x ^ { 3 } } { ( 3 ) ( 2 ) ( 1 ) } } } & { { \mathrm { h a s ~ s l o p e } } } & { { \frac { x ^ { 2 } } { ( 2 ) ( 1 ) } } } \\ & { { \frac { x ^ { 4 } } { 2 4 } } = { \frac { x ^ { 4 } } { ( 4 ) ( 3 ) ( 2 ) ( 1 ) } } } & { { \mathrm { h a s ~ s l o p e } } } & { { \cfrac { 4 x ^ { 3 } } { ( 4 ) ( 3 ) ( 2 ) ( 1 ) } } = { \cfrac { x ^ { 3 } } { 6 } } . } \end{array} }
$$

The pattern becomes more clear. The $x ^ { n }$ term is divided by $n$ factorial, which is $n ! =$ $( n ) ( n - 1 ) \dots ( 1 )$ : The first five factorials are 1;2;6;24;120: T he derivative of that term $x ^ { n } / n !$ is the previous term $x ^ { n - 1 } / ( n - 1 ) !$ (because the $n$ ’s cancel). As long as we don’t stop, this sum of infinitely many terms does achieve $d y / d x = y$ :

$$
y ( x ) = e ^ { x } = 1 + x + { \textstyle { \frac { 1 } { 2 } } } x ^ { 2 } + { \textstyle { \frac { 1 } { 6 } } } x ^ { 3 } + \cdots + { \textstyle { \frac { 1 } { n ! } } } x ^ { n } + \cdots
$$

If we substitute $x = 1 0$ into this series, do the infinitely many terms add to a finite number $e ^ { 1 0 }$ ? Yes. The numbers $n !$ Š grow much faster than $1 0 ^ { n }$ (or any other $x ^ { n }$ ). So the terms $x ^ { n } / n !$ in this “exponential series” become extremely small as $n \to \infty$ : Analysis shows that the sum of the series (which is $y = e ^ { x }$ ) does achieve $d y / d x = y$ :

Note 1 Let me just remember a series that you know, $1 + { \frac { 1 } { 2 } } + { \frac { 1 } { 4 } } + { \frac { 1 } { 8 } } + \cdots = 2$ : If I replace $\frac { 1 } { 2 }$ by $x$ , this becomes the geometric series $1 + x + x ^ { 2 } + x ^ { 3 } + \cdots$ and it adds up to $1 / ( 1 - x )$ : This is the most important series in mathematics, but it runs into a problem at $x = 1$ : the infinite sum $1 + 1 + 1 + 1 + \cdots$ doesn’t “converge.”

I emphasize that the series for $e ^ { x }$ is always safe, beca use the powers $x ^ { n }$ are divided by the rapidly growing numbers $n ! = n$ factorial. This is a great example to meet, long before you learn more about convergence and divergence.

Note 2 Here is another way to look at that series for $e ^ { x }$ : Start with $x ^ { n }$ and take its derivative $n$ times. First get $n x ^ { n - 1 }$ and then $n ( n - 1 ) x ^ { n - 2 }$ . Finally the nth derivative is $n ( n - 1 ) ( n - 2 ) \dots ( 1 ) x ^ { 0 }$ ; which is $n$ factorial. When we divide by that number, the nth derivative of $x ^ { n } / n !$ is equal to 1:

Now look at $e ^ { x }$ : All its derivatives are still $e ^ { x }$ : They all equal 1 at $x = 0$ : The series is matching every derivative of the function $e ^ { x }$ at the starting point $x = 0$ :

Set ${ \boldsymbol { x } } = \mathbf { 1 }$ in the exponential series. This tells us the amazing number $e ^ { 1 } = e$ :

$$
{ \begin{array} { r l r l } & { } & { { \mathrm { \mathrm { ~  ~ { ~ \cal ~ T ~ h e ~ n u m b e r ~ } ~ } } } e } & { \qquad } & { \quad e = 1 + 1 + { \frac { 1 } { 2 } } + { \frac { 1 } { 6 } } + { \frac { 1 } { 2 4 } } + { \frac { 1 } { 1 2 0 } } + \cdots } \end{array} }
$$

The first three terms add to 2.5. The first five terms almost reach 2.71. We never reach 2.72. With quite a few terms (how many ? ) you can pass 2.71828. It is certain that $e$ is not a fraction. It never appears in algebra, but it is the key number for calculus.

# MULTIPLYING BY ADDING EXPONENTS

We write $e ^ { 2 }$ in the same way that we write $3 ^ { 2 }$ : Is it true that e times e equals $e ^ { 2 } \mathopen { } \mathclose \bgroup  \mathclose \bgroup  \begin{array} { r l r l } \end{array} \aftergroup \egroup $ Up to now, $e$ and $e ^ { 2 }$ come from setting $x = 1$ and $x = 2$ in the infinite series. The wonderful fact is that for every $x$ , the series produces the “ $x$ th power of the number $e$ :” When $x = - 1$ , we get $e ^ { - 1 }$ which is $1 / e$ :

$$
\mathrm { S e t } \ x = - 1 \qquad e ^ { - 1 } = { \frac { 1 } { e } } = 1 - 1 + { \frac { 1 } { 2 } } - { \frac { 1 } { 6 } } + { \frac { 1 } { 2 4 } } - { \frac { 1 } { 1 2 0 } } + \cdots
$$

If we multiply that series for $1 / e$ by the series for $e$ , we get 1:

The best way is to go straight for all multiplications of $e ^ { x }$ times any power $e ^ { X }$ : The rule of adding exponents says that the answer is $e ^ { x + X }$ : The series must say this too! When $x = 1$ and $X = - 1$ , this rule produces $e ^ { 0 }$ from $e ^ { 1 }$ times $e ^ { - 1 }$ :

Add the exponents

$$
( e ^ { x } ) ( e ^ { X } ) = e ^ { x + X }
$$

We only know $e ^ { x }$ and $e ^ { X }$ from the infinite series. For this all-important rule, we can multiply those series and recognize the answer as the series for $\bar { e } ^ { x + X }$ : Make a start:

$$
\begin{array} { l c l } { { } } & { { \mathrm { M u l t i p l y ~ e a c h ~ t e r m } } } & { { \displaystyle e ^ { x } = { \bf 1 } + x + \frac { 1 } { 2 } x ^ { 2 } ~ + \frac { 1 } { 6 } x ^ { 3 } ~ + \cdots } } \\ { { } } & { { e ^ { x } ~ \mathrm { t i m e s } ~ e ^ { X } } } & { { \displaystyle e ^ { X } = { \bf 1 } + X + \frac { 1 } { 2 } X ^ { 2 } + \frac { 1 } { 6 } X ^ { 3 } + \cdots } } \\ { { } } & { { e ^ { x + X } } } & { { \displaystyle ( e ^ { x } ) ( e ^ { X } ) = { \bf 1 } + x + X + \frac { 1 } { 2 } x ^ { 2 } ~ + x X + \frac { 1 } { 2 } X ^ { 2 } + \cdots } } \end{array}
$$

Certainly you see $x + X$ : Do you see ${ \textstyle { \frac { 1 } { 2 } } } ( x + X ) ^ { 2 }$ in equation .4/ ? No problem:

$$
{ \frac { 1 } { 2 } } ( x + X ) ^ { 2 } = { \frac { 1 } { 2 } } ( x ^ { 2 } + 2 x X + X ^ { 2 } ) \quad { \mathrm { m a t c h e s ~ t h e ~ } } ^ { * } { \mathrm { s e c o n d ~ d e g r e e } } ^ { , \cdot } { \mathrm { t e r m s } }
$$

The step to third degree takes a little longer, but it also succeeds:

$\frac { 1 } { 6 } ( x + X ) ^ { 3 } = \frac { 1 } { 6 } x ^ { 3 } + \frac { 3 } { 6 } x ^ { 2 } X + \frac { 3 } { 6 } x X ^ { 2 } + \frac { 1 } { 6 } X ^ { 3 }$ matches the next terms in (4).

For high powers of $x + X$ we need the binomial theorem (or a healthy trust that mathematics comes out right). When $e ^ { x }$ multiplies $e ^ { X }$ , the coefficient of $x ^ { n } X ^ { m }$ will be $1 / n !$ times $1 / m !$ : Now look for that same term in the series for $e ^ { x + X }$ :

$$
{ \frac { ( x + X ) ^ { n + m } } { ( n + m ) ! } } { \mathrm { ~ i n c l u d e s ~ } } { \frac { x ^ { n } X ^ { m } } { ( n + m ) ! } } { \mathrm { ~ t i m e s ~ } } { \frac { ( n + m ) ! } { n ! m ! } } { \mathrm { ~ w h i c h ~ g i v e s ~ } } { \frac { x ^ { n } X ^ { m } } { n ! m ! } } .
$$

That binomial number $( n + m ) ! / n ! m !$ is known to successful gamblers. It counts the number of ways to choose $n$ aces out of $n + m$ aces. Out of 4 aces, you could choose 2 aces in $4 ! / 2 ! 2 ! = 6$ ways. To a mathematician, there are 6 ways to choose 2 $x$ ’s out of $x x x x$ . This number 6 will be the coefficient of $x ^ { 2 } X ^ { 2 }$ in $( x + X ) ^ { 4 }$ :

That 6 shows up in the fourth degree term. It is divided by 4! (to produce $1 / 4 )$ . When $e ^ { x }$ multiplies $e ^ { X }$ , ${ \scriptstyle { \frac { 1 } { 2 } } } x ^ { 2 }$ multiplies ${ \scriptstyle { \frac { 1 } { 2 } } } X ^ { 2 }$ (which also produces $1 / 4 { \cdot }$ ). All terms are good, but we are not going there—we accept $( e ^ { x } ) ( e ^ { X } ) = e ^ { x + X }$ as now confirmed.

Note A different way to see this rule for $( e ^ { x } ) ( e ^ { X } )$ is based on $d y / d x = y$ : Starting from $y = 1$ at $x = 0$ , follow this equation. At the point $x$ , you reach $y = e ^ { x }$ : Now go an additional distance X to arrive at exCX :

Notice that the additional part starts from $e ^ { x }$ (instead of starting from 1). That starting value $e ^ { x }$ will multiply $e ^ { X }$ in the additional part. So $e ^ { x }$ times $e ^ { X }$ must be the same as $e ^ { x + X }$ : (This is a “differential equations proof” that the exponents are added. Personally, I was happy to multiply the series and match the terms.)

The rule immediately gives $e ^ { x }$ times $e ^ { x }$ : The answer is $e ^ { x + x } = e ^ { 2 x }$ : If we multiply again by $e ^ { x }$ , we find $( e ^ { x } ) ^ { 3 }$ : This is equal to $e ^ { 2 x + x } = e ^ { 3 x }$ : We are finding a new rule for all powers $( e ^ { x } ) ^ { n } = ( e ^ { x } ) ( e ^ { x } ) \cdots ( e ^ { x } )$ :

# Multiply exponents

$$
( e ^ { x } ) ^ { n } = e ^ { n x }
$$

This is easy to see for $n = 1 , 2 , 3 , \ldots$ and then $\mathfrak { n } = - 1 , - 2 , - 3 , . . . I t$ remains true for all numbers $x$ and $n$ .

That last sentence about “all numbers” is important! Calculus cannot develop properly without working with all exponents (not just whole numbers or fractions). The infinite series (1) defines $e ^ { x }$ for every $x$ and we are on our way. Here is the graph: Function $( { \bf 1 } ) =$ Function $( 2 ) = e ^ { x } = \exp ( x )$ :

# THE EXPONENTIALS $2 ^ { x }$ AND $b ^ { x }$

We know that $2 ^ { 3 } = 8$ and $2 ^ { 4 } = 1 6$ . But what is the meaning of $2 ^ { \pi }$ ? One way to get close to that number is to replace $\pi$ by 3:14 which is 314=100: As long as we have a fraction in the exponent, we can live without calculus:

Fractional power $2 ^ { 3 1 4 / 1 0 0 } = 3 1 4 \mathrm { t h } \mathrm { p o w e r } \mathrm { o f } \mathrm { t h e } 1 0 0 \mathrm { t h } \mathrm { r o o t } 2 ^ { 1 / 1 0 0 } .$

But this is only “close” to $2 ^ { \pi }$ : And in calculus, we will want the slope of the curve $y = 2 ^ { x }$ : The good way is to connect $2 ^ { x }$ with $e ^ { x }$ ; whose slope we know (it is $e ^ { x }$ again). So we need to connect 2 with $e$ :

The key number is the logarithm of 2. This is written “ln $2 ^ { \circ }$ and it is the power of $e$ that produces 2: It is specially marked on the graph of $e ^ { x }$ :

# Natural logarithm of 2

$$
e ^ { \ln { 2 } } = 2
$$

This number $\ln 2$ is about $7 / 1 0$ . A calculator knows it with much higher accuracy.   
In the graph of $y = e ^ { x }$ , the number ln 2 on the $x$ axis produces $y = 2$ on the $y$ axis.

This is an example where we want the output $y = 2$ and we ask for the input $x = \ln 2$ : That is the opposite of knowing $x$ and asking for $y$ . “The logarithm $x = \ln { y }$ is the inverse of the exponential $y = e ^ { x }$ :” This idea will be explained in Section 4:3 and in two video lectures—inverse functions are not always simple.

Now $2 ^ { x }$ has a meaning for every $x$ : When we have the number ln 2; meeting the requirement $2 = e ^ { \ln { 2 } }$ ; we can take the $x$ th power of both sides:

# Powers of 2 from power

$$
\begin{array} { c c c } { { \textsf { s o f } e } } & { { } } & { { 2 = e ^ { \ln 2 } \quad \mathrm { a n d } \quad 2 ^ { x } = e ^ { x \ln 2 } . } } \end{array}
$$

All powers of $e$ are defined by the infinite series. The new function $2 ^ { x }$ also grows exponentially, but not as fast as $e ^ { x }$ (because 2 is smaller than $e$ ). Probably $y = 2 ^ { x }$ could have the same graph as $e ^ { x }$ , if I stretched out the $x$ axis. That stretching multiplies the slope by the constant factor ln 2: Here is the algebra:

$$
\mathrm { S l o p e \ o f \ } y = 2 ^ { x } \qquad { \frac { d } { d x } } 2 ^ { x } = { \frac { d } { d x } } e ^ { x \ln 2 } = ( \ln 2 ) e ^ { x \ln 2 } = ( \ln 2 ) 2 ^ { x } .
$$

For any positive number $b$ , the same approach leads to the function $y = b ^ { x }$ . First, find the natural logarithm $\ln b$ . This is the number (positive or negative) so that $b = e ^ { \ln b }$ . Then take the $x$ th power of both sides:

When $b$ is $e$ (the perfect choice), $\ln b = \ln e = 1$ : When $b$ is $e ^ { n }$ , then $\ln b = \ln e ^ { n } = n$ : “The logarithm is the exponent.” Thanks to the series that defines $e ^ { x }$ for every $x$ , that exponent can be any number at all.

Allow me to mention Euler’s Great Formula $e ^ { i x } = \cos x + i \sin x$ . The exponent $i x$ has become an imaginary number. (You know that $i ^ { 2 } = - 1 .$ ) If we faithfully use cos $x + i$ sin $x$ at $9 0 ^ { \circ }$ and $1 8 0 ^ { \circ }$ (where $x = \pi / 2$ and $x = \pi$ ), we arrive at these amazing facts:

Imaginary exponents

$$
e ^ { i \pi / 2 } = i \quad \mathrm { a n d } \quad e ^ { i \pi } = - 1 .
$$

Those equations are not imaginary, they come from the great series for $e ^ { x }$ :

# 0 Highlights of Calculus

# CONTINUOUS COMPOUNDING OF INTEREST

There is a different and important way to reach $e$ and $e ^ { x }$ (not by an infinite series). We solve the key equation $d y / d x = y$ in small steps. As these steps approach zero (a limit is always involved !) the small-step solution becomes the exact $y = e ^ { x }$ :

I can explain this idea in two different languages. Each step multiplies by $1 + \Delta x$ :

1. Compound interest. After each step $\Delta x$ , the interest is added to $y$ : Then the next step begins with a larger amount, and $y$ increases exponentially. 2. Finite differences. The continuous $d y / d x$ is replaced by small steps $\Delta Y / \Delta x$ :

$$
{ \frac { d y } { d x } } = y { \mathrm { ~ c h a n g e s ~ t o ~ } } { \frac { Y ( x + \Delta x ) - Y ( x ) } { \Delta x } } = Y ( x ) { \mathrm { ~ w i t h ~ } } Y ( 0 ) = 1 .
$$

This is Euler’s method of approximation. $Y ( x )$ approaches $y ( x )$ as $\Delta x  0$ .

Let me compute compound interest when 1 year is divided into 12 months, and then 365 days. The interest rate is $100 \%$ and you start with $Y ( 0 ) = \ S 1$ : If you only get interest once, at the end of the year, then you have $Y ( 1 ) = \$ 2$ :

If interest is added every month, you now get $\frac { 1 } { 1 2 }$ of $100 \%$ each time (12 times). So $Y$ is multiplied each month by $1 + { \frac { 1 } { 1 2 } }$ : (The bank adds $\scriptstyle { \frac { 1 } { 1 2 } }$ for every 1 you have.) Do this 12 times and the final value $\$ 2$ is improved to $\$ 2.61$ :

After 12 months

$$
Y ( 1 ) = \left( 1 + \frac { 1 } { 1 2 } \right) ^ { 1 2 } = \ S 2 . 6 1
$$

Now add interest every day. Y.0/ D \$1 is multiplied 365 times by 1C 615:

After 365 days

$$
Y ( 1 ) = { \bigg ( } 1 + { \frac { 1 } { 3 6 5 } } { \bigg ) } ^ { 3 6 5 } = \ S 2 . 7 1 \ ( c l o s e \ t o \ e )
$$

Very few banks use minutes, and nobody divides the year into $N = 3 1 , 5 3 6 , 0 0 0$ seconds. It would add less than a pennyÑto $\$ 2.71$ . But many bÑank8s are willing to use continuous compounding, the limit as $N \to \infty$ : After one year you have $\$ 2$ :

$$
{ \left| \begin{array} { l l l } { { \mathrm { A n o t h e r ~ l i m i t ~ g i v e s ~ } } e } & { } & { \left( 1 + { \frac { 1 } { N } } \right) ^ { N } \to e = 2 . 7 1 8 \dots { \mathrm { ~ a s ~ } } N \to \infty } \end{array} \right. }
$$

You could invest at the $100 \%$ rate for $x$ years. Now each of the $N$ steps is for $x / N$ years. Again the bank multiplies at every step by $1 + { \frac { x } { N } }$ : The 1 keeps what you have, the $x / N$ adds the interest in that step. After $N$ steps you are close to $e ^ { x }$ :

A formula for ex

$$
\begin{array} { r } { \left( 1 + \frac { x } { N } \right) ^ { N } \to e ^ { x } \mathrm { ~ a s ~ } N \to \infty } \end{array}
$$

Finally, I will change the interest rate to $a$ : Go for $x$ years at the interest rate $a$ : The differential equation changes from $d y / d x = y$ to $d y / d x = a y$ : The exponential function still solves it, but now that solution is $y = e ^ { a x }$ :

Change the rate to a

You can write down the series $e ^ { a x } = 1 + a x + { \frac { 1 } { 2 } } ( a x ) ^ { 2 } + \cdots$ and take its derivative:

$$
{ \frac { d } { d x } } ( e ^ { a x } ) = a + a ^ { 2 } x + \cdots = a ( 1 + a x + \cdots ) = a e ^ { a x }
$$

The derivative of $e ^ { a x }$ brings down the extra factor $a$ : So $y = e ^ { a x }$ solves $d y / d x = a y$ :

Looking for a function $y ( x )$ that equals its own derivative $\frac { d y } { d x }$   
A differential equation! We start at $x = 0$ with $y = 1$   
Infinite Series $y ( x ) = 1 + x + { \frac { x ^ { 2 } } { 2 ! } } + { \frac { x ^ { 3 } } { 3 ! } } + \cdots + \left( { \frac { x ^ { n } } { n ! } } \right) + \cdots$   
Take derivative ${ \frac { d y } { d x } } = 0 + 1 + x + { \frac { x ^ { 2 } } { 2 ! } } + \cdots + \left( { \frac { x ^ { n - 1 } } { ( n - 1 ) ! } } \right) + \cdots$   
Term by term $\frac { d y } { d x }$ agrees with $y$ Limit step $\ c =$ add up this series   
$n ! = ( n ) ( n - 1 ) \cdots ( 1 )$ grows much faster than $x ^ { n }$ so the terms get very small   
At $x = 1$ the number $y ( 1 )$ is called $e$ : Set $x = 1$ in the series to find $e$   
$e = 1 + 1 + { \frac { 1 } { 2 } } + { \frac { 1 } { 6 } } + { \frac { 1 } { 2 4 } } + \cdots = 2 . 7 1 8 2 8 \ldots$

GOAL Show that $y ( x )$ agrees with $e ^ { x }$ for all $x$ Series gives powers of $e$ Check that the series follows the rule to add exponents as in $e ^ { 2 } e ^ { 3 } = e ^ { 5 }$ Directly multiply series $e ^ { x }$ times $e ^ { X }$ to get $e ^ { x + X }$ $\left( 1 + x + { \frac { 1 } { 2 } } x ^ { 2 } \right)$ times $\left( 1 + X + { \frac { 1 } { 2 } } X ^ { 2 } \right)$ produces the right start for $e ^ { x + X }$ $1 + ( x + X ) + { \frac { 1 } { 2 } } ( x + X ) ^ { 2 } + \cdots$ HIGHER TERMS ALSO WORK The series gives us $e ^ { x }$ for EVERY $x$ , not just whole numbers CHECK ${ \frac { d e ^ { x } } { d x } } = \operatorname* { l i m } { \frac { e ^ { x + \Delta x } - e ^ { x } } { \Delta x } } = e ^ { x } \left( \operatorname* { l i m } { \frac { e ^ { \Delta x } - 1 } { \Delta x } } \right) = e ^ { x } { \mathrm { ~ Y E S t } }$ SECOND KEY RULE $( e ^ { x } ) ^ { n } = e ^ { n x }$ for every $x$ and $n$

Another approach to $e ^ { x }$ uses multiplication instead of an infinite sum Start with $\$ 1$ . Earn interest every day at yearly rate $x$ Multiply 365 times by 1C x  : End the year with $\mathbb { S } \left( 1 + { \frac { x } { 3 6 5 } } \right) ^ { \mathrm { i } }$ 365 Now pay $n$ times in the year. End the year with $\left( 1 + { \frac { x } { n } } \right) ^ { n } \to \ S e ^ { x }$ as $n \to \infty$ We are solving ${ \frac { \Delta Y } { \Delta x } } = Y$ in $n$ short steps $\Delta x$ : The limit solves ${ \frac { d y } { d x } } = y$ :

# 0 Highlights of Calculus

# Practice Questions

1. What is the derivative of ${ \frac { x ^ { 1 0 } } { 1 0 ! } } \ ?$ What is the derivative of ${ \frac { x ^ { 9 } } { 9 ! } } ?$

2. How to see that $\frac { x ^ { n } } { n ! }$ gets small as $n \to \infty$ ?

Start with $\frac { x } { 1 }$ $\frac { x ^ { 2 } } { 2 }$ , possibly big. But we multiply by ${ \frac { x } { 3 } } , { \frac { x } { 4 } } , \cdots$ which gets small.

3. Why is $\frac { 1 } { e ^ { x } }$ the same as $e ^ { - x }$ ? Use equation (3) and also use (6).

4. Why is $e ^ { - 1 } = 1 - 1 + { \frac { 1 } { 2 } } - { \frac { 1 } { 6 } } + \cdots$ etween $\frac 1 3$ and ${ \frac { 1 } { 2 } } \ ?$ Then $2 < e < 3$ :

5. Can you solve ${ \frac { d y } { d x } } = y$ starting from $y = 3$ at $x = 0$ ?

Why is $y = 3 e ^ { x }$ the right answer ? Notice how 3; multiplies $e ^ { x }$ :

6. Can you solve ${ \frac { d y } { d x } } = 5 y$ starting from $y = 1$ at $x = 0$ ?

Why is $y = e ^ { 5 x }$ the right answer ? Notice 5 in the exponent!

7. Why does $\frac { e ^ { \Delta x } - 1 } { \Delta x }$ approach 1 as $\Delta x$ gets smaller ? Use the $e ^ { \Delta x }$ series.

8. Draw the graph of $x = \ln y$ , just by flipping the graph of $y = e ^ { x }$ across the $4 5 ^ { \circ }$   
line $y = x$ . Remember that $y$ stays positive but $x = \ln y$ can be negative.   
9. What is the exact sum of $1 + \ln 2 + { \frac { 1 } { 2 } } ( \ln 2 ) ^ { 2 } + { \frac { 1 } { 3 ! } } ( \ln 2 ) ^ { 3 } + \cdots \cdot 2$   
10. If you replace ln 2 by 0:7; what is the sum of those four terms ?   
11. From Euler’s Great Formula $e ^ { i x } = \cos x + i$ sin $x$ ; what number is $e ^ { 2 \pi i } \geq$   
12. How close is $\left( 1 + { \frac { 1 } { 1 0 } } \right) ^ { 1 0 }$ to e ?   
13. What is the limit of $\left( 1 + { \frac { 1 } { N } } \right) ^ { 2 N }$ as $N \to \infty$ ?