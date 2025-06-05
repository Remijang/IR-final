# 6.6 Powers Instead of Exponentials

You may remember our first look at $e$ . It is the special base for which $e ^ { x }$ has slope 1 at $x = 0$ . That led to the great equation of exponential growth: The derivative of $e ^ { x }$ equals $e ^ { x }$ . But our look at the actual number $e = 2 . 7 1 8 2 8 \dots$ was very short. It appeared as the limit of $( 1 + 1 / n ) ^ { n }$ . This seems an unnatural way to write down such an important number.

I want to show how $( 1 + 1 / n ) ^ { n }$ and $( 1 + x / n ) ^ { n }$ arise naturally. They give discrete growth in finite steps—with applications to compound interest. Loans and life insurance and money market funds use the discrete form of $y ^ { \prime } = c y + s$ . (We include extra information about bank rates, hoping this may be useful some day.) The applications in science and engineering are equally important. Scientific computing, like accounting, has difference equations in parallel with differential equations.

Knowing that this section will be full of formulas,  Iwould like to jump ahead and tell you the best one. It is an infinite series for $e ^ { x }$ . What makes the series beautiful is that its derivative is itself.

Start with $y = 1 + x$ . This has $y = 1$ and $y ^ { \prime } = 1$ at $x = 0$ . But $y ^ { \prime \prime }$ is zero, not one. Such a simple function doesn’t stand a chance! No polynomial can be its own derivative, because the highest power $x ^ { n }$ drops down to $n x ^ { n - 1 }$ . The only way is to have no highest power. We are forced to consider infinitely many terms—a power series—to achieve “derivative equals function.”

To produce the derivative $1 + x$ ; we need $\textstyle 1 + x + { \frac { 1 } { 2 } } x ^ { 2 }$ : Then ${ \frac { 1 } { 2 } } x ^ { 2 }$ is the derivative of ${ \scriptstyle { \frac { 1 } { 6 } } } x ^ { 3 }$ ; which is the derivative of ${ \textstyle { \frac { 1 } { 2 4 } } } x ^ { 4 }$ : The best way is to write the whole series at once:

$$
I n f i n i t e s e r i e s \quad e ^ { x } = 1 + x + \textstyle { \frac { 1 } { 2 } } x ^ { 2 } + \textstyle { \frac { 1 } { 6 } } x ^ { 3 } + \textstyle { \frac { 1 } { 2 4 } } x ^ { 4 } + \cdots .
$$

This must be the greatest power series ever discovered.Its derivative is itself:

$$
d e ^ { x } / d x = 0 + 1 + x + { \textstyle { \frac { 1 } { 2 } } } x ^ { 2 } + { \textstyle { \frac { 1 } { 6 } } } x ^ { 3 } + \dots = e ^ { x } .
$$

The derivative of each term is the term before it. The integral of each term is the one after it (so $\textstyle \int e ^ { x } d x = e ^ { x } + C )$ . The approximation $e ^ { x } \approx 1 + x$ appears in the first two terms. Other properties like $( e ^ { x } ) ( e ^ { x } ) = e ^ { 2 x }$ are not so obvious. (Multiplying series is hard but interesting.) $I t$ is no teven clear why the sum is 2:718 : : : when $x = 1$ . Somehow $1 + 1 + { \frac { 1 } { 2 } } + { \frac { 1 } { 6 } } + \cdots$ equals $e$ : That is where $( 1 + 1 / n ) ^ { n }$ will come in.

Notice that $x ^ { n }$ is divided by the product $1 \cdot 2 \cdot 3 \cdot \cdots n$ : This is $^ { * * } n$ factorial.” Thus $x ^ { 4 }$ is divided by $1 \cdot 2 \cdot 3 \cdot 4 = 4 ! = 2 4$ ; and $x ^ { 5 }$ is divided by $5 ! = 1 2 0$ : The derivative of $x ^ { 5 } / 1 2 0$ is $x ^ { 4 } / 2 4$ ; because 5 from the derivative cancels 5 from the factorial. In general $x ^ { n } / n !$ has derivative $x ^ { n - 1 } / ( n - 1 ) !$ Surprisingly 0Š is 1:

Chapter 10 emphasizes that $x ^ { n } / n !$ becomes extremely small as $n$ increases. The infinite series adds up to a finite number—which is $e ^ { x }$ : We turn now to discrete growth, which produces the same series in the limit.

This headline was on page one of the New York Times for May 27; 1990:

# 213 Years After Loan, Uncle Sam is Dunned

