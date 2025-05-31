# 38.7 RAID Level 5: Rotating Parity  

To address the small-write problem (at least, partially), Patterson, Gibson, and Katz introduced RAID-5. RAID-5 works almost identically to RAID-4, except that it rotates the parity block across drives (Figure 38.7).  

![](images/1b4f3d2c75fa5b262be0caed5f2c9fe1b45ca93f83b558d52eec544ad6736919.jpg)  
Figure 38.7: RAID-5 With Rotated Parity  

As you can see, the parity block for each stripe is now rotated across the disks, in order to remove the parity-disk bottleneck for RAID-4.  

# RAID-5 Analysis  

Much of the analysis for RAID-5 is identical to RAID-4. For example, the effective capacity and failure tolerance of the two levels are identical. So are sequential read and write performance. The latency of a single request (whether a read or a write) is also the same as RAID-4.  

Random read performance is a little better, because we can now utilize all disks. Finally, random write performance improves noticeably over RAID-4, as it allows for parallelism across requests. Imagine a write to block 1 and a write to block 10; this will turn into requests to disk 1 and disk 4 (for block 1 and its parity) and requests to disk 0 and disk 2 (for  

OPERATINGSYSTEMS[VERSION 1.10]  

Figure 38.8: RAID Capacity, Reliability, and Performance   


<html><body><table><tr><td colspan="2">RAID-0</td><td>RAID-1</td><td>RAID-4</td><td>RAID-5</td></tr><tr><td>Capacity</td><td>N :B</td><td>(N : B)/2</td><td>(N-1B</td><td>(N-1)B</td></tr><tr><td>Reliability</td><td>0</td><td>1 (for sure) (if lucky)</td><td>1</td><td>1</td></tr><tr><td>Throughput</td><td></td><td></td><td></td><td></td></tr><tr><td>Sequential Read</td><td>N.S</td><td>(N/2) : s1</td><td>(N-1)S</td><td>(N-1)S</td></tr><tr><td>Sequential Write</td><td>N.S</td><td>(N/2) : s1</td><td>(N-1) S</td><td>(N-1) S</td></tr><tr><td>Random Read</td><td>N.R</td><td>NR</td><td>(N-1)R</td><td>N.R</td></tr><tr><td>Random Write</td><td>N.R</td><td>(N/2) : R</td><td>JR</td><td>4R</td></tr><tr><td>Latency</td><td></td><td></td><td></td><td></td></tr><tr><td>Read</td><td>T</td><td>T</td><td>T</td><td>T</td></tr><tr><td>Write</td><td>T</td><td>T</td><td>2T</td><td>2T</td></tr></table></body></html>  

block 10 and its parity). Thus, they can proceed in parallel. In fact, we can generally assume that given a large number of random requests, we will be able to keep all the disks about evenly busy. If that is the case, then our total bandwidth for small writes will be $\textstyle { \frac { N } { 4 } } \cdot R \mathbf { M } \mathbf { B } / { \mathbf { s } }$ . The factor of four loss is due to the fact that each RAID-5 write still generates 4 total I/O operations, which is simply the cost of using parity-based RAID.  

Because RAID-5 is basically identical to RAID-4 except in the few cases where it is better, it has almost completely replaced RAID-4 in the marketplace. The only place where it has not is in systems that know they will never perform anything other than a large write, thus avoiding the smallwrite problem altogether [HLM94]; in those cases, RAID-4 is sometimes used as it is slightly simpler to build.  

