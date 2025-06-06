# 10.1 The Geometric Series

We begin by looking at both sides of the geometric series:

$$
1 + x + x ^ { 2 } + x ^ { 3 } + \cdots = { \frac { 1 } { 1 - x } } .
$$

How does the series on the left produce the function on the right ? How does $1 / ( 1 -$ $x$ / produce the series ? Add up two terms of the series, then three terms, then $n$ terms:

$$
1 + x = { \frac { 1 - x ^ { 2 } } { 1 - x } } \quad 1 + x + x ^ { 2 } = { \frac { 1 - x ^ { 3 } } { 1 - x } } \quad 1 + \cdots + x ^ { n - 1 } = { \frac { 1 - x ^ { n } } { 1 - x } } .
$$

For the first, $1 + x$ times $_ { 1 - x }$ equals $1 - x ^ { 2 }$ by ordinary algebra. The second begins to make the point: $1 + x + x ^ { 2 }$ times $_ { 1 - x }$ gives $1 - x + x - x ^ { 2 } + x ^ { 2 } - x ^ { 3 }$ . Between 1 at the start and $- x ^ { 3 }$ at the end, everything cancels. The same happens in all cases: $1 + \cdots + x ^ { n - 1 }$ times $_ { 1 - x }$ leaves 1 at the start and $- x ^ { n }$ at the end. This proves equation (2)—the sum of $n$ terms of the series.

For the whole series we will push $n$ towards infinity. On a graph you can see what is happening. Figure 10.1 shows $n = 1$ and $n = 2$ and $n = 3$ and $n = \infty$ .

$$
1 + x + x ^ { 2 } + \cdots = { \frac { 1 } { 1 - x } } .
$$

$$
\begin{array} { r } { 1 + x + x ^ { 2 } + \cdots } \\ { 1 - x \sqrt { 1 } } \\ { \frac { 1 - x } { x } } \\ { \frac { x - x ^ { 2 } } { x ^ { 2 } } } \\ { \frac { x ^ { 2 } - x ^ { 3 } } { \cdots } } \end{array}
$$

The infinite sum gives a finite answer, provided $x$ is between $^ { - 1 }$ and 1. Then $x ^ { n }$ goes to zero:

$$
{ \frac { 1 - x ^ { n } } { 1 - x } } \to { \frac { 1 } { 1 - x } } .
$$

Now start with the function $1 / ( 1 - x )$ . How does it produce the series ? One way is elementary butbrutal, to do “long division” of $_ { 1 - x }$ into1 (nextto the figure). Another way is to look up the binomial formula for $( 1 - x ) ^ { - 1 }$ . That is cheating— we want to discover the series, not just memorize it. The successful approach uses calculus. Compute the derivatives of $f ( x ) = 1 / ( 1 - x )$ :

$$
f ^ { \prime } = ( 1 - x ) ^ { - 2 } \quad f ^ { \prime \prime } = 2 ( 1 - x ) ^ { - 3 } \quad f ^ { \prime \prime \prime } = 6 ( 1 - x ) ^ { - 4 } \cdots
$$

At $x = 0$ these derivatives are 1, 2, 6, 24, : : : : Notice how $^ { - 1 }$ from the chain rule keeps them positive. The nth derivative at $x = 0$ is $n$ factorial:

$$
f ( 0 ) = 1 \quad f ^ { \prime } ( 0 ) = 1 \quad f ^ { \prime \prime } ( 0 ) = 2 \quad f ^ { \prime \prime \prime } ( 0 ) = 6 \quad \cdots \quad f ^ { ( n ) } ( 0 ) = n ! .
$$

Now comes the idea. To match the series with $1 / ( 1 - x ) ;$ , match all those derivatives at $x = 0$ . Each power $x ^ { n }$ gets one derivative ri2ght. Its derivatives at $x = 0$ are zero, except the $n$ th derivative, which is $n$ ! By adding all powers we get every derivative right—so the geometric series matches the function:

$$
1 + x + x ^ { 2 } + x ^ { 3 } + \cdot \cdot \cdot h a s ~ t h e ~ s a m e ~ d e r i \nu a t i \nu e s ~ a t ~ x = 0 ~ a s ~ 1 / ( 1 - x ) .
$$

The linear approximation is $1 + x$ . Then comes ${ \textstyle { \frac { 1 } { 2 } } } f ^ { \prime \prime } ( 0 ) x ^ { 2 } = x ^ { 2 }$ . The third derivative is supposed to be 6, and $x ^ { 3 }$ is just what we need. Through its derivatives, the function produces the series.

With that example, you have seen a part of this subject. The geometric series diverges if $\left| x \right| \geqslant 1$ . Otherwise it adds up to the function it comes from (when $- 1 < x < 1 .$ ). To get familiar with other series, we now apply algebra or calculus—to reach the square of $1 / ( 1 - x )$ or its derivative or its integral. The point is that these operations are applied to the series.

The best I know is to show youeight operations that produce something useful. At the end we discover series for $\ln 2$ and $\pi$ .

1. Multiply the geometric series by a or ax:

$$
a + a x + a x ^ { 2 } + \cdots = { \frac { a } { 1 - x } } \quad a x + a x ^ { 2 } + a x ^ { 3 } + \cdots = { \frac { a x } { 1 - x } } .
$$

The first series fits the decimal 3:333 : : :: In that case $a = 3$ . The geometric series for $\textstyle x = { \frac { 1 } { 1 0 } }$ gave $1 . 1 1 1 . . . = 1 0 / 9$ , and this series is just three times larger. Its sum is $1 0 / 3$ .

The second series fits other decimals that are fractions in disguise. To get 12=99, choose $a = 1 2$ and $x = 1 / 1 0 0$ :

$$
. 1 2 1 2 1 2 . . . = { \frac { 1 2 } { 1 0 0 } } + { \frac { 1 2 } { 1 0 0 ^ { 2 } } } + { \frac { 1 2 } { 1 0 0 ^ { 3 } } } + \cdots = { \frac { 1 2 / 1 0 0 } { 1 - 1 / 1 0 0 } } = { \frac { 1 2 } { 9 9 } } .
$$

Problem 13 asks about :8787 : : : and :123123 : : :: It is usual in precalculus to write $a + a r + a r ^ { 2 } + \cdots = a / ( 1 - r )$ . But w e use $x$ instead of $r$ to emphasize that this is a function—which we can now differentiate.

2. The derivative of the geometric series $1 + x + x ^ { 2 } + \cdots$ is $1 / ( 1 - x ) ^ { 2 }$ :

$$
1 + 2 x + 3 x ^ { 2 } + 4 x ^ { 3 } + \cdots = { \frac { d } { d x } } \left( { \frac { 1 } { 1 - x } } \right) = { \frac { 1 } { ( 1 - x ) ^ { 2 } } } .
$$

At $\textstyle x = { \frac { 1 } { 1 0 } }$ the left side starts with 1:23456789. The right side is $1 / ( 1 - \textstyle { \frac { 1 } { 1 0 } } ) ^ { 2 } = 1 / ( 9 / 1 0 ) ^ { 2 }$ , which is 100=81. If you have a calculator, divide 100 by

The answer should also be near .1:11111111/2, which is 1:2345678987654321.

3. Subtract $1 + x + x ^ { 2 } + \cdots f r o m \ 1 + 2 x + 3 x ^ { 2 } + \cdots$ as you subtract functions:

$$
x + 2 x ^ { 2 } + 3 x ^ { 3 } + \cdots = { \frac { 1 } { ( 1 - x ) ^ { 2 } } } = { \frac { 1 } { ( 1 - x ) } } = { \frac { x } { ( 1 - x ) ^ { 2 } } } .
$$

Curiously, the same series comes from multiplying .5/ by $x$ . It answers a question left open in Section 8.4—the average number of coin tosses until the result is heads. This is the sum $1 ( p _ { 1 } ) + 2 ( p _ { 2 } ) + \cdots$ from probability, with $\begin{array} { r } { x = \frac { 1 } { 2 } } \end{array}$ :

$$
1 { \bigl ( } { \frac { 1 } { 2 } } { \bigr ) } + 2 { \bigl ( } { \frac { 1 } { 2 } } { \bigr ) } ^ { 2 } + 3 { \bigl ( } { \frac { 1 } { 2 } } { \bigr ) } ^ { 3 } + \cdots = { \frac { \frac { 1 } { 2 } } { ( 1 - { \frac { 1 } { 2 } } ) ^ { 2 } } } = 2 .
$$

The probability of waiting until the $n$ th toss is $\begin{array} { r } { p _ { n } = \left( \frac { 1 } { 2 } \right) ^ { n } } \end{array}$ . The expected value is two tosses. I suggested experiments, but now this mean v alue is exact.

4. Multiply series: the geometric series times itself is $1 / ( 1 - x )$ squared:

$$
( 1 + x + x ^ { 2 } + \cdots ) ( 1 + x + x ^ { 2 } + \cdots ) = 1 + 2 x + 3 x ^ { 2 } + \cdots .
$$

The series on the right is not new! In equation (5) it was the derivative of $y = 1 / ( 1 - x )$ . Now it is the square of the same $y$ . The geometric series satisfies $d y / d x = y ^ { 2 }$ , so the function does too. We have stumbled onto a differential equation.

Notice how the series was squared. A typical term in equation (8) is $3 x ^ { 2 }$ , coming from 1 times $x ^ { 2 }$ and $x$ times $x$ and $x ^ { 2 }$ times 1 on the left s1ide. It is a lot quicker to square $1 / ( 1 - x )$ —but other series can be multiplied when we don’t know what functions they addup to.

5. Solve $d y / d x = y ^ { 2 }$ from any starting value—a new application of series:

Suppose the starting value is $y = 1$ at $x = 0$ . The equation $y ^ { \prime } = y ^ { 2 }$ gives $1 ^ { 2 }$ for the de1rivative. Now a key step: The derivative of the equation gives $y ^ { \prime \prime } { = } 2 y y ^ { \prime }$ . At $x = 0$ that is $2 \cdot 1 \cdot 1$ . Continuing upwards, t1he derivative of $2 y y ^ { \prime }$ is $2 y y ^ { \prime \prime } + 2 ( y ^ { \prime } ) ^ { 2 }$ . At $x = 0$ that is $y ^ { \prime \prime \prime } { = } 4 + 2 = 6$ .

All derivatives are factorials: 1; 2; 6; 24; : : : : We are matching the derivatives of the geometric series $1 + x + x ^ { 2 } + x ^ { 3 } + \ldots$ Term by term, we rediscover the solution to $y ^ { \prime } = y ^ { 2 }$ . The solution starting from $y ( 0 ) = 1$ is $y = 1 / ( 1 - x )$ .

A different starting value is $^ { - 1 }$ . Then $y ^ { \prime } = ( - 1 ) ^ { 2 } = 1$ as before. The chain rule gives $y ^ { \prime \prime } { = } 2 y y ^ { \prime } { = } - 2$ and then $y ^ { \prime \prime \prime } = 6$ . With alternating signs to match these derivatives, the solution starting from $^ { - 1 }$ is

$$
y = - 1 + x - x ^ { 2 } + x ^ { 3 } + \cdots = - 1 / ( 1 + x ) .
$$

It is a small challenge to recognize the function on the right from the series on the left. The series has $- x$ in place of $x$ ; then multiply by $^ { - 1 }$ . The sum $y = - 1 / ( 1 + x )$ also satisfies $y ^ { \prime } = y ^ { 2 }$ . We can solve differential equations from all starting values by infinite series. Essentially we substitute an unknownseries into the equation, and calculate one term at a time.

6. The integrals of $1 + x + x ^ { 2 } + \cdots$ and $1 - x + x ^ { 2 } - \cdot \cdot \cdot$ are logarithms:

$$
{ \begin{array} { l } { { \displaystyle x + { \frac { 1 } { 2 } } x ^ { 2 } + { \frac { 1 } { 3 } } x ^ { 3 } + \cdots = { \int _ { 0 } ^ { x } { \frac { d x } { 1 - x } } = - \ln \left( 1 - x \right) } } } \\ { { \displaystyle x - { \frac { 1 } { 2 } } x ^ { 2 } + { \frac { 1 } { 3 } } x ^ { 3 } - \cdots = { \int _ { 0 } ^ { x } { \frac { d x } { 1 + x } } = + \ln \left( 1 + x \right) } } } \end{array} }
$$

The derivative of (10a) brings back the geometricseries. For log a8rithms we find $1 / n$ not $1 / n !$ The first term $x$ and second term ${ \scriptstyle { \frac { 1 } { 2 } } } x ^ { 2 }$ give linear and quadratic approximations. Now we have the whole series. I cannot fail to substitute 1 and $\frac { 1 } { 2 }$ , to find $\ln ( 1 - 1 )$ and $\ln ( 1 + 1 )$ and $\ln ( 1 - { \frac { 1 } { 2 } } )$ :

$$
\begin{array} { c c } { x = 1 : } & { 1 + \frac { 1 } { 2 } + \frac { 1 } { 3 } + \frac { 1 } { 4 } + \cdots = - \ln 0 = + \infty } \\ { x = 1 : } & { 1 - \frac { 1 } { 2 } + \frac { 1 } { 3 } - \frac { 1 } { 4 } + \cdots = \ln 2 { = . 6 9 3 } } \\ { x = \frac { 1 } { 2 } : } & { \frac { 1 } { 2 } + \frac { 1 } { 8 } + \frac { 1 } { 2 4 } + \frac { 1 } { 6 4 } + \cdots = - \ln \frac { 1 } { 2 } = \ln 2 . } \end{array}
$$

The first series diverges to infinity. This harmonic series $1 + { \frac { 1 } { 2 } } + { \frac { 1 } { 3 } } + \cdots$ came into the earliest discussion of limits (Section 2.6). The second series has alternating signs and converges to ln 2. The third has plus signs and also converges to ln 2. These will be examples for a major topic in infinite series— tests for convergence.

For the first time in this book we are able to compute a logarithm! Something remarkable is involved. The sums of numbers in .11/ and .12/ were discovered from the sums of functions in .10/. You might think it would be easier to deal only with numbers, to compute ln 2. But then we would never have integrated the series for $1 / ( 1 - x )$ and detected .10/. It is better to work with $x$ , and substitute special values like $\frac { 1 } { 2 }$ at the end.

There are two practical proble ms with these series. For $\ln 2$ they converge slowly. For ln $e$ they blow up. The correct answer is ln $e = 1$ , but the series can’t find it. Both problems are solved by adding (10a) to (10b), which cancels the even powers:

$$
2 \left( x + { \frac { x ^ { 3 } } { 3 } } + { \frac { x ^ { 5 } } { 5 } } + \cdots \right) = \ln ( 1 + x ) - \ln ( 1 - x ) = \ln { \frac { 1 + x } { 1 - x } } .
$$

At $\begin{array} { r } { x = \frac { 1 } { 3 } } \end{array}$ , the right side is $\ln { \frac { 4 } { 3 } } - \ln { \frac { 2 } { 3 } } = \ln 2$ . Powers of $\begin{array} { l } { { \frac { 1 } { 3 } } } \end{array}$ are much smaller than powers of 1 or $\frac { 1 } { 2 }$ , so ln 2 is quickly computed. All logarithms can be found from the improved series .13/.

7. Change variables in the geometric series (replace $x$ by $x ^ { 2 } o r \ - x ^ { 2 } )$ :

$$
\begin{array} { l } { { 1 + x ^ { 2 } + x ^ { 4 } + x ^ { 6 } + \cdots = 1 / ( 1 - x ^ { 2 } ) } } \\ { { 1 - x ^ { 2 } + x ^ { 4 } - x ^ { 6 } + \cdots = 1 / ( 1 + x ^ { 2 } ) . } } \end{array}
$$

This produces new functions (always our goal). They involve even powers of $x$ . The second series will soon be used to calculate $\pi$ . O ther changes are valuable:

$$
{ \begin{array} { l l l } { { \cfrac { x } { 2 } } { \mathrm { i n p l a c e ~ o f ~ } } x : } & { 1 + { \cfrac { x } { 2 } } + \left( { \cfrac { x } { 2 } } \right) ^ { 2 } + \cdots = { \cfrac { 1 } { 1 - ( x / 2 ) } } = { \cfrac { 2 } { 2 - x } } } \\ { { \cfrac { 1 } { x } } { \mathrm { i n p l a c e ~ o f ~ } } x : } & { 1 + { \cfrac { 1 } { x } } + { \cfrac { 1 } { x ^ { 2 } } } } & { + \cdots = { \cfrac { 1 } { 1 - ( 1 / x ) } } = { \cfrac { x } { x - 1 } } . } \end{array} }
$$

Equation (17) is aseries of negative powers $x ^ { - n }$ . It convergeswhen $| x |$ is greater than 1. Convergence in .17/ is for large $x$ . Convergence in .16/ is for $\vert x \vert < 2$ .

8. The integral of $1 - x ^ { 2 } + x ^ { 4 } - x ^ { 6 } + \cdot \cdot \cdot$ yields the inverse tangent of $x$ :

$$
x - { \frac { 1 } { 3 } } x ^ { 3 } + { \frac { 1 } { 5 } } x ^ { 5 } - { \frac { 1 } { 7 } } x ^ { 7 } + \cdots = \int { \frac { d x } { 1 + x ^ { 2 } } } = \tan ^ { - 1 } x .
$$

We integrated .15/ and got odd powers. The magical formula for $\pi$ (discovered by Leibniz) comes when $x = 1$ . The angle with tangent 1 is $\pi / 4$ :

$$
1 - { \frac { 1 } { 3 } } + { \frac { 1 } { 5 } } - { \frac { 1 } { 7 } } + \cdots = { \frac { \pi } { 4 } } .
$$

The first three terms give $\pi \approx 3 . 4 7$ (not very close). The 5000th term is still of size :0001, so the fourth decimal is still not settled. By changing to $x = 1 / \sqrt { 3 }$ , the astronomer Halley and his assistant found 71 correct digits of $\pi / 6$ (while waiting for the comet). That is one step in the long and amazing story of calculating $\pi$ . The

Chudnovsky brothers recently took the latest step with a supercomputer—they have found more than one billion decimal places of $\dot { \pi }$ (see Science, June 1989). The digits look completely random, as everyone expected. But so far we have no proof that all ten digits occur $\frac { 1 } { 1 0 }$ of the time.

Historical note Archimedes located $\pi$ above 3:14 and below $3 { \frac { 1 } { 7 } }$ . Variations of his method (polygons in circles) reached as far as 34 digits—but not for 1800 years. Then Halley found 71 digits of $\pi / 6$ with equation (18). For faster convergence that series was replaced by other inverse tangents, using smaller values of $x$ :

$$
{ \frac { \pi } { 4 } } = \tan ^ { - 1 } { \frac { 1 } { 2 } } + \tan ^ { - 1 } { \frac { 1 } { 3 } } = 4 \tan ^ { - 1 } { \frac { 1 } { 5 } } - \tan ^ { - 1 } { \frac { 1 } { 2 3 9 } } .
$$

A prodigy named Dase, who could multiply 100-digit numbers in his head in 8 hours, finally passed 200 digits of $\pi$ . The climax of hand calculation came when Shanks published 607 digits. I am sorry to say that only 527 were correct. (With years of calculation he went on to 707 digits, but still only 527 were correct.) The mistake was not noticed until 1945! Then Ferguson reached 808 digits with a desk calculator.

Now comes the computer. Three days on an ENIAC .1949/ gave 2000 digits. A hundred minutes on an IBM 704 .1958/ gave 10; 000 digits. Shanks (no relation) reached 100; 000 digits. Finally a million digits were found in a day in 1973, with a CDC 7600. All these calculations used variations of equation (20).

The record after that wentabetween Cray and Hitachi and now IBM. But the method changed. The calculations rely on an incredibly accurate algorithm, based on the “arithmetic-geometric mean iteration” of Gauss. It is also incredibly simple, all things considered:

$$
a _ { n + 1 } = { \frac { a _ { n } + b _ { n } } { 2 } } b _ { n + 1 } = \sqrt { a _ { n } b _ { n } } \pi _ { n } = 2 a _ { n + 1 } ^ { 2 } \Bigg / \left( 1 - \sum _ { k = 0 } ^ { n } 2 ^ { k } ( a _ { k } ^ { 2 } - b _ { k } ^ { 2 } ) \right) .
$$

The number of correct digits more than doubles at every step. By $n = 9$ we are far beyond Shan?ks (the hand calculator). No?end is in sight. Almost anyone can go past a billion digits, since with the Chudnovsky method we don’t have to start over again.

It is time to stop. You may think (or hop|e) th at nothing more could possibly be done with geometric series. We have gone a long way from $1 / ( 1 - x )$ , but some functions can never be reached. One is $e ^ { x }$ (and its relatives sin $x$ , cos $x$ , $\sinh x$ , cosh $x$ ). Another is $\sqrt { 1 - x }$ (and its relatives $1 / { \sqrt { 1 - x ^ { 2 } } } , \sin ^ { - 1 } x , \sec ^ { - 1 } x , \ldots )$ . The exponentials are in 10:4, with series that converge for all $x$ . The square-roots are in 10:5, closer to geometric series and converging for $\left| x \right| < 1$ . Before that we have to say what convergence means.

The series came fast, but I hope you see what can be done (subtract, multiply, differentiate, integrate). Addition is easy, division is harder, all are legal. Some unexpected numbers are the sums of infinite series.

Added in proof By e-mail I just learned that the record for $\pi$ is back in Japan: $2 ^ { 3 0 }$ digits which is more than 1:07 billion. The elapsed time was 100 hours (75 hours of CPU time on an NEC machine). The billionth digit after the decimal point is 9.