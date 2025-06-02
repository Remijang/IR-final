# 11.3 Cross Products and Determinants

After saying that vectors are not multiplied, we offered the dot product. Now we contradict ourselves further, by defining the cross product. Where $\mathbf { A \cdot B }$ was a number, the cross product $\mathbf { A } \times \mathbf { B }$ is a vector. It has length and direction:

The length is $\mathbf { \left| A \right| } \left| \mathbf { B } \right| \left| \sin \theta \right|$ : The direction is perpendicular to A and B:

The cross product (also called vector product) is defined in three dimensions only. $\mathbf { A }$ and $\mathbf { B }$ lie on a plane through the origin. $\mathbf { A } \times \mathbf { B }$ is along the normal vector $\mathbf { N }$ , perpendicular to that plane. We still have to say whether it points “up” or “down” along $\mathbf { N }$ |:

The length of $\mathbf { A } \times \mathbf { B }$ depends on sin $\theta$ , where $\mathbf { A \cdot B }$ involved cos $\theta$ : The dot product rewards vectors for being parallel .cos $0 = 1 \mathrm { \dot { \Omega } }$ /: The cross product is largest when $\mathbf { A }$ is perpendicular to $\mathbf { B }$ .sin $\pi / 2 = 1$ /: At every angle

$$
| \mathbf { A } \cdot \mathbf { B } | ^ { 2 } + | \mathbf { A } \times \mathbf { B } | ^ { 2 } = | \mathbf { A } | ^ { 2 } | \mathbf { B } | ^ { 2 } \cos ^ { 2 } \theta + | \mathbf { A } | ^ { 2 } | \mathbf { B } | ^ { 2 } \sin ^ { 2 } \theta = | \mathbf { A } | ^ { 2 } | \mathbf { B } | ^ { 2 } .
$$

That will be a bridge from geometry to al|gebra. |This| se||cti|on goes from definition to formula to volume to determinant. Equations (6) and (14) are the key formulas for $\mathbf { A } \times \mathbf { B }$ :

Notice that $\mathbf { A } \times \mathbf { A } = \mathbf { 0 }$ : (This is the zero vector, not the zero number.) When $\mathbf { B }$ is parallel to $\mathbf { A }$ , the angle is zero and the sine is zero. Parallel vectors have $\mathbf { A } \times \mathbf { B } = \mathbf { 0 }$ : Perpendicular vectors have sin $\theta = 1$ and $| \mathbf { A } \times \mathbf { B } | = | \mathbf { A } | | \mathbf { B } | =$ area of rectangle with sides A and $\mathbf { B }$ :

Here are four examples that lead to the cross product $\mathbf { A } \times \mathbf { B }$ :

EXAMPLE 1 (Fro |m g|eometry) Find t|he |a|rea of|a parallelogram and a triangle.

Vectors A and B, going out from the origin, form two sides of a triangle. They produce the parallelogram in Figure 11.13, which is|tw|i|ce||as larg|e as|thetria|ngle.

The area of a parallelogram is base times height (perpendicular height not sloping height). The base is $\mathbf { \left| A \right| }$ : The height is $\left| \mathbf { B } \right| \left| \sin \theta \right|$ : We take absolute values because height and area are not negative. Then the area is the length of the cross product:

$$
a r e a o f p a r a l l e l o g r a m = | \mathbf { A } | | \mathbf { B } | | \sin \theta | = | \mathbf { A } \times \mathbf { B } | .
$$

EXAMPLE 2 (From physics) The torque vector $\mathbf { T } = \mathbf { R } \times \mathbf { F }$ produces rotation.

The force $\mathbf { F }$ acts at the point $( x , y , z )$ : When $\mathbf { F }$ is parallel to the position vector $\mathbf { R } = x \mathbf { i } + y \mathbf { j } + z \mathbf { k }$ , the force pushes outward (no turning). When $\mathbf { F }$ is perpendicular to $\mathbf { R }$ , the force creates rotation. For in-between angles there is an outward force $\left| \mathbf { F } \right| \cos \theta$ and a turning force $\left| \mathbf { F } \right| \sin \theta$ : The turning force times the distance $\mathbf { \left| R \right| }$ is the moment $\left| \mathbf { R } \right| \left| \mathbf { F } \right| \sin \theta$ :



The moment gives the magnitude and sign of the torque vector $\mathbf { T } = \mathbf { R } \times \mathbf { F }$ . The direction of $\mathbf { T }$ is along the axis of rotation, at right angles to $\mathbf { R }$ and $\mathbf { F }$ :

EXAMPLE 3 Does the cross product go up or down ? Use the right-hand rule.

Forces and torques are probably just fine for physicists. Those who are not natural physicists want to see something turn. We can visualize a record or compact disc rotating around its axis—which comes up through the center.

At a point on the disc, you give a push. When the push is outward (hard to do), nothing turns. Rotation comes from force “around” the axis. The disc can turn either way—depending on the angle between force and position. A sign convention is necessary, and it is the right-hand rule:

$\mathbf { A } \times \mathbf { B }$ points along your right thumb when the fingers curl from A toward B:

This rule is simplest for the vectors $\mathbf { i } , \mathbf { j } , \mathbf { k }$ in Figure 11.14—which is all we need.

Suppose the fingers curl from i to $\mathbf { j }$ : The thumb points along $\mathbf { k }$ : The $x$ -y-z axes form $\pmb { a }$ “right-handed triple.” Since $| \mathbf { i } | = 1$ and $| \mathbf { j } | = 1$ and sin $\pi / 2 = 1$ , the length of $\mathbf { i } \times \mathbf { j }$ is 1: The cross product is $\mathbf { i } \times \mathbf { j } = \mathbf { k }$ . The disc turns counterclockwise—its angular velocity is up—when the force acts at i in the direction j:

Figure 11.14b reverses i and $\mathbf { j }$ : The force acts at $\mathbf { j }$ and its direction is i: The disc turns clockwise (the way records and compact discs actually turn). When the fingers curl from j to i, the thumb points down. Thus $\mathbf { j } \times \mathbf { i } = - \mathbf { k }$ : This is a special case of an amazing rule:

$$
T h e ~ c r o s s { p r o d u c t i s ~ a n t i c o m m u t a t i v e } \colon { \bf B } \times { \bf A } = - ( { \bf A } \times { \bf B } ) .
$$

That is quite remarkable. Its discovery by Hamilton produced an intellectual revolution in 19 th century algebra, which had been totally accustomed to $A B = B A$ : This commutative law is old and boring for numbers (it is new and boring for dot products). Here we see its opposite for vector products $\mathbf { A } \times \mathbf { B }$ : Neither law holds for matrix products.

EXAMPLE 4 A screw goes into a wall or out, following the right-hand rule.

The disc was in the $x y$ plane. So was the force. (We are not breaking records here.) The axis was up and down. To see the cross product more completely we need to turn a screw into a wall.

Figure 11.14b shows the $x z$ plane as the wall. The screw is in the $y$ direction. By turning from $x$ toward $z$ we drive the screw into the wall—which is the negative $y$ direction. In other words $\mathbf { i } \times \mathbf { k }$ equals minus j: We turn the screw clockwise to make it go in. To take out the screw, twist from $\mathbf { k }$ toward i: Then $\mathbf { k } \times \mathbf { i }$ equals plus j:



To summarize: $\mathbf { k } \times \mathbf { i } = \mathbf { j }$ and $\mathbf { j } \times \mathbf { k } = \mathbf { i }$ have plus signs because kij and jki are in the same “cyclic order” as ijk: (Anticyclic is minus.) The $z { - } x { - } y$ and $y - z - x$ axes form righthanded triples like $x { - } y { - } z$ :

# THE FORMULA FOR THE CROSS PRODUCT

We begin the algebra of $\mathbf { A } \times \mathbf { B }$ : It is essential for computation, and it comes out beautifully. The square roots in $\mathbf { \left| A \right| } \left| \mathbf { B } \right| \left| \sin \theta \right|$ will disappear in formula (6) for $\mathbf { A } \times \mathbf { B }$ : (The square roots also disappeared in $\mathbf { A } \cdot \mathbf { B }$ , which is $\mathbf { \left| A \right| } \left| \mathbf { B } \right| \cos \theta$ : But $\mathbf { \left| A \right| \left| B \right| }$ tan $\theta$ would be terrible.) Since $\mathbf { A } \times \mathbf { B }$ is a vector we need to find three components.

Start with the two-dimensional case. The vectors $a _ { 1 } \mathbf { i } + a _ { 2 } \mathbf { j }$ and $b _ { 1 } \mathbf { i } + b _ { 2 } \mathbf { j }$ are in the $x y$ plane. Their cross product must go in the $z$ direction. Therefore $\mathbf { A } \times \mathbf { B } = \mathop { ? } \mathbf { k }$ and there is only one nonzero component. It must be $\mathbf { \left| A \right| } \left| \mathbf { B } \right| \sin \theta$ (with the correct sign), but we want a better formula. There are two clean ways to compute $\mathbf { A } \times \mathbf { B }$ , either by algebra $\mathbf { \Pi } ( \pmb { a } )$ or by a bridge $( b )$ to the dot product and geometry:

$$
( a ) ( a _ { 1 } \mathbf { i } + a _ { 2 } \mathbf { j } ) \times ( b _ { 1 } \mathbf { i } + b _ { 2 } \mathbf { j } ) = a _ { 1 } b _ { 1 } \mathbf { i } \times \mathbf { i } + a _ { 1 } b _ { 2 } \mathbf { i } \times \mathbf { j } + a _ { 2 } b _ { 1 } \mathbf { j } \times \mathbf { i } + a _ { 2 } b _ { 2 } \mathbf { j } \times \mathbf { j } ( 4 )
$$

