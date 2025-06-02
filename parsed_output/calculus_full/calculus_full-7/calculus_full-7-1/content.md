# 7.1 Integration by Parts

There are two major ways to manipulate integrals (with the hope of making them easier). Substitutions are based on the chain rule, and more are ahead. Here we present the other method, based on the product rule. The reverse of the product rule, to find integrals not derivatives, is integration by parts.

We have mentioned $\int \cos ^ { 2 } x d x$ and $\int \ln x d x$ . Now is the right time to compute them (plus more examples). You will see how $\int \ln x d x$ is exchanged for $\int 1 d x -$ a definite improvement. Also $\int x e ^ { x } d x$ is exchanged for $\int e ^ { x } d x$ . The difference between the harder integral and the easier integral is a known term—that is the point.

One note before starting: Integration by parts is not just a trick with no meaning. On the contrary, it expresses basic physical laws of equilibrium and force balance. It is a foundation for the theory of differential equations (and even delta functions). The final paragraphs, which are completely optional, illustrate those points too.

We begin with the product rule for the derivative of $u ( x )$ times $v ( x )$ :

$$
u ( x ) { \frac { d v } { d x } } + v ( x ) { \frac { d u } { d x } } = { \frac { d } { d x } } ( u ( x ) v ( x ) ) .
$$

Integrate both sides. On the right, integration brings back $u ( x ) v ( x )$ . On the left are two integrals, and one of them moves to the other side (with a minus sign):

$$
\int u ( x ) { \frac { d v } { d x } } d x = u ( x ) v ( x ) - \int v ( x ) { \frac { d u } { d x } } d x .
$$

That is the key to this section—not too impressive at first, but very powerful. It is integration by parts ( $u$ and $v$ are the parts). In practice we write it without $x$ ’s:

7A The integration by parts formula is $\textstyle \int u d v = u v - \int v d u .$

The problem of integrating $u d v / d x$ is changed into the problem of integrating $v d u / d x$ . There is a minus sign to remember, and there is the “integrated term” $u ( x ) v ( x )$ . In the definite integral, that product $u ( x ) v ( x )$ is evaluated at the endpoints $a$ and $b$ :

$$
\int _ { a } ^ { b } u { \frac { d v } { d x } } d x = u ( b ) v ( b ) - u ( a ) v ( a ) - \int _ { a } ^ { b } v { \frac { d u } { d x } } d x .
$$

The key is in choosing $u$ and $v$ .The goal of that choice is to make $\int v d u$ easier than $\int u d v$ . This is best seen by examples.

EXAMPLE 1 For $\int \ln x d x$ choose $u = \ln x$ and $d v = d x$ (so $v = x$ ):

$$
\int \ln x d x = u v - \int v d u = x \ln x - \int x { \frac { 1 } { x } } d x .
$$

I used the basic formula (3). Instead of working with $\ln x$ (searching for an antiderivative), we now work with the right hand side. There $x$ times $1 / x$ is 1. The integral of 1 is $x$ . Including the minus sign and theintegrated term $u v = x$ ln $x$ and the constant $C$ , the answer is

$$
\textstyle \int \ln x d x = x \ln x - x + C .
$$

For safety, take the derivative. The product rule gives ln $x + x ( 1 / x ) - 1$ , which is ln $x$ . The area under $y = \ln x$ from 2 to 3 is $3 \ln 3 - 3 - 2 \ln 2 + 2$ .

To repeat: We exchanged the integral of ln $x$ for the integral of 1.

EXAMPLE 2 For r $\mathbf { \dot { \theta } } _ { x \cos x \ d x }$ choose $u = x$ and $d v = \cos x d x$ (so $v ( x ) = \sin { x } ,$ ):

$$
\textstyle { \int } x \cos x d x = u v - \int v d u = x \sin x - \int \sin x d x .
$$

Again the right side has a simple integral, which completes the solution:

$$
\textstyle { \int { x \cos x d x } = x \sin x + \cos x + C . }
$$

Note The new integral is not always simpler. We could have chosen $u = \cos { x }$ and $d v = x d x$ . Then $\textstyle v = { \frac { 1 } { 2 } } x ^ { 2 }$ . Integration using those parts give the true but useless result

