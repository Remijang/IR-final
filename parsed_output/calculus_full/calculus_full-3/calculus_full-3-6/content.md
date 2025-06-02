# 3.6 Iterations $x _ { n + 1 } = F ( x _ { n } )$

Iteration means repeating the same function. Suppose the function is $F ( x ) =$ cos $x$ : Choose any starting value, say $x _ { 0 } = 1$ : Take its cosine: $x _ { 1 } = \cos x _ { 0 } = . 5 4$ : Then take the cosine of $x _ { 1 }$ . That produces $x _ { 2 } = \mathrm { c o s }$ : $5 4 = . 8 6$ : The iteration is $x _ { n + 1 } = \cos x _ { n }$ . I am in radian mode on a calculator, pressing “cos” each time. The early numbers are not important, what is important is the output after 12 or 30 or 100 steps:

$$
x _ { 1 2 } = . 7 5 , x _ { 1 3 } = . 7 3 , x _ { 1 4 } = . 7 4 , \ldots , x _ { 2 9 } = . 7 3 9 1 , x _ { 3 0 } = . 7 3 9 1 .
$$

The goal is to explain why the $x$ ’s approach $x ^ { * } = . 7 3 9 0 8 5$ : : : : Every starting value $x _ { 0 }$ leads to this same number $x ^ { * }$ : What is special about :7391 ?

Note on iterations Do $x _ { 1 } = \cos x _ { 0 }$ , and $x _ { 2 } = \cos x _ { 1 }$ , mean that $x _ { 2 } = \cos ^ { 2 } x _ { 0 } \mathrm { ? }$ Absolutely not! Iteration creates a new and different function $\cos ( \cos x )$ : It uses the cos button, not the squaring button. The third step creates $F ( F ( F ( x ) ) )$ : As soon as you can, iterate with $\begin{array} { r } { { \dot { x } } _ { n + 1 } = { \frac { 1 } { 2 } } \cos x _ { n } } \end{array}$ : What limit do the $x$ ’s approach ? Is it $\textstyle { \frac { 1 } { 2 } } ( . 7 9 3 1 )$ ?

Let me slow down to understand these questions. The central idea is expressed by the equation $x _ { n + 1 } = F ( x _ { n } )$ . Substituting $x _ { 0 }$ into $F$ gives $x _ { 1 }$ : This output $x _ { 1 }$ is the input that leads to $x _ { 2 }$ : In its turn, $x _ { 2 }$ is the input and out comes $x _ { 3 } = F ( x _ { 2 } )$ : This is iteration, and it produces the sequence $x _ { 0 } , x _ { 1 } , x _ { 2 } , \ldots$

The $x$ ’s may approach a limit $x ^ { * }$ , depending on the function $F$ : Sometimes $x ^ { * }$ also depends on the starting value $x _ { 0 }$ : Sometimes there is $n o$ limit. Look at a second example, which does not need a calculator.

EXAMPLE 2 $\begin{array} { r } { x _ { n + 1 } = F ( x _ { n } ) = \frac { 1 } { 2 } x _ { n } + 4 } \end{array}$ : Starting from $x _ { 0 } = 0$ the sequence is

$$
x _ { 1 } = { \textstyle { \frac { 1 } { 2 } } } \cdot 0 + 4 = 4 , \ x _ { 2 } = { \textstyle { \frac { 1 } { 2 } } } \cdot 4 + 4 = 6 , \ x _ { 3 } = { \textstyle { \frac { 1 } { 2 } } } \cdot 6 + 4 = 7 , \ x _ { 4 } = { \textstyle { \frac { 1 } { 2 } } } \cdot 7 + 4 = 7 { \textstyle { \frac { 1 } { 2 } } } , \ \dots .
$$

Those numbers $0 , 4 , 6 , 7 , 7 { \scriptstyle { \frac { 1 } { 2 } } } ,$ : : : seem to be approaching $x ^ { * } = 8$ : A computer would convince us. So will mathematics, when we see what is special about 8:

8 is the “steady state” where input equals output: $8 = F ( 8 )$ : It is the fixed point. If we start at $x _ { 0 } = 8$ , the sequence is 8; 8; 8; : : :: When we start at $x _ { 0 } = 1 2$ , the sequence goes back toward 8:

$$
x _ { 1 } = { \textstyle { \frac { 1 } { 2 } } } \cdot 1 2 + 4 = 1 0 , \quad x _ { 2 } = { \textstyle { \frac { 1 } { 2 } } } \cdot 1 0 + 4 = 9 , \quad x _ { 3 } = { \textstyle { \frac { 1 } { 2 } } } \cdot 9 + 4 = 8 . 5 , \quad \ldots .
$$

Equation for limit: If the iterations $x _ { n + 1 } = F ( x _ { n } )$ converge to $x ^ { * }$ , then $x ^ { * } = F ( x ^ { * } )$ .

To repeat: 8 is special because it equals ${ \frac { 1 } { 2 } } \cdot 8 + 4$ : The number :7391 : : : is special because it equals cos :7391 : : :: The graphs of $y = x$ and $y = F ( x )$ intersect at $x ^ { * }$ . To explain why the $x$ ’s converge (or why they don’t) is the job of calculus.

EXAMPLE 3 $x _ { n + 1 } = x _ { n } ^ { 2 }$ has two fixed points: $0 = 0 ^ { 2 }$ 8and $1 = 1 ^ { 2 }$ : Here $F ( x ) = x ^ { 2 }$ :

Starting from $\begin{array} { r } { x _ { 0 } = \frac { 1 } { 2 } } \end{array}$ the sequence ${ \frac { 1 } { 4 } } , { \frac { 1 } { 1 6 } } , { \frac { 1 } { 2 5 6 } }$ ; : : : goes quickly to $x ^ { * } = 0$ : The only approaches to $x ^ { * } = 1$ are from $x _ { 0 } = 1$ (of course) and from $x _ { 0 } = - 1$ : Starting from $x _ { 0 } = 2$ we get 4; 16; 256; : : : and the sequence diverges to $+ \infty$ :

Each limit $x ^ { * }$ has a “basin of attraction.” The basin contains all starting points $x _ { 0 }$ that lead to $x ^ { * }$ : ForExamples 1 and 2, every $x _ { 0 }$ led to:7391 and 8: Thebasins were the whole line (that is still to be proved). Example 3 had three basins—the interval $- 1 < x _ { 0 } < 1$ , the two points $x _ { 0 } = \pm 1$ , and all the rest. The outer basin $\left. x _ { 0 } \right. > 1$ led to $\pm \infty$ : I challenge you to find the limits and the basins of attraction (by calculator) for $F ( x ) = x - \tan { x }$ :

In Example 3, $x ^ { * } = 0$ is attracting. Points near $x ^ { * }$ move toward $x ^ { * }$ : The fixed point $x ^ { * } = 1$ is repelling. Points near 1 move away. We now find the rule that decides whether $x ^ { * }$ is attracting or repelling. The key is the slope $d F / d x$ at $x ^ { * }$ .

First I will give a calculus proof. Then comes a picture of convergence, by “cobwebs.” Both methods throw light on this crucial testforattr1action: $| d F / d x | < 1$ :

First proof: Subtract $x ^ { * } = F ( x ^ { * } )$ from $x _ { n + 1 } = F ( x _ { n } )$ : The difference $x _ { n + 1 } - x ^ { * }$ is the same as $F ( x _ { n } ) - F ( x ^ { * } )$ : This is $\Delta F$ : The basic idea of calculus is that $\Delta F$ is close to $F ^ { \prime } \Delta x$ :

$$
x _ { n + 1 } - x ^ { * } = F ( x _ { n } ) - F ( x ^ { * } ) \approx F ^ { \prime } ( x ^ { * } ) ( x _ { n } - x ^ { * } ) .
$$

