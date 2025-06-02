# 0.5 Graphs and Graphing Calculators

This book started with the sentence “Calculus is about functions.” When these functions are given by formulas like $y = x + x ^ { 2 }$ , we now know a formula for the slope (and even the slope of the slope). When we only have a rough graph of the function, we can’t expect more than a rough graph of the slope. But graphs are very valuable in applications of calculus!

From a graph of $y ( x )$ , this section extracts the basic information about the growth rate (the slope) and the minimum=maximum and the bending (and area too). A big part of that information is contained in a plus or minus sign. Is $y ( x )$ increasing ? Is its slope increasing ? Is the area under its graph increasing ? In each case some number is greater than zero. The three numbers are $d y / d x$ and $d ^ { 2 } y / d x ^ { 2 }$ and $y ( x )$ itself.

When one of those numbers is exactly zero we always have a special situation. It is a good thing that mathematics invented zero, we need it.

This section is organized by two themes:

(1) Graphs that are drawn without a formula for $y ( x )$ . From that graph you can draw other graphs—the slope $d y / d x$ , the second derivative $d ^ { 2 } y / d x ^ { 2 }$ , the area $A ( x )$ under the graph. You can also identify where those functions are positive or negative—and especially the points where $d y / d x$ or $d ^ { 2 } y / d x ^ { 2 }$ or $y ( x )$ is zero.   
(2) Graphs that are drawn by a calculator or computer. Now there is a formula for $y ( x )$ . The display allows us to guess rules for derivatives:

# Chain Rule Inverse Rule l’Hôpital’s Rule

These rules come into later chapters of the book. They are also explained in Highlights of Calculus, the video lectures that are available to everyone. One specific goal is to see how the derivative of $2 ^ { x }$ is proportional to $2 ^ { x }$ .

This section was much improved by ideas that were offered by Benjamin Goldstein.

# GRAPH WITHOUT FORMULAS

# 0 Highlights of Calculus

1. Suppose this is the graph of some function $y ( x )$

a. At what value(s) of $x$ does $y ( x )$ have a local minimum ? b. At what value(s) of $x$ does $y ( x )$ have a local maximum ? c. At what value(s) of $x$ does $y ( x )$ have an inflection point ? (Estimate.)

2. Let’s change the problem. Suppose this is the graph of $d y / d x$ , the derivative of $y ( x )$ . Answer the following questions about $y ( x )$ , the original function.

a. At what value(s) of $x$ does $y ( x )$ have a local minimum ? b. At what value(s) of $x$ does $y ( x )$ have a local maximum ? c. At what value(s) of $x$ does $y ( x )$ have an inflection point ?

3. One more variation. Suppose this is the graph of the second derivative $d ^ { 2 } y / d x ^ { 2 }$ (slope of the slope). If any of these questions can’t be answered, explain why.

a. At what value(s) of $x$ does $y ( x )$ have a local minimum ? b. At what value(s) of $x$ does $y ( x )$ have a local maximum ? c. At what value(s) of $x$ does $y ( x )$ have an inflection point ?

4. Answer the same 9 questions for this second graph

5. The following table shows the velocity of a car at selected times.

a. Was there any time $t$ when the car was moving with acceleration $d ^ { 2 } y / d t ^ { 2 } = 0 ?$ Justify your answer.

b. If $y ( t )$ represents the car’s position as a function of time, was there ever a time when $d ^ { 3 } y / d t ^ { 3 } = 0 ?$ Justify your answer. The third derivative is sometimes referred to as ‘jerk’ because it indicates the jerkiness of the motion. This is important to roller-coaster designers. c. What assumptions have you made about $y ( t )$ and (more importantly) $d y / d t$ in your answers to parts (a) and (b) ? Are the assumptions reasonable ?

# 0.5 Graphs and Graphing Calculators

THE CHAIN RULE ON A CALCULATOR

