# 3.4 Graphs

Reading a graph is like appreciating a painting. Everything is there, but you have to know what to look for. One way to learn is by sketching graphs yourself, and in the past that was almost the only way. Now it is obsolete to spend weeks drawing curves— a computer or graphing calculator does it faster and better. That doesn’t remove the need to appreciate a graph (or a painting), since a curve displays a tremendous amount of information.

This section combines two approaches. One is to study actual machine-produced graphs (especially electrocardiograms). The other is to understand the mathematics of graphs—slope, concavity, asymptotes, shifts, and scaling. We introduce the centering transform and zoom transform. These two approaches are like the rest of calculus, where special derivatives and integrals are done by hand and day-to-day applications are by computer. Both are essential—the machine can do experiments that we could never do. But without the mathematics our instructions miss the point. To create good graphs you have to know a few of them personally.

# READING AN ELECTROCARDIOGRAM (ECG or EKG)

The graphs of an ECG show the electrical potential during a heartbeat. There are twelve graphs—six from leads attached to the chest, and six from leads to the arms and left leg. (It doesn’t hurt, but everybody is nervous. You have to lie still, because contraction of other muscles will mask the reading from the heart.) The graphs record electrical impulses, as the cells depolarize and the heart contracts.

What can I explain in two pages? The graph shows the fundamental pattern of the ECG. Note the P wave, the QRS complex, and the T wave. Those patterns, seen differently in the twelve graphs, tell whether the heart is normal or out of rhythm—or suffering an infarction (a heart attack).

First of all the graphs show the heart rate. The dark vertical lines are by convention $\textstyle { \frac { 1 } { 5 } }$ second apart. The light lines are $\textstyle { \frac { 1 } { 2 5 } }$ second apart. If the heart beats every $\textstyle { \frac { 1 } { 5 } }$ second (one dark line) the rate is 5 beats per second or 300 per minute. That is extreme tachycardia—not compatible with life. The normal rate is between three dark lines per beat $\frac { 3 } { 5 }$ second, or 100 beats per minute) and five dark lines (one second between beats, 60 per minute). A baby has a faster rate, over 100 per minute. In this figure the rate is : A rate below 60 is bradycardia, not in itself dangerous. For a resting athlete that is normal.

Doctors memorize the six rates 300; 150; 100; 75; 60; 50: Those correspond to 1; 2; 3; 4; 5; 6 dark lines between heartbeats. The distance is easiest to measure between spikes (the peaks of the R wave). Many doctors put a printed scale next to the chart. One textbook emphasizes that “Where the next wave falls determines the rate. No mathematical computation is necessary.” But you see where those numbers come from.

The next thing to look for is heart rhythm. The regular rhythm is set by the pacemaker, which produces the P wave. A constant distance between waves is good— and then each beat is examined. When there is a block in the pathway, it shows as a delay in the graph. Sometimes the pacemaker fires irregularly. Figure 3.10 shows sinus arrythmia (fairly normal). The time between peaks is changing. In disease or emergency, there are potential pacemakers in all parts of the heart.

I should have pointed out the main parts. We have four chambers, an atrium ventricle pair on the left and right. The SA node should be the pacemaker. The stimulus spreads from the atria to the ventricles— from the small chambers that “prime the pump” to the powerful chambers that drive blood through the body. The $\mathrm { \bf ~ P }$ wave comes with contraction of the atria. There is a pause of $\scriptstyle { \frac { 1 } { 1 0 } }$ second at the AV node. Then the big QRS wave starts contraction of the ventricles, and the $\mathrm { \Delta T }$ wave is when the ventricles relax. The cells switch back to negative charge and the heart cycle is complete.

The ECG shows when the pacemaker goes wrong. Other pacemakers take over— the AV node will pace at 60=minute: An early firing in the ventricle can give a wide spike in the QRS complex, followed by a long pause. The impulses travel by a slow path. Also the pacemaker can suddenly speed up (paroxysmal tachycardia is 150 250=minute). But the most critical danger is fibrillation.

