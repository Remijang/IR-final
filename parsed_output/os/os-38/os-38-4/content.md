# 38.4 RAID Level 0: Striping  

The first RAID level is actually not a RAID level at all, in that there is no redundancy. However, RAID level 0, or striping as it is better known, serves as an excellent upper-bound on performance and capacity and thus is worth understanding.  

The simplest form of striping will stripe blocks across the disks of the system as follows (assume here a 4-disk array):  

![](images/458f3fb89cba602eef35e1eb7a1de938b4bb61f9f08e43c53732fb317b565c10.jpg)  
Figure 38.1: RAID-0: Simple Striping  

From Figure 38.1, you get the basic idea: spread the blocks of the array across the disks in a round-robin fashion. This approach is designed to extract the most parallelism from the array when requests are made for contiguous chunks of the array (as in a large, sequential read, for example). We call the blocks in the same row a stripe; thus, blocks 0, 1, 2, and 3 are in the same stripe above.  

In the example, we have made the simplifying assumption that only 1 block (each of say size 4KB) is placed on each disk before moving on to the next. However, this arrangement need not be the case. For example, we could arrange the blocks across disks as in Figure 38.2:  

![](images/bc29e34e95cc2633565449d18171189bef16efe43da36838a6d165650026d283.jpg)  
Figure 38.2: Striping With A Bigger Chunk Size  

In this example, we place two 4KB blocks on each disk before moving on to the next disk. Thus, the chunk size of this RAID array is 8KB, and a stripe thus consists of 4 chunks or 32KB of data.  

OPERATINGSYSTEMS[VERSION 1.10]  

# ASIDE: THE RAID MAPPING PROBLEM  

Before studying the capacity, reliability, and performance characteristics of the RAID, we first present an aside on what we call the mapping problem. This problem arises in all RAID arrays; simply put, given a logical block to read or write, how does the RAID know exactly which physical disk and offset to access?  

For these simple RAID levels, we do not need much sophistication in order to correctly map logical blocks onto their physical locations. Take the first striping example above (chunk size $= 1$ block $\mathbf { \sigma } = \mathbf { \sigma }$ 4KB). In this case, given a logical block address A, the RAID can easily compute the desired disk and offset with two simple equations:  

Note that these are all integer operations (e.g., $4 / 3 = 1$ not 1.33333...).  

Let’s see how these equations work for a simple example. Imagine in the first RAID above that a request arrives for block 14. Given that there are 4 disks, this would mean that the disk we are interested in is $( 1 4 \ \% \ 4 = 2 )$ ): disk 2. The exact block is calculated as $( 1 4 ~ / ~ 4 = 3 )$ ): block 3. Thus, block 14 should be found on the fourth block (block 3, starting at 0) of the third disk (disk 2, starting at 0), which is exactly where it is.  

You can think about how these equations would be modified to support different chunk sizes. Try it! It’s not too hard.  

# Chunk Sizes  

Chunk size mostly affects performance of the array. For example, a small chunk size implies that many files will get striped across many disks, thus increasing the parallelism of reads and writes to a single file; however, the positioning time to access blocks across multiple disks increases, because the positioning time for the entire request is determined by the maximum of the positioning times of the requests across all drives.  

A big chunk size, on the other hand, reduces such intra-file parallelism, and thus relies on multiple concurrent requests to achieve high throughput. However, large chunk sizes reduce positioning time; if, for example, a single file fits within a chunk and thus is placed on a single disk, the positioning time incurred while accessing it will just be the positioning time of a single disk.  

Thus, determining the “best” chunk size is hard to do, as it requires a great deal of knowledge about the workload presented to the disk system [CL95]. For the rest of this discussion, we will assume that the array uses a chunk size of a single block (4KB). Most arrays use larger chunk sizes (e.g., 64 KB), but for the issues we discuss below, the exact chunk size does not matter; thus we use a single block for the sake of simplicity.  

# Back To RAID-0 Analysis  

Let us now evaluate the capacity, reliability, and performance of striping. From the perspective of capacity, it is perfect: given $N$ disks each of size $B$ blocks, striping delivers $N \cdot B$ blocks of useful capacity. From the standpoint of reliability, striping is also perfect, but in the bad way: any disk failure will lead to data loss. Finally, performance is excellent: all disks are utilized, often in parallel, to service user $\mathrm { I } / \mathrm { O }$ requests.  

# Evaluating RAID Performance  

In analyzing RAID performance, one can consider two different performance metrics. The first is single-request latency. Understanding the latency of a single I/O request to a RAID is useful as it reveals how much parallelism can exist during a single logical I/O operation. The second is steady-state throughput of the RAID, i.e., the total bandwidth of many concurrent requests. Because RAIDs are often used in high-performance environments, the steady-state bandwidth is critical, and thus will be the main focus of our analyses.  

