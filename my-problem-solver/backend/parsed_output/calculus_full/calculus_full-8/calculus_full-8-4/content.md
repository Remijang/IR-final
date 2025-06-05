# 8.4 Probability and Calculus

Discrete probability usually involves careful counting. Not many samples are taken and not many experiments are made. There is a list of possible outcomes, and a known probability for each outcome. But probabilities go far beyond red cards and black cards. The real questions are much more practical:

1. How often will too many passengers arrive for a flight ?   
2. How many random errors do you make on a quiz ?   
3. What is the chance of exactly one winner in a big lottery ?

Those are important questions and we will set up models to answer them.

There is another point. Discrete models do not involve calculus. The number of errors or bumped passengers or lottery winners is a small whole number. Calculus enters for continuous probability. Instead of results that exactly equal 1 or 2 or 3, calculus deals with results that fall in a range of numbers. Continuous probability comes up in at least two ways:

(A) An experiment is repeated many times and we take averages.   
$\mathbf { \left( B \right) }$ The outcome lies anywhere in an interval of numbers.

In the continuous case, the probability $p _ { n }$ of hitting a particular value $x = n$ becomes zero. Instead we have a probability density $p ( x )$ —which is a key idea. The chance that a random $X$ falls between a and $b$ is found by integrating the density $p ( x )$ :

$$
{ \mathrm { P r o b } } \left\{ a \leqslant X \leqslant b \right\} = \int _ { a } ^ { b } p ( x ) d x .
$$

Roughly speaking, $p ( x ) d x$ is the chance of falling between $x$ and $x + d x$ : Certainly $p ( x ) \geqslant 0$ : If $a$ and $b$ are the extreme limits $- \infty$ and $\infty$ , including all possible outcomes, the probability is necessarily one:

$$
\textstyle \operatorname* { P r o b } { \bigl \{ - \infty < X < + \infty \bigr \} } = \int _ { - \infty } ^ { \infty } p ( x ) d x = 1 .
$$

This is a case where infinite limits of integration are natural and unavoidable. In studying probability they create no difficulty—areas out to infinity are often easier.

Here are typical questions involving continuous probability and calculus:

4. How conclusive is a $5 3 \% - 4 7 \%$ poll of 2500 voters ?   
5. Are 16 random football players safe on an elevator with capacity 3600 pounds ?   
6. How long before your car is in an accident ?

It is not so traditional for a calculus course to study these questions. They need extra thought, beyond computing integrals (so this section is harder than average). But probability is more important than some traditional topics, and also more interesting. Drug testing and gene identification and market research are major applications. Comparing Questions 1–3 with 4–6 brings out the relation of discrete to continuous— the differences between them, and the parallels.

It would be impossible to give here a full treatment of probability theory. I believe you will see the point (and the use of calculus) from our examples. Frank Morgan’s lectures have been a valuable guide.

# 8 Applications of the Integral

# DISCRETE RANDOM VARIABLES

A discrete random variable $X$ has a list of possible values. For two dice the outcomes are $X = 2 , 3$ ; : : : ; 12: For coin tosses (see below), the list is infinite: $X = 1 , 2 , 3 , \dots$ A continuous variable lies in an interval $a \leqslant X \leqslant b$ :

EXAMPLE 1 Toss a fair coin until heads come up. The outcome $X$ is the number of tosses. The value of $X$ is 1 or 2 or 3 or : : :, and the probability is $\frac { 1 } { 2 }$ that $X = 1$ (heads on the first toss). The probability of tails then heads is $\begin{array} { r } { p _ { 2 } = \frac { 1 } { 4 } } \end{array}$ : The probability that $X = n$ is $\begin{array} { r } { p _ { n } = ( \frac { 1 } { 2 } ) ^ { n } } \end{array}$ —this is the chance of $n - 1$ tails followed by heads. The sum of all probabilities is necessarily 1:

$$
p _ { 1 } + p _ { 2 } + p _ { 3 } + \cdots = { \textstyle { \frac { 1 } { 2 } } } + { \textstyle { \frac { 1 } { 4 } } } + { \textstyle { \frac { 1 } { 8 } } } + \cdots = 1 .
$$

