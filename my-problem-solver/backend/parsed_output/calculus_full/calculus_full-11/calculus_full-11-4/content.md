# 11.4 Matrices and Linear Equations

We are moving from geometry to algebra. Eventually we get back to calculus, where functions are nonlinear—but linear equations come first. In Chapter 1, $y = m x + b$ produced a line. Two equations produce two lines. If they cross, the intersection point solves both equations—and we want to find it.

Three equations in three variables $x , y , z$ produce three planes. Again they go through one point (usually). Again the problem is to find that intersection point —which solves the three equations.

The ultimate problem is to solve $n$ equations in $n$ unknowns. There are $n$ hyperplanes in $n$ -dimensional space, which meet at the solution. We need a test to be sure they meet. We also want the solution. These are the objectives of linear algebra, which joins with calculus at the center of pure and applied mathematics.

Like every subject, linear algebra requires a good notation. To state the equations and solve them, we introduce a “matrix.” The problem will be $A \mathbf { u } = \mathbf { d }$ : The solution will be $\mathbf { u } = A ^ { - 1 } \mathbf { d }$ . It remains to understand where the equations come from, where the answer comes from, and what the matrices $A$ and $A ^ { - 1 }$ stand for.

# TWO EQUATIONS IN TWO UNKNOWNS

Linear algebra has no reason to choose one variable as special. The equation $y -$ $y _ { 0 } = m ( x - x _ { 0 } )$ separates $y$ from $x$ : A better equation for a line is $a x + b y = d$ : (A vertical line like $x = 5$ appears when $b = 0$ : The first form did not allow slope $m = \infty$ :) This section studies two lines:

$$
\begin{array} { l } { { a _ { 1 } x + b _ { 1 } y = d _ { 1 } } } \\ { { a _ { 2 } x + b _ { 2 } y = d _ { 2 } . } } \end{array}
$$

By solving both equations at once, we are asking $( x , y )$ to lie on both lines. The practical question is: Where do the lines cross ? The mathematician’s question is: Does a solution exist and is it unique ?

To understand everything is not possible. There are parts of life where you never know what is going on (until too late). But two equations in two unknowns can have no mysteries. There are three ways to write the system—by rows, by columns, and by matrices. Please look at all three, since setting up a problem is generally harder and more important than solving it. After that comes the concession to the real world: we compute $x$ and $y$ :

EXAMPLE 1 How do you invest $\$ 5000$ to earn $\$ 400$ a year interest, if a money market account pays $5 \%$ and a deposit account pays $10 \%$ ?

Set up equations by rows: With $x$ dollars at $5 \%$ the interest is . $0 5 x$ : With $y$ dollars at $10 \%$ the interest is . $1 0 y$ : One row for principal, another row for interest:

$$
\begin{array} { c } { { x + y = 5 0 0 0 } } \\ { { . 0 5 x + . 1 0 y = 4 0 0 . } } \end{array}
$$

# 11.4 Matrices and Linear Equations

Same equations by columns: The left side of (2) contains $x$ times one vector plus $y$ times another vector. The right side is a third vector. The equation by columns is

$$
x \left[ { \begin{array} { c } { 1 } \\ { . 0 5 } \end{array} } \right] + y \left[ { \begin{array} { c } { 1 } \\ { . 1 0 } \end{array} } \right] = \left[ { \begin{array} { c } { 5 0 0 0 } \\ { 4 0 0 } \end{array} } \right] .
$$

Same equations by matrices: Look again at the left side. There are two unknowns $x$ and $y$ ; which go into a vector $\mathbf { u }$ : They are multiplied by the four numbers 1; .05; 1; and .10; which go into a two by two matrix $A$ : The left side becomes $\pmb { a }$ matrix times $\pmb { a }$ vector:

$$
A \mathbf { u } = { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { . 0 5 } & { . 1 0 } \end{array} \right] } { \left[ \begin{array} { l } { x } \\ { y } \end{array} \right] } = { \left[ \begin{array} { l } { 5 0 0 0 } \\ { 4 0 0 } \end{array} \right] } .
$$

Now you see where the “rows” and “columns” came from. They are the rows and columns of a matrix. The rows entered the separate equations (2). The columns entered the vector equation (3). The matrix-vector multiplication $\boldsymbol { A } \mathbf { u }$ is defined so that all these equations are the same:

