# 7.4 Partial Fractions

Notice how multiplying by $x - 2$ produced a hole on the left side. Method 2 is the “cover-up method.” Cover up $x - 2$ and then substitute $x = 2$ . The result is $3 = A + 0 + 0$ ; just what we wanted.

In Method 1, the numerators of equation (2) must agree. The factors that multiply $B$ and $C$ are again zero at $x = 2$ : That leads to the same $A$ —but the cover-up method avoids the unnecessary step of writing down equation (2).

Calculation of $B$ Multiply equation (1) by $x + 2$ ; which covers up the $( x + 2 )$ :

$$
{ \frac { 3 x ^ { 2 } + 8 x - 4 } { ( x - 2 ) } } = { \frac { A ( x + 2 ) } { x - 2 } } + B + { \frac { C ( x + 2 ) } { x } } .
$$

Now set $x = - 2$ ; so $A$ and $C$ are multiplied by zero:

$$
{ \frac { 3 ( - 2 ) ^ { 2 } + 8 ( - 2 ) - 4 } { ( - 2 - 2 ) } } = { \frac { - 8 } { 8 } } = - 1 = B .
$$

This is almost full speed, but (4) was not needed. Just cover up in $\boldsymbol { Q }$ and give $x$ the right value (which makes the covered factor zero).

Calculation of $C$ (quickest) In equation (1), cover up the factor $( x )$ and set $x = 0$ :

$$
{ \frac { 3 ( 0 ) ^ { 2 } + 8 ( 0 ) - 4 } { ( 0 - 2 ) ( 0 + 2 ) } } = { \frac { - 4 } { - 4 } } = 1 = C .
$$

To repeat: The same result $A = 3$ ; $B = - 1$ ; $C = 1$ comes from Method 1.

# EXAMPLE 2

$$
{ \frac { x + 2 } { ( x - 1 ) ( x + 3 ) } } = { \frac { A } { x - 1 } } + { \frac { B } { x + 3 } } .
$$

First cover up $( x - 1 )$ on |the left|and s e|t $x = 1$ : Next cover up $( x + 3 )$ and set $x =$ $^ { - 3 }$ :