Figure 3.10b shows a dying heart. The ECG indicates irregular contractions—no normal PQRST sequence at all. What kind of heart would generate such a rhythm? The muscles are quivering or “fibrillating” independently. The pumping action is nearly gone, which means emergency care. The patient needs immediate CPR— someone to do the pumping that the heart can’t do. Cardio-pulmonary resuscitation is a combination of chest pressure and air pressure (hand and mouth) to restart the rhythm. CPR can be done on the street. A hospital applies a defibrillator, which shocks the heart back to life. It depolarizes all the heart cells, so the timing can be reset. Then the charge spreads normally from SA node to atria to AV node to ventricles.

This discussion has not used all twelve graphs to locate the problem. That needs vectors. Look ahead at Section 11.1 for the heart vector, and especially at Section 11.2 for its twelve projections. Those readings distinguish between atrium and ventricle, left and right, forward and back. This information is of vital importance in the event of a heart attack. A “heart attack” is a myocardial infarction (MI).

An MI occurs when part of an artery to the heart is blocked (a coronary occlusion).

An area is without blood supply—therefore without oxygen or glucose. Often the attack is in the thick left ventricle, which needs the most blood. The cells are first ischemic, then injured, and finally infarcted (dead). The classical ECG signals involve those three I’s:

Ischemia: Reduced blood supply, upside-down T wave in the chest leads. Injury: An elevated segment between S and T means a recent attack. Infarction: The Q wave, normally a tiny dip or absent, is as wide as a small square $\frac { 1 } { 2 5 }$ second). It may occupy a third of the entire QRS complex.

The Q wave gives the diagnosis. You can find all three I’s in Figure 3.10c. It is absolutely amazing how much a good graph can do.

# THE MECHANICS OF GRAPHS

From the meaning of graphs we descend to the mechanics. A formula is now given for $f ( x )$ : The problem is to create the graph. It would be too old1-fashion2ed to evaluate $f ( x )$ by hand and draw a curve through a dozen points. A computer has a much better idea of a parabola than an artist (who tends to make it asymptotic to a straight line). There are some things a computer knows, and other things an artist knows, and still others that you and I know—because we understand derivatives.

Our job is to apply1 calculus. We extract information from1 $f ^ { \prime }$ and $f ^ { \prime \prime }$ as well as $f .$ Small movements in2the graph may go unnoticed, but t2he important properties come through. Here are the main tests:

1. The sign of $f ( x )$ (aboÑve8or below axÑis: $f = 0$ at crossing point)   
2. The sign of $f ^ { \prime } ( x )$ (increasing or decreasing: $f ^ { \prime } = 0$ at stationary point)   
3. The sign of $f ^ { \prime \prime } ( x )$ (concave up or down: $f ^ { \prime \prime } { = } 0$ at injection point)   
4. The behavior of $f ( x )$ as $x \to \infty$ and $x \to - \infty$   
5. The points at which $f ( x )  \infty$ or $f ( x ) \to - \infty$   
6. Even or odd? Periodic? Jumps in $f$ or $f ^ { \prime } { ? }$ Endpoints? $f ( 0 ) ?$

$$
f ( x ) = { \frac { x ^ { 2 } } { 1 - x ^ { 2 } } } \qquad f ^ { \prime } ( x ) = { \frac { 2 x } { ( 1 - x ^ { 2 } ) ^ { 2 } } } \qquad f ^ { \prime \prime } ( x ) = { \frac { 2 + 6 x ^ { 2 } } { ( 1 - x ^ { 2 } ) ^ { 3 } } }
$$

The sign of $f ( x )$ depends on $1 - x ^ { 2 }$ : Thus $f ( x ) > 0$ in the inner interval wherÑe $x ^ { 2 } < 1$ : ThÑe gra8ph bends upwards $( f ^ { \prime \prime } ( x ) > 0 )$ in that same interval. There are no inflection points, since $f ^ { \prime \prime }$ is never zero. The stationarypoint where $f ^ { \prime }$ vanishes is $x = 0$ : We havea local minimum at $x = 0$ :

