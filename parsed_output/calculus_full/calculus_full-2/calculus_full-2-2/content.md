# 2.2 Powers and Polynomials

This section has two main goals. One is to find the derivatives of $\begin{array} { r } { f \left( x \right) = x ^ { 3 } } \end{array}$ and $x ^ { 4 }$ and $x ^ { 5 }$ (and more generally $f ( x ) = x ^ { n } )$ . The power or exponent $n$ is at first a positive integer. Later we allow $x ^ { \pi }$ and $x ^ { 2 . 2 }$ and every $x ^ { n }$ :

The other goal is different. While computing these derivatives, we look aheadto their applications. In using calculus, we meet equations with derivatives in them— “differential equations.” It is too early to solve those equations. But it is not too early to see the purpose of what we are doing. Our examples come from economics and biology.

With $n = 2$ , the derivative of $x ^ { 2 }$ is $2 x$ : With $n = - 1$ , the slope of $x ^ { - 1 }$ is $- 1 x ^ { - 2 }$ : Those are two pieces in a beautiful pattern, which it will be a pleasure to discover. We begin with $x ^ { 3 }$ and its derivative $3 x ^ { 2 }$ , before jumping to $x ^ { n }$ :

EXAMPLE 1 If $f ( x ) = x ^ { 3 }$ then $\Delta f = ( x + h ) ^ { 3 } - x ^ { 3 } = ( x ^ { 3 } + 3 x ^ { 2 } h + 3 x h ^ { 2 } + h ^ { 3 } ) - x ^ { 3 } .$

Step 1: Cancel $x ^ { 3 }$ : Step 2: Divide by $h$ : Step $3 { : } h$ goes to zero.

$$
{ \frac { \Delta f } { h } } = 3 x ^ { 2 } + 3 x h + h ^ { 2 } \quad { \mathrm { a p p r o a c h e s } } \quad { \frac { d f } { d x } } = 3 x ^ { 2 } .
$$

That is straightforward, and you see the crucial step. The power $( x + h ) ^ { 3 }$ yields four separate terms $x ^ { 3 } + 3 x ^ { 2 } h + 3 x h ^ { 2 } + h ^ { 3 }$ : (Notice 1, 3, 3, 1:) After $x ^ { 3 }$ is subtracted, we can divide by $h$ : At the limit . $\displaystyle { ( h = 0 ) }$ / we have $3 x ^ { 2 }$ :

For $f ( x ) = x ^ { n }$ the plan is the same. A step of size $h$ leads to $f ( x + h ) = ( x + h ) ^ { n }$ : One reason for algebra is to calculate powers like $( x + h ) ^ { n }$ , and if you have forgotten the binomial formula we can recapture its main point. Start with $n = 4$ :

$$
( x + h ) ( x + h ) ( x + h ) ( x + h ) = x ^ { 4 } + \quad 2 7 ? \quad + h ^ { 4 } .
$$

Multiplying the four $x$ ’s gives $x ^ { 4 }$ : Multiplying the four $h$ ’s gives $h ^ { 4 }$ : These are the easy terms, but not the crucial ones. The subtraction .x C h/4 x4 will remove x4, and the limiting step $h  0$ will wipe out $h ^ { 4 }$ (even after division by $h$ ). The products th at matter are those with exactly one $h$ . In E xample 1 with $( x + h ) ^ { 3 }$ , this key term was $3 x ^ { 2 } h$ : Division by $h$ left $3 x ^ { 2 }$ :

With only one $h$ , there are n places it  can co me from. Equation (1) has four $h$ ’s in parentheses, and four ways to produce $x ^ { 3 } h$ : Therefore the key term is $4 x ^ { 3 } h$ : (Division by $h$ leaves $4 x ^ { 3 }$ :) In general there are $n$ parentheses and $n$ ways to produce $x ^ { n - 1 } h$ , so the binomial formula contains $n x ^ { n - 1 } h$ :

$$
( x + h ) ^ { n } = x ^ { n } + \underline { { { n } } } x ^ { n - 1 } h + \cdots + h ^ { n } .
$$