San Antonio, May 26—More than 200 years ago, a wealthy Pennsylvania merchant named Jacob DeHaven lent $\$ 450,000$ to the Continental Congress to rescue the troops at Valley Forge. That loan was apparently never repaid.

So Mr. DeHaven’s descendants are taking the United States Government to court to collect what they believe they are owed. The total: $\$ 141$ billion if the interest is compounded daily at 6 percent, the going rate at the time. If compounded yearly, the bill is only $\$ 98$ billion.

The thousands of family members scattered around the country say they are not being greedy. “It’s not the money—it’s the principle of the thing,” said Carolyn Cokerham, a DeHaven on her father’s side who lives in San Antonio. “You have to wonder whether there would even be a United States if this man had not made the sacrifice that he did. He gave everything he had.”

The descendants say that they are willing to be flexible about the amount of settlement. But they also note that interest is accumulating at $\$ 190$ a second.

“None of these people have any intention of bankrupting the Government,” said Jo Beth Kloecker, a lawyer from Stafford, Texas. Fresh out of law school, Ms. Kloecker accepted the case for less than the customary 30 percent contingency.

It is unclear how many descendants there are. Ms. Kloecker estimates that based on 10 generations with four children in each generation, there could be as many as half a million.

The initial suit was dismissed on the ground that the statute of limitations is six years for a suit against the Federal Government. The family’s appeal asserts that this violates Article 6 of the Constitution, which declares as valid all debts owed by the Government before the Constitution was adopted.

Mr. DeHaven died penniless in 1812: He had no children.

# COMPOUND INTEREST

The idea of compound interest can be applied right away. Suppose you invest $\$ 1000$ at a rate of $100 \%$ (hard to do). If this is the annual rate, the interest after a year is another $\$ 1000$ : You receive $\$ 2000$ in all. But if the interest is compounded you receive more:

after six months: Interest of $\$ 500$ is reinvested to give $\$ 1500$ end of year: New interest of $\$ 750$ ( $50 \%$ of 1500) gives $\$ 2250$ total.

The bank multiplied twice by 1:5 (1000 to 1500 to 2250). Compounding quarterly multiplies four times by 1:25 (1 for principal, :25 for interest):

after one quarter the total is $1 0 0 0 + ( . 2 5 ) ( 1 0 0 0 ) { = } 1 2 5 0$ after two quarters the total is $1 2 5 0 + ( . 2 5 ) ( 1 2 5 0 ) { = } 1 5 6 2 . 5 0$ after nine months the total is $1 5 6 2 . 5 0 + ( . 2 5 ) ( 1 5 6 2 . 5 0 ) = 1 9 5 3 . 1 2$ after a full year the total is $1 9 5 3 . 1 2 + ( . 2 5 ) ( 1 9 5 3 . 1 2 ) = 2 4 4 1 . 4 1$

Each step multiplies by $1 + ( 1 / n )$ ; to add one $n$ thof a year’s interest—still at $100 \%$ :

quarterly conversion: $( 1 + 1 / 4 ) ^ { 4 } \times 1 0 0 0 ~ = 2 4 4 1 . 4 1$ monthly conversion: $( 1 + 1 / 1 2 ) ^ { 1 2 } \times 1 0 0 0 { = } 2 6 1 3 . 0 4$ daily conversion: $( 1 + 1 / 3 6 5 ) ^ { 3 6 5 } \times 1 0 0 0 = 2 7 1 4 . 5 7 .$

Many banks use 360 days in a year, although computers have made that obsolete. Very few banks use minutes (525; 600 per year). Nobody compounds every second . $( n = 3 1 , 5 3 6 , 0 0 0 )$ : But some banks offer continuous compounding. This is the limiting case . $( n  \infty )$ / that produces $e$ :



$$
{ \bigg ( } 1 + { \frac { 1 } { n } } { \bigg ) } ^ { n } \times 1 0 0 0 \ a p p r o a c h e s \ e \times 1 0 0 0 = 2 7 1 8 . 2 8 .
$$

1. Quick method for $( 1 + 1 / n ) ^ { n }$ : Take its logarithm. Use $\ln ( 1 + x ) \approx x$ with $x =$ $\underline { { 1 } }$ :

$$
\ln \left( 1 + { \frac { 1 } { n } } \right) ^ { n } = n \ln \left( 1 + { \frac { 1 } { n } } \right) \approx n \left( { \frac { 1 } { n } } \right) = 1 .
$$

As $1 / n$ gets smaller, this approximation gets better. The limit is 1: Conclusion: $( 1 + 1 / n ) ^ { n }$ approaches the number whose logarithm is 1: Sections 6:2 and 6:4 define the same number (which is $e$ ).

