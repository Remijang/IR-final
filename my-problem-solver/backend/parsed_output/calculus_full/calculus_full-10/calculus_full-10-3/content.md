# 10.3 Convergence Tests: All Series

This section finally allows the numbers $a _ { n }$ to be negative. The geometric series $1 - { \frac { 1 } { 2 } } + { \frac { 1 } { 4 } } - { \frac { 1 } { 8 } } + \cdot \dot { \bf \Phi } = { \frac { 1 } { 3 } }$ is certainly allowed. So is the series $\pi = { \bar { 4 } } - { \textstyle \frac { 4 } { 3 } } + { \textstyle \frac { 4 } { 5 } } - { \textstyle \frac { 4 } { 7 } } +$ . If we change all signs to $^ +$ , the geo |met|ric series would still converge (to the larger sum 2). This is the first test, to bring b|ac|k a positive series by taking the absolute value $\left| a _ { n } \right|$ of every term.

DEFINITION The series $\Sigma a _ { n }$ is “absolutely convergent” if $\Sigma \left| a _ { n } \right|$ is convergent.

Changing a negative number from $\scriptstyle a _ { n }$ |to $\left| a _ { n } \right|$ increases the sum. Main point: The smaller series $\Sigma a _ { n }$ is sure to converge if $\Sigma \left| a _ { n } \right|$ converges.

10G If $\Sigma \left| a _ { n } \right|$ converges then $\Sigma a _ { n }$ converges (absolutely). But $\Sigma a _ { n }$ might converge, as in the series for $\pi$ , even if $\Sigma \left| a _ { n } \right|$ diverges to infinity.

EXAMPLE 1 Start with the positive series ${ \frac { 1 } { 2 } } + { \frac { 1 } { 4 } } + { \frac { 1 } { 8 } } + \cdots$ . Change any signs to minus. Then the new series converges (absolutely). The right choice of signs will make it converge to any number between $^ { - 1 }$ and 1.

EXA|MP|LE82 Start with the alternating series $1 - { \frac { 1 } { 2 } } + { \frac { 1 } { 3 } } - { \frac { 1 } { 4 } } + \cdots$ which converges to ln 2.|Ch|ange to plus signs. The new series $1 + { \frac { 1 } { 2 } } + { \frac { 1 } { 3 } } + \cdots$ diverges to infinity. The origin|al a|lternating series was not absolutely con |verg|ent. It was only “conditio n|all|y convergent.” A series can converge (conditionally) by a careful choice of signs—even if $\Sigma | a _ { n } | = \infty$ .

$H \Sigma | a _ { n } |$ converges then $\Sigma a _ { n }$ converges. Here is a quick proof. The numbers $a _ { n } + \left| a _ { n } \right|$ are either zero (if $a _ { n }$ is negative) or $2 | a _ { n } |$ . By comparison with $\Sigma 2 | a _ { n } |$ , which converges, $\Sigma ( a _ { n } + | a _ { n } | )$ must converge. Now subtract the convergent series $\Sigma | a _ { n } |$ . The difference $\Sigma a _ { n }$ also converges, completing the proof. All tests for positive series (integral, ratio, comparison, : : :) apply immediatelyto absolute convergence, because we switch to $\left| a _ { n } \right|$ .

EXAMPLE 3 Start with the geometric series ${ \frac { 1 } { 3 } } + { \frac { 1 } { 9 } } + { \frac { 1 } { 2 7 } } + \cdots$ which converges to $\frac { 1 } { 2 }$ . Change any of those signs to minus. Then the new series must converge (absolutely). But the sign changes cannot achieve all sums between $- \frac { 1 } { 2 }$ and $\frac { 1 } { 2 }$ . This time the sums belong to the famous (and very thin) Cantor set of Section 3.7.

EXAMPLE 4 (looking ahead) Suppose $\Sigma a _ { n } x ^ { n }$ converges for a particular number $x$ . The|n for e |ve ry $x$ nearer to zero, it converges absolutely. This will be proved and used in Section 10:6 on power series, where it is the most important step in the theory.

EXAMPLE 5 Since $\Sigma { 1 / n ^ { 2 } }$ converges, so does $\Sigma ( \cos n ) / n ^ { 2 }$ . That second series has irregular signs, but it converges absolutely by comparison with the first series (since $| \cos n | < 1 )$ . Probably $\Sigma ( \bar { \tan n } ) / n ^ { 2 }$ does not converge, because the tangent does not stay bounded like the cosine.

# ALTERNATING SERIES

The series $1 - { \frac { 1 } { 2 } } + { \frac { 1 } { 3 } } - { \frac { 1 } { 4 } } + \cdots$ converges to ln 2. That was stated without proof. This is an example of an alternating series, in which the signs alternate between plus and minus. There is the additional property that the absolute values $\begin{array} { r } { 1 , \frac { 1 } { 2 } , \frac { 1 } { 3 } , \frac { 1 } { 4 } } \end{array}$ ; : : : decrease to zero. Those two facts—decrease to z¤ero with altÑernating signs—guarantee convergence.



10H An alternating series $a _ { 1 } - a _ { 2 } + a _ { 3 } - a _ { 4 } \cdots$ converges (at least conditionally, maybe not absolutely) if every $a _ { n + 1 } \leqslant a _ { n }$ and ${ a _ { n } } \to 0$ .

The best proof is in Figure 10.3. Look at $a _ { 1 } - a _ { 2 } + a _ { 3 }$ . It is below $a _ { 1 }$ , because $a _ { 3 }$ (with plus sign) is smaller than $a _ { 2 }$ (with minus sign). The sum of five terms is less than the