$$
{ \begin{array} { r l r } { A \mathbf { u } \mathbf { b } \operatorname { y } \operatorname { r o w s } : } & { { \left[ \begin{array} { l l } { a _ { 1 } } & { b _ { 1 } } \\ { a _ { 2 } } & { b _ { 2 } } \end{array} \right] } { \left[ \begin{array} { l } { x } \\ { y } \end{array} \right] } = { \left[ \begin{array} { l l } { a _ { 1 } x + b _ { 1 } y } \\ { a _ { 2 } x + b _ { 2 } y } \end{array} \right] } } & { { \mathrm { ( e a c h ~ r o w ~ i s ~ ) } } } \\ { \mathbf { 1 } \mathbf { u } \operatorname { b } \operatorname { y } \operatorname { c o l u m n s } : } & { { \left[ \begin{array} { l l } { a _ { 1 } } & { b _ { 1 } } \\ { a _ { 2 } } & { b _ { 2 } } \end{array} \right] } { \left[ \begin{array} { l } { x } \\ { y } \end{array} \right] } = x { \left[ \begin{array} { l } { a _ { 1 } } \\ { a _ { 2 } } \end{array} \right] } + y { \left[ \begin{array} { l } { b _ { 1 } } \\ { b _ { 2 } } \end{array} \right] } } & { { \mathrm { ( c o m b i n a t i o n ~ o f ~ } } } \end{array} }
$$

$A$ is the coefficient matrix. The unknown vector is $\mathbf { u }$ : The known vector on the right side, with components 5000 and 400; is $\mathbf { d }$ : The matrix equation is $A \mathbf { u } = \mathbf { d }$ :

This notation $\scriptstyle A \mathbf { u } = \mathbf { d }$ continues to apply when there are more equations and more unknowns. The matrix $A$ has a row for each equation (usually m rows). It has a column for each unknown (usually $n$ columns). For 2 equations in 3 unknowns it is a 2 by 3 matrix (therefore rectangular). For 6 equations in 6 unknowns the matrix is 6 by 6 (therefore square). The best way to get familiar with matrices is to work with them. Note also the pronunciation: “matrisees” and never “matrixes.”

Answer to the practical question The solution is $x = 2 0 0 0$ ; $y = 3 0 0 0$ : That is the intersection point in the row picture (Figure 11.16). It is also the correct combination in the column picture. The matrix equation checks both at once, because matrices are multiplied by rows or by columns. The product either way is $\mathbf { d }$ :

$$
\left[ \begin{array} { c c } { 1 } & { 1 } \\ { . 0 5 } & { . 1 0 } \end{array} \right] \left[ \begin{array} { c } { 2 0 0 0 } \\ { 3 0 0 0 } \end{array} \right] = \left[ \begin{array} { c } { 2 0 0 0 + } \\ { ( . 0 5 ) 2 0 0 0 + ( . 1 0 ) 3 0 0 0 } \end{array} \right] = \left[ \begin{array} { c } { 5 0 0 0 } \\ { 4 0 0 } \end{array} \right] = \mathbf { d } .
$$

Singular case In the row picture, the lines cross at the solution. But there is a case that gives trouble. When the lines are parallel, they never cross and there is no solution. When the lines are the same, there is an infinity of solutions:

$$
\begin{array} { c c c } { { } } & { { 2 x + y = 0 } } & { { 2 x + y = 0 } } \\ { { } } & { { 2 x + y = 1 } } & { { s a m e l i n e } } & { { 4 x + 2 y = 0 } } \end{array}
$$

This trouble also appears in the column picture. The columns are vectors a and b: The equation $A \mathbf { u } = \mathbf { d }$ is the same as $x \mathbf { a } + y \mathbf { b } = \mathbf { d }$ : We are asked to find the combination of a and $\mathbf { b }$ (with coefficients $x$ and $y$ ) that produces $\mathbf { d }$ : In the singular case a and $\mathbf { b }$ lie along the same line (Figure 11.17). No combination can produce $\mathbf { d }$ ; unless it happens to lie on this line.

The investment problem is nonsingular, and $2 0 0 0 { \bf a } + 3 0 0 0 { \bf b }$ equals $\mathbf { d }$ : We also drew

EXAMPLE 2 : The matrix $A$ multiplies $\mathbf { u } = ( 1 , 1 )$ to solve $x + 2 y = 3$ and $x - y =$ 0:

$$
A \mathbf { u } = { \left[ \begin{array} { l l } { 1 } & { 2 } \\ { 1 } & { - 1 } \end{array} \right] } { \left[ \begin{array} { l } { 1 } \\ { 1 } \\ { 1 } \end{array} \right] } = { \left[ \begin{array} { l } { 1 + 2 } \\ { 1 - 1 } \end{array} \right] } = { \left[ \begin{array} { l } { 3 } \\ { 0 } \\ { 0 } \end{array} \right] } . \quad \mathrm { B y ~ c o l u m n s } { \left[ \begin{array} { l } { 1 } \\ { 1 } \\ { 1 } \end{array} \right] } + { \left[ \begin{array} { l } { 2 } \\ { - 1 } \end{array} \right] } = { \left[ \begin{array} { l } { 3 } \\ { 0 } \\ { 0 } \end{array} \right] } .
$$

The crossing point is $( 1 , 1 )$ in the row picture. The solution is $x = 1 , y = 1$ in the column picture (Figure 11.17b). Then 1 times a plus 1 times $\mathbf { b }$ equals the right side $\mathbf { d }$ :

# SOLUTION BY DETERMINANTS

Up to now we just wrote down the answer. The real problem is to find $x$ and $y$ when they are unknown. We solve two equations with letters not numbers:

$$
\begin{array} { l } { { a _ { 1 } x + b _ { 1 } y = d _ { 1 } } } \\ { { a _ { 2 } x + b _ { 2 } y = d _ { 2 } . } } \end{array}
$$

The key is to eliminate $x$ : Multiply the first equation by $\scriptstyle a _ { 2 }$ and the second equation by $a _ { 1 }$ : Subtract the first from the second and the $x$ ’s disappear:

$$
( a _ { 1 } b _ { 2 } - a _ { 2 } b _ { 1 } ) y = ( a _ { 1 } d _ { 2 } - a _ { 2 } d _ { 1 } ) .
$$

To eliminate $y$ ; subtract $b _ { 1 }$ ; times the second equation from $b _ { 2 }$ times the first:

$$
( b _ { 2 } a _ { 1 } - b _ { 1 } a _ { 2 } ) x = ( b _ { 2 } d _ { 1 } - b _ { 1 } d _ { 2 } ) .
$$

What you see in those parentheses are 2 by 2 determinants! Remember from Section 11:3:

$$
T h e d e t e r m i n a n t o f \left[ \begin{array} { c c } { { a _ { 1 } } } & { { b _ { 1 } } } \\ { { a _ { 2 } } } & { { b _ { 2 } } } \end{array} \right] i s t h e n u m b e r \left| \begin{array} { c c } { { a _ { 1 } } } & { { b _ { 1 } } } \\ { { a _ { 2 } } } & { { b _ { 2 } } } \end{array} \right| = a _ { 1 } b _ { 2 } - a _ { 2 } b _ { 1 } .
$$

This number appears on the left side of (6) and (7). The right side of (7) is also a determinant—but it has $d$ ’s in place of $a$ ’s. The right side of (6) has $d$ ’s in place of $b$ ’s. So $x$ and $y$ are ratios of determinants, given by Cra mer’s Rule:

The investment example is solved by three determinants from the three columns:

$$
{ \left| \begin{array} { l l } { 1 } & { 1 } \\ { . 0 5 } & { . 1 0 } \end{array} \right| } = . 0 5 \qquad { \left| \begin{array} { l l } { 5 0 0 0 } & { 1 } \\ { 4 0 0 } & { . 1 0 } \end{array} \right| } = 1 0 0 \qquad { \left| \begin{array} { l l } { 1 } & { 5 0 0 0 } \\ { . 0 5 } & { 4 0 0 } \end{array} \right| } = 1 5 0 .
$$

Cramer’s Rule has $x = 1 0 0 / . 0 5 = 2 0 0 0$ and $y = 1 5 0 / . 0 5 = 3 0 0 0 .$ This is the solution. The singular case is when the determinant of A is zero—and we can’t divide by it.

11I Cramer’s Rule breaks down when det $A = 0$ —which is the singular case. Then the lines in the row picture are parallel, and one column is a multiple of the other column.

EXAMPLE 3 The lines $2 x + y = 0 , 2 x + y = 1$ are parallel. The determinant is zero:

$$
{ \left[ \begin{array} { l l } { 2 } & { 1 } \\ { 2 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l } { x } \\ { y } \end{array} \right] } = { \left[ \begin{array} { l } { 0 } \\ { 1 } \end{array} \right] } \operatorname { h a s } \operatorname* { d e t } A = { \left| \begin{array} { l l } { 2 } & { 1 } \\ { 2 } & { 1 } \end{array} \right| } = 0 .
$$

The lines in Figure 11.17a don’t meet. Notice the columns: $\left[ ^ { 2 } _ { 2 } \right]$ is a multiple of $\left[ ^ { 1 } _ { 1 } \right]$ :

One final comment on 2 by 2 systems. They are small enough so that all solution methods apply. Cramer’s Rule uses determinants. Larger systems use elimination (3 by 3 matrices are on the borderline). A third solution (the same solution!) comes from the inverse matrix $A ^ { - 1 }$ ; to be described next. But the inverse is more a symbol for the answerthan a new way of computing it, because to find $A ^ { - 1 }$ we still use determinants or elimination.

# THE INVERSE OF A MATRIX

The symbol $A ^ { - 1 }$ is pronounced “A inverse.” It stands for a matrix—the one that solves $A \mathbf { u } = \mathbf { d }$ : I think of $A$ as a matrix that takes $\mathbf { u }$ to $\mathbf { d }$ : Then $A ^ { - 1 }$ is a matrix that takes $\mathbf { d }$ back to $\mathbf { u }$ : If $\scriptstyle A \mathbf { u } = \mathbf { d }$ then $\mathbf { u } = A ^ { - 1 } \mathbf { d }$ (provided the inverse exists). This is exactly like functions and inverse functions: $g ( x ) = y$ and $x = g ^ { - 1 } ( y )$ : Our goal is to find $A ^ { - 1 }$ when we know $A$ :

The first approach will be very direct. Cramer’s Rule gave formulas for $x$ and $y$ ; the components of $\mathbf { u }$ : From that rule we can read off $A ^ { - 1 }$ ; assuming that $D = a _ { 1 } b _ { 2 } - a _ { 2 } b _ { 1 }$ is not zero. $D$ is det $A$ and we divide by it:

$$
: \mathbf { u } = { \frac { 1 } { D } } { \left[ \begin{array} { l l } { \ b _ { 2 } d _ { 1 } - b _ { 1 } d _ { 2 } } \\ { - a _ { 2 } d _ { 1 } + a _ { 1 } d _ { 2 } } \end{array} \right] } \quad { \mathrm { T h i s ~ i s ~ } } \mathbf { \mathit { A } } ^ { - 1 } \mathbf { \mathbf { d } } = { \frac { 1 } { D } } { \left[ \begin{array} { l l } { \ b _ { 2 } } & { - b _ { 1 } } \\ { - a _ { 2 } } & { \ a _ { 1 } } \end{array} \right] } { \left[ \begin{array} { l } { d _ { 1 } } \\ { d _ { 2 } } \\ { - a _ { 2 } } \end{array} \right] }
$$

The matrix on the right (including $1 / D$ in all four entries) is $A ^ { - 1 }$ : Notice the sign pattern and the subscript pattern. The inverse exists if $D$ is not zero—this is important. Then the solution comes from a matrix-vector multiplication, $A ^ { - 1 }$ times d: We repeat the rules for that multiplication:

DEFINITION A matrix $M$ times a vector $\mathbf { v }$ equals a vector of dot products:

$$
M \mathbf { v } = { [ \begin{array} { l } { { \mathrm { r o w ~ } } 1 } \\ { { \mathrm { r o w ~ } } 2 } \end{array} ] } { [ \begin{array} { l } { \mathbf { v } } \\ { \mathbf { v } } \\ { \mathbf { [ } { \mathrm { e v } } } \end{array} ] } = { [ \begin{array} { l } { ( { \mathrm { r o w ~ } } 1 ) \cdot \mathbf { v } } \\ { ( { \mathrm { r o w ~ } } 2 ) \cdot \mathbf { v } } \end{array} ] } .
$$

Equation (8) follows this rule with $M = A ^ { - 1 }$ and $\mathbf { v } = \mathbf { d }$ : Look at Example 1:

$$
A = { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { . 0 5 } & { . 1 0 } \end{array} \right] } , \quad \operatorname* { d e t } A = . 0 5 , \quad A ^ { - 1 } = { \frac { 1 } { . 0 5 } } { \left[ \begin{array} { l l } { ~ . 1 0 } & { - 1 } \\ { - . 0 5 } & { ~ 1 } \end{array} \right] } = { \left[ \begin{array} { l l } { ~ 2 } & { - 2 0 } \\ { - 1 } & { ~ 2 0 } \end{array} \right] } .
$$

There stands the inverse matrix. It multiplies $\mathbf { d }$ to give the solution $\mathbf { u }$ :

$$
A ^ { - 1 } \mathbf { d } = { \left[ \begin{array} { l l } { 2 } & { - 2 0 } \\ { - 1 } & { \quad 2 0 } \end{array} \right] } { \left[ \begin{array} { l } { 5 0 0 0 } \\ { 4 0 0 } \end{array} \right] } = { \left[ \begin{array} { l } { ( 2 ) ( 5 0 0 0 ) - ( 2 0 ) ( 4 0 0 ) } \\ { ( - 1 ) ( 5 0 0 0 ) + ( 2 0 ) ( 4 0 0 ) } \end{array} \right] } = { \left[ \begin{array} { l } { 2 0 0 0 } \\ { 3 0 0 0 } \end{array} \right] } .
$$

The formulas work perfectly, but you have to see a direct way to reach $A ^ { - 1 } \mathbf { d }$ : Multiply both sides of $\scriptstyle A \mathbf { u } = \mathbf { d }$ by $A ^ { - 1 }$ . The multiplication “cancels” $A$ on the left side, and leaves $ { \mathbf { u } } = A ^ { - 1 }  { \mathbf { d } }$ : This approach comes next.

# MATRIX MULTIPLICATION

To understand the power of matrices, we must multiply them. The product of $A ^ { - 1 }$ with $\boldsymbol { A } \mathbf { u }$ is a matrix times a vector. But that multiplication can be done another way. First $A ^ { - 1 }$ multiplies $A$ ; a matrix times a matrix. The product $A ^ { - 1 } A$ is another matrix (a very special matrix). Then this new matrix multiplies $\mathbf { u }$ :

The matrix-matrix rule comes directly from the matrix-vector rule. Effectively, a vector $\mathbf { v }$ is a matrix $V$ with only one column. When there are more columns, $M$ times $V$ splits into separate matrix-vector multiplications, side by side:

DEFINITION A matrix $M$ times a matrix $V$ equals a matrix of dot products:

$$
M V = { \left[ \operatorname { r o w } { 1 } \right] } { \left[ \begin{array} { l l } { \mathbf { v } _ { 1 } } & { \mathbf { v } _ { 2 } } \\ { \mathbf { r } { 0 } { \mathrm { w } } 2 } \end{array} \right] } = { \left[ \begin{array} { l l } { ( { \mathrm { r o w ~ } } 1 ) \cdot \mathbf { v } _ { 1 } } & { ( { \mathrm { r o w ~ } } 1 ) \cdot \mathbf { v } _ { 2 } } \\ { ( { \mathrm { r o w ~ } } 2 ) \cdot \mathbf { v } _ { 1 } } & { ( { \mathrm { r o w ~ } } 2 ) \cdot \mathbf { v } _ { 2 } } \end{array} \right] } .
$$

$$
{ \left[ \begin{array} { l l } { 1 } & { 2 } \\ { 3 } & { 4 } \end{array} \right] } { \left[ \begin{array} { l l } { 5 } & { 6 } \\ { 7 } & { 8 } \end{array} \right] } = { \left[ \begin{array} { l l } { 1 \cdot 5 + 2 \cdot 7 } & { 1 \cdot 6 + 2 \cdot 8 } \\ { 3 \cdot 5 + 4 \cdot 7 } & { 3 \cdot 6 + 4 \cdot 8 } \end{array} \right] } = { \left[ \begin{array} { l l } { 1 9 } & { 2 2 } \\ { 4 3 } & { 5 0 } \end{array} \right] } .
$$

EXAMPLE 5 Multiplying $A ^ { - 1 }$ times $A$ produces the “identity matrix” ${ \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] } ;$