EXAMPLE 2 Suppose a student (not you) makes an average of 2 unforced errors per hour exam. The number of actual errors on the next exam is $X = 0$ or 1 or 2 or : : : : A reasonable model for the probability of $n$ errors—when they are random and independent—is the Poisson model (pronounced Pwason):

$$
p _ { n } = p r o b a b i l i t y ~ o f n ~ e r r o r s = \frac { 2 ^ { n } } { n ! } ~ e ^ { - 2 } .
$$

The probabilities of no errors, one error, andtwo errors are $p _ { 0 } , p _ { 1 }$ ; and $p _ { 2 }$ :

$$
p _ { 0 } = { \frac { 2 ^ { 0 } } { 0 ! } } e ^ { - 2 } = { \frac { 1 } { 1 } } e ^ { - 2 } \approx . 1 3 5 \qquad p _ { 1 } = { \frac { 2 ^ { 1 } } { 1 ! } } e ^ { - 2 } \approx . 2 7 \qquad p _ { 2 } = { \frac { 2 ^ { 2 } } { 2 ! } } e ^ { - 2 } \approx . 2 7 .
$$

The probability of more than two errors is $1 - . 1 3 5 - . 2 7 - . 2 7 = . 3 2 5$ :

This Poisson model can be derived theoretically or tested experimentally. The total probability is again 1; from the infinite series (Section 6:6) for $e ^ { 2 }$ :

$$
p _ { 0 } + p _ { 1 } + p _ { 2 } + \cdots = \left( { \frac { 2 ^ { 0 } } { 0 ! } } + { \frac { 2 ^ { 1 } } { 1 ! } } + { \frac { 2 ^ { 2 } } { 2 ! } } + \cdots \right) e ^ { - 2 } = e ^ { 2 } e ^ { - 2 } = 1 .
$$

EXAMPLE 3 Suppose on average 3 out of 100 passengers with reservations don’t show up for a flight. If the plane holds 98 passengers, what is the probability that someone will be bumped ?

If the passengers come independently to the airport, use the Poisson model with 2 changed to 3: $X$ is the number of no-shows, and $X = n$ happens with probability $p _ { n }$ :

$$
p _ { n } = \frac { 3 ^ { n } } { n ! } e ^ { - 3 } \qquad p _ { 0 } = \frac { 3 ^ { 0 } } { 0 ! } e ^ { - 3 } \qquad p _ { 1 } = \frac { 3 ^ { 1 } } { 1 ! } e ^ { - 3 } = 3 e ^ { - 3 } .
$$

There are 98 seats and 100 reservations. Someone is bumped if $X = 0$ or $X = 1$ :

$$
{ \mathrm { c h a n c e ~ o f ~ b u m p i n g } } = p _ { 0 } + p _ { 1 } = e ^ { - 3 } + 3 e ^ { - 3 } \approx 4 / 2 0 .
$$

We will soon define the average or expected value or mean of $X$ —this model has $\mu = 3$ :

# 8.4 Probability and Calculus

# CONTINUOUS RANDOM VARIABLES

If $X$ is the lifetime of a VCR, all numbers $X \geqslant 0$ are possible. If $X$ is a sco¥re on the SAT, then $2 0 0 \leqslant X \leqslant 8 0 0$ : If $X$ is the fraction of computer owners in a poll of 600 people, $X$ is between 0 and 1: You may object that the SAT score is a whole number and the fraction of computer owners must be 0 or $1 / 6 0 0$ or $2 / 6 0 0$ or : : : : But it is completely impractical to work with 601 discrete possibilities. Instead we take $X$ to be a continuous random variable, falling anywhere in the range $X \geqslant 0$ or Œ200;800 or $0 \leqslant X \leqslant 1$ : Of course the various valu¤es o f $X$ are not equally probable.

EXAMPLE 4 The average lifetime of a VCR is 4 years. A reasonable model for breakdown time is an exponential random variable. Its probability density is

