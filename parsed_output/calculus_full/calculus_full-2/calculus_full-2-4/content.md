# 2.4 The Derivative of the Sine and Cosine

This section does two things. One is to compute the derivat2ivesof sin $x$ and cos $x$ : The other is to explain why these functions are so important. The1y desc2ribe oscillation, which will be expressed in words and equations. You will see a “differential equation.” It involves the derivative of an unknown function $y ( x )$ :

The differential equation will say that the second derivative—the derivative of the derivative—is equal and opposite to $y$ : In symbols this is $y ^ { \prime \prime } { = } - y$ : Distance in one direction leads to acceleration in the other direction. That makes $y$ and $y ^ { \prime }$ and $y ^ { \prime \prime }$ all oscillate. The solutions to $y ^ { \prime \prime } { = } - y$ are sin $x$ and cos $x$ and all their combinations.

We begin with the slope. The derivative of $y = \sin x$ is $y ^ { \prime } { = } \cos x$ : There is no reason for that to be a mystery, but I still find it beautiful.Chapter 1 followed a ball around a circle; the shadow went up and dÑown. Its height was sin $t$ and its velocity was cos $t$ : We now find that derivative by the standard method of limits, when $y ( x ) = \sin x$ :

$$
{ \frac { d y } { d x } } = \operatorname* { l i m i t } \operatorname { o f } { \frac { \Delta y } { \Delta x } } = \operatorname* { l i m } _ { h \to 0 } { \frac { \sin ( x + h ) - \sin x } { h } } .
$$

The sine is harder to work with than $x ^ { 2 }$ or $x ^ { 3 }$ : Where we had $( x + h ) ^ { 2 }$ or $( x + h ) ^ { 3 }$ , we now have $\sin ( x + h )$ : This calls for one of the basic “addition formulas” from trigonometry, reviewed in Section 1:5W

$$
\begin{array} { c } { \sin ( x + h ) = \sin x \cos h + \cos x \sin h } \\ { \cos ( x + h ) = \cos x \cos h - \sin x \sin h . } \end{array}
$$

Equation (2) puts $\Delta y = \sin ( x + h ) - \sin x$ in a new form:

$$
\frac { \Delta y } { \Delta x } = \frac { \sin x \cos h + \cos x \sin h - \sin x } { h } = \sin x \left( \frac { \cos h - 1 } { h } \right) + \cos x \left( \frac { \sin h } { h } \right) .
$$

The ratio splits into two simpler pieces on the right. Algebra and trigonometry got us this far, and now comes thecalculus problem. What happens as $h  0 ?$ It is no longer easy to divideÑby $h$ : (I will not even mention thÑe unspeakable crime of writing $( \sin h ) / h = \sin$ :) There are two critically important limits—the first is zero and the second is one:

$$
\operatorname* { l i m } _ { h \to 0 } { \frac { \cos h - 1 } { h } } = 0 \qquad { \mathrm { a n d } } \qquad \operatorname* { l i m } _ { h \to 0 } { \frac { \sin h } { h } } = 1 .
$$

The careful reader will object that limits have not been defined! You may further object to computing these limits separately, before combining them into equation (4). Nevertheless—following the principle of ideas now, rigor later—I would like to proceed. It is entirely true that the limit of (4) comes from the two limits in (5):

$$
{ \frac { d y } { d x } } = ( \sin x ) ( \operatorname { f i r s t } \operatorname { l i m i t } ) + ( \cos x ) ( \operatorname { s e c o n d } \operatorname { l i m i t } ) = 0 + \cos x .
$$

The secant slope $\Delta y / \Delta x$ has approached the tangent slope $d y / d x$ :

2G The derivative of $y = \sin x$ is $d y / d x = \cos x$ :

We cannot pass over the crucial step—the two limits in (5). They contain the real ideas. Both ratios become $0 / 0$ if we just substitute $h = 0$ . Remember that the cosine of a zero angle is 1, and the sine of a zero angle is 0: Figure 2.8a shows a small angle $h$ (as near to zero as we could reasonably draw). The edge of length sin $h$ is close to zero, and the edÑge of length cÑos $h$ is near 1:ÑFig8ure 2.8b shows how the ratio of sin $h$ to $h$ (both headed for zero) gives the slope of the sine curve at the start.

When two functions approach zero, their ratio might do anything. We might have