# 2. Slow method for $( 1 + 1 / n ) ^ { n }$ : Multiply out all theterms. Then let $n  \infty$ .

This is a brutal use of the binomial theorem. It involves nothing smart like logarithms, but the result is a fantastic new formula for $e$ :

$$
{ \mathrm { P r a c t i c e ~ f o r ~ } } n = 3 : \quad \left( 1 + { \frac { 1 } { 3 } } \right) ^ { 3 } = 1 + 3 \left( { \frac { 1 } { 3 } } \right) + { \frac { 3 \cdot 2 } { 1 \cdot 2 } } \left( { \frac { 1 } { 3 } } \right) ^ { 2 } + { \frac { 3 \cdot 2 \cdot 1 } { 1 \cdot 2 \cdot 3 } } \left( { \frac { 1 } { 3 } } \right) ^ { 3 } .
$$

Binomial theorem for any positive integer $n$ :

$$
\left( 1 + { \frac { 1 } { n } } \right) ^ { n } = 1 + n \left( { \frac { 1 } { n } } \right) + { \frac { n ( n - 1 ) } { 1 \cdot 2 } } \left( { \frac { 1 } { n } } \right) ^ { 2 } + { \frac { n ( n - 1 ) ( n - 2 ) } { 1 \cdot 2 \cdot 3 } } \left( { \frac { 1 } { n } } \right) ^ { 3 } + \cdots + \left( { \frac { 1 } { n } } \right) ^ { n } .
$$

Each term in equation(4) approaches a limit as $n \to \infty$ : Typical terms are

$$
\frac { n ( n - 1 ) } { 1 \cdot 2 } \left( \frac { 1 } { n } \right) ^ { 2 } \to \frac { 1 } { 1 \cdot 2 } \qquad \mathrm { a n d } \qquad \frac { n ( n - 1 ) ( n - 2 ) } { 1 \cdot 2 \cdot 3 } \left( \frac { 1 } { n } \right) ^ { 3 } \to \frac { 1 } { 1 \cdot 2 \cdot 3 } .
$$

Next comes $1 / 1 \cdot 2 \cdot 3 \cdot 4$ : The su8m of all those limits in (4) is our new formula for $e$ :

$$
\operatorname* { l i m } { \left( 1 + { \frac { 1 } { n } } \right) ^ { n } } = 1 + 1 + { \frac { 1 } { 1 \cdot 2 } } + { \frac { 1 } { 1 \cdot 2 \cdot 3 } } + { \frac { 1 } { 1 \cdot 2 \cdot 3 \cdot 4 } } + \cdots = e .
$$

In summation notation this is $\Sigma _ { k = 0 } ^ { \infty } 1 / k ! = e$ : The factorials give fast convergence:

$$
1 + 1 + . 5 + . 1 6 6 6 7 + . 0 4 1 6 7 + . 0 0 8 3 3 + . 0 0 1 3 9 + . 0 0 0 2 0 + . 0 0 0 0 2 = 2 . 7 1 8 2 8 .
$$

Those nine terms give an accuracy that was not reached by $n = 3 6 5$ compoundings. A limit is still involved (to add up the whole series). You never see e without a limit! It can be defined by derivatives or integrals or powers $( 1 + 1 / n ) ^ { n }$ or by an infinite series. Something goes to zero or infinity, and care is required.

All terms in equation (4) are below (or equal to) the corresponding terms in (5). The power $( 1 + 1 / n ) ^ { n }$ approaches e from below. There is a steady increase with $n$ : Faster compounding yields more interest. Continuous compounding at $100 \%$ yields $e$ ; as each term in (4) moves up to its limit in (5).

Remark Change $( 1 + 1 / n ) ^ { n }$ to $( 1 + x / n ) ^ { n }$ : Now the binomial theorem produces ex:

$$
\left( 1 + { \frac { x } { n } } \right) ^ { n } = 1 + n \left( { \frac { x } { n } } \right) + { \frac { n ( n - 1 ) } { 1 \cdot 2 } } \left( { \frac { x } { n } } \right) ^ { 2 } + \cdots { \mathrm { ~ a p p r o a c h e s ~ } } 1 + x + { \frac { x ^ { 2 } } { 1 \cdot 2 } } + \cdots .
$$

Please recognize $e ^ { x }$ on the right side! It is the infinite power series in equation (1). The next term is $x ^ { 3 } / 6$ ( $x$ can be positive or negative). This is a final formula for $e ^ { x }$ :

6L The limit of $( 1 + x / n ) ^ { n }$ is $e ^ { x }$ : At $x = 1$ we find $e$ :