The guidelines (or asymptotes) meet the graph at infinity. For large $x$ the important terms are $x ^ { 2 }$ and $- x ^ { 2 }$ : Their ratio is $+ x ^ { 2 } / - x ^ { 2 } = - 1$ —which is the limit as $x $ $\infty$ , and $x \to - \infty$ : The horizontal asymptote is the line $y = - 1$ .

The other infinities, where $f$ blows up, occur when $1 - x ^ { 2 }$ is zero. That happens at $x = 1$ and $x = - 1$ : The vertical asymptotes are the lines $x = 1$ and $x = - 1$ . The graph in Figure 3.11a approaches those lines.



if $f ( x )  b$ as $x \longrightarrow \infty$ or $- \infty$ , the line $y = b$ is a horizontal asymptote if $f ( x )  + \infty$ or $- \infty$ as $x \to a$ , the line $x = a$ is a vertical asymptote if $f ( x ) - ( m x + b )  0$ as $x \to + \infty$ or $ - \infty$ , the line $y = m x + b$ is a sloping asymptote.

Finally comes the vital fact that th1 is function is even2: $f ( x ) = f ( - x )$ because squaring $x$ obliterates the sign. The graph is symmetric across the $y$ axis.

$T o$ summarize the effect of dividing by $1 - x ^ { 2 }$ : No effect near $x = 0$ : Blowup at 1 and $^ { - 1 }$ from zero in the denominator. The function approaches $^ { - 1 }$ as $| x | \to \infty$ :

# EXAMPLE 2

$$
f ( x ) = { \frac { x ^ { 2 } } { x - 1 } } \qquad f ^ { \prime } = { \frac { x ^ { 2 } - 2 x } { ( x - 1 ) ^ { 2 } } } \qquad f ^ { \prime \prime } = { \frac { 2 } { ( x - 1 ) ^ { 3 } } }
$$

This example divides by $x - 1$ : Therefore $x = 1$ is a vertical asymptote, where $f ( x )$ becomes infinite. Vertical asymptotes come mostly from zero denominators.

Look beyond $x = 1$ : Both $f ( x )$ and $f ^ { \prime \prime } ( x )$ are positive for $x > 1$ : The slope is zero at $x = 2$ : That must be a local minimum.

What happens as $x \to \infty$ ? Dividing $x ^ { 2 }$ by $x - 1$ , the leading term is $x$ : The function becomes large. It grows linearly—we expect a sloping asymptote. To find it, do the division properly:

$$
{ \frac { x ^ { 2 } } { x - 1 } } = x + 1 + { \frac { 1 } { x - 1 } } .
$$

The last term goes to zero. The function approaches $y = x + 1$ as the asymptote.

This function is not odd or even. Its graph is in Figure 3.11b. With zoom out you see the asymptotes. Zoom in for $f = 0$ or $f ^ { \prime } = 0$ or $f ^ { \prime \prime } { = } 0$ :

EXAMPLE 3 $f ( x ) = \sin x + { \frac { 1 } { 3 } }$ sin $3 x$  has the slope $f ^ { \prime } ( x ) = \cos x + \cos 3 x .$ Ab ove all these functions are periodic. If $x$ increases by $2 \pi$ , nothing changes. The graphs from $2 \pi$ to $4 \pi$ are repetitions of the graphs from 0 to $2 \pi$ : Thus $f ( x + 2 \pi ) =$ $f ( x )$ and the period is $2 \pi$ : Any in1terval of le2ngth $2 \pi$ will show a complete picture, and Figure 3.11c picks the interval from $- \pi$ to $\pi$ :

The second outstanding property is that $f$ is odd. The sine functions satisfy $f ( - x ) = - f ( x )$ : The graph is symmetric through the origin. By reflecting the right half through the origin, you get the left half. In contrast, the cosines in $f ^ { \prime } ( x )$ are even.

