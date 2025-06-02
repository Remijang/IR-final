# 2.6 Limits

You have seen enough limits to be ready for a definition. It is true that we have survived this far without one, and we could continue. But this seems a reasonable time to define limits more carefully. The goal is to achieve rigor withouÑt rigor mortis.

First you sho uld know that limits of $\Delta y / \Delta x$ are by noÑmeans the only limits in mathematics. Here are five completely different examples. TheyÑinvolve $n \to \infty$ , not $\Delta x  0$ :

1. $a _ { n } = ( n - 3 ) / ( n + 3 )$ (for large $n$ , ignore the 3’s and find $a _ { n } \to 1$ )   
2. $\textstyle a _ { n } = { \frac { 1 } { 2 } } a _ { n - 1 } + 4$ (start with any $a _ { 1 }$ andÑalways $a \to 8$ )   
3. $a _ { n } =$ probability of living to year $n$ (unforÑtunately ${ a _ { n } } \to 0$ )   
4. $a _ { n } =$ fraction of zeros among the first $n$ digits of $\pi$ $\begin{array} { r } { ( a _ { n }  \frac { 1 } { 1 0 } ? ) } \end{array}$ /   
5. $a _ { 1 } = . 4$ ; $a _ { 2 } = . 4 9$ ; $a _ { 3 } = . 4 9 3$ ; : : : No matter what the remaining deÑcimals are,   
the a’s converge to a limit. Possibly $a _ { n }  . 4 9 3 0 0 0 \ldots _ { }$ , but not likely.

The problem is to say what the limit symbol $$ really means.

A good starting point is to ask about convergence to zero. When does a sequence of positive numbers approach zero ? What does it mean to write $a _ { n } \to 0 \ ?$ The numbers $a _ { 1 } , a _ { 2 } , a _ { 3 } , \dots$ ; must become “small,” but that is too vague. We will propose four definitions of convergence to zero, and I hope the right one will be clear .

1. All the numbers $\textstyle { a _ { n } }$ are below $1 0 ^ { - 1 0 }$ . That may be enough for practical purposes, but it certainly doesn’t make the $a _ { n }$ approach zero. 2. The sequence is getting closer to zero—each $a _ { n + 1 }$ is smaller than the preceding $a _ { n }$ : This test is met by 1:1, 1:01, 1:001, . . . which converges to 1 instead of 0: 3. For any small number you think of, at least one of the $a _ { n }$ ’s is smaller. That pushes something toward zero, but not necessarily the whole sequence. The condition would be satisfied by $1 , { \frac { 1 } { 2 } } , 1 , { \frac { 1 } { 3 } } , 1 , { \frac { 1 } { 4 } } , \ldots .$ , which does not approach zero. 4. For any small number you think of, the $a _ { n }$ ’s eventually go below that number and stay below. This is the correct definition.

I want to repeat that. To test for convergence to zero, start with a small number— say $1 0 ^ { - 1 0 }$ : The $a _ { n }$ ’s must go below that number. They may come back up and go below again—the first million terms make absolutely no difference. Neither do the next billion, but eventually all terms must go below $1 0 ^ { - 1 0 }$ : After waiting longer (possibly a lot longer), all terms drop below $1 0 ^ { - 2 0 }$ : The tail end of the sequence decides everything.

Question 1 Does the sequence $1 0 ^ { - 3 } , 1 0 ^ { - 2 } , 1 0 ^ { - 6 } , 1 0 ^ { - 5 } , 1 0 ^ { - 9 } , 1 0 ^ { - 8 } , \ldots$ approach 0 ?

Answer Yes, These up and down numbers eventually stay below any $\varepsilon$ :

# 2 Derivatives

Question 2 Does $1 0 ^ { - 4 }$ ; $1 0 ^ { - 6 }$ ; $1 0 ^ { - 4 }$ ; $1 0 ^ { - 8 }$ ; $1 0 ^ { - 4 }$ ; $1 0 ^ { - 1 0 }$ ; : : : approach zero ? Answer No. This sequence goes below $1 0 ^ { - 4 }$ but does not stay below.

