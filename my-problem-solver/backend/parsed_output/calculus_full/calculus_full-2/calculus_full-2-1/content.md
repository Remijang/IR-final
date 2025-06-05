This chapter begins with the definition of the derivative. Two examples were in Chapter 1: When the distance is $t ^ { 2 }$ , the velocity is $2 t$ : When $f ( t ) = \sin t$ we found $v ( t ) = \cos t$ : The velocity is now called the derivative of $f ( t )$ : As we move to a more formal definition and new examples, we use new symbols $f ^ { \prime }$ and $d f / d t$ for the derivative.

2A At time $t$ , the derivative $f ^ { \prime } ( t )$ or $d f / d t$ or $v ( t )$ is

$$
f ^ { \prime } ( t ) = \operatorname* { l i m } _ { \Delta t \to 0 } { \frac { f ( t + \Delta t ) - f ( t ) } { \Delta t } } .
$$

The ratio on the right is the average velocity over a short time $\Delta t$ : The derivative, on the left side, is its limit as the step $\Delta t$ (delta $t$ ) approaches zero.

Go slowly and look at each piece. The distance at time $t + \Delta t$ is $f ( t + \Delta t )$ : The distance at time $t$ is $f ( t )$ : Subtraction gives the change in distance, between those times. We often write $\Delta f$ for this differenceÑ: $\Delta f = f ( t + \Delta t ) - f ( t )$ : The average velocity is the ratio $\Delta f / \Delta t$ —change in distance divided by change in time.

The limit of the average velocity is the derivative, if this limit exists:

$$
{ \frac { d f } { d t } } = \operatorname* { l i m } _ { \Delta t \to 0 } { \frac { \Delta f } { \Delta t } } .
$$

This is the neat notation that Leibniz invented: $\Delta f / \Delta t$ approaches $d f / d t$ : Behind the innocent word “limit” is a process that this course will help you understand.

Note that $\Delta f$ is not $\Delta$ times $f ! I t$ is the change in $f .$ Similarly $\Delta t$ is not $\Delta$ times $t$ : It is the time step, positive or negative and eventually small. To have a one-letter symbol we replace $\Delta t$ by $h$ :

The right sides of (1) and (2) contain average speeds. On the graph of $f ( t )$ , the distance $u p$ is divided by the distance across. That gives the average slope $\Delta f / \Delta t$ :

The left sides of (1) and (2) are instantaneous speeds $d f / d t$ : They give the slope at the instant $t$ : This is the derivative $d f / d t$ (when $\Delta t$ and $\Delta f$ shrink to zero). Look again at the calculation for $f ( t ) = t ^ { 2 }$ :

$$
\frac { \Delta f } { \Delta t } = \frac { f ( t + \Delta t ) - f ( t ) } { \Delta t } = \frac { t ^ { 2 } + 2 t \Delta t + ( \Delta t ) ^ { 2 } - t ^ { 2 } } { \Delta t } = 2 t + \Delta t .
$$

Important point: Those steps are taken before $\Delta t$ goes to zero. $\pmb { I f }$ we set $\Delta t = 0$ too soon, we learn nothing. The ratio $\Delta f / \Delta t$ becomes $0 / 0$ (which is meaningless). The numbers $\Delta f$ and $\Delta t$ must approach zero together, not separately. Here their ratio is $2 t + \Delta t$ , the average speed.

To repeat: Success came by writing out $( t + \Delta t ) ^ { 2 }$ and subtracting $t ^ { 2 }$ and dividing by $\Delta t$ : Then and only then can we approach $\Delta t = 0$ : The limit is the derivative $2 t$ :

There are several new things in formulas (1) and (2). Some are easy but important, others are more profound. The idea of a function we will come back to, and the definition of a limit. But the notations can be discussed right away. They are used constantly and you also need to know how to read them aloud:

$$
\Delta f = ^ { \mathit { \mathrm { * } } } \mathrm { d e l t a } \ f ^ { \prime \prime } = { \mathrm { t h e \ c h a n g e \ } } f ( t + \Delta t ) - f ( t )
$$