2B For $n = 1 , 2 , 3 , 4 , \dots$ ; the derivat ive of $x ^ { n }$ is $n x ^ { n - 1 }$ :

Subtract $x ^ { n }$ from (2). Divide by $h$ : The key term is $n x ^ { n - 1 }$ : The rest disappears as $h \to 0$ :

$$
{ \frac { \Delta f } { \Delta x } } = { \frac { ( x + h ) ^ { n } - x ^ { n } } { h } } = { \frac { n x ^ { n - 1 } h + \cdots + h ^ { n } } { h } } \quad { \mathrm { s o } } \quad { \frac { d f } { d x } } = n x ^ { n - 1 } .
$$

The terms replaced by the dots involve $h ^ { 2 }$ and $h ^ { 3 }$ and higher powers. After dividing by $h$ , they still have at least one factor $h$ : All those terms vanish as $h$ approaches zero.

EXAMPLE 2 $( x + h ) ^ { 4 } = x ^ { 4 } + \underline { { { 4 x ^ { 3 } h } } } + 6 x ^ { 2 } h ^ { 2 } + 4 x h ^ { 3 } + h ^ { 4 }$ : This is $n = 4$ in detail.

Subtract $x ^ { 4 }$ , divide by $h$ , let $h  0$ : The derivative is $4 x ^ { 3 }$ : The coefficients 1; 4; 6; 4; 1 are in Pascal’s triangle below. For $( x + h ) ^ { 5 }$ the next row is $1 , 5 , 1 0 , \underline { { ? } }$ .

Remark The missing terms in the binomial formula (replaced by the dots) contain all the products $x ^ { n - j } \bar { h } ^ { j }$ : An $x$ or an $h$ comes from each parenthesis. The binomial coefficient “n choose $j ^ { \prime \prime }$ is the number of ways to choose $j h$ ’s out of n parentheses. It involves $n$ factorial, which is $n ( n - 1 ) \cdots ( 1 )$ : Thus $5 ! = 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 1 2 0$ : These are numbers that gamblers know and love:

$$
{ } ^ { \textit { \textbf { . } } } n c h o o s e \textit { j } ^ { , , } = { \binom { n } { j } } = \frac { n ! } { j ! ( n - j ) ! }
$$

$$
\begin{array} { c c } { { 1 } } & { { P a s c a l ^ { \prime } s } } \\ { { 1 1 } } & { { t r i a n g l e } } \\ { { 1 2 1 } } & { { } } \\ { { 1 3 3 1 } } & { { n = 3 } } \\ { { 1 4 6 4 1 } } & { { n = 4 } } \end{array}
$$

In the last row, the coefficient of $x ^ { 3 } h$ is $4 ! / 1 ! 3 ! = 4 \cdot 3 \cdot 2 \cdot 1 / 1 \cdot 3 \cdot 2 \cdot 1 = 4$ : For the $x ^ { 2 } h ^ { 2 }$ term, with $j = 2$ , there are $4 \cdot 3 \cdot 2 \cdot 1 / 2 \cdot 1 \cdot 2 \cdot 1 = 6$ ways to choose two $h$ ’s. Notice that $1 + 4 + 6 + 4 + 1$ equals 16; which is $2 ^ { 4 }$ : Each rowof Pascal’s triangle adds to a power of 2:

Choosing 6 numbers out of 49 in a lottery, the odds are $4 9 \cdot 4 8 \cdot 4 7 \cdot 4 6 \cdot 4 5 \cdot 4 4 / 6 !$ to 1: That number is $N = { } ^ { \ast } 4 9$ choose $6 ^ { \circ } = 1 3 , 9 8 3 , 8 1 6 .$ It is the coefficient of $x ^ { 4 3 } h ^ { 6 }$ in $( x + h ) ^ { 4 9 }$ : If $\lambda$ times $N$ tickets are bought, the expected number of winners is $\lambda$ : The chance of no winner is $e ^ { - \lambda }$ : The chance of one winner is $\lambda e ^ { - \lambda }$ : See Section 8:4:

Florida’s lottery in September 1990 (these rules) had six winners out of 109, 163, 978 tickets.

# DERIVATIVES OF POLYNOMIALS

Now we have an infinite list of functions and their derivatives:

$$
\begin{array} { c c } { { x ~ x ^ { 2 } ~ x ^ { 3 } ~ x ^ { 4 } ~ x ^ { 5 } ~ \cdots } } & { { ~ 1 ~ 2 x ~ 3 x ^ { 2 } ~ 4 x ^ { 3 } ~ 5 x ^ { 4 } ~ \cdots } } \end{array}
$$

The deri?vative of $x ^ { n }$ is1 $n$ times the next lower power $x ^ { n - 1 }$ : That rule extends beyond these integers 1;2;3;4;5 to all powers:

$$
\begin{array} { l l l l l } { { f = 1 / x } } & { { \mathrm { h a s } } } & { { f ^ { \prime } = - 1 / x ^ { 2 } : } } & { { \mathrm { E x a m p l e ~ 3 ~ o f ~ s e c t i o n ~ } 2 . 1 } } & { { ( n = - 1 ) } } \\ { { f = 1 / x ^ { 2 } } } & { { \mathrm { h a s } } } & { { f ^ { \prime } = - 2 / x ^ { 3 } : } } & { { \mathrm { E x a m p l e ~ 6 ~ o f ~ s e c t i o n ~ } 2 . 1 } } & { { ( n = - 2 ) } } \\ { { f = \sqrt { x } } } & { { \mathrm { h a s } } } & { { f ^ { \prime } = { \frac { 1 } { 2 } } x ^ { - 1 / 2 } : } } & { { \mathrm { t r u e ~ b u t ~ n o t ~ y e t ~ c h e c k e d ~ } } } & { { ( n = { \frac { 1 } { 2 } } ) } } \end{array}
$$

Remember that $x ^ { - 2 }$ means $1 / x ^ { 2 }$ and $x ^ { - 1 / 2 }$ means $1 / { \sqrt { x } }$ : Negative powers lead to decreasing functions, approaching zero as $x$ gets large. Their slopes have minus signs.

Question What are the derivatives of $x ^ { 1 0 }$ and $x ^ { 2 . 2 }$ and $x ^ { - 1 / 2 } ?$ Answer $1 0 x ^ { 9 }$ and $2 . 2 x ^ { 1 . 2 }$ and $- { \frac { 1 } { 2 } } x ^ { - 3 / 2 }$ : Maybe $( x + h ) ^ { 2 . 2 }$ is a little unusual. Pascal’s triangle can’t deal with this fractional power, but the formula stays firm: After $x ^ { 2 . 2 }$ comes $2 . 2 x ^ { 1 . 2 } h$ . The complete binomial formulais in Section 10:5:

That list is a good start, but plenty of functions are left. What comes next is really simple. A tremendous number of new functions are “linear combinations” like

$$
f ( x ) = 6 x ^ { 3 } \quad { \mathrm { o r } } \quad 6 x ^ { 3 } + { \frac { 1 } { 2 } } x ^ { 2 } \quad { \mathrm { o r } } \quad 6 x ^ { 3 } - { \frac { 1 } { 2 } } x ^ { 2 } .
$$

# 2 Derivatives

What are their derivatives ? The answers are kno1wn for $x ^ { 3 }$ and $x ^ { 2 }$ , and we want to multiply by 6 or divide by 2 or add or subtract. Do the same to the derivatives:

$$
f ^ { \prime } ( x ) = 1 8 x ^ { 2 } \quad { \mathrm { o r } } \quad 1 8 x ^ { 2 } + x \quad { \mathrm { o r } } \quad 1 8 x ^ { 2 } - x .
$$

2C The derivative of $c$ times $f ( x )$ is $c$ times $f ^ { \prime } ( x )$ :   
2D The derivative of $f ( x ) + g ( x )$ is $f ^ { \prime } ( x ) + g ^ { \prime } ( x )$ :