There is a recognized symbol for “an arbitrarily small positive number.” By worldwide agreement, it is the Greek letter $\varepsilon$ (epsilon). Convergence to zero means that the sequence eventually goes below $\varepsilon$ and stays there. The smaller the $\varepsilon$ , the tougher the test and the longer we wait. Think of $\varepsilon$ as the tolerance, and keep reducing it.

To emphasize that $\varepsilon$ comes from outside, Socrates can choose it. Whatever $\varepsilon$ he proposes, the $a$ ’s must eventually be smaller. After some $a _ { N }$ , all the a’s are below the tolerance ". Here is the exact statement:

for any " there is an $N$ such that $a _ { n } < \varepsilon$ if $n > N$ :

Once you see that idea, the rest is easy. Figure 2.17 has $N = 3$ and then $N = 6$ :

EXAMPLE 1 The sequence 21 ; 4 ; 98 ; : : : starts upward but goes to zero. Notice that $1 , 4 , 9 , \ldots , 1 0 0 , \ldots$ : are squares, and $\bar { 2 } , 4 , 8 , \ldots , 1 0 2 4 , .$ : : are powers of 2: Eventually $2 ^ { n }$ grows faster than $n ^ { 2 }$ , as in $a _ { 1 0 } = 1 0 0 / 1 0 2 4$ : The ratio goes below any $\varepsilon$ :

EXAMPLE 2 $1 , 0 , { \scriptstyle { \frac { 1 } { 2 } } } , 0 , { \scriptstyle { \frac { 1 } { 3 } } } , 0 , \ldots$ approaches zero. These $a$ ’s do not decrease steadily (the mathematical word for steadily is “monotonically”) but still their limit is zero. The choice $\varepsilon = 1 / 1 0$ produces the right response: Beyond $a _ { 2 0 0 1 }$ all terms are below $1 / 1 0 0 0$ : So $N = 2 0 0 1$ for that $\varepsilon$ :

T|heÑsequence $1 , { \frac { 1 } { 2 } } , { \frac { 1 } { 2 } } , { \frac { 1 } { 3 } } , { \frac { 1 } { 3 } } , { \frac { 1 } { 3 } } , \ldots$ is much sl|owe|r—but it also converges to zero.

Next we allow the numbers $\scriptstyle a _ { n }$ to be negative as well as positive. They can converge upward toward zero, or they can come in from bot|h si|de s. The te¡st still requires the $a _ { n }$ to go inside any strip near zero (and stay there). But now the strip starts at $- \varepsilon$ :

The distance from zero is the absolute value $\left| a _ { n } \right|$ . Therefore ${ a _ { n } } \to 0$ means $\left| a _ { n } \right| \to 0$ : The previous test can be applied to $\left| a _ { n } \right|$ :

for any " there is an $N$ such that $\left. a _ { n } \right. < \varepsilon$ if $n > N$ .

EXAMPLE 3 $\begin{array} { r } { 1 , - \frac { 1 } { 2 } , \frac { 1 } { 3 } , - \frac { 1 } { 4 } } \end{array}$ ; : : : converges to z|ero beca|us e $\begin{array} { r } { 1 , \frac { 1 } { 2 } , \frac { 1 } { 3 } , \frac { 1 } { 4 } , \dots } \end{array}$ converges to zero.

It is a short step to limits other than zero. The limit is $L$ if the numbers $\textstyle { a _ { n } - L }$ converge to zero. Our final test applies to the absolute value $\vert a _ { n } - L \vert$ :

for any " there is an $N$ such that $\vert a _ { n } - L \vert < \varepsilon$ if $n > N$ .

This is the definition of convergence! Only a finite number of $a$ ’s are outside any strip around $L$ (Figure 2.18). We write $a _ { n } \to L$ or $\operatorname* { l i m } a _ { n } = L$ or $\scriptstyle \operatorname* { l i m } _ { n \to \infty } a _ { n } = L$ :

# 2.6 Limits

EXAMPLE 4 The numbers 23 ; 54 ; 76 ; : : : converge to L D 1: After subtracting 1 the differences 1 ; 1 ; 1 ; 2 4 6 : : : converge to zero. Those difference are an L :

