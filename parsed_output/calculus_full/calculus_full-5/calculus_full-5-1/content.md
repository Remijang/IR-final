# 5.1 The Idea of the Integral

This chapter is about the idea of integration, and also about the technique of integration. We explain how it is done in principle, and then how it is done in practice. Integration is a problem of adding up infinitely many things, each of which is infinitesimally small. Doing the addition is not recommended. The whole point of calculus is to offer a better way.

The problem of integration is to find a limit of sums. The key is to work backward from a limit of differences (which is the derivative). We can integrate $v ( x )$ if $\dot { \pmb { u } }$ turns up as the derivative of another function $f ( x )$ . The integral of $v = \cos x$ is $f = \sin x$ . The integral of $v = x$ is $\textstyle f = { \frac { 1 } { 2 } } x ^ { 2 }$ . Basically, $f ( x )$ is an “antiderivative”. The list of $f$ ’s will grow much longer (Section 5:4 is crucial). A selection is inside the cover of this book. If we don’t find a suitable $f ( x )$ , numerical integration can still give an excellent answer.

I could go directly to the formulas for integrals, which allow you to compute areas under the most amazing curves. (Area is the clearest example of adding up infinitely many infinitely thin rectangles, so it always comes first. It is certainly not the only problem that integral calculus can solve.) But I am really unwilling just to write down formulas, and skip over all the ideas. Newton and Leibniz had an absolutely brilliant intuition, and there is no reason why we can’t share it.

They started with something simple. We will do the same.

# SUMS AND DIFFERENCES

Integrals and derivatives can be mostly explained by working (very briefly) with sums and differences. Instead of functions, we have $n$ ordinary numbers. The key idea is nothing more than a basic fact of algebra. In the limit as $n \to \infty$ , it becomes the basic fact of calculus. The step of “going to the limit” is the essential difference between algebra and calculus! It has to be taken, in order to add up infinitely many infinitesimals—but we start out this side of it.

To see what happens before the limiting step, we need two sets of n numbers. The first set will be $v _ { 1 } , v _ { 2 } , \ldots , v _ { n }$ , where $v$ suggests velocity. The second set of numbers will be $f _ { 1 } , f _ { 2 } , \ldots , f _ { n }$ ; where $f$ recalls the idea of distance. You might think $d$ would be a better symbol for distance, but that is needed for the $d x$ and $d y$ of calculus.

A first example has $n = 4$ :

$$
v _ { 1 } , v _ { 2 } , v _ { 3 } , v _ { 4 } = 1 , 2 , 3 , 4 \qquad f _ { 1 } , f _ { 2 } , f _ { 3 } , f _ { 4 } = 1 , 3 , 6 , 1 0 .
$$

The relation between the $v$ ’s and $f$ ’s is seen in that example. When you are given 1;3;6;10; how do you produce $1 , 2 , 3 , 4 \mathrm { ? } \ B y$ taking differences. The difference between 10 and 6 is 4. Subtracting $6 - 3$ is 3. The difference $f _ { 2 } - f _ { 1 } = 3 - 1$ is $v _ { 2 } = 2$ . Each $v$ is the difference between two $f$ ’s:

$$
v _ { j } i s t h e d i f f e r e n c e f _ { j } - f _ { j - 1 } .
$$

This is the discrete form of the derivative. I admit to a small difficulty at $j = 1$ , from the fact that there is no $f _ { 0 }$ . The first $v$ should be $f _ { 1 } - f _ { 0 }$ , and the natural idea is to agree that $f _ { 0 }$ is zero. This need for a starting point will come back to haunt us (or help us) in calculus.

Now look again at those same numbers—but start with $v$ . From $v = 1 , 2 , 3 , 4$ how do you produce $f = 1 , 3 , 6 , 1 0 ? B y$ taking sums. The first two $v$ ’s add to 3, which is $f _ { 2 }$ . The first three $v$ ’s add to $f _ { 3 } = 6$ . The sum of all four $v$ ’s is $1 + 2 + 3 + 4 = 1 0$ . Taking sums is the opposite of taking differences.

That idea from algebra is the key to calculus. The sum $f _ { j }$ involves all the numbers $v _ { 1 } + v _ { 2 } + \cdots + v _ { j } ,$ . The difference $v _ { j }$ involves only the two numbers $f _ { j } - f _ { j - 1 }$ . The fact that one reverses the other is the “Fundamental Theorem.” Calculus will change sums to integrals and differences to derivatives—but why not let the key idea come through now?

5A Fundamental Theorem of Calculus (before limits):

$$
I f e a c h v _ { j } = f _ { j } - f _ { j - 1 } , t h e n v _ { 1 } + v _ { 2 } + \cdots + v _ { n } = f _ { n } - f _ { 0 } .
$$

The differences of the $f$ ’s add up to $f _ { n } - f _ { 0 }$ . All $f$ ’s in between are canceled, leaving only the last $f _ { n }$ and the starting $f _ { 0 }$ . The sum “telescopes”:

$$
v _ { 1 } + v _ { 2 } + v _ { 3 } + \cdots + v _ { n } = ( f _ { 1 } - f _ { 0 } ) + ( f _ { 2 } - f _ { 1 } ) + ( f _ { 3 } - f _ { 2 } ) + \cdots + ( f _ { n } - f _ { n - 1 } ) { \mathrm { , } }
$$

