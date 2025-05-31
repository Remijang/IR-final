# 40.2 Overall Organization  

We now develop the overall on-disk organization of the data structures of the vsfs file system. The first thing we’ll need to do is divide the disk into blocks; simple file systems use just one block size, and that’s exactly what we’ll do here. Let’s choose a commonly-used size of $4 \mathrm { K B }$ .  

Thus, our view of the disk partition where we’re building our file system is simple: a series of blocks, each of size $4 \ \mathrm { K B }$ . The blocks are addressed from 0 to $N - 1 ,$ in a partition of size $N$ 4-KB blocks. Assume we have a really small disk, with just 64 blocks:  

![](images/cfd74ac78f719f1c2725d9954f2dbdf2cdeb794c453affa9f0cf2fedb71e01dd.jpg)  

Let’s now think about what we need to store in these blocks to build a file system. Of course, the first thing that comes to mind is user data. In fact, most of the space in any file system is (and should be) user data. Let’s call the region of the disk we use for user data the data region, and,  

OPERATINGSYSTEMS[VERSION 1.10]  

again for simplicity, reserve a fixed portion of the disk for these blocks, say the last 56 of 64 blocks on the disk:  

![](images/ee3fcafcddcdc866d5e25f6e542eb997698355be4c18f34ab61602e3e9a0bdeb.jpg)  

As we learned about (a little) last chapter, the file system has to track information about each file. This information is a key piece of metadata, and tracks things like which data blocks (in the data region) comprise a file, the size of the file, its owner and access rights, access and modify times, and other similar kinds of information. To store this information, file systems usually have a structure called an inode (we’ll read more about inodes below).  

To accommodate inodes, we’ll need to reserve some space on the disk for them as well. Let’s call this portion of the disk the inode table, which simply holds an array of on-disk inodes. Thus, our on-disk image now looks like this picture, assuming that we use 5 of our 64 blocks for inodes (denoted by I’s in the diagram):  

![](images/3c8cbb67e6fddc687240f7c076bc0439a8c2692304a3b2b5973a77ac3eadc7f7.jpg)  

We should note here that inodes are typically not that big, for example 128 or 256 bytes. Assuming 256 bytes per inode, a 4-KB block can hold 16 inodes, and our file system above contains 80 total inodes. In our simple file system, built on a tiny 64-block partition, this number represents the maximum number of files we can have in our file system; however, do note that the same file system, built on a larger disk, could simply allocate a larger inode table and thus accommodate more files.  

Our file system thus far has data blocks (D), and inodes (I), but a few things are still missing. One primary component that is still needed, as you might have guessed, is some way to track whether inodes or data blocks are free or allocated. Such allocation structures are thus a requisite element in any file system.  

Many allocation-tracking methods are possible, of course. For example, we could use a free list that points to the first free block, which then points to the next free block, and so forth. We instead choose a simple and popular structure known as a bitmap, one for the data region (the data bitmap), and one for the inode table (the inode bitmap). A bitmap is a simple structure: each bit is used to indicate whether the corresponding object/block is free (0) or in-use (1). And thus our new on-disk layout, with an inode bitmap (i) and a data bitmap (d):  

![](images/3fac3bacc620e8c294ede72db873b39f5bef820d342da7df61abd262d01de300.jpg)  

You may notice that it is a bit of overkill to use an entire 4-KB block for these bitmaps; such a bitmap can track whether 32K objects are allocated, and yet we only have 80 inodes and 56 data blocks. However, we just use an entire 4-KB block for each of these bitmaps for simplicity.  

The careful reader (i.e., the reader who is still awake) may have noticed there is one block left in the design of the on-disk structure of our very simple file system. We reserve this for the superblock, denoted by an S in the diagram below. The superblock contains information about this particular file system, including, for example, how many inodes and data blocks are in the file system (80 and 56, respectively in this instance), where the inode table begins (block 3), and so forth. It will likely also include a magic number of some kind to identify the file system type (in this case, vsfs).  

![](images/faf4cb8b700810a2d9cd11261fb2d7ddc4ef7afb5f3cf0e4118a277b948931d4.jpg)  

Thus, when mounting a file system, the operating system will read the superblock first, to initialize various parameters, and then attach the volume to the file-system tree. When files within the volume are accessed, the system will thus know exactly where to look for the needed on-disk structures.  

