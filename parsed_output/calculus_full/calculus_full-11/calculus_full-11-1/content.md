# 11.1 Vectors and Dot Products

In a plane, every point is described by two numbers. We measure across by $x$ and up by $y$ . Starting from the origin we reach the point with coordinates $( x , y )$ . I want to describe this movement by a vector—the straight line that starts at $( 0 , 0 )$ and ends at $( x , y )$ . This vector $\mathbf { v }$ has a direction, which goes from $( 0 , 0 )$ to $( x , y )$ and not the other way.

In a picture, the vector is shown by an arrow. In algebra, $\mathbf { v }$ is given by its two components. For a column vector, write $x$ above $y$ :

$$
\mathbf { v } = { \left[ \begin{array} { l } { x } \\ { y } \end{array} \right] } \quad ( x { \mathrm { ~ a n d ~ } } y { \mathrm { ~ a r e ~ t h e ~ c o m p o n e n t s ~ o f ~ } } \mathbf { v } ) .
$$

Note that $\mathbf { v }$ is printed in boldface; its components $x$ and $y$ are in lightface. $\dagger$ The vector $- \mathbf { v }$ in the opposite direction changes signs. Adding $\mathbf { v }$ to $- \mathbf { v }$ gives the zero vector (different from the zero number and also in boldface):