$$
A ^ { - 1 } A = \frac { \left[ \begin{array} { c c } { b _ { 2 } \ - b _ { 1 } } \\ { - a _ { 2 } \ a _ { 1 } } \end{array} \right] } { D } \left[ \begin{array} { c } { a _ { 1 } \ b _ { 1 } } \\ { a _ { 2 } \ b _ { 2 } } \end{array} \right] = \frac { \left[ \begin{array} { c c } { a _ { 1 } b _ { 2 } \ - a _ { 2 } b _ { 1 } } & { 0 } \\ { 0 } & { - a _ { 2 } b _ { 1 } + a _ { 1 } b _ { 2 } } \end{array} \right] } { D } = \left[ \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] .
$$

This identity matrix is denoted by $I$ : It has 1’s on the diagonal and 0’s off the diagonal. It acts like the number 1: Every vector satisfies $I \mathbf { u } = \mathbf { u }$ :

$$
\left. \begin{array} { c c } { { a } } & { { b } } \\ { { c } } & { { d } } \end{array} \right] \qquad A ^ { - 1 } = \frac { 1 } { D } \left[ \begin{array} { c c } { { d } } & { { - b } } \\ { { - c } } & { { a } } \end{array} \right] \qquad \left[ \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { 0 } } & { { 1 } } \end{array} \right] \left[ \begin{array} { c } { { x } } \\ { { y } } \end{array} \right] = \left[ \begin{array} { c } { { x } } \\ { { y } } \end{array} \right] .
$$

