# 2.3 The Slope and the Tangent Line

Chapter 1 started with straight line graphs. The velocity was constant (at least piecewise). The distance function was linear. Now we are facing polynomials like $\bar { x } ^ { 3 } - 2$ or $x ^ { 4 } - x ^ { 2 } + 3$ , with other functions to come soon. Their graphs are definitely curved. Most functions are not close to linear—except if you focus all your attention near a single point. That is what we will do.

Over a very short range a curve looks straight. Look through a microscop1e, or zoom in with a computer, and there is no doubt. The graph of distance versus time become1s nearly linear. Its slope is the velocity at that moment. We want to find the line that the graph stays closest to—the “tangent line”—before it curves away.

The tangent line is easy to describe. We are at a particular point on the graph of $y = f ( x )$ : At that point $x$ equals $a$ and $y$ equals $f ( a )$ and the slope equals $f ^ { \prime } ( a )$ : The tangent line goes through that point $x = a , y = f ( a )$ with that slope $m = f ^ { \prime } ( a )$ . Figure 2.5 shows the line more clearly than any equation, but we have to turn the geometry into algebra. We need the equation of the line.

EXAMPLE 1 Suppose $y = x ^ { 4 } - x ^ { 2 } + 3$ : At the point $x = a = 1$ , the height is $y = f ( a ) = 3$ : The slope is ${ d y } / { d x } = 4 x ^ { 3 } - 2 x$ : At $x = 1$ the slope is $4 - 2 = 2$ : That is $f ^ { \prime } ( a )$ :

The numbers $x = 1$ ; $y = 3$ ; $d y / d x = 2$ determine the tangent line.

The equation of the tangent line is $y - 3 = 2 ( x - 1 )$ , and this section explains why.

# THE EQUATION OF A LINE

A straight line is determined by two conditions. We know the line if we know two of its points. (We still have to write down the equation.) Also, if we know one point and the slope, the line is set. That is the situation for the tangent line, which has a known slope at a known point:

1. The equation of a line has the form $y = m x + b$   
2. The number $m$ is the slope of the line, because $d y / d x = m$   
3. The number $b$ adjusts the line to go through the required point.

I will take those one at a time—first $y = m x + b$ , then $m$ , then $b$ :

# 2.3 The Slope and the Tangent Line

1. The graph of $y = m x + b$ is not curved. How do we know ? For the specific example $y = 2 x + 1$ , take two points whose coordinates $x , y$ satisfy the equation:

$$
x = 0 , y = 1 \quad { \mathrm { a n d } } \quad x = 4 , y = 9 \quad { \mathrm { b o t h ~ s a t i s f y } } \quad y = 2 x + 1 .
$$

Those points $( 0 , 1 )$ and $( 4 , 9 )$ lie on the graph. The point halfway between has $x = 2$ and $y = 5$ . That point also satisfies $y = 2 x + 1$ : The halfway point is on the graph. If we subdivide again, the midpoint between $( 0 , 1 )$ and $( 2 , 5 )$ is $( 1 , 3 )$ : This also has $y = 2 x + 1$ : The graph contains all halfway points and must be straight.

2. What is the correct slope m for the tangent line ? In our example it is $m = f ^ { \prime } ( a ) = 2$ :

The curve and its tangent line have the same slope at the crucial point: $d y / d x = 2$ :

Allow me to say in another way why the line $y = m x + b$ has slope $m$ : At $x = 0$ its height is $y = b$ : At $x = 1$ its height is $y = m + b$ : The graph has gone one unit across .0 to 1/ and m units up . $\mathit { \Delta } _ { b }$ to $m + b$ /: The whole idea is

$$
{ \mathrm { s l o p e } } = { \frac { { \mathrm { d i s t a n c e ~ } } \operatorname* { u p } } { { \mathrm { d i s t a n c e ~ a c r o s s } } } } = { \frac { m } { 1 } } .
$$

Each unit across means $m$ units up, to $2 m + b$ or $3 m + b$ : A straight line keeps a constant slope, whereas the slope of $y = x ^ { 4 } - x ^ { 2 } + 3$ equals 2 only at $x = 1$ :

3. Finally we decide on $b$ : The tangent line $y = 2 x + b$ must go through $x = 1$ ; $y = 3$ : Therefore $b = 1$ : With letters instead ofnumbers, $y = m x + b$ leads to $f ( a ) = m a + b$ : So we know $b$ :

