# 15.3 Green’s Theorem

This section contains the Fundamental Theorem of Calculus, extended to two dimensions. That sounds important and it is. The formula was discovered 150 years after Newton and Leibniz, by an ordinary mortal named George Green. His theorem connects a double integral over a region $R$ to a line integral along its boundary $C$ :

The integral of $d f / d x$ equals $f ( b ) - f ( a )$ : This connects a one-dimensional integral to a zero-dimensional integral. The boundary only contains two points $a$ and $b$ ! The answer $f ( b ) - f ( a )$ is some kind of a “point integral.” It is this absolutely crucial idea—to integrate a derivative from information at the boundary—that Green’s Theorem extends into two dimensions.

There are two important integrals around $C$ : The work is $\textstyle \int \mathbf { F } \cdot \mathbf { T } d s = \int M d x +$ $N d y$ : The $\mathbf { \mathcal { \mathbf { \mathit { \Pi } } } } \mathbf { \mathcal { \mathit { \mathbf { \mathit { \Pi } } } } } \mathbf { \mathcal { \mathit { \mathbf { \mathcal { \Pi } } } } } \mathbf { \mathcal { \mathit { \hat { \mathbf { \Pi } } } } } \mathbf { \mathcal { \mathbf { \mathit { \Pi } } } } \mathbf { \mathcal { \hat { \mathbf { \Pi } } } } \mathbf { \mathcal { \mathbf { \Pi } } } \mathbf { \mathcal { \mathbf { \mathit { \Pi } } } } \mathbf { \mathcal { \hat { \mathbf { \Pi } } } } \mathbf { \mathcal { \Pi } } \mathbf { \mathcal { \mathbf { \Pi } } } \mathbf { \mathcal { \hat { \Pi } } } \mathbf { \mathcal { \Pi } } \mathbf { \mathcal { \mathbf { \Pi } } } \mathbf { \mathcal { \Pi } } \mathbf { \mathcal { \hat { \mathbf { \Pi } } } } \mathbf { \mathcal { \Pi } } \mathbf { \mathcal { \Pi } } \mathbf { \mathcal { \hat { \mathbf { \Pi } } } } \mathbf { \mathcal { \Pi } } \mathbf { \mathcal { \Pi } }$ is $\textstyle \int \mathbf { F } \cdot \mathbf { n } d s = \int M d y - N d x$ (notice the switch). The first is for a force field, the second is for a flow field. The tangent vector $\mathbf { T }$ turns $9 0 ^ { \circ }$ clockwise to become the normal vector $\mathbf { n }$ : Green’s Theorem handles both, in two dimensions. In three dimensions they split into the Divergence Theorem (15.5) and Stokes’ Theorem (15.6).

Green’s Theorem applies to “smooth” functions $M ( x , y )$ and $N ( x , y )$ ; with continuous first derivatives in a region slightly bigger than $R$ : Then all integrals are well defined. $M$ and $N$ will have a definite and specific meaning in each application—to electricity or magnetism or fluid flow or mechanics. The purpose of a theorem is to capture the central ideas once and for all. We do that now, and the applications follow.

15E Green’s Theorem Suppose the region $R$ is bounded by the simple closed piecewise smooth curve $C$ : Then an integral over $R$ equals a line integral around $C$ :

$$
\oint _ { C } M d x + N d y = \iint _ { R } \left( { \frac { \partial N } { \partial x } } - { \frac { \partial M } { \partial y } } \right) d x d y .
$$

A curve is “simple” if it doesn’t cross itself (figure 8’s are excluded). It is “closed” if its endpoint $\boldsymbol { Q }$ is the same as its starting point $P$ : This is indicated by the closed circle on the integral sign. The curve is “smooth” if its tangent $\mathbf { T }$ changes continuously— the word “piecewise” allows a finite number of corners. Fractals are not allowed, but all reasonable curves are acceptable (later we discuss figure 8’s and rings). First comes an understanding of the formula, by testing it on special cases.

Special case $^ { \small 1 }$ : $M = 0$ and $N = x$ : Green’s Theorem with $\partial N / \partial x = 1$ becomes

$$
\int _ { C } x d y = \iint _ { R } 1 d x d y \quad ( { \mathrm { w h i c h i s t h e a r e a o f } } R ) .
$$

