# 5.3 Summation versus Integration

This section does integration the hard way. We find explicit formulas for $f _ { n } = v _ { 1 } + \cdots + v _ { n }$ : From areas of rectangles, the limits produce the area $f ( x )$ under a curve. According to the Fundamental Theorem, $d f / d x$ should return us to $v ( x )$ —and we verify in each case that it does.

May I recall that there is sometimes an easier way? If we can find an $f ( x )$ whose derivative is $v ( x )$ , then the integral of $v$ is $f .$ Sums and limits are not required, when $f$ is spotted directly. The next section, which explains how to look for $f ( x )$ , will displace this one. (If we can’t find an antiderivative we fall back on summation.) Given a successful $f ,$ ; adding any constant produces another $f$ —since the derivative of the constant is zero. The right constant achieves $f ( 0 ) = 0$ , with no extra effort.

This section constructs $f ( x )$ from sums. The next section searches for antiderivatives.

# THE SIGMA NOTATION

In a section about sums, there has to be a decent way to express them. Consider $1 ^ { 2 } + 2 ^ { 2 } + 3 ^ { 2 } + 4 ^ { 2 }$ : The individual terms are $v _ { j } = j ^ { 2 }$ : Their sum can be written in summation notation, using the capital Greek letter $\Sigma$ (pronounced sigma):

$$
1 ^ { 2 } + 2 ^ { 2 } + 3 ^ { 2 } + 4 ^ { 2 } { \mathrm { ~ i s ~ w r i t t e n } } \sum _ { j = 1 } ^ { 4 } j ^ { 2 } .
$$

Spoken aloud, that becomes “the sum of $j ^ { 2 }$ from $j = 1$ to 4.” It equals 30: The limits on $j$ (written below and above $\Sigma$ ) indicate where to start and stop:

$$
v _ { 1 } + \cdots + v _ { n } = \sum _ { j = 1 } ^ { n } v _ { j } \quad { \mathrm { a n d } } \quad v _ { 3 } + \cdots + v _ { 9 } = \sum _ { k = 3 } ^ { 9 } v _ { k } .
$$

The $k$ at the end of (1) makes an additional point. There is nothing special about the letter $j$ : That is a “dummy variable,” no better and no worse than $k$ (or $i$ ). Dummy variables are only on one side (the side with $\Sigma$ ), and they have no effect on the sum. The upper limit $n$ is on both sides. Here are six sums:

$$
\sum _ { k = 1 } ^ { n } k = 1 + 2 + 3 + \cdots + n \qquad \quad \sum _ { j = 1 } ^ { 4 } ( - 1 ) ^ { j } = - 1 + 1 - 1 + 1 = 0
$$

$$
\sum _ { j = 1 } ^ { 5 } ( 2 j - 1 ) = 1 + 3 + 5 + 7 + 9 = 5 ^ { 2 } \sum _ { i = 0 } ^ { 0 } v _ { i } = v _ { 0 } \left[ { \mathrm { o n l y ~ o n e ~ t e r m } } \right]
$$

$$
\sum _ { k = 0 } ^ { \infty } { \frac { 1 } { 2 ^ { k } } } = 1 + { \frac { 1 } { 2 } } + { \frac { 1 } { 4 } } + \cdots = 2 \left[ { \mathrm { i n f n i t e ~ s e r i e s } } \right]
$$

The numbers 1 and $n$ or 1 and 4 (or 0 and $\infty$ ) are the lower limit and upper limit. The dummy variable $i$ or $j$ or $k$ is the index of summation. I hope it seems reasonable that the infinite series $\textstyle 1 + { \frac { 1 } { 2 } } + { \frac { 1 } { 4 } } + \cdots$ adds to 2: We will come back to it in Chapter $1 0 . \dagger$

