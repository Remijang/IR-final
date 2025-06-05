# CHAPTER 15 Vector Calculus

Chapter 14 introduced double and triple integrals. We went from $\textstyle \int d x$ to $\iint d x d y$ and $\iint d x d y d z$ . All those integrals add up small pieces, and the limit gives area or volume or mass. What could be more natural than that? I regret to say, after the success of those multiple integrals, that something is missing. It is even more regrettable that we didn’t notice it. The missing piece is nothing less than the Fundamental Theorem of Calculus.

The double integral $\iiint d x d y$ equals the area. To compute it, we did not use an antiderivative of 1: At least not consciously. The method was almost trial and error, and the hard part was to find the limits of integration. This chapter goes deeper, to show how the step from a double integral to a single integral is really a new form of the Fundamental Theorem—when it is done right.

Two new ideas are needed early, one pleasant and one not. You will like vector fields. You may not think so highly of line integrals. Those are ordinary single integrals like $\int v ( x ) d x$ ; but they go along curves instead of straight lines. The nice step $d x$ becomes the confusing step $d s$ : Where $\textstyle \int d x$ equals the length of the interval, $\int d s$ is the length of the curve. The point is that regions are enclosed by curves, and we have to integrate along them. The Fundamental Theorem in its two-dimensional form (Green’s Theorem) connects $\pmb { a }$ double integral over the region to a single integral along its boundary curve.

The great applications are in science and engineering, where vector fields are so natural. But there are changes in the language. Instead of an antiderivative, we speak about a potential function. Instead of the derivative, we take the “divergence” and “curl.” Instead of area, we compute flux and circulation and work. Examples come first.

# 15.1 Vector Fields

For an ordinary scalar function, the input is a number $x$ and the output is a number $f ( x )$ : For a vector field (or vector function), the input is a point $( x , y )$ and the output is a two-dimensional vector $\mathbf { F } ( x , y )$ : There is a “field” of vectors, one at every point. In three dimensions the input point is $( x , y , z )$ and the output vector $\mathbf { F }$ has three components.

DEFINITION Let $R$ be a region in the $x y$ plane. A vector field $\mathbf { F }$ assigns to every point $( x , y )$ in $R$ a vector $\mathbf { F } ( x , y )$ with two components:

$$
{ \displaystyle { \bf F } ( x , y ) = M ( x , y ) { \bf i } + N ( x , y ) { \bf j } . }
$$

This plane vector field involves two functions of two variables. They are the components $M$ and $N$ ; which vary from point to point. A vector has fixed components, a vector field has varying components.

A three-dimensional vector field has components $M ( x , y , z )$ and $N ( x , y , z )$ and $P ( x , y , z )$ : Then the vectors are $\mathbf { F } = M \mathbf { i } + N \mathbf { j } + P \mathbf { k }$ :

EXAMPLE 1 The position vector at $( x , y )$ is $\mathbf { R } = x \mathbf { i } + y \mathbf { j }$ : Its components are $M = x$ and $N = y$ : The vectors grow larger as we leave the origin (Figure 15.1a). Their direction is outward and their length is $| \mathbf { R } | = { \sqrt { x ^ { 2 } + y ^ { 2 } } } { \overset { - } { = } } r$ : The vector $\mathbf { R }$ is boldface, the number $r$ is lightface.

EXAMPLE 2 The vector field ${ \bf R } / r$ consists of unit vectors ${ \bf u } _ { r }$ ; pointing outward. We divide $\mathbf { R } = x \mathbf { i } + y \mathbf { j }$ by its length, at every point except the origin. The components of ${ \bf R } / r$ are $M = x / r$ and $N = y / r$ : Figure 15.1 shows a third field ${ \bf R } / r ^ { 2 }$ ; whose length is $1 / r$ :

$$
\therefore \frac { N } { 2 } = - \frac { 1 } { 3 } + \frac { 3 } { 5 } - \frac { 1 } { 4 } \frac { N ^ { 2 } } { 5 }
$$

EXAMPLE 3 The spin field or rotation field or turning field goes around the origin instead of away from it. The field is S: Its components are $M = - y$ and $N = x$ :

$$
\mathbf { S } = - y \mathbf { i } + x \mathbf { j } { \mathrm { ~ a l s o ~ h a s ~ l e n g t h ~ } } | \mathbf { S } | = { \sqrt { ( - y ) ^ { 2 } + x ^ { 2 } } } = r .
$$

S is perpendicular to $\mathbf { R }$ —their dot product is zero: $\mathbf { S } \cdot \mathbf { R } = ( - y ) ( x ) + ( x ) ( y ) = 0$ : The spin fields $\mathbf { S } / r$ and $\mathbf { S } / r ^ { 2 }$ have lengths 1 and $1 / r$ :

$$
{ \frac { \mathbf { S } } { r } } = - { \frac { y } { r } } \mathbf { i } + { \frac { x } { r } } \mathbf { j } \quad { \mathrm { h a s } } \quad \left| { \frac { \mathbf { S } } { r } } \right| = 1 \qquad { \frac { \mathbf { S } } { r ^ { 2 } } } = - { \frac { y } { x ^ { 2 } + y ^ { 2 } } } \mathbf { i } + { \frac { x } { x ^ { 2 } + y ^ { 2 } } } \mathbf { j } \quad { \mathrm { h a s } } \quad \left| { \frac { \mathbf { S } } { r ^ { 2 } } } \right| = { \frac { 1 } { r } } .
$$

The unit vector $\mathbf { S } / r$ is ${ \bf u } _ { \theta }$ : Notice the blank at $( 0 , 0 )$ ; where this field is not defined.

EXAMPLE 4 A gradient field starts with an ordinary function $f ( x , y )$ : The components $M$ and $N$ are the partial derivatives $\partial f / \partial x$ and $\partial f / \partial y$ : Then the field $\mathbf { F }$ is the gradient of $f$ :

$$
{ \bf F } = \mathrm { g r a d } f = \nabla f = \partial f / \partial x { \bf i } + \partial f / \partial y { \bf j } .
$$