EXAMPLE 5 The sequence 1; $1 + { \frac { 1 } { 2 } }$ ; $\textstyle 1 + { \frac { 1 } { 2 } } + { \frac { 1 } { 3 } }$ ; $\textstyle 1 + { \frac { 1 } { 2 } } + { \frac { 1 } { 3 } } + { \frac { 1 } { 4 } }$ ; : : : fails to converge.

The distance between terms is getting smaller. But those numbers $a _ { 1 } , a _ { 2 } , a _ { 3 } , a _ { 4 } , . . .$ go past any proposed limit $L$ : The second term is $1 \textstyle { \frac { 1 } { 2 } }$ : The fourth term adds on $\textstyle { { \frac { 1 } { 3 } } + { \frac { 1 } { 4 } } }$ , so $a _ { 4 }$ goes past 2: The eighth term has four new fractions $\textstyle { { \frac { 1 } { 5 } } + { \frac { 1 } { 6 } } + { \frac { 1 } { 7 } } + { \frac { 1 } { 8 } } }$ , totaling more than $\textstyle { { \frac { 1 } { 8 } } + { \frac { 1 } { 8 } } + { \frac { 1 } { 8 } } + { \frac { 1 } { 8 } } = { \frac { 1 } { 2 } } }$ : Therefore $a _ { 8 }$ exceeds $2 { \frac { 1 } { 2 } }$ : Eight more terms will add more than 8 times $\scriptstyle { \frac { 1 } { 1 6 } }$ , so $a _ { 1 6 }$ is beyond 3: The lines in Figure 2.1Ñ8c8are infinitely long, not stopping at any $L$ :

In the language of Chapter 10,Ñthe harmonic series $1 + { \textstyle \frac { 1 } { 2 } } + { \textstyle \frac { 1 } { 3 } } + \ldots$ does not converge. The sum is infinite, because the “partial sums” $a _ { n }$ go beyond everÑy limit $L$ $( a _ { 5 0 0 0 }$ is past $L = 9$ ). We will come back to infinite series, but this example makes a subtle point: The steps between the $a _ { n }$ can go to zero while still $a _ { n } \to \infty$ :

Thus the condition $a _ { n + 1 } - a _ { n } \to 0$ is not sufficient for convergence. However this condition is necessary. If we do have convergence, then $a _ { n + 1 } - a _ { n } \to 0$ : That is a good exercise in the logic of convergence, emphasizing the differe|ncebet |we en “sufficien|t” and “nec|es sary.” We discussthis logic below, after proving that [statement $\boldsymbol { A } \boldsymbol { ] }$ implies [statement $B$ ]:

$$
I f \left[ a _ { n } \mathrm { c o n v e r g e s } \mathrm { t o } L \right] t h e n \left[ a _ { n + 1 } - a _ { n } \mathrm { c o n v e r g e s } \mathrm { t o } \mathrm { z e r o } \right] .
$$

Proof Because the $a _ { n }$ converge, there is a number $N$ beyond which $\left. a _ { n } - L \right. < \varepsilon$ and also $\left| a _ { n + 1 } - L \right| < \varepsilon$ : Since $a _ { n + 1 } - a _ { n }$ is the sum of $a _ { n + 1 } - L$ and $L - a _ { n }$ , its absolute value cannot exceed $\varepsilon + \varepsilon = 2 \varepsilon$ : Therefore $a _ { n + 1 } - a _ { n }$ approaches zero.

Objection by Socrates: We only got below $2 \varepsilon$ and he asked for $\varepsilon$ : Our reply: If he particularly wants $\left| a _ { n + 1 } - a _ { n } \right| < 1 / 1 0$ , we start with $\varepsilon = 1 / 2 0$ : Then $2 \varepsilon = 1 / 1 0$ : But this juggling is not necessary. To stay below $2 \varepsilon$ is just as convincing as to stay below $\varepsilon$ :

# THE LOGIC OF “IF” AND “ONLY IF”