On the right are $\mathbf { 0 } , a _ { 1 } b _ { 2 } \mathbf { k } , - a _ { 2 } b _ { 1 } \mathbf { k }$ and 0: The cross product is $( a _ { 1 } b _ { 2 } - a _ { 2 } b _ { 1 } ) \mathbf { k }$

$( \pmb { b } )$ Rotate $\mathbf { B } = b _ { 1 } \mathbf { i } + b _ { 2 } \mathbf { j }$ clockwise through $9 0 ^ { \circ }$ into $\mathbf { B } ^ { * } = b _ { 2 } \mathbf { i } - b _ { 1 } \mathbf { j }$ : Its length is unchanged (and $\mathbf { B } \cdot \mathbf { B } ^ { * } = 0$ ). Then $\left| \mathbf { A } \right| \left| \mathbf { B } ^ { * } \right| \sin \theta$ equals $| \mathbf { A } | | \mathbf { B } ^ { * } \cos \theta$ , which is $\mathbf { A \cdot B ^ { * } }$ :

$$
| \mathbf { A } | | \mathbf { B } | \sin \theta = \mathbf { A } \cdot \mathbf { B } ^ { * } = { \left[ \begin{array} { l } { a _ { 1 } } \\ { a _ { 2 } } \end{array} \right] } \cdot { \left[ \begin{array} { l } { b _ { 2 } } \\ { - b _ { 1 } } \end{array} \right] } = a _ { 1 } b _ { 2 } - a _ { 2 } b _ { 1 } .
$$

11F In the $x y$ plane, $\mathbf { A } \times \mathbf { B }$ equals $( a _ { 1 } b _ { 2 } - a _ { 2 } b _ { 1 } ) \mathbf { k }$ : The parallelogram with sides A and $\mathbf { B }$ has area $| a _ { 1 } b _ { 2 } - a _ { 2 } b _ { 1 } |$ : The triangle $O A B$ has area $\begin{array} { r } { \frac { 1 } { 2 } | a _ { 1 } b _ { 2 } - a _ { 2 } b _ { 1 } | } \end{array}$ :

EXAMPLE 5 For $\mathbf { A } = \mathbf { i } + 2 \mathbf { j }$ and $\mathbf { B } = 4 \mathbf { i } + 5 \mathbf { j }$ the cross product is $( 1 \cdot 5 - 2 \cdot 4 ) \mathbf { k } =$ $- 3 \mathbf { k }$ : Area of parallelogram $= 3$ , area of triangle $= 3 / 2$ : The minus sign in $\mathbf { A } \times \mathbf { B } =$ $- 3 \mathbf { k }$ is absent in the areas.

Note Splitting $\mathbf { A } \times \mathbf { B }$ intofour separate cross productsis correct, but it does not follow easily from $\mathbf { \left| A \right| } \left| \mathbf { B } \right| \sin \theta$ : Method $\mathbf { \Pi } ( \pmb { a } )$ is not justified until Remark 1 below. An algebraist would change the definition of $\mathbf { A } \times \mathbf { B }$ to start with the distributive law (splitting rule) and the anticommutative law:

$$
\mathbf { A } \times ( \mathbf { B } + \mathbf { C } ) = ( \mathbf { A } \times \mathbf { B } ) + ( \mathbf { A } \times \mathbf { C } ) \quad { \mathrm { ~ a n d ~ } } \quad \mathbf { A } \times \mathbf { B } = - ( \mathbf { B } \times \mathbf { A } ) .
$$

# THE CROSS PRODUCT FORMULA (3 COMPONENTS)

We move to three dimensions. The goal is to compute all three components of $\mathbf { A } \times \mathbf { B }$ (not just the length). Method $\mathbf { \Pi } ( \pmb { a } )$ splits each vector into its i; j; k components, making nine separate cross products:

$( a _ { 1 } { \mathbf i } + a _ { 2 } { \mathbf j } + a _ { 3 } { \mathbf k } ) \times ( b _ { 1 } { \mathbf i } + b _ { 2 } { \mathbf j } + b _ { 3 } { \mathbf k } ) = a _ { 1 } b _ { 2 } ( { \mathbf i } \times { \mathbf i } ) + a _ { 1 } b _ { 2 } ( { \mathbf i } \times { \mathbf j } ) +$ seven more terms:

# 11.3 Cross Products and Determinants

Remember $\mathbf { i } \times \mathbf { i } = \mathbf { j } \times \mathbf { j } = \mathbf { k } \times \mathbf { k } = \mathbf { 0 }$ : Those three terms disappear. The other six terms come in pairs, and please notice the cyclic pattern:

$$
\mathbf { A } \times \mathbf { B } = ( a _ { 2 } b _ { 3 } - a _ { 3 } b _ { 2 } ) \mathbf { i } + ( a _ { 3 } b _ { 1 } - a _ { 1 } b _ { 3 } ) \mathbf { j } + ( a _ { 1 } b _ { 2 } - a _ { 2 } b _ { 1 } ) \mathbf { k } .
$$