The integrals look equal, because the inner integral of $d x$ is $x$ : Then both integrals have $x d y$ —but we need to go carefully. The area of a  layer of $R$ is $d y$ times the difference in $x$ (the length of the strip). The line integral in Figure 15.8 agrees. It has an upward $d y$ times $x$ (at the right) plus a downward $- d y$ times $x$ (at the left). The integrals add up the strips, to give the total area.

Special case 2: $M = y$ and $N = 0$ and $\begin{array} { r } { \oint _ { C } y d x = \iint _ { R } ( - 1 ) d x d y = - ( \mathrm { a r e a o f } R ) . } \end{array}$

Now Green’s formula has a minus sign, because the line integral is counterclockwise. The top of each slice has $d x < 0$ (going left) and the bottom has $d x > 0$ (going right). Then $y d x$ at the top and bottom combine to give minus the area of the slice in Figure 15.8b.

Special case 3: $\oint 1 d x = 0$ : The $d x$ ’s to the right cancel the $d x$ ’s to the left (the curve is closed). With $M = 1$ and $N = 0$ ; Green’s Theorem is $0 = 0$ :

Most important case: $M \mathbf { i } + N \mathbf { j }$ is a gradient field. It has a potential function $f ( x , y )$ : Green’s Theorem is $0 = 0$ ; because $\hat { \sigma } M / \partial y = \hat { \sigma } N / \partial x$ : This is test $\mathbf { D }$ :

$$
\frac { \partial M } { \partial y } = \frac { \partial } { \partial y } \left( \frac { \partial f } { \partial x } \right) i s t h e s a m e a s \frac { \partial N } { \partial x } = \frac { \partial } { \partial x } \left( \frac { \partial f } { \partial y } \right) .
$$

The cross derivatives always satisfy $f _ { y x } { = } f _ { x y }$ : That is why gradient fields pass test $\mathbf { D }$ :

When the double integral is zero, the lineintegral is also zero: $\oint _ { \cal C } M d x + N d y =$ 0: ThBe w oBrk is zBero.  BThe field is conservative! This last step in $\mathbf { A } \Rightarrow \mathbf { B } \Rightarrow \mathbf { C } \Rightarrow \mathbf { D } \Rightarrow$ A will be complete when Green’s Theorem is proved.

Conservative examples are¾ $\oint x d x = 0$ a¾nd $\oint y ~ d y = 0$ : Area is not involved.

Remark The special cases $\oint x d y$ and $- \oint y d x$ led to the area of $R$ : As long as $1 = \partial N / \partial x - \partial M / \partial y$ ; the double integral becomes $\iint 1 d x d y$ : This gives a way to compute area by a line integral.

$$
T h e a r e a o f R i s \oint _ { C } x d y = - \oint _ { C } y d x = { \frac { 1 } { 2 } } \oint _ { C } ( x d y - y d x ) .
$$

EXAMPLE 1 The area of the triangle in Figure 15.9 is 2: Check Green’s Theorem. The last area formula in (4) uses $\textstyle { \frac { 1 } { 2 } } \mathbf { S }$ ; half the spin field. $\begin{array} { r } { N = \frac { 1 } { 2 } x } \end{array}$ and $M = - { \textstyle \frac { 1 } { 2 } } y$ yield $\begin{array} { r } { N _ { x } - M _ { y } = \frac { 1 } { 2 } + \frac { 1 } { 2 } = 1 } \end{array}$ : On one side of Green’s Theorem is $\operatorname { J } \int 1 d x d y =$ area of triangle. On the other side, the line integral has three pieces.

# 15.3 Green’s Theorem

Two pieces are zero: $x d y - y d x = 0$ on the sides where $x = 0$ and $y = 0$ : The sloping side $x = 2 - y$ has $d x = - d y$ : The line integral agrees with the area, confirming Green’s Theorem:

$$
{ \frac { 1 } { 2 } } \oint _ { C } x d y - y d x = { \frac { 1 } { 2 } } \int _ { y = 0 } ^ { 2 } ( 2 - y ) d y + y d y = { \frac { 1 } { 2 } } \int _ { 0 } ^ { 2 } 2 d y = 2 .
$$

EXAMPLE 2 The area of an ellipse is ab when the semiaxes have lengths a and $b$ .