The next section moves to three equations. The algebra gets more complicated (and 4 by 4 is worse). It is not easy to write out $A ^ { - 1 }$ : So we stay longer with the 2 by 2 formulas, where each step can be checked. Multiplying $A \mathbf { u } = \mathbf { d }$ by the inverse matrix gives $A ^ { - 1 } A \mathbf { u } = A ^ { - 1 } \mathbf { d }$ —and the left side is $I \mathbf { u } = \mathbf { u }$ :

EXAMPLE 6 $A = { \left[ \begin{array} { l l } { \cos \theta } & { - \sin \theta } \\ { \sin \theta } & { \quad \cos \theta } \end{array} \right] }$ rotates every $\mathbf { v }$ to $\ A \mathbf { v }$ ; through the angle $\theta$ :   
Question 1 Where is the vector $\mathbf { v } = { \left[ \begin{array} { l } { 1 } \\ { 0 } \end{array} \right] } { \mathrm { ~ r o t a t e d ~ t o ~ } } ?$   
Question 2 What is $A ^ { - 1 } { } ^ { \cdot }$   
Question 3 Which vector $\mathbf { u }$ is rotated into $\mathbf { d } = { \left[ \begin{array} { l } { 0 } \\ { 1 } \end{array} \right] } \ 2$   
Solution 1 v rotates into $A \mathbf { v } = { \left[ \begin{array} { l l } { \cos \theta } & { - \sin \theta } \\ { \sin \theta } & { \quad \cos \theta } \end{array} \right] } { \left[ \begin{array} { l } { 1 } \\ { 0 } \end{array} \right] } = { \left[ \begin{array} { l } { \cos \theta } \\ { \sin \theta } \end{array} \right] } .$