Th1e number $c$ can be any constant. We can add (or subtract) any functions. The rules allow any combination of $f$ and $g$ : The derivative of $9 f ( x ) - 7 g ( x )$ is $9 f ^ { \prime } ( x ) - 7 g ^ { \prime } ( x )$ :

The reasoninÑg is direct. Wh1en $f ( x )$ is multiplied by $c$ , so is $f ( x + h )$ : The difference $\Delta f$ is also multiplied by $c$ : All averages $\Delta f / h$ contain $c$ , so their limit is $c f ^ { \prime }$ : The only incomplete step is the last one (the limit). We still have to say what “limit” means.

Rule 2D is similar. Adding $f + g$ means adding $\Delta f + \Delta g$ : Now divide by $h$ : In the limit as $h  0$ we reach $f ^ { \prime } + g ^ { \prime }$ —because a limit of sums is a sum of limits. Any example is easy and so is the proof—it is the definition of limit that needs care (Section 2:6).

You can now find the derivative of every polynomial. A “polynomial” is a combination of $1 , x , x ^ { 2 } , \ldots , x ^ { n }$ —for example $9 + 2 x - x ^ { 5 }$ : That particular polynomial has slope $2 - 5 x ^ { 4 }$ : Note that the derivative of 9 is zero! A constant just raises or lowers the graph, without changing its slope. It alters the mileage before starting the car.

The disappearance of constants is one of the nice things in differential calculus. The reappearance of those constants is one of the headaches in integral calculus. When you find $v$ from $f$ , the starting mileage doesn’t matter. The constant in $f$ has no effect on $v$ : ( $\Delta f$ is measured by a trip meter; $\Delta t$ comes from a stopwatch.) To find distance from velocity, you need to know the mileage at the start.

# A LOOK AT DIFFERENTIAL EQUATIONS (FIND $y$ FROM $d y / d x$ )

We know that $y = x ^ { 3 }$ has the derivative $d y / d x = 3 x ^ { 2 }$ : Starting with the function, we found its slope. Now reverse that process. Start with the slope and find the function. This is what science does all the time—and it seems only reasonable to say so.

Begin with $d y / d x = 3 x ^ { 2 }$ : The slope is given, the function $y$ is not given.

Question Can you go backward to reach $y = x ^ { 3 } \cdot$ ?   
Answer Almost but not quite. You are only entitled to say that $y = x ^ { 3 } + C$ : The constant $C$ is the starting value of $y$ (when $x = 0$ ). Then the differential equation $d y / d x = 3 x ^ { 2 }$ is solved.

Every time you find a derivative, you can go backward to solve a differential equation. The function $y = x ^ { 2 } + x$ has the slope $d y / d x = 2 x + 1$ : In reverse, the slope $2 x + 1$ produces $x ^ { 2 } + x$ —and all the other functions $x ^ { 2 } + x + C$ , shifted up and down. After going from distance $f$ to velocity $v$ , we return to $f + C$ : But there is a lot more to differential equations. Here are two crucial points:

1. We reach $d y / d x$ by way of $\Delta y / \Delta x$ , but we have no system to go backward. With $d y / d x = ( \sin x ) / x$ we are lost. What function has this derivative ?

2. Many equations have the same solution $y = x ^ { 3 }$ : Economics has $d y / d x = 3 y / x$ : Geometry has $d y / d x = 3 y ^ { 2 / 3 }$ : These equations involve $y$ as well as $d y / d x$ : Function and slope are mixed together! This is typical of differential equations.

To summarize: Chapters 2-4 compute and use derivatives. Chapter 5 goes in reverse. Integral calculus discovers the function from its slope. Given $d y / d x$ we find $y ( x )$ : Then Chapter 6 solves the differential equation ${ d y } / { d t } = y$ , function mixed with slope. Calculus moves from derivatives to integrals to differential equations.

