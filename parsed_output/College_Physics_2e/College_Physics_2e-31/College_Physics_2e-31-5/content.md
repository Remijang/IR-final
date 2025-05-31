# 31.5 Half-Life and Activity

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

Define half-life.   
• Define dating.   
• Calculate age of old objects by radioactive dating.

Unstable nuclei decay. However, some nuclides decay faster than others. For example, radium and polonium, discovered by the Curies, decay faster than uranium. This means they have shorter lifetimes, producing a greater rate of decay. In this section we explore half-life and activity, the quantitative terms for lifetime and rate of decay.

# Half-Life

Why use a term like half-life rather than lifetime? The answer can be found by examining Figure 31.19, which shows how the number of radioactive nuclei in a sample decreases with time. The timeinwhichhalfoftheoriginalnumber ofnucleidecayis defined as the half-life, $t _ { 1 / 2 }$ . Half of the remaining nuclei decay in the next half-life. Further, half of that amount decays in the following half-life. Therefore, the number of radioactive nuclei decreases from $N$ to $N / 2$ in one half-life, then to $N / 4$ in the next, and to $N / 8$ in the next, and so on. If $N$ is a large number, then manyhalflives (not just two) pass before all of the nuclei decay. Nuclear decay is an example of a purely statistical process. A more precise definition of half-life is that eachnucleushasa $50 \%$ chanceoflivingforatimeequaltoonehalf-life $t _ { 1 / 2 }$ . Thus, if $N$ is reasonably large, half of the original nuclei decay in a time of one half-life. If an individual nucleus makes it through that time, it still has a $5 0 \%$ chance of surviving through another half-life. Even if it happens to make it through hundreds of half-lives, it still has a $50 \%$ chance of surviving through one more. The probability of decay is the same no matter when you start counting. This is like random coin flipping. The chance of heads is $5 0 \%$ , no matter what has happened before.

There is a tremendous range in the half-lives of various nuclides, from as short as $1 0 ^ { - 2 3 }$ s for the most unstable, to more than $1 0 ^ { 1 6 }$ y for the least unstable, or about 46 orders of magnitude. Nuclides with the shortest half-lives are those for which the nuclear forces are least attractive, an indication of the extent to which the nuclear force can depend on the particular combination of neutrons and protons. The concept of half-life is applicable to other subatomic particles, as will be discussed in Particle Physics. It is also applicable to the decay of excited states in atoms and nuclei. The following equation gives the quantitative relationship between the original number of nuclei present at time zero $( N _ { 0 } )$ and the number $( N )$ at a later time $t$ :

$$
N = N _ { 0 } e ^ { - \lambda t } ,
$$

where $e = 2 . 7 1 8 2 8 . . .$ is the base of the natural logarithm, and $\lambda$ is the decay constant for the nuclide. The shorter the half-life, the larger is the value of $\lambda$ , and the faster the exponential $e ^ { - \lambda t }$ decreases with time. The relationship between the decay constant $\lambda$ and the half-life $t _ { 1 / 2 }$ is

$$
\lambda = \frac { \ln ( 2 ) } { t _ { 1 / 2 } } \approx \frac { 0 . 6 9 3 } { t _ { 1 / 2 } } .
$$

To see how the number of nuclei declines to half its original value in one half-life, let $t = t _ { 1 / 2 }$ in the exponential in the equation $N = N _ { 0 } e ^ { - \lambda t }$ . This gives $N = N _ { 0 } e ^ { - \lambda t } = N _ { 0 } e ^ { - 0 . 6 9 3 } = 0 . 5 0 0 N _ { 0 }$ . For integral numbers of half-lives, you can just divide the original number by 2 over and over again, rather than using the exponential relationship. For example, if ten half-lives have passed, we divide $N$ by 2 ten times. This reduces it to . For an arbitrary time, not just a multiple of the half-life, the exponential relationship must be used.