To find the zeros of $f ( x )$ and $f ^ { \prime } ( x )$ and $f ^ { \prime \prime } ( x )$ , rewrite those functions as $\begin{array} { r } { f ( x ) = 2 \sin x - \frac { 4 } { 3 } \sin ^ { 3 } x \quad f ^ { \prime } ( x ) = - 2 \cos x + 4 \cos ^ { 3 } x \quad f ^ { \prime \prime } ( x ) = - 1 0 \sin x + 1 2 \sin ^ { 3 } x . } \end{array}$

We changed sin $3 x$ to 3 sin $x - 4 \sin ^ { 3 } x$ : For the derivativesñuse $\sin ^ { 2 } x = 1 - \cos ^ { 2 } x$ : N2ow find the zeros—the crossiñng points, stationary points,ñand inflection points:

$$
{ \begin{array} { r l } { f = 0 } & { 2 \sin x = { \frac { 4 } { 3 } } \sin ^ { 3 } x \Rightarrow \sin x = 0 { \mathrm { o r } } \sin ^ { 2 } x = { \frac { 3 } { 2 } } \Rightarrow x = 0 , \pm \pi } \\ { f ^ { \prime } = 0 } & { 2 \cos x = 4 \cos ^ { 3 } x \Rightarrow \cos x = 0 { \mathrm { o r } } \cos ^ { 2 } x = { \frac { 1 } { 2 } } \Rightarrow x = \pm \pi / 4 , \pm \pi / 2 , \pm 3 \pi / 4 } \\ { f ^ { \prime \prime } = 0 } & { 5 \sin x = 6 \sin ^ { 3 } x \Rightarrow \sin x = 0 { \mathrm { o r } } \sin ^ { 2 } x = { \frac { 5 } { 6 } } \Rightarrow x = 0 , \pm 6 6 ^ { \circ } , \pm 1 1 4 ^ { \circ } , \pm \pi } \end{array} }
$$

That is more than enough information to sketch the graph. The stationary points $\pi / 4 , \pi / 2 , 3 \pi / 4$ are evenly spaced. At th ose points $f ( x )$ is ${ \sqrt { 8 } } / 3$ (maximum), $2 / 3$ (local minimum), ${ \sqrt { 8 } } / 3$ (maximum). Figure 3.11c shows the graph.

I would like to mention a beautiful continuation of this same pattern:

$$
\begin{array} { r } { f ( x ) = \sin x + \frac { 1 } { 3 } \sin 3 x + \frac { 1 } { 5 } \sin 5 x + \cdots \qquad f ^ { \prime } ( x ) = \cos x + \cos 3 x + \cos 5 x + \cdots } \end{array}
$$

If we stop after ten terms, $f ( x )$ is extremely close to a step function. If we don’t stop, the exact step function contains infinitely many sines. It jumps from $- \pi / 4$ to $+ \pi / 4$ as $x$ goes past zero. More precisely it is a “square wave,” because the graph jumps back down at $\pi$ and repeats. The slope cos $x + \cos 3 x + \cdots$ also has period $2 \pi$ : Infinitely many cosines add up to a delta function! (The slope at the jump is an infinite spike.) These sums of sines and cosines are Fourier series.

# GRAPHS BY COMPUTERS AND CALCULATORS

We have come to a topic of prime importance. If you have graphing software for a computer, or if you have a graphing calculator, you can bring calculus to life. A graph presents $y ( x )$ in a new way—different from the formula. Information that is buried in the formula is clear on the graph. But don’t throw away $y ( x )$ and $d y / d x$ . The derivative is far from obsolete.

These pages discuss how calculus and graphs go together. We work on a crucial problem of applied mathematics—to find where $y ( x )$ reaches its minimum. There is no need to tell you a hundred applications. Begin with the formula. How do you find the point $x ^ { * }$ where $y ( x )$ is smallest ?