The “err|or” $x _ { n } - x ^ { * }$ is multiplied by the slope $d F / d x$ : The next error $x _ { n + 1 } - x ^ { * }$ is smaller or larger, based on $\left| F ^ { \prime } \right| < 1$ or $\left| F ^ { \prime } \right| > 1$ at $x ^ { * }$ : Every step multiplies approximately by $F ^ { \prime } ( x ^ { * } )$ : Its size controls the speed of convergence.

In Example 1, $F ( x )$ is cos $x$ and $F ^ { \prime } ( x )$ is $- \sin x$ : There is attraction to :7391 because $\left| \sin x ^ { * } \right| < 1$ : In Example 2, $F$ is ${ \frac { 1 } { 2 } } x + 4$ and $F ^ { \prime }$ is $\frac { 1 } { 2 }$ : There is attraction to 8: In Example 3, $F$ is $x ^ { 2 }$ and $F ^ { \prime }$ is $2 x$ : There is superattraction to $x ^ { * } = 0$ (where $F ^ { \prime } { = } 0$ ). There is repulsion from $x ^ { * } = 1$ (where $F ^ { \prime } { = } 2$ ).

I admit one major difficulty. The approximation in equation (1) only holds near $x ^ { * }$ : If $x _ { 0 }$ is far away, does the sequence still approach $x ^ { * }$ ? When there are several attracting points, which $x ^ { * }$ do we reach ? This section starts with good iterations, which solve the equation $x ^ { * } = F ( x ^ { * } )$ or $f ( x ) = 0$ : At the end we discover Newton’s method. The next section produces crazy but wonderful iterations, not converging and not blowing up. They lead to “fractals” and “Cantor sets” and “chaos.”

The mathematics of iterations is not finished. It may never be finished, but we are converging on the answers. Please choose a function and join in.

# THE GRAPH OF AN ITERATION: COBWEBS

The iteration $x _ { n + 1 } = F ( x _ { n } )$ involves two graphs at the same time. One is the graph of $y = F ( x )$ : The other is the graph of $y = x$ (the $4 5 ^ { \circ }$ line). The iteration jumps back and forth between these graphs. It is a very convenient way tosee the whole process.

Example 1 was $x _ { n + 1 } = \cos x _ { n }$ : Figure 3.19 shows the graph of cos $x$ and the “cobweb.” Starting at $( x _ { 0 } , x _ { 0 } )$ on the $4 5 ^ { \circ }$ line, the rule is based on $x _ { 1 } = F ( x _ { 0 } )$ :

These steps are repeated forever. From $x _ { 1 }$ go up to the curve at $F ( x _ { 1 } )$ : That height is $x _ { 2 }$ : Now cross to the $4 5 ^ { \circ }$ line at $( x _ { 2 } , x _ { 2 } )$ : The iterations are aiming for $( x ^ { * } , x ^ { * } ) =$ .:7391; :7391/: This is the crossing point of the two graphs $y = F ( x )$ and $y = x$ :

Example 2 was $\textstyle x _ { n + 1 } = { \frac { 1 } { 2 } } x _ { n } + 4$ : Both graphs are straight lines. The cobweb is one-sided, from $( 0 , 0 )$ to $( 0 , 4 )$ to $( 4 , 4 )$ to $( 4 , 6 )$ t1o $( 6 , 6 )$ : Notice how $y$ changes (vertical line) and then $x$ changes (horizontal line).The slope of $F ( x )$ is $\frac { 1 } { 2 }$ , so the distance to 8 is multiplied by $\frac { 1 } { 2 }$ at ev¡ery step.

