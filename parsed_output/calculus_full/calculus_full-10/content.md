CHAPTER 10

# Infinite Series

Infinite series can be a pleasure (sometimes). They throw a beautiful light on sin $x$ and cos $x$ . They give famous numbers like $\pi$ and $e$ . Usually they produce totally unknown functions—which might be good. But on the painful side is the fact that an infinite series has infinitely many terms.

It is not easy to kno w the sum of those terms.8Morethan that, it is not certain that there is a sum. We need tests, to decide if the series converges. We also need ideas, to discover what the series converges $t o$ . Here are examples of convergence, divergence, and oscillation:

$$
\begin{array} { r l } { 1 + \frac { 1 } { 2 } + \frac { 1 } { 4 } + \dots = 2 } & { { } 1 + 1 + 1 + \dots = \infty \quad 1 - 1 + 1 - 1 \dots = ? } \end{array}
$$

The first series converges. Its next term is $1 / 8$ , after that is $1 / 1 6$ —and every step brings us halfway to 2. The second series (the sum of $1 \mathrm { { ^ { \circ } s } }$ ) obviously diverges to infinity. The oscillating example (with 1’s and $- 1 \mathrm { { ' s } ) }$ also fails to converge.

All those and more are special cases of one infinite series which is absolutely the most important of all:

$$
T h e \ g e o m e t r i c \ s e r i e s \ i s \ 1 + x + x ^ { 2 } + x ^ { 3 } + \cdots = { \frac { 1 } { 1 - x } } .
$$

This is a series of functions. It is a “power series.” When wesubstitute numbers for $x$ , the series on the left may converge to the sum on the right. We need to know when it doesn’t. Choose $\begin{array} { r } { x = \frac { 1 } { 2 } } \end{array}$ and $x = 1$ and $x = - 1$ :

${ \begin{array} { l } { \displaystyle 1 + { \frac { 1 } { 2 } } + \left( { \frac { 1 } { 2 } } \right) ^ { 2 } + \cdots { \mathrm { ~ i s ~ t h e ~ c o n v e r g e n t ~ s e r i e s . ~ I t s ~ s u m ~ i s ~ } } { \frac { 1 } { 1 - { \frac { 1 } { 2 } } } } = 2 } \\ { \displaystyle 1 + 1 + 1 + \cdots { \mathrm { ~ i s ~ d i v e r g e n t . ~ I t s ~ s u m ~ i s ~ } } { \frac { 1 } { 1 - 1 } } = { \frac { 1 } { 0 } } = \infty } \end{array} }$ $1 + ( - 1 ) + ( - 1 ) ^ { 2 } + \cdots$ is the oscillating series. Its sum should be ${ \frac { 1 } { 1 - ( - 1 ) } } = { \frac { 1 } { 2 } }$

The last sum bounces between one and zero, so at least its average is $\frac { 1 } { 2 }$ . At $x = 2$ there is no way that $1 + 2 + 4 + 8 + \cdots$ agrees with $1 / ( 1 - 2 )$ .

This behavior is typical of a power series—to converge in an interval of $x$ ’s and to diverge when $x$ is large. The geometric series is safe for $x$ between $^ { - 1 }$ and 1. Outside that range it diverges.

# The next example shows a repeating decimal 1:111 : :

The decimal 1:111 : : : is also the fraction $1 / \left( 1 - { \frac { 1 } { 1 0 } } \right)$ , which is $1 0 / 9$ . Every fraction leads to a repeating decimal. $E$ very rep eatingdecimal adds up (through the geometric series) to a fraction.

To get 3:333 : : : ; just multiply by 3. This is $1 0 / 3$ . To get 1:0101 : : :; set $x = 1 / 1 0 0$ This is the fraction $\begin{array} { r } { \dot { 1 } / \big ( 1 - \frac { \dot { 1 } } { 1 0 0 } \big ) } \end{array}$ , which is 100=99.

Here is an unusual decimal (which eventually repeats). I don’t really understand it:

$$
{ \frac { 1 } { 2 4 3 } } = . 0 0 4 1 1 5 2 2 6 3 3 7 4 4 8 \ldots
$$

Most numbers are not fractions (or repeating decimals). A good example is $\pi$ :

$$
\pi = 3 + { \frac { 1 } { 1 0 } } + { \frac { 4 } { 1 0 0 } } + { \frac { 1 } { 1 0 0 0 } } + { \frac { 5 } { 1 0 0 0 0 } } + \cdots .
$$

This is 3:1415 : : :, a series that certainly converges. We happen to know the first billion terms (the billionth is given below). Nobody knows the 2 billionth term. Compare that series with this one, which also equals $\pi$ :

$$
\pi = 4 - { \frac { 4 } { 3 } } + { \frac { 4 } { 5 } } - { \frac { 4 } { 7 } } + \cdots
$$

That alternating series is really remarkable. It is typical of this chapter, because its pattern is clear. We know the 2 billionth term (it has a minus sign). This is not a geometric series, but in Section 10.1 it comes from a geometric series.

Question Does this series actually converge ? What if all signs are $+ ?$

Answer The alternating series converges to $\pi$ (Section 10.3). The positive series diverges to infinity (Section 10.2). The terms go to zero, but their sum is infinite.

This example begins to show what the chapter is about. Part of the subject deals with special series, adding to $1 0 / 9$ or $\pi$ or $e ^ { x }$ . The other part is about series in general, adding to numbers or functions that nobody has heard of. The situation was the same for integrals—they give famous answers like $\ln x$ or unknown answers like $\int x ^ { x } d x$ . The sum of $1 + 1 / 8 + 1 / 2 7 + \cdots$ is also unknown—although a lot of mathematicians have tried.

The chapter is not long, but it is full. The last half studies power series. We begin with a linear approximation like $1 + x$ . Next is a quadratic approximation like $1 + x + x ^ { 2 }$ . In the end we match all the derivatives of $f ( x )$ . This is the “Taylor series,” a new way to create functions—not by formulas or integrals but by infinite series.

No example can be better than $1 / ( 1 - x )$ , which dominates Section 10.1. Then we define convergence and test for it. (Most tests are really comparisons with a geometric series.) The second most important series in mathematics is the exponential series $e ^ { x } = 1 + x + { \textstyle \frac { 1 } { 2 } } x ^ { 2 } + { \textstyle \frac { 1 } { 6 } } x ^ { 3 } + \cdots .$ . It includes the series for sin $x$ and cos $x$ , because of the formula $e ^ { i x } = \cos x + i \sin x$ . Finally a whole range of new and old functions will come from Taylor series.

In the end, all the key functions of calculus appear as “infinite polynomials” (except the step function). This is the ultimate voyage from the linear function $y =$ $m x + b$ .