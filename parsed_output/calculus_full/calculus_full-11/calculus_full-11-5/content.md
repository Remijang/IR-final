# 11.5 Linear Algebra

This section moves from two to three dimensions. There are three unknowns $x , y , z$ and also three equations. This is at the crossover point between formulas and algorithms—it is real linear algebra. The formulas give a direct solution using determinants. The algorithms use elimination and the numbers $x , y , z$ appear at the end. In practice that end result comes quickly. Computers solve linear equations by elimination.

The situation for a nonlinear equation is similar. Quadratic equations $a x ^ { 2 } + b x + c = 0$ are solved by a formula. Cubic equations are solved by Newton’s method (even though a formula exists). For equations involving $x ^ { 5 }$ or $x ^ { 1 0 }$ , algorithms take over completely.

Since we are at the crossover point, we look both ways. This section has a lot to do, in mixing geometry, determinants, and 3 by 3 matrices:

1: The row picture: three planes intersect at the solution   
2: The column picture: a vector equation combines the columns   
3: The formulas: determinants and Cramer’s Rule   
4: Matrix multiplication and $A ^ { - 1 }$   
5: The algorithm: Gaussian elimination.

Part of our goal is three-dimensional calculus. Another part is $n$ -dimensional algebra. And a third possibility is that you may not take mathematics next year. If that happens, I hope you will use mathematics. Linear equations are so basic and important, in such a variety of applications, that the effort in this section is worth making.

An example is needed. It is convenient and realistic if the matrix contains zeros. Most equations in practice are fairly simple—a thousand equations each with 990 zeros would be very reasonable. Hereare three equations in three unknowns:

$$
\begin{array} { l } { { x + { y } \quad \quad = \quad 1 } } \\ { { x \quad \quad + 2 z = \quad 0 } } \\ { { - 2 y + 2 z = - 4 . } } \end{array}
$$

In matrix-vector form, the unknown u has components $x , y , z$ : The right sides $1 , 0 , - 4$ go into $\mathbf { d }$ : The nine coefficients, including three zeros, enter the matrix $A$ :

$$
{ \left[ \begin{array} { l l l } { 1 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 2 } \\ { 0 } & { - 2 } & { 2 } \end{array} \right] } { \left[ \begin{array} { l } { x } \\ { y } \\ { z } \end{array} \right] } = { \left[ \begin{array} { l } { 1 } \\ { 0 } \\ { - 4 } \end{array} \right] } \quad { \mathrm { o r } } \quad A \mathbf { u } = \mathbf { d } .
$$

The goal is to understand that system geometrically, and then solve it.

# THE ROW PICTURE: INTERSECTING PLANES

Start with the first equation $x + y = 1$ : In the $x y$ plane that produces a line. In three dimensions it is a plane. It has the usual form $a x + b y + c z = d$ , except that $c$ happens to be zero. The plane is easy to visualize (Figure 11.20a), because it cuts straight down through the line. The equation $x + y = 1$ allows $z$ to have any value, so the graph includes all points above and below the line.

The second equation $x + 2 z = 0$ gives a second plane, which goes through the origin. When the right side is zero, the point $( 0 , 0 , 0 )$ satisfies the equation. This time $y$ is absent from the equation, so the plane contains the whole $y$ axis. All points $( 0 , y , 0 )$ meet the requirement $x + 2 z = 0$ : The normal vector to the plane is $\mathbf { N } =$ $\mathbf { i } + 2 \mathbf { k }$ : The plane cuts across, rather than down, in 11.20b.



Before the third equation we combine the first two. The intersection of two planes is a line. In three-dimensional space, two equations (not one) describe a line. The points on the line have to satisfy $x + y = 1$ and also $x + 2 z = 0$ : A convenient point is $P = ( 0 , 1 , 0 )$ : Another point is $\overset { \cdot } { Q } \overset { \cdot } { = } ( - 1 , 2 , \frac { 1 } { 2 } )$ : The line through $P$ and $\boldsymbol { Q }$ extends out in both directions.

The solution is on that line. The third plane decides where.