Radioactive dating is a clever use of naturally occurring radioactivity. Its most famous application is carbon-14 dating. Carbon-14 has a half-life of 5730 years and is produced in a nuclear reaction induced when solar neutrinos strike $^ { 1 4 } \mathrm { N }$ in the atmosphere. Radioactive carbon has the same chemistry as stable carbon, and so it mixes into the ecosphere, where it is consumed and becomes part of every living organism. Carbon-14 has an abundance of 1.3 parts per trillion of normal carbon. Thus, if you know the number of carbon nuclei in an object (perhaps determined by mass and Avogadro’s number), you multiply that number by $1 . 3 \times 1 0 ^ { - 1 2 }$ to find the number of $^ { 1 4 } \mathrm { C }$ nuclei in the object. When an organism dies, carbon exchange with the environment ceases, and $^ { 1 4 } \mathrm { C }$ is not replenished as it decays. By comparing the abundance of $^ { 1 4 } \mathrm { C }$ in an artifact, such as mummy wrappings, with the normal abundance in living tissue, it is possible to determine the artifact’s age (or time since death). Carbon-14 dating can be used for biological tissues as old as 50 or 60 thousand years, but is most accurate for younger samples, since the abundance of $^ { 1 4 } \mathrm { C }$ nuclei in them is greater. Very old biological materials contain no $^ { 1 4 } \mathrm { C }$ at all. There are instances in which the date of an artifact can be determined by other means, such as historical knowledge or tree-ring counting. These cross-references have confirmed the validity of carbon-14 dating and permitted us to calibrate the technique as well. Carbon-14 dating revolutionized parts of archaeology and is of such importance that it earned the 1960 Nobel Prize in chemistry for its developer, the American chemist Willard Libby (1908–1980).

One of the most famous cases of carbon-14 dating involves the Shroud of Turin, a long piece of fabric purported to be the burial shroud of Jesus (see Figure 31.20). This relic was first displayed in Turin in 1354 and was denounced as a fraud at that time by a French bishop. Its remarkable negative imprint of an apparently crucified body resembles the then-accepted image of Jesus, and so the shroud was never disregarded completely and remained controversial over the centuries. Carbon-14 dating was not performed on the shroud until 1988, when the process had been refined to the point where only a small amount of material needed to be destroyed. Samples were tested at three independent laboratories, each being given four pieces of cloth, with only one unidentified piece from the shroud, to avoid prejudice. All three laboratories found samples of the shroud contain $9 2 \%$ of the $^ { 1 4 } \mathrm { C }$ found in living tissues, allowing the shroud to be dated (see Example 31.4).

# EXAMPLE 31.4

# How Old Is the Shroud of Turin?

Calculate the age of the Shroud of Turin given that the amount of $^ { 1 4 } \mathrm { C }$ found in it is $9 2 \%$ of that in living tissue.

# Strategy

Knowing that $9 2 \%$ of the $^ { 1 4 } \mathrm { C }$ remains means that $N / N _ { 0 } = 0 . 9 2$ . Therefore, the equation $N = N _ { 0 } e ^ { - \lambda t }$ can be used to find . We also know that the half-life of $^ { 1 4 } \mathrm { C }$ is ${ 5 7 3 0 \mathrm { y } } ,$ and so once is known, we can use the equation $\begin{array} { r } { \lambda = \frac { 0 . 6 9 3 } { t _ { 1 / 2 } } } \end{array}$ to find $\lambda$ and then find $t$ as requested. Here, we postulate that the decrease in $^ { 1 4 } \mathrm { C }$ is solely due to nuclear decay.

# Solution

Solving the equation $N = N _ { 0 } e ^ { - \lambda t }$ for $N / N _ { 0 }$ gives

$$
\frac { N } { N _ { 0 } } = e ^ { - \lambda t } .
$$

Thus,

$$
0 . 9 2 = e ^ { - \lambda t } .
$$

Taking the natural logarithm of both sides of the equation yields

$$
\ln { 0 . 9 2 } = - \lambda t
$$

so that

$$
- 0 . 0 8 3 4 = - \lambda t .
$$

Rearranging to isolate $t$ gives

$$
t = { \frac { 0 . 0 8 3 4 } { \lambda } } .
$$

Now, the equation can be used to find $\lambda$ for $^ { 1 4 } \mathrm { C }$ . Solving for $\lambda$ and substituting the known half-life gives

$$
\lambda = { \frac { 0 . 6 9 3 } { t _ { 1 / 2 } } } = { \frac { 0 . 6 9 3 } { 5 7 3 0 \mathrm { y } } } .
$$

We enter this value into the previous equation to find $t$ :

$$
t = { \frac { 0 . 0 8 3 4 } { \frac { 0 . 6 9 3 } { 5 7 3 0 { \mathrm { ~ y } } } } } = 6 9 0 { \mathrm { ~ y } } .
$$

# Discussion

This dates the material in the shroud to $1 9 8 8 - 6 9 0 = \mathsf { a . d }$ . 1300. Our calculation is only accurate to two digits, so that the year is rounded to 1300. The values obtained at the three independent laboratories gave a weighted average date of a.d. $1 3 2 0 \pm 6 0$ . The uncertainty is typical of carbon-14 dating and is due to the small amount of $^ { 1 4 } \mathrm { C }$ in living tissues, the amount of material available, and experimental uncertainties (reduced by having three independent measurements). It is meaningful that the date of the shroud is consistent with the first record of its existence and inconsistent with the period in which Jesus lived.

