# 9.2 Polar Equations and Graphs

The most important equation in polar coordinates, by far, is $r = 1$ : The angle $\theta$ does not even appear. The equation looks too easy, but that is the point! The graph is a circle around the origin (the unit circle). Compare with the line $x = 1$ : More important, compare the simplicity of $r = 1$ with the complexity of $y = \pm { \sqrt { 1 - x ^ { 2 } } }$ : Circles are so common in applications that they created the need for polar coordinates.

This section studies polar curves $r = F ( \theta )$ : The cardioid is a sentimental favorit e— maybe parabolas are more practical. The cardioid is $r = 1 + \cos \theta$ ; the parabola is $r = 1 / ( 1 + \cos \theta )$ : Section 12.2 adds cycloids and astroids. A graphics package can draw them and so can we.

Together with the circles $r =$ constant go the straight lines $\theta =$ constant. The equation $\theta = \pi / 4$ is a ray out from the origin, at that fixed angle. If we allow $r < 0$ ; as we do in drawing graphs, the one-directional ray changes to a full line. Important: The circles are perpendicular to the rays. We have “orthogonal coordinates”— more interesting than the $x - y$ grid of perpendicular lines. In principle $x$ could be mixed with $\theta$ (non-orthogonal), but in practice that never happens.

Other curves are attractive in polar coordinates—we look first at five examples. Sometimes we switchback to $x = r$ cos $\theta$ and $y = r$ sin $\theta$ ; to recognize the graph.

EXAMPLE 1 The graph of $r = 1 / \cos \theta$ is the straight line $x = 1$ (because $r$ cos $\theta = 1$ ).

EXAMPLE 2 The graph of $r = \cos 2 \theta$ is the four-petal flower in Figure 9.3.

The points at $\theta = 3 0 ^ { \circ }$ and $- 3 0 ^ { \circ }$ and $1 5 0 ^ { \circ }$ and $- 1 5 0 ^ { \circ }$ are marked on the flower. They all have $\begin{array} { r } { r = \cos 2 \theta = \frac { 1 } { 2 } } \end{array}$ : There are three important symmetries—acrossthe $x$ axis, across the $y$ axis, and through the origin. This four-petal curve has them all. So does the vertical flower $r = \sin 2 \theta$ —but surprisingly, the tests it passes are different.

(Across the $x$ axis: $y \ t o \ - y )$ ) There are two ways to cross. First, change $\theta$ to $- \theta$ : The equation $r = \cos 2 \theta$ stays the same. Second, change $\theta$ to $\pi - \theta$ and also $r$ to $- \boldsymbol { r }$ : The equation $r = \sin 2 \theta$ stays the same. Both flowers have $x$ axis symmetry.

(Across the y axis: $x \ t o \ - x )$ There are two ways to cross. First, change $\theta$ to $\pi - \theta$ : The equation $r = \cos 2 \theta$ stays the same. Secon d, change $\theta$ to $- \theta$ and $r$ to $- \boldsymbol { r }$ : Now $r = \sin 2 \theta$ stays the same (the sine is odd). Both curves have $y$ axis symmetry.

(Through the origin) Now we c hange $r$ to $- \boldsymbol { r }$ or $\theta$ to $\theta + \pi$ : The flower equations pass the second test only: cos $2 ( \theta + \pi ) = \cos 2 \theta$ and s $\dot { \ln { 2 } } ( \theta + \pi ) = \dot { \sin { 2 \theta } }$ : Every equation $r ^ { 2 } = F ( { \boldsymbol { \theta } } )$ passes the first test, since $( - r ) ^ { 2 } = r ^ { 2 }$ .

The circle $r = \cos \theta$ has $x$ axis symmetry, but not $y$ or $r$ : The spiral $r = \theta ^ { 3 }$ has $y$ axis symmetry, because $- r = ( - \theta ) ^ { 3 }$ is the same equation.

Question What happens if you change $r$ to $- \boldsymbol { r }$ and also change $\theta$ to $\theta + \pi ?$ Answer Nothing—because $( r , \theta )$ and $( - r , \theta + \pi )$ are always the same point.

EXAMPLE 3 The graph of $r = \theta$ is a spiral of Archimedes—or maybe two spirals.

The spiral adds new points as $\theta$ increases past $2 \pi$ : Our other examples are “periodic”— $\mathbf { \nabla } \cdot \theta = 2 \pi$ gives the same point as $\theta = 0$ : A periodic curve repeats itself. The spiral moves out by $2 \pi$ each time it comes around. If we allow negative angles and negative $r = \theta$ ; a second spiral appears.