A sum like $\Sigma _ { j = 1 } ^ { n } 6$ looks meaningless, but it is actually $6 + 6 + \cdots + 6 = 6 n$ : It follows the rules. In fact $\Sigma _ { i = 1 } ^ { 4 } j ^ { 2 }$ is not meaningless either. Every term is $j ^ { 2 }$ and by the same rules, that sum is $4 j ^ { 2 }$ : However the $i$ was probably intended to be $j$ : Then the sum is $1 + 4 + 9 + 1 6 = 3 0$ :



Question What happens to these sums when the upper limits are changed to $n$ ?

Answer The sum depends on the stopping point $n$ . A formula is required (when possible). Integrals stop at $x$ , sums stop at $n$ , and we now look for special cases when $f ( x )$ or $f _ { n }$ can be found.

# A SPECIAL SUMMATION FORMULA

How do you add the first 100 whole numbers? The problem is to compute

$$
\sum _ { j = 1 } ^ { 1 0 0 } j = 1 + 2 + 3 + \cdots + 9 8 + 9 9 + 1 0 0 = ?
$$

If you were Gauss, you would see the answer at once. (He solved this problem at a ridiculous age, which gave his friends the idea of getting him into another class.) His solution was to combine $1 + 1 0 0$ , and $2 + 9 9$ , and $3 + 9 8$ , always adding to 101. There are fifty of those combinations. Thus the sum is . $5 0 ) ( 1 0 1 ) = 5 0 5 0$ .

The sum from 1 to $n$ uses the same idea. The first and last terms add to $n + 1$ : The next terms $n - 1$ and 2 also add to $n + 1$ : If $n$ is even (as 100 was) then there are ${ \begin{array} { l } { { \frac { 1 } { 2 } } n } \end{array} }$ parts. Therefore the sum is ${ \begin{array} { l } { { \frac { 1 } { 2 } } n } \end{array} } $ times $n + 1$ :

$$
\sum _ { j = 1 } ^ { n } j = 1 + 2 + \cdots + ( n - 1 ) + n = { \frac { 1 } { 2 } } n ( n + 1 ) .
$$

The important term is ${ \frac { 1 } { 2 } } n ^ { 2 }$ , but the exact sum is ${ \frac { 1 } { 2 } } n ^ { 2 } + { \frac { 1 } { 2 } } n$ :

What happens if $n$ is an odd number (like $n = 9 9$ )? Formula (2) remains true. The combinations $1 + 9 9$ and $2 + 9 8$ still add to $n + 1 = 1 0 0$ : There are $\begin{array} { r } { \frac { 1 } { 2 } ( 9 9 ) = 4 9 \frac { 1 } { 2 } } \end{array}$ such pairs, because the middle term (which is 50) has nothing to combine with. Thus $1 + 2 + \cdots + 9 9$ equals $4 9 { \frac { 1 } { 2 } }$ times 100, or 4950.

Remark That sum had to be 4950; because it is 5050 minus 100: The sum up to 99 equals the sum up to 100 with the last term removed. Our key formula $f _ { n } - f _ { n - 1 } =$ $v _ { n }$ has turned up again!

EXAMPLE Find the sum $1 0 1 + 1 0 2 + \cdots + 2 0 0$ of the second hundred numbers.

First solution This is the sum from 1 to 200 minus the sum from 1 to 100 W

$$
\sum _ { 1 0 1 } ^ { 2 0 0 } j = \sum _ { 1 } ^ { 2 0 0 } j - \sum _ { 1 } ^ { 1 0 0 } j .
$$

The middle sum is ${ \scriptstyle { \frac { 1 } { 2 } } } ( 2 0 0 ) ( 2 0 1 )$ and the last is ${ \scriptstyle { \frac { 1 } { 2 } } } ( 1 0 0 ) ( 1 0 1 )$ : Their difference is 15050:   
Note! I left out $\cdot \cdot _ { j } = "$ in the limits. It is there, but not written.

Second solution The answer 15050 is exactly the sum of the first hundred numbers (which was 5050) plus an additional 10000: Believing that a number like 10000 can never turn up by accident, we look for a reason. It is found through changing the limits of summation:

$$
\sum _ { j = 1 0 1 } ^ { 2 0 0 } j { \mathrm { ~ i s ~ t h e ~ s a m e ~ s u m ~ a s ~ } } \sum _ { k = 1 } ^ { 1 0 0 } ( k + 1 0 0 ) .
$$

This is important, to be able to shift limits around. Often the lower limit is moved to zero or one, for convenience. Both sums have 100 terms (that doesn’t change). The dummy variable $j$ is replaced by another dummy variable $k$ : They are related by $j = k + 1 0 0$ or equivalently by $k = j - 1 0 0$ :

The variable must change everywhere—in the lower limit and the upper limit as well as inside the sum. If $j$ starts at 101; then $k = j - 1 0 0$ starts at 1: If $j$ ends at 200; $k$ ends at 100: If $j$ appears in the sum, it is replaced by $k + 1 0 0$ (and if $j ^ { 2 }$ appeared it would become $( k + 1 0 0 ) ^ { 2 } )$ :

From equation (4) you see why the answer is 15050: The sum $1 + 2 + \cdots + 1 0 0$ is 5050 as before. 100 is added to each of those 100 terms. That gives 10000:

# EXAMPLES OF CHANGING THE VARIABLE (and the limits)

$$
\begin{array} { r l } { \displaystyle \sum _ { i = 0 } ^ { 3 } 2 ^ { i } \mathrm { \ e q u a l s } \sum _ { j = 1 } ^ { 4 } 2 ^ { j - 1 } } & { ( \mathrm { h e r e \ } i = j - 1 ) . \mathrm { B o t h \ s u m s \ a r e \ } 1 + 2 + 4 + 8 } \\ { \displaystyle \sum _ { i = 3 } ^ { n } v _ { i } \mathrm { \ e q u a l s } \sum _ { j = 0 } ^ { n - 3 } v _ { j + 3 } } & { ( \mathrm { h e r e \ } i = j + 3 \mathrm { \ a n d \ } j = i - 3 ) . \mathrm { B o t h \ s u m s \ a r e \ } v _ { 3 } + \cdots + v _ { n } . } \end{array}
$$

Why change $n$ to $n - 3 2$ Because the upper limit is $i = n$ : So $j + 3 = n$ and $j =$ $n - 3$ :

A final step is possible, and you will often see it. The new variable $j$ can be changed back to $i$ : Dummy variables have no meaning of their own, but at first the result looks surprising:

$$
\sum _ { i = 0 } ^ { 5 } 2 ^ { i } \mathrm { \ e q u a l s \ } \sum _ { j = 1 } ^ { 6 } 2 ^ { j - 1 } \mathrm { \ e q u a l s \ } \sum _ { i = 1 } ^ { 6 } 2 ^ { i - 1 } .
$$

With practice you might do that in one step, skipping the temporary letter $j$ : Every $i$ on the left becomes $i - 1$ on the right. Then $i = 0 , . . . , 5$ changes to $i = 1 , . . . , 6$ : (At first two steps are safer.) This may seem a minor point, but soon we will be changing the limits on integrals instead of sums. Integration is parallel to summation, and it is better to see a “change of variable” here first.

Note about $1 + 2 + \cdots + n$ : The good thing is that Gauss found the sum ${ \textstyle { \frac { 1 } { 2 } } n ( n + 1 ) }$ : The bad thing is that his method looked too much like a trick. I wo uld like toshow how this fits the fundam ental rule connecting sums and differences:

$$
i f \ v _ { 1 } + v _ { 2 } + \cdots + v _ { n } = f _ { n } \ t h e n \ v _ { n } = f _ { n } - f _ { n - 1 } .
$$

Gauss says that $f _ { n }$ is ${ \textstyle { \frac { 1 } { 2 } } n ( n + 1 ) }$ : Reducing $n$ by 1, his formula f or $f _ { n - 1 }$ is $\frac { 1 } { 2 } ( n - 1 ) n$ : The difference $f _ { n } - f _ { n - 1 }$ should be the last term $n$ in the sum:

$$
\begin{array} { r } { f _ { n } - f _ { n - 1 } = \frac { 1 } { 2 } n ( n + 1 ) - \frac { 1 } { 2 } ( n - 1 ) n = \frac { 1 } { 2 } ( n ^ { 2 } + n - n ^ { 2 } + n ) = n . } \end{array}
$$

This is the one term $v _ { n } = n$ that is included in $f _ { n }$ but not in $f _ { n - 1 }$ :

There is a deeper point here. For any sum $f _ { n }$ ; there are two things to check. The $f$ ’s must begin correctly and they must change correctly. The underlying idea is mathematical induction: Assume the statement is true below $n$ : Prove it for $n$ .

Goal: To prove that $1 + 2 + \cdots + n = { \frac { 1 } { 2 } } n ( n + 1 )$ : This is the guess $f _ { n }$ .

Proof by induction: Check $f _ { 1 }$ (it equals 1). Check $f _ { n } - f _ { n - 1 } ( i t ~ e q u a l s n )$ .

For $n = 1$ the answer $\textstyle { \frac { 1 } { 2 } } n ( n + 1 ) = { \frac { 1 } { 2 } } \cdot 1 \cdot 2$ is correct. For $n = 2$ this formula ${ \frac { 1 } { 2 } } \cdot 2 \cdot 3$ agrees with $1 + 2$ : But that separate test is not necessary! If $f _ { 1 }$ is right, and if the change $f _ { n } - f _ { n - 1 }$ is right for every $n$ ; then $f _ { n }$ must be right. Equation (6) was the key test, to show that the change in $f$ ’s agrees with $v$ :

That is the logic behind mathematical induction, but I am not happy with most of the exercises that use it. There is absolutely no excitement. The answer is given by some higher power (like Gauss), and it is proved correct by some lower power (like us). It is much better when we lower powers find the answer for ourselves. $\dag$ Therefore I will try to do that for the second problem, which is the sum of squares.

# THE SUM OF $j ^ { 2 }$ AND THE INTEGRAL OF $x ^ { 2 }$

An important calculation comes next. It is the area in Figure 5.6. One region is made up of rectangles, so its area is a sum of $n$ pieces. The other region lies under the parabola $v = x ^ { 2 }$ : It cannot be divided into rectangles, and calculus is needed.

The first problem is to find $f _ { n } = 1 ^ { 2 } + 2 ^ { 2 } + 3 ^ { 2 } + \cdot \cdot \cdot + n ^ { 2 }$ : This is a sum of squares, with $f _ { 1 } = 1$ and $f _ { 2 } = 5$ and $f _ { 3 } = 1 4$ : The goal is to find the pattern in that sequence. By trying to guess $f _ { n }$ we are copying what will soon be done for integrals.

Calculus looks for an $f ( x )$ whose derivative is $v ( x )$ : There $f$ is an antiderivative

(or an integral).Algebra looks for $f _ { n } ^ { \mathrm { ~ * ~ } }$ s whose differences produce $v _ { n }$ : Here $f _ { n }$ could be called an antidifference (better to call it a sum).

The best start is agood guess. Copying directly from integrals, we might try $\begin{array} { r } { f _ { n } = \frac { 1 } { 3 } n ^ { 3 } } \end{array}$ : To test if it is right, check whether $f _ { n } - f _ { n - 1 }$ produces on $v _ { n } = n ^ { \bar { 2 } }$ :

$$
\begin{array} { r } { \frac { 1 } { 3 } n ^ { 3 } - \frac { 1 } { 3 } ( n - 1 ) ^ { 3 } = \frac { 1 } { 3 } n ^ { 3 } - \frac { 1 } { 3 } ( n ^ { 3 } - 3 n ^ { 2 } + 3 n - 1 ) = n ^ { 2 } - n + \frac { 1 } { 3 } . } \end{array}
$$

