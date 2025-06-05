# 13.2 Partial Derivatives

The central idea of differential calculus is the derivative. A change in $x$ produces a change in $f$ . The ratio $\Delta f / \Delta x$ approaches the derivative, or slope, or rate of change. What to do if $f$ depends on both $x$ and $y$ ?

The new idea isBto vary $x$ and $y$ one at a time. First, only $x$ moves. If the function is $x + x y$ , then $\Delta f$ is $\Delta x + y \Delta x$ Ñ. The ratio $\Delta f / \Delta x$ is $1 + y$ . The “ $x$ derivative” of $x + x y$ is $1 + y$ . For all functions the method is the same: Keep $y$ constant, change $x$ , take the limit of $\Delta f / \Delta x$ :

# DEFINITION

$$
{ \frac { \partial f } { \partial x } } ( x , y ) = \operatorname* { l i m } _ { \Delta x \to 0 } { \frac { \Delta f } { \Delta x } } = \operatorname* { l i m } _ { \Delta x \to 0 } { \frac { f ( x + \Delta x , y ) - f ( x , y ) } { \Delta x } } .
$$

On the left is a new symbol $\partial f / \partial x$ . It signals tBhat only $x$ is allowed to vary— $\partial f / \partial x$ is a partial derivative. The different form $\partial$ of the same letter (still say $^ { \cdot \cdot } d ^ { \cdot \cdot } )$ ) is a reminder that $x$ is not the only variable. Another variable $y$ is presentBbut  Bnot moving.

$$
f ( x , y ) = x ^ { 2 } y ^ { 2 } + x y + y \quad { \frac { \partial f } { \partial x } } ( x , y ) = 2 x y ^ { 2 } + y + 0 .
$$

Do not treat $y$ as zero! Treat it as a cBonst aBnt, like 6. Its $x$ derivative is zero. If $f ( x ) = \sin { 6 x }$ then $d f / d x = 6$ cos $6 x$ . If $f ( x , y ) = \sin { x y }$ then $\partial f / \partial x = y \cos x y$

Spoken aloud, $\partial f / \partial x$ is still $\operatorname { \mathfrak { s } } d f d \ v { x }$ :” It is a function of $x$ and $y$ . When more is needed, call it “the partial of $f$ with respect to $x$ .” The symbol $f ^ { \prime }$ is no longer availablBe, since it gives no special indication abBout $x$ . Its replacement $f _ { x }$ is pronounced “ $f x ^ { , , }$ oBr $^ { 6 6 } f$ sub $x$ ,” which is shorter than $\partial f / \partial x$ and means the sameBthing.

We may also want to indicate the point $( x _ { 0 } , y _ { 0 } )$ where the derivative is computed:

$$
 \frac { \partial f } { \partial x } ( x _ { 0 } , y _ { 0 } ) \quad \mathrm { o r } \quad f _ { x } ( x _ { 0 } , y _ { 0 } ) \quad \mathrm { o r } \quad  \frac { \partial f } { \partial x } | _ { ( x _ { 0 } , y _ { 0 } ) } \quad \mathrm { o r j u s t } \quad ( \frac { \partial f } { \partial x } ) _ { 0 } .
$$

EXAMPLE 2 $f ( x , y ) = \sin 2 x \cos y \quad f _ { x } = 2 \cos 2 x \cos y$ (cos $y$ is constant for $\partial / \partial x )$

The particular point $( x _ { 0 } , y _ { 0 } )$ is $( 0 , 0 )$ . The height of thesurface is $f ( 0 , 0 ) = 0$ . The slope in the $x$ direction is $f _ { x } = 2$ . At a different point $x _ { 0 } = \pi$ ; $y _ { 0 } = \pi$ we find $f _ { x } ( \pi , \pi ) = - 2$ .

Now keep $x$ constant and vary $y$ . The ratio $\Delta f / \Delta y$ approaches $\partial f / \partial y$ :

$$
f _ { y } ( x , y ) = \operatorname* { l i m } _ { \Delta y \to 0 } \frac { \Delta f } { \Delta y } = \operatorname* { l i m } _ { \Delta y \to 0 } \frac { f ( x , y + \Delta y ) - f ( x , y ) } { \Delta y } .
$$

This is the slope in the $y$ direction. PleaBse realize that a surface cBan go up in the $x$ direction and down in the $y$ direction. The plane $f ( x , y ) = 3 x - 4 y$ has $f _ { x } = 3$ (up) and $f _ { y } = - 4$ (down). We will soon ask what happens in the $4 5 ^ { \circ }$ direction.