From those last words you see what lies b1 ehind the notation $d f / d t$ : The symbol $\Delta t$ indicates a nonzero (usually short) length of time. The symbol $d t$ indicates an infinitesimal (even shorter) length of time. Some mathematicians work separately with $d f$ and $d t$ , and $d f / d t$ is their ratio. For us $d f / d t$ is a single notation (don’t cancel $d$ and don’t cancel $\Delta$ ). The derivative $d f / d t$ is the limit of $\Delta f / \Delta t$ : When that notation $d f / d t$ is awkward, use $f ^ { \prime } o r v$ :

Remark The notation hides one thing w1e should mention. The time step can be negative just as easily as positive. We can compute the average $\Delta f / \Delta t$ over a time interval before the time $t$ , instead of after. This ratio also approaches $d f / d t$ :

The notation also hides another thing: The derivative might not exist. The averages $\Delta f / \Delta t$ might not approach a limit (it has to be the same limit going forward and backward from time $t$ ). In that case $f ^ { \prime } ( t )$ is not defined. At that instant there is no clear reading on the speedometer. This will happen in Example 2.

EXAMPLE 1 (Constant velocity $V = 2$ ) The distance $f$ is $V$ times $t$ : The distance at time $t + \Delta t$ is $V$ times $t + \Delta t$ : The difference $\Delta f$ is $V$ times $\Delta t$ :

$$
{ \frac { \Delta f } { \Delta t } } = { \frac { V \Delta t } { \Delta t } } = V \quad { \mathrm { s o ~ t h e ~ l i m i t ~ i s } } \quad { \frac { d f } { d t } } = V .
$$

The derivative of $V t$ is $V .$ The derivative of $2 t$ is 2: The averages $\Delta f / \Delta t$ are always $V = 2$ , in this exceptional case of a constant velocity.

# 2.1 The Derivative of a Function

EXAMPLE 2 Constant velocity 2 up to time $t = 3$ , then stop.

For small time¡s we still have $f ( t ) = 2 t$ : But after the stopÑping time, the distance is fixed at $f ( t ) = 6$ : The graph is flat beyond time 3. Then $f ( t + \Delta t ) = f ( t )$ and $\Delta f = 0$ and the derivative of a constant function is zero:

$$
t > 3 : \ : \ : f ^ { \prime } ( t ) = \operatorname* { l i m } _ { \Delta t \to 0 } { \frac { f ( t + \Delta t ) - f ( t ) } { \Delta t } } = \operatorname* { l i m } _ { \Delta t \to 0 } { \frac { 0 } { \Delta t } } = 0 .
$$

In this example the derivative is not defined at the instant wh1en $t = 3$ . The velocity falls suddenly from 2 to zero. The ratio $\Delta f / \Delta t$ depends, at that special moment, on whether $\Delta t$ is positive or negative. The average velocity after time $t = 3$ is zero. The average velocity before that time is 2: When the graph of $f$ has a corner, the graph of $v$ has a jump. It is a step function.

One new part of that example is the notation $( d f / d t$ or $f ^ { \prime }$ instead of $v$ ). Please look also at the third figure. It shows how the function takes $t$ (on the left) to $f ( t )$ : Especially it shows $\Delta t$ and $\Delta f .$ At the start, $\Delta f / \Delta t$ is 2. After the stop at $t = 3$ , all $t$ ’s go to the same $f ( t ) = 6$ : So $\Delta f = 0$ and $d f / d t = 0$ :

# THE DERIVATIVE OF 1=t

Here is a completely different slope, for the “demand function” $f ( t ) = 1 / t$ : The demand is $1 / t$ when the price is $t$ : A high price $t$ means a low demand $1 / t$ : Increasing the price reduces the demand. The calculus question is: How quickly does $1 / t$ change when t changes ? The “marginal demand” is the slope of the demand curve.

The big thing is to find the derivative of $1 / t$ once and for all. It is $- 1 / t ^ { 2 }$ :

Line 1 is algebra, line 2 is calculus. The first step in line 1 subtracts $f ( t )$ from $f ( t + \Delta t )$ : The difference is $1 / ( t + \Delta t )$ minus $1 / t$ : The common denominator is $t$ times $t + \Delta t$ —this makes the algebra possible. We can’t set $\Delta t = 0$ in line 2; until we have divided by $\Delta t$ :