Solution 2 det $A = 1$ so $A ^ { - 1 } = { \left[ \begin{array} { l l } { \cos \theta } & { \sin \theta } \\ { - \sin \theta } & { \cos \theta } \end{array} \right] } = { \mathrm { r o t a t i o n ~ t h r o u g h } } - \theta .$

Solution 3 If $A \mathbf { u } = \mathbf { d }$ the $\mathbf { \Omega } _ { 1 } \mathbf { u } = A ^ { - 1 } \mathbf { d } = { \left[ \begin{array} { l l } { \cos \theta } & { \sin \theta } \\ { - \sin \theta } & { \cos \theta } \end{array} \right] } { \left[ \begin{array} { l } { 0 } \\ { 1 } \end{array} \right] } = { \left[ \begin{array} { l } { \sin \theta } \\ { \cos \theta } \end{array} \right] } .$

Historical note I was amazed to learn that it was Leibniz (again!) who proposed the notation we use for matrices. The entry in row $i$ and column $j$ is $a _ { i j }$ : The identity matrix has $a _ { 1 1 } = a _ { 2 2 } = 1$ and $a _ { 1 2 } = a _ { 2 1 } = 0$ : This is in a linear algebra book by Charles Dodgson—better known to the world as Lewis Carroll, the author of Alice in Wonderland. I regret to say that he preferred his own notation $i \ i$ instead of $a _ { i j }$ : “I have turned the symbol toward the left, to avoid all chance of confusion with $\scriptstyle \int$ :” It drove his typesetter mad.