EXAMPLE 3 $f ( x , y ) = { \sqrt { x ^ { 2 } + y ^ { 2 } } } \quad { \frac { \partial f } { \partial x } } = { \frac { x } { \sqrt { x ^ { 2 } + y ^ { 2 } } } } = { \frac { x } { f } } \quad { \frac { \partial f } { \partial y } } = { \frac { y } { \sqrt { x ^ { 2 } + y ^ { 2 } } } } =$ ${ \frac { y } { f } } .$

The $x$ derivative of $\sqrt { x ^ { 2 } + y ^ { 2 } }$ is really one-variable calculus, because $y$ is constant. The exponent drops from $\frac { 1 } { 2 }$ to $- \frac { 1 } { 2 }$ , and there is $2 x$ from the chain rule. This distance function has the curious derivative $\partial f / \partial x = x / f$ .

The graph is a cone. Above the point $( 0 , 2 )$ the height is ${ \sqrt { 0 ^ { 2 } + 2 ^ { 2 } } } = 2$ . The partial derivatives are $f _ { x } = 0 / 2$ and $f _ { y } = 2 / 2$ . At that point, Figure 13.5 climbs in the $y$ direction. It is level in the $x$ direction. An actual step $\Delta x$ will increase $0 ^ { 2 } + 2 ^ { 2 }$ to $( \Delta x ) ^ { 2 } + 2 ^ { 2 }$ . But this change is of order $( \Delta x ) ^ { 2 }$ and the $x$ derivative is zero.

Figure 13.5 is rather important. It shows how $\partial f / \partial x$ and $\partial f / \partial y$ are the ordinary derivatives of $f ( x , y _ { 0 } )$ and $f ( x _ { 0 } , y )$ . It is natural to call these partial functions. The first has $y$ fixed at $y _ { 0 }$ while $x$ varies. The second has $x$ fixed at $x _ { 0 }$ while $y$ varies. Their graphs are cross sections down the surface —cut out by the vertical planes $y = y _ { 0 }$ and $x = x _ { 0 }$ . Remember that the level curve is cut out by the horizontal plane $z = c$ .

The limits of $\Delta f / \Delta x$ and $\Delta f / \Delta y$ are computed as always. With partial functions we are back to a single variable. The partial derivative is the ordinary derivative of a partialBfun cBtion (constant $y$ or constant $x$ ). For the cone, $\partial f / \partial y$ exists at all points except $( 0 , 0 )$ . The figure shows how the cross section down the middle of the cone produces the absolute value function: $f ( 0 , y ) = | y |$ . It has one-sided derivatives but not a two-sided derivative.

Similarly $\partial f / \partial x$ will not exist at the sharp point of the cone. We develop the idea of a continuous function $f ( x , y )$ as needed (the definition is in the exercises). Each partial derivative involves one direction, but limits and continuity involve all directions. The distance function is continuous at $( 0 , 0 )$ , where it is not differentiable.

$$
f ( x , y ) = y ^ { 2 } - x ^ { 2 } \quad \hat { \sigma } f / \partial x = - 2 x \quad \hat { \sigma } f / \partial y = 2 y
$$

Move in the $x$ direction from $( 1 , 3 )$ . Then $y ^ { 2 } - x ^ { 2 }$ has the partial function $9 - x ^ { 2 }$ . With $y$ fixed at 3, a parabola opens downward. In the $y$ direction (along $x = 1$ ) the partial function $y ^ { 2 } - 1$ opens upward. The surface in Figure 13.6 is called a hyperbolic paraboloid, because the level curves $y ^ { 2 } - x ^ { 2 } = c$ are hyperbolas. Most people call it a saddle, and the special point at the origin is a saddle point. The origin is special for $y ^ { 2 } - x ^ { 2 }$ because both derivatives are zero. The bottom of the $y$ parabola at $( 0 , 0 )$ is the top of the $x$ parabola. The surface is momentarily flat in all directions. It is the top of a hill and the bottom of a mountain range at the same time. A saddle point is neither a maximum nor a minimum, although both derivatives are zero.

Note Do not think that $f ( x , y )$ must contain $y ^ { 2 }$ and $x ^ { 2 }$ to have a saddle point. The function $2 x y$ does just as well. The level curves $2 x y = c$ are still hyperbolas. The partial functions $2 x y _ { 0 }$ and $2 x _ { 0 } y$ now give straight lines—which is remarkable. Along the $4 5 ^ { \circ }$ line $x = y$ , the function is $2 x ^ { 2 }$ and climbing. Along the $- 4 5 ^ { \circ }$ line $x = - y$ , the function is $- 2 x ^ { 2 }$ and falling. The graph of $2 x y$ is Figure 13.6 rotated by $4 5 ^ { \circ }$ .



$$
f ( x , y , z ) = x ^ { 2 } + y ^ { 2 } + z ^ { 2 } \quad P ( T , V ) = n R T / V
$$