The k component is the $2 \times 2$ answer, when $a _ { 3 } = b _ { 3 } = 0$ : The i component involves indices 2 and 3, $\mathbf { j }$ involves 3 and 1, $\mathbf { k }$ involves 1 and 2: The cross product formula is written as a “determinant” in equation (14) below—many people use that form to compute $\mathbf { A } \times \mathbf { B }$ :

EXAMPLE 6 $( { \bf i } + 2 { \bf j } + 3 { \bf k } ) \times ( 4 { \bf i } + 5 { \bf j } + 6 { \bf k } ) = ( 2 \cdot 6 - 3 \cdot 5 ) { \bf i } + ( 3 \cdot 4 - 1 \cdot 6 ) { \bf j } + ( 1 \cdot $ $5 -$   
$2 \cdot 4 ) \mathbf { k }$ : The i; j; k components give $\mathbf { A } \times \mathbf { B } = - 3 \mathbf { i } + 6 \mathbf { j } - 3 \mathbf { k }$ : Never add the $^ { - 3 , 6 }$ ; and $^ { - 3 }$ :

Remark 1 The three-dimensional formula (6) is still to be matched with $\mathbf { A } \times \mathbf { B }$ from geometry. One way is to rotate $\mathbf { B }$ into $\mathbf { B } ^ { * }$ as before, staying in the plane of A and B: Fortunately there isan easier test. The vector in equation (6)satisfies all four geometric requirements on $\mathbf { A } \times \mathbf { B }$ : perpendicular to A, perpendicular to $\mathbf { B }$ , correct length, right-hand rule. The length is checked in Problem 16—here is the zero dot product with A:

$$
\mathbf { A } \cdot ( \mathbf { A } \times \mathbf { B } ) = a _ { 1 } ( a _ { 2 } b _ { 3 } - a _ { 3 } b _ { 2 } ) + a _ { 2 } ( a _ { 3 } b _ { 1 } - a _ { 1 } b _ { 3 } ) + a _ { 3 } ( a _ { 1 } b _ { 2 } - a _ { 2 } b _ { 1 } ) = 0 .
$$

Remark 2 (Optional) There is a wonderful extension of the Pythagoras formula $a ^ { 2 } + b ^ { 2 } = c ^ { 2 }$ : Instead of sides of a triangle, we go to areas of projections on the $y z$ , $x z$ , and $x y$ planes. $3 ^ { 2 } + 6 ^ { 2 } + 3 ^ { 2 }$ is the square of the parallelogram area in Example 6.

For triangles these areas are cut in half. Figure 11.15a shows three projected triangles of area $\frac { 1 } { 2 }$ : Its Pythagoras formula is $\begin{array} { r } { \left( \frac { 1 } { 2 } \right) ^ { 2 } + \left( \frac { 1 } { 2 } \right) ^ { 2 } + \left( \frac { 1 } { 2 } \right) ^ { 2 } = ( \mathrm { a r e a } \mathrm { o f } P Q R ) ^ { 2 } } \end{array}$ :

EXAMPLE 7 $P = ( 1 , 0 , 0 ) , Q = ( 0 , 1 , 0 ) , R = ( 0 , 0 , 1 )$ lie in a plane. Find its equation.

Idea for any $P , Q , R$ : Find vectors A and B in the plane. Compute the normal $\mathbf { N } = \mathbf { A } \times \mathbf { B }$ :

Solution The vector from $P$ to $\boldsymbol { Q }$ has components $- 1 , 1 , 0 .$ : It is $\mathbf { A } = \mathbf { j } - \mathbf { i }$ (subtract to go from $P$ to $\boldsymbol { Q }$ ). Similarly the vector from $P$ to $R$ is $\mathbf { B } = \mathbf { k } - \mathbf { i }$ : Since $\mathbf { A }$ and $\mathbf { B }$ are in the plane of Figure 11.15, $\mathbf { N } = \mathbf { A } \times \mathbf { B }$ is perpendicular:

$$
( \mathbf { j } - \mathbf { i } ) \times ( \mathbf { k } - \mathbf { i } ) = ( \mathbf { j } \times \mathbf { k } ) - ( \mathbf { i } \times \mathbf { k } ) - ( \mathbf { j } \times \mathbf { i } ) + ( \mathbf { i } \times \mathbf { i } ) = \mathbf { i } + \mathbf { j } + \mathbf { k } .
$$

The normal vector is $\mathbf { N } = \mathbf { i } + \mathbf { j } + \mathbf { k }$ : The equation of the plane is $1 x + 1 y + 1 z =$ $d$ :

With the right choice $d = 1$ , this plane contains $P , Q , R$ . |Theeq|uatio| n is $x + y + z =$ 1:

EXAMPLE 8 What is the area of this same triangle PQR ?

Solution The area is half of the cross-product length $| \mathbf { A } \times \mathbf { B } | = | \mathbf { i } + \mathbf { j } + \mathbf { k } | = { \sqrt { 3 } }$ :

# DETERMINANTS AND VOLUMES

