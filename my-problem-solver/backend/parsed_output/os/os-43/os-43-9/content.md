# 43.9 A New Problem: Garbage Collection  

You may have noticed another problem with LFS; it repeatedly writes the latest version of a file (including its inode and data) to new locations on disk. This process, while keeping writes efficient, implies that LFS leaves old versions of file structures scattered throughout the disk. We (rather unceremoniously) call these old versions garbage.  

For example, let’s imagine the case where we have an existing file referred to by inode number $k ,$ which points to a single data block $D 0$ . We now update that block, generating both a new inode and a new data block. The resulting on-disk layout of LFS would look something like this (note we omit the imap and other structures for simplicity; a new chunk of imap would also have to be written to disk to point to the new inode):  

![](images/5e32193542fdbc822eaef156643027f367b9b52254c755fda92d17e1a6a155e7.jpg)  

In the diagram, you can see that both the inode and data block have two versions on disk, one old (the one on the left) and one current and thus live (the one on the right). By the simple act of (logically) updating a data block, a number of new structures must be persisted by LFS, thus leaving old versions of said blocks on the disk.  

As another example, imagine we instead append a block to that original file $k$ . In this case, a new version of the inode is generated, but the old data block is still pointed to by the inode. Thus, it is still live and very much part of the current file system:  

![](images/069b3a519dbceb252a7bb0d11a7a2024a9ce10294ffcd384c931cc5304881654.jpg)  

So what should we do with these older versions of inodes, data blocks, and so forth? One could keep those older versions around and allow users to restore old file versions (for example, when they accidentally overwrite or delete a file, it could be quite handy to do so); such a file system is known as a versioning file system because it keeps track of the different versions of a file.  

However, LFS instead keeps only the latest live version of a file; thus (in the background), LFS must periodically find these old dead versions of file data, inodes, and other structures, and clean them; cleaning should thus make blocks on disk free again for use in subsequent writes. Note that the process of cleaning is a form of garbage collection, a technique that arises in programming languages that automatically free unused memory for programs.  

Earlier we discussed segments as important as they are the mechanism that enables large writes to disk in LFS. As it turns out, they are also quite integral to effective cleaning. Imagine what would happen if the LFS cleaner simply went through and freed single data blocks, inodes, etc., during cleaning. The result: a file system with some number of free holes mixed between allocated space on disk. Write performance would drop considerably, as LFS would not be able to find a large contiguous region to write to disk sequentially and with high performance.  

Instead, the LFS cleaner works on a segment-by-segment basis, thus clearing up large chunks of space for subsequent writing. The basic cleaning process works as follows. Periodically, the LFS cleaner reads in a number of old (partially-used) segments, determines which blocks are live within these segments, and then write out a new set of segments with just the live blocks within them, freeing up the old ones for writing. Specifically, we expect the cleaner to read in $M$ existing segments, compact their contents into $N$ new segments (where $N < M$ ), and then write the $N$ segments to disk in new locations. The old $M$ segments are then freed and can be used by the file system for subsequent writes.  

We are now left with two problems, however. The first is mechanism: how can LFS tell which blocks within a segment are live, and which are dead? The second is policy: how often should the cleaner run, and which segments should it pick to clean?  