Example 5 shows more variables. Example 6 shows that the variables may not be named $x$ anBd $y$ . BAlso, the function may not be named $f$ ! Pressure and temperature and volume are $P$ and $T$ and $V$ . The letters change but nothing else:

$$
\hat { \sigma } P / \hat { \sigma } T = n R / V \quad \hat { \sigma } P / \hat { \sigma } V = - n R T / V ^ { 2 } \quad \mathrm { ( n o t e ~ t h e ~ d e r i v a t i v e ~ o f ~ } 1 / V \mathrm { ) } .
$$

There is no $\partial P / \partial R$ because $R$ is a constant from chemistry—not a variable.

Physics produces six variables for a moving body—the coordinates $x , y , z$ and the momenta $p _ { x } , p _ { y } , p _ { z }$ . Economics and the social sciences do better than that. If there are 26 products there are 26 variables—sometimes 52, to show prices as well as amounts. The profit can be a complicated function of these variables. The partial derivatives are the marginal profits, as one of the 52 variables is changed. A spreadsheet shows the 52 values and the effect of a change. An infinitesimal spreadsheet shows the derivative.

# SEBCON BD BDERIVABTIVE

Genius is not essential, to move to second derivatives. The only difficulty is that two first derivatives $f _ { x }$ and $f _ { y }$ lead to four second derivatives $f _ { x x }$ and $f _ { x y }$ and $f _ { y x }$ and $f _ { y y }$ . (Two subscripts: $f _ { x x }$ is the $x$ derivative of the $x$ derivative. Other notations are $\partial ^ { 2 } f / \partial x ^ { 2 }$ and $\partial ^ { 2 } f / \partial x \partial y$ and $\partial ^ { 2 } f / \partial y \partial x$ and $\partial ^ { 2 } f / \partial y ^ { 2 } .$ .) Fortunately $f _ { x y }$ equals $f _ { y x }$ , as we see first by example.

EXAMPLE 7 $f = x / y$ has $f _ { x } = 1 / y$ , which has $f _ { x x } = 0$ and $f _ { x y } = - 1 / y ^ { 2 }$ . The function $x / y$ is linear in $x$ (which explains $f _ { x x } = 0 ) ,$ ). Its $y$ derivative is $f _ { y } =$ $- x / y ^ { 2 }$ . This has the $x$ derivative $f _ { y x } = - 1 / y ^ { 2 }$ . The mixed derivatives $f _ { x y }$ and $f _ { y x }$ are equal.

In the pure $y$ direction, the second derivative is $f _ { y y } = 2 x / y ^ { 3 }$ . One-variable calculus is sufficient for all these derivatives, because only one variable is moving.

EXAMPLE 8 $f = 4 x ^ { 2 } + 3 x y + y ^ { 2 }$ has $f _ { x } = 8 x + 3 y$ and $f _ { y } = 3 x + 2 y$ . Both “cross derivatives” $f _ { x y }$ and $f _ { y x }$ equal 3. The second derivative in the $x$ direction is $\partial ^ { 2 } f / \partial x ^ { 2 } = 8$ or $f _ { x x } = 8$ . Thus “ $f x x ^ { , , , }$ is $^ { * } d$ second $f d x$ squared.” Similarly $\partial ^ { 2 } f / \partial y ^ { 2 } = 2$ . The only change is from $d$ to $\partial$ .

If $f ( x , y )$ has continuous second derivatives then $f _ { x y } = f _ { y x }$ . Problem43 sketches a proof basedon the Mean Value Theorem. For third derivatives almost any example shows that $f _ { x x y } = f _ { x y x } = f _ { y x x }$ is different from $f _ { y y x } = f _ { y x y } = f _ { x y y }$ .

Question How do you plot a space curve $x ( t ) , y ( t ) , z ( t )$ in a plane? One way is to look parallel to the direction $( 1 , 1 , 1 )$ . On your $X Y$ screen, plot $X = ( y - x ) / { \sqrt { 2 } }$ and $Y = ( 2 z - x - y ) / \sqrt { 6 }$ . The line $x = y = z$ goes to the point $( 0 , 0 )$ !

How do you graph a surface $z = f ( x , y ) ?$ Use the same $X$ and $Y$ . Fix $x$ and let $y$ vary, for curves one way in the surface. Then fix $y$ and vary $x$ , for the other partial function. For a parametric surface like $x = ( 2 + v \sin \textstyle { \frac { 1 } { 2 } } u ) \cos u$ , $y = ( 2 + v \sin \frac { 1 } { 2 } u )$ sin $u$ , $\begin{array} { r } { z = v \cos { \frac { 1 } { 2 } } u } \end{array}$ , vary $u$ and then $v$ . Dick Williamson showed how this draws a one-sided “Möbius strip.”