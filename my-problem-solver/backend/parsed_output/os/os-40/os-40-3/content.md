# 40.3 File Organization: The Inode  

One of the most important on-disk structures of a file system is the inode; virtually all file systems have a structure similar to this. The name inode is short for index node, the historical name given to it in UNIX [RT74] and possibly earlier systems, used because these nodes were originally arranged in an array, and the array indexed into when accessing a particular inode.  

OPERATINGSYSTEMS[VERSION 1.10]  

WWW.OSTEP.ORG  

# ASIDE: DATA STRUCTURE — THE INODE  

The inode is the generic name that is used in many file systems to describe the structure that holds the metadata for a given file, such as its length, permissions, and the location of its constituent blocks. The name goes back at least as far as UNIX (and probably further back to Multics if not earlier systems); it is short for index node, as the inode number is used to index into an array of on-disk inodes in order to find the inode of that number. As we’ll see, design of the inode is one key part of file system design. Most modern systems have some kind of structure like this for every file they track, but perhaps call them different things (such as dnodes, fnodes, etc.).  

Each inode is implicitly referred to by a number (called the i-number), which we’ve earlier called the low-level name of the file. In vsfs (and other simple file systems), given an i-number, you should directly be able to calculate where on the disk the corresponding inode is located. For example, take the inode table of vsfs as above: 20KB in size (five 4KB blocks) and thus consisting of 80 inodes (assuming each inode is 256 bytes); further assume that the inode region starts at 12KB (i.e, the superblock starts at 0KB, the inode bitmap is at address 4KB, the data bitmap at 8KB, and thus the inode table comes right after). In vsfs, we thus have the following layout for the beginning of the file system partition (in closeup view):  

![](images/037c165ab16fcad7897cd977802a3fa1b4c80885843f83c451bd0d606a47ab0b.jpg)  

To read inode number 32, the file system would first calculate the offset into the inode region $( 3 2 \cdot s i z e o f ( i n o d e )$ or 8192), add it to the start address of the inode table on disk (inodeStartAddr $= 1 2 K B$ ), and thus arrive upon the correct byte address of the desired block of inodes: $2 0 K B$ . Recall that disks are not byte addressable, but rather consist of a large number of addressable sectors, usually 512 bytes. Thus, to fetch the block of inodes that contains inode 32, the file system would issue a read to sector $\frac { 2 0 \times 1 0 2 4 } { 5 1 2 }$ , or 40, to fetch the desired inode block. More generally, the sector address sector of the inode block can be calculated as follows:  

blk $\mathbf { \Sigma } = \mathbf { \Sigma }$ (inumber $\star$ sizeof(inode_t)) / blockSize;   
sector $\mathbf { \Sigma } = \mathbf { \Sigma }$ ((blk \* blockSize) $^ +$ inodeStartAddr) / sectorSize;  

Inside each inode is virtually all of the information you need about a file: its type (e.g., regular file, directory, etc.), its size, the number of blocks allocated to it, protection information (such as who owns the file, as well  

#  

<html><body><table><tr><td>Size</td><td>Name</td><td>What is this inode field for?</td></tr><tr><td>2</td><td>mode</td><td>can this file be read/written/executed?.</td></tr><tr><td>2</td><td>uid</td><td>who owns this file?</td></tr><tr><td>4</td><td>size</td><td>how many bytes are in this file?.</td></tr><tr><td>4</td><td>time</td><td>what time was this file last accessed?</td></tr><tr><td>4</td><td>ctime</td><td>what time was this file created?</td></tr><tr><td>4</td><td>mtime</td><td>what time was this file last modified?</td></tr><tr><td>4</td><td>dtime</td><td>what time was this inode deleted?</td></tr><tr><td>2</td><td>gid</td><td>which group does this file belong to?</td></tr><tr><td>2</td><td>links.count.</td><td>how many hard links are there to this file?</td></tr><tr><td>4</td><td>blocks</td><td>how many blocks have been allocated to this file?</td></tr><tr><td>4</td><td>flags</td><td>how should ext2 use this inode?</td></tr><tr><td>4</td><td>osd1</td><td>an OS-dependent field</td></tr><tr><td>60</td><td>block</td><td>a set of disk pointers (15 total).</td></tr><tr><td>4</td><td>generation</td><td>file version (used by NFS)</td></tr><tr><td>4</td><td>file-acl</td><td>a new permissions model beyond mode bits</td></tr><tr><td>4</td><td>dir_acl</td><td>called access control lists.</td></tr></table></body></html>  

as who can access it), some time information, including when the file was created, modified, or last accessed, as well as information about where its data blocks reside on disk (e.g., pointers of some kind). We refer to all such information about a file as metadata; in fact, any information inside the file system that isn’t pure user data is often referred to as such. An example inode from ext2 [P09] is shown in Figure $4 0 . 1 ^ { 1 }$ .  