There are other forms of radioactive dating. Rocks, for example, can sometimes be dated based on the decay of $^ { 2 3 8 } \mathrm { U }$ . The decay series for $^ { 2 3 8 } \mathrm { U }$ ends with $^ { 2 0 6 } \mathrm { { P b } }$ , so that the ratio of these nuclides in a rock is an indication of how long it has been since the rock solidified. The original composition of the rock, such as the absence of lead, must be known with some confidence. However, as with carbon-14 dating, the technique can be verified by a consistent body of knowledge. Since $^ { 2 3 8 } \mathrm { U }$ has a half-life of $4 . 5 \times 1 0 ^ { 9 } \ : \mathrm { y } ,$ it is useful for dating only very old materials, showing, for example, that the oldest rocks on Earth solidified about $3 . 5 \times 1 0 ^ { 9 }$ years ago.

# Activity, the Rate of Decay

What do we mean when we say a source is highly radioactive? Generally, this means the number of decays per unit time is very high. We define activity $R$ to be the rate of decay expressed in decays per unit time. In equation form, this is

$$
R = { \frac { \Delta N } { \Delta t } }
$$

where $\Delta N$ is the number of decays that occur in time $\Delta t$ . The SI unit for activity is one decay per second and is given the name becquerel (Bq) in honor of the discoverer of radioactivity. That is,

$$
1 \mathrm { B q } = 1 \mathrm { d e c a y } / \mathrm { s } .
$$

Activity $R$ is often expressed in other units, such as decays per minute or decays per year. One of the most common units for activity is the curie (Ci), defined to be the activity of $\mathtt { 1 } \mathtt { g }$ of $^ { 2 2 6 } \mathrm { { R a } }$ , in honor of Marie Curie’s work with radium. The definition of curie is

$$
1 { \mathrm { C i } } = 3 . 7 0 \times 1 0 ^ { 1 0 } { \mathrm { B q } } ,
$$

or $3 . 7 0 \times 1 0 ^ { 1 0 }$ decays per second. A curie is a large unit of activity, while a becquerel is a relatively small unit. $1 \mathrm { M B q } = 1 0 0$ microcuries $( \mu \mathrm { C i } )$ . In countries like Australia and New Zealand that adhere more to SI units, most radioactive sources, such as those used in medical diagnostics or in physics laboratories, are labeled in Bq or megabecquerel (MBq).

Intuitively, you would expect the activity of a source to depend on two things: the amount of the radioactive substance present, and its half-life. The greater the number of radioactive nuclei present in the sample, the more will decay per unit of time. The shorter the half-life, the more decays per unit time, for a given number of nuclei. So activity $R$ should be proportional to the number of radioactive nuclei, $N$ , and inversely proportional to their half-life, $t _ { 1 / 2 }$ . In fact, your intuition is correct. It can be shown that the activity of a source is

$$
R = \frac { 0 . 6 9 3 N } { t _ { 1 / 2 } }
$$

where $N$ is the number of radioactive nuclei present, having half-life $t _ { 1 / 2 }$ . This relationship is useful in a variety of calculations, as the next two examples illustrate.

# EXAMPLE 31.5

# How Great Is the $^ { 1 4 } \mathrm { C }$ Activity in Living Tissue?

Calculate the activity due to $^ { 1 4 } \mathrm { C }$ in $1 . 0 0 \mathsf { k g }$ of carbon found in a living organism. Express the activity in units of Bq and Ci.

# Strategy

To find the activity $R$ using the equation $\begin{array} { r } { R = \frac { 0 . 6 9 3 N } { t _ { 1 / 2 } } } \end{array}$ , we must know $N$ and $t _ { 1 / 2 }$ . The half-life of $^ { 1 4 } \mathrm { C }$ can be found in Appendix B, and was stated above as 5730 y. To find $N$ , we first find the number of $^ { 1 2 } \mathrm { C }$ nuclei in $\displaystyle 1 . 0 0 { \mathsf { k g } }$ of carbon using the concept of a mole. As indicated, we then multiply by $1 . 3 \times 1 0 ^ { - 1 2 }$ (the abundance of $^ { 1 4 } \mathrm { C }$ in a carbon sample from a living organism) to get the number of $^ { 1 4 } \mathrm { C }$ nuclei in a living organism.

