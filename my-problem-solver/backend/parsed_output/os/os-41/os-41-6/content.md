# 41.6 The Large-File Exception  

In FFS, there is one important exception to the general policy of file placement, and it arises for large files. Without a different rule, a large file would entirely fill the block group it is first placed within (and maybe others). Filling a block group in this manner is undesirable, as it prevents subsequent “related” files from being placed within this block group, and thus may hurt file-access locality.  

Thus, for large files, FFS does the following. After some number of blocks are allocated into the first block group (e.g., 12 blocks, or the number of direct pointers available within an inode), FFS places the next “large” chunk of the file (e.g., those pointed to by the first indirect block) in another block group (perhaps chosen for its low utilization). Then, the next chunk of the file is placed in yet another different block group, and so on.  

Let’s look at some diagrams to understand this policy better. Without the large-file exception, a single large file would place all of its blocks into one part of the disk. We investigate a small example of a file $( / \alpha )$ with 30 blocks in an FFS configured with 10 inodes and 40 data blocks per group. Here is the depiction of FFS without the large-file exception:  

![](images/cd8370405a3a1f04b37d771970f225151b8063fe64e6fecbf7da32ec357688b9.jpg)  

OPERATINGSYSTEMS[VERSION 1.10]  

As you can see in the picture, $/ \mathsf { a }$ fills up most of the data blocks in Group 0, whereas other groups remain empty. If some other files are now created in the root directory $\bar { ( / ) }$ , there is not much room for their data in the group.  

With the large-file exception (here set to five blocks in each chunk), FFS instead spreads the file spread across groups, and the resulting utilization within any one group is not too high:  

![](images/ec1e316cead668288e8af101cc9ac7d37ec367f8918b82a3284eccaa0d3ed3cc.jpg)  

The astute reader (that’s you) will note that spreading blocks of a file across the disk will hurt performance, particularly in the relatively common case of sequential file access (e.g., when a user or application reads chunks 0 through 29 in order). And you are right, oh astute reader of ours! But you can address this problem by choosing chunk size carefully.  

Specifically, if the chunk size is large enough, the file system will spend most of its time transferring data from disk and just a (relatively) little time seeking between chunks of the block. This process of reducing an overhead by doing more work per overhead paid is called amortization and is a common technique in computer systems.  

Let’s do an example: assume that the average positioning time (i.e., seek and rotation) for a disk is $1 0 \mathrm { m s }$ . Assume further that the disk transfers data at $4 0 ~ \mathrm { M B / s }$ . If your goal was to spend half our time seeking between chunks and half our time transferring data (and thus achieve $5 0 \%$ of peak disk performance), you would thus need to spend $1 0 ~ \mathrm { { m s } }$ transferring data for every $1 0 ~ \mathrm { { m s } }$ positioning. So the question becomes: how big does a chunk have to be in order to spend $\bar { 1 0 } ~ \mathrm { { m s } }$ in transfer? Easy, just use our old friend, math, in particular the dimensional analysis mentioned in the chapter on disks [AD14a]:  

$$
\frac { 4 0 \mathcal { M } \mathcal { B } } { s e c } \cdot \frac { 1 0 2 4 ~ K B } { 1 \mathcal { M } \mathcal { B } } \cdot \frac { 1 s e c } { 1 0 0 0 \mathcal { p } \alpha \mathcal { S } } \cdot 1 0 \mathcal { p } \mathcal { R } \mathcal { S } = 4 0 9 . 6 ~ K B
$$  

Basically, what this equation says is this: if you transfer data at 40 MB/s, you need to transfer only 409.6KB every time you seek in order to spend half your time seeking and half your time transferring. Similarly, you can compute the size of the chunk you would need to achieve $9 0 \%$ of peak bandwidth (turns out it is about 3.6MB), or even $9 9 \%$ of peak bandwidth (39.6MB!). As you can see, the closer you want to get to peak, the bigger these chunks get (see Figure 41.2 for a plot of these values).  

FFS did not use this type of calculation in order to spread large files across groups, however. Instead, it took a simple approach, based on the  

![](images/f2d96c376b9350fc808632d2e06558c3271f38984da20189d521761de794fa66.jpg)  
Figure 41.2: Amortization: How Big Do Chunks Have To Be? structure of the inode itself. The first twelve direct blocks were placed in the same group as the inode; each subsequent indirect block, and all the blocks it pointed to, was placed in a different group. With a block size of 4KB, and 32-bit disk addresses, this strategy implies that every 1024 blocks of the file (4MB) were placed in separate groups, the lone exception being the first 48KB of the file as pointed to by direct pointers.  

Note that the trend in disk drives is that transfer rate improves fairly rapidly, as disk manufacturers are good at cramming more bits into the same surface, but the mechanical aspects of drives related to seeks (disk arm speed and the rate of rotation) improve rather slowly [P98]. The implication is that over time, mechanical costs become relatively more expensive, and thus, to amortize said costs, you have to transfer more data between seeks.  