This discussion of the purpose of calculus should mention a specific example. Differential equations are applied to an epidemic (like AIDS). In most epidemics the number of cases grows exponentially. The peak is quickly reached by $e ^ { t }$ , and the epidemic dies down. Amazingly, exponential growth is not happening with AIDS—the best fit to the data through 1988 is a cubic polynomial (Los Alamos Science, 1989):

The number of cases fits a cubic within $2 \% : y = 1 7 4 . 6 ( t - 1 9 8 1 . 2 ) ^ { 3 } + 3 4 0 .$

This is dramatically different from other epidemics. Instead of ${ d y } / { d t } = y$ we have $d y / d t = 3 y / t$ : Before this book is printed, we may know what has been preventing $e ^ { t }$ (fortunately). Eventually the curve will turn away from a cubic—I hope that mathematical models will lead to knowledge that saves lives.

Added in proof : In 1989 the curve for the U.S. dropped from $t ^ { 3 }$ to $t ^ { 2 }$ :

# MARGINAL COST AND ELASTICITY IN ECONOMICS

First point about economics: The marginal cost and marginal income are crucially important. The average cost of making automobiles may be $\$ 10,000$ : But it is the $\$ 8,000$ cost of the next car that decides whether Ford makes it. “The average describes the past, the marginal predicts the future.” For bank deposits or work hours or wheat, which come in smaller units, the amounts are continuous variables. Then the word “marginal” says one thing: Take the derivative.

The average pay over all the hours we ever worked may be low. We wouldn’t work another hour for that! This average is rising, but the pay for each additional hour rises faster—possibly it jumps. When $\$ 10$ =hour increases to $\$ 15$ =hour after a 40-hour week, a 50-hour week pays $\$ 550$ : The average income is $\$ 11$ =hour. The marginal income is $\$ 15$ =hour—the overtime rate.

Concentrate next on cost. Let $y ( x )$ be the cost of producing $x$ tons of steel. The cost of $x + \Delta x$ tons is $y ( x + \Delta x )$ : The extra cost is the difference $\Delta y$ : Divide by $\Delta x$ , the number of extra tons. The ratio $\Delta y / \Delta x$ is the average cost per extra ton. When $\Delta x$ is an ounce instead of a ton, we are near the marginal cost $d y / d x$ :

Example: When the cost is $x ^ { 2 }$ , the average cost is $x ^ { 2 } / x = x$ : The marginal cost is $2 x$ : Figure 2.4 has increasing slope—an example of “diminishing returns to scale.”

This raises another point about economics. The units are arbitrary. In yen per kilogram the numbers look different. The way to correct for arbitrary units is to work with percentage change or relative change. An increase of $\Delta x$ tons is a relative increase of $\Delta x / x$ : A cost increase $\Delta y$ is a relative increase of $\Delta y / y$ : Those are dimensionless, the same in tons=tons or dollars=dollars or yen=yen.

A third example is the demand $y$ at price $x$ . Now $d y / d x$ is negative. But again the units are arbitrary. The demand is in liters or gallons, the price is in dollars or pesos.

Relative changes are better. When the price goes up by $10 \%$ , the demand may drop by $5 \%$ : If that ratio stays the same for small increases, the elasticity of demand is $\frac { 1 } { 2 }$ :

Actually this number should be $- \frac { 1 } { 2 }$ : The price rose, the demand dropped. In our definition, the elasticity will be 1 : In conversation between economists the minus sign is left out (I hope not forgotten).

DEFINITION The elasticity of the demand function $y ( x )$ is

$$
E ( x ) = \operatorname* { l i m } _ { \Delta x \to 0 } { \frac { \Delta y / y } { \Delta x / x } } = { \frac { d y / d x } { y / x } } .
$$

Elasticity is “marginal” divided by “average.” $E ( x )$ is also relative change in $y$ divided by relative change in $x$ : Sometimes $E ( x )$ is the same at all prices—this important case is discussed below.

EXAMPLE 4 Suppose the demand is $y = c / x$ when the price is $x$ : The derivative $d y / d x = - c / x ^ { 2 }$ comes fro|m |ca¡lculus. The division $y / x = c / x ^ { 2 }$ is only algebra. The ratio is $E = - 1$ :