Example 3 was $x _ { n + 1 } = x _ { n } ^ { 2 }$ : The graph of $y = x ^ { 2 }$ crosses the $4 5 ^ { \circ }$ line at two fixed points: $0 ^ { 2 } = 0$ and $1 ^ { 2 } = 1$ : Figure 3.20a starts the iteration close to 1, but it quickly goes away. This fixed point is repelling because $F ^ { \prime } ( 1 ) = 2$ : Distance from $x ^ { * } = 1$ is doubled (at the start). One path moves down to $x ^ { * } = 0 .$ —which is superattractive because $F ^ { \prime } = 0$ : The path from $x _ { 0 } > 1$ diverges to infinity.

EXAMPLE 4 $F ( x )$ has two attracting points $x ^ { * }$ (a repelling $x ^ { * }$ is always between).

Figure 3.20b shows two crossings with slope zero. The iterations and cobwebs converge quickly. In between, the graph of $F ( x )$ must cross the $4 5 ^ { \circ }$ IliNneEf:romPbLelOowT. That requires a slope greater than one. Cobwebs diverge from this unstable point, which separates the basins of attraction. The fixed point $x = \pi$ is in a basin by itself!

Note 1 To draw cobwebs on a calculator, graph $y = F ( x )$ on top of $y = x$ : On a CasioY, one way is to pYlot $( x _ { 0 } , x _ { 0 } )$ and give the command ${ \sf X } , { \sf Y }$ followed by . Now move the cursor vertically to $y = F ( x )$ and press . Then move horizontally to $y = x$ and press . Continue. Each step draws aPlringe.m

For the TI-81 (and also the Casio) a short program produces a cobweb. Store $F ( x )$ in th1e ${ \boldsymbol { \mathsf { Y } } } =$ function slot $\textsf { Y } _ { 1 }$ . Set the range (square1window or autoscaling). Run the p:rLogirnaem(aSnd,aTn,sTw,erTt)he p:roTmÑpXt wit:h $x _ { 0 }$ :u

PrgmC:COBWEB :Disp \*INITIAL Xg"' :Input X :All-off $= Y 1 - 0 n : 1 1 \times 1 1  Y 4$ :Lbl 1 : $x  s$ ： $\yen 123,456$ :Line (s,S,s,t) :Line(S,T,T,T): $T \to { \mathsf { X } }$ : Pause :Goto 1

Note 2 The $x$ ’s approach $x ^ { * }$ from one side when $0 < d F / d x < 1$ :

Note 3 A basin of attraction can include faraway $x _ { 0 }$ ’s (basins can come in infinitely many pieces). This makes the problem interesting. If no fixed points are attracting, see Section 3.7 for “cycles” and “chaos.”

At this point we offer the reader a choice. One possibility is to jump ahead to the next section on “Newton’s Method.” That method is an iteration to solve $f ( x ) = 0$ : The function $F ( x )$ combines $x _ { n }$ and $f ( x _ { n } )$ and $f ^ { \prime } ( x _ { n } )$ into an optimal formula for $x _ { n + 1 }$ : We will see how quickly Newton’s method works (when it works). It is the outstanding algorithm to solve equations, and it is totally built on tangent approximations.

The other possibility is to understand (through calculus) a whole family of iterations. This family depends on a number $c$ , which is at our disposal. The best choice of c produces Newton’s method. I emphasize that iteration is by no means a new and peculiar idea. It is a fundamental technique in scientific computing.

We start by recognizing that there are many ways to reach $f ( x ^ { * } ) = 0$ : (I write $x ^ { * }$ for the solution.) A good algorithm may switch to Newton as it gets close. The iterations use $f ( x _ { n } )$ to decide on the next point $x _ { n + 1 }$ :

$$
x _ { n + 1 } = F ( x _ { n } ) = x _ { n } - c f ( x _ { n } ) .
$$

Notice how $F ( x )$ is constructed from $f ( x )$ —they are different! We move $f$ to the right side and multiply by a “preconditioner” $c$ : The choice of $c$ (or $c _ { n }$ , if it changes from step to step) is absolutely critical. The starting guess $x _ { 0 }$ is also important—but its accuracy is not always under our control.