The following page is inserted to help with the language of mathÑematics. In ordinary language we might say $^ { \ast } \mathrm { I }$ will come if you call.” Or we might say $^ { \ast } \mathrm { I }$ will come only if you call.” That is different! A mathematician might even say $^ { \mathrm { { * } } } \mathrm { { I } }$ will come $i f$ and only $i f$ you call.” Our goal is to think through the logic, because it is important and not so fami1iar.

Statement $A$ above implies statement $B$ : Statement $A$ is $a _ { n } \to L$ ; statement $B$ is $a _ { n + 1 } - a _ { n } \to 0$ : Mathematics has at leasñt five ways of writing down $A \Rightarrow B$ , and I though you might like to see them together. It seems excessive to have so many expressions for the same idea, but authors get desperate for a little variety. Here are the five ways that come to mind:

$$
A \Rightarrow B
$$

EXAMPLES ${ \pmb I } { \pmb f }$ [positive numbers are decreasing] then [they converge to a limit]. $\pmb { I f }$ [sequences $a _ { n }$ and $b _ { n }$ converge] then [the sequence $a _ { n } + b _ { n }$ converges]. If $[ f ( x )$ is the integral of $v ( x ) ]$ then $[ v ( x )$ is the derivative of $f ( x ) ]$ .

Those are all true, but not proved. $A$ is the hypothesis, $B$ is the conclusion.

Now we go in the other direction. (It is called the “converse,” not the inverse.) We exchange $A$ and $B$ . Of course stating the converse does not make it true! $B$ might imply $A$ , or it might not. In the first two examples the converse was false—the $a _ { n }$ can converge without decreasing, and $a _ { n } + b _ { n }$ can converge when the separate sequences do not. The converse of the third statement is true—and there are five more ways to state it:

$$
A \Leftarrow B
$$

$A$ is implied by $B$

# if B then A

$A$ is a necessary condition for $B$

$B$ is true only if $A$ is true

Those words “necessary” and “sufficient” are not always easy to master. The same is true of the deceptively short phrase “if and only if.” The two statements $A \Rightarrow B$ and $A \Leftarrow B$ are completely different and they both require proof. That means two separate proofs. But they can be stated together for convenience (when both are true):

$$
A \Leftrightarrow B
$$

$A$ implies $B$ and $B$ implies $A$

$A$ isÑequivaôlent to $B$

$A$ is a necessary and sufficient condition for $B$

$A$ is true if and only if $B$ is true

$$
[ a _ { n }  L ] \Leftrightarrow [ 2 a _ { n }  2 L ] \Leftrightarrow [ a _ { n } + 1  L + 1 ] \Leftrightarrow [ a _ { n } - L  0 ] .
$$

# RULES FOR LIMITS

Calculus needs a definition of limits, to define $d y / d x$ : That derivative contains two limits: $\Delta x  0$ and $\Delta y / \Delta x \to d y / d x$ : Calculus also needs rules for limits, to prove the sum rule and product rule for derivatives. We started on the definition, and now we start on the rules.

Given two convergent sequences, $a _ { n } \to L$ and $b _ { n } \to M$ , other sequences also converge:

Addition: $a _ { n } + b _ { n } \to L + M$ Subtraction: an bn L M Multipli1cation: $a _ { n } b _ { n } \to L M$ Divis1ion: $a _ { n } / b _ { n } \to L / M$ .provided $M \neq 0$ /

We check the multiplication rule, which uses a convenieÑnt identity:

$$
a _ { n } b _ { n } - L M = ( a _ { n } - L ) ( b _ { n } - M ) + M ( a _ { n } - L ) + L ( b _ { n } - M ) .
$$

Suppose $\left. a _ { n } - L \right. < \varepsilon$ beyond some point $N$ , and $\left. b _ { n } - M \right. < \varepsilon$ beyond some other point $N ^ { \prime }$ : Then beyond the larger of $N$ and $N ^ { \prime }$ , the right side of .2/ is small. It is less than $\varepsilon \cdot \varepsilon + M \varepsilon + L \varepsilon$ : This proves that .2/ gives $a _ { n } b _ { n } \to L M$ :