One of the most important decisions in the design of the inode is how it refers to where data blocks are. One simple approach would be to have one or more direct pointers (disk addresses) inside the inode; each pointer refers to one disk block that belongs to the file. Such an approach is limited: for example, if you want to have a file that is really big (e.g., bigger than the block size multiplied by the number of direct pointers in the inode), you are out of luck.  

# The Multi-Level Index  

To support bigger files, file system designers have had to introduce different structures within inodes. One common idea is to have a special pointer known as an indirect pointer. Instead of pointing to a block that contains user data, it points to a block that contains more pointers, each of which point to user data. Thus, an inode may have some fixed number of direct pointers (e.g., 12), and a single indirect pointer. If a file grows large enough, an indirect block is allocated (from the data-block region of the disk), and the inode’s slot for an indirect pointer is set to point to it. Assuming 4-KB blocks and 4-byte disk addresses, that adds another 1024 pointers; the file can grow to be $( 1 2 + 1 0 2 4 ) \cdot 4 K$ or 4144KB.  

# TIP: CONSIDER EXTENT-BASED APPROACHES  

A different approach is to use extents instead of pointers. An extent is simply a disk pointer plus a length (in blocks); thus, instead of requiring a pointer for every block of a file, all one needs is a pointer and a length to specify the on-disk location of a file. Just a single extent is limiting, as one may have trouble finding a contiguous chunk of on-disk free space when allocating a file. Thus, extent-based file systems often allow for more than one extent, thus giving more freedom to the file system during file allocation.  

In comparing the two approaches, pointer-based approaches are the most flexible but use a large amount of metadata per file (particularly for large files). Extent-based approaches are less flexible but more compact; in particular, they work well when there is enough free space on the disk and files can be laid out contiguously (which is the goal for virtually any file allocation policy anyhow).  

Not surprisingly, in such an approach, you might want to support even larger files. To do so, just add another pointer to the inode: the double indirect pointer. This pointer refers to a block that contains pointers to indirect blocks, each of which contain pointers to data blocks. A double indirect block thus adds the possibility to grow files with an additional $1 0 2 4 \cdot 1 0 2 4 \$ or 1-million 4KB blocks, in other words supporting files that are over 4GB in size. You may want even more, though, and we bet you know where this is headed: the triple indirect pointer.  

Overall, this imbalanced tree is referred to as the multi-level index approach to pointing to file blocks. Let’s examine an example with twelve direct pointers, as well as both a single and a double indirect block. Assuming a block size of 4 KB, and 4-byte pointers, this structure can accommodate a file of just over 4 GB in size (i.e., $( 1 2 + 1 0 2 4 + 1 0 2 4 ^ { 2 } ) \times 4 K B )$ . Can you figure out how big of a file can be handled with the addition of a triple-indirect block? (hint: pretty big)  

Many file systems use a multi-level index, including commonly-used file systems such as Linux ext2 [P09] and ext3, NetApp’s WAFL, as well as the original UNIX file system. Other file systems, including SGI XFS and Linux ext4, use extents instead of simple pointers; see the earlier aside for details on how extent-based schemes work (they are akin to segments in the discussion of virtual memory).  

You might be wondering: why use an imbalanced tree like this? Why not a different approach? Well, as it turns out, many researchers have studied file systems and how they are used, and virtually every time they find certain “truths” that hold across the decades. One such finding is that most files are small. This imbalanced design reflects such a reality; if most files are indeed small, it makes sense to optimize for this case. Thus, with a small number of direct pointers (12 is a typical number), an inode can directly point to $4 8 \mathrm { K B }$ of data, needing one (or more) indirect blocks for larger files. See Agrawal et. al $[ \mathrm { A } { + } 0 7 ]$ for a recent-ish study; Figure 40.2 summarizes those results.  

<html><body><table><tr><td>Most files are small</td><td>~2K is the most common size</td></tr><tr><td>Average file size is growing</td><td>Almost 200K is the average</td></tr><tr><td>Most bytes are stored in large files</td><td>A few big files use most of space</td></tr><tr><td>File systems contain lots of files</td><td>Almost 100K on average</td></tr><tr><td>File systems are roughly half full</td><td>Even as disks grow, file systems remain ~50% full</td></tr><tr><td>Directories are typically small</td><td>Many have few entries; most. have 20 or fewer</td></tr></table></body></html>  

Of course, in the space of inode design, many other possibilities exist; after all, the inode is just a data structure, and any data structure that stores the relevant information, and can query it effectively, is sufficient. As file system software is readily changed, you should be willing to explore different designs should workloads or technologies change.  

