# 5.2 Antiderivatives

The symbol $\scriptstyle \int$ was invented by Leibniz to represent the integral. It is a stretched-out S, from the Latin word for sum. This symbol is a powerful reminder of the whole construction: Sum approaches integral, S approaches $\int .$ , and rectangular area approaches curved area:

$$
\begin{array} { r } { c u r v e d \ a r e a = \int v ( x ) \ d x = \int \sqrt { x } \ d x . } \end{array}
$$

The rectangles of base $\Delta x$ lead to this limit—the integral of $\sqrt { x }$ . The $\cdot _ { d x } ,$ ” indicates that $\Delta x$ approaches zero. The heights $v _ { j }$ of the rectangles are the heights $v ( x )$ of the curve. The sum of $v _ { j }$ times $\Delta x$ approaches “the integral of $v$ of $x d x$ .” You can imagine an infinitely thin rectangle above every point, instead of ordinary rectangles above special points.

We now find the area under the square root curve. The “limits of integration” are 0 and 4. The lower limit is $x = 0$ , where the area begins. (The »start could be any point $x = a .$ .) The upper limit is $x = 4$ , since we stop after four years. (The finish couldÑbe any point $x = b$ .) The area of the rectangles is a sum of base $\Delta x$ times heights $\sqrt { x }$ . The curved area is the limit of this sum. That limit is the integral of $\sqrt { x }$ from 0 to 4:

$$
\operatorname* { l i m } _ { \Delta x \to 0 } \left[ ( { \sqrt { \Delta x } } ) ( \Delta x ) + ( { \sqrt { 2 \Delta x } } ) ( \Delta x ) + \cdots + ( { \sqrt { 4 } } ) ( \Delta x ) \right] = \int _ { x = 0 } ^ { x = 4 } { \sqrt { x } } d x .
$$

The outstanding problem of integral calculus is still to be solved?. What is this limiting area? We have a symbol for the answer, involving $\scriptstyle \int$ and $\sqrt { x }$ and $d x$ —but we don’t have a number.

# THE ANTIDERIVATIVE

I wish I knew who discovered the area under the graph of $\sqrt { x }$ . It may have been Newton. The answer was available earlier, but the key idea was shared by Newton and Leibniz. They understood the parallels between sums and integrals, and between differences and derivatives. I can give the answer, by following that analogy. I can’t give the proof (yet)—it is the Fundamental Theorem of Calculus.

In algebra the difference $f _ { j } - f _ { j - 1 }$ is $v _ { j }$ . When we add, the sum of the $v$ ’s is $f _ { n } - f _ { 0 }$ . In calculus the derivative of $f ( x )$ is $v ( x )$ . When we integrate, the area under the $v ( x )$ curve is $f ( x )$ minus $f ( 0 )$ . Our problem asks for the area out to $x =$ 4:

5B (Discrete vs. continuous, rectangles vs. c?urved areas, addition vs. integration) The integral of $v ( x )$ is the difference in $f ( x )$ :? $I f \ d f / d x = { \sqrt { x } } \ t h e n \ a r e a = \int _ { x = 0 } ^ { x = 4 } { \sqrt { x } } \ d x = f ( 4 ) - f ( 0 ) .$ (3)

What is $f ( x ) ?$ Instead of the derivative of $\sqrt { x }$ , we need its “antiderivative.” We have to find a function $f ( x )$ whose derivative is $\sqrt { x }$ . It is the opposite of Chapters $2 - 4$ ; and requires us to work backwards. The derivative of $x ^ { n }$ is $n x ^ { n - 1 }$ —now we need the antiderivative. The quick formula is $f ( x ) = x ^ { n + 1 } / ( n + 1 )$ —we aim to understand it.

Solution Since the derivative lowers the exponent, the antiderivative raises it. We go from $x ^ { 1 / 2 }$ to $x ^ { 3 / 2 }$ . But then the derivative is $( 3 / 2 ) x ^ { 1 / 2 }$ . It contains an unwanted factor 3=2. To cancel that factor, put $2 / 3$ into the antiderivative:

$\begin{array} { r } { f ( x ) = \frac { 2 } { 3 } x ^ { 3 / 2 } } \end{array}$ has the required derivative $v ( x ) = x ^ { 1 / 2 } = \sqrt { x }$ :

