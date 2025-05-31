# 1.5 Measurement Uncertainty, Accuracy, and Precision

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

• Define accuracy and precision   
• Distinguish exact and uncertain numbers   
• Correctly represent uncertainty in quantities using significant figures   
• Apply proper rounding rules to computed quantities

Counting is the only type of measurement that is free from uncertainty, provided the number of objects being counted does not change while the counting process is underway. The result of such a counting measurement is an example of an exact number. By counting the eggs in a carton, one can determine exactlyhow many eggs the carton contains. The numbers of defined quantities are also exact. By definition, 1 foot is exactly 12 inches, 1 inch is exactly 2.54 centimeters, and 1 gram is exactly 0.001 kilogram. Quantities derived from measurements other than counting, however, are uncertain to varying extents due to practical limitations of the measurement process used.



# Significant Figures in Measurement

The numbers of measured quantities, unlike defined or directly counted quantities, are not exact. To measure the volume of liquid in a graduated cylinder, you should make a reading at the bottom of the meniscus, the lowest point on the curved surface of the liquid.

Refer to the illustration in Figure 1.26. The bottom of the meniscus in this case clearly lies between the 21 and 22 markings, meaning the liquid volume is certainlygreater than $2 1 \mathrm { m L }$ but less than $2 2 ~ \mathrm { m L }$ . The meniscus appears to be a bit closer to the $2 2 \mathrm { - m L }$ mark than to the 21-mL mark, and so a reasonable estimate of the liquid’s volume would be $2 1 . 6 \mathrm { m L }$ . In the number 21.6, then, the digits 2 and 1 are certain, but the 6 is an estimate. Some people might estimate the meniscus position to be equally distant from each of the markings and estimate the tenth-place digit as 5, while others may think it to be even closer to the $2 2 \mathrm { - m L }$ mark and estimate this digit to be 7. Note that it would be pointless to attempt to estimate a digit for the hundredths place, given that the tenths-place digit is uncertain. In general, numerical scales such as the one on this graduated cylinder will permit measurements to one-tenth of the smallest scale division. The scale in this case has $1 { \cdot } \mathrm { m L }$ divisions, and so volumes may be measured to the nearest $0 . 1 \mathrm { m L }$ .

This concept holds true for all measurements, even if you do not actively make an estimate. If you place a quarter on a standard electronic balance, you may obtain a reading of $6 . 7 2 { \mathrm { g } }$ . The digits 6 and 7 are certain, and the 2 indicates that the mass of the quarter is likely between 6.71 and 6.73 grams. The quarter weighs about6.72 grams, with a nominal uncertainty in the measurement $\mathbf { 0 } \mathbf { f } \pm 0 . 0 1$ gram. If the coin is weighed on a more sensitive balance, the mass might be $6 . 7 2 3 \ : \mathrm { g }$ . This means its mass lies between 6.722 and 6.724 grams, an uncertainty of 0.001 gram. Every measurement has some uncertainty, which depends on the device used (and the user’s ability). All of the digits in a measurement, including the uncertain last digit, are called significant figures or significant digits. Note that zero may be a measured value; for example, if you stand on a scale that shows weight to the nearest pound and it shows $^ { \ast } 1 2 0$ ,” then the 1 (hundreds), 2 (tens) and 0 (ones) are all significant (measured) values.



A measurement result is properly reported when its significant digits accurately represent the certainty of the measurement process. But what if you were analyzing a reported value and trying to determine what is significant and what is not? Well, for starters, all nonzero digits are significant, and it is only zeros that require some thought. We will use the terms “leading,” “trailing,” and “captive” for the zeros and will consider how to deal with them.

Starting with the first nonzero digit on the left, count this digit and all remaining digits to the right. This is the number of significant figures in the measurement unless the last digit is a trailing zero lying to the left of the decimal point.

Captive zeros result from measurement and are therefore always significant. Leading zeros, however, are never significant—they merely tell us where the decimal point is located.