The third equation $- 2 y + 2 z = - 4$ gives the third plane—which misses the origin because the right side is not zero. What is important is the point where the three planes meet. The intersection line of the first two planes crosses the third plane. We used determinants (but elimination is better) to find $x = - 2$ ; $y = 3$ ; $z = 1$ : This solution satisfies the three equations and lies on the three planes.

A brief comment on 4 by 4 systems. The first equation might be $x + y + z - t = 0$ : It represents a three-dimensional “hyperplane” in four-dimensional space. (In physics this is space-time.) The second equation gives a second hyperplane, and its intersection with the first one is two-dimensional. The third equation (third hyperplane) reduces the intersection to a line. The fourth hyperplane meets that line at a point, which is the solution. It satisfies the four equations and lies on the four hyperplanes. In this course three dimensions are enough.

# COLUMN PICTURE: COMBINATION OF COLUMN VECTORS

There is an extremely important way to rewrite our three equations. In (1) they were separate, in (2) they went into a matrix. Now they becomea vector equation:

$$
x \left[ 1 \atop 1 \right] + y \left[ \begin{array} { r } { 1 } \\ { 0 } \\ { - 2 } \end{array} \right] + z \left[ \begin{array} { r } { 0 } \\ { 2 } \\ { 2 } \\ { 2 } \end{array} \right] = \left[ \begin{array} { r } { 1 } \\ { 0 } \\ { - 4 } \end{array} \right] .
$$

The columns of the matrix are multiplied by $x , y , z$ : That is a special way to see matrix-vector multiplication: Au is a combination of the columns of $A$ : We are looking for the numbers $x , y , z$ so that the combination produces the right side $\mathbf { d }$ :

The column vectors ${ \mathbf a } , { \mathbf b } , { \mathbf c }$ are shown in Figure 11.21a. The vector equation is $x \mathbf { a } + y \mathbf { b } + z \mathbf { c } = \mathbf { d } .$ : The combination that solves this equation must again be $x = - 2$ , $y = 3 , z = 1$ : That agrees with the intersection point of the three planes in the row picture.

# THE DETERMINANT AND THE INVERSE MATRIX

For a 3 by 3 determinant, the section on cross products gave two formulas. One was the triple product a $\mathbf { \nabla } \cdot ( \mathbf { b } \times \mathbf { c } )$ : The other wrote out the six terms:

$$
\operatorname { t } A = \mathbf { a } \cdot ( \mathbf { b } \times \mathbf { c } ) = a _ { 1 } ( b _ { 2 } c _ { 3 } - b _ { 3 } c _ { 2 } ) + a _ { 2 } ( b _ { 3 } c _ { 1 } - b _ { 1 } c _ { 3 } ) + a _ { 3 } ( b _ { 1 } c _ { 2 } - b _ { 2 } c _ { 1 } ) .
$$

Geometricallythis is the volume of abox. The columns ${ \mathbf a } , { \mathbf b } , { \mathbf c }$ are the edges going out from the origin. In our example the determinant and volume are 2:

$$
\begin{array} { r l } { \left| a _ { 1 } \quad b _ { 1 } \quad c _ { 1 } \right| = \left| { 1 } \quad { 1 } \quad { 0 } \right| } & { { } } \\ { \left| a _ { 2 } \quad b _ { 2 } \quad c _ { 2 } \right| = \left| { 1 } \quad { 0 } \quad { 2 } \right| = \quad } & { { } ( 1 ) ( 0 ) ( 2 ) - ( 1 ) ( - 2 ) ( 2 ) + ( 1 ) ( - 2 ) ( 0 ) } \\ { \left| a _ { 3 } \quad b _ { 3 } \quad c _ { 3 } \right| } & { { } = \left| { 0 } \quad { - 2 } \quad { 2 } \right| } \end{array} \quad \begin{array} { r l } { - ( 1 ) ( 1 ) ( 2 ) + ( 0 ) ( 1 ) ( 2 ) - ( 0 ) ( 0 ) ( 0 ) } & { { } = 2 . } \end{array}
$$