The logarithm of that power is $n$ $\iota \ln ( 1 + x / n ) \approx n ( x / n ) = x .$ : The power approaches $e ^ { x }$ : To summarize: The quick method proves $( 1 + 1 / n ) ^ { n } \to e$ by logarithms. The slow method (multiplying out every term) led to the infinite series. Together they show the agreement of all our definitions of $e$ :

# DIFFERENCE EQUATIONS VS. DIFFERENTIAL EQUATIONS

We have the chance to see an important part of applied mathematics. This is not a course on differential equations, and it cannot become a course on difference equations. But it is a course with a purpose—we aim to use what we know. Our main application of $e$ was to solve $y ^ { \prime } = c y$ and $y ^ { \prime } { = } c y + s$ : Now we solve the corresponding difference equations.

Above all, the goal is to see the connections. The purpose of mathematics is to understand and explain patterns. The path from “discrete to continuous” is beautifully illustrated by these equations. Not every class will pursue them to the end, but I cannot fail to show the pattern in a difference equation:

$$
y ( t + 1 ) = a y ( t ) .
$$

Each step multiplies by the same number $a$ : The starting value $y _ { 0 }$ is followed by $a y _ { 0 } , a ^ { 2 } y _ { 0 }$ , and ${ \bar { a } } ^ { 3 } y _ { 0 }$ : The solution at discrete times $t = 0 , 1 , 2 , \ldots$ is $y ( t ) = a ^ { t } y _ { 0 }$ :

This formula $a ^ { t } y _ { 0 }$ replaces the continuous solution $e ^ { c t } y _ { 0 }$ of the differential equation.

$$
\overbrace  \underbrace { \mathrm { g r o w i n g } } _ { \mathrm { o s c i l l a k o } } \int \underbrace { \mathrm { e } ^ { - \mathrm { o s c i l l a t i o n } } } _ { - 1 } \mathrm { d e c a y } \underbrace { \mathrm { e } ^ { - \pi } \mathrm { g r o w t h } } _ { \textit { o s c i l l a k o } } \cdots \mathrm { d }
$$

A source or sink (birth or death, deposit or withdrawal) is like $y ^ { \prime } = c y + s$ :

$$
y ( t + 1 ) = a y ( t ) + s .
$$

Each step multiplies by $a$ and adds $s$ : The first outputs are

$$
y \left( 1 \right) = a y _ { 0 } + s , \quad y \left( 2 \right) = a ^ { 2 } y _ { 0 } + a s + s , \quad y \left( 3 \right) = a ^ { 3 } y _ { 0 } + a ^ { 2 } s + a s + s .
$$

We saw this pattern for differential equations—every input $s$ becomes a new starting point. It is multiplied by powers of $a$ : Since $s$ enters later than $y _ { 0 }$ ; the powers

stop at $t - 1$ : Algebra turns the sum into a clean formula by adding the geometric series:

$$
y ( t ) = a ^ { t } y _ { 0 } + s \left[ a ^ { t - 1 } + a ^ { t - 2 } + \cdots + a + 1 \right] = a ^ { t } y _ { 0 } + s ( a ^ { t } - 1 ) / ( a - 1 ) .
$$

EXAMPLE 1 Interest at $8 \%$ from annual IRA deposits of $s = \$ 2000$ (here $y _ { 0 } = 0$ ).

The first deposit is at year $t = 1$ : In a year it is multiplied by $a = 1 . 0 8$ ; because $8 \%$ is added. At the same time a new $s = 2 0 0 0$ goes in. At $t = 3$ the first deposit has been multiplied by $( 1 . 0 8 ) ^ { 2 }$ ; the second by 1:08; and there is another $s = 2 0 0 0$ : After year $t$ ;

$$
y ( t ) = 2 0 0 0 ( 1 . 0 8 ^ { t } - 1 ) / ( 1 . 0 8 - 1 ) .
$$

With $t = 1$ this is 2000: With $t = 2$ it is 2000 . $( 1 . 0 8 + 1 ) \$ —two deposits. Notice how $a - 1$ (the interest rate :08) appears in the denominator.

EXAMPLE 2 Approach to steady state when $| a | < 1 .$ Compare with $c < 0$ :

With $a > 1$ ; everything has been increasing. That corresponds to $c > 0$ in the differential equation (which is growth). But things die, and moneyis spent, so $a$ can be smaller than one. In that case $a ^ { t } y _ { 0 }$ approaches zero—the starting balance disappears. WhÑat8happens if there is also a source ? Every year half of the balance $y ( t )$ is spent and a new $\$ 2000$ is deposited. Now $\begin{array} { r } { a = \frac { 1 } { 2 } } \end{array}$ :