The number $f _ { 1 }$ is canceled by $- f _ { 1 }$ . Similarly $- f _ { 2 }$ cancels $f _ { 2 }$ and $- f _ { 3 }$ cancels $f _ { 3 }$ Eventually $f _ { n }$ and $- f _ { 0 }$ are left. When $f _ { 0 }$ is zero, the sum is the final $f _ { n }$ .

That completes the algebra. We add the v’s by finding the $f$ ’s.

Question How do you add the odd numbers $1 + 3 + 5 + \cdots + 9 9$ (the $v$ ’s)? Answer They are the differences between 0; 1; 4; 9; : : :: These $f$ ’s are squares. By the Fundamental Theorem, the sum of 50 odd numbers is $( 5 0 ) ^ { 2 }$ .

The tricky part is to discover the right $f$ ’s! Their differences must produce the $v$ ’s. In calculus, the tricky part is to find the right $f ( x )$ . Its derivative must produce $v ( x )$ . It is remarkable how often $f$ can be found—more often for integrals than for sums. O?ur n?ext s?tep is to u?nderstand how the integral is a limit of sums.

# SUMS APPROACH INTEGRALS

Suppose you start a successful company. The rate of income is increasing. After $x$ years, the income per year is $\sqrt { x }$ million dollars. In the first four years you reach ${ \sqrt { 1 } } , { \sqrt { 2 } } , { \sqrt { 3 } }$ ; and $\sqrt { 4 }$ million dollars. Those numbers are displayed in a bar graph (Figure 5.1a, for investors). I realize that most start-up companies make losses, but your company is an exception. If the example is too good to be true, please keep reading.

The graph shows four rectangles, of heights ${ \sqrt { 1 } } , { \sqrt { 2 } } , { \sqrt { 3 } } , { \sqrt { 4 } }$ . Since the base of each rectangle is one year, those numbers are also the areas of the rectangles. One investor, possibly weak in arithmetic, asks a simple question: What is the total income for all four years? There are two ways to answer, and I will give both.

The first answer is ${ \sqrt { 1 } } + { \sqrt { 2 } } + { \sqrt { 3 } } + { \sqrt { 4 } }$ . Addition gives 6:15 million dollars. Figure 5.1b shows this total—which is reached at year 4. This is exactly like velocities and distances, but now $v$ is the income per year and $f$ is the total income. Algebraically, $f _ { j }$ is still $v _ { 1 } + \cdots + v _ { j }$ .

The second answer comes from geometry. The total income is the total area of the rectangles. We are emphasizing the correspondence between addition and area. That point may seem obvious, but it becomes important when a second investor (smarter than the first) asks a harder question.

Here is the problem. The incomes as stated are false. The company did not make a million dollars the first year. After three months, when $x$ was $1 / 4$ ; the rate of income was only $\sqrt { x } = 1 / 2$ . The bar graph showed ${ \sqrt { 1 } } = 1$ f?or the wh?ole year, but t?hat was an overstatement. The income in three months was not more than $1 / 2$ times $1 / 4$ ; the rate multiplied by the time.

All other quarters and years were also overstated. Figure 5.2a is closer to reality, with 4 years divided into 16 quarters. It gives a new estimate for total income.

Again there are two ways to find the total. We add ${ \sqrt { 1 / 4 } } + { \sqrt { 2 / 4 } } + \cdots + { \sqrt { 1 6 / 4 } }$ , remembering to multiply them all by $1 / 4$ (because each rate applies to $1 / 4$ year). This is also the area of the 16 rectangles. The area approach is better because the $1 / 4$ is automatic. Each rectangle has base $1 / 4$ ; so that factor enters each area. The total area is now 5:56 million dollars, closer to the truth.

You see what is coming. The next step divides time into weeks. After one week the rate $\sqrt { x }$ only $\sqrt { 1 / 5 2 }$ . That is the height of the first rectangle—its base is $\Delta x =$ $1 / 5 2$ . There is a rectangle for every week. Then a hard-working investor divides time into days, and the base of each rectangle is $\Delta x = 1 / 3 6 5$ . At that point there are $4 \times 3 6 5 = 1 4 6 0$ rectangles, or 1461 because of leap year, with a total area below $5 \frac 1 2$ million dollars. The calculation is elementary but?depress?ing—adding?up thousands of square roots, each multiplied by $\Delta x$ from the base. There has to be a better way.



The better way, in fact the best waÑy, is calculus. The whole idea is to allow for continuous change: The geometry problem is to find the area under the square root curve. That question cannot be answered by arithmetic, because it involves a limit. The rectangles have base $\Delta x$ and heights ${ \sqrt { \Delta x } } , { \sqrt { \Delta 2 x } } , . . . , { \sqrt { 4 } }$ . There are $4 / \Delta x$ rectangles—more and more terms from thinner and thinner rectangles. The area is the limit of the sum as $\Delta x \to 0$ .

This limiting area is the “integral.” We are looking for a number below $5 \frac 1 2$

Algebra (area of n rectangles): Compute $v _ { 1 } + \cdots + v _ { n }$ by finding $f$ ’s. Key idea: If $v _ { j } = f _ { j } - f _ { j - 1 }$ , then the sum is $f _ { n } - f _ { 0 }$ . Calculus (area under curve): Compute the limit of $\Delta x [ v ( \Delta x ) + v ( 2 \Delta x ) + \cdot \cdot \cdot ]$ Key idea: If $v ( x ) = d f / d x$ then area $\ b =$ integral to be explained next.