The average is $\Delta f / \Delta t = - 1 / t ( t + \Delta t )$ : Now set $\Delta t = 0$ : The derivative is $- 1 / t ^ { 2 }$ : Section 2:4 will discuss the first of many cases when substituting $\Delta t = 0$ is not possible, and the idea of a limit has to be made clearer.

Check the algebra at $t = 2$ and $t + \Delta t = 3$ : The demand $1 / t$ drops from $1 / 2$ to $1 / 3$ : The difference is $\Delta f = - 1 / 6$ , which agrees with $- 1 / ( 2 ) ( 3 )$ in line 1. As the steps $\Delta f$ and $\Delta t$ get smaller, their ratio approaches $- 1 / ( 2 ) ( 2 ) = - 1 / 4$ :

This derivative is negative. The function $1 / t$ is decreasing, and $\Delta f$ is below zero. The graph is going downward in Figure 2.2, and its slope is negative:

An increasing $f ( t )$ has positive slope. A decreasing $f ( t )$ has negative slope.

The slope $- 1 / t ^ { 2 }$ is very negative for small $t$ : A price increase severely cuts demand.

The next figure makes a small but important point. There is nothing sacred about $t$ : Other letters can be used—especially $x$ : A quantity can depend on position instead of time. The height changes as we go west. The area of a square changes as the side changes. Those are not affected by the passage of time, and there is no reason to use $t$ : You will often see $y = f ( x )$ , with $x$ across and $y$ up—connected by a function $f .$

Similarly, $f$ is not the only possibility. Not every function is named $f !$ That letter is useful because it stands for the word function—but we are perfectly entitled to write $y ( x )$ or $y ( t )$ instead of $f ( x )$ or $f ( t )$ : The distance up is a function of the distance across. This relationship $^ { 6 6 } y$ of $x ^ { \prime \prime }$ is all-important to mathematics.

The slope is also a function. Calculus is about two functions, $y ( x )$ and $d y / d x$ :

Question If we add 1 to $y ( x )$ , what happens to the slope ? Answer Nothing.

Question If we add 1 to the slope, what happens to the height ? Answer

The symbols $t$ and $x$ represent independent variables—they take any value they want to (in the domain). Once they are set, $f ( t )$ and $y ( x )$ are determined. Thus $f$ and $y$ represent dependent variables—they depend on $t$ and $x$ : A change $\Delta t$ produces a

# 2.1 The Derivative of a Function

change $\Delta f .$ A change $\Delta x$ produces $\Delta y$ : The independent variable goes inside the parentheses in $f ( t )$ and $y ( x )$ : It is not the letter that matters, it is the idea:

$$
{ \begin{array} { r l } & { { \mathrm { i n d e p e n d e n t ~ v a r i a b l e } } t { \mathrm { ~ o r ~ } } x } \\ & { { \mathrm { d e p e n d e n t ~ v a r i a b l e ~ } } f { \mathrm { ~ o r ~ } } g { \mathrm { ~ o r ~ } } y { \mathrm { ~ o r ~ } } z { \mathrm { ~ o r ~ } } u } \\ & { { \mathrm { d e r i v a t i v e ~ } } d f / d t { \mathrm { ~ o r ~ } } d f / d x { \mathrm { ~ o r ~ } } d y / d x { \mathrm { ~ o r ~ } } \cdots } \end{array} }
$$

The derivative $d y / d x$ comes from [change in $y ]$ divided by [change in $x$ ]. The time step becomes a space step, forward or backward. The slope is the rate at w1 hich $y$ changes with $x$ : The derivative of a function is its “rate of chaÑnge.”

I mention that physics books use $x ( t )$ for distance. Darn it.

To emphasize the definition of a derivative, here it is again with $y$ and $x$ :

$$
{ \frac { \Delta y } { \Delta x } } = { \frac { y ( x + \Delta x ) - y ( x ) } { \Delta x } } = { \frac { \mathrm { d i s t a n c e \ u p } } { \mathrm { d i s t a n c e \ a c r o s s } } } { \frac { d y } { d x } } = \operatorname* { l i m } _ { \Delta x \to 0 } { \frac { \Delta y } { \Delta x } } = y ^ { \prime } ( x ) .
$$