$$
\begin{array} { r } { y ( t + 1 ) = \frac { 1 } { 2 } y ( t ) + 2 0 0 0 \quad \mathrm { y i e l d s } \quad y ( t ) = \left( \frac { 1 } { 2 } \right) ^ { t } y _ { 0 } + 2 0 0 0 \Big [ \big ( \left( \frac { 1 } { 2 } \right) ^ { t } - 1 \big ) / \left( \frac { 1 } { 2 } - 1 \right) \Big ] . } \end{array}
$$

The limit as $t \to \infty$ is an equilibrium point. As $\begin{array} { l } { \left( { \frac { 1 } { 2 } } \right) ^ { t } } \end{array}$ goes to z8ero, $y ( t )$ stabilizes to

$$
y _ { \infty } = 2 0 0 0 { \bigl ( } 0 - 1 { \bigr ) } / { \bigl ( } { \textstyle } { \frac { 1 } { 2 } } - 1 { \bigr ) } = 4 0 0 0 = s t e a d y s t a t e .
$$

Why8is 4000 steady ? Because half is lost an8d the new 2000 makes it up again. The iteration is $y _ { n + 1 } = { \frac { 1 } { 2 } } y _ { n } + 2 0 0 0$ : Its fixed point iswhere $y _ { \infty } = { \textstyle \frac { 1 } { 2 } } y _ { \infty } \dot { + } 2 0 0 0$ .

In general the steady equation is $y _ { \infty } = a y _ { \infty } + s$ : Solving for $y _ { \infty }$ gives $s / ( 1 - a )$ : Compare with the steady differential equation $y ^ { \prime } = c y + s = 0$ :

$$
y _ { \infty } = - { \frac { s } { c } } ( { \mathrm { d i f f e r e n t i a l ~ e q u a t i o n } } ) \quad \nu s . \quad y _ { \infty } = { \frac { s } { 1 - a } } ( { \mathrm { d i f f e r e n c e ~ e q u a t i o n } } ) .
$$

EXAMPLE 3 Demand equals supply when the price is right.

Difference equations are basic to economics. Decisions are madeevery year (by a farmer) or every day (by a bank) or every minute (by the stock market). There are three assumptions:

1. Supply next time depends on price this time: $S ( t + 1 ) = c P ( t )$ :   
2. Demand next time depends on price next time: $D ( t + 1 ) = - d P ( t + 1 ) + b$ :   
3. Demand next time equals supply next time: $D ( t + 1 ) = S ( t + 1 )$ :

Comment on 3: the price sets itself to make $d e m a n d = s u p p l y$ . The demand slope $- d$ is negative. The supply slope $c$ isposit8ive. Those l8ines interse8ct at the competitive price, where supply equals demand. To find the difference equation, substitute 1 and 2 into 3:



If the price starts above $P _ { \infty }$ ; the difference equation brings it down. If below, the price goes up. When the price is $P _ { \infty }$ ; it stays there. This is not news—economic

theory depends on approach to a steady state. But convergence only occurs if $c < d$ : If supply is less sensitive than demand, the economy is stable.

Blow-up example: $c = 2$ , $b = d = 1$ : The difference equation is $- P ( t + 1 ) + 1 =$ $2 P ( t )$ : From $P ( 0 ) = 1$ the price oscillates as it grows: $P = - 1 , 3 , - 5 , 1 1 , . . . .$

Stable example: $c = 1 / 2 , \ b = d = 1$ : The price moves from $P ( 0 ) = 1$ to $P ( \infty ) = 2 / 3$ :

$$
- P ( t + 1 ) + 1 = { \frac { 1 } { 2 } } P ( t ) \mathrm { y i e l d s } P = 1 , { \frac { 1 } { 2 } } , { \frac { 3 } { 4 } } , { \frac { 5 } { 8 } } , \dots , \mathrm { a p p r o a c h i n g } { \frac { 2 } { 3 } } .
$$

Increasing $d$ gives greater stability. That is the effect of price supports. For $d = 0$ (fixed demand regardless of price) the economy is out of control.

# THE MATHEMATICS OF FINANCE

It would be a pleasure to make this supply-demand model more realistic—with curves, not straight lines. Stability depends on the slope—calculus enters. But we also have to be realistic about class time. I believe the most practical application is to solve the fundamental problems of finance. Section 6.3 answered six questions about continuous interest. We now answer the same six questions when the annual rate is $x = . 0 5 = 5 \%$ and interest is compounded n times a year.

First we compute effective rates, higher than :05 because of compounding:

$$
\begin{array} { l } { { \mathrm { c o m p o u n d e d ~ } q u a r t e r l y } \displaystyle \left( 1 + \frac { . 0 5 } { 4 } \right) ^ { 4 } = 1 . 0 5 0 9 ~ \left[ e f f e c t i v e ~ r a t e . 0 5 0 9 = 5 . 0 9 \% \right] } \\ { { \mathrm { c o m p o u n d e d ~ } c o n t i n u o u s l y } \quad { { e } ^ { . 0 5 } = 1 . 0 5 1 3 } } \end{array}
$$

Now come the six questions. Next to the new answer (discrete) we write the old answer (continuous). One is algebra, the other is calculus. The time period is 20 years, so simple interest on $y _ { 0 }$ would produce $( . 0 5 ) ( 2 0 ) ( y _ { 0 } ) .$ That equals $y _ { 0 }$ —money doubles in 20 years at $5 \%$ simple interest.

Questions 1 and 2 ask for the future value $y$ and present value $y _ { 0 }$ with compound interest n times a year:

$$
{ \begin{array} { r l r l } & { \mathbf { 1 } . \ y \ { \mathrm { g r o w i n g ~ f r o m } } \ y _ { 0 } \colon } & & { y = \left( 1 + { \frac { . 0 5 } { n } } \right) ^ { 2 0 n } \ y _ { 0 } \qquad } & & { y = e ^ { ( . 0 5 ) ( 2 0 ) } y _ { 0 } } \\ & { } & & { } \\ & { \qquad 2 . \ \scriptstyle { \mathrm { d e p o s i t ~ } } y _ { 0 } { \mathrm { ~ t o ~ r e a c h ~ } } y \colon } & & { y _ { 0 } = \left( 1 + { \frac { . 0 5 } { n } } \right) ^ { - 2 0 n } \ y } & & { y _ { 0 } = e ^ { - ( . 0 5 ) ( 2 0 ) } y } \end{array} }
$$

Each step multiplies by $a = ( 1 + . 0 5 / n )$ : There are $2 0 n$  steps in 20 years. Time goes backward in Question 2. We divide by the growth factor instead of multiplying. The future value is greater than the present value (unless the interest rate is negative!). As $n \to \infty$ the discrete $y$ on the left approaches the continuous $y$ on the right.

Questions 3 and 4 connect $y$ to $s$ (with $y _ { 0 } = 0$ at the start). As soon as each $s$ is deposited, it starts growing. Then $y = s + a s + a ^ { 2 } s + \cdots$

$$
\begin{array} { r l r l } & { \mathrm { 3 . ~ y ~ g r o w i n g ~ f r o m ~ d e p o s i t s } s \colon } & & { y = s \Biggl [ \frac { ( 1 + . 0 5 / n ) ^ { 2 0 n } - 1 } { . 0 5 / n } \Biggr ] } & & { y = s \Biggl [ \frac { e ^ { ( . 0 5 ) ( 2 0 ) } - 1 } { . 0 5 } \Biggr ] } \\ & { \mathrm { 4 . ~ d e p o s i t s ~ } s \mathrm { ~ t o ~ r e a c h ~ } y \colon } & & { s = y \Biggl [ \frac { . 0 5 / n } { ( 1 + . 0 5 / n ) ^ { 2 0 n } - 1 } \Biggr ] } & & { s = y \Biggl [ \frac { . 0 5 } { e ^ { ( . 0 5 ) ( 2 0 ) } - 1 } \Biggr ] } \end{array}
$$

Questions 5 and 6 connect $y _ { 0 }$ to $s$ : This time $y$ is zero—there is nothing left at the end. Everything is paid. The deposit $y _ { 0 }$ is just enough to allow payments of $s$ : This is an annuity, where the bank earns interest on your $y _ { 0 }$ while it pays you $s$ $\dot { n }$ times a year for 20 years). So your deposit in Question 5 is less than $2 0 n s$ :

Question 6 is the opposite—a loan. At the start you borrow $y _ { 0 }$ (instead of giving the bank $y _ { 0 }$ ). You canearn interest on it as you pay it back.Therefore your payments have to total more than $y _ { 0 }$ : This is the calculation for car loans and mortgages.

5: Annuity: Deposit $y _ { 0 }$ to receive $2 0 n$ payments of $s$ :

$$
y _ { 0 } = s \Bigg [ \frac { 1 - ( 1 + . 0 5 / n ) ^ { - 2 0 n } } { . 0 5 / n } \Bigg ] \qquad y _ { 0 } = s \Bigg [ \frac { 1 - e ^ { - ( . 0 5 ) ( 2 0 ) } } { . 0 5 } \Bigg ]
$$