# PROJECTION ONTO A PLANE $\ c =$ LEAST SQUARES FITTING BY A LINE

We close with a genuine application. It starts with three-dimensional vectors ${ \mathbf a } , { \mathbf b } , { \mathbf d }$ and leads to a 2 by 2 system. One good feature: ${ \mathbf a } , { \mathbf b } , { \mathbf d }$ can be $n$ -dimensional with no change in the algebra. In practice that happens. Second good feature: There is a calculus problem in the background. The example is to fit points by a straight line.

There are three ways to state the problem, and they look different:

1. Solve $x { \mathbf a } + y { \mathbf b } = { \mathbf d }$ as well as possible (three equations, two unknowns $x$ and $y$ ).   
2. Project the vector d onto the plane of the vectors a and b:   
3. Find the closest straight line (“least squares”) to three given points.

Figure 11.19 shows a three-dimensional vector $\mathbf { d }$ above the plane of a and b: Its projection onto the plane is $\mathbf { p } = x \mathbf { a } + y \mathbf { b }$ : The numbers $x$ and $y$ are unknown, and our goal is to find them. The calculation will use the dot product, which is always the key to right angles.

The difference $\mathbf { d } - \mathbf { p }$ is the “error.” There has to be an error, because no combination of a and $\mathbf { b }$ can produce d exactly. (Otherwise $\mathbf { d }$ is in the plane.) The projection $\mathbf { p }$ is the closest point to $\mathbf { d }$ ; and it is governed by one fundamental law: The error is perpendicular to the plane. That makes the error perpendicular to both vectors a and $\mathbf { b }$ :