A slight dishonesty is present in that calculation, and will be admitted now. In Section 11.3 the vectors ${ \bf A } , { \bf B } , { \bf C }$ were rows. In this section ${ \mathbf a , \mathbf b , \mathbf c }$ are columns. It doesn’t matter, because the determinant is the same either way. Any matrix can be “transposed” —exchanging rows for columns—without altering the determinant. The six terms $\dot { \boldsymbol { a } } _ { 1 } \boldsymbol { b } _ { 2 } \boldsymbol { c } _ { 3 }$ is the first) may come in a different order, but they are the same six terms. Here four of those terms are zero, because of the zeros in the matrix. The sum of all six terms is $D = \det A = 2$ :

Since $D$ is not zero, the equations can be solved. The three planes meet at a point. The column vectors ${ \mathbf a } , { \mathbf b } , { \mathbf c }$ produce a genuine box, and are not flattened into the same plane (with zero volume). The solution involves dividing by $D$ —which is only possible if $D = \operatorname* { d e t } A$ is not zero.

11L When the determinant $D$ is not zero, $A$ bas an inverse: $A A ^ { - 1 } = A ^ { - 1 }$ $A = I$ : Then the equations $\boldsymbol { A } \mathbf { u } = \mathbf { d }$ have one and only one solution $\mathbf { u } = A ^ { - 1 } \mathbf { d }$ :

The 3 by 3 identity matrix $I$ is at the end of equation (5). Always $I \mathbf { u } = \mathbf { u }$ : We now compute $A ^ { - 1 }$ ; first with letters and then with numbers. The neatest formula uses cross products of the columns of $A$ —it is special for 3 by 3 matrices.

Every entry is divided by $D$ : The inverse matrix is $\boldsymbol { A } ^ { - 1 } = \frac { 1 } { D } \left[ \begin{array} { l } { \mathbf { b } \times \mathbf { c } } \\ { \mathbf { c } \times \mathbf { a } } \\ { \mathbf { a } \times \mathbf { b } } \end{array} \right] .$

To test this formula, multiply by $A$ : Matrix multiplication produces a matrix of dot products—from the rows of the first matrix and the columns of the second, $A ^ { - 1 } A =$

I :

$$
{ \frac { 1 } { D } } { \left[ \begin{array} { l } { \mathbf { b } \times \mathbf { c } } \\ { \mathbf { c } \times \mathbf { a } } \\ { \mathbf { a } \times \mathbf { b } } \end{array} \right] } { \left[ \begin{array} { l l } { \mathbf { a } } & { \mathbf { b } } & { \mathbf { c } } \\ { \mathbf { a } } & { \mathbf { b } } & { \mathbf { c } } \\ { \mathbf { a } \times \mathbf { a } } & { \mathbf { b } } \end{array} \right] } = { \frac { 1 } { D } } { \left[ \begin{array} { l } { \mathbf { a } \cdot ( \mathbf { b } \times \mathbf { c } ) \ \mathbf { b } \cdot ( \mathbf { b } \times \mathbf { c } ) \ \mathbf { c } \cdot ( \mathbf { b } \times \mathbf { c } ) } \\ { \mathbf { a } \cdot ( \mathbf { c } \times \mathbf { a } ) \ \mathbf { b } \cdot ( \mathbf { c } \times \mathbf { a } ) \ \mathbf { c } \cdot ( \mathbf { c } \times \mathbf { a } ) } \\ { \mathbf { a } \cdot ( \mathbf { a } \times \mathbf { b } ) \ \mathbf { b } \cdot ( \mathbf { a } \times \mathbf { b } ) \ \mathbf { c } \cdot ( \mathbf { a } \times \mathbf { b } ) } \end{array} \right] } = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } .
$$

On the right side, six of the triple products are zero. They are the off-diagonals like ${ \bf b } \cdot ( { \bf b } \times { \bf c } )$ , which contain the same vector twice. Since $\mathbf { b } \times \mathbf { c }$ is perpendicular to $\mathbf { b }$ , this triple product is zero. The same is true of the others, like $\mathbf { a } \cdot ( \mathbf { a } \times \mathbf { b } ) = 0$ : That is the volume of a box with two identical sides. The six off-diagonal zeros are the volumes of completely flattened boxes.