We see n2, but also n C 31 : The guess31 n3 needs correction terms. To cancel 31 in the difference, I subtract ${ \begin{array} { l } { { \frac { 1 } { 3 } } n } \end{array} }$ from the sum. To put back $n$ in the difference, I add $1 + 2 + \cdots + n = { \frac { 1 } { 2 } } n ( n + 1 ) $ to the sum. The new guess (which should be right) is

$$
\begin{array} { r } { f _ { n } = \frac { 1 } { 3 } n ^ { 3 } + \frac { 1 } { 2 } n ( n + 1 ) - \frac { 1 } { 3 } n = \frac { 1 } { 3 } n ^ { 3 } + \frac { 1 } { 2 } n ^ { 2 } + \frac { 1 } { 6 } n . } \end{array}
$$

To check this answer, verify first that $f _ { 1 } = 1$ : Also $f _ { 2 } = 5$ and $f _ { 3 } = 1 4$ : To be certain, verify that $f _ { n } - f _ { n - 1 } = n ^ { 2 }$ : For calculus the important term is ${ \scriptstyle { \frac { 1 } { 3 } } } n ^ { 3 }$ :

$$
T h e s u m \sum _ { j = 1 } ^ { n } j ^ { 2 } \ o f t h e f i r s t \ n s q u a r e s \ i s \ \frac 1 3 \ n ^ { 3 } p l u s \ c o r r e c t i o n s \ \frac 1 2 \ n ^ { 2 } \ a n d \ \frac 1 6 n .
$$

In practice ${ \frac { 1 } { 3 } } n ^ { 3 }$ is an excellent estimate. The sum of the first 100 squares is approximately ${ \textstyle \frac { 1 } { 3 } } ( 1 0 0 ) ^ { 3 }$ , or a third of a million. If we need the exact answer, equation (7) is available: the sum is 338; 350: Many applications (example: the number of steps to solve 100 linear equations) can settle for ${ \overline { { \frac { 1 } { 3 } } } } n ^ { 3 }$ :

What is fascinating is the contrast with calculus. Calculus has no correction terms! They get washed away in the limit of thin rectangles. When the sum is replaced by the integral (the area), we get an absolutely clean answer:

The area under the parabola, out to the point $x = 1 0 0$ , is precisely a third of a million.   
We have to explain why, with many rectangles.

The idea is to approach an infinite number of infinitely thin rectangles. A hundred rectangles gave an area of 338; 350: Now take a thousand rectangles. Their heights are $\begin{array} { r } { \left( \frac { \bar { 1 } } { 1 0 } \right) ^ { 2 } , \left( \frac { 2 } { 1 0 } \right) ^ { 2 } } \end{array}$ ; : : : because the curve is $v = x ^ { 2 }$ : The base of every rectangle is $\begin{array} { r } { \Delta x = \frac { 1 } { 1 0 } } \end{array}$ , a nd we add heights times base:

$$
= { \bigg ( } { \frac { 1 } { 1 0 } } { \bigg ) } ^ { 2 } \left( { \frac { 1 } { 1 0 } } \right) + \left( { \frac { 2 } { 1 0 } } \right) ^ { 2 } \left( { \frac { 1 } { 1 0 } } \right) + \cdots + \left( { \frac { 1 0 0 0 } { 1 0 } } \right) ^ { 2 } \left( { \frac { 1 } { 1 0 } } \right) .
$$

Factor out $\scriptstyle \left( { \frac { 1 } { 1 0 } } \right) ^ { 3 }$ : What you have left is $1 ^ { 2 } + 2 ^ { 2 } + \cdots + 1 0 0 0 ^ { 2 }$ , which fits the sum of squares for mula. The exact area of the thousand rectangles is 333; 833:5: I could try to guess ten thousand rectangles but I won’t.