6: Loan: Repay $y _ { 0 }$ with $2 0 n$ payments of $s$ :

$$
s = y _ { 0 } \biggl [ \frac { . 0 5 / n } { 1 - ( 1 + . 0 5 / n ) ^ { - 2 0 n } } \biggr ] \qquad s = y _ { 0 } \biggl [ \frac { . 0 5 } { 1 - e ^ { - ( . 0 5 ) ( 2 0 ) } } \biggr ]
$$

Questions $^ { 2 , 4 , 6 }$ are the inverses of 1; 3; 5: Notice the pattern: There are three numbers $y , y _ { 0 }$ ; and $s$ : One of them is zero each time. If all three are present, go back to equation (9).

The algebra for these lines is in the exercises. $I t$ is not calculus because $\Delta t$ is not $d t$ . All factors in brackets $\big [ \begin{array} { l l } \end{array} \big ]$ are listed in tables, and the banks keep copies. It might also be helpful to know their symbols. If a bank has interest rate $i$ per period over $N$ periods, then in our notation $a = 1 + i = 1 + . 0 5 / n$ and $t = N = 2 0 n$ :

$$
{ \mathrm { ; ~ o f ~ } } s = \ S 1 \left( \operatorname* { l i n e } 3 \right) : y ( N ) = s _ { N \left. i \right. } = \left[ ( 1 + i ) ^ { N } - 1 \right] / i
$$

$$
\dot { s } = \mathfrak { H } \left( \operatorname { l i n e } \mathfrak { H } \right) : y _ { 0 } = a _ { N } ] _ { i } = \left[ 1 - ( 1 + i ) ^ { - N } \right] / i
$$

To tell the truth, I never knew the last two formulas until writing this book. The mortgage on my home has $N = ( 1 2 ) ( 2 5 )$ monthly payments with interest rate $i = . 0 7 / 1 2$ : In 1972 the present value was $\$ 42,000$ amount borrowed. I am now going to see if the bank is honest.

Remark In many loans, the bank computes interest on the amount paid back instead of the amount received. This is called discounting. A loan of $\$ 1000$ at $5 \%$ for one year costs $\$ 50$ interest. Normally you receive $\$ 1000$ and pay back $\$ 1050$ : With discounting you receive $\$ 950$ (called the proceeds) and you pay back $\$ 1000$ : The true interest rate is higher than $5 \%$ —because the $\$ 50$ interest is paid on the smaller amount $\$ 950$ : In this case the “discount rate” is $5 0 / 9 5 0 = 5 . 2 6 \%$ :

# SCIENTIFIC COMPUTING: DIFFERENTIAL EQUATIONS BY DIFFERENCE EQUATIONS

In biology and business, most events are discrete. In engineering and physics, time and space are continuous. Maybe at some quantum level it’s all the same, but the

equations of physics (starting with Newton’s law $F = m a$ ) are differential equations.   
The great contribution of calculus is to model the rates of change we see in nature.   
But to solve that model with a computer, it needs to be made digital and discrete.

These paragraphs work with $d y / d t = c y$ : It is the test equation that all analysts use, as soon as a new computing method is proposed. Its solution is $y = e ^ { c t }$ ; starting from $y _ { 0 } = 1$ : Here we test Euler’s method (nearly ancient, and not well thought of). He replaced $d y / d t$ by $\Delta y / \Delta t$ :

$$
\mathbf { E u l e r ^ { * } s . M e t h o d } \qquad \varliminf _ { \Delta t } - y ( t ) = c y ( t ) .
$$

The left side is $d y / d t$ ; in the limit $\Delta t \to 0$ : We stop earlier, when $\Delta t > 0$

The problem is to solve (13). Multiplying by $\Delta t$ ; the equation is

$$
y ( t + \Delta t ) = ( 1 + c \Delta t ) y ( t ) \qquad ( \mathrm { w i t h } y ( 0 ) = 1 ) .
$$

Each step multiplies by $a = 1 + c \Delta t$ ; so $n$ steps multiply by $a ^ { n }$ :

$$
y = a ^ { n } = ( 1 + c \Delta t ) ^ { n } { \mathrm { ~ a t ~ t i m e } } n \Delta t .
$$

This is growth or decay, depending on $a$ : The correct $e ^ { c t }$ is growth or decay, depending on $c$ : The question is whether $a ^ { n }$ and $e ^ { c t }$ stay close. Can one of them grow while the other decays ? We expect the difference equation to copy $y ^ { \prime } = c y$ ; but we might be wrong.