First, draw the graph. That shows the main features. We should see (roughly) where $x ^ { * }$ lies. There may be several minima, or possibly none. But what we see depends on a decision that is ours to make—the range of $x$ and $y$ in the viewing window.

If nothing is known about $y ( x )$ , the range is hard to choose. We can accept a default range, and zoom in¤or o¤ut. We can use the autoscaling program in Section 1.7. Somehow $x ^ { * }$ can be observed on the screen. Then the problem is to compute it.

I would like to work with a specific example. We solved it by calculus—to find the best point $x ^ { * }$ to enter an expressway. Thae speeds in Section 3.2 were 30 and 60: The length of the fast road will be $b = 6$ : The range of reasonable values for the entering point is $0 \leqslant x \leqslant 6$ : The distance to the road in Figure 3.12 is $a = 3$ : We drive a distance $\sqrt { 3 ^ { 2 } + x ^ { 2 } }$ at speed 30 and the remaining distance $6 - x$ at speed 60:

$$
d r i \nu i n g t i m e y ( x ) = \frac { 1 } { 3 0 } \sqrt { 3 ^ { 2 } + x ^ { 2 } } + \frac { 1 } { 6 0 } ( 6 - x ) .
$$

This is the function to be minimized. Its graph is extremely flat.

It may seem unusual for the graph to be so level. On the contrary, it is common. A flat graph is the whole point of $d y / d x = 0$ :

The graph near the minimum looks like $y = C x ^ { 2 }$ : It is a parabola sitting on a horizontal tangent. At a distance of $\Delta x = . 0 1$ , we only go up by $C ( \Delta x ) ^ { 2 } = . 0 \bar { 0 } 0 1 C$ : Unless $C$ is a large number, this $\Delta y$ can hardly be seen.

The solution is to change scale. Zoom in on $x ^ { * }$ : The tangent line stays flat, since $d y / d x$ is still zero. But the bending from $C$ is increased. Figure 3.12 shows the zoom box blown up into a new graph of $y ( x )$ :

A calculator has one or more ways to find $x ^ { * }$ : With a TRACE mode, you direct a cursor along the graph. From the display of $y$ values, read $y _ { \mathrm { m a x } }$ and $x ^ { * }$ to the nearest pixel. A zoom gives better accuracy, because it stretches the axes—each pixel represents a smaller $\Delta x$ and $\Delta y$ : The TI-81 stretches by 4 as default. Even better, let the whole process be graphical—draw theactual ZOOM BOX on the screen. Pick two opposite corners, press ENTER, and the box becomes the new viewing window (Figure 3.12).

The first zoom narrows the search for $x ^ { * }$ : It lies between $x = 1$ and $x = 3$ : We build a new ZOOM BOX and zoom in again. Now $1 . 5 \leqslant x ^ { * } \leqslant 2$ : Reasonable accuracy comes quickly. High accuracy does not come quickly. It takes time to create the box and execute the zoom.

Question 1 What happens as we zoom in, if all boxes are square (equal scaling) ?

Answer The picture gets flatter and flatter. We are zooming in to the tangent line. Changing $x$ to $X / 4$ and $y$ to $Y / 4$ , the parabola $y = x ^ { 2 }$ flattens to $Y = X ^ { 2 } / 4$ : To see any bending, we must use a long thin zoom box.

I want to change to a tot?ally differentapproach. Suppose we have a formula for $d y / d x$ : That derivative was produced by an infinite zoom! The limit of $\Delta y / \Delta x$ came by brainpower alone:

$$
{ \frac { d y } { d x } } = { \frac { x } { 3 0 { \sqrt { 3 ^ { 2 } + x ^ { 2 } } } } } = - { \frac { 1 } { 6 0 } } . \qquad { \mathrm { C a l l ~ t h i s ~ } } f ( x ) .
$$

This function is zero at $x ^ { * }$ : The computing problem is completely changed: Solve $f ( x ) = 0 . I t$ is easier to find a root of $f ( x )$ than a minimum of $y ( x )$ . The graph of $f ( x )$ crosses the $x$ axis. The graph of $y ( x )$ goes flat—this is harder to pinpoint.