To understand throughput in more detail, we need to put forth some workloads of interest. We will assume, for this discussion, that there are two types of workloads: sequential and random. With a sequential workload, we assume that requests to the array come in large contiguous chunks; for example, a request (or series of requests) that accesses 1 MB of data, starting at block $x$ and ending at block $\mathbf { \Gamma } ( { \boldsymbol { x } } + 1 \mathbf { M } \mathbf { B } )$ , would be deemed sequential. Sequential workloads are common in many environments (think of searching through a large file for a keyword), and thus are considered important.  

For random workloads, we assume that each request is rather small, and that each request is to a different random location on disk. For example, a random stream of requests may first access 4KB at logical address 10, then at logical address 550,000, then at 20,100, and so forth. Some important workloads, such as transactional workloads on a database management system (DBMS), exhibit this type of access pattern, and thus it is considered an important workload.  

Of course, real workloads are not so simple, and often have a mix of sequential and random-seeming components as well as behaviors inbetween the two. For simplicity, we just consider these two possibilities.  

As you can tell, sequential and random workloads will result in widely different performance characteristics from a disk. With sequential access, a disk operates in its most efficient mode, spending little time seeking and waiting for rotation and most of its time transferring data. With random access, just the opposite is true: most time is spent seeking and waiting for rotation and relatively little time is spent transferring data. To capture this difference in our analysis, we will assume that a disk can transfer data at $S$ MB/s under a sequential workload, and $R$ MB/s when under a random workload. In general, $S$ is much greater than $R$ (i.e., $S \gg R$ ).  

OPERATINGSYSTEMS[VERSION 1.10]  

To make sure we understand this difference, let’s do a simple exercise. Specifically, let’s calculate $S$ and $R$ given the following disk characteristics. Assume a sequential transfer of size $1 0 \mathrm { M B }$ on average, and a random transfer of $1 0 \mathrm { K B }$ on average. Also, assume the following disk characteristics:  

Average seek time 7 ms Average rotational delay 3 ms  

Transfer rate of disk 50 MB/s  

To compute $S _ { \nu }$ , we need to first figure out how time is spent in a typical $1 0 ~ \mathrm { M B }$ transfer. First, we spend $7 ~ \mathrm { m s }$ seeking, and then $3 ~ \mathrm { m s }$ rotating. Finally, transfer begins; $1 0 \dot { \mathrm { M B } } \ @ 5 0 \mathrm { M B } / { s }$ leads to 1/5th of a second, or $2 0 0 \mathrm { m s }$ , spent in transfer. Thus, for each $1 0 \mathrm { M B }$ request, we spend $2 1 0 \mathrm { m s }$ completing the request. To compute $S$ , we just need to divide:  

$$
\begin{array} { r } { S = \frac { A m o u n t o f \ D a t a } { T i m e \ t o \ a c c e s s } = \frac { 1 0 \ M B } { 2 1 0 \ m s } = 4 7 . 6 2 \ M B / s } \end{array}
$$  

As we can see, because of the large time spent transferring data, $S$ is very near the peak bandwidth of the disk (the seek and rotational costs have been amortized).  

We can compute $R$ similarly. Seek and rotation are the same; we then compute the time spent in transfer, which is $1 0 \mathrm { K B } \ @ \ 5 0 \mathrm { M B / s } ,$ or 0.195 ms.  

$$
\begin{array} { r } { R = \frac { A m o u n t o f D a t a } { T i m e t o a c c e s s } = \frac { 1 0 K B } { 1 0 . 1 9 5 m s } = 0 . 9 8 1 M B / s } \end{array}
$$  

As we can see, $R$ is less than $\boldsymbol { 1 } \mathrm { M B / s } ,$ , and $S / R$ is almost 50.  

# Back To RAID-0 Analysis, Again  

Let’s now evaluate the performance of striping. As we said above, it is generally good. From a latency perspective, for example, the latency of a single-block request should be just about identical to that of a single disk; after all, RAID-0 will simply redirect that request to one of its disks.  

From the perspective of steady-state sequential throughput, we’d expect to get the full bandwidth of the system. Thus, throughput equals $N$ (the number of disks) multiplied by $S$ (the sequential bandwidth of a single disk). For a large number of random $\mathrm { I / O s }$ , we can again use all of the disks, and thus obtain $N \cdot R \mathbf { M } \mathbf { B } / \mathbf { s }$ . As we will see below, these values are both the simplest to calculate and will serve as an upper bound in comparison with other RAID levels.  

