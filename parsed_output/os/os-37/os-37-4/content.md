# 37.4 I/O Time: Doing The Math  

Now that we have an abstract model of the disk, we can use a little analysis to better understand disk performance. In particular, we can now represent $\mathrm { I } / \mathrm { O }$ time as the sum of three major components:  

$$
T _ { I / O } = T _ { s e e k } + T _ { r o t a t i o n } + T _ { t r a n s f e r }
$$  

Note that the rate of $\operatorname { I } / \operatorname { O } \left( R _ { I / O } \right)$ , which is often more easily used for  

OPERATINGSYSTEMS[VERSION 1.10]  

WWW.OSTEP.ORG  

Figure 37.5: Disk Drive Specs: SCSI Versus SATA   


<html><body><table><tr><td colspan="2">Cheetah 15K.5</td><td>Barracuda</td></tr><tr><td>Capacity</td><td>300 GB</td><td>1 TB</td></tr><tr><td>RPM</td><td>15,000</td><td>7,200</td></tr><tr><td>Average Seek</td><td>4 ms</td><td>9 ms</td></tr><tr><td>Max Transfer</td><td>125 MB/s</td><td>105 MB/s</td></tr><tr><td>Platters</td><td>4</td><td>4</td></tr><tr><td>Cache</td><td>16 MB</td><td>16/32 MB</td></tr><tr><td>Connects via</td><td>SCSI</td><td>SATA</td></tr></table></body></html>  

comparison between drives (as we will do below), is easily computed from the time. Simply divide the size of the transfer by the time it took:  

$$
R _ { I / O } = { \frac { S i z e _ { T r a n s f e r } } { T _ { I / O } } }
$$  

To get a better feel for $\mathrm { I } / \mathrm { O }$ time, let us perform the following calculation. Assume there are two workloads we are interested in. The first, known as the random workload, issues small (e.g., 4KB) reads to random locations on the disk. Random workloads are common in many important applications, including database management systems. The second, known as the sequential workload, simply reads a large number of sectors consecutively from the disk, without jumping around. Sequential access patterns are quite common and thus important as well.  

To understand the difference in performance between random and sequential workloads, we need to make a few assumptions about the disk drive first. Let’s look at a couple of modern disks from Seagate. The first, known as the Cheetah 15K.5 [S09b], is a high-performance SCSI drive. The second, the Barracuda [S09a], is a drive built for capacity. Details on both are found in Figure 37.5.  

As you can see, the drives have quite different characteristics, and in many ways nicely summarize two important components of the disk drive market. The first is the “high performance” drive market, where drives are engineered to spin as fast as possible, deliver low seek times, and transfer data quickly. The second is the “capacity” market, where cost per byte is the most important aspect; thus, the drives are slower but pack as many bits as possible into the space available.  

From these numbers, we can start to calculate how well the drives would do under our two workloads outlined above. Let’s start by looking at the random workload. Assuming each 4 KB read occurs at a random location on disk, we can calculate how long each such read would take. On the Cheetah:  

$$
T _ { s e e k } = 4 m s , T _ { r o t a t i o n } = 2 m s , T _ { t r a n s f e r } = 3 0 m i c r o s e c s
$$  

The average seek time (4 milliseconds) is just taken as the average time reported by the manufacturer; note that a full seek (from one end of the  

# TIP: USE DISKS SEQUENTIALLY  

When at all possible, transfer data to and from disks in a sequential manner. If sequential is not possible, at least think about transferring data in large chunks: the bigger, the better. If $\mathrm { I } / \mathrm { O }$ is done in little random pieces, I/O performance will suffer dramatically. Also, users will suffer. Also, you will suffer, knowing what suffering you have wrought with your careless random I/Os.  

surface to the other) would likely take two or three times longer. The average rotational delay is calculated from the RPM directly. 15000 RPM is equal to 250 RPS (rotations per second); thus, each rotation takes $4 \mathrm { m s }$ . On average, the disk will encounter a half rotation and thus $2 { \mathrm { m s } }$ is the average time. Finally, the transfer time is just the size of the transfer over the peak transfer rate; here it is vanishingly small (30 microseconds; note that we need 1000 microseconds just to get 1 millisecond!).  

Thus, from our equation above, $T _ { I / O }$ for the Cheetah roughly equals $6 \mathrm { m s }$ . To compute the rate of $\mathrm { I } / \mathrm { O } ,$ , we just divide the size of the transfer by the average time, and thus arrive at $R _ { I / O }$ for the Cheetah under the random workload of about $0 . 6 6 \mathrm { M B / s }$ . The same calculation for the Barracuda yields a $T _ { I / O }$ of about $1 3 . 2 \mathrm { m s }$ , more than twice as slow, and thus a rate of about $0 . 3 \mathrm { { 1 } \mathrm { { M B / s } } }$ .  