Main point: The area is approaching 333; 333:333 : : :: But the calculations are getting worse. It is time for algebra—which means that we keep “ $\Delta x ^ { , \mathbf { \vec { \mathbf { \tau } } } }$ and avoid numbers.

The interval of length 100 is divided into $n$ pieces of length $\Delta x$ : (Thus $n = 1 0 0 / \Delta x . )$ The $j$ th rectangle meets the curve $v = x ^ { 2 }$ , so its height is $( j \Delta x ) ^ { 2 }$ : Its base is $\Delta x$ , and we add areas:

$$
a r e a = ( \Delta x ) ^ { 2 } ( \Delta x ) + ( 2 \Delta x ) ^ { 2 } ( \Delta x ) + \cdots + ( n \Delta x ) ^ { 2 } ( \Delta x ) = \sum _ { j = 1 } ^ { n } ( j \Delta x ) ^ { 2 } ( \Delta x ) .
$$

Factor out $( \Delta x ) ^ { 3 }$ , leaving a sum of $n$ squares. The area is $( \Delta x ) ^ { 3 }$ times $f _ { n }$ ; and $n = \frac { 1 0 0 } { \Delta x }$ (8) 100

$$
( \Delta x ) ^ { 3 } \left[ \frac { 1 } { 3 } \left( \frac { 1 0 0 } { \Delta x } \right) ^ { 3 } + \frac { 1 } { 2 } \left( \frac { 1 0 0 } { \Delta x } \right) ^ { 2 } + \frac { 1 } { 6 } \left( \frac { 1 0 0 } { \Delta x } \right) \right] = \frac { 1 } { 3 } 1 0 0 ^ { 3 } + \frac { 1 } { 2 } 1 0 0 ^ { 2 } ( \Delta x ) + \frac { 1 } { 6 } 1 0 0 ( \Delta x ) ^ { 2 } .
$$

This equation shows what is happening. The leading term is a third of a million, as predicted. The other terms are approaching zero! They contain $\Delta x$ , and as the rectangles get thinner they disappear. They only account for the small corners of rectangles that lie above the curve. The vanishing of those corners will eventually be proved for any continuous functions—the area from the correction terms goes to zero—but here in equation (9) you see it explicitly.

The area under the curve came from the central idea of integration: $1 0 0 / \Delta x$ rectangles of width $\Delta x$ approach the limiting area $\scriptstyle = { \frac { 1 } { 3 } } ( 1 0 0 ) ^ { 3 }$ : The rectangular area is $\Sigma v _ { j } \Delta x$ : The exact area is $\int v ( x ) d x$ : In the limit $\Sigma$ becomes $\int$ and $v _ { j }$ becomes $v ( x )$ and $\Delta x$ becomes $d x$ :

That completes the calculation for a parabola. It used the formula for a sum of squares, which was special. But the underlying idea is much more general. The limit of the sums agrees with the antiderivative: The antiderivative of $v ( x ) = x ^ { 2 }$ is $\begin{array} { r } { f ( x ) = \frac { 1 } { 3 } x ^ { 3 } } \end{array}$ . According to the Fundamental Theorem, the area under $v ( x )$ is $f ( x )$ :

$$
\begin{array} { r } { \int _ { 0 } ^ { 1 0 0 } v ( x ) d x = f ( 1 0 0 ) - f ( 0 ) = \frac { 1 } { 3 } ( 1 0 0 ) ^ { 3 } . } \end{array}
$$

That Fundamental Theorem is not yet proved! I mean it is not proved by us. Whether Leibniz or Newton managed to prove it, I am not quite sure. But it can be done. Starting from sums of differences, the difficulty is that we have too many limits at once. The sums of $v _ { j } \Delta x$ are approaching the integral. The differences $\Delta f / \Delta x$ approach the derivative. A real proof has to separate those steps, and Section 5.7 will do it.

Proved or not, you are seeing the main point. What was true for the numbers $f _ { j }$ and $v _ { j }$ is true in the limit for $v ( x )$ and $f ( x )$ : Now $v ( x )$ can vary continuously, but it is still the slope of $f ( x )$ : The reverse of slope is area.