$$
\begin{array} { r } { \int x \cos x d x = u v - \int v d u = \frac 1 2 x ^ { 2 } \cos x + \int \frac 1 2 x ^ { 2 } \sin x d x . } \end{array}
$$

The last integral is harder instead of easier $\cdot x ^ { 2 }$ is worse than $x$ ). In the forward direction this is no help. But in the opposite direction it simplifies $\textstyle \int { \frac { 1 } { 2 } } x ^ { 2 } \sin x d x$ . The idea in choosing $u$ and $v$ is this: Try to give u a nice derivative and $d v$ a nice integral.

EXAMPLE 3 For $\int ( \cos x ) ^ { 2 } d x$ choose $u = \cos x$ and $d v = \cos x d x$ (s $) v = \sin { x }$ ):

$$
\begin{array} { r } { \int ( \cos x ) ^ { 2 } d x = u v - \int v d u = \cos x \sin x + \int ( \sin x ) ^ { 2 } d x . } \end{array}
$$

The integral of $( \sin x ) ^ { 2 }$ is no better and no worse than the integral of $( \cos x ) ^ { 2 }$ . But we never see $( \sin x ) ^ { 2 }$ without thinking of $1 - ( \cos x ) ^ { 2 }$ . So substitute for $( \sin x ) ^ { 2 }$ :

$$
\begin{array} { r } { \int ( \cos x ) ^ { 2 } d x = \cos x \sin x + \int 1 d x - \int ( \cos x ) ^ { 2 } d x . } \end{array}
$$

The last integral on the right joins its twin on the left, and $\textstyle \int 1 d x = x$ :

$$
2 \int ( \cos x ) ^ { 2 } d x = \cos x \ \sin x + x .
$$

Dividing by 2 gives the answer, which is definitely not ${ \scriptstyle { \frac { 1 } { 3 } } } ( \cos x ) ^ { 3 }$ . Add any $C$ :

$$
\textstyle \int ( \cos x ) ^ { 2 } d x = { \frac { 1 } { 2 } } ( \cos x \sin x + x ) + C .
$$

Question Integrate $( \cos x ) ^ { 2 }$ from 0 to $2 \pi$ . Why should the area be $\pi$ ?

Answer The definite integral is ${ \scriptstyle { \frac { 1 } { 2 } } } ( \cos x \sin x + x ) \Big ] _ { 0 } ^ { 2 \pi }$ .This does give $\pi$ . That area can also be found by common sense, starting from $( \cos x ) ^ { 2 } + ( \sin x ) ^ { 2 } = 1$ . The area under 1 is $2 \pi$ . The areas under $( \cos x ) ^ { 2 }$ and $( \sin x ) ^ { 2 }$ are the same. So each one is $\pi$ .

EXAMPLE 4 Ev»aluate $\int \tan ^ { - 1 } x d x$ by choosing $u = \tan ^ { - 1 } x$ and $v = x$ :

$$
\int \tan ^ { - 1 } { x } d x = u v - \int v d u = x \tan ^ { - 1 } { x } - \int x { \frac { d x } { 1 + x ^ { 2 } } } .
$$

The last integral has $w = 1 + x ^ { 2 }$ below and almost has $d w = 2 x d x$ above:

$$
\int { \frac { x d x } { 1 + x ^ { 2 } } } = { \frac { 1 } { 2 } } \int { \frac { d w } { w } } = { \frac { 1 } { 2 } } \ln w = { \frac { 1 } { 2 } } \ln ( 1 + x ^ { 2 } ) .
$$

Substituting back into (9) gives $\int \tan ^ { - 1 } x d x$ as $x \tan ^ { - 1 } x - { \textstyle { \frac { 1 } { 2 } } } \ln ( 1 + x ^ { 2 } )$ . All the familiar inverse functions can be integrated by parts (take $v = x$ , and add “ $+ C ^ { , , }$ at the end).

Our final example shows how two integrations by parts may be needed, when the first one only simplifies the problem half way.

EXAMPLE 5 For $\int x ^ { 2 } e ^ { x } d x$ choose $u = x ^ { 2 }$ and $d v = e ^ { x } d x$ ( $\operatorname { s o } v = e ^ { x }$ ):

$$
\begin{array} { r } { \int x ^ { 2 } e ^ { x } d x = u v - \int v d u = x ^ { 2 } e ^ { x } - \int e ^ { x } ( 2 x d x ) . } \end{array}
$$

