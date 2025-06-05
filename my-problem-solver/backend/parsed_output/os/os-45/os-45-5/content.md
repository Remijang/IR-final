# 45.5 A New Problem: Misdirected Writes  

The basic scheme described above works well in the general case of corrupted blocks. However, modern disks have a couple of unusual failure modes that require different solutions.  

The first failure mode of interest is called a misdirected write. This arises in disk and RAID controllers which write the data to disk correctly, except in the wrong location. In a single-disk system, this means that the disk wrote block $\hat { D } _ { x }$ not to address $x$ (as desired) but rather to address $y$ (thus “corrupting” $D _ { y }$ ); in addition, within a multi-disk system, the controller may also write $D _ { i , x }$ not to address $x$ of disk $i$ but rather to some other disk $j$ . Thus our question:  

CRUX: HOW TO HANDLE MISDIRECTED WRITES How should a storage system or disk controller detect misdirected writes? What additional features are required from the checksum?  

The answer, not surprisingly, is simple: add a little more information to each checksum. In this case, adding a physical identifier (physical ID) is quite helpful. For example, if the stored information now contains the checksum $\hat { C } ( D )$ and both the disk and sector numbers of the block, it is easy for the client to determine whether the correct information resides within a particular locale. Specifically, if the client is reading block 4 on disk 10 $( \bar { D } _ { 1 0 , 4 } )$ , the stored information should include that disk number and sector offset, as shown below. If the information does not match, a misdirected write has taken place, and a corruption is now detected. Here is an example of what this added information would look like on a twodisk system. Note that this figure, like the others before it, is not to scale, as the checksums are usually small (e.g., 8 bytes) whereas the blocks are much larger (e.g., $4 \mathrm { K B }$ or bigger):  

<html><body><table><tr><td>Disk 1</td><td>Doalo</td><td>p=ys!p</td><td>0=lckkq</td><td></td><td>DO</td><td>[a]]</td><td>l=ys!p</td><td>pllekkq</td><td>D1</td><td></td><td>l=ys!p</td><td></td><td>D2</td></tr><tr><td colspan="2"></td><td></td><td></td><td></td><td colspan="2"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Disk 0</td><td>Coal</td><td>0=ys!p</td><td>0=qkkq</td><td></td><td>DO</td><td></td><td>0=ys!p</td><td>blekk</td><td>D1</td><td></td><td>0=ys!p</td><td></td><td>D2</td></tr></table></body></html>  

OPERATINGSYSTEMS[VERSION 1.10]  

WWW.OSTEP.ORG  

You can see from the on-disk format that there is now a fair amount of redundancy on disk: for each block, the disk number is repeated within each block, and the offset of the block in question is also kept next to the block itself. The presence of redundant information should be no surprise, though; redundancy is the key to error detection (in this case) and recovery (in others). A little extra information, while not strictly needed with perfect disks, can go a long ways in helping detect problematic situations should they arise.  