$$
\textstyle p ( x ) = { \frac { 1 } { 4 } } e ^ { - x / 4 } \quad { \mathrm { f o r } } \quad 0 \leqslant x < \infty .
$$

The probability that the VCR will eventually break is 1:

$$
\begin{array} { r } { \int _ { 0 } ^ { \infty } \frac { 1 } { 4 } e ^ { - x / 4 } d x = \left[ - e ^ { - x / 4 } \right] _ { 0 } ^ { \infty } = 0 - ( - 1 ) = 1 . } \end{array}
$$

The probability of breakdown within 12 years ( $X$ from 0 to 12) is :95:

$$
\begin{array} { r } { \int _ { 0 } ^ { 1 2 } \frac 1 4 e ^ { - x / 4 } d x = \left[ - e ^ { - x / 4 } \right] _ { 0 } ^ { 1 2 } = - e ^ { - 3 } + 1 \approx . 9 5 . } \end{array}
$$

An exponential distribution has $p ( x ) = a e ^ { - a x }$ : Its integral from 0 to $x$ is $F ( x ) = 1 - e ^ { - a x }$ : Figure 8.11 is the graph for $a = 1$ : It shows the area up to $x = 1$ : To repeat: The probability that $a \leqslant X \leqslant b$ is the integral of $p ( x )$ from a to $b$ .

$$
1 / e ^ { 2 } \underbrace { \left[ \begin{array} { l l l l l l l l } { \displaystyle \uparrow } & { \displaystyle \uparrow } & { \displaystyle \uparrow } & { \displaystyle } & { \displaystyle 4 . 5 e ^ { - 3 } } \end{array} \right] } _ { \displaystyle \uparrow } \underbrace { \uparrow } _ { \begin{array} { l } { \displaystyle 1 / e ^ { 2 } } \\ { \displaystyle 1 / e ^ { 2 } } \end{array} } \underbrace { \left[ \begin{array} { l l l l l l l } { \displaystyle \uparrow } & { \displaystyle \uparrow } & { \displaystyle \uparrow } & { \displaystyle } & { \displaystyle } & { \displaystyle } & { \displaystyle } & { \displaystyle } & { \displaystyle ^ { 1 } } \\ { \displaystyle \downarrow } & { \displaystyle 1 / e ^ { 2 } } \end{array} \right] } _ { \displaystyle 0 } \underbrace { \left[ \begin{array} { l l l l l l l l } { \displaystyle \downarrow } & { \displaystyle \uparrow } & { \displaystyle } & { \displaystyle } & { \displaystyle } & { \displaystyle } & { \displaystyle } & { \displaystyle } & { \displaystyle } & { \displaystyle } \\ { \displaystyle 0 } & { \displaystyle 1 / e ^ { 2 } } & { \displaystyle 3 } & { \displaystyle 0 } & { \displaystyle 1 / e ^ { 3 } } \end{array} \right] } _ { \displaystyle 0 } \underbrace { \left[ \begin{array} { l l l l l l l l } { \displaystyle \downarrow } & { \displaystyle } & { \displaystyle } & { \displaystyle } & { \displaystyle } & { \displaystyle } & { \displaystyle } & { \displaystyle } & { \displaystyle } \\ { \displaystyle 0 } & { \displaystyle 1 / e ^ { 2 } } & { \displaystyle 3 } & { \displaystyle 0 } & { \displaystyle 1 / e ^ { 3 } } \end{array} \right] } _ { \displaystyle 0 } \underbrace { \left[ \begin{array} { l l l l l l l l } { \displaystyle \downarrow } & { \displaystyle } & { \displaystyle } & { \displaystyle } & { \displaystyle } & { \displaystyle } & { \displaystyle } & { \displaystyle } & { \displaystyle } \\ { \displaystyle \downarrow } & { \displaystyle } & { \displaystyle } & { \displaystyle } & { \displaystyle } & { \displaystyle } & { \displaystyle } & { \displaystyle } & { \displaystyle } \\ { \displaystyle 0 } & { \displaystyle 0 } & { \displaystyle 1 / e ^ { 2 } } & { \displaystyle 3 } & { \displaystyle 0 } & { \displaystyle 0 } & { \displaystyle 1 / e ^ { 3 } } \end{array} \right] } _ { \displaystyle 0 } ,
$$