We are close to good algebra. The two plane vectors $a _ { 1 } \mathbf { i } + a _ { 2 } \mathbf { j }$ and $b _ { 1 } \mathbf { i } + b _ { 2 } \mathbf { j }$ are the sides of a parallelogram. Its area is $a _ { 1 } b _ { 2 } - a _ { 2 } b _ { 1 }$ , possibly witha sign change. There is a special way to write these four numbers—in a “square matrix.” There is also a name for the combination that leads to area. It is the “determinant of the matrix”:

$$
T h e m a t r i x ~ i s \left[ \begin{array} { l l } { a _ { 1 } } & { a _ { 2 } } \\ { b _ { 1 } } & { b _ { 2 } } \end{array} \right] , i t s d e t e r m i n a n t ~ i s \left| \begin{array} { l l } { a _ { 1 } } & { a _ { 2 } } \\ { b _ { 1 } } & { b _ { 2 } } \end{array} \right| = a _ { 1 } b _ { 2 } - a _ { 2 } b _ { 1 } .
$$

This is a 2 by 2 matrix (notice brackets) and a 2 by 2 determinant (notice vertical bars). The matrix is an array of four numbers and the determinant is one number:

$$
\begin{array}{c} \left. { \begin{array} { l l } { \operatorname { t s } ; { \left| \begin{array} { l l } { 2 } & { 1 } \\ { 4 } & { 3 } \end{array} \right| } = 6 - 4 = 2 , } \end{array} \right| } 2  & { 1 } \\ { \left| \begin{array} { l l } { 2 } & { 1 } \\ { 4 } & { 3 } \end{array} \right| } = 1 .  \end{array}
$$

The second has no area because $\mathbf { A } = \mathbf { B }$ : The third is a unit square . $( \mathbf { A } = \mathbf { i } , \mathbf { B } = \mathbf { j } )$ :

Now move to three dimensions, where determinants are most useful. The parallelogram becomes a parallelepiped. The word “box” is much shorter, and we will use it, but remember that the box is squashed. (Like a rectangle squashed to a parallelogram, the angles are generally not $9 0 ^ { \circ }$ .) |Th|e three e|dg|es from|th|e origin are $\mathbf { A } = ( a _ { 1 } , a _ { 2 } , a _ { 3 } ) , \mathbf { B } = ( b _ { 1 } , b _ { 2 } , b _ { 3 } ) , \mathbf { C } = ( c _ { 1 } , c _ { 2 } , c _ { 3 } )$ : Those edges are at right angles only when $\mathbf { A \cdot B } = \mathbf { A \cdot C } = \mathbf { B \cdot C } = 0$ :

Question: What is the volume of the box ? The right-angle case is easy—it is length times width times height. The volume is $\mathbf { \left| A \right| }$ times $\mathbf { \left| B \right| }$ times $| \mathbf { C } |$ , when the angle|s are $9 0 ^ { \circ }$ . For|a s|quashed box (Figure 11.15) we need the perpendicular height, not the sloping height.

There is a beautiful formula for volume. $\mathbf { B }$ and $\mathbf { C }$ give a parallelogram in the base, and $| \mathbf { B } \times \mathbf { C } |$ is the base area. This cross product points straight up. The third vector A points up at an angle—its perpendicularheight is $| \mathbf { A } | \cos \theta$ : Thu|s the volum |e is area $| \mathbf { B } \times \mathbf { C } |$ times $\mathbf { \left| A \right| }$ times cos $\theta$ : The volume is the dot product of A with $\mathbf { B } \times \mathbf { \partial }$ C:

Important: $\mathbf { A } \cdot ( \mathbf { B } \times \mathbf { C } )$ is a number, not a vector. This volume is zero when $\mathbf { A }$ is in the same plane as $\mathbf { B }$ and C (the box is totally flattened). Then $\mathbf { B } \times \mathbf { C }$ is perpendicular

to A and their dot product iszero.

$$
U s e f u l f a c t s : \quad \mathbf { A } \cdot ( \mathbf { B } \times \mathbf { C } ) = ( \mathbf { A } \times \mathbf { B } ) \cdot \mathbf { C } = \mathbf { C } \cdot ( \mathbf { A } \times \mathbf { B } ) = \mathbf { B } \cdot ( \mathbf { C } \times \mathbf { A } ) .
$$

All those come from the same box, with different sides chosen as base—but no change in volume. Figure 11.15 has $\mathbf { B }$ and C in the base but it can be A and $\mathbf { B }$ or $\mathbf { A }$ and $\mathbf { C }$ : The triple product $\mathbf { A } \cdot ( \mathbf { C } \times \mathbf { B } )$ has opposite sign, since $\mathbf { C } \times \mathbf { B } = - ( \mathbf { B } \times \mathbf { C } )$ . This order ACB is not cyclic like ABC and CAB and BCA:

To compute this triple product A $\mathbf { \nabla } \cdot ( \mathbf { B } \times \mathbf { C } )$ , we take $\mathbf { B } \times \mathbf { C }$ from equation (6):

