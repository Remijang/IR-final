# 41.1 The Problem: Poor Performance  

The problem: performance was terrible. As measured by Kirk McKusick and his colleagues at Berkeley [MJLF84], performance started off bad and got worse over time, to the point where the file system was delivering only $2 \%$ of overall disk bandwidth!  

The main issue was that the old UNIX file system treated the disk like it was a random-access memory; data was spread all over the place without regard to the fact that the medium holding the data was a disk, and thus had real and expensive positioning costs. For example, the data blocks of a file were often very far away from its inode, thus inducing an expensive seek whenever one first read the inode and then the data blocks of a file (a pretty common operation).  

Worse, the file system would end up getting quite fragmented, as the free space was not carefully managed. The free list would end up pointing to a bunch of blocks spread across the disk, and as files got allocated, they would simply take the next free block. The result was that a logically contiguous file would be accessed by going back and forth across the disk, thus reducing performance dramatically.  

For example, imagine the following data block region, which contains four files (A, B, C, and D), each of size 2 blocks:  

<html><body><table><tr><td>A1</td><td>A2</td><td>B1</td><td>B2</td><td>C1</td><td>C2</td><td>D1</td><td>D2</td></tr></table></body></html>  

If B and $\mathrm { ~ D ~ }$ are deleted, the resulting layout is:  

<html><body><table><tr><td>A1</td><td>A2</td><td></td><td></td><td>C1</td><td>C2</td><td></td><td></td></tr></table></body></html>  

As you can see, the free space is fragmented into two chunks of two blocks, instead of one nice contiguous chunk of four. Let’s say you now wish to allocate a file $\scriptstyle \mathrm { E , }$ of size four blocks:  

<html><body><table><tr><td>A1</td><td>A2</td><td>E1 E2</td><td>C1</td><td>C2</td><td>E3 E4</td></tr></table></body></html>  

You can see what happens: E gets spread across the disk, and as a result, when accessing E, you don’t get peak (sequential) performance from the disk. Rather, you first read E1 and E2, then seek, then read E3 and E4. This fragmentation problem happened all the time in the old UNIX file system, and it hurt performance. A side note: this problem is exactly what disk defragmentation tools help with; they reorganize ondisk data to place files contiguously and make free space for one or a few contiguous regions, moving data around and then rewriting inodes and such to reflect the changes.  

One other problem: the original block size was too small (512 bytes). Thus, transferring data from the disk was inherently inefficient. Smaller blocks were good because they minimized internal fragmentation (waste within the block), but bad for transfer as each block might require a positioning overhead to reach it. Thus, the problem:  

# THE CRUX:  

HOW TO ORGANIZE ON-DISK DATA TO IMPROVE PERFORMANCE  

How can we organize file system data structures so as to improve performance? What types of allocation policies do we need on top of those data structures? How do we make the file system “disk aware”?  

OPERATINGSYSTEMS[VERSION 1.10]  