An important special case is $c a _ { n }  c L$ : (The sequence of $b$ ’s is $\boldsymbol { c } , \boldsymbol { c } , \boldsymbol { c } , \boldsymbol { c } , \boldsymbol { \ldots } )$ Thus a constant can be brought “outside” the limit, to give lim $c a _ { n } = c$ lim $\scriptstyle a _ { n }$ :

# THE LIMIT OF $f ( x )$ AS $x \to a$

The final step is to replace sequences by functions. Instead of $a _ { 1 } , a _ { 2 } , \dots$ there is a continuum of values $f ( x )$ : The limit is taken as $x$ approaches a specified point $a$ (instead of $n \to \infty$ ). Example: As $x$ approaches $a = 0$ , the function $f ( x ) = 4 - x ^ { 2 }$ approaches $L = 4$ : As $x$ approaches $a = 2$ , the function $5 x$ approaches $L = 1 0$ : Those statements are fairly obvious, but we have to say what they mean. Somehow it must be this:

If $x - a$ is small, then $f ( x ) - L$ should be small. As before, the word small does not say everything. We really mean “arbitrarily smal|l,”or “|b elow any $\varepsilon$ :” T|he differe|nc e $f ( x ) - L$ must become as small as anyone wants, when $x$ gets near $a$ : In that case $\begin{array} { r } { \operatorname* { l i m } _ { x \to a } f ( x ) = L } \end{array}$ : Or we write $f ( x )  L$ as $x \to a$ :

The statement is awkward because it involves two limits. The limit $x \to a$ is forcing $f ( x )  L$ : (Previously $n \to \infty$ forced $a  L$ :) But it is wrong to expect the same $\varepsilon$ in both limits. We do not and cannot require that $| x - a | < \varepsilon$ produces) $| f ( x ) - L | <$ $\varepsilon . H t$ may be necessary to push $x$ extremely close to $a$ (closer than $\varepsilon$ ). We must guarantee that if $x$ is close enough to $a$ , then $| f ( x ) - L | < \varepsilon$ :

We have come to the “e ps|ilon-d|el ta definition|” of limits|. First, Socrates chooses $\varepsilon$ : He has to be shown that $f ( x )$ is within $\varepsilon$ of $L$ , for every $x$ near $a$ : Then somebody else (maybe Plato) replies with a number $\boldsymbol { \delta }$ : That gives the meaning of “near $a$ :” Plato’s goal is to get $f ( x )$ within $\varepsilon$ of $L$ , by keeping $x$ within $\delta$ of $a$ :

$$
i f 0 < | x - a | < \delta t h e n | f ( x ) - L | < \varepsilon .
$$

The input tolerance is $\delta$ (delta), the output tolerance is $\varepsilon$ : When Plato can find a $\delta$ for every $\varepsilon$ , Socrates concedes that the limit is $L$ :

EXAMPLE Prove that $\operatorname* { l i m } _ { x \to 2 } { 5 x } = 1 0$ : In this case $a = 2$ and $L = 1 0$ :

Socrates asks for $\left| 5 x - 1 0 \right| < \varepsilon$ : Plato responds by requiring $| x - 2 | < \delta$ : What $\delta$ should he choose ${ \ ? } \ \mathrm { I n }$ this case $\left. 5 x - 1 0 \right.$ is exactly 5 times $\left| x - 2 \right|$ : So Plato picks $\boldsymbol { \delta }$ below $\varepsilon / 5$ (a smaller $\boldsymbol { \delta }$ is always OK). Whenever $| x - 2 | < \varepsilon / 5$ , mult|iplication b|y 5 shows that $| 5 x - 1 0 | < \varepsilon$ :

Remark 1 In Figure 2.19, Socrates chooses the height of the box. It extends above and below $L$ , by the small number $\varepsilon$ : Second, Plato chooses the width. He must make the box narrow enough for the graph to go out the sides. Then $| f ( x ) - L | < \varepsilon$ :

When $f ( x )$ has a jump, the box can’t hold it. A step function has no limit as $x$ approaches the jump, because the graph goes through the top or bottom—no matter how thin the box.

Remark 2 The second figure has $f ( x )  L$ , because in taking limits we ignore the final point $x = a$ . The value $f ( a )$ can be anything, with no effect on $L$ : The first figure has more: $f ( a )$ equals $L$ : Then a special name applies— $f$ is continuous. The left figure shows a continuous function, the other figures do not.