a. On your calculator, graph $\mathrm { Y } _ { 1 } = \sin \left( \mathrm { X } \right)$ and its slope ${ \boldsymbol { \mathrm { Y } } } _ { 2 } = { \mathrm { n D e r i v } } ( { \boldsymbol { \mathrm { Y } } } _ { 1 } , { \boldsymbol { \mathrm { X } } } , { \boldsymbol { \mathrm { X } } } )$ : Make sure you are in radian mode, and select the trigonometric viewing window.

1. What function does $\mathrm { Y } _ { 2 }$ appear to be ? 2. Change ${ \mathrm { Y } } _ { 1 }$ to $\mathrm { Y } _ { 1 } = \sin \left( 2 \mathrm { X } \right)$ : Now what function does $\mathrm { Y } _ { 2 }$ appear to be ? Check your guess by graphing the true derivative. 3. Finally, change ${ \mathrm { Y } } _ { 1 }$ to $\mathrm { Y } _ { 1 } = \sin \left( 3 \mathrm { X } \right)$ : What does $\mathbf { Y } _ { 2 }$ appear to be this time ? 4. Conjecture: If $k$ is some constant, then the derivative of $\sin \left( k x \right)$ is   
b. Those functions are chains (also called compositions). They can be written in the form $\mathbf { Y } = f ( g ( x ) )$ : For $\sin \left( k x \right)$ the outer?function is $f ( x ) = -$ and the inner function is $g ( x ) = \_$   
c. So far the inner function $g ( x )$ has been linear, but it doesn’t have to be. Let $Y = \sin \left( { \sqrt { x } } \right)$ : Conjecture: ${ \frac { d Y } { d x } } = { \mathrm { ~ - ~ } } { \mathrm { ~ w h e n ~ } } g ( x ) = { \sqrt { x } } .$ Check your conjecture by graphing $Y$ and comparing to the graph of the numerical derivative.   
d. Now we generalize. Suppose $g ( x )$ is any function. If $y = \sin { ( g ( x ) ) }$ ; then $d y / d x = -$   
e. There is nothing magical about the sine function. Whenever we have a composition of an outer and an inner function, the chain rule applies. Predict the following derivatives and check by graphing the numerical derivative on your calculator.

$$
\begin{array} { c c } { { y = ( 2 x + 4 ) ^ { 3 } ; d y / d x = } } & { { \qquad 2 . \ y = \cos ^ { 2 } x = ( \cos x ) ^ { 2 } ; d y / d x = } } \\ { { y = \cos ( x ^ { 2 } ) ; d y / d x = } } & { { \qquad 4 . \ y = [ \sin ( x ^ { 2 } + 1 ) ] ^ { 3 } ; d y / d x = } } \end{array}
$$

# COMPUTING IN CALCULUS

Software is available for calculus courses—a lot of it. The packages keep getting better. Which program to use (if any) depends on cost and convenience and purpose. How to use it is a much harder question. These pages identify some of the goals. Our aim is to support, with examples, the effort to use computing to help learning.

For calculus, the greatest advantage of the computer is to offer graphics. You see the function, not just the formula. As you watch, $f ( x )$ reaches a maximum or a minimum or zero. A separate graph shows its derivative. Those statements are not $100 \%$ true, as everybody learns right away—as soon as a few functions are typed in. But the power to see this subject is enormous, because it is adjustable. If we don’t like the picture we change to a new viewing window.

This is computer-based graphics. It combines numerical computation with graphical computation. You get pictures as well as numbers—a powerful combination. The computer offers the experience of actually working with a function. The domain and range are not just abstract ideas. You choose them. May I give a few examples.

EXAMPLE 1 Certainly $x ^ { 3 }$ equals $3 ^ { x }$ when $\scriptstyle x = 3 . D o$ those graphs ever meet again ? At this point we don’t know the full meaning of $3 ^ { x }$ , except when $x$ is a nice number. (Neither does the computer.) Checking at $\scriptstyle x = 2$ and 4, the function $x ^ { 3 }$ is smaller both times: $2 ^ { 3 }$ is below $3 ^ { 2 }$ and $4 ^ { 3 } = 6 4$ is below $3 ^ { 4 } { = } 8 1$ . If $x ^ { 3 }$ is always less than $3 ^ { x }$ we ought to know—these are among the basic functions of mathematics.