The notation $y ^ { \prime } ( x )$ pins down the point $x$ where the 1slope is computed. In $d y / d x$ that extra precision is omitted. This book will try for a reasonable compromise between logical perfection and ordinary simplicity. The notation $d y / d x ( x )$ is not good; $y ^ { \prime } ( x )$ is better; when $x$ is understood it need not be written in parentheses.

You are allowed to say that the function is $y = x ^ { 2 }$ and the derivative is $y ^ { \prime } = 2 x -$ even if the strict notation requires $y ( x ) = x ^ { 2 }$ and $y ^ { \prime } ( x ) = 2 x$ : You can even say that the function is $x ^ { 2 }$ and its derivative is $2 x$ and its second derivative is 2—provided everybody knows what you mean.

Here is an example. It is a little early and optional but terrific. You get excellent practice with letters and symbols, and out come new derivatives.

EXAMPLE 4 If $u ( x )$ has slope $d u / d x$ , what is the slope of $f ( x ) = ( u ( x ) ) ^ { 2 } ?$

From the derivative of $x ^ { 2 }$ this will give the derivative of $x ^ { 4 }$ : In that case $u = x ^ { 2 }$ and $f = x ^ { 4 }$ : First point: The derivative of $u ^ { 2 }$ is not $( d u / d x ) ^ { 2 }$ . We do not square the derivative $2 x$ : To find the “square rule” we start as we have to—with $\Delta f = f ( x + \Delta x ) - f ( x )$ :

$$
\Delta f = ( u ( x + \Delta x ) ) ^ { 2 } - ( u ( x ) ) ^ { 2 } = [ u ( x + \Delta x ) + u ( x ) ] [ u ( x + \Delta x ) - u ( x ) ] .
$$

This algebra puts $\Delta f$ in a convenient form. We factored $a ^ { 2 } - b ^ { 2 }$ into $[ a + b ]$ times $[ a - b ]$ : Notice that we don’t have $( \Delta u ) ^ { 2 }$ : We have $\Delta f$ , the change in $u ^ { 2 }$ : Now divide by $\Delta x$ and take the limit:

$$
\frac { \Delta f } { \Delta x } = \left[ u ( x + \Delta x ) + u ( x ) \right] \left[ \frac { u ( x + \Delta x ) - u ( x ) } { \Delta x } \right] \mathrm { a p p r o a c h e s } 2 u ( x ) \frac { d u } { d x } .
$$

This is the square rule: The derivative of $( u ( x ) ) ^ { 2 }$ is $2 u ( x )$ times $d u / d x$ .  From the derivatives of $x ^ { 2 }$ and $1 / x$ and sin $x$ (all known) the examples give new derivatives.

EXAMPLE 5 . $\left( u = x ^ { 2 } \right)$ / The derivative of $x ^ { 4 }$ is $2 u d u / d x = 2 ( x ^ { 2 } ) ( 2 x ) = 4 x ^ { 3 } .$ : EXAMPLE 6 . $( u = 1 / x )$ / The derivative of $1 / x ^ { 2 }$ is $2 u d u / d x = ( 2 / x ) ( - 1 / x ^ { 2 } ) = - 2 / x ^ { 3 } .$ EXAMPLE 7 . $\overset { \cdot } { u } = \sin \overset { \cdot } { x }$ ; $d u / d x = \cos x ,$ / The derivative of $u ^ { 2 } = \sin ^ { 2 } x$ is $2 \sin x \cos x$ :

Mathematics is really about ideas. The notation is created to express those ideas. Newton and Leibniz invented calculus independently, and Newton’s friends spent a lot of time proving that he was first. He was, but it was Leibniz who thought of writing $d y / d x$ —which caught on. It is the perfect way to suggest the limit of $\Delta y / \Delta x$ : Newton was one of the great scientists of all time, and calculus was one of the great inventions of all time-but the notation must help. You now can write and speak about the derivative. What is needed is a longer list of functions and derivatives.