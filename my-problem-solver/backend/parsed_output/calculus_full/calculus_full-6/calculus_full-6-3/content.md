# 6.3 Growth and Decay in Science and Economics

The derivative of $y = e ^ { c x }$ has taken time and effort. The result was $y ^ { \prime } = c e ^ { c x }$ ; which means that $y ^ { \prime } = c y$ . That computation brought others with it, virtually for free—the derivatives of $b ^ { x }$ and $x ^ { x }$ and $e ^ { \overset { . } { u } ( x ) }$ : But I want to stay with $y ^ { \prime } = c y$ —which is the most important differential equation in applied mathematics.

Compare $y ^ { \prime } = x$ with $y ^ { \prime } = y$ . The first only asks for an antiderivative of $x$ : We quickly find $\begin{array} { r } { y = \frac { 1 } { 2 } x ^ { 2 } + C } \end{array}$ : The second has $d y / d x$ equal to $y$ itself—which we rewrite as $d y / y = d x$ : The integral is in $y = x + C$ : Then $y$ itself is $e ^ { x } e ^ { c }$ : Notice that the first solution is ${ \frac { 1 } { 2 } } x ^ { 2 } p l u s$ 1a constant, and the second solution is $e ^ { x }$ times a constant.

There is a way to graph slope $x$ versus slope $y$ : Figure 6.7 shows “tangent arrows,” which give the slope at each $x$ and $y$ : For parabolas, the arrows grow steeper as $x$ grows—because $y ^ { \prime } { = } { \mathrm { s l o p e } } = x$ : For exponentials, the arrows grow steeper as $y$ grows—the equation is $y ^ { \prime } { = } { \mathrm { s l o p e } } = y$ : Now the arrows are connected by $y = A e ^ { x }$ : A differential equation gives a field of arrows (slopes). Its solution is a curve that stays tangent to the arrows—then the curve has the right slope.

A field of arrows can show many solutions at once (this comes in a differential equations course). Usually a single $y _ { 0 }$ is not sacred. To understand the equation we start from many $y _ { 0 }$ —on the left the parabolas stay parallel, on the right the heights stay proportional. For $y ^ { \prime } = - y$ all solution curves go to zero.

From $y ^ { \prime } = y$ it is a short step to $y ^ { \prime } = c y$ : To make $c$ appear in the derivative, put $c$ into the exponent. The derivative of $y = e ^ { c x }$ is $c e ^ { c x }$ ; which is $c$ times $y$ : We have reached the key equation, which comes with an initial condition—a starting value $y _ { 0 }$ :

$$
d y / d t = c y { \mathrm { ~ w i t h ~ } } y = y _ { 0 } { \mathrm { ~ a t ~ } } t = 0 .
$$

A small change: $x$ has switched to $t$ : In most applications time is the natural variable, rather than space. The factor $c$ becomes the “growth rate” or “decay rate”—and $e ^ { c x }$ converts to ect :

The last step is to match the initial condition. The problem requires $y = y _ { 0 }$ at $t = 0$ : Our $e ^ { c t }$ starts from $e ^ { c 0 } = 1$ : The consta1nt of integration is needed now—the solutions are $y = A e ^ { c t }$ : By choosing $A = y _ { 0 }$ , we match the initial condition and solve equation (1). The formula to remember is $y _ { 0 } e ^ { c t }$ :

6I The exponential law $y = y _ { 0 } e ^ { c t }$ solves $y ^ { \prime } = c y$ starting from $y _ { 0 }$ :

The rate of growth or decay is $c$ : May I call your attention to a basic fact ? The formula $y _ { 0 } e ^ { c t }$ contains three quantities $y _ { 0 } , c , t$ : If two of them are given, plus one additional piece of information, the third is determined. Manyapplications have one of these three forms: find $t$ , find $c$ , find $y _ { 0 }$ :

1. Find the doubling time $T$ if $c = 1 / 1 0$ : At that time $y _ { 0 } e ^ { c T }$ equals $2 y _ { 0 }$ :

$$
e ^ { c T } = 2 { \mathrm { ~ y i e l d s ~ } } c T = \ln 2 { \mathrm { ~ s o ~ t h a t ~ } } T = { \frac { \ln 2 } { c } } \approx { \frac { . 7 } { . 1 } } .
$$