$$
- \mathbf { v } = { [ - x ] } - { [ - y ] }  [ \begin{array} { l l } { \quad } & { { \mathrm { a n d } } \quad } & { \mathbf { v } - \mathbf { v } = { [ \begin{array} { l } { x - x } \\ { y - y } \end{array} ] } = { [ \begin{array} { l } { 0 } \\ { 0 } \end{array} ] } = \mathbf { 0 } . } \end{array}
$$

Notice how vector addition or subtraction is done separately on the $x$ ’s and $y$ ’s:

$$
\mathbf { v } + \mathbf { w } = { \left[ \begin{array} { l } { 3 } \\ { 1 } \end{array} \right] } + { \left[ \begin{array} { l } { - 1 } \\ { 2 } \end{array} \right] } = { \left[ \begin{array} { l } { 2 } \\ { 3 } \end{array} \right] } .
$$

The vector $\mathbf { v }$ has components $v _ { 1 } = 3$ and $v _ { 2 } = 1$ . (I write $v _ { 1 }$ for the first component and $v _ { 2 }$ for the second component. I also write $x$ and $y$ , which is fine for two components.) The vector w has $w _ { 1 } = - 1$ and $w _ { 2 } = 2$ . To add the vectors, add the components. To draw this addition, place the start of w at the end of v. Figure 11.3 shows how w starts where $\mathbf { v }$ ends.

# VECTORS WITHOUT COORDINATES

In that head-to-tail addition of $\mathbf { v } + \mathbf { w }$ , we did something new. The vector $\mathbf { w }$ was moved away from the origin. Its length and direction were not changed! The new arrow is parallel to the old arrow—only the starting point is different. The vector is the same as before.

A vector can be defined without an origin and without $x$ and $y$ axes. The purpose of axes is to give the components—the separate distances $x$ and $y$ . Those numbers are necessary for calculations. But $x$ and $y$ coordinates are not necessary for head-totail addition $\mathbf { v } + \mathbf { w }$ , or for stretching to $2 \mathbf { v }$ , or for linear combinations $2 \mathbf { v } + 3 \mathbf { w }$ . Some applications depend on coordinates, others don’t.



Generally speaking, physics works without axes—it is “coordinate-free.” A velocity has direction and magnitude, but it is not tied to a point. A force also has direction and magnitude, but it can act anywhere—not only at the origin. In contrast, a vector that gives the prices of five stocks is not floating in space. Each component has a meaning—there are five axes, and we know when prices are zero. After examples from geometry and physics (no axes), we return to vectors with coordinates.

EXAMPLE 1 (Geometry) Take any four-sided figure in space. Connect the midpoints   
of the four straight sides. Remarkable fact: Those four midpoints lie in the same plane. More than that, they form a parallelogram.

Frankly, this is amazing. Figure $1 1 . 4 \mathrm { a }$ cannot do justice to the problem, because it is printed on a flat page. Imagine the vectors A and $\mathbf { D }$ coming upward. $\mathbf { B }$ and C go down at different angles. Notice how easily we indicate the four sides as vectors, not caring about axes or origin.

I will prove that $\mathbf { V } = \mathbf { W }$ . That shows that the midpoints form a parallelogram.

What is V ? It starts halfway along A and ends halfway along B. The small triangle at the bottom shows $\begin{array} { r } { { \bf V } = \frac { 1 } { 2 } { \bf A } + \frac { 1 } { 2 } { \bf B } } \end{array}$ . This is vector addition—the tail of $\scriptstyle { \frac { 1 } { 2 } } \mathbf { B }$ is at the head of $\textstyle { \frac { 1 } { 2 } } \mathbf { A }$ . Together they equal the shortcut V. For the same reason $\mathbf { W } = \textstyle { \frac { 1 } { 2 } } \mathbf { C } + \frac { 1 } { 2 } \mathbf { D }$ . The heart of the proof is to see these relationships.

One step is left. Why is $\begin{array} { r } { \frac { 1 } { 2 } \mathbf { A } + \frac { 1 } { 2 } \mathbf { B } } \end{array}$ equal to ${ \textstyle \frac { 1 } { 2 } } \mathbf { C } + { \frac { 1 } { 2 } } \mathbf { D } ?$ In other words, why is $\mathbf { A } + \mathbf { B }$ equal to $\mathbf { C } + \mathbf { D } ?$ (I multiplied by 2.) When the right question is asked, the answer jumps out. A head-to-tail addition $\mathbf { A } + \mathbf { B }$ brings us to the point $R$ . Also $\mathbf { C } + \mathbf { D }$ brings us to $R$ . The proof comes down to one line:

$$
\mathbf { A } + \mathbf { B } = P R = \mathbf { C } + \mathbf { D } . { \mathrm { ~ T h e n ~ } } \mathbf { V } = { \frac { 1 } { 2 } } \mathbf { A } + { \frac { 1 } { 2 } } \mathbf { B } { \mathrm { ~ } } \operatorname { e q u a l s } \mathbf { \Delta W } = { \frac { 1 } { 2 } } \mathbf { C } + { \frac { 1 } { 2 } } \mathbf { D } .
$$

EXAMPLE 2 (Also geometry) In any triangle, draw lines from the corners to the midpoints of the opposite sides. To prove by vectors: Those three lines meet at $\pmb { a }$ point. Problem 38 finds the meeting point in Figure 11.4c. Problem 37 says that the three vectors add to zero.

EXAMPLE 3 (Medicine) An electrocardiogram shows the sum of many small vectors, the voltages in the wall of the heart. What happens to this sum—the heart vector V—in two cases that a cardiologist is watching for ?

Case 1. Part of the heart is dead (infarction).   
Case 2. Part of the heart is abnormally thick (hypertrophy).

A heart attack kills part of the muscle. A defective valve, or hypertension, overworks it. In case 1 the cells die from the cutoff of blood (loss of oxygen). In case 2 the heart wall can triple in size, from excess pressure. The causes can be chemical or mechanical. The effect we see is electrical.

# The machine is adding small vectors and “projecting” them in twelve directions.

The leads on the arms, left leg, and chest give twelve directions in the body. Each graph shows the component of V in one of those directions. Three of the projections— two in the vertical plane, plus lead 2 for front-back—produce the “mean QRS vector” in Figure 11.5. That is the sum $\mathbf { V }$ when the ventricles start to contract. The left ventricle is larger, so the heart vector normally points down and to the left.

We come soon to projections, but here the question is about $\mathbf { V }$ itself. How does the ECG identify the problem ?

Case 1W Heart attack The dead cells make no contribution to the electrical potential. Some small vectors are missing. Therefore the sum V turns away from the infarcted part.   
Case 2W Hypertrophy The overwork increases the contribution to the potential. Some vectors are larger than normal. Therefore $\mathbf { V }$ turns toward the thickened part.

When $\mathbf { V }$ points in an abnormal direction, the ECG graphs locate the problem. The $P , Q , R , S , T$ waves on separate graphs can all indicate hypertrophy, in different regions of the heart. Infarctions generally occur in the left ventricle, which needs the greatest blood supply. When the supply of oxygen is cut back, that ventricle feels it first. The result can be a heart attack $\ l =$ myocardial infarction $\ b =$ coronary occlusion). Section 11.2 shows how the projections on the ECG point to the location.

First come the basic facts about vectors—components, lengths, and dot products.

# COORDINATE VECTORS AND LENGTH

To compute with vectors we need axes and coordinates. The picture of the heart is “coordinate-free,” but calculations require numbers. A vector is known by its components. The unit vectors along the axes are i and j in the plane and i; j; k in space:

$$
{ \mathrm { i n ~ 2 D } } \mathbf { : } \quad \mathbf { i } = { \left[ \begin{array} { l } { 1 } \\ { 0 } \\ { 0 } \end{array} \right] } , \ \mathbf { j } = { \left[ \begin{array} { l } { 0 } \\ { 1 } \\ { 1 } \end{array} \right] } \qquad { \mathrm { i n ~ 3 D } } \mathbf { : } \quad \mathbf { i } = { \left[ \begin{array} { l } { 1 } \\ { 0 } \\ { 0 } \end{array} \right] } , \ \mathbf { j } = { \left[ \begin{array} { l } { 0 } \\ { 1 } \\ { 0 } \\ { 0 } \end{array} \right] } , \ \mathbf { k } = { \left[ \begin{array} { l } { 0 } \\ { 1 } \\ { 0 } \\ { 0 } \end{array} \right] } .
$$

Notice how easily we moved into three dimensions! The only change is that vectors have three components. The combinations of i and j (or i, j, k) produce all vectors $\mathbf { v }$ in the plane (and all vectors $\mathbf { V }$ in space):

$$
\mathbf { v } = 3 \mathbf { i } + \mathbf { j } = { \left[ \begin{array} { l l } { 3 } \\ { 1 } \\ { 1 } \end{array} \right] } \quad \mathbf { V } = \mathbf { i } + 2 \mathbf { j } - 2 \mathbf { k } = { \left[ \begin{array} { l } { 1 } \\ { 2 } \\ { - 2 } \end{array} \right] } .
$$

Those vectors are also written $\mathbf { v } = ( 3 , 1 )$ and $\mathbf { V } = ( 1 , 2 , - 2 )$ . The components of the vector are also the coordinates of a point. (The vector goes from the origin to the point.) This relation between point and vector is so close that we allow them the same notation: $P = ( x , y , z )$ and $\mathbf { v } = ( x , y , z ) = x \mathbf { i } + y \mathbf { j } + z \mathbf { k }$ .

The sum $\mathbf { v } + \mathbf { V }$ is totally meaningless. Those vectors live in different dimensions.

From the components we find the length. The length of $( 3 , 1 )$ is ${ \sqrt { 3 ^ { 2 } + 1 ^ { 2 } } } = { \sqrt { 1 0 } }$ . This comes directbly from a ribght triangle. Inbthree dimensions, $\mathbf { V }$ has a third component t|o |be squared and added. The le|ng|th of ${ \bf V } = ( x , y , z )$ is $| \mathbf { V } | = { \sqrt { x ^ { 2 } + y ^ { 2 } + z ^ { 2 } } }$ .

Vertical bars indicate length, which takes the place of absolute value. The length of $\mathbf { v } = 3 \mathbf { i } + \mathbf { j }$ is the distance from the point $( 0 , 0 )$ to the point $( 3 , 1 )$ :

$$
| \mathbf { v } | = { \sqrt { v _ { 1 } ^ { 2 } + v _ { 2 } ^ { 2 } } } = { \sqrt { 1 0 } } \qquad | \mathbf { V } | = { \sqrt { 1 ^ { 2 } + 2 ^ { 2 } + ( - 2 ) ^ { 2 } } } = 3 .
$$

A unit vector is a vector of length one. Dividing $\mathbf { v }$ and $\mathbf { V }$ by their lengths produces unit vectors in the same directions:

$$
{ \frac { \mathbf { v } } { | \mathbf { v } | } } = { \left[ \begin{array} { l } { 3 / { \sqrt { 1 0 } } } \\ { 1 / { \sqrt { 1 0 } } } \end{array} \right] } \qquad { \mathrm { a n d } } \qquad { \frac { \mathbf { V } } { | \mathbf { V } | } } = { \left[ \begin{array} { l } { ~ 1 / 3 } \\ { ~ 2 / 3 } \\ { - 2 / 3 } \end{array} \right] } \quad { \mathrm { a r e ~ u n } }
$$

11A Each nonzero vector has a positive length $| \mathbf { v } |$ . The direction of v is given by a unit vector $\mathbf u = \mathbf v / | \mathbf v |$ . The length times direction equals $\mathbf { v }$ .

A unit vector in the plane is determined by its angle $\theta$ with the $x$ axis:

$$
\mathbf { u } = { \left[ \begin{array} { l } { \cos \theta } \\ { \sin \theta } \end{array} \right] } = ( \cos \theta ) \mathbf { i } + ( \sin \theta ) \mathbf { j } { \mathrm { ~ i s ~ a ~ u n i t ~ v e c t o r : ~ } } | \mathbf { u } | ^ { 2 } = \cos ^ { 2 } \theta + \sin ^ { 2 } \theta = 1 .
$$