On the main diagonal the triple products equal $D$ : The order of vectors can be abc or bca or cab, and the volume of the box stays the same. Dividing by thisnumber $D$ , which is placed outside for that purpose, gives the 1’s in the identity matrix $I$ :

Now we change to numbers. The goal isto find $A ^ { - 1 }$ and to test it.

EXAMPLE 1 The inverse of $A = \left[ 1 \begin{array} { r r } { { 1 } } & { { 1 } } & { { 0 } } \\ { { 1 } } & { { 0 } } & { { 2 } } \\ { { 0 } } & { { - 2 } } & { { 2 } } \end{array} \right] i s { \cal A } ^ { - 1 } = \frac { 1 } { 2 } \left[ \begin{array} { r r } { { 4 } } & { { - 2 } } & { { 2 } } \\ { { - 2 } } & { { 2 } } & { { - 2 } } \\ { { - 2 } } & { { 2 } } & { { - 1 } } \end{array} \right] .$

That comes from the formula, and it absolutely has to be checked. Do not fail to multiply $A ^ { - 1 }$ times $A$ (or $A$ times $A ^ { - 1 }$ ). Matrix multiplication is much easier than the formula for $A ^ { - 1 }$ : Wehighlight row 3times column 1, with dot product zero:

$$
\frac { 1 } { 2 } \left[ \begin{array} { r r } { 4 \mathrm { ~ - } 2 } & { 2 } \\ { - 2 } & { 2 \mathrm { ~ - } 2 } \\ { - 2 } & { 2 \mathrm { ~ - } 1 } \end{array} \right] \left[ \begin{array} { r r } { 1 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 2 } \\ { 0 } & { - 2 } & { 2 } \end{array} \right] = \frac { 1 } { 2 } \left[ \begin{array} { r r } { 4 \mathrm { - } 2 } & { 4 \mathrm { - } 4 } & { - 4 \mathrm { + } 4 } \\ { - 2 \mathrm { + } 2 } & { - 2 \mathrm { + } 4 } & { 4 \mathrm { - } 4 } \\ { - 2 \mathrm { + } 2 } & { - 2 \mathrm { + } 2 } & { 4 \mathrm { - } 2 } \end{array} \right] = \left[ \begin{array} { r r } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] .
$$

Remark on $A ^ { - 1 }$ Inverting a matrix requires $D \neq 0$ : We divide by $D = \operatorname* { d e t } A$ : The cross products ${ \bf b } \times { \bf c }$ and $\mathbf { c } \times \mathbf { a }$ and $\mathbf { a } \times \mathbf { b }$ give $A ^ { - 1 }$ in a neat form, but errors are easy. We prefer to avoid writing i; j; $\mathbf { k }$ : There are nine 2 by 2 determinants to be calculated, and here is $A ^ { - 1 }$ in full—containing the nine “cofactors” divided by $D$ :

$$
A ^ { - 1 } = \frac { 1 } { D } \left[ \begin{array} { l l l } { b _ { 2 } c _ { 3 } - b _ { 3 } c _ { 2 } } & { b _ { 3 } c _ { 1 } - b _ { 1 } c _ { 3 } } & { b _ { 1 } c _ { 2 } - b _ { 2 } c _ { 1 } } \\ { c _ { 2 } a _ { 3 } - c _ { 3 } a _ { 2 } } & { c _ { 3 } a _ { 1 } - c _ { 1 } a _ { 3 } } & { c _ { 1 } a _ { 2 } - c _ { 2 } a _ { 1 } } \\ { a _ { 2 } b _ { 3 } - a _ { 3 } b _ { 2 } } & { a _ { 3 } b _ { 1 } - a _ { 1 } b _ { 3 } } & { a _ { 1 } b _ { 2 } - a _ { 2 } b _ { 1 } } \end{array} \right] .
$$

Important: The first row of $A ^ { - 1 }$ does not use the first column of $A$ , except in $1 / D$ : In other words, $\mathbf { b } \times \mathbf { c }$ does not involve a: Here are the 2 by 2 determinants that produce $4 , - 2 , 2$ —which is divided by $D = 2$ in the top row of $A ^ { - 1 }$ :