Now let’s look at the sequential workload. Here we can assume there is a single seek and rotation before a very long transfer. For simplicity, assume the size of the transfer is $1 0 0 \mathrm { M B }$ . Thus, $\mathbf { \bar { \it T } } _ { I / O }$ for the Cheetah and Barracuda is about $8 0 0 ~ \mathrm { { m s } }$ and $9 5 0 ~ \mathrm { m s }$ , respectively. The rates of I/O are thus very nearly the peak transfer rates of $1 2 5 \mathrm { \ : M B / s }$ and $1 0 5 \mathrm { M B / s }$ , respectively. Figure 37.6 summarizes these numbers.  

![](images/806fb73a92957e0515fa833afe9fa47c4af37091c5177fa3a9f21402bd5bb4a9.jpg)  
Figure 37.6: Disk Drive Performance: SCSI Versus SATA  

The figure shows us a number of important things. First, and most importantly, there is a huge gap in drive performance between random and sequential workloads, almost a factor of 200 or so for the Cheetah and more than a factor 300 difference for the Barracuda. And thus we arrive at the most obvious design tip in the history of computing.  

A second, more subtle point: there is a large difference in performance between high-end “performance” drives and low-end “capacity” drives. For this reason (and others), people are often willing to pay top dollar for the former while trying to get the latter as cheaply as possible.  

OPERATINGSYSTEMS[VERSION 1.10]  

ASIDE: COMPUTING THE “AVERAGE” SEEK  

In many books and papers, you will see average disk-seek time cited as being roughly one-third of the full seek time. Where does this come from?  

Turns out it arises from a simple calculation based on average seek distance, not time. Imagine the disk as a set of tracks, from 0 to $N$ . The seek distance between any two tracks $x$ and $y$ is thus computed as the absolute value of the difference between them: $\left| x - y \right|$ .  

To compute the average seek distance, all you need to do is to first add up all possible seek distances:  

$$
\sum _ { x = 0 } ^ { N } \sum _ { y = 0 } ^ { N } | x - y | .
$$  

Then, divide this by the number of different possible seeks: $N ^ { 2 }$ . To compute the sum, we’ll just use the integral form:  

$$
\int _ { x = 0 } ^ { N } \int _ { y = 0 } ^ { N } | x - y | { \mathrm { d } } y { \mathrm { d } } x .
$$  

To compute the inner integral, let’s break out the absolute value:  

$$
\int _ { y = 0 } ^ { x } ( x - y ) \mathrm { d } y + \int _ { y = x } ^ { N } ( y - x ) \mathrm { d } y .
$$  

Solving this leads to $\begin{array} { r } { \left( x y - \frac { 1 } { 2 } y ^ { 2 } \right) \Big | _ { 0 } ^ { x } + \left( \frac { 1 } { 2 } y ^ { 2 } - x y \right) \Big | _ { x } ^ { N } } \end{array}$ which can be simplified to $\begin{array} { r } { ( x ^ { 2 } - N x + \frac { 1 } { 2 } N ^ { 2 } ) } \end{array}$ . Now we have to compute the outer integral:  

$$
\int _ { x = 0 } ^ { N } ( { x ^ { 2 } } - N x + { \frac { 1 } { 2 } } N ^ { 2 } ) \mathrm { d } x ,
$$  

which results in:  

$$
( \frac { 1 } { 3 } x ^ { 3 } - \frac { N } { 2 } x ^ { 2 } + \frac { N ^ { 2 } } { 2 } x ) \bigg | _ { 0 } ^ { N } = \frac { N ^ { 3 } } { 3 } .
$$  

Remember that we still have to divide by the total number of seeks $( N ^ { 2 } )$ to compute the average seek distance: $\scriptstyle \left( { \frac { N ^ { 3 } } { 3 } } \right) / ( N ^ { 2 } ) \ = \ { \frac { 1 } { 3 } } N$ . Thus the average seek distance on a disk, over all possible seeks, is one-third the full distance. And now when you hear that an average seek is one-third of a full seek, you’ll know where it came from.  

![](images/78d1ab85d8252a57bcf919f13eaa11e2e47f8f6ccf8e7d916178a06965d80e76.jpg)  
Figure 37.7: SSTF: Scheduling Requests 21 And 2  