The last integral involves $x e ^ { x }$ . This is better than $x ^ { 2 } e ^ { x }$ , but it still needs work:

$$
\begin{array} { r } { \int x e ^ { x } d x = u v - \int v d u = x e ^ { x } - \int e ^ { x } d x \quad ( \mathrm { n o w } u = x ) . } \end{array}
$$

Finally $e ^ { x }$ is alone. After two integrations by parts, we reach $\int e ^ { x } d x$ . In equation (11), the integral of $x e ^ { x }$ is $x e ^ { x } - e ^ { x }$ . Substituting back into (10),

$$
\begin{array} { r } { \int x ^ { 2 } e ^ { x } d x = x ^ { 2 } e ^ { x } - 2 \left[ x e ^ { x } - e ^ { x } \right] + C . } \end{array}
$$

# These five examples are in the list of prime candidates for integration by parts:

$$
x ^ { n } e ^ { x } , \ x ^ { n } \sin x , \ x ^ { n } \cos x , \ x ^ { n } \ln x , \ e ^ { x } \sin x , \ e ^ { x } \cos x , \ \sin ^ { - 1 } x , \ \tan ^ { - 1 } x , \ \dots
$$

This concludes the presentation of the method—brief and straightforward. Figure 7.1a shows how the areas $\int u d v$ and $\int v d u$ fill out the difference between the big area $u ( b ) v ( b )$ and the smaller area $u ( a ) v ( a )$ .

In the movie Stand and Deliver, the Los Angeles teacher Jaime Escalante computed $\int x ^ { 2 } \sin x d x$ with two integrations by parts. His success was through exercises—plus insight in choosing $u$ and $v$ . (Notice the difference from $\int x \sin x ^ { 2 } d x$ That falls the other way—to a substitution.) The class did extremely well on the Advanced Placement Exam. If you saw the movie, you remember that the examiner didn’t believe it was possible. I spoke to him long after, and he confirms that practice was the key.

# THE DELTA FUNCTION

From the most familiar functions we move to the least familiar. The delta function is the derivative of a step function. The step function $U ( x )$ jumps from 0 to 1 at $x = 0$ . We write $\boldsymbol { \delta } ( \boldsymbol { x } ) = d \boldsymbol { U } / d \boldsymbol { x }$ , recognizing as we do it that there is no genuine derivative at the jump. The delta function is the limit of higher and higher spikes— from the “burst of speed” in Section 1.2. They approach an infinite spike concentrated at a single point (where $U$ jumps). This “non-function” may be unconventional—it is certainly optional»—but it is import»ant enough to come back to.

The slope $d U / d x$ is zero except at $x = 0$ , where the step function jumps. Thus $\ \delta ( x ) = 0$ except at that one point, where the delta function has a “spike.” We cannot give a value for $\delta$ at $x = 0$ , but $_ { w e }$ know its integral across the jump. On every interval from $- A$ to $A$ , the integral of $d U / d x$ brings back $U$ :

$$
\int _ { - A } ^ { A } \delta ( x ) d x = \int _ { - A } ^ { A } { \frac { d U } { d x } } d x = U ( x ) \big ] _ { - A } ^ { A } = 1 .
$$

“The area under the infinitely tall and infinitely thin spike $\delta ( x )$ equals 1.”

# 7.1 Integration by Parts

So far so good. The integral of $\delta ( x )$ is $U ( x )$ . We now integrate by parts for a crucial purpose—to find the area under $v ( x ) \delta ( x )$ . This is an ordinary function times the delta function. In some sense $v ( x )$ times $\delta ( x )$ equals $v ( 0 )$ times $\delta ( x )$ —because away from $x = 0$ the product is always zero. Thus $e ^ { x } \delta ( x )$ equals $\delta ( x )$ , and sin $x \ : \delta ( x ) = 0$ .

The area under $v ( x ) \delta ( x )$ is $v ( 0 )$ —which integration by parts will prove:

7B The integral of $v ( x )$ times $\delta ( x )$ is $\begin{array} { r } { \int _ { - A } ^ { A } v ( x ) \delta ( x ) d x = v ( 0 ) . } \end{array}$