# Solution

One mole of carbon has a mass of $\mathtt { 1 2 . 0 ~ \AA }$ , since it is nearly pure $^ { 1 2 } \mathrm { C }$ . (A mole has a mass in grams equal in magnitude to $A$ found in the periodic table.) Thus the number of carbon nuclei in a kilogram is

$$
N ( ^ { 1 2 } \mathbf { C } ) = { \frac { 6 . 0 2 \times 1 0 ^ { 2 3 } ~ { \mathrm { m o l } } ^ { - 1 } } { 1 2 . 0 ~ { \mathrm { g / m o l } } } } \times ( 1 0 0 0 ~ \mathrm { g } ) = 5 . 0 2 \times 1 0 ^ { 2 5 } .
$$

So the number of $^ { 1 4 } \mathrm { C }$ nuclei in $1 \kappa \theta$ of carbon is

$$
N ( ^ { 1 4 } \mathbf { C } ) { = } ( 5 . 0 2 \times 1 0 ^ { 2 5 } ) ( 1 . 3 \times 1 0 ^ { - 1 2 } ) { = } 6 . 5 2 \times 1 0 ^ { 1 3 } .
$$

Now the activity $R$ is found using the equation $\begin{array} { r } { R = \frac { 0 . 6 9 3 N } { t _ { 1 / 2 } } } \end{array}$

Entering known values gives

$$
R = { \frac { 0 . 6 9 3 ( 6 . 5 2 \times 1 0 ^ { 1 3 } ) } { 5 7 3 0 \mathrm { y } } } = 7 . 8 9 { \times } 1 0 ^ { 9 } \mathrm { y } ^ { - 1 } ,
$$

or $7 . 8 9 \times 1 0 ^ { 9 }$ decays per year. To convert this to the unit Bq, we simply convert years to seconds. Thus,

$$
R = ( 7 . 8 9 \times 1 0 ^ { 9 } ~ \mathrm { y } ^ { - 1 } ) \frac { 1 . 0 0 ~ \mathrm { y } } { 3 . 1 6 \times 1 0 ^ { 7 } ~ \mathrm { s } } = 2 5 0 ~ \mathrm { B q } ,
$$

or 250 decays per second. To express $R$ in curies, we use the definition of a curie,

$$
R = { \frac { 2 5 0 ~ { \mathrm { B q } } } { 3 . 7 \times 1 0 ^ { 1 0 } ~ { \mathrm { B q / C i } } } } = 6 . 7 6 { \times } 1 0 ^ { - 9 } ~ { \mathrm { C i } } .
$$

Thus,

$$
R = 6 . 7 6 \mathrm { \ n C i } .
$$

# Discussion

Our own bodies contain kilograms of carbon, and it is intriguing to think there are hundreds of $^ { 1 4 } \mathrm { C }$ decays per second taking place in us. Carbon-14 and other naturally occurring radioactive substances in our bodies contribute to the background radiation we receive. The small number of decays per second found for a kilogram of carbon in this example gives you some idea of how difficult it is to detect $^ { 1 4 } \mathrm { C }$ in a small sample of material. If there are 250 decays per second in a kilogram, then there are 0.25 decays per second in a gram of carbon in living tissue. To observe this, you must be able to distinguish decays from other forms of radiation, in order to reduce background noise. This becomes more difficult with an old tissue sample, since it contains less $^ { 1 4 } \mathrm { C }$ , and for samples more than

50 thousand years old, it is impossible.

Human-made (or artificial) radioactivity has been produced for decades and has many uses. Some of these include medical therapy for cancer, medical imaging and diagnostics, and food preservation by irradiation. Many applications as well as the biological effects of radiation are explored in Medical Applications of Nuclear Physics, but it is clear that radiation is hazardous. A number of tragic examples of this exist, one of the most disastrous being the meltdown and fire at the Chernobyl reactor complex in the Ukraine (see Figure $3 1 . 2 1 \mathrm { \AA }$ ). Several radioactive isotopes were released in huge quantities, contaminating many thousands of square kilometers and directly affecting hundreds of thousands of people. The most significant releases were of , $^ { 9 0 } \mathrm { S r } ,$ , $^ { 1 3 7 } \mathrm { C s }$ , $^ { 2 3 9 } \mathrm { P u }$ , $^ { 2 3 8 } \mathrm { U } _ { ; }$ , and $^ { 2 3 5 } \mathrm { U }$ . Estimates are that the total amount of radiation released was about 100 million curies.

# Human and Medical Applications

# EXAMPLE 31.6