The question asks for an exponent $T .$ The answer involves logarithms. If a cell grows at a continuous rate of $c = 1 0 \%$ per day, it takes about : $7 / . 1 = 7$ days to double in size. (Note that :7 is close to ln 2:) If a savings account earns $10 \%$ continuous interest, it doubles in 7 years.

In this problem we knew $c$ : In the next problem we know $T _ { \mathbf { \delta } }$ :

2. Find the decay constant $c$ for carbon-14 if $\begin{array} { r } { y = \frac 1 2 y _ { 0 } } \end{array}$ in $T = 5 5 6 8$ years.

$$
e ^ { c T } = { \textstyle { \frac { 1 } { 2 } } } { \mathrm { ~ y i e l d s ~ } } c T = \ln { \textstyle { \frac { 1 } { 2 } } } { \mathrm { ~ s o ~ t h a t ~ } } c \approx \left( \ln { \textstyle { \frac { 1 } { 2 } } } \right) / { 5 5 6 8 } .
$$

After the half-life $T = 5 5 6 8$ , the factor $e ^ { c T }$ equals $\frac { 1 } { 2 }$ : Now $c$ is negative $\begin{array} { r l } {  { ( \ln { \frac { 1 } { 2 } } = } } & { { } } \end{array}$ $- \ln 2 )$ :

Question 1 was about growth. Question 2 was about decay. Both answers found $e ^ { c T }$ as the ratio $y ( T ) / y ( 0 )$ : Then $c T$ is its logarithm. Note how $c$ sticks to $T .$ : $T$ has the units of time, $c$ has the units of “1=time:”

Main point: The doubling time is $( \ln 2 ) / c$ , because $c T = \ln 2$ : The time to multiply by $e$ is $1 / c$ : The time to multiply by 10 is $( \ln { 1 0 } ) / c$ : The time to divide by $e$ is $- 1 / c$ , when a negative $c$ brings decay.

3. Find the initial value $y _ { 0 }$ if $c = 2$ and $y ( 1 ) = 5$ :

All we do is run the process backward. Start from 5 and go back to $y _ { 0 }$ : With time reversed, $e ^ { c t }$ becomes $e ^ { - c t }$ : The product of $e ^ { 2 }$ and $e ^ { - 2 }$ is 1—growth forward and decay backward.

Equally important is $T + t$ : Go forward to time $T$ and go on to $T + t$ :

$$
y ( T + t ) { \mathrm { ~ i s ~ } } y _ { 0 } e ^ { c ( T + t ) } { \mathrm { ~ w h i c h ~ i s ~ } } ( y _ { 0 } e ^ { c T } ) e ^ { c t } .
$$

Ever step $t$ ; at the start or later, multiplies by the same $e ^ { c t }$ : This uses the fundamental property of exponentials, that $e ^ { T + t } = e ^ { T } e ^ { { \dot { t } } }$ :

EXAMPL¡E 1 Population growth from birth rate $b$ and death rate $d$ (both constant):

$$
d y / d t = b y - d y = c y \quad { \mathrm { ( t h e ~ n e t ~ r a t e ~ i s ~ } } c = b - d { \mathrm { ) } } .
$$

The population in this model is $y _ { 0 } e ^ { c t } = y _ { 0 } e ^ { b t } e ^ { - d t }$ : It grows when $b > d$ (which makes $c > 0$ ). One estimate of the growth rate is $c = 0 . 0 2$ =year:

The earth’s population doubles in about $T = { \frac { \ln 2 } { c } } \approx { \frac { . 7 } { . 0 2 } } = 3 5 y e a r s .$

First comment: W1 e predict the future based on $c$ : We count the past population to find $c$ : Changes in $c$ are a serious problem for this model.

Second comment: $y _ { 0 } e ^ { c t }$ is not a whole number. You may prefer to think of bacteria instead of people. (This section begins a m1ajor application of mathematics to economics and the life sciences.) Malthus based his theory of human population on this equation $y ^ { \prime } = c y$ —and with large numbers a fraction of a person doesn’t matter so much. To use calculus we go from discrete to continuous. The theory must fail when $t$ is very large, since populations cannot grow exponentially forever. Section 6.5 introduces the logistic equation $y ^ { \prime } { = } c y - b y ^ { 2 }$ , with a competition term $- b y ^ { 2 }$ to slow the growth.