EXAMPLE 4 The graph of $r = 1 + \cos \theta$ is a cardioid. It is drawn in Figure $9 . 4 \mathrm { c }$ .

The cardioid has no simple $x y$ equation. Still the curve is very attractive. It has a cusp at the origin and it is heart-shaped (hence its name). To draw it, plot $r = 1 +$ cos $\theta$ at $3 0 ^ { \circ }$ intervals and connect the points. For this curve $r$ is never negative, since cos $\theta$ never goes below $^ { - 1 }$ :

It is a curious fact that the electrical vector in your heart almost traces out a cardioid. See Section 11.1 about electrocardiograms. If it is a perfect cardioid you are in a little trouble.

EXAMPLE 5 The graph of $r = 1 + b$ cos $\theta$ is a limaçon (a cardioid when $b = 1$ ).

Limaçon (soft $c$ ) is a French word for snail—not so well known as escargot but just as inedible. (I am only referring to the shell. Excusez-moi!) Figure 9.4 shows how a dimple appears as $b$ increases. Then an inner loop appears beyond $b = 1$ (the cardioid at $b = 1$ is giving birth to a loop). For large $b$ the curve looks more like two circles. The limiting case is a double circle, when the inner loop is the same as the outer loop. Remember that $r = \cos \theta$ goes around the circle twice.

We could magnify the limaçon by a factor $c$ ; changing to $r = c ( 1 + b \cos \theta )$ : We could rotate $1 8 0 ^ { \circ }$ to $r = 1 - b \cos \theta$ : But the real interest is whether these figures arise in applications, and Donald Saari showed me a nice example.

Mars seen from Earth The Earth goes around the Sun and so does Mars. Roughly speaking Mars is $1 \textstyle { \frac { 1 } { 2 } }$ times as far out, and completes its orbit in two Earth years.

We take the orbits as circles: $r = 2$ for Earth and $r = 3$ for Mars. Those equations tell where but not when. With time as a parameter, the coordinates of Earth and Mars are given at every instant $t$ :

$$
x _ { \mathrm { E } } = 2 \cos 2 \pi t , y _ { \mathrm { E } } = 2 \sin 2 \pi t \qquad { \mathrm { a n d } } \qquad x _ { \mathrm { M } } = 3 \cos \pi t , y _ { \mathrm { M } } = 3 \sin \pi t .
$$

At $t = 1$ year, the Earth completes a circle (angle $= 2 \pi$ ) and Mars is halfway. Now the keystep. Subtract to find the position of Mars relative to Earth:

$$
x _ { \mathrm { M - E } } = 3 \cos \pi t - 2 \cos 2 \pi t \qquad \mathrm { a n d } \qquad y _ { \mathrm { M - E } } = 3 \sin \pi t - 2 \sin 2 \pi t .
$$

Replacing cos $2 \pi t$ by $2 \cos ^ { 2 } \pi t - 1$ and sin $2 \pi t$ by 2 sin $\pi t$ cos $\pi t$ ; this is

$$
x _ { \mathrm { M - E } } = ( 3 - 4 \cos \pi t ) \cos \pi t + 2 \qquad \mathrm { a n d } \qquad y _ { \mathrm { M - E } } = ( 3 - 4 \cos \pi t ) \sin \pi t .
$$

Seen from the Earth, Mars does a loop in the sky! There are two $t$ ’s for which $3 - 4 \cos { \pi t } = 0$ (or cos $\begin{array} { r } { \pi t = \frac { 3 } { 4 } . } \end{array}$ ). At both times, Mars is two units from Earth $( x _ { \mathrm { M - E } } = 2$ and $y _ { \mathrm { M - E } } = 0$ ). When we move the origin to that point, the 2 is subtracted away—the $\mathbf { M } - \mathbf { E }$ coordinates become $x = r \cos \pi t$ and $y = r$ sin $\pi t$ with $r = 3 - 4 \cos \pi t$ : That is a limaçon with a loop, like Figure 9.4d.

Note added in proof I didn’t realize that a 3-to-2 ratio is also responsible for heating up two spots on opposite sides of Mercury. From the newspaper of June 13; 1990:

“Astronomers today reported the first observations showing that Mercury has two extremely hot spots. That is because Mercury, the planet closest to the Sun, turns on its axis once every 59:6 days, which is a day on Mercury. It goes around the sun every 88 days, a Mercurian year. With this 3-to-2 ratio between spin and revolution, the Sun appears to stop in the sky and move backward, describing a loop over each of the hot spots.”

# CONIC SECTIONS IN POLAR COORDINATES

The exercises include other polar curves, like lemniscates and 200-petal flowers. But get serious. The most important curves are the ellipse and parabola and hyperbola. In Section 3.5 their equations involved $1 , x , y , x ^ { 2 } , x y , y ^ { 2 }$ : With one focus at the origin, their polar equations are even better.

9A The graph of $r = A / ( 1 + e \cos \theta )$ is a conic section with “eccentricity” $e$ : circle if $e = 0$ ellipse if $0 < e < 1$ parabola if $e = 1$ hyperbola if $e > 1$ :

EXAMPLE 6 . $\displaystyle { \mathit { \tilde { e } } } = 1 { \mathit { \check { \Psi } } }$ / The graph of $r = 1 / ( 1 + \cos \theta )$ is a parabola. This equation is $r + r \cos \theta = 1$ or $r = 1 - x$ : Squaring both sides gives $\bar { x ^ { 2 } } + y ^ { 2 } = 1 - 2 \bar { x } + x ^ { 2 }$ : Canceling $x ^ { 2 }$ leaves $y ^ { 2 } = 1 - 2 x$ ; the parabola in Figure 9.5b.

The amplifying factor $A$ blows up all curves, with no change in shape.

EXAMPLE 7 . $\displaystyle { \mathit { \ell } } _ { e } = 2 { \mathit { \ell } } _ { , }$ / The same steps lead from $r ( 1 + 2 \cos \theta ) = 1$ to $r = 1 - 2 x$ : Squaring gives $x ^ { 2 } + y ^ { 2 } = 1 - 4 x + 4 x ^ { 2 }$ and the $x ^ { 2 }$ terms do not cancel. Instead we have $y ^ { 2 } - 3 x ^ { 2 } = 1 - 4 x .$ : This is the hyperbola in Figure 9.5c, with a focus at $( 0 , 0 )$ :

The hyperbola $y ^ { 2 } - 3 x ^ { 2 } = 1$ (without the $- 4 x )$ has its center at $( 0 , 0 )$ .

EXAMPLE 8 . $\begin{array} { r } { ( e = \frac { 1 } { 2 } ) } \end{array}$ The same steps lead from $\textstyle r ( 1 + { \frac { 1 } { 2 } } \cos \theta ) = 1$ to $\begin{array} { r } { r = 1 - \frac { 1 } { 2 } x } \end{array}$ : Squaring gives the ellipse $\scriptstyle x ^ { 2 } + y ^ { 2 } = 1 - x + { \frac { 1 } { 4 } } x ^ { 2 }$ : Polar equations look at conics in a new way, which happens to match the sun and planets perfectly. The sun at $( 0 , 0 )$ is not the center of the system, but a focus.

Finally $e = 0$ gives the circle $r = 1$ : Center of circle $= { \tt b o t h f o c i } = ( 0 , 0 ) \$ .

The directrix The figure shows the line $d$ (the “directrix”) for each curve. All points $P$ on the curve satisfy $r = | P F | = e | P d |$ : The distñance to the focus is e times the distance to the directrix. $\scriptstyle { \mathcal { e } }$ is still the eccentricity, nothing to do with exponentials.) A geometer would start from this property $r = e | P d |$ and const|ruct |the c|urve.| We derive the property from the equation:

$$
r = { \frac { A } { 1 + e \cos \theta } } \quad \Rightarrow \quad r + e x = A \quad \Rightarrow \quad r = e \left( { \frac { A } { e } } - x \right) .
$$

The directrix is the line at $x = A / e$ : That last equation is exactly $| P F | = e | P d |$ .

Notice how two numbers determine these curves. Here the numbers are $A$ and $e$ : In Section 3.5 they were $a$ and $b$ : (The ellipse was $x ^ { 2 } / a ^ { 2 } + y ^ { 2 } / b ^ { 2 } = 1 .$ ) Using $A$ and $e$ we go smoothly from ellipses through parabolas (at $e = 1$ ) and on to hyperbolas. With three more numbers we can move the focus to any point and rotate the curve through any angle. Conics are determined by five numbers.