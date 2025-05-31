# 43.3 How Much To Buffer?  

This raises the following question: how many updates should LFS buffer before writing to disk? The answer, of course, depends on the disk itself, specifically how high the positioning overhead is in comparison to the transfer rate; see the FFS chapter for a similar analysis.  

For example, assume that positioning (i.e., rotation and seek overheads) before each write takes roughly ${ T _ { p o s i t i o n } } ^ { - }$ seconds. Assume further that the disk transfer rate is $R _ { p e a k }$ MB/s. How much should LFS buffer before writing when running on such a disk?  

The way to think about this is that every time you write, you pay a fixed overhead of the positioning cost. Thus, how much do you have to write in order to amortize that cost? The more you write, the better (obviously), and the closer you get to achieving peak bandwidth.  

To obtain a concrete answer, let’s assume we are writing out $D \ \mathrm { M B }$ . eptlouswtrhite tiomute thoitsrcahnsufnekr $( T _ { w r i t e } )$ is the positioning time $T _ { p o s i t i o n }$ $\begin{array} { r } { D \left( \frac { D } { R _ { p e a k } } \right) } \end{array}$  

$$
T _ { w r i t e } = T _ { p o s i t i o n } + \frac { D } { R _ { p e a k } }
$$  

And thus the effective rate of writing $( R _ { e f f e c t i v e } ) _ { , }$ , which is just the amount of data written divided by the total time to write it, is:  

$$
R _ { e f f e c t i v e } = \frac { \overline { { D } } ^ { \prime } } { T _ { w r i t e } } = \frac { D } { T _ { p o s i t i o n } + \frac { D } { R _ { p e a k } } } .
$$  

What we’re interested in is getting the effective rate $( R _ { e f f e c t i v e } )$ close to the peak rate. Specifically, we want the effective rate to be some fraction $F$ of the peak rate, where $\dot { 0 } < F < 1$ (a typical $F$ might be 0.9, or $9 0 \%$ of the peak rate). In mathematical form, this means we want $\begin{array} { r } { R _ { e f f e c t i v e } = } \end{array}$ F × Rpeak.  

OPERATINGSYSTEMS[VERSION 1.10]  

At this point, we can solve for $D$ :  

$$
\begin{array} { r } { R _ { e f f e c t i v e } = \frac { D } { T _ { p o s i t i o n } + \frac { D } { R _ { p e a k } } } = F \times R _ { p e a k } } \\ { D = F \times R _ { p e a k } \times ( T _ { p o s i t i o n } + \frac { D } { R _ { p e a k } } ) } \end{array}
$$  

$$
\begin{array} { c } { D = ( F \times R _ { p e a k } \times T _ { p o s i t i o n } ) + ( F \times R _ { p e a k } \times \displaystyle \frac { D } { R _ { p e a k } } ) } \\ { D = \displaystyle \frac { F } { 1 - F } \times R _ { p e a k } \times T _ { p o s i t i o n } } \end{array}
$$  

Let’s do an example, with a disk with a positioning time of $1 0 \ \mathrm { m i l } .$ - liseconds and peak transfer rate of $1 0 0 ~ \mathrm { M B } \dot { / } \mathrm { s }$ ; assume we want an effective bandwidth of $9 0 \%$ of peak $F = 0 . 9$ ). In this case, $\begin{array} { r } { D \ = \ \frac { 0 . 9 } { 0 . 1 } \ \times } \end{array}$ $1 0 0 ~ M B / s \times 0 . 0 1$ seconds = 9 MB. Try some different values to see how much we need to buffer in order to approach peak bandwidth. How much is needed to reach $9 5 \%$ of peak? $9 9 \% ?$  