Third comment: The dimensions of $b , c , d$ are “1=time.” The dictionary gives birth rate $\ b =$ number of births per person in a unit of time. It is a relative rate—people divided by people and time. The product $c t$ is dimensionless and $e ^ { c t }$ makes sense (also dimensionless). Some texts replace $c$ by $\lambda$ (lambda). Then $1 / \lambda$ is the growth time or decay time or drug elimination time or diffusion time.

EXAMPLE 2 Radioactive dating A gram of charcoal from the cave paintings in France gives 0:97 disintegrations per minute. A gram of living wood gives 6:68 disintegrations per minute. Find the age of those Lascaux paintings.

The charcoal stopped adding radiocarbon when it was burned (at $t = 0$ ). The amount has decayed to $y _ { 0 } e ^ { c t }$ : In living wood this amount is still $y _ { 0 }$ ; because cosmic rays maintain the balance. Their ratio is $e ^ { c t } = 0 . 9 7 / 6 . 6 8 .$ Knowing the decay rate $c$ from Question 2 above, we know the present time $t$ :

$$
c t = \ln \left( { \frac { 0 . 9 7 } { 6 . 6 8 } } \right) \quad { \mathrm { y i e l d s } } \quad t = { \frac { 5 5 6 8 } { - . 7 } } \ln \left( { \frac { 0 . 9 7 } { 6 . 6 8 } } \right) = 1 4 , 4 0 0 { \mathrm { y e a r s } } .
$$

Here is a related problem—the age of uranium. Right now there is 140 times as much U-238 as U-235. Nearly equal amounts were created, with half-lives of $( 4 . 5 ) 1 0 ^ { 9 }$ and $( 0 . 7 ) 1 0 ^ { 9 }$ years. Question: How long since uranium was created ? Answer: Find $t$ by substituting $c = \overline { { ( \ln { \frac { 1 } { 2 } } ) } } / ( 4 . 5 ) 1 0 ^ { 9 }$ and $C = ( \ln { \frac { 1 } { 2 } } ) / ( 0 . 7 ) 1 0 ^ { 9 }$ :

$$
e ^ { c t } / e ^ { C t } = 1 4 0 \Rightarrow c t - C t = \ln 1 4 0 \Rightarrow t = { \frac { \ln 1 4 0 } { c - C } } = 6 ( 1 0 ^ { 9 } )
$$

EXAMPLE 3 Calculus in Economics: price inflation and the value of money

We begin with two inflation rates—a continuous rate and an annual rate. For the price change $\Delta y$ over a year, use the annual rate:

$$
\Delta y = ( a n n u a l r a t e ) \ { \mathrm { ~ t i m e s ~ } } \left( y \right) \ { \mathrm { t i m e s ~ } } ( \Delta t ) .
$$

Calculus applies the continuous rate to each instant $d t$ : The price change is $d y$ :

$$
d y = ( c o n t i n u o u s r a t e ) { \mathrm { ~ t i m e s ~ } } ( y ) { \mathrm { ~ t i m e s ~ } } ( d t ) .
$$

Dividing by $d t$ , this is a differential equation for the price:

$$
d y / d t = ( c o n t i n u o u s r a t e ) \mathrm { ~ t i m e s ~ } ( y ) = . 0 5 y .
$$

The solution is $y _ { 0 } e ^ { . 0 5 t }$ : Set $t = 1$ : Then $e ^ { . 0 5 } \approx 1 . 0 5 1 3$ and the annual rate is $5 . 1 3 \%$

When you ask a bank what interest they pay, they give both rates: $8 \%$ and $8 . 3 3 \%$ : The higher one they call the “effective rate.” It comes from compounding (and depends how often they do it). If the compounding is continuous, every $d t$ brings an increase of $d y$ —and $e ^ { . 0 8 }$ is near 1:0833:

Section 6.6 returns to compound interest. The interval drops from a month to a day to a second. That leads to $( 1 + 1 / n ) ^ { n }$ , and in the limit to $e$ : Here we compute the effect of $5 \%$ continuous interest:

Future value A dollar now has the same value as $e ^ { . 0 5 T }$ dollars in $T$ years.   
Present value A dollar in $T$ years has the same value as $e ^ { - . 0 5 T }$ dollars now.   
Doubling time Prices double . $\boldsymbol { e } ^ { . 0 5 T } = 2 ,$ / in $T = \ln 2 / . 0 5 \approx 1 4$ years.