The leading zeros in this example are not significant. We could use exponential notation (as described in Appendix B) and express the number as $8 . 3 2 4 0 7 \times 1 0 ^ { - 3 }$ ; then the number 8.32407 contains all of the significant figures, and $1 0 ^ { - 3 }$ locates the decimal point.

The number of significant figures is uncertain in a number that ends with a zero to the left of the decimal point location. The zeros in the measurement 1,300 grams could be significant or they could simply indicate where the decimal point is located. The ambiguity can be resolved with the use of exponential notation: $1 . 3 \times 1 0 ^ { 3 }$ (two significant figures), $1 . 3 0 \times 1 0 ^ { 3 }$ (three significant figures, if the tens place was measured), or $1 . 3 0 0 \times 1 0 ^ { 3 }$ (four significant figures, if the ones place was also measured). In cases where only the decimal-formatted number is available, it is prudent to assume that all trailing zeros are not significant.

value makes sense. For example, the official January 2014 census reported the resident population of the US as 317,297,725. Do you think the US population was correctly determined to the reported nine significant figures, that is, to the exact number of people? People are constantly being born, dying, or moving into or out of the country, and assumptions are made to account for the large number of people who are not actually counted. Because of these uncertainties, it might be more reasonable to expect that we know the population to within perhaps a million or so, in which case the population should be reported as $3 . 1 7 \times 1 0 ^ { 8 }$ people.

# Significant Figures in Calculations

A second important principle of uncertainty is that results calculated from a measurement are at least as uncertain as the measurement itself. Take the uncertainty in measurements into account to avoid misrepresenting the uncertainty in calculated results. One way to do this is to report the result of a calculation with the correct number of significant figures, which is determined by the following three rules for rounding numbers:

1. When adding or subtracting numbers, round the result to the same number of decimal places as the number with the least number of decimal places (the least certain value in terms of addition and subtraction).   
2. When multiplying or dividing numbers, round the result to the same number of digits as the number with the least number of significant figures (the least certain value in terms of multiplication and division).   
3. If the digit to be dropped (the one immediately to the right of the digit to be retained) is less than 5, “round down” and leave the retained digit unchanged; if it is more than 5, “round up” and increase the retained digit by 1. If the dropped digit is 5, and it’s either the last digit in the number or it’s followed only by zeros, round up or down, whichever yields an even value for the retained digit. If any nonzero digits follow the dropped 5, round up. (The last part of this rule may strike you as a bit odd, but it’s based on reliable statistics and is aimed at avoiding any bias when dropping the digit “5,” since it is equally close to both possible values of the retained digit.)

The following examples illustrate the application of this rule in rounding a few different numbers to three significant figures:

• 0.028675 rounds “up” to 0.0287 (the dropped digit, 7, is greater than 5) • 18.3384 rounds “down” to 18.3 (the dropped digit, 3, is less than 5) • 6.8752 rounds “up” to 6.88 (the dropped digit is 5, and a nonzero digit follows it) • 92.85 rounds “down” to 92.8 (the dropped digit is 5, and the retained digit is even)

Let’s work through these rules with a few examples.

# EXAMPLE 1.3

# Rounding Numbers

Round the following to the indicated number of significant figures:

(a) 31.57 (to two significant figures) (b) 8.1649 (to three significant figures) (c) 0.051065 (to four significant figures) (d) 0.90275 (to four significant figures)

# Solution

(a) 31.57 rounds “up” to 32 (the dropped digit is 5, and the retained digit is even) (b) 8.1649 rounds “down” to 8.16 (the dropped digit, 4, is less than 5) (c) 0.051065 rounds “down” to 0.05106 (the dropped digit is 5, and the retained digit is even) (d) 0.90275 rounds “up” to 0.9028 (the dropped digit is 5, and the retained digit is even)

# Check Your Learning

Round the following to the indicated number of significant figures:

(a) 0.424 (to two significant figures) (b) 0.0038661 (to three significant figures) (c) 421.25 (to four significant figures) (d) 28,683.5 (to five significant figures)

# Answer:

(a) 0.42; (b) 0.00387; (c) 421.2; (d) 28,684

# EXAMPLE 1.4

# Addition and Subtraction with Significant Figures

Rule: When adding or subtracting numbers, round the result to the same number of decimal places as the number with the fewest decimal places (i.e., the least certain value in terms of addition and subtraction).

(a) Add $\boldsymbol { 1 . 0 0 2 3 \mathrm { g } }$ and $4 . 3 8 3 \ : \mathrm { g }$ .   
(b) Subtract $\mathsf { 4 2 1 . 2 3 9 }$ from $4 8 6 \ \mathrm { g }$ .

# Solution

(a) 1.0023 g + 4.383g 5.3853 g

Answer is $5 . 3 8 5 \mathrm { g }$ (round to the thousandths place; three decimal places)

(b) $\frac { - 4 2 1 . 2 3 \mathrm { ~ g } } { 6 4 . 7 7 \mathrm { ~ g } }$

Answer is $6 5 { \mathrm { g } }$ (round to the ones place; no decimal places)

# Check Your Learning

(a) Add $2 . 3 3 4 \mathrm { m L }$ and $0 . 3 1 \mathrm { m L }$ .   
(b) Subtract 55.8752 m from 56.533 m.

# Answer:

(a) 2.64 mL; (b) $0 . 6 5 8 \mathrm { m }$

# EXAMPLE 1.5

# Multiplication and Division with Significant Figures

Rule: When multiplying or dividing numbers, round the result to the same number of digits as the number with the fewest significant figures (the least certain value in terms of multiplication and division).

(a) Multiply 0.6238 cm by $6 . 6 \mathrm { c m }$ .   
(b) Divide $\mathsf { 4 2 1 . 2 3 9 }$ by $4 8 6 ~ \mathrm { m L }$ .

# Solution

$0 . 6 2 3 8 { \mathrm { ~ c m } } \times 6 . 6 { \mathrm { ~ c m } } = 4 . 1 1 7 0 8 { \mathrm { ~ c m } } ^ { 2 } \longrightarrow$ result is $4 . 1 \mathrm { c m } ^ { 2 }$ (round to two significant figures)   
(a) four significant figures $\times$ two significant figures $\longrightarrow$ two significant figures answer 41230..→sultisg/(oudtoesigiiantfires)   
(b) five significant figures →three significant figures answer three significant figures

# Check Your Learning

(a) Multiply 2.334 cm and $0 . 3 2 0 \mathrm { c m }$ .   
(b) Divide 55.8752 m by 56.53 s.

# Answer:

(a) $0 . 7 4 7 \mathrm { c m } ^ { 2 }$ (b) $0 . 9 8 8 4 \mathrm { m } / \mathrm { s }$

In the midst of all these technicalities, it is important to keep in mind the reason for these rules about significant figures and rounding—to correctly represent the certainty of the values reported and to ensure that a calculated result is not represented as being more certain than the least certain value used in the calculation.

# EXAMPLE 1.6

# Calculation with Significant Figures

One common bathtub is 13.44 dm long, $5 . 9 2 0 \mathrm { d m }$ wide, and 2.54 dm deep. Assume that the tub is rectangular and calculate its approximate volume in liters.

# Solution

${ \begin{array} { l l l } { V } & { = } & { l \times w \times d } \\ & { = } & { 1 3 . 4 4 \mathrm { d m } \times 5 . 9 2 0 \mathrm { d m } \times 2 . 5 4 \mathrm { d m } } \\ & { = } & { 2 0 2 . 0 9 4 5 9 . . . \mathrm { d m } ^ { 3 } { \mathrm { ~ ( v a l u e ~ f r o m ~ c a l c u l a t } } } \\ & { = } & { 2 0 2 \mathrm { d m } ^ { 3 } , { \mathrm { o r ~ } } 2 0 2 \mathrm { L ~ ( a n s w e r ~ r o u n d e d ~ t o ~ } } \end{array} }$ or) 0 three significant figures)

