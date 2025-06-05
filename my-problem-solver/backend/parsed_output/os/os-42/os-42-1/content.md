# 42.1 A Detailed Example  

To kick off our investigation of journaling, let’s look at an example. We’ll need to use a workload that updates on-disk structures in some way. Assume here that the workload is simple: the append of a single data block to an existing file. The append is accomplished by opening the file, calling lseek() to move the file offset to the end of the file, and then issuing a single 4KB write to the file before closing it.  

Let’s also assume we are using standard simple file system structures on the disk, similar to file systems we have seen before. This tiny example includes an inode bitmap (with just 8 bits, one per inode), a data bitmap (also 8 bits, one per data block), inodes (8 total, numbered 0 to 7, and spread across four blocks), and data blocks (8 total, numbered 0 to 7). Here is a diagram of this file system:  

![](images/6238ce4f59ca742a6b101fc709f4a906da7c94334331f5177bf9df2d19110506.jpg)  

If you look at the structures in the picture, you can see that a single inode is allocated (inode number 2), which is marked in the inode bitmap, and a single allocated data block (data block 4), also marked in the data bitmap. The inode is denoted I[v1], as it is the first version of this inode; it will soon be updated (due to the workload described above).  

Let’s peek inside this simplified inode too. Inside of I[v1], we see:  

owner : remzi   
permissions : read-write   
size : 1   
pointer : 4   
pointer : null   
pointer : null   
pointer : null  

In this simplified inode, the size of the file is 1 (it has one block allocated), the first direct pointer points to block 4 (the first data block of  

OPERATINGSYSTEMS[VERSION 1.10]  

the file, Da), and all three other direct pointers are set to null (indicating that they are not used). Of course, real inodes have many more fields; see previous chapters for more information.  

When we append to the file, we are adding a new data block to it, and thus must update three on-disk structures: the inode (which must point to the new block and record the new larger size due to the append), the new data block Db, and a new version of the data bitmap (call it B[v2]) to indicate that the new data block has been allocated.  

Thus, in the memory of the system, we have three blocks which we must write to disk. The updated inode (inode version 2, or I[v2] for short) now looks like this:  

owner : remzi permissions : read-write size : 2 pointer : 4 pointer : 5 pointer : null pointer : null  

The updated data bitmap (B[v2]) now looks like this: 00001100. Finally, there is the data block (Db), which is just filled with whatever it is users put into files. Stolen music, perhaps?  

What we would like is for the final on-disk image of the file system to look like this:  

![](images/0687b645896f7821b255a350003ab6bb83cf97eb0fb71a14d7219287016af3f8.jpg)  

To achieve this transition, the file system must perform three separate writes to the disk, one each for the inode (I[v2]), bitmap (B[v2]), and data block (Db). Note that these writes usually don’t happen immediately when the user issues a write() system call; rather, the dirty inode, bitmap, and new data will sit in main memory (in the page cache or buffer cache) for some time first; then, when the file system finally decides to write them to disk (after say 5 seconds or 30 seconds), the file system will issue the requisite write requests to the disk. Unfortunately, a crash may occur and thus interfere with these updates to the disk. In particular, if a crash happens after one or two of these writes have taken place, but not all three, the file system could be left in a funny state.  

# Crash Scenarios  

To understand the problem better, let’s look at some example crash scenarios. Imagine only a single write succeeds; there are thus three possible outcomes, which we list here:  

• Just the data block (Db) is written to disk. In this case, the data is on disk, but there is no inode that points to it and no bitmap that even says the block is allocated. Thus, it is as if the write never occurred. This case is not a problem at all, from the perspective of file-system crash consistency1.   
• Just the updated inode (I[v2]) is written to disk. In this case, the inode points to the disk address (5) where Db was about to be written, but Db has not yet been written there. Thus, if we trust that pointer, we will read garbage data from the disk (the old contents of disk address 5). Further, we have a new problem, which we call a file-system inconsistency. The on-disk bitmap is telling us that data block 5 has not been allocated, but the inode is saying that it has. The disagreement between the bitmap and the inode is an inconsistency in the data structures of the file system; to use the file system, we must somehow resolve this problem (more on that below).   
• Just the updated bitmap (B[v2]) is written to disk. In this case, the bitmap indicates that block 5 is allocated, but there is no inode that points to it. Thus the file system is inconsistent again; if left unresolved, this write would result in a space leak, as block 5 would never be used by the file system.  

There are also three more crash scenarios in this attempt to write three blocks to disk. In these cases, two writes succeed and the last one fails:  

• The inode (I[v2]) and bitmap (B[v2]) are written to disk, but not data (Db). In this case, the file system metadata is completely consistent: the inode has a pointer to block 5, the bitmap indicates that 5 is in use, and thus everything looks OK from the perspective of the file system’s metadata. But there is one problem: 5 has garbage in it again. • The inode (I[v2]) and the data block (Db) are written, but not the bitmap (B[v2]). In this case, we have the inode pointing to the correct data on disk, but again have an inconsistency between the inode and the old version of the bitmap (B1). Thus, we once again need to resolve the problem before using the file system. • The bitmap (B[v2]) and data block (Db) are written, but not the inode (I[v2]). In this case, we again have an inconsistency between the inode and the data bitmap. However, even though the block was written and the bitmap indicates its usage, we have no idea which file it belongs to, as no inode points to the file.  

# The Crash Consistency Problem  

Hopefully, from these crash scenarios, you can see the many problems that can occur to our on-disk file system image because of crashes: we can have inconsistency in file system data structures; we can have space leaks; we can return garbage data to a user; and so forth. What we’d like to do ideally is move the file system from one consistent state (e.g., before the file got appended to) to another atomically (e.g., after the inode, bitmap, and new data block have been written to disk). Unfortunately, we can’t do this easily because the disk only commits one write at a time, and crashes or power loss may occur between these updates. We call this general problem the crash-consistency problem (we could also call it the consistent-update problem).  