In 3-space the components of a unit vector are its “direction cosines”:

$$
\mathbf { U } = ( \cos \alpha ) \mathbf { i } + ( \cos \beta ) \mathbf { j } + ( \cos \gamma ) \mathbf { k } ; \quad \alpha , \beta , \gamma = \mathrm { a n g l e s ~ w i t h } x , y , z \mathrm { a x e s . }
$$

Then $\cos ^ { 2 } \alpha + \cos ^ { 2 } \beta + \cos ^ { 2 } \gamma = 1$ . We are doing algebra with numbers while we are doing geometry with vectors. It was the great contribution of Descartes to see how to study algebra and geometry at the same time.

# THE DOT PRODUCT OF TWO VECTORS

There are two basic operations on vectors. First, vectors are added $( \mathbf { v } + \mathbf { w } )$ . Second, a vector is multiplied by a scalar .7v or $- 2 \mathbf { w } )$ /. That leaves a natural question—how do you multiply two vectors ? The main part of the answer is—|y o|u don’t.|B|ut there is an extremely important operation that begins with two vectors and produces a number. It is usually i|nd |i|cat|ed by a dot between the vectors, as in $\mathbf { v } \cdot \mathbf { w }$ , so it is called the dot product.

DEFINITION 1 The dot product multiplies the lengths $| \mathbf { v } |$ times $\big | \mathbf { w } \big |$ times a cosine:

$$
\mathbf { v } \cdot \mathbf { w } = | \mathbf { v } | | \mathbf { w } | \cos \theta , \qquad \theta = { \mathrm { a n g l e ~ b e t w e e n ~ } } \mathbf { v } { \mathrm { ~ a n d ~ } } \mathbf { w } .
$$

EXAMPLE $\left[ { 3 } \right] \mathrm { { h a s \ l e n g t h \ 3 , } } \left[ { 2 } \right] .$ has length $\sqrt { 8 }$ , the angle is $4 5 ^ { \circ }$ :

The dot product is $| \mathbf { v } | | \mathbf { w } | \cos \theta = ( 3 ) ( { \sqrt { 8 } } ) ( 1 / { \sqrt { 2 } } )$ , which simplifies to 6: The square roots in the lengths are “canceled” by square roots in the cosine. For computing $\mathbf { v } \cdot \mathbf { w }$ , a second and much simpler way involves no square roots in the first place.

DEFINITION 2 The dot product v w multiplies component by component and adds:

$$
\mathbf { v } \cdot \mathbf { w } = v _ { 1 } w _ { 1 } + v _ { 2 } w _ { 2 } \quad { \bigg [ } { 3 } { \bigg ] } \cdot { \bigg [ } { 2 } { \bigg ] } = ( 3 ) ( 2 ) + ( 0 ) ( 2 ) = 6 .
$$

The first form $\mathbf { \left| v \right| } \mathbf { \left| w \right| } \cos \theta$ is coordinate-free. The second form $v _ { 1 } w _ { 1 } + v _ { 2 } w _ { 2 }$ computes with coordinates|. R||ema|rk 4 explains why these two forms are equal.

11B The dot product or scalar product or inner product of three-dimensional vectors is

$$
\mathbf { V } \cdot \mathbf { W } = \left| \mathbf { V } \right| \left| \mathbf { W } \right| \cos \theta = V _ { 1 } W _ { 1 } + V _ { 2 } W _ { 2 } + V _ { 3 } W _ { 3 } .
$$

If the vectors are perpendicular then $\theta = 9 0 ^ { \circ }$ and cos $\theta = 0$ and $\mathbf { V } \cdot \mathbf { W } = 0$ .

$$
\begin{array} { r } { \begin{array} { r } { \left[ \begin{array} { l } { 1 } \\ { 2 } \\ { 3 } \\ { 3 } \end{array} \right] \cdot \left[ \begin{array} { l } { 4 } \\ { 5 } \\ { 6 } \\ { 6 } \end{array} \right] = 3 2 ( n o t p e r p e n d i c u l a r ) \quad \left[ \begin{array} { l } { 2 } \\ { 2 } \\ { - 1 } \end{array} \right] \cdot \left[ \begin{array} { l } { - 1 } \\ { 2 } \\ { 2 } \end{array} \right] = 0 ( p e r p e n d i c u l a r ) . } \end{array} } \end{array}
$$