$$
{ \frac { 1 + 2 } { ( - 3 - 1 ) ( 1 + 3 ) } } = { \frac { 3 } { 4 } } = A \qquad { \frac { - 3 + 2 } { ( - 3 - 1 ) ( } } = { \frac { - 1 } { - 4 } } = B .
$$

The integral is $\textstyle { \frac { 3 } { 4 } } \ln | x - 1 | + { \frac { 1 } { 4 } } \ln | x + 3 | + C .$ :

EXAMPLE 3 This was needed for the logistic equation in Section 6.5:

$$
{ \frac { 1 } { y ( c - b y ) } } = { \frac { A } { y } } + { \frac { B } { c - b y } } .
$$

First multiply by $y$ : That covers up $y$ in the first two terms and changes $B$ to $B y$ : Then set $y = 0$ : The equation becomes $1 / c = A$ :

To find $B$ ; multiply by $c - b y$ : That covers up $c - b y$ in the outside terms. In the middle, $A$ times $c - b y$ will be zero at $y = c / b$ : That leaves $B$ on the right equal to $1 / y = b / c$ on the left. Then $A = 1 / c$ and $B = b / c$ give the integral announced in Equation 6:5:9 W

$$
\int \frac { d y } { c y - b y ^ { 2 } } = \int \frac { d y } { c y } + \int \frac { b ~ d y } { c ( c - b y ) } = \frac { \ln y } { c } - \frac { \ln ( c - b y ) } { c } .
$$

$I t$ is time to admit that the general method of partial fractions can be very awkward. First of all, it requires the factors of the denominator $\boldsymbol { Q }$ : When $\boldsymbol { Q }$ is a quadratic $a x ^ { 2 } + b x + c$ ; we can find its roots and its factors. In theory a cubic or a quartic can also be facto»red, but in practice only a few are possible—for example $x ^ { 4 } -$ 1 is $( x ^ { 2 } - 1 ) ( x ^ { 2 } + 1 )$ : Even for this good example, two of the roots are imaginary. We can split $x ^ { 2 } - 1$ into $( x + 1 ) ( x - 1 )$ : We cannot split $x ^ { 2 } + 1$ without introducing $i$ :



The method of partial fractions can work directly with $x ^ { 2 } + 1$ ; as we now see.

# EXAMPLE 4

$$
\int { \frac { 3 x ^ { 2 } + 2 x + 7 } { x ^ { 2 } + 1 } } d x \quad ( { \mathrm { a ~ q u a d r a t i c ~ o v e r ~ a ~ q u a d r a t i c } } ) .
$$

This has another difficulty. The degree of $P$ equals the degree of $Q ( = 2 )$ : Partial fractions cannot start until $P$ has lower degree. Therefore I divide the leading term $x ^ { 2 }$ into the leading term $3 x ^ { 2 }$ : That gives 3; which is separated off by itself:

$$
{ \frac { 3 x ^ { 2 } + 2 x + 7 } { x ^ { 2 } + 1 } } = 3 + { \frac { 2 x + 4 } { x ^ { 2 } + 1 } } .
$$

Note how 3 really used $3 x ^ { 2 } + 3$ from the original numerator. That left $2 x + 4$ : Partial fractions will accept a linear factor $2 x + 4$ (or $A x + B$ ; not just $A$ ) above $\pmb { a }$ quadratic.

This example contains $2 x / ( x ^ { 2 } + 1 )$ ; which integrates to $\ln ( x ^ { 2 } + 1 )$ : The final $4 / ( x ^ { 2 } + 1 )$ integrates to $4 \tan ^ { - 1 } x$ : When the denominator is $x ^ { 2 } + x + 1$ we complete the square before integrating. The point of Sections 7.2 and 7.3 was to make that integration possible. This section gets the fraction ready—in parts.

The essential point is that we never have to go higher than quadratics. Every denominator $\boldsymbol { Q }$ can be split into linear factors and quadratic factors. There is no magic way to find those factors, and most examples begin by giving them. They go into their own fractions, and they have their own numerators—which are the $A$ and $B$ and $2 x + 4$ we have been computing.

The one remaining question is what to do if a factor is repeated. This happens in Example 5.

# EXAMPLE 5

$$
{ \frac { 2 x + 3 } { ( x - 1 ) ^ { 2 } } } = { \frac { A } { ( x - 1 ) } } + { \frac { B } { ( x - 1 ) ^ { 2 } } } .
$$

The key is the new term $B / ( x - 1 ) ^ { 2 }$ : That is the right form to expect. With $( x - 1 )$ $( x - 2 )$ this term would have been $B / ( x - 2 )$ : But when $( x - 1 )$ is repeated, something new is needed. To find $B$ ; multiply through by $( x - 1 ) ^ { 2 }$ and set $x = 1$ :

$$
2 x + 3 = A ( x - 1 ) + B { \mathrm { \quad { b e c o m e s } } } \quad 5 = B \quad { \mathrm { w h e n } } \quad x = 1 .
$$

This cover-up method gives $B$ : Then $A = 2$ is easy, and the integral is $2 \ln | x - 1 | - 5 / ( x - 1 )$ : The fraction $5 / ( x - 1 ) ^ { 2 }$ has an integral without logarithms.

# EXAMPLE 6

$$
\frac { 2 x ^ { 3 } + 9 x ^ { 2 } + 4 } { x ^ { 2 } ( x ^ { 2 } + 4 ) ( x - 1 ) } = \frac { A } { x } + \frac { B } { x ^ { 2 } } + \frac { C x + D } { x ^ { 2 } + 4 } + \frac { E } { x - 1 } .
$$

This final example has almost everything! It is more of a game tha n a calculus problem. In fact calculus doesn’t enter until we integrate (and nothing is new there). Before computing $A , B , C , D , E$ ; we write down the overall rules for partial fractions:

1. The degree of $P$ must be less than the degree of $\boldsymbol { Q }$ : Otherwise divide their leading terms as in equation (8) to lower the degree of $P$ : Here $3 < 5$ : 2. Expect the fractions illustrated by Example 6. The linear factors $x$ and $x + 1$ (and the repeated $x ^ { 2 }$ ) are underneath constants. The quadratic $x ^ { 2 } + 4$ is under a linear term. A repeated $( x ^ { 2 } + 4 ) ^ { 2 }$ would be under a new $F x + G$ :

3. Find the numbers $A , B , C , \ldots$ by any means, including cover-up.   
4. Integrate each term separately and add.

We could prove that this method always works. It makes better sense to show that it works once, in Example 6.

To find $E$ ; cover up $( x - 1 )$ on theleft and substitute $x = 1$ : Then $E = 3$ : To find $B$ ; cover up $x ^ { 2 }$ on the left and set $x = 0$ : Then $B = 4 / ( 0 + 4 ) ( 0 - 1 ) = - 1$ : The cover-up method has done its job, and there are several ways to find $A , C , D$ : Compare the numerators, after multiplying through by the common denominator $\boldsymbol { Q }$ :

$$
2 x ^ { 3 } + 9 x ^ { 2 } + 4 = A x ( x ^ { 2 } + 4 ) ( x - 1 ) - ( x ^ { 2 } + 4 ) ( x - 1 ) + ( C x + D ) ( x ^ { 2 } ) ( x - 1 ) + 3 x ^ { 2 } ( x ^ { 2 } + 4 ) .
$$

The known terms on the right, from $B = - 1$ and $E = 3$ ; can move to the left:

$$
- 3 x ^ { 4 } + 3 x ^ { 3 } - 4 x ^ { 2 } + 4 x = A x ( { x ^ { 2 } + 4 } ) ( x - 1 ) + ( C x + D ) x ^ { 2 } ( x - 1 ) .
$$

We can divide through by $x$ and $x - 1$ ; which checks that $B$ and $E$ were correct:

$$
- 3 x ^ { 2 } - 4 = A ( x ^ { 2 } + 4 ) + ( C x + D ) x .
$$

Finally $x = 0$ yields $A = - 1$ : This leaves $- 2 x ^ { 2 } = ( C x + D ) x$ : Then $C = - 2$ and $D = 0$ :

You should never have to do such a problem! I never intend to do another one. It completely depends on expecting the right form and matching the numerators. They could also be matched by comparing coefficients of $x ^ { 4 } , x ^ { 3 } , x ^ { 2 } , x , 1$ —to give five equations for $A , B , C , D , E$ : That is an invitation to human error. Cover-up is the way to start, and usually the way to finish. With repeated factors and quadratic factors, match numerators at the end.