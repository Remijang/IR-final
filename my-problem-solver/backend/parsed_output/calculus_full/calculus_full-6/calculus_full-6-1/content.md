# 6.1 An Overview

There is a good chance you have met logarithms. They turn multiplication into addition, which is a lot simpler. They are the basis for slide rules (not so important) and for graphs on log paper (very important). Logarithms are mirror images of exponentials—and those I know you have met.

Start with exponentials. The numbers 10 and $1 0 ^ { 2 }$ and $1 0 ^ { 3 }$ are basic to the decimal system. For completeness I also include $1 0 ^ { 0 }$ ; which is “ten to the zeroth power” or 1: The logarithms of those numbers are the exponents. The logarithms of 1 and 10 and 100 and 1000 are 0 and 1 and 2 and 3: These are logarithms “to base 10,” because the powers are powers of 10:

Question When the base changes from 10 to $b$ , what is the logarithm of 1 ?

Answer Since $b ^ { 0 } = 1$ , $\log _ { b } 1$ is always zero. To base $b$ , the logarithm of $b ^ { n }$ is $n$ : Negative powers are also needed. The number $1 0 ^ { x }$ is positive, but its exponent $x$ can be negative. The first examples are $1 / 1 0$ and $1 / 1 0 0$ , which are the same as $1 0 ^ { - 1 }$ and $1 0 ^ { - 2 }$ : The logarithms are the exponents $^ { - 1 }$ and $^ { - 2 }$ :

$$
\begin{array} { r l } { 1 0 0 0 = 1 0 ^ { 3 } \quad } & { { } \mathrm { a n d } \qquad \log 1 0 0 0 = 3 } \\ { 1 / 1 0 0 0 = 1 0 ^ { - 3 } \quad } & { { } \mathrm { a n d } \qquad \log 1 / 1 0 0 0 = - 3 . } \end{array}
$$

Multiplying 1000 times $1 / 1 0 0 0$ gives $1 = 1 0 ^ { 0 }$ : Adding logarithms gives $3 + ( - 3 ) =$ 0: Always $1 0 ^ { m }$ times $1 0 ^ { n }$ equals $1 0 ^ { m + n }$ : In particular $1 \bar { 0 } ^ { 3 }$ times $1 0 ^ { 2 }$ produces five tens:

$$
( 1 0 ) ( 1 0 ) ( 1 0 ) { \mathrm { ~ t i m e s ~ } } ( 1 0 ) ( 1 0 ) { \mathrm { ~ e q u a l s ~ } } ( 1 0 ) ( 1 0 ) ( 1 0 ) ( 1 0 ) ( 1 0 ) = 1 0 ^ { 5 } .
$$

The law for $b ^ { m }$ times $b ^ { n }$ extends to all exponents, as in $1 0 ^ { 4 . 6 }$ times $1 0 ^ { \pi }$ : Furthermore the law applies to all bases (we restrict the base to $b > 0$ and $b \neq 1$ ). In every case multiplication of numbers is addition of exponents.

Historical note In the days of slide rules, 1:2 and 1:3 were multipliedby sliding one edge across to 1:2 and reading the answer under 1:3: A slide rule made in Germany would give the third digit in 1:56: Its photograph shows the numbers on a log scale. The distance from 1 to 2 equals the distance from 2 to 4 and from 4 to 8: By sliding the edges, you add distances and multiply numbers.

Division goes the other way. Notice how $1 0 0 0 / 1 0 = 1 0 0$ matches $3 - 1 = 2$ : To divide 1:56 by 1:3, look back along line $\mathrm { ~ D ~ }$ for the answer 1:2:

The second figure, though smaller, is the important one. When $x$ increases by $1 , 2 ^ { x }$ is multiplied by 2. Adding to x multiplies $y$ : This rule easily gives $y = 1 , 2 , 4 , 8$ ; but look ahead to calculus—which doesn’t stay with whole numbers.