EXAMPLE 5 We now define the most important density8fu nctio n.8Suppose the average SAT score is 500; and the standard deviation (defined below—it measures the spread around the average) is 200: Then the normal distribution of grades has

$$
p ( x ) = \frac { 1 } { 2 0 0 \sqrt { 2 \pi } } e ^ { - ( x - 5 0 0 ) ^ { 2 } / 2 ( 2 0 0 ) ^ { 2 } } \quad \mathrm { f o r } \quad - \infty < x < \infty .
$$

This is the normal (or Gaussian) distribution with mean 500 and standard deviation 200: The graph of $p ( x )$ is the famous bell-shaped curve in Figure 8.12.

A new objection is possible.8The actual scores are between 200 and 800, while the density $p ( x )$ extends all the way from $- \infty$ to $\infty$ : I think the Educational Testing Service counts all scores over 800 as 800: The fraction of such scores is pretty small—in fact the normal distribution gives

$$
\operatorname* { P r o b } { \big \{ } X \geqslant 8 0 0 { \big \} } = \int _ { 8 0 0 } ^ { \infty } { \frac { 1 } { 2 0 0 { \sqrt { 2 \pi } } } } e ^ { - ( x - 5 0 0 ) ^ { 2 } / 2 ( 2 0 0 ) ^ { 2 } } d x \approx . 0 0 1 3 .
$$

Regrettably, $e ^ { - x ^ { 2 } }$ has no elementary antiderivative. We need numerical integration. But there is nothing the matter with that! The integral is called the “error function,” and special tables give its value to great accuracy. The integral of $e ^ { - x ^ { 2 } / 2 }$ from $- \infty$ to $\infty$ is exactly $\sqrt { 2 \pi }$ : Thendivision by $\sqrt { 2 \pi }$ keeps $\int p ( x ) d x = 1$ :

Notice that the normal distribution involves two parameters. They are the mean value (in this case $\mu = 5 0 0 _ { , }$ ) and the standard deviation (in this case $\sigma = 2 0 0$ ). Those numbers mu and sigma are often given the “normalized” values $\mu = 0$ and $\sigma = 1$ :

$$
p ( x ) = { \frac { 1 } { \sigma { \sqrt { 2 \pi } } } } e ^ { - ( x - \mu ) ^ { 2 } / 2 \sigma ^ { 2 } } \quad { \mathrm { b e c o m e s } } \quad p ( x ) = { \frac { 1 } { \sqrt { 2 \pi } } } e ^ { - e ^ { 2 } / 2 } .
$$

The bell-shaped graph of $p$ is symmetric around the middle point $x = \mu$ : The width of the graph is governed by the second parameter $\sigma$ —which stretches the $x$ axis and shrinks the $y$ ax¤is (uleaving8total area equal to 1). The axes are labeled to show the standard case $\mu = 0 , \sigma = 1$ and also the graph for any other $\mu$ and $\sigma$ :

We now give a name to the integral of $p ( x )$ : The limits will be $- \infty$ and $x$ , so the integral $F ( x )$ m ea8sures the probability that $\mathbf { \Delta } _ { \pmb { a } }$ r8ando8m sample is below $x$ :

$$
\begin{array} { r } { \operatorname { P r o b } \left\{ X \leqslant x \right\} = \int _ { - \infty } ^ { x } p ( x ) d x = c u m u l a t i v e d e n s i t y f u n c t i o n F ( x ) . } \end{array}
$$

$F ( x )$ accumulates the probabilities given by $p ( x )$ , so $d F / d x = p ( x )$ : The total probability is $F ( \infty ) = 1$ : This integral from $- \infty$ to $\infty$ covers all outcomes.

