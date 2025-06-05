# CHAPTER 13

# Partial Derivatives

This chapter is at the center of multidimensional calculus. Other chapters and other topics may be optional; this chapter and these topics are required. We are back to the basic idea of calculus—the derivative. There is a function $f _ { : }$ ; the variables move a little bit, and $f$ moves. The question is how much $f$ moves and how fast. Chapters 1–4 answered this question for $f ( x )$ ; a function of one variable. Now we have $f ( x , y )$ or $f ( x , y , z )$ —with two or three or more variables that move independently. As $x$ and $y$ change, $f$ changes. The fundamental problem of differential calculus is to connect $\Delta x$ and $\Delta y$ to $\Delta f .$ Calculus solves that problem in the limit. It connects $d x$ and $d y$ to $d f .$ In using this language I am building on the work already done. You know that $d f / d x$ is the limit of $\Delta f / \Delta x$ : Calculus computes the rate of change— which is the slope of the tangent line. The goal is to extend those ideas to

$$
f ( x , y ) = x ^ { 2 } - y ^ { 2 } \quad { \mathrm { o r } } \quad f ( x , y ) = { \sqrt { x ^ { 2 } + y ^ { 2 } } } \quad { \mathrm { o r } } \quad f ( x , y , z ) = 2 x + 3 y + 4 z .
$$

These functions have graphs, they have derivatives, and they must have tangents.

The heart of this chapter is summarized in six lines. The subject is differential calculus—small changes in a short time. Still to come is integral calculus—adding up those small changes. We give the words and symbols for $f ( x , y )$ ; matched with the words and symbols for $f ( x )$ : Please use this suBmmary asBa guide, to know where calculus is going.

$$
C u r v e \ y = f ( x ) \quad \nu s . \quad S u r f a c e \ z = f ( x , y )
$$

$$
\begin{array} { r l } { \frac { d \vec { f } } { d x } } & { \mathrm { ~ h e c o n v e s ~ t w o ~ p a r i a l ~ d e i v a t i v e s ~ } \frac { \partial \vec { f } } { \partial x } } & { \mathrm { ~ a n d ~ } \frac { \partial \vec { f } } { \partial y } } \\ { \frac { d ^ { 2 } \vec { f } } { d x ^ { 2 } } } & { \mathrm { ~ h e c o n v e s ~ f o u r ~ s e c o n d ~ d e i v a t i v e s ~ } \frac { \partial ^ { 2 } \vec { f } } { \partial x ^ { 2 } } , \frac { \vec { \sigma } ^ { 2 } \vec { f } } { \partial \vec { x } \partial \gamma } , \frac { \vec { \sigma } ^ { 2 } \vec { f } } { \partial \vec { x } \partial x } , \frac { \vec { \sigma } ^ { 2 } \vec { f } } { \partial \gamma ^ { 2 } } } \\ { \Delta \vec { f } \approx \frac { d \vec { f } } { d x } \Delta x } & { \mathrm { ~ b e c o n v e s ~ t h e ~ i n e a r ~ a p p r o x i m a t i o n ~ } \Delta f \approx \frac { \vec { \sigma } } { \partial x } \Delta x + \frac { \vec { \sigma } } { \vec { \sigma } y } \Delta x + \frac { \vec { \sigma } } { \vec { \sigma } y } \Delta y } \\ { \mathrm { ~ t o t e n l i n e ~ \ b e c o n v e s ~ t h e ~ t o u g e n t ~ p l a n e ~ } z - z _ { 0 } = \frac { \partial \vec { f } } { \partial x } ( x - x _ { 0 } ) + \frac { \vec { \sigma } \vec { f } } { \partial y } ( y - y _ { 0 } ) } \\ { \frac { d \vec { f } } { d t } = \frac { d y } { d x } \frac { d x } { d t } } & { \mathrm { ~ b e c o n v e s ~ t h e ~ c h a i n t ~ n u ~ } \frac { d z } { d t } = \frac { \vec { \sigma } } { \vec { \sigma } x } \frac { d x } { d t } + \frac { \vec { \sigma } } { \vec { \sigma } y } \frac { d y } { d t } } \\ { \frac { d \vec { f } } { d x } = 0 } & { \mathrm { ~ b e c o n v e s ~ t w o ~ m a x i n u m ~ c o u n a c t u a n ~ } \frac { \partial \vec { f } } { \partial x } = 0 , } \end{array}
$$