# Check Your Learning

What is the density of a liquid with a mass of 31.1415 g and a volume of $3 0 . 1 3 \mathrm { c m } ^ { 3 } \mathrm { ? }$

Answer: 1.034 g/mL

# EXAMPLE 1.7

# Experimental Determination of Density Using Water Displacement

A piece of rebar is weighed and then submerged in a graduated cylinder partially filled with water, with results as shown.

(a) Use these values to determine the density of this piece of rebar. (b) Rebar is mostly iron. Does your result in (a) support this statement? How?

# Solution

The volume of the piece of rebar is equal to the volume of the water displaced:

$$
\mathrm { ) I u m e } = 2 2 . 4 \ \mathrm { m L } - 1 3 . 5 \ \mathrm { m L } = 8 . 9 \ \mathrm { m L } = 8 . 9 \ \mathrm { c m } ^ { 3 }
$$

(rounded to the nearest $0 . 1 \mathrm { m L }$ , per the rule for addition and subtraction)

The density is the mass-to-volume ratio:

$$
{ \mathrm { d e n s i t y } } = { \frac { \mathrm { m a s s } } { \mathrm { v o l u m e } } } = { \frac { 6 9 . 6 5 8 { \mathrm { g } } } { 8 . 9 { \mathrm { c m } } ^ { 3 } } } = 7 . 8 { \mathrm { g / c m } } ^ { 3 }
$$

(rounded to two significant figures, per the rule for multiplication and division)

From Table 1.4, the density of iron is $7 . 9 \ : \mathrm { g } / \mathrm { c m } ^ { 3 }$ , very close to that of rebar, which lends some support to the fact that rebar is mostly iron.

# Check Your Learning

An irregularly shaped piece of a shiny yellowish material is weighed and then submerged in a graduated cylinder, with results as shown.

(a) Use these values to determine the density of this material.

(b) Do you have any reasonable guesses as to the identity of this material? Explain your reasoning.

# Answer:

(a) $1 9 \mathrm { g } / \mathrm { c m } ^ { 3 }$ ; (b) It is likely gold; the right appearance for gold and very close to the density given for gold in Table 1.4.

# Accuracy and Precision

Scientists typically make repeated measurements of a quantity to ensure the quality of their findings and to evaluate both the precision and the accuracy of their results. Measurements are said to be precise if they yield very similar results when repeated in the same manner. A measurement is considered accurate if it yields a result that is very close to the true or accepted value. Precise values agree with each other; accurate values agree with a true value. These characterizations can be extended to other contexts, such as the results of an archery competition (Figure 1.27).

Suppose a quality control chemist at a pharmaceutical company is tasked with checking the accuracy and precision of three different machines that are meant to dispense 10 ounces $( 2 9 6 ~ \mathrm { m L } )$ of cough syrup into storage bottles. She proceeds to use each machine to fill five bottles and then carefully determines the actual volume dispensed, obtaining the results tabulated in Table 1.5.

Considering these results, she will report that dispenser #1 is precise (values all close to one another, within a few tenths of a milliliter) but not accurate (none of the values are close to the target value of $2 9 6 ~ \mathrm { m L }$ , each being more than $1 0 \mathrm { m L }$ too low). Results for dispenser $\# 2$ represent improved accuracy (each volume is less than $3 \mathrm { m L }$ away from $2 9 6 ~ \mathrm { m L }$ ) but worse precision (volumes vary by more than $4 \mathrm { m L }$ ). Finally, she can report that dispenser $\# 3$ is working well, dispensing cough syrup both accurately (all volumes within $0 . 1 \mathrm { m L }$ of the target volume) and precisely (volumes differing from each other by no more than $0 . 2 \mathrm { m L }$ ).