Figure 8.12b shows the integral of the bell-shaped normal distribution. The middle point $x = \mu$ has $\begin{array} { r } { F = \frac { 1 } { 2 } } \end{array}$ : By symmetry there is a $5 0 - 5 0 \$ chance of an outcome below the mean. The cumulative density $F ( x )$ is near : $l 6$ at $\mu - \sigma$ and near :84 at $\mu + \sigma$ : The chance of falling in between is : $8 4 - . 1 6 = . 6 8$ : Thus $68 \%$ of the outcomes are less than one deviation $\sigma$ away from the center $\mu$ :

Moving out to $\mu - 2 \sigma$ and $\mu + 2 \sigma$ , $9 5 \%$ of the area is in between. With $9 5 \%$ confidence $X$ is less than two deviations from the mean. Only one sample in 20 is further out (less than one in 40 on each side).

Note that $\sigma = 2 0 0$ is not the precise value for the SAT!

# MEAN, VARIANCE, AND STANDARD DEVIATION

In Example 1, $X$ was the number of coin tosses until the appearance of heads. The probabilities were $\begin{array} { r } { p _ { 1 } = \frac { 1 } { 2 } , p _ { 2 } = \frac { 1 } { 4 } , p _ { 3 } = \frac { 1 } { 8 } } \end{array}$ ; : :: What is the averagenumber of tosses ? We now find the “mean” $\mu$ of any distribution $p ( x )$ —not only the normal distribution, where symmetry guarantees that the built-in number $\mu$ is the mean.

To find $\mu$ ; multiply outcomes by probabilities and add:

$$
\mu = m e a n = \sum n p _ { n } = 1 ( p _ { 1 } ) + 2 ( p _ { 2 } ) + 3 ( p _ { 3 } ) + \cdots .
$$

The average number of tosses is $1 ( { \textstyle { \frac { 1 } { 2 } } } ) + 2 ( { \textstyle { \frac { 1 } { 4 } } } ) + 3 ( { \textstyle { \frac { 1 } { 8 } } } ) + \cdots$ : This series adds up (in Section 10:1) to $\mu = 2$ : Please do the experiment 10 times. I am almost certain that the average will be near 2:

When the average is $\lambda = 2$ quiz errors or $\lambda = 3$ no-shows, the Poisson probabilities are $p _ { n } = \lambda ^ { n } e ^ { - \lambda } / \bar { n } !$ Š Check that the formula ${ \boldsymbol { \mu } } = \Sigma n p _ { n }$ does give $\lambda$ as the mean:

$$
\left[ 1 \frac { \lambda } { 1 ! } + 2 \frac { \lambda ^ { 2 } } { 2 ! } + 3 \frac { \lambda ^ { 3 } } { 3 ! } + \cdots \right] e ^ { - \lambda } = \lambda \left[ 1 + \frac { \lambda } { 1 ! } + \frac { \lambda ^ { 2 } } { 2 ! } + \cdots \right] e ^ { - \lambda } = \lambda e ^ { \lambda } e ^ { - \lambda } = \lambda .
$$

For continuous probability, the sum ${ \boldsymbol { \mu } } = \Sigma { \boldsymbol { n } } p _ { n }$ changes to $\textstyle \mu = \int x p ( x ) d x$ : We multiply outcome $x$ by probability $p ( x )$ and integrate. In the VCR model, integration by parts gives a mean breakdown time of $\mu = 4$ years:

$$
\begin{array} { r } { \int x ~ p ( x ) d x = \int _ { 0 } ^ { \infty } x ( \frac { 1 } { 4 } e ^ { - x / 4 } ) d x = \left[ - x e ^ { - x / 4 } - 4 e ^ { - x / 4 } \right] _ { 0 } ^ { \infty } = 4 . } \end{array}
$$

Together with the meanwe introduce the variance. It is always written $\sigma ^ { 2 }$ , and in the normal distribution that measured the “width” of the curve. When $\sigma ^ { 2 }$ was $2 0 0 ^ { 2 }$ , SAT scores spread out pretty far. If the testing service changed to $\sigma ^ { 2 } = 1 ^ { 2 }$ , the scores would be a disaster. $9 5 \%$ of them would be within $\pm 2$ of the mean. When a teacher announces an average grade of 72, the variance should also be announced—if it is big then those with 60 can relax. At least they have company.

