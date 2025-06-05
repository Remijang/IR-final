# CHAPTER 7

# Techniques of Integration

Chapter 5 introduced the integral as a limit of sums. The calculation of areas was started—by hand or computer. Chapter 6 opened a different door. Its new functions $e ^ { x }$ and $\ln x$ led to differential equations. You might say that all along we have been solving the special differential equation $d f / d x = v ( x )$ . The solution is $f = \int v ( x ) d x$ . But the step to $d y / d x = c y$ was a breakthrough.

The truth is that we are able to do remarkable things. Mathematics has a language, and you are learning to speak it. A short time ago the symbols $d y / d x$ and $\int v ( x ) d x$ were a mystery. (My own class was not too sure about $v ( x )$ itself—the symbol for a function.) It is easy to forget how far we have come, in looking ahead to what is next.

I do want to look ahead. For integrals there are two steps to take—more functions and more applications. By using mathematics we make it live. The applications are most complete whe»n we know the int»egral. This short chapter will widen (very much) the range of functions we can integrate. A computer with symbolic algebra widens it more.

Up to now, integration depended on recognizing derivatives. If $v ( x ) = \sec ^ { 2 } { x }$ then $f ( x ) = \tan x$ . To integrate tan $x$ we use a substitution:

$$
\int { \frac { \sin x } { \cos x } } d x = - \int { \frac { d u } { u } } = - \ln u = - \ln \cos x .
$$

What we need now are techniques for other integrals, to change them around until we can attack them. Two examples are $\int x \cos x d x$ and $\int { \sqrt { 1 - x ^ { 2 } } } d x$ , which are not immediately recognizable. With integration by parts, and a new substitution, they become simple.

Those examples indicate where this chapter starts and stops. With reasonable effort (and the help of tables, which is fair) you can integrate important functions. With intense effort you could integrate even more functions. In older books that extra exertion was made—it tended to dominate the cours1e. Theyhad integrals like $\textstyle \int ( x + 1 ) d x / { \sqrt { 2 x ^ { 2 } - 6 x + 4 } }$ , which we could work on if we had to. Our time is too valuable for that! Like long division, the ideas are for us and their intricate elaboration is for the computer.

Integration by parts comes first. Then we do new substitutions. Partial fractions is a useful idea (already applied to the logistic equation $y ^ { \prime } { = } c y - b y ^ { 2 } )$ . In the last section $x$ goes to infinity or $y ( x )$ goes to infinity—but the area stays finite. These improper integrals are quite common. Chapter 8 brings the applications.