The computer will answer numerically or graphically. At our command, it solves $x ^ { 3 } = 3 ^ { x }$ . At another command, it plots both functions—this shows more. The screen proves a point of logic (or mathematics) that escaped us. If the graphs cross once, they must cross again—because $3 ^ { x }$ is higher at 2 and 4. A crossing point near 2:5 is seen by zooming in. I am less interested in the exact number than its position—it comes before $x = 3$ rather than after.

A few conclusions from such a basic example:

1. A supercomputer is not necessary.   
2. High-level programming is not necessary.   
3. We can do mathematics without completely understanding it.

The third point doesn’t sound so good.Write it differently:We can learn mathematics while doing it. The hardest part of teaching calculus is to turn it from a spectator sport into a workout. The computer makes that possible.

EXAMPLE 2 (mental computer) Compare $x ^ { 2 }$ with $2 ^ { x }$ . The functions meet at $x = 2$ . Where do they meet again ? Is it before or after 2 ?

That is mental computing because the answer happens to be a whole number (4). Now we are on a different track. Does an accident like $2 ^ { 4 } { = } 4 ^ { 2 }$ ever happen again ? Can the machine tell us about integers ? Perhaps it can plot the solutions of ${ x ^ { \bar { b } } } { = } b ^ { x }$ . I asked Mathematica for a formula, hoping to discover $x$ as a function of $b$ —but the program just gave back the equation. For once the machine typed HELP instead of the user.

Well, mathematics is not helpless. I am proud of calculus. There is a new exercise at the end of Section 6:4, to show that we never see whole numbers again.

EXAMPLE 3 Find the number $b$ for which $x ^ { b } = b ^ { x }$ has only one solution (at $\scriptstyle x = b$ ).

When $b$ is 3, the second solution is below 3. When $b$ is 2, the second solution .4/ is above 2. If we move $b$ from 2 to 3, there must be a special “double point”—where the graphs barely touch but don’t cross. For that particular $b$ —and only for that one value—the curve $x ^ { b }$ never goes above $b ^ { x }$ .

This special point $b$ can be found with computer-based graphics. In many ways it is the “center point of calculus.” Since the curves touch but don’t cross, they are tangent. They have the same slope at the double point. Calculus was created to work with slopes, and we already know the slope of $x ^ { 2 }$ . Soon comes $x ^ { b }$ . Eventually we discover the slope of $b ^ { x }$ , and identify the most important number in calculus.

The point is that this number can be discovered first by experiment.

EXAMPLE 4 Graph $y ( x ) = e ^ { x } - x ^ { e }$ . Locate its minimum. Zoom in near $x = e$ :

From the derivatives of $e ^ { x }$ and $x ^ { e }$ ; show that $d y / d x = 0$ at $x = e$ : If you try, you can also find the next derivative $d ^ { 2 } y / d x ^ { 2 }$ : Can you see why $d ^ { 2 } y / d x ^ { 2 } > 0$ at $x = e$ ?

# 0.5 Graphs and Graphing Calculators

The next example was proposed by Don Small. Solve $x ^ { 4 } - 1 1 x ^ { 3 } + 5 x - 2 = 0$ . The first tool is algebra—try to factor the polynomial. That succeeds for quadratics, and then gets extremely hard. Even if the computer can do algebra better than we can, factoring is seldom the way to go. In reality we have two good choices:

1. (Mathematics) Use the derivative. Solve by Newton’s method.   
2. (Graphics) Plot the function and zoom in.

Both will be done by the computer. Both have potential problems! Newton’s method is fast, but that means it can fail fast. (It is usually terrific.) Plotting the graph is also fast—but solutions can be outside the viewing window. This particular function is zero only once, in the standar¤d wi¤ndow from¤ $- 1 0$ to 10. The graph seems to be leaving zero, but mathematics again predicts a second crossing point. So we zoom out before we zoom in.