These dot products 32 and 0 equal $\mathbf { \lvert { V } \rvert } \mathbf { \lvert { W } \rvert } \cos \theta$ . In the second one, cos $\theta$ must be zero. The angle is $\pi / 2$ or $- \pi / 2$ —in either case a right angle. Fortunately the cosine is the same for $\theta$ and $- \theta$ , so we need not decide the sign of $\theta$ .

Remark 1 When $\mathbf { V } = \mathbf { W }$ the angle is zero but not the cosine! In this case cos $\theta = 1$ and $\mathbf { V } \cdot \mathbf { V } = | \mathbf { V } | ^ { 2 }$ . The dot product of $\mathbf { V }$ with itself is the length squared:

$$
\mathbf { V } \cdot \mathbf { V } = ( V _ { 1 } , V _ { 2 } , V _ { 3 } ) \cdot ( V _ { 1 } , V _ { 2 } , V _ { 3 } ) = V _ { 1 } ^ { 2 } + V _ { 2 } ^ { 2 } + V _ { 3 } ^ { 2 } = | \mathbf { V } | ^ { 2 } .
$$

Remark 2 The dot product of $\mathbf { i } = ( 1 , 0 , 0 )$ with ${ \bf j } = ( 0 , 1 , 0 )$ is $\mathbf { i } \cdot \mathbf { j } = 0$ . The axes are perpendicular. Similarly $\mathbf { i } \cdot \mathbf { k } = 0$ and $\mathbf { j } \cdot \mathbf { k } = 0$ . Those are unit vectors: $\mathbf { i } \cdot \mathbf { i } = \mathbf { j } \cdot \mathbf { j } = \mathbf { k } \cdot \mathbf { k } = 1$ .

Remark 3 The dot product has three properties that keep the algebra simple:

$$
{ \mathrm { , ~ } } \nabla \cdot \mathbf { W } = \mathbf { W } \cdot \mathbf { V } \qquad 2 \cdot \mathbf { \sigma } ( c \mathbf { V } ) \cdot \mathbf { W } = c ( \mathbf { V } \cdot \mathbf { W } ) \qquad 3 \cdot \mathbf { \sigma } ( \mathbf { U } + \mathbf { V } ) \cdot \mathbf { W } = \mathbf { U } \cdot \mathbf { W } + \mathbf { V } \cdot \mathbf { W }
$$