Take the model function $y = x ^ { 2 }$ for $\left| x \right| < . 0 1$ : The slope $f = 2 x$ changes from $- . 0 2$ to $+ . 0 2$ : The value of $x ^ { 2 }$ moves only by :0001 —its minimum point is hard to see.

To repeat: Minimization is easier with $d y / d x$ : The screen shows an order of magnitude improvement, when we trace or zoom on $f ( x ) = 0$ : In calculus, we have been taking the derivative for granted. It is natural to get blasé about $d y / d x = 0$ : We forget how intelligent it is, to work with the slope instead of the function.

Question 2 How do you get another order of magnitude improvement ?

Answer Use the next derivative! With a fo?rmula for $d f / d x$ , which is $d ^ { 2 } y / d x ^ { 2 }$ , the convergence is even faster. In two steps the error goes from?:01 to :0001 to :00000001: Another infinite zoom went into the formula for $d f / d x$ , and Newton’s method takes account of it. Sections 3.6 and 3.7 study $f ( x ) = 0$ :

The expressway example allo?ws perfect accuracy. We can solve $d y / d x = 0$ by algebra. The equation simplifies to $6 0 x = 3 0 { \sqrt { 3 ^ { 2 } + x ^ { 2 } } }$ : Dividing by 30 and squaring yields $4 x ^ { 2 } = \hat { 3 ^ { 2 } } + x ^ { 2 }$ : Then $3 x ^ { 2 } = 3 ^ { 2 }$ : The exact solution is $x ^ { * } = \dot { \sqrt { 3 } } = 1 . 7 3 \dot { 2 } 0 5 \ldots$

A model like this is a benchmark, to test competing methods. It also displays what we never appreciated—the extreme flatness of the graph. The difference in driving time between entering at $x ^ { * } = { \sqrt { 3 } }$ and $x = 2$ is one second.

# THE CENTERING TRANSFORM AND ZOOM TRANSFORM

For a photograph we do two things—point the right way and stand at the right distance. Then take the picture. Those steps are the same for a graph. First we pick the new center point. The graph is shifted, to move that point from $( a , b )$ to $( 0 , 0 )$ : Then we decide how far the graph should reach. It fits in a rectangle, just like the photograph. Rescaling to $x / c$ and $y / d$ puts the desired section of the curve into the rectangle.

A good photographer does more (like an artist). The subjects are placed and the camera is focused. For good graphs those are necessary too. But an everyday calculator or computer or camera is built to operate without an artist—just aim and shoot. I want to explain how to aim at $y = f ( x )$ :

We are doing exactly what a calculator does, with one big difference. It doesn’t change coordinates. We do. When $x = 1$ , $y = - 2$ moves to the center of the viewing window, the calculator still shows that point as $( 1 , - 2 )$ : When the centering transform acts on $y + 2 = m ( x - 1 )$ , those numbers disappear. This will be confusing unless $x$ and $y$ also change. The new coordinates are $X = x - 1$ and $Y = y + 2$ . Then the new equation is $Y = m X$ .

The main point (for humans) is to make the algebra simpler. The computer has no preference for $Y = m X$ over $y - y _ { 0 } = m ( x - x _ { 0 } )$ : It accepts $2 x ^ { 2 } - 4 x$ as easily as $x ^ { 2 }$ : But we do prefer $Y = m X$ and $y = x ^ { 2 }$ , partly because their graphs go through $( 0 , 0 )$ : Ever since zero was invented, mathematicians have liked that number best.

3F A centering transform shifts left by $a$ and down by $b$ : $X = x - a$ and $Y = y - b$ change $y = f ( x )$ into $Y + b = f ( X + a )$ :

EXAMPLE 4 The parabola $y = 2 x ^ { 2 } - 4 x$ has its minimum when $d y / d x =$ $4 x - 4 = 0$ : Thus $x = 1$ and $y = - 2$ : Move this bottom point to the center:

$y = 2 x ^ { 2 } - 4 x$ is

$$
Y + 2 = 2 ( X - 1 ) ^ { 2 } - 4 ( X - 1 ) \qquad { \mathrm { o r } } \qquad Y = 2 X ^ { 2 } .
$$

The new parabola $Y = 2 X ^ { 2 }$ has its bottom at $( 0 , 0 )$ : It is the same curve, shifted across and up. The only simpler parabola is $y = x ^ { 2 }$ : This final step is the job of the zoom.

Next comes scaling. We may want more detail (zoom in to see the tangent line). We may want a big picture (zoom out to check asymptotes). We might stretch one axis more than the other, if the picture looks like a pancake or a skyscraper.

3G A zoom transform scales the $X$ and $Y$ axes by $c$ and $d$ : $\mathbf { x } = c X \quad { \mathrm { a n d } } \quad \mathbf { y } = d Y \quad { \mathrm { c h a n g e } } \quad Y = F ( X ) \quad { \mathrm { t o } } \quad \mathbf { y } = d F ( \mathbf { x } / c ) .$ The new $\mathbf { x }$ and $\mathbf { y }$ are boldface letters, and the graph is rescaled. Often $c = d$ :

EXAMPLE 5 Start with $Y = 2 X ^ { 2 }$ : Apply a square zoom with $c = d$ : In the new xy coordinates, the equation is $\mathbf { y } / c = 2 ( \mathbf { x } / c ) ^ { 2 }$ : The number 2 disappears if $c = d = 2$ : With the right centering and the right zoom, every parabola that opens upward is y D x2:

Question 3 What happens to the derivatives (slope and bending) after a zoom ?

Answer The slope (first derivative) is multiplied by $d / c$ : Apply the chain rule to ${ \bf y } = d { \cal F } ( { \bf x } / c )$ : A square zoom has $d / c = 1$ —lines keep their slope. The second derivative is multiplied by $d / c ^ { 2 }$ , whichchanges the bending. A zoom out divides by small numbers $c = d$ , so the big picture is more, curved.

Combining the centering and zoom transforms, as we do in practice, gives $\textbf { y }$ in terms of $\mathbf { x }$ :

$$
y = f ( x ) \quad { \mathrm { b e c o m e s } } \quad Y = f ( X + a ) - b \quad { \mathrm { a n d ~ t h e n } } \quad \mathbf { y } = d \left[ f \left( { \frac { \mathbf { x } } { c } } + a \right) - b \right] .
$$

Question 4 Find $x$ and $y$ ranges after two transforms. Start between $^ { - 1 }$ and 1: Answer The window after centering is $- 1 \leqslant x - a \leqslant 1$ and $- 1 \leqslant y - b \leqslant 1$ : The window after zoom is $- 1 \leqslant c ( x - a ) \leqslant 1$ and $- 1 \leqslant d ( y - b ) \leqslant 1 .$ : The point $( 1 , 1 )$ was originally in the corner. The point $( c ^ { - 1 } + a , d ^ { - 1 } + b )$ is now in the corner.

The numbers ${ a , b , c , d }$ are chosen to produce a simpler function (like $\mathbf { y } = \mathbf { x } ^ { 2 }$ ). Or else—this is important in applied mathematics—they are chosen to make $\mathbf { x }$ and $\mathbf { y }$ “dimensionless.” An example is $y = { \frac { 1 } { 2 } } \cos 8 t$ : The frequency 8 has dimension 1=time. The amplitude $\frac { 1 } { 2 }$ is a distance. With $d = 2 { \mathrm { ~ c m } }$ and $c = 8$ sec, the units are removed and $\mathbf { y } = \cos \mathbf { t }$ :

May I mention one transform that does change the slope ? It is a rotation. The whole plane is turned. A photographer might use it—but normally people are supposed to be upright. You use rotation when you turn a map or straighten a picture. In the next section, an unrecognizable hyperbola is turned into $Y = 1 / X$ :