The area is $v ( 0 )$ because the spike is multiplied by $v ( 0 )$ —the value of the smooth function $v ( x )$ at the spike. But multiplying infinity is dangerous, to say the least. (Two times infi»nity is infinity). We cannot deal direc»tly with the delta function. $I t$ is only known by its integrals! As long as the applications produce integrals (as they do), we can avoid the fact that $\delta$ is not a true function.

The integral of $v ( x ) \delta ( x ) = v ( x ) d U / d x$ is computed “by parts:”

$$
\int _ { - A } ^ { A } v ( x ) \delta ( x ) d x = v ( x ) U ( x ) { \Big ] } _ { - A } ^ { A } - \int _ { - A } ^ { A } U ( x ) { \frac { d v } { d x } } d x .
$$

Remember that $U = 0$ or $U = 1$ . The right side of (14) is our area $v ( 0 )$ :

$$
v ( A ) \cdot 1 - \int _ { 0 } ^ { A } 1 { \frac { d v } { d x } } d x = v ( A ) - ( v ( A ) - v ( 0 ) ) = v ( 0 ) .
$$

When $v ( x ) = 1$ , this answer matches $\textstyle \int { \delta d x } = 1$ . We give three examples:

$$
\begin{array} { r l } { \int _ { - 2 } ^ { 2 } \cos x \ \delta ( x ) d x = 1 } & { { } \int _ { - 5 } ^ { 6 } ( U ( x ) + \delta ( x ) ) d x = 7 \quad \int _ { - 1 } ^ { 1 } ( \delta ( x ) ) ^ { 2 } d x = \infty . } \end{array}
$$

A nightmare question occurs to me. What is the derivative of the delta function ?

# INTEGRATION BY PARTS IN ENGINEERING

Physics and engineering and economics frequently involve products. Work is force times distance. Power is voltage times current. Income is price times quantity. When there are several forces orcurrents or sales, we add the products. When there are infinitely many, we integrate (probably by parts).

I start with differential equations for the displacement $u$ at point $x$ in a bar:

$$
- { \frac { d v } { d x } } = f ( x ) \operatorname { w i t h } v ( x ) = k { \frac { d u } { d x } } .
$$

This describes a hanging bar pulled down by a force $f ( x )$ . Each point $x$ moves through a distance $u ( x )$ . The top of the bar is fixed, so $u ( 0 ) = 0$ . The stretching in the bar is $d u / d x$ . The internal force created by stretching is $v = k d u / d x$ . (This is Hooke’s law.) Equation (16) is a balance of forces on the small piece of the bar in Figure 7.2.

$$
- \Delta v = f \Delta x { \mathrm { ~ o r } } - d v / d x = f ( x )
$$

EXAMPLE 6 Suppose $f ( x ) = F$ , a constant force per unit length. We can solve (16):

$$
v ( x ) = - F x + C \quad { \mathrm { a n d } } \quad k u ( x ) = - { \textstyle { \frac { 1 } { 2 } } } F x ^ { 2 } + C x + D .
$$

Th»e constants $C$ and $D$ a»re settled at the endpoints (as usual f»or integrals). At $x = 0$ we are given $u = 0$ so $D = 0$ . At $x = 1$ we are given $v = W$ so $C = W + F$ . Then $v ( x )$ and $u ( x )$ give force and displacement in the bar.

To see integration by parts, multiply $- d v / d x = f ( x )$ by $u ( x )$ and integrate:

$$
\int _ { 0 } ^ { 1 } f ( x ) u ( x ) d x = - \int _ { 0 } ^ { 1 } { \frac { d v } { d x } } u ( x ) d x = - u ( x ) v ( x ) \bigg ] _ { 0 } ^ { 1 } + \int _ { 0 } ^ { 1 } v ( x ) { \frac { d u } { d x } } d x .
$$

The left side is force times displacement, or external work. The last term is internal force times stretching—or internal work. The integrated term has $u ( 0 ) = 0$ —the fixed support does no work. It also has $- u ( 1 ) W$ , the work by the hanging weight. The balance of forces has been replaced by a balance of work.

This is a touch of engineering mathematics, and here is the main point. Integration by parts makes physical sense! When $- d v / d x = f$ is multiplied by other functions— called test functions or virtual displacements—then equation (18) becomes the principle of virtual work. It is absolutely basic to mechanics.