sum of three terms, because $a _ { 5 }$ is smaller than $a _ { 4 }$ . These partial sums $s _ { 1 } , s _ { 3 } , s _ { 5 } , \ldots$ with an odd number of terms are decreasing.

Now look at two terms $a _ { 1 } - a _ { 2 }$ , then four terms, then six terms. Adding on $a _ { 3 } - a _ { 4 }$ increases the sum (because $a _ { 3 } \geqslant a _ { 4 }$ ). Similarly $s _ { 6 }$ is greater than $s _ { 4 }$ (because it includes $a _ { 5 } - a _ { 6 }$ which is positive). So the sums $s _ { 2 } , s _ { 4 } , s _ { 6 } , . . .$ are increasing.

The difference between $s _ { n - 1 }$ and $s _ { n }$ is the single number $\pm a _ { n }$ . It is required by 10H to approach zero. Therefore the decreasing sequence $s _ { 1 } , s _ { 3 }$ ; : : : approaches the same limit $s$ as the increasing sequence $s _ { 2 } , s _ { 4 }$ ; : : :: Theseries converges to $s$ , which always lies between $s _ { n - 1 }$ and $s _ { n }$ .

This plus-minus pattern is special but important. The positive series $\Sigma a _ { n }$ may not converge. The alternating series is $\Sigma ( - 1 ) ^ { \bar { n } + 1 } a _ { n }$ .

EXAMPLE 6 The alternating series $\textstyle 4 - { \frac { 4 } { 3 } } + { \frac { 4 } { 5 } } - { \frac { 4 } { 7 } } \cdots$ is conditionally convergent (to $\pi$ ). The absolute values decrease to zero. Is this series absolutely convergent ? No. With plus signs, $4 ( 1 + { \textstyle { \frac { 1 } { 3 } } } + { \textstyle { \frac { 1 } { 5 } } } + \cdots )$ diverges like the harmonic series.

EXAMPLE 7 The alternating series $1 - 1 + 1 - 1 + \cdots$ is not convergent at all. Which requirement in 10H is not met ? The partial sums $s _ { 1 } , s _ { 3 } , s _ { 5 } , \ldots$ all equal 1 and $s _ { 2 } , s _ { 4 } , s _ { 6 } , . . .$ all equal 0—but they don’t approach the saÑme limit $s$ .

# MULTIPLYING AND REARRANGING SERIES

In Section 10:1 we added and subtracted and multiplied series. Certainly addition and subtraction are safe. If one series has partial sums $s _ { n } \to s$ and the other has partial sums $t _ { n } \to t$ , then addition gives partial sums $s _ { n } + t _ { n } \to s + t$ . But multiplication is more dangerous, because the order of the multiplication can make a difference. More exactly, the order of terms is important when the series are conditionally convergent. For absolutely convergent series, the order makes no difference. We can rearrange their terms and multiply them in any order, and the sum and product comes out right:



10I Suppose $\Sigma a _ { n }$ converges absolutely. If $A _ { 1 } , A _ { 2 } , \ldots$ is any reordering of the $a$ ’s, then $\Sigma A _ { n } = \Sigma a _ { n }$ . In the new order $\textstyle \sum A _ { n }$ also converges absolutely. 10J Suppose $\Sigma a _ { n } = s$ and $\Sigma b _ { n } = t$ converges absolutely. Then the infinitely many terms $a _ { i } b _ { j }$ in their product add (in any order) to $^ { s t }$ .

Rather than proving 10I and 10J, we show what happens when there is only conditional convergence. Our favorite is $1 - { \textstyle { \frac { 1 } { 2 } } } + { \textstyle { \frac { 1 } { 3 } } } - { \textstyle { \frac { 1 } { 4 } } } + \cdots$ , converging conditionally to $\ln 2$ . By rearranging, it will converge conditionally to anything! Suppose the desired sum is 1000. Take positive terms $1 + { \frac { 1 } { 3 } } + \cdots$ until they pass 1000. Then add negative terms 21 41 until the subtotal drops below 1000. Then new positive terms bring it above 1000, and so on. All terms are eventually used, since at least one new term is needed at each step. The limit is $s = 1 0 0 0$ .

We also get strange products, when series fail to converge absolutely:

$$
\left( 1 - { \frac { 1 } { \sqrt { 2 } } } + { \frac { 1 } { \sqrt { 3 } } } \cdots \right) \left( 1 - { \frac { 1 } { \sqrt { 2 } } } + { \frac { 1 } { \sqrt { 3 } } } \cdots \right) = 1 - \left( { \frac { 1 } { \sqrt { 2 } } } + { \frac { 1 } { \sqrt { 2 } } } \right) + \left( { \frac { 1 } { \sqrt { 3 } } } + { \frac { 1 } { \sqrt { 4 } } } + { \frac { 1 } { \sqrt { 3 } } } \right) \cdots .
$$

On the left the series converge (conditionally). The alternating terms go to zero. On the right the series diverges. Its terms in parentheses don’t even approach zero, and the product is completely wrong.

I close by emphasizing that it is absolute convergence that matters. The most important series are power series $\Sigma a _ { n } x ^ { n }$ . Like the geometric series (with all $a _ { n } =$ 1) there is absolute convergence over an interval of $x$ ’s. They give functions of $x$ , which is what calculus needs and wants.

We go next to the series for $e ^ { x }$ , which is absolutely convergent everywhere. From the viewpoint of convergence tests it is too easy—the danger is gone. But from the viewpoint of calculus and its applications, $e ^ { x }$ is unconditionally the best.