With no compounding, the doubling time is 20 years. Simple interest adds on 20 times $5 \% = 1 0 0 \%$ : With continuous compounding the time is reduced by the factor ln $2 \approx . 7$ , regardless of the interest rate.

EXAMPLE 4 In 1626 the Indians sold Manhattan for $\$ 24$ : Our calculations indicate that they knew what they were doing. Assuming $8 \%$ compound interest, the original $\$ 24$ is multiplied by $e ^ { . 0 8 t }$ : After $t = 3 6 5$ years the multiplier is $e ^ { 2 9 . 2 }$ and the $\$ 24$ has grown to 115 trillion dollars. With that much money they could buy back the land and pay off the national debt.

This seems farfetched. Possibly there is a big flaw in the model. It is absolutely true that Ben Franklin left money to Boston and Philadelphia, to be invested for 200 years. In 1990 it yielded millions (not trillions, that takes longer). Our next step is a new model.

Question How can you estimate $e ^ { 2 9 . 2 }$ with a $\$ 24$ calculator (log but not ln) ? Answer Mult1iply 29:2 by $\log _ { 1 0 } e = . 4 3 4$ to get 12:7: This is the exponent to base 10. After that base change, we have $1 0 ^ { 1 2 . 7 }$ or more than a trillion.

# GROWTH OR DECAY WITH A SOURCE TERM

The equation $y ^ { \prime } = y$ will be given a new term. Up to now, all growth or decay has started from $y _ { 0 }$ : No deposit or withdrawal was made later. The investment grew by itself—a pure exponential. The new term s allows you to add or subtract from the account. It is a “source”—or a “sink” if $s$ is negative. The source $s = 5$ adds $5 d t$ , proportional to $d t$ but not to $y$ :



Constant source: $d y / d t = y + 5 { \mathrm { ~ s t a r t i n g ~ f r o m ~ } } y = y _ { 0 } .$

Notice $y$ on both sides! My first guess $y = e ^ { t + 5 }$ failed completely. Its derivative is $e ^ { t + 5 }$ again, which is not $y + 5$ : The class suggested $y = e ^ { t } + 5 t$ : But its derivative $e ^ { t } + 5$ is still not $y + 5$ : We tried other ways to produce 5 in $d y / d t$ : This idea is doomed to failure. Finally we thought of $y = A e ^ { t } - 5$ . That has $y ^ { \prime } = A e ^ { t } = y + 5$ as required.

Important: $A$ is not $y _ { 0 }$ . Set $t = 0$ to find $y _ { 0 } = A - 5$ : The source contributes $5 e ^ { t } -$ 5:

The solution is $( y _ { 0 } + 5 ) e ^ { t } - 5$ : That is the same as $y _ { 0 } e ^ { t } + 5 ( e ^ { t } - 1 )$ :

$s = 5$ multiplies the growt8h term $e ^ { t } - 1$ that starts at zero. $y _ { 0 } e ^ { t }$ grows8as before.

EXAMPLE 5 $d y / d t = - y + 5$ has $y = ( y _ { 0 } - 5 ) e ^ { - t } + 5$ : This is $y _ { 0 } e ^ { - t } + 5 ( 1 - e ^ { - t } )$ :

That final term from the source is still positive. The other term $y _ { 0 } e ^ { - t }$ decays to zero. The limit as $t \to \infty i s y _ { \infty } = 5$ . A negative $c$ leads to a steady state $y _ { \infty }$ :

Based on these examples with $c = 1$ and $c = - 1$ , we can find $y$ for any $c$ and $s$ .