Finally we review the area under $v = x$ : The sum of $1 + 2 + \cdots + n$ is ${ \frac { 1 } { 2 } } n ^ { 2 } + { \frac { 1 } { 2 } } n$ : This gives the area of $n = 4 / \Delta x$ rectangles, going out to $x = 4$ : The heights are $j \Delta x$ , the bases are $\Delta x$ , and we add areas:

$$
\sum _ { j = 1 } ^ { 4 / \Delta x } ( j \Delta x ) ( \Delta x ) = ( \Delta x ) ^ { 2 } \left[ \frac { 1 } { 2 } \left( \frac { 4 } { \Delta x } \right) ^ { 2 } + \frac { 1 } { 2 } \left( \frac { 4 } { \Delta x } \right) \right] = 8 + 2 \Delta x .
$$

With $\Delta x = 1$ the area is $1 + 2 + 3 + 4 = 1 0 .$ : WithÑeight rectangles and $\begin{array} { r } { \Delta x = \frac { 1 } { 2 } } \end{array}$ , the area was $8 + 2 \Delta x = 9$ : Sixteen rectangles of width $\textstyle { \frac { 1 } { 4 } }$ brought the correction $2 \Delta x$ down to $\frac { 1 } { 2 }$ : The exact area is 8: The error is proportional to $\Delta x$ .

Important note There you see a question in applied mathematics. If there is an error, what size is it? How does it behave as $\Delta x \to 0 ?$ The $\Delta x$ term disappears in the limit, and $( \Delta x ) ^ { 2 }$ disappears faster. But to get an error of $1 0 ^ { - 6 }$ we need eight million rectangles:

$$
2 \Delta x = 2 \cdot 4 / 8 , 0 0 0 , 0 0 0 = 1 0 ^ { - 6 } .
$$

That is horrifying! The numbers $1 0 , 9 , 8 { \scriptstyle \frac 1 2 } , 8 { \scriptstyle \frac 1 4 } , .$ : : : seem to approach the area 8 in a satisfactory way, but the convergence is much too slow. It takes twice as much work to get one more binary digit in the answer—which is absolutely unacceptable. Somehow the $\Delta x$ term must be removed. If the correction is $( \Delta x ) ^ { 2 }$ instead of $\Delta x$ , then a thousand rectangles will reach an accuracy of $1 0 ^ { - 6 }$ :

The problem is that the rectangles are unbalanced. Their right sides touch the graph of $v$ , but their left sides are much too high. The best is to cross the graph in the middle of the interval—this is the midpoint rule. Then the rectangle sits halfway across the line $v = x$ , and the error is zero. Section 5.8 comes back to this rule—and to Simpson’s rule that fits parabolas and removes the $( \Delta x ) ^ { 2 }$ term and is built into many calculators.

Finally we try the quick way. The area under $v = x$ is $\scriptstyle f = { \frac { 1 } { 2 } } x ^ { 2 }$ , because $d f / d x$ is $v$ : The area out to $x = 4$ is ${ \begin{array} { l } { { \frac { 1 } { 2 } } ( 4 ) ^ { 2 } = 8 } \end{array} }$ : Done.

Optional: $p$ th powers Our sums are following a pattern. First, $1 + \cdots + n$ is ${ \scriptstyle { \frac { 1 } { 2 } } } n ^ { 2 }$ plus ${ \frac { 1 } { 2 } } n$ : The sum of squares is ${ \scriptstyle { \frac { 1 } { 3 } } } n ^ { 3 }$ plus correction terms. The sum of $p$ th powers is

$$
1 ^ { p } + 2 ^ { p } + \cdots + n ^ { p } = { \frac { 1 } { p + 1 } } n ^ { p + 1 } p l u s c o r r e c t i o n t e r m s .
$$