Calculus will add $\Delta x$ : Then $y$ is multiplied by $2 ^ { \Delta x }$ : This number is near 1: If $\begin{array} { r } { \Delta x = \frac { 1 } { 1 0 } } \end{array}$ then $2 ^ { \Delta x } \approx 1 . 0 7$ —the tenth root of 2: To find the slope, we have to consider $( { 2 ^ { \Delta x } } - 1 ) / \Delta x$ . The limit is near $\begin{array} { r } { ( 1 . 0 7 - 1 ) / \frac { 1 } { 1 0 } = . 7 \qquad } \end{array}$ , but the exact number will take time.

Base Change Bases other than 10 and exponents other than $1 , 2 , 3 , \ldots$ are needed for applications. The population of the world $x$ years from now is predicted to grow by a factor close to $1 . 0 2 ^ { x }$ : Certainly $x$ does not need to be a whole number of years. And certainly the base 1:02 should not be 10 (or we are in real trouble). This prediction will be refined as we study the differential equations for growth. It can be rewritten to base 10 if that is preferred (but look at the exponent):

$$
1 . 0 2 ^ { x } \quad i s t h e s a m e a s \quad 1 0 ^ { ( \log 1 . 0 2 ) x } .
$$

When the base changes from 1:02 to 10, the exponent is multiplied—as we now see. For practice, start with base $b$ and change to base $a$ : The logarithm to base $a$ will be written “log :” Everything comes from the rule that logarithm $\ b =$ exponent:

$$
b a s e c h a n g e f o r n u m b e r s : b = a ^ { \log b } .
$$

Now raise both sides to the power $x$ : You see the change in the exponent:

$$
b a s e c h a n g e f o r e x p o n e n t i a l s : b ^ { x } = a ^ { ( \log b ) x } .
$$

Finally set $y = b ^ { x }$ : Its logarithm to base $b$ is $x$ : Its logarithm to base $a$ is the exponent on the right hand side: $\log _ { a } y = ( \log _ { a } b ) x$ : Now replace $x$ by $\log _ { b } y$ :

$$
b a s e c h a n g e f o r l o g a r i t h m s : \quad \log _ { a } y = ( \log _ { a } b ) ( \log _ { b } y ) .
$$

We absolutely need this ability to change the base. An example with $a = 2$ is

$$
b = 8 = 2 ^ { 3 } \qquad 8 ^ { 2 } = ( 2 ^ { 3 } ) ^ { 2 } = 2 ^ { 6 } \qquad \log _ { 2 } { 6 } 4 = 3 \cdot 2 = ( \log _ { 2 } { 8 } ) ( \log _ { 8 } { 6 } 4 ) .
$$

The rule behind base changes is $( a ^ { m } ) ^ { x } = a ^ { m x }$ : When the $m$ th power is raised to the $x$ th power, the exponents multiply. The square of the cube is the sixth power:

$$
( a ) ( a ) ( a ) \mathrm { t i m e s } ( a ) ( a ) ( a ) \mathrm { e q u a l s } ( a ) ( a ) ( a ) ( a ) ( a ) ( a ) : ( a ^ { 3 } ) ^ { 2 } = a ^ { 6 } .
$$

Another base will soon be more important than 10—here are the rules for base changes:

6B To change numbers, powers, and logarithms from base $b$ to base $a$ , use $b = a ^ { \log _ { a } b } \qquad b ^ { x } = a ^ { ( \log _ { a } b ) x } \qquad \log _ { a } y = ( \log _ { a } b ) ( \log _ { b } y )$

The first is the definition. The second is the $x$ th power of the first. The third is the logarithm of the second (remember $y$ is $b ^ { x }$ ). An important case is $y = a$ :

$$
\log _ { a } a = ( \log _ { a } b ) ( \log _ { b } a ) = 1 \operatorname { s o } \log _ { a } b = 1 / \log _ { b } a .
$$

EXAMPLE $8 = 2 ^ { 3 }$ means $8 ^ { 1 / 3 } = 2$ : Then $( \log _ { 2 } 8 ) ( \log _ { 8 } 2 ) = ( 3 ) ( 1 / 3 ) = 1 .$