$$
\mathrm { E Q U A T I O N ~ W I T H ~ S O U R C E } \quad \frac { d y } { d t } = c y + s \mathrm { ~ s t a r t s ~ f r o m ~ } y = y _ { 0 } \mathrm { ~ a t ~ } t = 0 . ( 7 ) \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ ~ } s \mathrm { ~ a t ~ } s \mathrm { ~ a t ~ ~ } s \mathrm { ~ a t ~ ~ } ~ s \mathrm { ~ a t ~ a t ~ ~ } ~ s \mathrm { ~ a t ~ ~ } ~ s ~ a t ~ ~ a t ~  \mathrm { ~ a t ~ ~ } ~ s \mathrm { ~ a t ~ a t ~ ~ ~ } ~ s ~ a t ~ a t ~ ~ ~ a t ~ ~  ~ s ~ a t ~ a t ~ s ~ a t ~ a t ~ ~ ~ a t ~ ~ ~ a t ~ ~ ~ a t ~ ~ a t ~ ~ a t ~ ~ a t ~ ~ a t ~ ~ ~ a t ~ ~ a t ~ a t ~ ~ a t ~ a t ~ ~ ~ a t ~ a t ~ a ~ a t ~ ~ a t ~ ~ a t ~ a ~ a t ~ a t ~ a ~ a t ~ a ~ s ~ a t ~ a t ~ a t ~ a ~ a t ~ a t ~ a t ~ a ~ a t ~ a ~ a t ~ a ~ a t ~ s ~ a t ~ a t ~ a t ~ a t ~ a ~ a t ~ a t ~ a t ~ a ~ a t ~ a ~ a t ~ a t ~ a t ~ a ~ a t ~ a t ~ a ~ a t ~ a ~ a t ~ a t ~ a ~ a t ~ a ~ a t ~ a t ~ a t ~ a ~ a t ~ a t ~ a t ~ a ~ a t ~ a ~ a t ~ a t 
$$

The source could be a deposit of $s = \$ 1000$ =year, after an initial investme1nt of $y _ { 0 } =$ $\$ 8000$ : Or we can withdraw funds at $s = - \$ 200,$ =year. The units are “dollars per year” to match $d y / d t$ : The equation feeds in $\$ 1000$ or removes $\$ 200$ continuously— not all at once.

Note again that $y = e ^ { ( c + s ) t }$ is not a solution. Its derivative is $( c + s ) y$ : The combination $y = e ^ { c t } + s$ is also not a solution (but closer). The analysis of $y ^ { \prime } = c y + s$ will be our main achievement for differential equations (in this section). The equation is not restricted to finance—far from it—but that produces excellent examples.

I propose to find $y$ in four ways. You may feel that one way is enough. $\dag$ The first way is the fastest—only thr1ee lines—but please give the others a chance. There is no point in preparing for real problems if we don’t solve them.

Solution by Method 1 (fast way) Substitute the combination $y = A e ^ { c t } + B$ : The solution has this form—exponential plus constant. From two facts we find $A$ and $B$ :

the equation $y ^ { \prime } { = } c y + s$ gives $c A e ^ { c t } = c ( A e ^ { c t } + B ) + s$ the initial value at $t = 0$ gives $A + B = y _ { 0 }$ :

The first line has $c A e ^ { c t }$ on both sides. Subtraction leaves $c B + s = 0$ , or $B = - s / c$ : Then the second line becomes $A = y _ { 0 } - B = y _ { 0 } + ( s / c )$ :

$$
y = \left( y _ { 0 } + { \frac { s } { c } } \right) e ^ { c t } - { \frac { s } { c } } \quad { \bf { o r } } \quad y = y _ { 0 } e ^ { c t } + { \frac { s } { c } } { \left( e ^ { c t } - 1 \right) } .
$$

With $s = 0$ this is the old solution $y _ { 0 } e ^ { c t }$ (no source). The example with $c = 1$ and $s = 5$ produced $( y _ { 0 } + 5 ) e ^ { t } - 5$ : Separating the source term gives $y _ { 0 } e ^ { t } + 5 ( e ^ { t } - 1 )$ :

Solution by Method 2 (slow way) The input $y _ { 0 }$ produces the output $y _ { 0 } e ^ { c t }$ : After $t$ years any deposit is multiplied by $e ^ { c t }$ : That also applies to deposits made after the account is opened. If the deposit enters»at time $T$ , the growing time is only $t - T$ : Therefore the multiplying factor is only $e ^ { c ( t - T ) }$ : This growth factor applies to the small deposit (amount $s d T$ ) made between time $T$ and $T + d T$ :

Now add up all outputs at time $t$ : The output from $y _ { 0 }$ is $y _ { 0 } e ^ { c t }$ : The small deposit $s d T$ near time $T$ grows to $e ^ { c ( t - T ) } s d T $ : The total is an integral:

$$
y ( t ) = y _ { 0 } e ^ { c t } + \int _ { T = 0 } ^ { t } e ^ { c ( t - T ) } s d T .
$$