$$
\mathbf { A } \cdot ( \mathbf { B } \times \mathbf { C } ) = a _ { 1 } ( b _ { 2 } c _ { 3 } - b _ { 3 } c _ { 2 } ) + a _ { 2 } ( b _ { 3 } c _ { 1 } - b _ { 1 } c _ { 3 } ) + a _ { 3 } ( b _ { 1 } c _ { 2 } - b _ { 2 } c _ { 1 } ) .
$$

The numbers $a _ { 1 } , a _ { 2 } , a _ { 3 }$ multiply 2 by 2 determinants to give a 3 by 3 determinant! There are three terms with plus signs (like $a _ { 1 } b _ { 2 } c _ { 3 }$ ). The other three have minus signs (like $- a _ { 1 } b _ { 3 } c _ { 2 } )$ . The plus terms have indices 123; 231; 312 in cyclic order. The minus terms have anticyclic indices 132; 213; 321: Again there is a special way to writethe nine components of $\mathbf { A } , \mathbf { B } , \mathbf { C } .$ —as a “3 by 3 matrix.” The combination in (9), which gives volume, is a “3 by 3 determinant:”

$$
\mathbf { m a t r i x } = \left[ { \begin{array} { l l l } { a _ { 1 } } & { a _ { 2 } } & { a _ { 3 } } \\ { b _ { 1 } } & { b _ { 2 } } & { b _ { 3 } } \\ { c _ { 1 } } & { c _ { 2 } } & { c _ { 3 } } \end{array} } \right] , \ \mathbf { d e t e r m i n a n t } = \mathbf { A } \cdot ( \mathbf { B } \times \mathbf { C } ) = \left| { \begin{array} { l l l } { a _ { 1 } } & { a _ { 2 } } & { a _ { 3 } } \\ { b _ { 1 } } & { b _ { 2 } } & { b _ { 3 } } \\ { c _ { 1 } } & { c _ { 2 } } & { c _ { 3 } } \end{array} } \right| .
$$

A single number is produced out of nine numbers, by formula .9/: The nine numbers are multiplied three at a time, as in $a _ { 1 } b _ { 1 } c _ { 2 }$ —except this product is not allowed. Each row and column must be represented once. This gives the six terms in the determinant:

$$
{ \left| \begin{array} { l l l } { a _ { 1 } } & { a _ { 2 } } & { a _ { 3 } } \\ { b _ { 1 } } & { b _ { 2 } } & { b _ { 3 } } \\ { c _ { 1 } } & { c _ { 2 } } & { c _ { 3 } } \end{array} \right| } = { \begin{array} { r } { a _ { 1 } b _ { 2 } c _ { 3 } + a _ { 2 } b _ { 3 } c _ { 1 } + a _ { 3 } b _ { 1 } c _ { 2 } } \\ { - a _ { 1 } b _ { 3 } c _ { 2 } - a _ { 2 } b _ { 1 } c _ { 3 } - a _ { 3 } b _ { 2 } c _ { 1 } } \end{array} }
$$

The trick is in the $\pm$ signs. Products down to the right are “plus”:

$$
{ \left| \begin{array} { l l l } { 2 } & { 1 } & { 1 } \\ { 1 } & { 2 } & { 1 } \\ { 1 } & { 1 } & { 2 } \end{array} \right| } = { \begin{array} { r } { 2 \cdot 2 \cdot 2 + 1 \cdot 1 \cdot 1 \cdot + 1 \cdot 1 \cdot 1 } \\ { - 2 \cdot 1 \cdot 1 - 1 \cdot 1 \cdot 2 - 1 \cdot 2 \cdot 1 } \end{array} } = { \begin{array} { r } { 8 + 1 + 1 } \\ { - 2 - 2 - 2 } \end{array} } = 4 .
$$

With practice the six products like 2 2 2 are done in your head. Write down only $8 + 1 + 1 - 2 - 2 - 2 = 4$ : This is the determinant and the volume.

Note the special case when the vectors are i; j; $\mathbf { k }$ : The box is a unit cube:

$$
{ \mathrm { v o l u m e ~ o f ~ c u b e } } = { \left| \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right| } = { \begin{array} { r l } { 1 + 0 + 0 } & { = 1 . } \\ { - 0 - 0 - 0 } & { } \end{array} }
$$

$H \mathbf { A } , \mathbf { B } , \mathbf { C }$ lie in the same plane,the v olume is z ero. A ze ro determinant is the test to see whether three vectors lie in a plane. Here row $\mathbf { A } = \operatorname { r o w } \mathbf { B } -$ row $\mathbf { C }$ :

$$
\left| { \begin{array} { r r r } { 0 } & { 1 } & { - 1 } \\ { - 1 } & { 1 } & { 0 } \\ { - 1 } & { 0 } & { 1 } \end{array} } \right| = { \begin{array} { r r r } { 0 \cdot 1 \cdot 1 + 1 \cdot 0 \cdot ( - 1 ) + ( - 1 ) \cdot ( - 1 ) \cdot 0 } & { } \\ { - 0 \cdot 0 \cdot 0 - 1 \cdot ( - 1 ) \cdot 1 - ( - 1 ) \cdot 1 \cdot ( - 1 ) } & { = 0 . } \end{array} }
$$