The use of the zoom is the best part of graphing. Not only do we choose the domain and range, we change them. The viewing window is controlled by four numbers. They can be the limits $A \leqslant x \leqslant B$ and $C \leqslant y \leqslant D$ . They can be the coordinates of two opposite corners: $( A , C )$ and $( B , D )$ . They can be the center position $( a , b )$ and the scale factors $c$ and $d$ . Clicking on opposite corners of the zoom box is the fastest way, unless the center is unchanged and we only need to give scale factors. (Even faster: Use the default factors.) Section 3:4 discusses the centering transform and zoom transform—a change of picture on the screen and a change of variable within the function.

EXAMPLE 5 Find all real solutions to $x ^ { 4 } - 1 1 x ^ { 3 } + 5 x - 2 = 0$ :

EXAMPLE 6 Zoom out and in on the graphs of $y = \cos { 4 0 x }$ and $y = x \sin ( 1 / x )$ .   
Describe what you see.

EXAMPLE 7 What does $y = ( \tan x - \sin x ) / x ^ { 3 }$ approach at $\scriptstyle x = 0 ?$ For small $x$ the machine eventually can’t separate tan $x$ from $\sin x$ . It may give $y = 0$ . Can you get close enough to see the limit of $y$ as $x \to 0 \ ?$

# SYMBOLIC COMPUTATION

In symbolic computation, answers can be formulas as well as numbers and graphs. The derivative of $y = x ^ { 2 }$ is seen as $^ { 6 6 } 2 x$ .” The derivative of sin t is “cos t.” The slope of $b ^ { x }$ is known to the program. The computer does more than substitute numbers into formulas—it operates directly on the formulas. We need to think where this fits with learning calculus.

In a way, symbolic computing is close to what we ourselves do. Maybe too close— there is some danger that symbolic manipulation is all we do. With a higher-level language and enough power, a computer can print the derivative of $\sin ( x ^ { 2 } )$ . So why learn the chain rule ? Because mathematics goes deeper than “algebra with formulas.” We deal with ideas.

I want to say clearly:Mathematics is not formulas or computations or even proofs, but ideas. The symbols and pictures are the language. The book and the professor and the computer can join in teaching it. The computer should be non-threatening (like this book and your professor)—you can work at your own pace. Your part is to learn by doing.

# 0 Highlights of Calculus

EXAMPLE 8 A computer algebra system quickly finds 100 factorial. This is $1 0 0 ! = ( 1 0 0 ) ( 9 9 ) ( 9 8 ) \dots ( 1 )$ . The number has 158 digits (not written out here). The last 24 digits are zeros. For $1 0 ! { = } 3 6 2 8 8 0 0$ there are seven digits and two zeros. Between 10 and 100, and beyond, are simple questions that need ideas:

1. How many digits (approximately) are in the number $N$ Š ?   
2. How many zeros (exactly) are at the end of N Š ?

For Question 1, the computer shows more than $N$ digits when $N = 1 0 0$ . It will never show more than $N ^ { 2 }$ digits, because none of the $N$ terms can have more than $N$ digits. A much tighter bound would be $2 N$ , but is it true ? Does N Š always have fewer than 2N digits ?

For Question 2, the zeros in 10Š can be explained. One comes from 10, the other from 5 times 2. .10 is also 5 times 2:/ Can you explain the 24 zeros in 100Š ? An idea from the card game blackjack applies here too: Count the fives.

Hard question: How many zeros at the end of 200Š ?

Writing in Calculus May I emphasize the importance of writing ? We totally miss it, when the answer is just a number. A one-page report is harder on instructors as well as students—but much more valuable. You can’t write sentences without being forced to organize ideas—and part of yourself goes into it.

I will propose a writing exercise with options. If you have computer-based graphing, follow through on Examples 1 4 above and report. Without a computer, pick a paragraph from this book that should be clearer and make it clearer. Rewrite it with examples. Identify the key idea at the start, explain it, and come back to express it differently at the end. Ideas are like surfaces—they can be seen many ways.

Mathematics can be learned by talking and writing—it is a human activity. Our goal is not to test but to teach and learn.