This principle of Duhamel would still apply when the source $s$ varies with time. Here $s$ is constant, and the integral divides by $c$ :

$$
s \int _ { T = 0 } ^ { t } e ^ { c ( t - T ) } d T = { \frac { s e ^ { c ( t - T ) } } { - c } } \int _ { 0 } ^ { t } = - { \frac { s } { c } } + { \frac { s } { c } } e ^ { c t } .
$$

That agrees with the source term from Method 1; at the end of equat1ion (8). There we looked for “exponential plus constant,” here we added up outputs.

Method 1 was easier. It succeeded because we knew the form $A e ^ { c t } + B$ —with “undetermined coefficients.” Method 2 is more complete. The form for $y$ is part of the output, not the input. The source $s$ is a continuous supply of new deposits, all growing separately.1 Section6:5 startsfrom scratch, by directly integrating $y ^ { \prime } = c y + s$ :

Remark Method 2 is often described in terms of an integrating factor. First write the equation as $y ^ { \prime } - c y = s$ : Then multiply by a magic factor that makes integration possible:

$$
\begin{array} { r l r } & { y ^ { \prime } - c y ) e ^ { - c t } = s e ^ { - c t } } & { \mathrm { m u l t i p l y ~ b y ~ t h e ~ f a c t o r ~ } e ^ { - c t } } \\ & { } & { y e ^ { - c t } \bigg ] _ { 0 } ^ { t } = - \frac { S } { c } e ^ { - c t } \bigg ] _ { 0 } ^ { t } \qquad \mathrm { i n t e g r a t e ~ b o t h ~ s i d e s } } \\ & { y e ^ { - c t } - y _ { 0 } = - \frac { S } { c } \left( e ^ { - c t } - 1 \right) } & { \mathrm { s u b s t i u t e ~ 0 ~ a n d ~ } t } \\ & { y = e ^ { c t } y _ { 0 } + \frac { S } { c } \left( e ^ { c t } - 1 \right) } & { \mathrm { i s o l a t e ~ y ~ t o ~ r e a c h ~ f o r m u l a ~ ( 8 ) } } \end{array}
$$

The integrating factor produced a perfect derivative in line 1: I prefer Duhamel’s idea, that all inputs $y _ { 0 }$ and $s$ grow the same way. Either method gives formula (8) for $y$ :

# THE MATHEMATICS OF FINANCE (AT A CONTINUOUS RATE)

The question from finance is this: What inputs give what outputs ? The inputs can come at the start by $y _ { 0 }$ , or continuously by $s$ : The output can be paid at the end or continuously. There are six basic questions, two of which are already answered.

The future value is $y _ { 0 } e ^ { c t }$ from a deposit of $y _ { 0 }$ : To produce $y$ in the future, deposit the present value $y e ^ { - c t }$ : Questions 3–6 involve the source term s. We fix the continuous rateat $5 \%$ per year . $\overset { \cdot } { c } = . 0 5 \overset { \cdot } { , }$ /, and start the accountfrom $y _ { 0 } = 0$ : The answers come fast from equation (8).

Question 3 With deposits of $s = \$ 1000$ =year; how large is $y$ after 20 years ?

$$
y = { \frac { s } { c } } \left( e ^ { c t } - 1 \right) = { \frac { 1 0 0 0 } { . 0 5 } } \left( e ^ { \left( . 0 5 \right) \left( 2 0 \right) } - 1 \right) = 2 0 , 0 0 0 ( e - 1 ) \approx \ S 3 4 , 4 0 0 .
$$

One big deposit yields $2 0 , 0 0 0 e \approx \mathbb { 5 5 4 } , 0 0 0$ : The same 20; 000 via $s$ yields $\$ 34,400$ :

Notice a small by-product (for mathematicians). When the interest rate is $c = 0$ , our formulÑa $s ( e ^ { c t } - 1 ) / c$ tuÑrns into $0 / 0$ : We are absolutely sure that depositing $\$ 1000$ =year with no interest produces $\$ 20,000$ after 20 years. But this is not obvious from $0 / 0$ : By l’Hôpital’s rule we take $c$ -derivatives in the fraction:

$$
\operatorname* { l i m } _ { c \to 0 } { \frac { s ( e ^ { c t } - 1 ) } { c } } = \operatorname* { l i m } _ { c \to 0 } { \frac { s t e ^ { c t } } { 1 } } = s t . { \mathrm { ~ T h i s ~ i s ~ } } ( 1 0 0 0 ) ( 2 0 ) = 2 0 , 0 0 0 .
$$