Suppose the $x _ { n }$ converge to $x ^ { * }$ : TheÑn the limit of equatioÑn (2) is

$$
x ^ { * } = x ^ { * } - c f ( x ^ { * } ) .
$$

That gives $f ( x ^ { * } ) = 0$ : If the $x _ { n }$ ’s have a limit, it solves the right equation. It is a fixed point of $F$ (we can assume $c _ { n } \to c \neq 0$ and $f ( x _ { n } ) \to f ( x ^ { * } ) )$ . There are two key questions, and both of them are answered by the slope $F ^ { \prime } ( x ^ { * } )$ :

1. How quickly does $x _ { n }$ approach $x ^ { * }$ (or do the $x _ { n }$ diverge) ?   
2. What is a good choice of $c$ (or $c _ { n }$ ) ?

EXAMPLE 5 $f ( x ) = a x - b$ is zero at $x ^ { * } = b / a$ : The iteration $x _ { n + 1 } =$ $x _ { n } - c ( a x _ { n } - b )$ intends to find $b / a$ without actually dividing. (Early computers

could not divide; they used iteration.)Subtracting $x ^ { * }$ from both sides leaves an equation for the error:

$$
x _ { n + 1 } - x ^ { * } = x _ { n } - x ^ { * } - c ( a x _ { n } - b ) .
$$

Replace| $b$ |by $a x ^ { * }$ : The right side is $( 1 - c a ) ( x _ { n } - x ^ { * } )$ : This “error equation” is

$$
( \operatorname { e r r o r } ) _ { n + 1 } = ( 1 - c a ) ( \operatorname { e r r o r } ) _ { n } .
$$

At every step the error is multiplied by $( 1 - c a )$ , which is $F ^ { \prime }$ : The errorgoes to zero if $\left| F ^ { \prime } \right|$ is less than 1. The absolute value $| 1 - c a |$ decides everything:

$$
x _ { n } ~ c o n v e r g e s ~ t o ~ x ^ { * } ~ i f a n d o n l y ~ i f - 1 < 1 - c a < 1 .
$$

The perfect choice (if we knew it) is $c = 1 / a$ , which turns the multiplier $1 - c a$ into zero. Then one iteration gives the exact answer: $x _ { 1 } = x _ { 0 } - ( 1 / a ) ( a x _ { 0 } - b ) = b / a$ : That is the horizontal line in Figure 3.21a, converging in one step. But look at the other lines.

This example did not need calculus. Linear equations never do. The key idea is that close to $x ^ { * }$ the nonlinear equation $f ( x ) = 0$ is nearly linear. We apply the tangent approximation. You are seeing how calculus is used, in a problem that doesn’t start by asking for a derivative.

# THE BEST CHOICE OF $\scriptstyle { c }$

The immediate goal is to study the errors $x _ { n } - x ^ { * }$ : They go quickly to zero, if the multiplier is small. To understand $x _ { n + 1 } = x _ { n } - c f ( x _ { n } )$ , subtract the equation $x ^ { * } = x ^ { * } - c f ( x ^ { * } )$ :

$$
x _ { n + 1 } - x ^ { * } = x _ { n } - x ^ { * } - c ( f ( x _ { n } ) - f ( x ^ { * } ) ) .
$$

Now calculus enters. When you see a difference of $f$ ’s think of $d f / d x$ : Replace $f ( x _ { n } ) - f ( x ^ { * } )$ by $A ( x _ { n } - x ^ { * } )$ , where $A$ stands for the slope $d f / d x$ at $x ^ { * }$ :

$$
x _ { n + 1 } - x ^ { * } \approx ( 1 - c A ) ( x _ { n } - x ^ { * } ) .
$$