For the demand $y = c / x ,$ , the elasticity is $( - c / x ^ { 2 } ) / ( c / x ^ { 2 } ) = - 1 .$

All demand curves are compared with this one. The demand is inelastic when $| E | < 1$ : It is elastic when $| E | > 1$ : The demand $2 0 / { \sqrt { x } }$ is inelastic $\begin{array} { r } { ( E = - \frac { 1 } { 2 } ) } \end{array}$ /, while $x ^ { - 3 }$ is elastic . $( E = - 3 )$ /: The power $y = c x ^ { n }$ , whose derivative we know, is the function with constant elasticity $n$ :

$$
{ \mathrm { i f } } \quad y = c x ^ { n } \quad { \mathrm { t h e n } } d y / d x = c n x ^ { n - 1 } \quad { \mathrm { a n d } } E = c n x ^ { n - 1 } / ( c x ^ { n } / x ) = n .
$$

It is because $y = c x ^ { n }$ sets the standard that we could come so early to economics.

In the special case when $y = c / x$ , consumers spend the same at all prices. Price $x$ times quantity $y$ remains constant at $x y = c$ :

EXAMPLE 5 The supply curve has $E > 0$ —supply increases with price. Now the baseline case is $y = c x$ : The slope is $c$ and the average is $y / x = c$ : The elasticity is $E = c / c = 1$ :

Compare $E = 1$ with $E = 0$ and $E = \infty$ : A constant supply is “perfectly inelastic.” The power $n$ is zero and the slope is zero: $y = c$ : No more is available when the harvest is over. Whatever the price, the farmer cannot suddenly grow more wheat. Lack of elasticity makes farm economics difficult.

The other extreme $E = \infty$ is “perfectly elastic.” The supply is unlimited at a fixed price $x$ : Once this seemed true of water and timber. In reality the steep curve $x =$ constant is leveling off to a flat curve $y =$ constant. Fixed price is changing¡to fixed supply, $E = \infty$ is becoming $E = 0$ , and the supply of water follows a “gamma curve” shaped like $\Gamma$ :



EXAMPLE 6 Demand is an increasing function of income—more income, more demand. The income elasticity is $E ( I ) = ( d y / d I ) / ( y / I )$ : A luxury has $E > 1$ (elastic). Doubling your income more than doubles the demand for caviar. A necessity has $E < 1$ (inelastic). The demand for bread does not double. Please recognize how the central ideas of calculus provide a language for the central ideas of economics.

Important note on supply $\ c =$ demand This is the basic equation of microeconomics. Where the supply curve meets the demand curve, the economy finds the equilibrium price. Supply $\ c =$ demand assumes perfect competition. With many suppliers, no one can raise the price. If someone tries, the customers go elsewhere.

The opposite case is a monopoly—no competition. Instead of many small producers of wheat, there is one producer of electricity. An airport is a monopolist (and maybe the National Football League). If the price is raised, some demand remains.

Price fixing occurs when several producers act like a monopoly-which antitrust laws try to prevent. The price is not set by supply $\ b =$ demand. The calculus problem is different—to maximize profit. Section 3:2 locates the maximum where the marginal profit (the slope!) is zero.

Question on income elasticity From an income of $\$ 10,000$ you save $\$ 500$ : The income elasticity of savings is $E = 2$ : Out of the next dollar what fraction do you save ?

Answer The savings is $y = c x ^ { 2 }$ because $E = 2$ : The number $c$ must give $5 0 0 =$ $c ( 1 0 , 0 0 0 ) ^ { 2 }$ , so $c$ is $5 \cdot 1 0 ^ { - 6 }$ : Then the slope $d y / d x$ is $2 c x = 1 0 \cdot 1 0 \cdot 1 0 ^ { - 6 } \cdot 1 0 ^ { 4 } =$ $\frac { 1 } { 1 0 }$ : This is the marginal savings, ten cents on the dollar. Average savings is $5 \%$ ; marginal savings is $10 \%$ ; and $E = 2$ .