2E The equation of the tangent line has $b = f ( a ) - m a$ :

$$
y = m x + f ( a ) - m a \qquad { \mathrm { o r } } \qquad y - f ( a ) = m ( x - a ) .
$$

That last form is the best. You see immediately what happens at $x = a$ : The factor $x - a$ is zero. Therefore $y = f ( a )$ as required. This is the point-slope form of the equation, and we use it constantly:

$$
y - 3 = 2 ( x - 1 ) \quad { \mathrm { o r } } \quad { \frac { y - 3 } { x - 1 } } = { \frac { \mathrm { d i s t a n c e ~ u p } } { \mathrm { d i s t a n c e ~ a c r o s s } } } = { \mathrm { s l o p e ~ } } 2 .
$$

EXAMPLE 2 The curve $y = x ^ { 3 } - 2$ goes through $y = 6$ when $x = 2$ : At that point $d y / d x = 3 x ^ { 2 } = 1 2$ : The point-slope equation of the tangent line uses 2 and 6 and 12:

$$
y - 6 = 1 2 ( x - 2 ) \quad { \mathrm { w h i c h i s ~ a l s o } } \quad y = 1 2 x - 1 8 .
$$

There is another important line. It is perpendicular to the tangent line and perpendicular to thecurve. Thisis the normal line in Figure 2.6. Its new feature is its slope. When the tangent line has slope $m$ , the normal line has slope $- 1 / m$ : (Rule: Slopes of perpendicular lines multiply to give $^ { - 1 }$ :) Example 2 has $m = 1 2$ , so the normal line has slope $- 1 / 1 2$ :

$$
n g e n t l i n e ; ~ y - 6 = 1 2 ( x - 2 ) ~ n o r m a l l i n e ; ~ y - 6 = - \frac { 1 } { 1 2 } ( x - 2 ) .
$$

Light rays travel in the normal direction. So do brush fires—they move perpendicular to the fire line. Use the point-slope form! The tangent is $y = 1 2 x - 1 8$ , the normal is not $y = - { \textstyle { \frac { 1 } { 1 2 } } } x - 1 8$ :

# 2 Derivatives

EXAMPLE 3 You are on a roller-coaster whose track follows $y = x ^ { 2 } + 4$ : You see a friend at $( 0 , 0 )$ and want to get there quickly. Where do you step off ?

Solution Your path will be the tangent line (at high speed). The problem is to choose $x = a$ so the tangent line passes through $x = 0 , y = 0$ :When you step off at $x = a$ , the height is $y = a ^ { 2 } + 4$ and the slope is $2 a$ the equation of the tangent line is $y - ( a ^ { 2 } + 4 ) = 2 a ( x - a )$ this line goes through $( 0 , 0 )$ if $- ( a ^ { 2 } + 4 ) = - 2 a ^ { 2 }$ or $a = \pm 2$ :



The same problem is solved by spacecraft controllers and baseball pitchers. Releasing a ball at the right time to hit a target 60 feet away is an amazing display of calculus. Quarterbacks with a moving target should read Chapter 4 on related rates.

Here is a better example than a roller-coaster. Stopping at a red light wastes gas. It is smarter to slow down early, and then accelerate. When a car is waiting in front of you, the timing needs calculus:

EXAMPLE 4 How much must you slow down when a red light is 72 meters away ? In 4 seconds it will be green. The waiting car will accelerate at 3 meters= $\sec ^ { 2 }$ : You cannot pass the car.

Strategy Slow down immediately to the speed $V$ at which you will just catch that car. (If you wait and brake later, your speed will have to go below $V .$ ) At the catchup time $T$ , the cars have the same speed and same distance. Two conditions, so the distance functions in Figure 2.6d are tangent.

Solution At time $T$ , the other car’s speed is $3 ( T - 4 )$ : That shows the delay of 4 seconds. Speeds are equal when $3 ( T - 4 ) = V$ or $\begin{array} { r } { T = \frac { 1 } { 3 } V + 4 } \end{array}$ : Now require equal distances. Your distance is $V$ times $T .$ The other car’s distance is $7 2 + { \textstyle { \frac { 1 } { 2 } } } a t ^ { 2 }$ :