$$
\mathbf { a } \cdot ( x \mathbf { a } + y \mathbf { b } - \mathbf { d } ) = 0 \qquad { \mathrm { a n d } } \qquad \mathbf { b } \cdot ( x \mathbf { a } + y \mathbf { b } - \mathbf { d } ) = 0 .
$$

Rewrite those as two equations for the two unknown numbers $x$ and $y$ :

$$
{ \begin{array} { r l } & { ( \mathbf { a } \cdot \mathbf { a } ) x + ( \mathbf { a } \cdot \mathbf { b } ) y = \mathbf { a } \cdot \mathbf { d } } \\ & { ( \mathbf { b } \cdot \mathbf { a } ) x + ( \mathbf { b } \cdot \mathbf { b } ) y = \mathbf { b } \cdot \mathbf { d } . } \end{array} }
$$

These are the famous normal equations in statistics, to compute $x$ and $y$ and $\mathbf { p }$ :

EXAMPLE 7 For ${ \bf \ddot { a } } = ( 1 , 1 , 1 )$ and ${ \bf b } = ( 1 , 2 , 3 )$ and $\mathbf { d } = ( 0 , 5 , 4 )$ ; solve equation (14):

$$
\begin{array} { r l } & { 3 x + \ 6 y = \ 9 } \\ & { 6 x + 1 4 y = 2 2 \quad \mathrm { g i v e s } } \\ & { 6 x + 1 4 y = 2 2 \quad \mathrm { g i v e s } } \end{array} \begin{array} { l } { x = - 1 } \\ { 3 } \\ { y = \quad 2 } \end{array} \begin{array} { l } { \mathrm { s o } \quad \mathbf { p } = - \mathbf { a } + 2 \mathbf { b } = ( 1 , 3 , 5 ) = p r o j e c t i o n . } \end{array}
$$

Notice the three equations that we are not solving (we can’t): $x \mathbf { a } + y \mathbf { b } = \mathbf { d }$ is

$$
\begin{array} { r l } & { x + \ y = 0 } \\ & { x + 2 y = 5 \ \mathrm { w i t h ~ t h e } \ 3 \mathrm { b y ~ 2 ~ m a t r i x } \ A = \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 1 } & { 2 } \\ { 1 } & { 3 } \end{array} \right] . } \end{array}
$$

For $\mathbf { d } = ( 0 , 5 , 4 )$ there is no solution; $\mathbf { d }$ is not in the plane of a and b: For $\mathbf { p } = ( 1 , 3 , 5 )$ there is a solution, $x = - 1$ and $y = 2$ : The vector $\mathbf { p }$ is in the plane. The error $\mathbf { d } - \mathbf { p }$ is $( - 1 , 2 , - 1 )$ : This error is perpendicular to the columns $( 1 , 1 , 1 )$ and .1; 2; 3/; so it is perpendicular to their plane.

SAME EXAMPLE (written as a line-fitting problem) Fit the points $( 1 , 0 )$ and $( 2 , 5 )$ and $( 3 , 4 )$ as closely as possible (“least squares”) by a straight line.

Two points determine a line. The example asks the line $f = x + y t$ to go through three points. That gives the three equations in (15), which can’t be solved with two unknowns. We have to settle for the closest line, drawn in Figure 11.19b. This line is computed again below, by calculus.

Notice that the closest line has heights 1; 3; 5 where the data points have heights $_ { 0 , 5 , 4 }$ : Those are the numbers in $\mathbf { p }$ and $\mathbf { d }$ ! The heights 1; 3; 5 fit onto a line; the heights $_ { 0 , 5 , 4 }$ do not. In the first figure, $\mathbf { p } = ( 1 , 3 , 5 )$ is in the plane and $\mathbf { d } = ( 0 , 5 , 4 )$ is not. Vectors in the plane lead to heights that lie on a line.