We soon co |me bac k| to continuous functions.

Remark 3 In the example with $f = 5 x$ and $\delta = \varepsilon / 5$ , the number 5 was the slope. That choice barely ke1pt the graph in the box—it goes out the corners. A little narrower, say $\delta = \varepsilon / 1 0$ |, and the graph goes safely out the sides. A reasonable choice is to divide " by $2 | f ^ { \prime } ( a ) |$ . (We double the slope for safety.) I want to say why this $\delta$ works—even if the $\varepsilon - \delta$ test is seldom used in practice.

The ratio of $f ( x ) - L$ to $x - a$ is distance up over distance across. This is $\Delta f / \Delta x$ , close to the slope $f ^ { \prime } ( a )$ : When the distance across is $\delta$ , the distance up or down is near $\delta | f ^ { \prime } ( a ) |$ : That equals $\varepsilon / 2$ for our “reasonable choice” of $\delta \cdot$ —so we are safely below $\varepsilon$ : This choice solves most exerciÑses. But Example 7 shows that a limit might exist even when the slope is infinitÑe.

EXAMPLE 7 $\operatorname* { l i m } _ { x \to 1 ^ { + } } { \sqrt { x - 1 } } = 0 \quad ( a o n e { - } s i d e d l i m i t ) .$

Notice the plus sign in the symbol $x \to 1 ^ { + }$ . The number $x$ approaches $a = 1$ only from above. An ordinary limit $x \to 1$ requires us to accept $x$ on both sides of 1 (the exact value $x = 1$ is not considered). Since negative numbers are not allowed by the square root, we have a one-sided limit. It is $L = 0$ :

Suppose $\varepsilon$ is $1 / 1 0$ : Then the response could be $\delta = 1 / 1 0 0$ : A number below $1 / 1 0 0$ has a square root below $1 / 1 0$ : In this case the box must be made extremely narrow, $\delta$ much smaller than $\varepsilon$ , because the square root starts with infinite slope.

Those examples show the point of the $\varepsilon - \delta$ definition. (Given $\varepsilon$ , look for ı: This came from CauchÑy in France, not Socrates in Greece.) We also see its bad feature: The test is not convenient. Mathematicians do not go around proposing $\varepsilon$ ’s and replying with ${ \boldsymbol { \delta } } ^ { \prime } { \bf { s } }$ . We may live a strange life, but not that strange.

It is easier to establish once and for all that $5 x$ approaches its obvious limit $5 a$ : The same is true for other familiar functions: $x ^ { n } \to a ^ { n }$ and sin $x \to \sin a$ and $( 1 - x ) ^ { - 1 } \to ( 1 - a ) ^ { - 1 } .$ —except at $a = 1$ : The correct limit $L$ comes by substituting $x = a$ into the function. Thi¤s is exac¤tly the property of a “continuÑous function.” BefÑore the sÑection on continuous functions, we prove the Squeeze Theorem using $\varepsilon$ and $\boldsymbol { \delta }$ :

2H SqueezeTheorem Suppose $f ( x ) \leqslant g ( x ) \leqslant h ( x )$ for $x$ near $a$ : If $f ( x )  { \ v { \mathbf { l } } }$ $L$ and $h ( x )  L$ as $x \to a$ , then the limit of $g ( x )$ is also $L$ :

Proof $g ( x )$ is squeezed between $f ( x )$ and $h ( x )$ : After subtracting $L$ $, g ( x ) - L$ is between $f ( x ) - L$ and $h ( x ) - L$ : Therefore

$$
| g ( x ) - L | < \varepsilon \quad { \mathrm { i f } } \quad | f ( x ) - L | < \varepsilon \quad { \mathrm { a n d } } \quad | h ( x ) - L | < \varepsilon .
$$

For any $\varepsilon$ , the last two inequalities hold in some region $0 < \left| x - a \right| < \delta$ : So the first one also holds. This proves that $g ( x )  L$ : Values at $x = a$ are not involved—until we get to continuous functions.