There you see the key to integrals: Work backward from derivatives (and adjust). Now comes a number—the exact area. At $x = 4$ we find $x ^ { 3 / 2 } = 8$ . Multiply by $2 / 3$ to get $1 6 / 3$ . Then subtract $f ( 0 ) = 0$ :

$$
\int _ { x = 0 } ^ { x = 4 } { \sqrt { x } } d x = { \frac { 2 } { 3 } } ( 4 ) ^ { 3 / 2 } - { \frac { 2 } { 3 } } ( 0 ) ^ { 3 / 2 } = { \frac { 2 } { 3 } } ( 8 ) = { \frac { 1 6 } { 3 } }
$$

The total income over four years is $1 6 / 3 = 5 \frac { 1 } { 3 }$ million dollars. This is $f ( 4 ) -$ $f ( 0 )$ . The sum from thousands of rectangles was slowly app?roaching this exact area $5 \frac 1 3$ .

Other areas The income in the first year, at $x = 1$ , is $\textstyle { \frac { 2 } { 3 } } ( 1 ) ^ { 3 / 2 } = { \frac { 2 } { 3 } }$ million dollars. (The false income was 1 million dollars.) The total income after $x$ years is ${ \textstyle \frac { 2 } { 3 } } ( x ) ^ { 3 / 2 }$ , which is the antiderivative $f ( x )$ . The square root curve covers $2 / 3$ of the overall rectangle it sits in. The rectangle goes out to $x$ and up to $\sqrt { x }$ , with area $x ^ { 3 / 2 }$ , and $2 / 3$ of that rectangle is below the curve. $1 / 3$ is above.)

Other antiderivatives The derivative of $x ^ { 5 }$ is $5 x ^ { 4 }$ . Therefore the antiderivative of $x ^ { 4 }$ is $x ^ { 5 } / 5$ . Divide by $5 ( \mathrm { o r } n + 1 )$ to cancel the 5 (or $n + 1$ ) from the derivative. And don’t allow $n + 1 = 0$ :

The der?ivative $v ( x ) = x ^ { n }$ has the a?ntiderivative $f ( x ) = x ^ { n + 1 } / ( n + 1 )$ :

EXAMPLE 1 The antiderivative of $x ^ { 2 }$ is ${ \scriptstyle { \frac { 1 } { 3 } } } x ^ { 3 }$ . This is the area under the parabola $v ( x ) = x ^ { 2 }$ . The area out to $x = 1$ is $\textstyle { \frac { 1 } { 3 } } ( 1 ) ^ { 3 } - { \frac { 1 } { 3 } } ( 0 ) ^ { 3 }$ , or $1 / 3$ .

Remark on $\sqrt { x }$ and $x ^ { 2 }$ The $2 / 3$ from $\sqrt { x }$ and the $1 / 3$ from $x ^ { 2 }$ add to 1. Those are the areas below and above the $\sqrt { x }$ curve, in the corner of Figure 5.3. If you turn the curve by $9 0 ^ { \circ }$ , it becomes the parabola. The functions $y = { \sqrt { x } }$ and $x = y ^ { 2 }$ are inverses! The areas for these inverse functions add to a square of area 1.

# AREA UNDER A STRAIGHT LINE

You already know the area of a triangle. The region is below the diagonal line $v = x$ in Figure 5.4. The base is 4, the height is 4, and the area is $\scriptstyle { \frac { 1 } { 2 } } ( 4 ) ( 4 ) = 8$ . Integration is

not required! But if you allow calculus to repeat that answer, and build up the integral $\textstyle f ( x ) { \overset { } { = } } { \frac { 1 } { 2 } } x ^ { 2 }$ as the limiting area of many rectangles, you will have the beginning of something important.

The four rectangles have area $1 + 2 + 3 + 4 = 1 0$ . That is greater than 8, because the triangle is inside. 10 is a first approximation to the triangular area 8, and to improve it we need more rectangles.