When $\mathbf { V }$ is doubled . $( c = 2$ / the dot product is doubled. When $\mathbf { V }$ is split into i; j; k components, the dot product splits in three pieces. The same applies to $\mathbf { W }$ , since $\mathbf { V } \cdot \mathbf { W } = \mathbf { W } \cdot \mathbf { V }$ . The nine dot products of i; j; k are zeros and ones, and a giant splitting of both $\mathbf { V }$ and $\mathbf { W }$ gives back the correct $\mathbf { V } \cdot \mathbf { W }$ :

$$
\mathbf { V } \cdot \mathbf { W } = V _ { 1 } \mathbf { i } \cdot W _ { 1 } \mathbf { i } + V _ { 2 } \mathbf { j } \cdot W _ { 2 } \mathbf { j } + V _ { 3 } \mathbf { k } \cdot W _ { 3 } \mathbf { k } + \mathrm { s i x ~ z e r o e s } = V _ { 1 } W _ { 1 } + V _ { 2 } W _ { 2 } + V _ { 3 } W _ { 3 } .
$$

Remark 4 The two f|orms of|the |dot| pro|duc|t are |eq|u| al.|This comes from computing $| \mathbf { V } - \mathbf { W } | ^ { 2 }$ by coordinates and also by the “law of cosines”:

with coordinates $\begin{array} { r l } & { | \mathbf { V } - \mathbf { W } | ^ { 2 } = ( V _ { 1 } - W _ { 1 } ) ^ { 2 } + ( V _ { 2 } - W _ { 2 } ) ^ { 2 } + ( V _ { 3 } - W _ { 3 } ) ^ { 2 } } \\ & { | \mathbf { V } - \mathbf { W } | ^ { 2 } = | \mathbf { V } | ^ { 2 } + | \mathbf { W } | ^ { 2 } - 2 | \mathbf { V } | | \mathbf { W } | \cos \theta . } \end{array}$ from cosine law

Compare those two lines. Line 1 contains $V _ { 1 } ^ { 2 }$ and $V _ { 2 } ^ { 2 }$ and $V _ { 3 } ^ { 2 }$ . Their sum matches $| \mathbf { V } | ^ { 2 }$ in the cosine law. Also $\dot { W _ { 1 } ^ { 2 } } + \dot { W _ { 2 } ^ { 2 } } + \dot { W _ { 3 } ^ { 2 } }$ matches $| \mathbf { W } | ^ { 2 }$ . Therefore the terms containing $- 2$ are the same (you can mentally cancel the $- 2$ ). The definitions agree:

$$
\begin{array} { r } { - 2 ( { \cal V } _ { 1 } { \cal W } _ { 1 } + { \cal V } _ { 2 } { \cal W } _ { 2 } + { \cal V } _ { 3 } { \cal W } _ { 3 } ) \ e q u a l s - 2 | { \bf V } | | { \bf W } | \cos \theta \ e q u a l s - 2 { \bf V } \cdot { \bf W } . } \end{array}
$$

The cosine law is coordinate-free. It applies to all triangles (even in $n$ dimensions). Its vector form in Figure 11.8 is $| \mathbf { V } - \bar { \mathbf { W } } | ^ { 2 } = | \mathbf { V } | ^ { 2 } - 2 \mathbf { V } \cdot \mathbf { W } + | \mathbf { W } | ^ { 2 }$ . This application to $\mathbf { V } \cdot \mathbf { W }$ is its brief moment of glory.

Remark 5 The dot product is the best way to compute the cosine of $\theta$ :

$$
\cos \theta = { \frac { \mathbf { V } \cdot \mathbf { W } } { | \mathbf { V } | | \mathbf { W } | } } .
$$

Here are examples of $\mathbf { V }$ and $\mathbf { W }$ with a range of angles from 0 to $\pi$ :

$$
{ \begin{array} { l l l } { \mathbf { i } { \mathrm { ~ a n d ~ } } 3 \mathbf { i } { \mathrm { ~ h a v e ~ t h e ~ s a m e ~ d i r e c t i o n } } } & { \cos \theta = 1 } & { \theta = 0 } \\ { \mathbf { i } \cdot ( \mathbf { i } + \mathbf { j } ) = 1 { \mathrm { ~ i s ~ p o s i t i v e } } } & { \cos \theta = 1 / { \sqrt { 2 } } } & { \theta = \pi / 4 } \\ { \mathbf { i } { \mathrm { ~ a n d ~ } } \mathbf { j } { \mathrm { ~ a r e ~ p e r p e n d i c u l a r . ~ } } \mathbf { i } \cdot \mathbf { j } = 0 } & { \cos \theta = 0 } & { \theta = \pi / 2 } \\ { \mathbf { i } \cdot ( - \mathbf { i } + \mathbf { j } ) = - 1 { \mathrm { ~ i s ~ n e g a t i v e } } } & { \cos \theta = - 1 / { \sqrt { 2 } } } & { \theta = 3 \pi / 4 } \\ { \mathbf { i } { \mathrm { ~ a n d ~ } } - 3 \mathbf { i } { \mathrm { ~ h a v e ~ o p p o s i t e ~ d i r e c t i o n s } } } & { \cos \theta = - 1 } & { \theta = \pi } \end{array} }
$$

Remark 6 The Cauchy-Schwarz inequality $| \mathbf { V } \cdot \mathbf { W } | \leqslant | \mathbf { V } | | \mathbf { W } |$ comes from $| \cos \theta | \leqslant 1$ .

The left side is $| \mathbf { V } | | \mathbf { W } | | \cos \theta |$ .¤It| n|ever| ex|ceed |s th|e|rig|ht| side $\mathbf { | \nabla V | | \mathbf { W } } |$ . This is a key inequality in mathematics, from which so many others follow:

|Geome|tr¤ic| m|e|an $\sqrt { x y } \leqslant$ arithmetic mean ${ \frac { 1 } { 2 } } ( x + y )$ (true for any $x \geqslant 0$ and $y \geqslant 0$ ).   
Triangle inequality $| \mathbf { V } + \mathbf { W } | \leqslant | \mathbf { V } | + | \mathbf { W } |$ $( | \mathbf { V } | , | \mathbf { W } | , | \mathbf { V } + \mathbf { W } |$ are lengths of sides).

These and other examples are in Problems 39 to 44: The Schwarz inequality $| \mathbf { V } \cdot \mathbf { W } | \leqslant | \mathbf { V } | | \mathbf { W } |$ becomes an equality when $| \cos \theta | = 1$ and the vectors are