# What Mass of $^ { 1 3 7 } \mathrm { C s }$ Escaped Chernobyl?

It is estimated that the Chernobyl disaster released 6.0 MCi of $^ { 1 3 7 } \mathrm { C s }$ into the environment. Calculate the mass of released.

# Strategy

We can calculate the mass released using Avogadro’s number and the concept of a mole if we can first find the number of nuclei $N$ released. Since the activity $R$ is given, and the half-life of $^ { 1 3 7 } \mathrm { C s }$ is found in Appendix B to be 30.2 y, we can use the equation $\begin{array} { r } { R = \frac { 0 . 6 9 3 N } { t _ { 1 / 2 } } } \end{array}$ to find $N$ .

# Solution

Solving the equation $\begin{array} { r } { R = \frac { 0 . 6 9 3 N } { t _ { 1 / 2 } } } \end{array}$ for gives

$$
N = \frac { R t _ { 1 / 2 } } { 0 . 6 9 3 } .
$$

Entering the given values yields

$$
N = \frac { ( 6 . 0 \mathrm { M C i } ) ( 3 0 . 2 \mathrm { y } ) } { 0 . 6 9 3 } .
$$

Converting curies to becquerels and years to seconds, we get

$$
{ \begin{array} { r c l } { N } & { = } & { { \frac { ( 6 . 0 \times 1 0 ^ { 6 } { \mathrm { ~ C i } } ) ( 3 . 7 \times 1 0 ^ { 1 0 } { \mathrm { ~ B q } } / { \mathrm { C i } } ) ( 3 0 . 2 { \mathrm { ~ y } } ) ( 3 . 1 6 \times 1 0 ^ { 7 } { \mathrm { ~ s } } / { \mathrm { y } } ) } { 0 . 6 9 3 } } } \\ & { = } & { 3 . 1 \times 1 0 ^ { 2 6 } . } \end{array} }
$$

One mole of a nuclide $^ A X$ has a mass of $A$ grams, so that one mole of $^ { 1 3 7 } \mathrm { C s }$ has a mass of 137 g. A mole has $6 . 0 2 \times 1 0 ^ { 2 3 }$ nuclei. Thus the mass of $^ { 1 3 7 } \mathrm { C s }$ released was

$$
{ \begin{array} { l l l } { m } & { = } & { { \Bigl ( } { \frac { 1 3 7 \ \mathrm { g } } { 6 . 0 2 \times 1 0 ^ { 2 3 } } } { \Bigr ) } ( 3 . 1 \times 1 0 ^ { 2 6 } ) = 7 0 \times 1 0 ^ { 3 } \ \mathrm { g } } \\ & { = } & { 7 0 \ \mathrm { k g } . } \end{array} }
$$

# Discussion

While $7 0 ~ \mathsf { k g }$ of material may not be a very large mass compared to the amount of fuel in a power plant, it is extremely radioactive, since it only has a 30-year half-life. Six megacuries (6.0 MCi) is an extraordinary amount of activity but is only a fraction of what is produced in nuclear reactors. Similar amounts of the other isotopes were also released at Chernobyl. Although the chances of such a disaster may have seemed small, the consequences were extremely severe, requiring greater caution than was used. More will be said about safe reactor design in the next chapter, but it should be noted that more recent reactors have a fundamentally safer design.

Activity $R$ decreases in time, going to half its original value in one half-life, then to one-fourth its original value in the next half-life, and so on. Since $\begin{array} { r } { R = \frac { 0 . 6 9 3 N } { t _ { 1 / 2 } } } \end{array}$ , the activity decreases as the number of radioactive nuclei decreases. The equation for as a function of time is found by combining the equations and , yielding

$$
R = R _ { 0 } e ^ { - \lambda t } ,
$$

where $R _ { 0 }$ is the activity at $t = 0$ . This equation shows exponential decay of radioactive nuclei. For example, if a source originally has a $\pm . 0 0 - \mathsf { m C i }$ activity, it declines to $0 . 5 0 0 \mathsf { m } \mathsf { C i }$ in one half-life, to $0 . 2 5 0 \mathsf { m C i }$ in two half-lives, to $0 . 1 2 5 { \mathsf { m C i } }$ in three half-lives, and so on. For times other than whole half-lives, the equation $R = R _ { 0 } e ^ { - \lambda t }$ must be used to find $R$ .

# PHET EXPLORATIONS

# Alpha Decay

Watch alpha particles escape from a polonium nucleus, causing radioactive alpha decay. See how random decay times relate to the half life.

Click to view content (https://openstax.org/l/02alphadecay).