Question 4 What continuous deposit of $s$ per year yields $\$ 20,000$ after 20 years ?

$$
2 0 , 0 0 0 = { \frac { s } { . 0 5 } } \left( e ^ { ( . 0 5 ) ( 2 0 ) } - 1 \right) { \mathrm { ~ r e q u i r e s ~ } } s = { \frac { 1 0 0 0 } { e - 1 } } \approx 5 8 2 .
$$

Deposits of $\$ 582$ over 20 years total $\$ 11,640$ : A single deposit of $y _ { 0 } = 2 0 , 0 0 0 / e =$ $\$ 7,360$ produces the same $\$ 20,000$ at the end. Better to be rich at $t = 0$ :

Questions 1 and 2 had $s = 0$ (no source). Questions 3 and 4 had $y _ { 0 } = 0$ (no initial deposit). Now we come to $y = 0$ : In 5, everything is paid out by an annuity. In ${ \bf 6 }$ , everything is paid up on a loan.

Question 5 What deposit $y _ { 0 }$ provides $\$ 1000$ =year for 20 years ? End with $y = 0$ :

$$
y = y _ { 0 } e ^ { c t } + { \frac { s } { c } } \left( e ^ { c t } - 1 \right) = 0 { \mathrm { ~ r e q u i r e s ~ } } y _ { 0 } = { \frac { - s } { c } } ( 1 - e ^ { - c t } ) .
$$

Substituting $s = - 1 0 0 0$ ; $c = . 0 5$ ; $t = 2 0$ gives $y _ { 0 } \approx 1 2 , 6 4 0$ : If you win $\$ 20,000$ in a lottery, and it is paid over 20 years, the lottery only has to put in $\$ 12,640$ : Even less if the interest rate is above $5 \%$ :

Question 6 What payments $s$ will clear a loan of $y _ { 0 } = \$ 20,000$ in 20 years ?

Unfortunately, $s$ exceeds $\$ 1000$ per year. The bank gives up more than the $\$ 20,000$ to buy your car (and pay tuition). It also gives up the interest on that money. You pay that back too, but you don’thave to stay even at every moment. Instead you repay at a constant rate for 20 years. Your payments mostly cover interest at the start and principal at the end. After $t = 2 0$ years you are even and your debt is $y = 0$ :

This is like Question 5 (also $y = 0$ ), but now we know $y _ { 0 }$ and we want $s$ :

$$
y = y _ { 0 } e ^ { c t } + { \frac { s } { c } } \left( e ^ { c t } - 1 \right) = 0 { \mathrm { ~ r e q u i r e s ~ } } s = - c y _ { 0 } e ^ { c t } / ( e ^ { c t } - 1 ) .
$$

The loan is $y _ { 0 } = \ S 2 0 , 0 0 0$ , the rate is $c = . 0 5 /$ year; the time is $t = 2 0$ years.   
Substituting in the formula for $s$ , your payments are $\$ 1582$ per year.

Puzzle How is $s = \$ 1582$ for loan payments related to $s = \$ 582$ for deposits ? $0 \to \$ 582$ per year $ \$ 320,000$ and $\$ 20,000$ per year $ 0$ :

That difference of exactly 1000 cannot be an accident. 1582 and 582 came from

$$
1 0 0 0 ~ { \frac { e } { e - 1 } } ~ { \mathrm { a n d } } ~ 1 0 0 0 { \frac { 1 } { e - 1 } } ~ { \mathrm { w i t h ~ d i f f e r e n c e } } ~ 1 0 0 0 { \frac { e - 1 } { e - 1 } } = 1 0 0 0 .
$$

Why ? Here is the real reason. Instead of repaying 1582 we can pay only 1000 (to keep even with the interest on 20; 000). The other 582 goes into a separate account. After 20 years the continuous 582 has built up to 20; 000 (including interest as in Question 4). From that account we pay back the loan.

Section 6.6 deals with daily compounding—which differs from continuous compounding by only a few cents. Yearly compounding differs by a few dollars.

# TRANSIENTS VS. STEADY STATE