The standard deviation (written $\sigma$ ) is the square root of $\sigma ^ { 2 }$ :

EXAMPLE 6 (Yes-no poll, one person asked) The probabilities are $p$ and $1 - p$ :

A fraction $\begin{array} { r } { p = \frac { 1 } { 3 } } \end{array}$ of the population thinks yes, the remaining fraction $\textstyle 1 - p = { \frac { 2 } { 3 } }$ thinks no. Suppose we only as?k one person. If $X = 1$ for yes and $X = 0$ for no, the expected value of $X$ is $\begin{array} { r } { \dot { \mu } = p = \frac { 1 } { 3 } } \end{array}$ : The variance is $\begin{array} { r } { \sigma ^ { 2 } = \dot { p } ( 1 - p ) = \frac { 2 } { 9 } } \end{array}$ :

$$
\mu = 0 \left( { \frac { 2 } { 3 } } \right) + 1 \left( { \frac { 1 } { 3 } } \right) = { \frac { 1 } { 3 } } \qquad { \mathrm { a n d } } \qquad \sigma ^ { 2 } = \left( 0 - { \frac { 1 } { 3 } } \right) ^ { 2 } \left( { \frac { 2 } { 3 } } \right) + \left( 1 - { \frac { 1 } { 3 } } \right) ^ { 2 } \left( { \frac { 1 } { 3 } } \right) = { \frac { 2 } { 9 } } .
$$

The standard deviation is $\sigma = \sqrt { 2 / 9 }$ : When the fraction $p$ is near one or near zero, the spread is smaller—and one person is more likely to give the right answer for everybody. The maximum of $\sigma ^ { 2 } = p ( 1 - p )$ is at $\begin{array} { r } { p = \frac { 1 } { 2 } } \end{array}$ , where $\begin{array} { r } { \sigma = \frac { \overline { { 1 } } } { 2 } } \end{array}$ :

The table shows $\mu$ and $\sigma ^ { 2 }$ for important probability distributions.

# THE LAW OF AVERAGESAND THE CENTRAL LIMIT THEOREM

We come to the center of probability theory (without intending to give proofs). The key idea is to repeat an experiment many times—poll many voters, or toss many dice, or play considerable poker. Each independent experiment produces an outcome $X$ , and the average from $N$ experiments is $\bar { X }$ : It is called “ $X$ bar”:

$$
{ \bar { X } } = { \frac { X _ { 1 } + X _ { 2 } + \cdots + X _ { N } } { N } } = { \mathrm { a v e r a g e ~ o u t c o m e } } .
$$

All we know about $p ( x )$ is its mean $\mu$ and variance $\sigma ^ { 2 }$ : It is amazing how much information that gives about the average $\bar { X }$ :

8F Law of Averages: $\bar { X }$ is almost sure to approach $\mu$ as $N \to \infty$ : Central Limit Theorem: The probability density $p _ { N } ( x )$ for $\bar { X }$ approaches a normal distribution with the same mean $\mu$ and variance $\sigma ^ { 2 } / N$ :

No matter what the probabilities for $X$ , the probabilities for $\bar { X }$ move toward the normal bell-shaped curve. The standard deviation is close to $\sigma / \sqrt { N }$ when the experiment is repeated $N$ times. In the Law of Averages, “almost sure” means that the chance of $\bar { X }$ not approaching $\mu$ is zero. It can happen, but it won’t.

Remark 1 The Boston Globe doesn’t understand the Law of Averages. I quote from September 1988 W “What would happen if a giant Red Soxslump arrived ? What would happen if the fabled Law of Averages came into play, reversing all those can’t miss decisions during the winning streak ? ” They think the Law of Averages evens everything up, favoring heads aft?er a series of tails. See Problem 20:

EXAMPLE 7 Yes-no poll of $N = 2 5 0 0$ voters. Is a $5 3 \% - 4 7 \%$ outcome conclusive ?

The fraction $p$ of “yes” voters in the whole population is not known. That is the reason for the poll. The deviation $\sigma = { \sqrt { p ( 1 - p ) } }$ is also not known, but for one voter this is never more than $\frac { 1 } { 2 }$ (when $\begin{array} { r } { p = \frac { 1 } { 2 } . } \end{array}$ ). Therefore $\sigma / \sqrt { N }$ for 2500 voters is no larger than $\scriptstyle { \frac { 1 } { 2 } } / { \sqrt { 2 5 0 0 } }$ , which is $1 \%$ :

The result of the poll was $\bar { X } = 5 3 \%$ : With $9 5 \%$ confidence, this sample is within two standard deviations (here $2 \%$ ) of its mean. Therefore with $9 5 \%$ confidence, the unknown mean $\mu = p$ of the whole population is between $51 \%$ and $5 5 \%$ . This poll is conclusive.

If the true mean had been $p = 5 0 \%$ , the poll would have had only a :0013 chance of reaching $53 \%$ : The error margin on each side of a poll is a?mazingly simple; it is always $1 / \hat { \sqrt { N } }$ :

Remark 2 The New York Times has better mathematicians than the Globe. Two days after Bush defeated Dukakis, their poll of $N = 1 1 , 6 4 5$ voters was printed with the following explanation. “In theory, in 19 cases out of 20 [there is $9 5 \% ]$ ] the results should differ by no more than one percentage point [there is $\overset { \mathcal { } } { 1 } / \overset { } { \sqrt { N } } \overset { } { ] }$ from what would have been obtained by seeking out all voters in the United States.”

EXAMPLE 8 Football players at Caltech (if any) have average weight $\mu = 2 1 0$ pounds and standard deviation $\sigma = 3 0$ pounds. Are $N = 1 6$ players safe on an elevator with capacity 3600 pounds ? 16 times 210 is 3360:

# 8.4 Probability and Calculus

The average weight $\bar { X }$ is approximately a normal random variable with $\bar { \mu } = 2 1 0$ and $\bar { \sigma } = 3 0 / \sqrt { N } = 3 0 / 4$ : There is only a $2 \%$ chance that $\bar { X }$ is above $\bar { \mu } + 2 \bar { \sigma } = 2 2 5$ (see Figure 8.12b—weights below the mean are no problem on an elevator). Since 16 times 225 is 3600, a statistician would have $98 \%$ confidence that the elevator is safe. This is an example where $98 \%$ is not good enough—I wouldn’t get on.

EXAMPLE 9 (The famous Weldon Dice) Weldon threw 12 dice 26;306 times and counted the 5’s and $6 \mathrm { ^ { \circ } s }$ . They came up in $3 3 . 7 7 \%$ of the 315; 672 separate rolls. Thus $\bar { X } = . 3 3 7 7$ instead of the expected fraction $\begin{array} { r } { p = \frac { 1 } { 3 } } \end{array}$ of 5’s and 6’s. Were the dice fair ?

The variance in each roll is $\sigma ^ { 2 } = p ( 1 - p ) = 2 / 9$ : The standard deviation of $\bar { X }$ is $\bar { \sigma } = \sigma / \sqrt { N } = \sqrt { 2 / 9 } / \sqrt { 3 1 5 6 7 2 } \approx . 0 0$ 084: For fair dice, there is a $9 5 \%$ chance that $\bar { X }$ will differ from $\textstyle { \frac { 1 } { 3 } }$ by less than $2 \bar { \sigma }$ : (For Poisson probabilities that is false. Here $\bar { X }$ is normal.) But :3377 differs from :3333 by more than $5 \bar { \sigma }$ : The chance of falling 5 standard deviations away from the mean is only about 1 in $1 0 , 0 0 0 . { \dagger }$

So the dice were unfair. The faces with 5 or 6 indentations were lighter than the others, and a little more likely to come up. Modern dice are made to compensate for that, but Weldon never tried again.