A good example is $y ^ { \prime } = - y$ :Then $c = - 1$ and $y = e ^ { - t }$ —the true solution decays. The calculator gives the following answers $a ^ { n }$ for $n = 2 , 1 0 , 2 0$ :

The big step $\Delta t = 3$ shows total instability (top row). The numbers blowup when they should decay. The row with $\Delta t = 1$ is equally useless (all zeros). In practice the magnitude of $c \Delta t$ must come down to .10 or .05: For accurate calculations it would have to be even smaller, unless we change to a better difference equation. That is the right thing to do.

Noticethe two reasonable numbers. They are :35 and :36; approÑaching $e ^ { - 1 } = . 3 7$ : They come from $n = 1 0$ (with $\Delta t = 1 / 1 0$ ) and $n = 2 0$ (with $\Delta t = 1 / 2 0 \$ ). Those have the same clock time $n \Delta t = 1$ :

$$
\left( 1 - { \frac { 1 } { 1 0 } } \right) ^ { 1 0 } = . 3 5 \qquad \left( 1 - { \frac { 1 } { 2 0 } } \right) ^ { 2 0 } = . 3 6 \qquad \left( 1 - { \frac { 1 } { n } } \right) ^ { n } \to e ^ { - 1 } = . 3 7 .
$$

The main diagonal of the table is executing $( 1 + x / n ) ^ { n } \to e ^ { x }$ in the case $x = - 1$ :

Final question: How quickly are :35 and :36 converging to $e ^ { - 1 } = . 3 7 \cdot 2$ With $\Delta t = . 1 0$ the error is :02: With $\Delta t = . 0 5$ the error is :01: Cutting the time step in half cuts the error in half. We are not keeping enough digits to be sure, but the

error seems close to $\scriptstyle { \frac { 1 } { 5 } } \Delta t$ : To test that, apply the “quick method” and estimate $a ^ { n } = ( 1 - \Delta t ) ^ { n }$ from its logarithm:

$$
\begin{array} { r } { \ln ( 1 - \Delta t ) ^ { n } = n \ln ( 1 - \Delta t ) \approx n \Big [ - \Delta t - \frac 1 2 \big ( \Delta t \big ) ^ { 2 } \Big ] = - 1 - \frac 1 2 \Delta t . } \end{array}
$$

The clock time is $n \Delta t = 1$ : Now take exponentials of the far left and right:

$$
a ^ { n } = ( 1 - \Delta t ) ^ { n } \approx e ^ { - 1 } e ^ { - \Delta t / 2 } \approx e ^ { - 1 } \big ( 1 - { \textstyle \frac { 1 } { 2 } } \Delta t \big ) .
$$

The difference between $a ^ { n }$ and $e ^ { - 1 }$ is the last term $\scriptstyle { \frac { 1 } { 2 } } \Delta t e ^ { - 1 }$ : Everything comes down to one question: Is that error the same as $\begin{array} { r } { \frac { 1 } { 5 } \Delta t \mathrm { ~ ? ~ } } \end{array}$ The answer is yes, because $e ^ { - 1 } / 2$ is $1 / 5$ : If we keep only one digit, the prediction is perfect!

That took an hour to work out, and I hope it takes longer than $\Delta t$ to read. I wanted you to see in use the properties of ln $x$ and $e ^ { x }$ : The exact property ln $a ^ { n } = n$ ln $a$ came first. In the middle of (15) was the key approximation $\ln ( 1 + x ) \approx x - { \textstyle { \frac { 1 } { 2 } } } x ^ { 2 }$ ; with $x = - \Delta t$ : That $x ^ { 2 }$ term uses the second derivative (Section 6.4). At the very end came $e ^ { x } \approx 1 + x$ :

A linear approximation shows convergence: $( 1 + x / n ) ^ { n } \to e ^ { x }$ : A quadratic shows the error: proportional to $\Delta t = 1 / n$ : It is like using rectangles for areas, with error proportional to $\Delta x$ : This minimal accuracy was enough to define the integral, and here it is enough to define $e$ : It is completely unacceptablefor scientific computing.

The trapezoidal rule, for integrals or for $y ^ { \prime } = c y$ ; has errors of order $( \bar { \Delta x } ) ^ { 2 }$ and $( \Delta t ) ^ { 2 }$ : All good software goes further than that. Euler’s first-order method could not predict the weather before it happens.

$$
\cdot { \frac { d y } { d t } } = F ( y , t ) : \quad { \frac { y \left( t + \Delta t \right) - y ( t ) } { \Delta t } } = F ( y ( t ) , t ) .
$$