Suppose there is decay instead of growth. The constant $c$ is negative and $y _ { 0 } e ^ { c t }$ dies out. That is the “transient” term, which disappears as $t \to \infty$ : What is leftÑis the “steady state.” We denote that limit by $y _ { \infty }$ :

Without a source, $y _ { \infty }$ is zero (total decay). When $s$ is present, $y _ { \infty } = - s / c$ :

At this steady state, the source $s$ exactly balances the decay $c y$ : In other words $c y + s = 0$ : From the leftside of the differential equation, this means $d y / d t = 0$ : There is no change. That is why $y _ { \infty }$ is steady.

Notice that $y _ { \infty }$ d8epends on the source and on $c$ —but not on $y _ { 0 }$ :

EXAMPLE 6 8Suppose Bermuda has a birth rate $b = . 0 2$ and death rate $d = . 0 3$ : The net decay rate is $c = - . 0 1$ : There is also immigration from outside, of $s = 1 2 0 0 /$ =year: The initial population might be $y _ { 0 } = 5$ thousand or $y _ { 0 } = 5$ million, but that number has no effect on $y _ { \infty }$ : The steady state is independent of $y _ { 0 }$ :

In this case $y _ { \infty } = - s / c = 1 2 0 0 / . 0 1 = 1 2 0 , 0 0 0 .$ The population grows to 120;000 if $y _ { 0 }$ is smaller. It decays to 120; 000 if $y _ { 0 }$ is larger.

EXAMPLE 7 $N e w t o n ^ { \prime } s L a w o f C o o l i n g : \qquad d y / d t = c ( y - y _ { \infty } ) .$

This is back to physics. The temperature of a body is $y$ : The temperature around it is $y _ { \infty }$ : Then $y$ starts at $y _ { 0 }$ and approaches $y _ { \infty }$ , following Newton’s rule:8The rate is proportional to $y - y _ { \infty }$ . The bigger the difference, the faste8r heat flows.

The equation has $- c y _ { \infty }$ where b8efore we had $s$ : That fits with $y _ { \infty } = - s / c$ : For the solution, replace $s$ by $- c y _ { \infty }$ in formula (8). Or use this new method:

Solution by M8ethod 3 The8new idea is to look at the diff8erence $y - y _ { \infty } .$ . Its derivative is $d y / d t$ , since $y _ { \infty }$ is constant. But $d y / d t$ is $c ( y - y _ { \infty } )$ —this is our equation. The difference starts from $y _ { 0 } - y _ { \infty }$ , and grows or decays as a pure exponential:

$$
\frac { d } { d t } \left( y - y _ { \infty } \right) = c ( y - y _ { \infty } ) h a s t h e s o l u t i o n \quad ( y - y _ { \infty } ) = ( y _ { 0 } - y _ { \infty } ) e ^ { c t } .
$$

This solves the law of cooling. We repeat Method 3 using the letters $s$ and $c$ :

$$
{ \frac { d } { d t } } \left( y + { \frac { s } { c } } \right) = c \left( y + { \frac { s } { c } } \right) \quad h a s t h e s o l u t i o n \quad \left( y + { \frac { s } { c } } \right) = \left( y _ { 0 } + { \frac { s } { c } } \right) e ^ { c t } .
$$

Moving $s / c$ to the right side recovers formula (8). There is a constant term and an exponential term. In a differential equations course, those are the “particular solution” and the “h8omogeneous solution.” In a calculus course, it’s time to stop.

EXAMPLE 8 In a $7 0 ^ { \circ }$ room, Newton’s corpse is found with a temperature of $9 0 ^ { \circ }$ : A day later the body registers $8 0 ^ { \circ }$ : When did he stop integrating (at $9 8 . 6 ^ { \circ }$ ) ?

Solution Here $y _ { \infty } = 7 0$ and $y _ { 0 } = 9 0$ : Newton’s equation (13) is $y = 2 0 e ^ { c t } +$ 70: Then $y = 8 0$ at $t = 1$ gives $2 0 e ^ { c } = 1 0$ : The rate of cooling is $\begin{array} { r } { c = \ln { \frac { 1 } { 2 } } } \end{array}$ : Death occurred when $2 0 e ^ { c t } + 7 0 = 9 8 . 6$ or $e ^ { c t } = 1 . 4 3$ : The time was $\begin{array} { r } { t = \ln { 1 . 4 3 } / \ln { \frac { 1 } { 2 } } = } \end{array}$ half a day earlier.