$$
\frac { h ^ { 2 } } { h } \to 0 \quad \mathrm { o r } \quad \frac { h } { h } \to 1 \quad \mathrm { o r } \quad \frac { \sqrt { h } } { h } \to \infty .
$$

No clue comes from $0 / 0$ : When matters is whether the top or bottom goes to zero more quickly. Roughly speaking, we want to show that $( \cos h - 1 ) / h$ is like $h ^ { 2 } / h$ and $( \sin h ) / h$ is like $h / h$ :

Time out The graph of sin $x$ is in Figure 2.9 (in black). The graph of $\sin ( x + \Delta x )$ sits just beside it (in red). The height difference is $\Delta f$ when the shift distance is $\Delta x$ :

Now divide by that small number $\Delta x$ (or $h$ ). The second figure shows $\Delta f / \Delta x$ : It is close to cos $x$ : (Look how it starts—it is not quite cos $x$ :) Mathematics will prove that the limit is cos $x$ exactly, when $\Delta x  0$ : Curiously, the reasoning concentrates on only one point . $( x = 0$ /: The slope at that point is cos $0 = 1$ :

We now prove this: sin $\Delta x$ divided by $\Delta x$ goes to 1: The sine curve starts with slope 1: By the addition formula for $\sin ( x + h )$ , this answer at one point will lead to the slope cos $x$ at all points.

Question Why does the graph of $f ( x + \Delta x )$ shift left from $f ( x )$ when $\Delta x > 0 ?$ Answer When $x = 0$ , the shifted graph is already showing $f ( \Delta x )$ : In Figure 2.9a, the red graph is shifted left from the black graph. The red graph shows sin $h$ when the black graph shows sin 0:

$$
\mathsf { T H E } \mathsf { L I M I T O F } ( \sin h ) / h \mathsf { I S } 1
$$

There are several ways to find this limit. The direct approach is to let a computer draw a graph. Figure 2.10a is very convincing. The function $( \sin h ) / h$ approaches 1 at the key point $h = 0$ . So does $( \tan h ) / h$ : In practice, the only danger is that you might get a message like “undefined function” and no graph. (The machine may refuse to divide by zero at $h = 0$ : Probably you can get around that.) Because of the importance of this limit, I want to give a mathematical proof that it equals 1:

Figure 2.10b indicates, but still only graphically, that sin $h$ stays below $h$ : (The first graph shows that too; $( \sin h ) / h$ is below 1:) We als¡o see that tan $h$ stays above $h$ : Remember that the tangent is the ratio of sine to cosine. Dividing by the cosine is enough to push the tangent above $h$ : The crucial inequalities (to be proved when $h$ is small and positive) are

$$
\sin h < h \qquad { \mathrm { a n d } } \qquad \tan h > h .
$$

Since tan $h = ( \sin h ) / ( \cos h )$ , those are the same as

$$
{ \frac { \sin h } { h } } < 1 \qquad { \mathrm { a n d } } \qquad { \frac { \sin h } { h } } > \cos h .
$$

What happens as $h$ goes to zero ? The ratio $( \sin h ) / h$ is squeezed between cos $h$ and 1. But cos $h$ is approaching 1! The squeeze as $h  0$ leaves only one possibility for $( \sin h ) / h$ , which is caught in be tween: The ratio $( \sin h ) / h$ approaches 1.

Figure 2.10 shows that “squeeze play.” If two functions approach the same limit, so does any function caught in between. This is proved at the end of Section 2:6:

For negative values of $h$ , which are absolutely allowed, the result is the same. To the left of zero, $h$ reverses sign and sin $h$ reverses sign. The ratio $( \sin h ) / h$ is unchanged. (The sine is an odd function: $\sin ( - h ) = - \sin h .$ ) The ratio is an even function, symmetric around zero and approaching 1 from both sides.

The proof depends on sin $h < h < \tan h$ , which is displayed by the graph but not explained. We go back to right triangles.

Figure 2.11a shows why si n $h < h$ : The straight line $P Q$ has length $2 \sin h$ : The circular arc must be longer, because the shortest distance between two points is a straight line. $\dagger$ The arc $P Q$ has length $2 h$ : (Important: When the radius is 1, the arc length equals the angle. The full circumference is $2 \pi$ and the full angle is also $2 \pi$ :) The straight distance $2 \sin h$ is less than the circular distance $2 h$ ; so sin $h < h$ .

Figure 2.11b shows why $h < \tan h$ : This time we look at areas. The triangular area is $\scriptstyle { \frac { 1 } { 2 } } ( { \mathrm { b a s e } } ) ( { \mathrm { h e i g h t } } ) = { \frac { 1 } { 2 } } ( 1 ) ( \tan h )$ : Inside that triangle is the shaded sector of the circle.

Its area is $h / 2 \pi$ times the area of the whole circle (because the angle is that fraction of the whole angle). The circle has area $\pi r ^ { 2 } = \pi$ , so multiplication by $h / 2 \pi$ gives $\textstyle { \frac { 1 } { 2 } } h$ for the area of the sector. Comparing with the triangle around it, $\frac { 1 } { 2 }$ tan $\dot { h } > \frac { 1 } { 2 } h$ :

The inequalities sin $h < h < \tan h$ are now proved. The squeeze in equation (8) produces $( \sin h ) / h \to 1$ : Q.E.D. Problem 13 shows how to prove sin $h < h$ from areas.

Note All angles $x$ and $h$ are being measured in radians. In degrees, cos $x$ is not the derivative of sin $x$ . A degree is much less than a radian, and $d y / d x$ is reduced by the factor $2 \pi / 3 6 0$ :

This second limit is different. We will show that $1 - \cos h$ shrinks to zero more quickly than $h$ : Cosines are connected to sines by $( \sin h ) ^ { 2 } + ( \cos h ) ^ { 2 } = 1$ : We start from the known fact sin $h < h$ and work it into a form involving cosines:

$$
( 1 - \cos h ) ( 1 + \cos h ) = 1 - ( \cos h ) ^ { 2 } = ( \sin h ) ^ { 2 } < h ^ { 2 } .
$$

Note that everything is positive. Divide through by $h$ and also by $1 + \cos h$ :

$$
0 < \frac { 1 - \cos h } { h } < \frac { h } { 1 + \cos h } .
$$

Our ratio is caught in the middle. The right side goes to zero because $h  0$ . This is another “squeeze”—there is no escape. Our ratio goes to zero.

For cos $h - 1$ or for negative $h$ , the signs changebut minus zero is still zero. This confirms equation (6). The slope of sin $x$ is cos $x$ :

Remark Equation (10) also shows that $1 - \cos h$ is approximately ${ \scriptstyle { \frac { 1 } { 2 } } } h ^ { 2 }$ : The 2 comes from $1 + \cos h$ : This is a basic purpose of calculus—to find simple approximations like ${ \textstyle \frac { 1 } { 2 } } h ^ { 2 }$ : A “tangent parabola” $\textstyle { \mathrm { ~ \bar { 1 } ~ - ~ } } { \frac { 1 } { 2 } } h ^ { 2 }$ is close to the top of the cosine curve.

# THE DERIVATIVE OF THE COSINE

This will be easy. The quick way to differentiate cos $x$ is to shift the sine curve by $\pi / 2$ : That yields the cosine curve (solid line in Figure 2.12b). The derivative also shifts by $\pi / 2$ (dotted line). The derivative of cos $x i s - \sin { x }$ .

Notice how the dotted line (the slope) goes below zero when the solid line turns downward. The slope equals zero when the solid line is level. Increasing functions have positive slopes. Decreasing functions have negative slopes. That is important, and we return to it.

There is more information in $d y / d x$ than “function rising” or “function falling.” The slope tells how quickly the function goes up or down. It gives the rate of change. The slope of $y = \cos x $ canbe computed in the normal way, as the limit of $\Delta y / \Delta x$ :

$$
{ \begin{array} { l } { { \frac { \Delta y } { \Delta x } } = { \frac { \cos ( x + h ) - \cos x } { h } } = \cos x \left( { \frac { \cos h - 1 } { h } } \right) - \sin x \left( { \frac { \sin h } { h } } \right) } \\ { { \frac { d y } { d x } } = ( \cos x ) ( 0 ) - ( \sin x ) ( 1 ) = - \sin x . } \end{array} }
$$

The first line came from formula (3) for $\cos ( x + h )$ : The second line took limits, reaching 0 and 1 as before. This confirms the graphical proof that the slope of cos $x$ is $- \sin x$ :

# THE SECOND DERIVATIVES OF THE SINE AND COSINE

We now introduce the derivative of the derivative. That is the second derivative of the original function. It tells how fast the slope is changing, not how fast $y$ itself is changing. The second derivative is the “rate of change of the velocity.” A straight line has constant slope (constant velocity), so its second derivative is zero:

$$
f ( t ) = 5 t \quad \mathrm { { h a s } } \quad d f / d t = 5 \quad \mathrm { { a n d } } \quad d ^ { 2 } f / d t ^ { 2 } = 0 .
$$

The parab2ola $y = x ^ { 2 }$ has slope $2 x$ (linear) which has slope 2 (constant). Similarly

$$
\textstyle f ( t ) = { \frac { 1 } { 2 } } a t ^ { 2 } \quad { \mathrm { ~ h a s ~ } } \quad d f / d t = a t \quad { \mathrm { ~ a n d ~ } } \quad d ^ { 2 } f / d t ^ { 2 } = a .
$$

There stands the notation $d ^ { 2 } f / d t ^ { 2 } ( \mathrm { o r } d ^ { 2 } y / d x ^ { 2 } )$ for the second derivative. A short form is $f ^ { \prime \prime }$ or $y ^ { \prime \prime }$ : (This is pronounced $f$ double prime or $y$ double prime). Example: The second derivative of ${ \bar { y } } = x ^ { 3 }$ is $y ^ { \prime \prime } { = } 6 x$ :

In the distance-velocity problem, $f ^ { \prime \prime }$ is acceleration. It tells how fast $v$ is changing, while $v$ tells how fast $f$ is changing.Where $d f / d t$ was distance=time, the second derivative is distance= $( \mathrm { t i m e } ) ^ { 2 }$ : The acceleration du2e to gravity is about $3 2 \mathrm { f t } / \mathrm { s e c } ^ { 2 }$ or $9 . 8 ~ \mathrm { m } / \mathrm { s e c } ^ { 2 }$ , which means that $v$ increases by 32 ft=sec in one second. It does not mean that the distance increases by 32 feet!

The graph of $y = \sin t$ increases at the start. Its derivative cos $t$ is positive. However t2he¡second derivati1ve is $- \sin t$ : The curve is bending down while going up. 2The arch is “conca1ve down” because $y ^ { \prime \prime } { = } - \sin t$ is negative.

At $t = \pi$ the curve reaches zero and goes negative. The second derivative becomes positive. Now the curve bends upward. The lower arch is “concave up.”

Chapter 3 studies these things properly—here we get an advance look for sin $t$ :

The remarkable fact about the sine and cosine is that $y ^ { \prime \prime } { = } - y$ : That is unusual and special: acceleratio $\iota = - d i s t a n c e$ : The greater the distance, the greater the force pulling back:

$$
\begin{array} { r } { y = \sin t \quad \mathrm { ~ h a s ~ } \quad d y / d t = + \cos t \quad \mathrm { ~ a n d ~ } \quad d ^ { 2 } y / d t ^ { 2 } = - \sin t = - y . } \\ { y = \cos t \quad \mathrm { ~ h a s ~ } \quad d y / d t = - \sin t \quad \mathrm { ~ a n d ~ } \quad d ^ { 2 } y / d t ^ { 2 } = - \cos t = - y . } \end{array}
$$

Question Does ${ d ^ { 2 } y } / { d t ^ { 2 } } < 0$ mean that the distance $y ( t )$ is decreasing ? Answer No. Absolutely not! It means that $d y / d t$ is decreasing, not necessarily $y$ : At the start of the sine curve, $y$ is still increasing but $y ^ { \prime \prime } < 0$ :

# 2 Applications of the Derivative

Sines and cosines give simple harmonic motion—up and down, forward and back, out and in, tension and compression. Stretch a spring, and the restoring force pulls it back. Push a swing up, and gravity brings it down. These motions are controlled by a differential equation:

$$
{ \frac { d ^ { 2 } y } { d t ^ { 2 } } } = - y .
$$

All solutions are combinatioÑns of the sine and coÑsine: $y = A$ sinÑ $t + B$ cos t:

This is not a course on differential equations. But you have to see the purpose of calculus. It models events by equations. It models oscillation by equation (12). Your heart fills and empties. Balls bounce. Current alternates. The economy goes up and down:

$$
{ \mathrm { h i g h ~ p r i c e s } }  { \mathrm { h i g h ~ p r o d u c t i o n } }  { \mathrm { l o w ~ p r i c e s } }  \cdots
$$

We can’t live without oscillations (or differential equations).