This is the error equation. The new error at step $n + 1$ is approximate|ly  t|h e old error multiplied by $m = 1 - c A$ : This corresponds to $m = 1 - c a$ in the linear example. We keep returning to the basic test $| m | = | F ^ { \prime } ( x ^ { * } ) | < 1$ :

3K Starting near $x ^ { * }$ ; the errors $x _ { n } - x ^ { * }$ go to zero if multiplier has $| m | < 1$ : The perfect choice is $c = 1 / A = 1 / f ^ { \prime } ( x ^ { * } )$ : Then $m = 1 - c A = 0$ :

There is only one difficulty: We don’t know $x ^ { * }$ . Therefore we don’t know the perfect $c$ : It depends on the slope $A = f ^ { \prime } ( x ^ { * } )$ at the unknown solution. However we can come close, by using the slope at $x _ { n }$ :

$$
\hom o s e c _ { n } = 1 / f ^ { \prime } ( x _ { n } ) . { T h e n } ~ x _ { n + 1 } = x _ { n } - f ( x _ { n } ) / f ^ { \prime } ( x _ { n } ) = F ( x _ { n } ) .
$$

This is Newton’s method. The multiplier $m = 1 - c A$ is as near to zero as we can make it. By building $d f / d x$ into $F ( x )$ , Newton speeded up the convergence of the iteration.

EXAMPLE 6 Solve $f ( x ) = 2 x - \cos x = 0$ with different iterations (1different $c$ ’s).

The line $y = 2 x$ crosses the cosine curve som1ewhere near $\begin{array} { r } { x = \frac { 1 } { 2 } } \end{array}$ 1: The intersection point where $2 x ^ { * } = \cos x ^ { * }$ has no simple formula. We start from $\begin{array} { r } { { \dot { x } } _ { 0 } = \frac { 1 } { 2 } } \end{array}$ and iterate $x _ { n + 1 } = x _ { n } - c ( 2 x _ { n } - \cos x _ { n } )$ with three different choices of $c$ :

Take $c = 1$ or $c = 1 / f ^ { \prime } ( x _ { 0 } )$ or update $c$ by Newton’s rule $c _ { n } = 1 / f ^ { \prime } ( x _ { n } )$ :

$$
\begin{array} { l c l c l } { { x _ { 0 } = . 5 0 } } & { { \quad c = 1 } } & { { \quad c = 1 / f ^ { \prime } ( x _ { 0 } ) } } & { { \quad c _ { n } = 1 / f ^ { \prime } ( x _ { n } ) } } \\ { { x _ { 1 } = } } & { { \quad . 3 8 } } & { { \quad . 4 5 0 6 3 } } & { { \quad . 4 5 0 6 2 6 6 9 } } \\ { { x _ { 2 } = } } & { { \quad . 5 5 } } & { { \quad . 4 5 0 1 9 } } & { { \quad . 4 5 0 1 8 3 6 5 } } \\ { { x _ { 3 } = } } & { { \quad . 3 0 } } & { { \quad . 4 5 0 1 8 } } & { { \quad . 4 5 0 1 8 3 6 1 . . . } } \end{array}
$$

The column with $c = 1$ is diverging (repelled from $x ^ { * }$ ). The second column shows convergence (attracted to $x ^ { * }$ ). The third column (Newton’s method) approaches $x ^ { * }$ so quickly that :4501836 and seven more digits are exact for $x _ { 3 }$ :

How does this convergence match the prediction ? Note that $f ^ { \prime } ( x ) = 2 + \sin { x }$ so $A = 2 . 4 3 5$ : Look to see whether the actual errors $x _ { n } - x ^ { * }$ , going down each column, are multiplied by the predicted $m$ below that column:

$$
{ \begin{array} { r l r l r l } & { } & & { c = 1 } & & { c = 1 / ( 2 + \sin { \frac { 1 } { 2 } } ) } & & { c _ { n } = 1 / ( 2 + \sin { x _ { n } } ) } \\ & { } & & { 0 . 0 5 } & & { 4 . 9 8 \cdot 1 0 ^ { - 2 } } & & { 4 . 9 8 \cdot 1 0 ^ { - 2 } } \\ & { } & { x _ { 1 } - x ^ { * } = } & & { - 0 . 0 7 } & & { 4 . 4 3 \cdot 1 0 ^ { - 4 } } & & { 4 . 4 3 \cdot 1 0 ^ { - 4 } } \\ & { } & { x _ { 2 } - x ^ { * } = } & & { 0 . 1 0 } & & { 7 . 8 8 \cdot 1 0 ^ { - 6 } } & & { 3 . 6 3 \cdot 1 0 ^ { - 8 } } \\ & { } & { x _ { 3 } - x ^ { * } = } & & { - 0 . 1 5 } & & { 1 . 4 1 \cdot 1 0 ^ { - 7 } } & & { 2 . 7 8 \cdot 1 0 ^ { - 1 6 } } \\ & { } & & { m = - 1 . 4 } & & { m = . 0 1 8 } & & { m  0 \ { \mathrm { ( N e w t o n ) } } } \end{array} }
$$

The first column shows a multiplier below $^ { - 1 }$ : The errors grow at every step. Because $m$ is negative the errors change sign—the cobweb goes outward.

The second column shows convergence with $m = . 0 1 8$ : It takes one genuine Newton step, then $c$ is fixed. Af¤ter $n$ steps the error is closely proportional to $m ^ { n } = ( . 0 1 8 ) ^ { n }$ — that is “linear convergence” with a good multiplier.

The third column shows the “quadratic convergence” of Newton’s method. Multiplying the error by $m$ is more attractive than ever, because $m \to 0$ : In fact $m$ itself is proportional to the error, so at each step the error is squared. Problem 3:8:31 will show that $( \mathrm { e r r o r } ) _ { n + 1 } \leqslant M ( \mathrm { e r r o r } ) _ { n } ^ { 2 }$ : This squaring carries us from $1 0 ^ { - 2 }$ to $1 0 ^ { - 4 }$ to $1 0 ^ { - 8 }$ to “machine $\varepsilon ^ { \prime \prime }$ in three steps. The number of correct digits is doubled at every step as Newton converges.

Note 1 The choice $c = 1$ produces $x _ { n + 1 } = x _ { n } - f ( x _ { n } )$ : This is “successive substitution.” The equation $f ( x ) = 0$ is rewritten as $x = x - f ( x )$ , and |ea ch $x _ { n }$ is substituted back to produce $x _ { n + 1 }$ : Iteration with $c = 1$ does not always fail!

Note 2 Newton’s method is successive substitution for $f / f ^ { \prime }$ , not $f .$ Then $m \approx 0$ :

Note 3 Edwards and Penn1ey happened to choose the same example $2 x = \cos x$ : But they cleverly wrote it as $\begin{array} { r } { { \dot { x _ { n + 1 } } } = \frac { 1 } { 2 } \cos x _ { n } } \end{array}$ , which has $\begin{array} { r } { | F ^ { \prime } | = | \frac { 1 } { 2 } \mathrm { { s i n } } x | < 1 } \end{array}$ : This iteration fits into our family with $\begin{array} { r } { c = \frac { 1 } { 2 } } \end{array}$ , and it succeeds. We asked earlier if its limit is $\scriptstyle { \frac { 1 } { 2 } } ( . 7 3 9 1 ) . N o$ , it is $x ^ { * } = . 4 5 0 \ldots$

Note 4 The choice $c = 1 / f ^ { \prime } ( x _ { 0 } )$ is “modified Newton.” After one step of Newton’s method, $c$ is fixed. The steps are quicker, because they don’t require a new $f ^ { \prime } ( x _ { n } )$ : But we need more steps. Millions of dollars are spent on Newton’s method, so speed is important. In all its forms, $f ( x ) = 0$ is the central problem of computing.