$$
\begin{array} { r } { 7 2 + \frac { 1 } { 2 } \cdot 3 ( T - 4 ) ^ { 2 } = V T \quad \mathrm { b e c o m e s } \quad 7 2 + \frac { 1 } { 2 } \cdot \frac { 1 } { 3 } V ^ { 2 } = V \left( \frac { 1 } { 3 } V + 4 \right) . } \end{array}
$$

The solution is $V = 1 2$ meters=second. This is $4 3 \mathrm { k m / h r }$ or 27 miles per hour.

Without the other car, you only slow down to $V = 7 2 / 4 = 1 8$ meters=second. As the light turns green, you go through at $6 5 \mathrm { k m / h r }$ or 40 miles per hour. Try it.

# 2.3 The Slope and the Tangent Line

# THE SECANT LINE CONNECTING TWO POINTS ON A CURVE

Instead of the tangent line through one point, consider the secant line through two points. For the tangent line the points came together. Now spread them apart. The point-slope form of a linear equation is replaced by the two-point form.

The equation of the curve is still $y = f ( x )$ : The first point remains at $x = a$ ; $y = f ( a )$ : The other point is at $x = c , y = f ( c )$ : The secant line goes between them, and we want its equation. This time we don’t start with the slope—but $m$ is easy to find.

EXAMPLE 5 The curve $y = x ^ { 3 } - 2$ goes through $x = 2 , y = 6 .$ It also goes through $x = 3 , y = 2 5$ : The slope between those points is

$$
m = { \frac { \mathrm { c h a n g e ~ i n ~ } y } { \mathrm { c h a n g e ~ i n ~ } x } } = { \frac { 2 5 - 6 } { 3 - 2 } } = 1 9 .
$$

The point-slope form (at the first point) is $y - 6 = 1 9 ( x - 2 )$ : This line automatically goes through the second point .3; 25/: Check: $2 5 - 6$ equals $1 9 ( 3 - 2 )$ : The secant has the right slope 19 to reach the second point. It is the average slope $\Delta y / \Delta x$ .

A look ahead The second point is going to approach the first point. The secant slope $\Delta y / \Delta x$ will approach the tangent slope $d y / d x$ : We discover the derivative (in the limit). That is the main point now—but not forever.

Soon you will be fast at derivatives. The exact $d y / d x$ will be much easier than $\Delta y / \Delta x$ : The situation is turned around as soon as you know that $x ^ { 9 }$ has slope $9 { x ^ { 8 } }$ : Near $x = 1$ , the distance up is about 9 times the distance across. To find $\Delta y = 1 . 0 0 1 ^ { 9 } - 1 ^ { 9 }$ , just multiply $\Delta x = . 0 0 1$ by 9: The quick approximation is :009, the calculator gives $\Delta y = . 0 0 9 0 3 6$ : It is easier to follow the tangent line than the curve.

Come back to the secant line, and change numbers to letters. What line connects $x = a , y = f ( a )$ to $x = c , y = f ( c ) ?$ A mathematician puts formulas ahead of numbers, and reasoning ahead of formulas, and ideas ahead of reasoning:

(1) The slope is $m = { \frac { \mathrm { d i s t a n c e ~ u p } } { \mathrm { d i s t a n c e ~ a c r o s s } } } = { \frac { f ( c ) - f ( a ) } { c - a } }$ (2) The height is $y = f ( a )$ at $x = a$ (3) The height is $y = f ( c )$ at $x = c$ (automatic with correct slope).

2F The two-point form uses the slope between the points: $s e c a n t l i n e : \quad y - f ( a ) = \left( { \frac { f ( c ) - f ( a ) } { c - a } } \right) ( x - a ) .$

At $x = a$ the right side is zero. So $y = f ( a )$ on the left side. At $x = c$ the right side has two factors $c - a$ : They cancel to leave $y = f ( c )$ : With equation (2) for the tangent line and equation (3) for the secant line, we are ready for the moment of truth.

# THE SECANT LINE APPROACHES THE TANGENT LINE

What comes now is pretty basic. It matches what we did with velocities:

$$
{ \mathrm { a v e r a g e ~ v e l o c i t y } } = { \frac { \Delta { \mathrm { ~ d i s t a n c e } } } { \Delta { \mathrm { ~ t i m e } } } } = { \frac { f ( t + \Delta t ) - f ( t ) } { \Delta t } } .
$$

The limit is $d f / d t$ : We now do exactly the same thing with slopes. The secant line turns into the tangent line as $c$ approaches $a$ :