Zeros in the matrix simplify the calculation. All three products with plus signs— down to the right—are zero. The only two nonzero products cancel each other.

If the three $^ { - 1 }$ ’s are changed to $+ 1$ ’s, the determinant is $- 2$ : The determinant can be negative when all nine entries are positive! A negative determinant only means that the rows ${ \bf A } , { \bf B } , { \bf C }$ form a “left-handed triple.” This extra information from the sign—right-handed vs. left-handed—is free and useful, but the volume is the absolute value.

The determinant yields the volume also in higher dimensions. In physics, four dimensions give space-time. Ten dimensions give superstrings. Mathematics uses all dimensions. The 64 numbers in an 8 by 8 matrix give the volume of an eightdimensional box—with $8 ! = 4 0 , 3 2 0$ terms instead of $3 ! = 6$ : Under pressure from my class I omit the formula.

Question When is the point $( x , y , z )$ on the plane through the origin containing $\mathbf { B }$ and C ? For the vector $\mathbf { A } = x \mathbf { i } + y \mathbf { j } + z \mathbf { k }$ to lie in that plane, the volume $\mathbf { A } \cdot ( \mathbf { B } \times \mathbf { C } )$ must be zero. The equation of the plane is determinan $\prime = z e r o$ .

Follow this example for $\mathbf { B } = \mathbf { j } - \mathbf { i }$ and $\mathbf { C } = \mathbf { k } - \mathbf { i }$ to find the p lane parallel to $\mathbf { B }$ and C:

$$
\left| { \begin{array} { r r r } { x } & { y } & { z } \\ { - 1 } & { 1 } & { 0 } \\ { - 1 } & { 0 } & { 1 } \end{array} } \right| = \begin{array} { r } { x \cdot 1 \cdot 1 + y \cdot 0 \cdot ( - 1 ) + z \cdot 0 \cdot ( - 1 ) } \\ { - x \cdot 0 \cdot 0 - y \cdot 1 \cdot ( - 1 ) - z \cdot 1 \cdot ( - 1 ) } \end{array} = 0 .
$$

This equation is $x + y + z = 0$ : The normal vector $\mathbf { N } = \mathbf { B } \times \mathbf { C }$ has components $1 , 1 , 1$ :

# THE CROSS PRODUCT AS A DETERMINA NT

There is a connectionbetween 3 by 3 and 2 by 2 determ inants that you have to see. The numbers in the top row multiply determinants from the other rows:

$$
\left| { \begin{array} { c c c } { { \underline { { a _ { 1 } } } } } & { { a _ { 2 } } } & { { a _ { 3 } } } \\ { { b _ { 1 } } } & { { \underline { { b _ { 2 } } } } } & { { \underline { { b _ { 3 } } } } } \\ { { c _ { 1 } } } & { { c _ { 2 } } } & { { c _ { 3 } } } \end{array} } \right| = { \underline { { a _ { 1 } } } } \left| { \begin{array} { c c } { { \underline { { b _ { 2 } } } } } & { { \underline { { b _ { 3 } } } } } \\ { { c _ { 2 } } } & { { c _ { 3 } } } \end{array} } \right| - a _ { 2 } \left| { \begin{array} { c c } { { b _ { 1 } } } & { { b _ { 3 } } } \\ { { c _ { 1 } } } & { { c _ { 3 } } } \end{array} } \right| + a _ { 3 } \left| { \begin{array} { c c } { { b _ { 1 } } } & { { b _ { 2 } } } \\ { { c _ { 1 } } } & { { c _ { 2 } } } \end{array} } \right| .
$$

The highlighted product $a _ { 1 } ( b _ { 2 } c _ { 3 } - b _ { 3 } c _ { 2 } )$ gives two of the six terms. All six products contain an a and $b$ and $c$ from different columns. There are $3 ! = 6$ different orderings of columns 1; 2; 3: Note how $a _ { 3 }$ multiplies a determinant from columns 1 and 2:

Equation (13) is identical with equations (9) and (10). We are meeting the same six terms in different ways. The new feature is the minus sign in front of $a _ { 2 }$ —and the common mistake is to forget that sign. In a 4 by 4 determinant, $a _ { 1 } , - a _ { 2 } , a _ { 3 } , - a _ { 4 }$ would multiply 3 by 3 deter minants.

Now comes a key step. We write $\mathbf { A } \times \mathbf { B }$ as a determinant. Thevectors i; j; $\mathbf { k }$ go in the top row, the componentsof $\mathbf { A }$ and $\mathbf { B }$ go in the other rows. The “determinant” is exactly $\mathbf { A } \times \mathbf { B }$ :