Notice another coincidence. The coefficients $x = - 1$ and $y = 2$ give the projection $- \mathbf { a } + 2 \mathbf { b }$ : They also give the closest line $f = - 1 + 2 t$ : All numbers appear in both figures.

Remark Finding the closest line is a calculus problem: Minimize a sum of squares. The numbers $x$ and $y$ that minimize $E$ give the least squares solution:

$$
E ( x , y ) = ( x + y - 0 ) ^ { 2 } + ( x + 2 y - 5 ) ^ { 2 } + ( x + 3 y - 4 ) ^ { 2 } .
$$

Those are the three errors in equation (15), squared and added. They are also the three errors in the straight line fit, between the line and the data points. The projection minimizes the error (by geometry), the normal equations (14) minimize the error (by algebra), and now calculus minimizes the error by setting the derivatives of $E$ to zero.

The new feature is this: $E$ depends on two variables $x$ and $y$ : Therefore $E$ has two derivatives. They both have to be zero at the minimum. That gives two equations for $x$ and $y$ :

$x$ derivative of $E$ is zero: $\begin{array} { r l } { 2 ( x + y ) + 2 ( x + 2 y - 5 ) } & { { } + 2 ( x + 3 y - 4 ) } \end{array} \quad = 0$ $\begin{array} { r l } & { 2 ( x + y ) + 2 ( x + 2 y - 5 ) \quad + 2 ( x + 3 y - 4 ) \quad = 0 } \\ & { 2 ( x + y ) + 2 ( x + 2 y - 5 ) ( 2 ) + 2 ( x + 3 y - 4 ) ( 3 ) = 0 . } \end{array}$ $y$ derivative of $E$ is zero:

When we divide by 2; those are the normal equations $3 x + 6 y = 9$ and $6 x + 1 4 y =$ 22: The minimizing $x$ and $y$ from calculus are the same numbers $^ { - 1 }$ and 2:

The $x$ derivative treats $y$ as a constant. The $y$ derivative treats $x$ as a constant. These are partial derivatives. This calculus approach to least squares is in Chapter 13, as an important application of partial derivatives.

We now summarize the least squares problem—to find the closest line to $n$ data points. In practice $n$ may be 1000 instead of 3: The points have horizontal coordinates $b _ { 1 } , b _ { 2 } , \ldots , b _ { n }$ : The vertical coordinates are $d _ { 1 } , d _ { 2 } , \ldots , d _ { n }$ : These vectors $\mathbf { b }$ and $\mathbf { d }$ ; together with $\mathbf { a } = ( 1 , 1 , . . . , 1 )$ ; determine a projection—the combination $\mathbf { p } = x \mathbf { a } +$ $y \mathbf { b }$ that is closest to $\mathbf { d }$ : This problem is the same in $n$ dimensions—the error $\mathbf { d } - \mathbf { p }$ is perpendicular to aand $\mathbf { b }$ : That is still tested by dot products, $\mathbf { p } \cdot \mathbf { a } = \mathbf { d } \cdot \mathbf { a }$ and $\mathbf { p } \cdot \mathbf { b } =$ $\mathbf { d } \cdot \mathbf { b }$ ; which give the normal equations for $x$ and $y$ :

$$
\begin{array} { c } { { ( { \bf a } \cdot { \bf a } ) x + ( { \bf a } \cdot { \bf b } ) y = { \bf a } \cdot { \bf d } \qquad \qquad \quad ( n ) ~ x + ( \Sigma b _ { i } ) y = \Sigma d _ { i } } } \\ { { ( { \bf b } \cdot { \bf a } ) x + ( { \bf b } \cdot { \bf b } ) y = { \bf b } \cdot { \bf d } \qquad \quad \mathrm { o r } \qquad \quad ( \Sigma b _ { i } ) x + ( \Sigma b _ { i } ^ { 2 } ) y = \Sigma b _ { i } d _ { i } . } } \end{array}
$$

11K The least squares problem projects $\mathbf { d }$ onto the plane of a and $\mathbf { b }$ : The projection is $\mathbf { p } = x \mathbf { a } + y \mathbf { b }$ ; in $n$ dimensions. The closest line $f = x + y t$ ; in two dimensions. The normal equations (17) give the best $x$ and $y$ :