This is a classical example, which all authors like. The points on the ellipse are $x = a \cos t , y = b \sin t$ ; as $t$ goes from 0 to $2 \pi$ : (The ellipse has $( x / a ) ^ { 2 } + ( y ^ { \prime } / b ) ^ { 2 } =$ 1:/ By computing the boundary integral, we discover the area inside. Note that the differential $x d y - y d x$ is just ab d t :

$$
( a \cos t ) ( b \cos t d t ) - ( b \sin t ) ( - a \sin t d t ) = a b ( \cos ^ { 2 } t + \sin ^ { 2 } t ) d t = a b d t .
$$

The line integral is ${ \textstyle { \frac { 1 } { 2 } } } \int _ { 0 } ^ { 2 \pi } a b d t = \pi a b$ : This a Brea  Bab is $\pi r ^ { 2 }$ ; for a circle with $a = b = r$ :

Proof of Green’s Theorem: In our special cases, the two sides of the formula were equal. We now show that they are always equal. The proof uses the Fundamental Theorem to integrate $( \partial N / \partial x ) d x$ and $( { \partial M } / { \partial y } ) d y$ : Frankly speaking, this one-dimensional theorem is all we have to work with—since we don’t know $M$ and $N$ :¾

The proof is a stepup in mathematics, to work with symbols $M$ and $N$ instead of specific functions. The iBntegral in (6) below has no numbers. The idea iBs to deal with $M$ and $N$ in two separate parts, which added together give Green’s Theorem:

$$
\oint _ { C } M d x = \iint _ { R } \int _ { \hat { \sigma } y } d x d y \quad { \mathrm { a n d ~ s e p a r a t e l y } } \quad \oint _ { C } N d y = \iint _ { R } { \frac { { \hat { \sigma } } N } { \hat { \sigma } x } } d x d y .
$$

Start with a “vBery simple” region (Figure 15.10a). Its top is given by $y = f ( x )$ and its bottom by $y = g ( x )$ : In the double integral, integrate $- { \partial M } / { \partial y }$ first with respect to $y$ : The inner integral is

$$
\int _ { g ( x ) } ^ { f ( x ) } - { \frac { \hat { \sigma } M } { \hat { \sigma } y } } d y = - M ( x , y ) \int _ { g ( x ) } ^ { f ( x ) } = - M ( x , f ( x ) ) + M ( x , g ( x ) ) .
$$

The Fundamental Theorem (in the $y$ variable) gives this answer that depends on $x$ : If we knew $M$ and $f$ and $g$ ; we could do the outer integral—from $x = a$ to $x = b$ : But we have to leave it and go to the other side of Green’s Theorem—the line integral:

$$
\oint M d x = \int _ { \log } M ( x , y ) d x + \int _ { \mathrm { b o t t o m } } M ( x , y ) d x = \int _ { b } ^ { a } M ( x , f ( x ) ) d x + \int _ { a } ^ { b } M ( x , g ( x ) ) d x .
$$

Compare (7) with (6). The integral of $M ( x , g ( x ) )$ is the same for both. The integral of $M ( x , f ( x ) )$ has a minus sign from (6). In .7/ it has a plus sign but the integral is from $b$ to $a$ : So life is good.

The part for $N$ uses the same idea. Now the $x$ integral comes first, because $( \partial N / \partial x ) d x$ is practically asking to be integrated—from $x = G ( y )$ at the left to $x =$ $F ( y )$ at the right. We reach $N ( F ( y ) , y ) - N ( G ( y ) , y )$ : Then the $y$ integral matches $\oint N d y$ and completes (5). Adding the two parts of (5) proves Green’s Theorem.

Finally we discuss the shape of $R$ : The broken ring in Figure 15.10 is not “very simple,” because horizontal lines go in and out and in and out. Vertical lines do the same. The $x$ and $y$ strips break into pieces. Our reasoning assumed no break between $y = f ( x )$ at the top and $y = g ( x )$ at the bottom.

There is a nice idea that saves Green’s Theorem. Separate the broken ring into three very simple regions $R _ { 1 }$ ; $R _ { 2 }$ ; $R _ { 3 }$ : The three double integrals equal the three line integrals around the $R$ ’s. Now add these separate results, to produce the double integral over all of $R$ : When we add the line integrals, the crosscuts $C C$ are covered twice and they cancel. The cut between $R _ { 1 }$ and $R _ { 2 }$ is covered upward (around $R _ { 1 }$ ) and downward (around $R _ { 2 }$ ). That leaves the integral around the boundary equal to the double integral inside—which is Green’s Theorem.

When $R$ is a complete ring, including the piece $R _ { 4 }$ ; the theorem is still true. The integral around the outside is still counterclockwise. But the integral is clockwise around the inner circle. Keep the region $R$ to your left as you go around $C$ : The complete ring is “doubly” connected, not “simply” connected. Green’s Theorem allows any finite number of regions $R _ { i }$ and crosscuts $C C$ and holes.

EXAMPLE 3 The area under a curve is $\textstyle \int _ { a } ^ { b } y d x$ ; as we always believed.

In computing area we never noticed the whole boundary. The true area is a line integral $- \oint y d x$ around the closed curve in Figure 15.11a. But $y = 0$ on the $x$ axis. Also $d x = 0$ on the vertical lines (up and down at $b$ and $a$ ). Those parts contribute zero to the integral of $y d x$ : The only nonzero part is back along the curve—which is the area $- \int _ { b } ^ { a } y d x$ or $\textstyle \int _ { a } ^ { b } y d x$ that we know well.

What about signs, when the curve dips below the $x$ axis? That area has been counted as negative since Chapter 1. I saved the proof for Chapter 15. The reason lies in the arrows on $C$ :

The line integral around that part goes the other way. The arrows are clockwise, the region is on the right, and the area counts as negative. With the correct rules, a figure 8 is allowed after all.

# CONSERVATIVE FIELDS

We never leave gradients alone! They give conservative fields—the work around a closed path is $f ( P ) - f ( P ) = 0$ : But a potential function $f ( x , y )$ is only available when test $\mathbf { D }$ is passed: If $\partial f / \partial x = M$ and $\partial f / \partial y = N$ then $\hat { \sigma } M / \partial y = \hat { \sigma } N / \partial x$ The reason is that $f _ { x y } = f _ { y x }$ :

Some applications prefer the language of “differentials.”BInst eBad ofBlook Bing for $f ( x , y )$ ; we look for $d f$ :

DEFINITION The expression $M ( x , y ) d x + N ( x , y ) d y$ is a differential form. When it agrees with the differential $d f = ( \partial f / \partial x ) d x + ( \partial f / \partial y ) d y$ of some function, the form is called exact. The test for an exact differential is D: $\partial N / \partial x = \partial M / \partial y$ :

Nothing is new but the language. Is $y d x$ an exact differential? $N o$ , because $M _ { y } = 1$ and $N _ { x } = 0$ : Is $y d x + x d y$ an exact differential? Yes, it is the differential of $f =$ $x y$ : That is the product rule! Now comeBs an important example, to show why $R$ should be simply connected (a region with no holes).

EXAMPLE 4 The spin field $\mathbf { S } / r ^ { 2 } = ( - y \mathbf { i } + x \mathbf { j } ) / ( x ^ { 2 } + y ^ { 2 } )$ almost passes test $\mathbf { D }$ :

$$
N _ { x } = { \frac { \partial } { \partial x } } \left( { \frac { x } { x ^ { 2 } + y ^ { 2 } } } \right) = { \frac { x ^ { 2 } + y ^ { 2 } - x ( 2 x ) } { ( x ^ { 2 } + y ^ { 2 } ) ^ { 2 } } } = M _ { y } = { \frac { \partial } { \partial y } } \left( { \frac { - y } { x ^ { 2 } + y ^ { 2 } } } \right) = { \frac { - ( x ^ { 2 } + y ^ { 2 } ) + y ( 2 y ) } { ( x ^ { 2 } + y ^ { 2 } ) ^ { 2 } } } .
$$

Both numerators are $y ^ { 2 } - x ^ { 2 }$ : Test $\mathbf { D }$ looks good. To find $f ,$ integrate $M =  { \partial } f /  { \partial } x$ :

$$
f ( x , y ) = \int - y d x / ( x ^ { 2 } + y ^ { 2 } ) = \tan ^ { - 1 } ( y / x ) + C ( y ) .
$$

The extra part $C ( y )$ can be zero—the $y$ derivative of $\tan ^ { - 1 } ( y / x )$ gives $N$ with no help from $C ( y )$ : The potential $f$ is the angle $\theta$ in the usual $x , y , r$ right triangle.

Test $\mathbf { D }$ is passed and $\mathbf { F }$ is grad $\theta$ : What am I worried about? It is only this, that Green’s Theorem on a circle seems to give $2 \pi = 0$ : The double integral is $\iint ( N _ { x } - M _ { y } ) d x d y$ : According to (8) this is the integral of zero. But the line integral is $2 \pi$ :

$$
\oint \mathbf { F } \cdot d \mathbf { R } = \oint ( - y ~ d x + x ~ d y ) / ( x ^ { 2 } + y ^ { 2 } ) = 2 ( { \mathrm { a r e a ~ o f ~ c i r c l e } } ) / { \mathit { a } ^ { 2 } } = 2 \pi a ^ { 2 } / a ^ { 2 } = 2 \pi .
$$

With $x = a$ cos $t$ and $y = a$ sin $t$ we would find the same answer. The work is $2 \pi$ (not zero!) when the path goes around the origin.

We have a paradox. If Green’s Theorem is wrong, calculus is in deep trouble. Some requirement must be violated to reach $2 \pi = 0$ : Looking at $\mathbf { S } / r ^ { 2 }$ ; the problem is at the origin. The field is not defined when $r = 0$ (it blows up). The derivatives in (8)

are not continuous. Test D does not apply at the origin, and was not passed. We could remove $( 0 , 0 )$ ; but then the region where test D is passed would have a hole.

It is amazing how one point can change everything. When the path circles the origin, the line integral is not zero. The potential function $f = \theta$ increases by $2 \pi$ . That agrees with $\int \mathbf { F } \cdot d \mathbf { R } = 2 \pi$ from (9). It disagrees with $\textstyle \iint 0 d x d y$ : The $2 \pi$ is right, the zero is wrong. $N _ { x } - M _ { y }$ must be a “delta function of strength $2 \pi$ :”

The double integral is $2 \pi$ from an infinite spike over the origin—even though $N _ { x } = M _ { y }$ everywhere else. In fluid flow the delta function is a “vortex.”

# FLOW ACROSS A CURVE: GREEN’S THEOREM TURNED BY $9 0 ^ { \circ }$

A flow field is easier to visualize than a force field, because something is really there and it moves. Instead of gravity in empty space, water has velocity $M ( x , y ) \mathbf { i } + N ( x , y ) \mathbf { j }$ : At the boundary $C$ it can flow in or out. The new form of Green’s Theorem is a fundamental “balance equation” of applied mathematics:

Flow through $C$ (out minus in) $\ c =$ replacement in $R$ (source minus sink).

The flow is steady. Whatever goes out through $C$ must be replaced in $R$ : When there are no sources or sinks (negative sources), the total flow through $C$ must be zero. This balance law is Green’s Theorem in its “normal form” (for $\mathbf { n }$ ) instead of its “tangential form” (for $\mathbf { T }$ ):

$$
\oint M d x + N d y  \oint - N d x + M d y \iint ( N _ { x } - M _ { y } ) d x d y  \iint ( M _ { x } + N _ { y } ) d x d y .
$$

Playing with letters has proved a new theorem! The two left sides in (11) are equal, so the right sides are equal—which is Green’s Theorem (10) for the flux. The components $M$ and $N$ can be chosen freely and named freely.

The change takes $M \mathbf { i } + N \mathbf { j }$ into its perpendicular field $- N \mathbf { i } + M \mathbf { j }$ : The field is turned at every point (we are not just turning the plane by $9 0 ^ { \circ }$ ). The spin field $\mathbf { S } =$ $- y \mathbf { i } + x \mathbf { j }$ changes to the position field $\mathbf { R } = x \mathbf { i } + y \mathbf { j }$ : The position field $\mathbf { R }$ changes to $- \mathbf { S }$ : Streamlines of one field are equipotentials of the other field. The new form (10) of Green’s Theorem is just as important as the old one—in fact I like it better. It is easier to visualize flow across a curve than circulation along it.

The change of letters was jusBt for Bthe prBoof. BFrom now on $\mathbf { F } = M \mathbf { i } + N \mathbf { j }$ :

EXAMPLE 5 Compute both sides of the new form (10) for $\mathbf { F } = 2 x \mathbf { i } + 3 y \mathbf { j }$ : The region $R$ is a rectangle with sides $a$ and $b$ :

Solution This field has $\hat { \sigma } M / \hat { \sigma } x + \hat { \sigma } N / \hat { \sigma } y = 2 + 3$ : The integral over $R$ is $\iint _ { R } 5 d x d y = 5 a b$ : The line integral has four parts, because $R$ has four sides. Between the left and right sides, $M = 2 x$ increaseBs by B $2 a$ : BDow nB the left and up the right, $\int M d y = 2 a b$ (those sides have length $b$ ). Similarly $N = 3 y$ changes by $3 b$ between the bottom and top. Those sides have length $a$ ; so they contribute $3 a b$ to a total line integral of $5 a b$ :

Important: The “divergence” of a flow field is $\hat { \sigma } M / \hat { \sigma } x + \hat { \sigma } N / \hat { \sigma } y$ : The example has divergence $= 5$ : To maintain this flow we must replace 5 units continually—not just at the origin but everywhere. (A one-point source is in example 7.) The divergence is the source strength, because it equals the outflow. $\pmb { T 0 }$ understand Green’s Theorem for any vector field $M \mathbf { i } + N \mathbf { j }$ ; look at a tiny rectangle (sides $d x$ and $d y )$ :

Flow out the right side minus flow in the left side $\ c =$ .change in $M$ / times $d y$

Flow out the top minus flow in the bottom $\ c =$ .change in $N$ / times $d x$

Total flow out of rectangle: $d M d y + d N d x = ( \partial M / \partial x + \partial N / \partial y ) d x d y$

The divergence times the area $d x d y$ equals the total flow out. Section 15:5 gives more detail with more care in three dimensions. The divergence is $M _ { x } + N _ { y } + P _ { z }$ :

EXAMPLE 6 Find the flux through a closed curve $C$ of the spin field $\mathbf { S } = - y \mathbf { i } +$ $x \mathbf { j }$ :

Solution The field has $M = - y$ and $N = x$ and $M _ { x } + N _ { y } = 0$ : The double integral is zero. Therefore the total flow (out minus in) is also zero—through any closed curve. Figure 15.13 shows flow entering and leaving a square. No fluid is added or removed. There is no rain and no evaporation. When the divergence $M _ { x } + N _ { y }$ is zero, there is no source or sink.



# FLOW FIELDS WITHOUT SOURCES

This is really quite important. Remember that conservative fields do no work around $C$ ; they have a potential $f _ { : }$ ; and they have “zero curl.” Now turn those statements through $9 0 ^ { \circ }$ ; to find their twins. Source-free fields have no flux through $C$ ; they have stream functions $g$ ; and they have “zero divergence.” The new statements $\mathbf { E { - } F { - } G { - } H }$ describe fields without sources.

15G The field $\mathbf { F } = M ( x , y ) \mathbf { i } + N ( x , y ) \mathbf { j }$ is source-free if it has these properties: E The total flux $\oint \mathbf { F } \cdot \mathbf { n } d s$ through every closed curve is zero. F Across all curves from $P$ to $\boldsymbol { Q }$ ; the flux $\int _ { P } ^ { Q } \mathbf { F } \cdot \mathbf { n } d s$ is the same. G There is astream function $g ( x , y )$ ; for which $M = \partial g / \partial y$ and $N = - \hat { \sigma } g / \hat { d } x$ : H The components satisfy $\partial M / \partial x + \partial N / \partial y = 0$ (the divergence is zero). A field with one of these properties has them all. $\mathbf { H }$ is the quick test.

The spin field $- y \mathbf { i } + x \mathbf { j }$ passed this test (Example 6 was source-free). The field $2 x \mathbf { i } + 3 y$ j does not pass (Example 5 had $M _ { x } + N _ { y } = 5$ ). Example 7 almost passes.

EXAMPLE 7 The radial field $\mathbf { R } / r ^ { 2 } = ( x \mathbf { i } + y \mathbf { j } ) / ( x ^ { 2 } + y ^ { 2 } )$ has a point source at $( 0 , 0 )$ :

The new test $\mathbf { H }$ is divergenc $e = \partial M / \partial x + \partial N / \partial y = 0$ : Those two derivatives are

$$
\frac { \hat { \mathcal { O } } } { \partial x } \left( \frac { x } { x ^ { 2 } + y ^ { 2 } } \right) = \frac { x ^ { 2 } + y ^ { 2 } - x ( 2 x ) } { ( x ^ { 2 } + y ^ { 2 } ) ^ { 2 } } \quad \mathrm { a n d } \quad \frac { \hat { \mathcal { O } } } { \partial y } \left( \frac { y } { x ^ { 2 } + y ^ { 2 } } \right) = \frac { x ^ { 2 } + y ^ { 2 } - y ( 2 y ) } { ( x ^ { 2 } + y ^ { 2 } ) ^ { 2 } } .
$$

They add to zero. There seems to be no source (if the calculation is correct). The flow through a circle $x ^ { 2 } + y ^ { 2 } = a ^ { 2 }$ should be zero. But it’s not:

$$
\oint M d y - N d x = \oint ( x d y - y d x ) / ( x ^ { 2 } + y ^ { 2 } ) = 2 ( \mathrm { a r e a } \mathrm { o f } \mathrm { c i r c l e } ) / a ^ { 2 } = 2 \pi .
$$

A source is hidden somewhere. Looking at ${ \bf R } / r ^ { 2 }$ ; the problem is at $( 0 , 0 )$ : The field is not defined when $r = 0$ (it blows up). The derivatives in (12) are not continuous. Test $\mathbf { H }$ does not apply, and was not passed. The divergence $M _ { x } + N _ { y }$ must be a “delta function” of strength $2 \pi$ : There is a point source sending flow out through all circles.

I hope you see the analogy with Example 4. The field $\mathbf { S } / r ^ { 2 }$ is curl-free except at $r = 0$ : The field ${ \bf R } / r ^ { 2 }$ is divergence-free except at $r = 0$ : The mathematics is parallel and the fields are perpendicular. A potential $f$ and a stream function $g$ require a region without holes.

# THE BEST FIELDS: CONSERVATIVE AND SOURCE-FREE

What if F is conservative and also source-free? Those are outstandingly important fields. The curl is zero and the divergence is zero. Because the field is conservative, it comes from a potential. Because it is source-free, there is a stream function:

$$
M = \frac { \partial f } { \partial x } = \frac { \partial g } { \partial y } \qquad \mathrm { a n d } \qquad N = \frac { \partial f } { \partial y } = - \frac { \partial g } { \partial x } .
$$

Those are the Cauchy-Riemann equations, named after a great mathematician of his time and one of the greatest of all time. I can’t end without an example.

EXAMPLE 8 Show that $y \mathbf { i } + x \mathbf { j }$ is both conservative and source-free. Find $f$ and $g$ :

Solution With $M = y$ and $N = x$ ; check first that $\partial M / \partial y = 1 = \partial N / \partial x$ : There must be a potential function. It is $f { = } x y$ ; which achieves $\partial f / \partial x = y$ and $\partial f / \partial y =$ $x$ : Note that $f _ { x x } + f _ { y y } = 0$ :

Check next that $\hat { \sigma } M / \hat { \sigma } x + \hat { \sigma } N / \hat { \sigma } y = 0 + 0$ : There must be a stream function. It is $g { = } { \scriptstyle { \frac { 1 } { 2 } } } ( y ^ { 2 } - x ^ { 2 } )$ ; which achieves $\partial g / \partial y = y$ and ${ \partial g } / { \partial x } = - x$ : Note that $g _ { x x } +$ gyy D0:

The curves $f =$ constant are the equipotentials. The curves $g =$ constant are the streamlines (Figure 15.4). These are the twin properties—a conservative field with a potential and a source-free field with a stream function. They come together into the fundamental partial differential equation of equilibrium—Laplace’s equation $f _ { x x } + f _ { y y } = 0$ :

15H There is a potential and stream function when $M _ { y } = N _ { x }$ and $M _ { x } = - N _ { y }$ : They satisfy Laplace’s equation: $f _ { x x } + f _ { y y } = M _ { x } + N _ { y } = 0 \qquad { \mathrm { a n d } } \qquad g _ { x x } + g _ { y y } = - N _ { x } + M _ { y } = 0 .$ (15)

If we have $f$ without $g$ ; as in $f = x ^ { 2 } + y ^ { 2 }$ and $M = 2 x$ and $N = 2 y$ ; we don’t have Laplace’s equation: $f _ { x x } + f _ { y y } = 4$ : This is a gradient field that needs a source. If we have $g$ without $f ,$ ; as in $g = x ^ { 2 } + y ^ { 2 }$ and $M = 2 y$ and $N = - 2 x$ ; we don’t have Laplace’s equation. The field is source-free but it has spin. The first field is 2R and the second field is 2S:

With no source an»d»no spin, we are with¾Laplace at the cen»te»r of mathematics and science.