$$
\begin{array} { l l } { { \mathrm { s l o p e ~ o f ~ s e c a n t ~ l i n e } ; ~ } } & { { \displaystyle \frac { \Delta f } { \Delta x } = \frac { f ( c ) - f ( a ) } { c - a } } } \\ { { \mathrm { s l o p e ~ o f ~ t a n g e n t ~ l i n e } ; ~ } } & { { \displaystyle \frac { d f } { d x } = \mathrm { l i m i t ~ o f ~ } \frac { \Delta f } { \Delta x } . } } \end{array}
$$

There stands the fundamental idea of differential calculus! You have to imagine more secant lines than I can draw in Figure 2.7, as $c$ comes close to $a$ : Everybody recognizes $c - a$ as $\Delta x$ : Do you recognize $f ( c ) - f ( a )$ as $f ( x + \Delta x ) - f ( x ) ^ { \ast }$ ? It is $\Delta f$ , the change in height. All lines go through $x = a , y = f ( a )$ : Their limit is the tangent line.

$$
\mathbf { \Psi } _ { f ( c ) } ^ { f ( c ) } \equiv \underbrace { \sum _ { i } ^ { \cdots } \sum _ { c } ^ { \Delta x } } _ { \textit { f ( a ) } } \underbrace { \mathrm { s e c a n t } } _ { \textit { s c c } } \underbrace { \mathrm { s e c a n t } } _ { \textit { s e c a n t } } \underbrace { \mathrm {  ~ \Psi ~ } _ { y } - f ( a ) = \frac { f ( c ) - f ( a ) } { c - a } ( x - a ) } _ { \textit { t a n g e n t } } \underbrace { \mathrm {  ~ \Psi ~ } _ { y } - f ( a ) = f ^ { \prime } ( a ) ( x - a ) } _ { \textit { s p - f } ( a ) = f ^ { \prime } ( a ) ( x - a ) }
$$

Intuitively, the limit is pretty clear. The two points come together, and the tangent line touches the curve at one point. (It could touch again at faraway points.) Mathematically this limit can be trickyÑ—it takesus from algebra to calculus. Algebra stays away from $0 / 0$ , but calculus gets as close as it can.

The new limit for $d f / d x$ looks different, but it is the same as before:

$$
f ^ { \prime } ( a ) = \operatorname* { l i m } _ { c \to a } { \frac { f ( c ) - f ( a ) } { c - a } } .
$$

EXAMPLE 6 Find the secant lines and tangent line for $y = f ( x ) = \sin { x }$ at $x = 0$ :

The starting point is $x = 0 , y = \sin \mathrm { 0 }$ : This is the origin $( 0 , 0 )$ : The ratio of distance up to distance across is $( \sin c ) / c$ :

$$
e q u a t i o n \quad y = { \frac { \sin c } { c } } x \qquad t a n g e n t e q u a t i o n \quad y = 1 x .
$$

As $c$ approaches zero, the secant line becomes the tangent line. The limit of $( \sin c ) / c$ is not $0 / 0$ , which is meaningless, but 1; which is $d y / d x$ :

EXAMPLE 7 The gold you own will be worth $\sqrt { t }$ million dollars in $t$ years. When does the rate of increase drop to $10 \%$ of the current value, so you should sell the gold and buy a bond ? At $t = 2 5$ , how far does that put you ahead of $\sqrt { t } = 5 ?$

# 2.3 The Slope and the Tangent Line

Solution The rate of increase is the derivative of $\sqrt { t }$ , which is $1 / 2 { \sqrt { t } }$ : That is $10 \%$ of the current value $\sqrt { t }$ when $1 / 2 \sqrt { t } = \sqrt { t } / 1 0$ : Therefore $2 t = 1 0$ or $t = 5$ : At that time yo?u sell the gold, leave the curve, and go onto the tangent line:

$$
y - { \sqrt { 5 } } = { \frac { \sqrt { 5 } } { 1 0 } } \left( t - 5 \right) \quad { \mathrm { b e c o m e s } } \quad y - { \sqrt { 5 } } = 2 { \sqrt { 5 } } \quad { \mathrm { a t } } \quad t = 2 5 .
$$

With straight interest on the bond, not compounded, you have reached $y = 3 { \sqrt { 5 } } = 6 . 7$ million dollars. The gold is worth a measly five million.