This completes the algebra of logarithms. The addition rules 6A came from $( b ^ { m } ) ( b ^ { n } ) = b ^ { m + n }$ : The multiplication rule 6B came from $( a ^ { m } ) ^ { x } = a ^ { m x }$ : We still need to define $b ^ { x }$ and $a ^ { x }$ for all real numbers $x$ . When $x$ is a fraction, the definition is easy. The square root of $a ^ { 8 }$ is $a ^ { 4 } ( m = 8$ times $x = 1 / 2 ,$ /: When $x$ is not a fraction, as in $2 ^ { \pi }$ ; the graph suggests one way to fill in the hole.

We could define 2 as the limit of 23; 231=10; 2314=100; As the fractions $r$ approach $\pi$ , the powers $2 ^ { r }$ approach $2 ^ { \pi }$ : This makes $y = 2 ^ { x }$ into a continuous function, with the desired properties $( 2 ^ { m } ) ( 2 ^ { n } ) = 2 ^ { m + n }$ and $( 2 ^ { m } ) ^ { x } = 2 ^ { m x }$ —whether $m$ and $n$ and $x$ are integers or not. But the $\varepsilon$ ’s and $\delta$ ’s of continuity are not attractive, and we eventually choose (in Section 6:4) a smoother approach based on integrals.

$$
{ \mathsf { G R A P H S } } \ { \mathsf { O F } } \ b ^ { x } \ { \mathsf { A N D } } \ \log _ { b } y
$$

It is time to draw graphs. In principle one graph should do the job for both functions, because $y = b ^ { x }$ means the same as $x = \log _ { b } y$ : These are inverse functions. What one function does, its inverse undoes. The logarithm of $g ( x ) = b ^ { x }$ is $x$ :

$$
g ^ { - 1 } ( g ( x ) ) = \log _ { b } ( b ^ { x } ) = x .
$$

In the opposite direction, the exponential of the logarithm of $y$ is $y$ :

$$
g ( g ^ { - 1 } ( y ) ) = b ^ { ( \log _ { b } y ) } = y .
$$

This holds for every base $b$ , and it is valuable to see $b = 2$ and $b = 4$ on the same graph. Figure 6.2a shows $y = 2 ^ { x }$ and $y = 4 ^ { x }$ : Their mirror images in the $4 5 ^ { \circ }$ line give the logarithms to base 2 and base 4, which are in the right graph.

When $x$ is negative, $y = b ^ { x }$ is still positive. If the first graph is extended to the left, it stays above the $x$ axis. Sketch it in with your pencil. Also extend the second graph down, to be the mirror image. Don’t cross the vertical axis.

# 6.1 An Overview

There are interesting relations within the left figu8re. All exponentials start at 1, bec8ause $b ^ { 0 }$ is always 1: At the height $y = 1 6$ , one graph is above $x = 2$ (because $4 ^ { 2 } = 1 6$ . The other graph is above $x = 4$ (because $2 ^ { 4 } = 1 6$ ). Why does $4 ^ { x }$ in one graph equal $2 ^ { 2 x }$ in the other ? This is the base change for powers, since $4 = 2 ^ { 2 }$ :

The figure on the right shows the mirror image—the logarithm. All logarithms start from zero at $y = 1$ : The graphs go down to $- \infty$ at $y = 0$ : (Roughly speaking $2 ^ { - \infty }$ is zero.) Again $x$ in one graph corresponds to $2 x$ in the other (base change for logarithms). Both logarithms climb slowly, since the exponentials climb so fast.

The number $\log _ { 2 } 1 0$ is between 3 and 4, because 10 is between $2 ^ { 3 }$ and $2 ^ { 4 }$ : The slope of $2 ^ { x }$ is proportional to $2 ^ { x }$ —which never happened for $x ^ { n }$ : But there are two practical difficulties with those graphs:

1. $2 ^ { x }$ and $4 ^ { x }$ increase too fast. The curves turn virtually straight up. 2. The most important fact about $A b ^ { x }$ is the value of $b$ —and the base doesn’t stand out in the graph.

There is also another point. In many problems we don’t know the function $y = f ( x )$ : We are looking for it! All we have are measured values of $y$ (with errors mixed in). When the values are plotted on a graph, we want to discover $f ( x )$ :

Fortunately there is a solution. Scale the y axis differently. On ordinary graphs, each unit upward adds a fixed amount to $y$ : On a log scale each unit multiplies $y$ by a fixed amount. The step from $y = 1$ to $y = 2$ is the same length as the step from 3 to 6 or 10 to 20:

On a log scale, $y = 1 1$ is not halfway between 10 and 12: And $y = 0$ is not there at all. Each step down divides by a fixed amount—we never reach zero. This is completely satisfactory for $A b ^ { x }$ , which also never reaches zero.

Figure 6.3 is on semilog paper (also known as log-linear), with an ordinary $x$ axis. The graph of $y = A b ^ { x }$ is a straight line. To see why, take logarithms of that equation:

$$
\log y = \log A + x \log b .
$$

The relation between $x$ and log $y$ is linear. It is really $\log y$ that is plotted, so the graph is straight. The markings on the $y$ axis allow you to enter $y$ without looking up its logarithm—you get an ordinary graph of $\log y$ against $x$ :

Figure 6.3 shows two examples. One graph is an exact plot of $y = 2 \cdot 1 0 ^ { x }$ : It goes upward with slope 1; because a unit across has the same length as multiplication by 10 going up. $1 0 ^ { x }$ has slope 1 and $1 0 ^ { ( \log b ) x }$ (which is $b ^ { x }$ ) will have slope $\log b$ . The crucial number $\log b$ can be measured directly as the slope.

The second graph in Figure 6.3 is more typical of actual practice, in which we start with measurements and look for $f ( x )$ : Here are the data points:

$$
\begin{array} { l l l l l l } { x = 0 . 0 } & { 0 . 2 } & { 0 . 4 } & { 0 . 6 } & { 0 . 8 } & { 1 . 0 } \\ { y = 4 . 0 } & { 3 . 2 } & { 2 . 4 } & { 2 . 0 } & { 1 . 6 } & { 1 . 3 } \end{array}
$$

We don’t know in advancewhether these values fit the model $y = A b ^ { x }$ : The graph is strong evidence that they do. The points lie close to a line with negative slope— indicating $\log b < 0$ and $b < 1$ : The slope down is half of the earlier slope up, so the model is consistent with

$$
y = A \cdot 1 0 ^ { - x / 2 } \quad { \mathrm { o r } } \quad \log y = \log A - { \frac { 1 } { 2 } } x .
$$

When $x$ reaches $2 , y$ drops by a factor of 10: At $x = 0$ we see $A \approx 4$ :

Another model—a power $y = A x ^ { k }$ instead of an exponential—also stands out with logarithmic scaling. This time we use log-log paper, with both axes scaled. The logarithm of $y = \hat { A } x ^ { k }$ gives a linear relation between log $y$ and $\log x$ :

$$
\log y = \log A + k \log x .
$$

The exponent $k$ becomes the slope on log-log paper. The base? $b$ makes no difference. We just measure the slope, and a straight line is a lot more attractive than a power curve.

The graphs in Figure 6.4 have slopes 3 and $\frac { 1 } { 2 }$ and $^ { - 1 }$ : They represent $A x ^ { 3 }$ and $A { \sqrt { x } }$ and $A / x$ : To find the $A$ ’s, look at one point on the line. At $x = 4$ the height is 8; so adjust the $A$ ’s to make this happen: The functions are $x ^ { 3 } / 8$ and $4 { \sqrt { x } }$ and $3 2 / x$ : On semilog paper those graphs would not be straight!

You can buy log paper or create it with computer graphics.

This is a calculus book. We have to ask about slopes. The algebra of exponents is done, the rules are set, and on log paper the graphs are straight. Now come limits.

The central question is the derivative. What is $d y / d x$ when $y = b ^ { x } \ ;$ What is $d x / d y$ when $x$ is the logarithm $\log _ { b } { y } \ \vdots$ Those questions are closely related, because $b ^ { x }$ and $\log _ { b } y$ are inverse functions. If one slope can be found, the other is known from $d x / \bar { d y } = 1 / ( d y / d x )$ : The problem is to find one of them, and the exponential comes first.

You will now see that those questions have quick (and beautiful) answers, except for a mysterious constant. There is a multiplying factor $c$ which needs more time.

# 6.1 An Overview

I think it is worth separating out the part that can be done immediately, leaving $c$ in $d y / d x$ and $1 / c$ in $d x / d y$ : Then Section 6:2 discovers $c$ by studying the special number called $e$ (but $c \neq e$ ).

6C The derivative of $b ^ { x }$ is a multiple $c b ^ { x }$ : The number $c$ depends on the base $b$ :

The product and power and chain rules do not yield this derivative. We are pushed all the way back to the original definition, the limit of $\Delta y / \Delta x$ :

$$
{ \frac { d y } { d x } } = \operatorname* { l i m } _ { h \to 0 } { \frac { y ( x + h ) - y ( x ) } { h } } = \operatorname* { l i m } _ { h \to 0 } { \frac { b ^ { x + h } - b ^ { x } } { h } } .
$$

Key idea: Split $b ^ { x + h }$ inÑto $b ^ { x }$ times $b ^ { h }$ : ThenÑthe crucial quantity $b ^ { x }$ factors out. More than that, $b ^ { x }$ comes outside the limit because it does not depend on $h$ : The remaining limit, inside the brackets, is the number $c$ that we don’t yet know:

$$
{ \frac { d y } { d x } } = \operatorname* { l i m } _ { h \to 0 } { \frac { b ^ { x } b ^ { h } - b ^ { x } } { h } } = b ^ { x } \left[ \operatorname* { l i m } _ { h \to 0 } { \frac { b ^ { h } - 1 } { h } } \right] = c b ^ { x } .
$$

This equation is central to the whole chapter: $d y / d x$ equals $c b ^ { x }$ which equals $c y$ : The rate of change of $y$ is proportional to $y$ . The slope increases in the same way that $b ^ { x }$ increases (except for the factor $c$ ). A typical example is money in a bank, where interest is proportional to the principal. The rich get richer, and the poor get slightly richer. We will come back to compound interest, and identify $b$ and $c$ :

The inverse function is $x = \log _ { b } y$ : Now the unknown factor is $1 / c$ :

6D The slope of $\log _ { b } y$ is $1 / c y$ with the same $c$ (depending on $b$ ).

Proof I ${ \mathrm { ~ f ~ } } d y / d x = c b ^ { x } { \mathrm { ~ t h e n ~ } } d x / d y = 1 / c b ^ { x } = 1 / c y .$

That proof was like a Russian toast, powerful but too quick! We go more carefully:

$$
\begin{array} { r l } { f ( b ^ { x } ) = x } & { \mathrm { ( l o g a r i t h m o f e x p o n e n t i a l ) } } \\ { f ^ { \prime } ( b ^ { x } ) ( c b ^ { x } ) = 1 } & { \mathrm { ( } x \mathrm { d e r i v a t i v e b y c h a i n r u l e ) } } \\ { f ^ { \prime } ( b ^ { x } ) = 1 / c b ^ { x } } & { \mathrm { ( d i v i d e b y } c b ^ { x } ) } \\ { f ^ { \prime } ( y ) = 1 / c y } & { \mathrm { ( i d e n t i f y } b ^ { x } \mathrm { a s } y ) } \end{array}
$$

The logarithm gives another way to find $c$ : From its slope we can discover $1 / c$ : This is the way that finally works (next section).

Final remark It is extremely satisfying to meet an $f ( y )$ whose derivative is $1 / c y$ : At last the $^ { 6 6 } - 1$ power” has an antiderivative. Remember that $\textstyle \int x ^ { n } d x = x ^ { n + 1 } / ( n +$

1/ is a failure when $n = - 1$ : The derivative of $x ^ { 0 }$ (a constant) does not produce $x ^ { - 1 }$ We had no integral for $x ^ { - 1 }$ , and the logarithm fills that gap. If $y$ is replaced by $x$ or $t$ (all dummy variables) then

$$
{ \frac { d } { d x } } \log _ { b } x = { \frac { 1 } { c x } } \qquad { \mathrm { a n d } } \qquad { \frac { d } { d t } } \log _ { b } t = { \frac { 1 } { c t } } .
$$

The base $b$ can be chosen so that $c = 1$ : Then the derivative is $1 / x$ : This final touch comes from the magic choice $b = e$ —the highlight of Section 6.2.