$$
\begin{array} { r l r } { \left[ { \begin{array} { r r r } { 1 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 2 } \\ { 0 } & { - 2 } & { 2 } \end{array} } \right] \left[ { \begin{array} { r r r } { 1 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 2 } \\ { 0 } & { - 2 } & { 2 } \end{array} } \right] \left[ { \begin{array} { r r r } { 1 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 2 } \\ { 0 } & { - 2 } & { 2 } \end{array} } \right] } & { } & { \left[ { \begin{array} { r r r } { + } & { - } & { + } \\ { - } & { + } & { - } \\ { + } & { - } & { + } \end{array} } \right] . } \end{array}
$$

The second highlighted determinant looks like $+ 2$ not $- 2$ : But the sign matrix on the right assigns a minus to that position in $A ^ { - 1 }$ : We reverse the sign of $b _ { 1 } c _ { 3 } - b _ { 3 } c _ { 1 }$ , to find the cofactor $b _ { 3 } c _ { 1 } - b _ { 1 } c _ { 3 }$ in the top row of (6).

To repeat: For a row of $A ^ { - 1 }$ ; cross out the corresponding column of A: Find the three 2 by 2 determinants, use the sign matrix, and divide by $D$ :

$$
B = { \left[ \begin{array} { l l l } { 1 } & { 1 } & { 1 } \\ { 0 } & { 1 } & { 1 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } { \mathrm { ~ h a s ~ } } D = 1 { \mathrm { ~ a n d ~ } } B ^ { - 1 } = { \left[ \begin{array} { l l l } { 1 } & { - 1 } & { ~ 0 } \\ { 0 } & { ~ 1 } & { - 1 } \\ { 0 } & { ~ 0 } & { ~ 1 } \end{array} \right] } .
$$

The multiplication $B B ^ { - 1 } = I$ checks the arithmetic. Notice how $\begin{array} { c c } { { 1 } } & { { 1 } } \\ { { 1 } } & { { 1 } } \end{array}$ in $B$ leads to a zero in the top row of $B ^ { - 1 }$ : To find row 1, column 3 of $B ^ { - 1 }$ we ignore column 1 and row 3 of $B$ : (Also: the inverse of a triangular matrix is triangular.) The minus signs come from the sign matrix.

$$
\mathsf { T H E S O L U T I O N u } = A ^ { - 1 } \mathbf { d }
$$

The purpose of $A ^ { - 1 }$ is to solve the equation $A \mathbf { u } = \mathbf { d }$ : Multiplying by $A ^ { - 1 }$ produces $I \mathbf { u } = A ^ { - 1 } \mathbf { d }$ : The matrix becomes the identity, $\boldsymbol { I \mathbf { u } }$ equals $\mathbf { u }$ , and the solution is immediate:

$$
\mathbf { u } = A ^ { - 1 } \mathbf { d } = { \frac { 1 } { D } } { \left[ \begin{array} { l } { \mathbf { b } \times \mathbf { c } } \\ { \mathbf { c } \times \mathbf { a } } \\ { \mathbf { a } \times \mathbf { b } } \end{array} \right] } { \left[ \begin{array} { l } { \mathbf { d } } \\ { \mathbf { d } } \\ { \mathbf { a } } \end{array} \right] } = { \frac { 1 } { D } } { \left[ \begin{array} { l } { \mathbf { d } \cdot ( \mathbf { b } \times \mathbf { c } ) } \\ { \mathbf { d } \cdot ( \mathbf { c } \times \mathbf { a } ) } \\ { \mathbf { d } \cdot ( \mathbf { a } \times \mathbf { b } ) } \end{array} \right] } .
$$

By writing those components $x , y , z$ a|s ratios o|f determ| inants, |we have|Cramer’s Rule:

$$
\begin{array} { r } { [ \mathbb { 1 } \mathbb { M } ( \boldsymbol { C } \boldsymbol { r } a m e r ^ { \prime } s \boldsymbol { R } u l e )  \quad } \\ {  \qquad \mathrm { T h e ~ s o l u t i o n ~ i s ~ } x = \displaystyle \frac { | \textbf { d b c } | } { | \textbf { a b c } | } , \quad y = \displaystyle \frac { | \textbf { a d c } | } { | \textbf { a b c } | } , \quad z = \displaystyle \frac { | \textbf { a b d } | } { | \textbf { a b c } | } . } \end{array}
$$

The right side $\mathbf { d }$ replaces, in turn, columns a and $\mathbf { b }$ and c: All denominators are $D = \mathbf { a } \cdot ( \mathbf { b } \times \mathbf { c } )$ : The numerator of $x$ is the determinant $\mathbf { d } \cdot ( \mathbf { b } \times \mathbf { c } )$ in (9). The second numerator agrees with the second component ${ \bf d } \cdot ( { \bf c } \times { \bf a } )$ , because the cyclic order is correct. The third determinant with columns abd equals the triple product $\mathbf { d } \cdot ( \mathbf { a } \times \mathbf { b } )$ in $A ^ { - 1 } \mathbf { u }$ : Thus (10) is the sameas (9).

EXAMPLE A: Multiply by $A ^ { - 1 }$ tofind theknown solution $x = - 2 , y = 3 , z = 1$ :

$$
\mathbf { u } = A ^ { - 1 } \mathbf { d } = { \frac { 1 } { 2 } } { \left[ \begin{array} { l l l } { \quad 4 } & { - 2 } & { \quad 2 } \\ { - 2 } & { \quad 2 } & { - 2 } \\ { - 2 } & { \quad 2 } & { - 1 } \end{array} \right] } { \left[ \begin{array} { l } { \ 1 } \\ { \ 0 } \\ { - 4 } \end{array} \right] } = { \frac { 1 } { 2 } } { \left[ \begin{array} { l } { \ 4 - 8 } \\ { - 2 + 8 } \\ { - 2 + 4 } \end{array} \right] } = { \left[ \begin{array} { l } { - 2 } \\ { \ 3 } \\ { \ 1 } \end{array} \right] } .
$$

EXAMPLE B: Multiply by $B ^ { - 1 }$ to solve $B \mathbf { u } = \mathbf { d }$ when $\mathbf { d }$ is the column .6; 5; 4/:

$$
\mathbf { u } = B ^ { - 1 } \mathbf { d } = { \left[ \begin{array} { l l l } { 1 } & { - 1 } & { ~ 0 } \\ { 0 } & { ~ 1 } & { - 1 } \\ { 0 } & { ~ 0 } & { ~ 1 } \end{array} \right] } { \left[ \begin{array} { l } { 6 } \\ { 5 } \\ { 4 } \end{array} \right] } = { \left[ \begin{array} { l } { 1 } \\ { 1 } \\ { 4 } \end{array} \right] } . \quad C h e c k \ B \mathbf { u } = { \left[ \begin{array} { l l l } { 1 } & { 1 } & { 1 } \\ { 0 } & { 1 } & { 1 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l } { 1 } \\ { 1 } \\ { 4 } \end{array} \right] } = { \left[ \begin{array} { l } { 6 } \\ { 5 } \\ { 4 } \end{array} \right] } .
$$

EXAMPLE C: Put $\mathbf { d } = ( 6 , 5 , 4 )$ in each column of $B$ : Cramer’s Rule gives $\mathbf { u } =$ .1; 1; 4/:

$$
{ \left| \begin{array} { l l l } { 6 } & { 1 } & { 1 } \\ { 5 } & { 1 } & { 1 } \\ { 4 } & { 0 } & { 1 } \end{array} \right| } = 1 \left| { \begin{array} { l l l } { 1 } & { 6 } & { 1 } \\ { 0 } & { 5 } & { 1 } \\ { 0 } & { 4 } & { 1 } \end{array} } \right| = 1 \left| { \begin{array} { l l l } { 1 } & { 1 } & { 6 } \\ { 0 } & { 1 } & { 5 } \\ { 0 } & { 0 } & { 4 } \end{array} } \right| = 4 \ \mathrm { a l l ~ d i v i d e d ~ b y } \ D = { \left| \begin{array} { l l l } { 1 } & { 1 } & { 1 } \\ { 0 } & { 1 } & { 1 } \\ { 0 } & { 0 } & { 1 } \end{array} \right| } = 1 .
$$

This rule fills the page with determinants. Those are good ones to check by eye, without writing down the six terms (three $+$ and three ).

The formulas for $A ^ { - 1 }$ are honored chiefly in their absence. They are not used by the computer, even though the algebra is in some ways beautiful. In big calculations, the computer never finds $A ^ { - 1 }$ —just the solution.

We now look at the singular case $D = 0$ : Geometry-algebra-algorithm must all break down. After that is the algorithm: Gaussian elimination.

# THE SINGULAR CASE

Changing one entry of a matrix can make the determinant zero. The triple product $\mathbf { a } \cdot ( \mathbf { b } \times \mathbf { c } )$ , which is also the volume, becomes $D = 0$ : The box is flattened and the matrix is singular. That happensin our example when the lower right entry is changed from 2 to 4:

$$
S = { \left[ \begin{array} { l l l } { 1 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 2 } \\ { 0 } & { - 2 } & { 4 } \end{array} \right] } { \mathrm { ~ h a s ~ d e t e r m i n a n t ~ } } D = 0 .
$$

This does more than change the inverse. It destroys the inverse. We can no longer divide by $D$ : There is no $S ^ { - 1 }$ :

What happens to the row picture and column picture ? For 2 by 2 systems, the singular case had two parallel lines. Now the row picture has three planes, which need not be parallel. Here the planes are not parallel. Their normal vectors are the rows of $S$ , which go in different directions. But somehow the planes fail to go through a common point.

What happens is more subtle. The intersection line from two planes misses the third plane. The line is parallel to the plane and stays above it (Figure 11.22)a. When all three planes are drawn, they form an open tunnel. The picture tells more than the numbers, about how three planes can fail to meet. The third figure shows an end view, where the planes go directly into the page. Each pair meets in a line, but those lines don’t meet in a point.

When two planes are parallel, the determinant is again zero. One row of the matrix is a multiple of another row. The extreme case has all three planes parallel—as in a matrix with nine 1’s.

The column picture must also break down. In the 2 by 2 failure (previous section), the columns were on the same line. Now the three columns are in the same plane. The combinations of those columns produce d only if it happens to lie in that particular plane. Most vectors $\mathbf { d }$ will be outside the plane, so most singular systems have no solution.

When the determinant is zero, $\boldsymbol { A } \mathbf { u } = \mathbf { d }$ has no solution or infinitely many.

# THE ELIMINATION ALGORITHM

Go back to the 3 by 3 example $\scriptstyle A \mathbf { u } = \mathbf { d }$ : If you were given those equations, you would never think of determinants. You would—quite correctly—start with the first equation. It gives $x = 1 - y$ , which goes into the next equation toeliminate $x$ :

$$
\begin{array} { l c l } { { x + } } & { { y } } & { { = } } & { { 1 } } \\ { { x } } & { { + 2 z = } } & { { 0 } } & { { { \xrightarrow { x = 1 - y } } } } \\ { { } } & { { - 2 y + 2 z = - 4 } } & { { - 2 y + 2 z = - 4 . } } \end{array}
$$

Stop there for a minute. On the right is a 2 by 2 system for $y$ and $z$ : The first equation and first unknown are eliminated—exactly what we want. But that step was not organized in the best way, because a “1” ended up on the left side. Constants should stay on the right side—the pattern should be preserved. It is better to take the same step by subtracting the first equation from the second:

$$
\begin{array} { l } { { x + \ y \qquad = \ 1 } } \\ { { x \qquad + 2 z = \ 0 \qquad \quad \qquad \qquad \ - \ y + 2 z = - 1 } } \\ { { - 2 y + 2 z = - 4 \qquad \qquad \quad - 2 y + 2 z = - 4 . } } \end{array}
$$

Same equations, better organization. Now look at the corner term $- y$ : Its coefficient $^ { - 1 }$ is the second pivot. (The first pivot was $+ 1$ , the coefficient of $x$ in the first corner.) We are ready for the next elimination step:

Plan: Subtract a multiple of the “pivoÑt equation” from the equation below it. Goal: To produce a zero below the pivot, so $y$ is eliminated. Method: Subtract 2 times the pivot equation to cancel $- 2 y$ :

$$
\begin{array} { c } { { - \ y + 2 z = - 1 } } \\ { { - 2 y + 2 z = - 4 } } \end{array} \to \ _ { - 2 z = - 2 . }
$$

The answer comes by back substitution. Equation (12) gives $z = 1$ : Then equation (11) gives $y = 3$ : Then the first equation gives $x = - 2$ : This is much quicker than determinants. You may ask: Why use Cramer’s Rule ? Good question.

With numbers elimination is better. It is faster and also safer. (To check against error, substitute $^ { - 2 , 3 , 1 }$ into the original equations.) The algorithm reaches the answer without the determinant and without the inverse. Calculations with letters use det $A$ and $A ^ { - 1 }$ :

Here are the steps in a definite order (top to bottom):

Subtract a multiple of equation 1 to produce $0 x$ in equation 2   
Subtract a multiple of equation 1 to produce $0 x$ in equation 3   
Subtract a multiple of equation 2 (new) to produce $0 y$ in equation 3

EXAMPLE (notice the zeros appearing under the pivots):

$$
{ \begin{array} { r l r } { \quad } & { \mathbf { \psi } _ { x } + \ \mathbf { \psi } _ { y } + \ \mathbf { \psi } _ { z } = \ 1 } & { \quad x + \ \mathbf { \psi } _ { y } + \ \mathbf { \psi } _ { z } = 1 } & { \quad x + \ \mathbf { \psi } _ { y } + \mathbf { \psi } _ { z } = 1 } \\ { 2 x + 5 { \mathbf { \psi } } _ { y } + 3 z = \ 7 } & {  } & { 3 y + \ z = 5 \  } & { \quad 3 y + z = 5 } \\ { 4 x + 7 y + 6 z = 1 1 } & { \quad 3 y + 2 z = 7 } & { \quad z = 2 . } \end{array} }
$$

Elimination leads to a triangular system. The coefficients below the diagonal are zero.

First $z = 2$ , then $y = 1$ , then $x = - 2$ :Back substitution solves triangular systems (fast).

As a final example, try the singular case $S \mathbf { u } = \mathbf { d }$ when the corner entry is changed from 2 to 4: With $D = 0$ , there is no inverse matrix $S ^ { - 1 }$ : Elimination also fails, by reachingan impossibleequation $0 = - 2$ :

$$
\begin{array} { l c r } { { x + y \quad \quad = \quad 1 \quad \quad x + \ y \quad \quad = \quad 1 \quad \quad x + y \quad \quad = \quad 1 \quad \quad x + y \quad \quad = \quad 1 } } \\ { { x \quad \quad + 2 z = \quad 0  \quad - \quad y + 2 z = - 1  \quad - y + 2 z = - 1 } } \\ { { - 2 y + \underline { { { 4 } } } z = - 4 \quad \quad \quad - 2 y + \underline { { { 4 } } } z = - 4 \quad \quad \quad \quad \quad 0 = - 2 } } \end{array}
$$

The three planes do not meet at a point—a fact that was not obvious at the start. Algebra discovers this fact from $D = 0$ : Elimination discovers it from $0 = - 2$ : The chapter is ending at the point where my linear algebra book begins.

One final comment. In actual computing, you will use a code written by professionals. The steps will be the same as above. A multiple of equation 1 is subtracted from each equation below it, to eliminate the first unknown $x$ : With one fewer unknown and equation, elimination starts again. (A parallel computer executes many steps at once.) Extra instructions are included to reduce roundoff error. You only see the result! But it is more satisfying to know what the computer is doing.

In the end, solving linear equations is the key step in solving nonlinear equations. The central idea of differential calculus is to linearize near a point.