192 The correction involves lower powers of $n$ , and you know what is coming. Those corrections disappear in calculus. The area under $v = x ^ { p }$ from 0 to $n$ is

$$
\int _ { x = 0 } ^ { n } x ^ { p } d x = \operatorname* { l i m } _ { \Delta x \to 0 } \sum _ { j = 1 } ^ { n / \Delta x } ( j \Delta x ) ^ { p } ( \Delta x ) = { \frac { 1 } { p + 1 } } n ^ { p + 1 } .
$$

Calculus doesn’t care if the upper limit $n$ is an integer, and it doesn’t care if the power $p$ is an integer. We only need $p + 1 > 0$ to be sure $n ^ { p + 1 }$ is genuinely the leading term. The antiderivative of $v = x ^ { p }$ is $f = x ^ { p + 1 } / ( p + 1 )$ .

We are close to interesting experiments. The correction terms disappear and the sum approaches the integral. Here are actual numbers for $p = 1$ , when the sum and integral are easy: $S _ { n } = 1 + \cdots + n$ and $\textstyle I _ { n } = \int x d x = { \frac { 1 } { 2 } } n ^ { 2 }$ : The difference is $\begin{array} { r } { D _ { n } = \frac { 1 } { 2 } n } \end{array}$ : The thing to watch is the relative error $\check { E } _ { n } = D _ { n } / \bar { I _ { n } }$ :

$$
\begin{array} { c c c c c } { { n } } & { { S _ { n } } } & { { I _ { n } } } & { { D _ { n } = S _ { n } - I _ { n } } } & { { E _ { n } = D _ { n } / I _ { n } } } \\ { { 1 0 0 } } & { { 5 0 5 0 } } & { { 5 0 0 0 } } & { { 5 0 } } & { { . 0 1 0 } } \\ { { 2 0 0 } } & { { 2 0 1 0 0 } } & { { 2 0 0 0 0 } } & { { 1 0 0 } } & { { . 0 0 5 } } \end{array}
$$

The number 20;100 is ${ \scriptstyle { \frac { 1 } { 2 } } } ( 2 0 0 ) ( 2 0 1 )$ : Please write down the next line $n = 4 0 0$ , and please find a formula for $E _ { n }$ . You can guess $E _ { n }$ from the table, or you can derive it from knowing $S _ { n }$ and $I _ { n }$ : The formula should show that $E _ { n }$ goes to zero. More important, it should show how quick (or slow) that convergence will be.

One more number—a third of a million—was mentioned earlier. It came from integrating $x ^ { 2 }$ from 0 to 100, which compares to the sum $S _ { 1 0 0 }$ of 100 squares:

$$
{ \begin{array} { c c c c c c } { n } & { p } & { S _ { n } } & { I _ { n } = { \frac { 1 } { 3 } } n ^ { 3 } } & { D = S - I } & { E = D / I } \\ { 1 0 0 } & { 2 } & { 3 3 8 3 5 0 } & { 3 3 3 3 3 { \frac { 1 } { 3 } } } & { 5 0 1 6 { \frac { 2 } { 3 } } } & { . 0 1 5 0 5 } \\ { 2 0 0 } & { 2 } & { 2 6 8 6 7 0 0 } & { 2 6 6 6 6 6 { \frac { 2 } { 3 } } } & { 2 0 0 3 3 { \frac { 1 } { 3 } } } & { . 0 0 7 5 1 2 5 } \end{array} }
$$

These numbers suggest a new idea, to keep n fixed and change $p$ . The computer can find sums without a formula! With its help we go to fourth powers and square roots:

In this and future tables we don’t expect exact values. The last entries are rounded off, and the goal is to see the pattern. The errors $E _ { n , p }$ are sure to obey a systematic rule—they are proportional to $1 / n$ and to an unknown number $C ( \boldsymbol { p } )$ that depends on $p$ : I hope you can push the experiments far enough to discover $C ( \boldsymbol { p } )$ : This is not an exercise with an answer in the back of the book—it is mathematics.