The next rectangles will be thinner, of width $\Delta x = 1 / 2$ instead of the original $\Delta x = 1$ . There will be eight rectangles instead of four. They extend above the line, so the answer is still too high. The new heights are $1 / 2 , 1 , 3 / 2 , 2 , 5 / 2 , 3 , 7 / 2 , 4 .$ The total area in Figure $5 . 4 \mathrm { b }$ is the sum of the base $\Delta x = 1 / 2$ times those heights:

Question What is the area of 16 rectangle s? Their heights are ${ \textstyle { \frac { 1 } { 4 } } , { \frac { 1 } { 2 } } , \ldots , 4 }$ Answer With base $\begin{array} { r } { \Delta x = \frac { 1 } { 4 } } \end{array}$ the area is $\textstyle { \frac { 1 } { 4 } } ( { \frac { 1 } { 4 } } + { \frac { 1 } { 2 } } + \cdots + 4 ) = { \dot { 8 } } { \frac { 1 } { 2 } }$ .

The effort of doing the addition is increasing. A formula for the sums is needed, and will be established soon. (The next answer would be $8 { \scriptstyle { \frac { 1 } { 4 } } }$ .) But more important than the formula is the idea. We are carrying out a Iimiting process, one step at a time. The area of the rectangles is approaching the area of the triangle, as $\Delta x$ decreases. The same limiting process will apply to other areas, in which the region is much more complicated. Therefore we pause to comment on what is important.

# Area Under a Curve

What requirements are imposed on those thinner and thinner rectangles? It is not essential that they all have the same width. And it is not required that they cover the triangle completely. The rectangles could lie below the curve. The limiting answer will still be 8, even if the widths $\Delta x$ are unequal and the rectangles fit inside the triangle or across it. We only impose two rules:

1. The largest width $\Delta x _ { \mathrm { m a x } }$ must approach zero.   
2. The top of each rectangle must touch or cross the curve.

The area under the graph is defined to be the limit of these rectangular areas, if that limit exists. For the straight line, the limit does exist and equals 8. That limit is independent of the particular widths and heights—as we absolutely insist it should be.

Section 5.5 allows any continuous $v ( x )$ . The question will be the same—Does the limit exist? The answer will be the same—Yes. That limit will be the integral of $v ( x )$ , and it will be the area under the curve. It will be $f ( x )$ .

EXAMPLE 2 The triangular area from 0 to $x$ is ${ \textstyle \frac { 1 } { 2 } } ( \mathrm { b a s e } ) ( \mathrm { h e i g h t } ) = { \textstyle \frac { 1 } { 2 } } ( x ) ( x )$ . That is $\begin{array} { r } { f ( x ) = \frac { 1 } { 2 } x ^ { 2 } } \end{array}$ . Its derivative is $v ( x ) = x$ . But notice that ${ \frac { 1 } { 2 } } x ^ { 2 } + 1$ has the same derivative. So does $f = { \textstyle \frac { 1 } { 2 } } x ^ { 2 } + C$ , for any constant $C$ . There is a “constant of integration” in $f ( x )$ , which is wiped out in its derivative $v ( x )$ .

EXAMPLE 3 Suppose the velocity is decreasing: $v ( x ) = 4 - x$ . If we sample $v$ at $x = 1 , 2 , 3 , 4$ ; the rectangles lie under the graph. B ecause $v$ is decreasing, the right end of each interval gives $v _ { \mathrm { m i n } }$ . Then the rectangular area $3 + 2 + 1 + 0 = 6$ is less than the exact area 8. The rectangles are inside the triangle, and eight rectangles with base $\frac { 1 } { 2 }$ come closer:

$$
{ \mathrm { r e c t a n g u l a r ~ a r e a } } = { \textstyle { \frac { 1 } { 2 } } } ( 3 { \textstyle { \frac { 1 } { 2 } } } + 3 + \cdots + { \frac { 1 } { 2 } } + 0 ) = 7 .
$$

Sixteen rectangles would have area $7 \frac { 1 } { 2 }$ . We repeat that the rectangles need not have the same widths $\Delta x$ , but it makes these calculations easier.

What is the area out to an arbitrarypoint (like $x = 3$ or $x = 1$ )? We could insert rectangles, but the Fundamental Theorem offers a faster way. Any antiderivative of $4 - x$ will give the area. We look for a function whose derivative is $_ { 4 - x }$ . The derivative of $_ { 4 x }$ is 4, the derivative of ${ \scriptstyle { \frac { 1 } { 2 } } } x ^ { 2 }$ is $x$ , so work backward:

$$
) { \mathrm { ~ a c h i e v e ~ } } d f / d x = 4 - x { \mathrm { ~ c h o o s e ~ } } f ( x ) = 4 x - { \textstyle { \frac { 1 } { 2 } } } x ^ { 2 } .
$$

Calculus skips past the rectangles and computes $f ( 3 ) = 7 { \frac { 1 } { 2 } }$ . The area between $x =$ 1 and $x = 3$ is the difference $7 { \frac { 1 } { 2 } } - 3 { \frac { 1 } { 2 } } = 4$ . In Figure 5.5, this is the area of the trapezoid.

The f-curve flattens out when the $v$ -curve touches zero. No new area is being added.

# 5 Integrals

# INDEFINITE INTEGRALS AND DEFINITEINTEGRALS

We have to distinguish two different kinds of integrals. They both use the antiderivative $f ( x )$ . The definite one involves the limits 0 and 4, the indefinite one doesn’t:

The indefinite integral is a function $f ( x ) = 4 x - { \textstyle { \frac { 1 } { 2 } } } x ^ { 2 } .$ .   
The definite integral from $x = 0$ to $x = 4$ is the number $f ( 4 ) - f ( 0 )$ .

The definite integral is definitely 8. Butthe indefinite integral is not necessarily $4 x - { \textstyle { \frac { 1 } { 2 } } } x ^ { 2 }$ . We can change $f ( x )$ by a constant without changing its derivative (since the derivative of a constant is zero). The following functions are also antiderivatives:

$$
\begin{array} { r } { f ( x ) = 4 x - \frac { 1 } { 2 } x ^ { 2 } + 1 , \qquad f ( x ) = 4 x - \frac { 1 } { 2 } x ^ { 2 } - 9 , \qquad f ( x ) = 4 x - \frac { 1 } { 2 } x ^ { 2 } + C . } \end{array}
$$

The first two are particular examples. The last is the general case. The constant $C$ can be anything (including zero), to give all functions with the required derivative. The theory of calculus will show that there are no others. The indefinite integral is the most general antiderivative (with no limits):

$$
\begin{array} { r } { i n d e f i n i t e \ i n t e g r a l \ f ( x ) = \int v ( x ) \ d x = 4 x - \frac { 1 } { 2 } x ^ { 2 } + C . } \end{array}
$$

By contrast, the definite integral is a number. It contains no arbitrary constant $C$ . More that that, it contains no variable $x$ . The definite integral is determined by the function $v ( x )$ and the limits of integration (also known as the endpoints). It is the area under the graph between those endpoints.

To see the relation of indefinite todefinite, answer thisquestion: What is the definite integral between $x = 1$ and $x = 3 2$ The indefinite integral gives $f ( 3 ) = 7 { \scriptstyle { \frac { 1 } { 2 } } + } \bar { C }$ and $f ( 1 ) = 3 { \frac { 1 } { 2 } } + C$ . To find the area between the limits, subtract $f$ at one limit from $f$ at the other limit:

$$
\begin{array} { r } { \int _ { x = 1 } ^ { 3 } v ( x ) d x = f ( 3 ) - f ( 1 ) = ( 7 \frac { 1 } { 2 } + C ) - ( 3 \frac { 1 } { 2 } + C ) = 4 . } \end{array}
$$

The constant cancels itself! The definite integral is the difference between the values of the indefinite integ»ral. $C$ disappea»rs in the subtraction.

The difference $f ( 3 ) - f ( 1 )$ is like $f _ { n } - f _ { 0 }$ . The sum of $v _ { j }$ from 1 to $n$ has become “the integral of $v ( x )$ from 1 to 3.” Section 5.3 computes other areas from sums, and 5:4 computes many more from antiderivatives. Then we come back to the definite integral and the Fundamental Theorem:

$$
\int _ { a } ^ { b } v ( x ) d x = \int _ { a } ^ { b } { \frac { d f } { d x } } d x = f ( b ) - f ( a ) .
$$