$$
\mathbf { A \times B } = { \left| \begin{array} { l l l } { \mathbf { i } } & { \mathbf { j } } & { \mathbf { k } } \\ { { \underline { { a _ { 1 } } } } } & { a _ { 2 } } & { { \underline { { a _ { 3 } } } } } \\ { { \underline { { b _ { 1 } } } } } & { b _ { 2 } } & { { \underline { { b _ { 3 } } } } } \end{array} \right| } = \mathbf { i } { \left| \begin{array} { l l } { a _ { 2 } } & { a _ { 3 } } \\ { b _ { 2 } } & { b _ { 3 } } \end{array} \right| } - \mathbf { j } { \left| \begin{array} { l l } { { \underline { { a _ { 1 } } } } } & { { \underline { { a _ { 3 } } } } } \\ { { \underline { { b _ { 1 } } } } } & { { \underline { { b _ { 3 } } } } } \end{array} \right| } + \mathbf { k } { \left| \begin{array} { l l } { a _ { 1 } } & { a _ { 2 } } \\ { b _ { 1 } } & { b _ { 2 } } \end{array} \right| } .
$$

This time we highlighted the $\mathbf { j }$ component with its minus sign. There is no great mathematics in formula (14)—it is probably illegal to mix i; j; k with six numbers

# 11.3 Cross Products and Determinants

but it w orks. This is the good wayto remember and compute $\mathbf { A } \times \mathbf { B }$ : In the example $( \mathbf { j } - \mathbf { i } ) \times ( \mathbf { k } - \mathbf { i } )$ from equation (8), those two vectors go into the last two rows:

$$
\left| { \begin{array} { r r r } { \mathbf { i } } & { \mathbf { j } } & { \mathbf { k } } \\ { { \frac { - 1 } { - 1 } } } & { { \frac { 1 } { 2 } } } & { 0 } \\ { { \frac { - 1 } { - 1 } } } & { { \frac { 0 } { 2 } } } & { 1 } \end{array} }  \right| = \mathbf { i } \left| { \begin{array} { r r } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} } \right| - \mathbf { j } \left| { \begin{array} { r r } { - 1 } & { 0 } \\ { - 1 } & { 1 } \end{array} } \right| + \mathbf { \underline { { k } } } \left| { \begin{array} { r r } { { \frac { - 1 } { 1 } } } & { { \frac { 1 } { 3 } } } \\ { { \frac { - 1 } { - 1 } } } & { { \frac { 0 } { 2 } } } \end{array} } \right| = \mathbf { i } + \mathbf { j } + \mathbf { \underline { { k } } } .
$$

The $\mathbf { k }$ component is highlighted, to see $a _ { 1 } b _ { 2 } - a _ { 2 } b _ { 1 }$ again. Note the change from equation (11), which had $0 , 1 , - 1$ in the top row. That triple product was a number (zero). This cross product is a vector $\mathbf { i } + \mathbf { j } + \mathbf { k }$ :

Review question 1 With the i; j; k row changed to 3; 4; 5; what is the determinant ? Answer $3 \cdot 1 + 4 \cdot 1 + 5 \cdot 1 = 1 2$ : That triple product is the volume of a box.

Review question 2 When is $\mathbf { A } \times \mathbf { B } = \mathbf { 0 }$ and when is $\mathbf { A } \cdot ( \mathbf { B } \times \mathbf { C } ) = 0 ^ { \cdot }$ ? Zero vector, zero number.

Answer When A and $\mathbf { B }$ are on the same line. When A; B; C are in the same plane.

Reviewquestion 3 Does the parallelogram area $\left| \mathbf { A } \times \mathbf { B } \right|$ equal a 2 by 2 determinant ?

Answer If $\mathbf { A }$ and $\mathbf { B }$ lie in the $x y$ plane, yes. Generally no.

Review question 4 What are the vector triple products $( \mathbf { A } \times \mathbf { B } ) \times \mathbf { C }$ and $\mathbf { A } \times ( \mathbf { B } \times \mathbf { C } )$ ? Answer Not computed yet. These are two new vectors in Problem 47:

Review question 5 Find the plane through the origin containing $\mathbf { A } = \mathbf { i } + \mathbf { j } + 2 \mathbf { k }$ and $\mathbf { B } = \mathbf { i } + \mathbf { k }$ : Find the cross product of those same vectors $\mathbf { A }$ and $\mathbf { B }$ : Answer The position vector $\mathbf { P } = x \mathbf { i } + y \mathbf { j } + z \mathbf { k }$ is perpendicular to $\mathbf { N } = \mathbf { A } \times \mathbf { B }$ :

$$
\mathbf { P } \cdot ( \mathbf { A } \times \mathbf { B } ) = { \left| \begin{array} { l l l } { x } & { y } & { z } \\ { 1 } & { 1 } & { 2 } \\ { 1 } & { 0 } & { 1 } \end{array} \right| } = x + y - z = 0 . \mathbf { A } \times \mathbf { B } = { \left| \begin{array} { l l l } { \mathbf { i } } & { \mathbf { j } } & { \mathbf { k } } \\ { 1 } & { 1 } & { 2 } \\ { 1 } & { 0 } & { 1 } \end{array} \right| } = \mathbf { i } + \mathbf { j } - \mathbf { k } .
$$