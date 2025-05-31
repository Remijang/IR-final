# 43.8 What About Directories?  

Thus far, we’ve simplified our discussion a bit by only considering inodes and data blocks. However, to access a file in a file system (such as /home/remzi/foo, one of our favorite fake file names), some directories must be accessed too. So how does LFS store directory data?  

Fortunately, directory structure is basically identical to classic UNIX file systems, in that a directory is just a collection of (name, inode number) mappings. For example, when creating a file on disk, LFS must both write a new inode, some data, as well as the directory data and its inode that refer to this file. Remember that LFS will do so sequentially on the disk (after buffering the updates for some time). Thus, creating a file foo in a directory would lead to the following new structures on disk:  

![](images/a0e2ec066bd4377b9c6b9dd55bb0c0bf7c0d4c8f5a6765911bb49158679fb724.jpg)  

The piece of the inode map contains the information for the location of both the directory file dir as well as the newly-created file $f$ . Thus, when accessing file foo (with inode number $k$ ), you would first look in the inode map (usually cached in memory) to find the location of the inode of directory dir $( A { \bar { 3 } } )$ ; you then read the directory inode, which gives you the location of the directory data $( A 2 )$ ; reading this data block gives you the name-to-inode-number mapping of $( \mathrm { f o o } , k )$ . You then consult the inode map again to find the location of inode number $k \left( A 1 \right)$ , and finally read the desired data block at address $\mathbf { \nabla } A 0 \mathbf { \nabla }$ .  

There is one other serious problem in LFS that the inode map solves, known as the recursive update problem $\scriptstyle [ Z + 1 2 ]$ . The problem arises in any file system that never updates in place (such as LFS), but rather moves updates to new locations on the disk.  

Specifically, whenever an inode is updated, its location on disk changes. If we hadn’t been careful, this would have also entailed an update to the directory that points to this file, which then would have mandated a change to the parent of that directory, and so on, all the way up the file system tree.  

LFS cleverly avoids this problem with the inode map. Even though the location of an inode may change, the change is never reflected in the directory itself; rather, the imap structure is updated while the directory holds the same name-to-inode-number mapping. Thus, through indirection, LFS avoids the recursive update problem.  

OPERATINGSYSTEMS[VERSION 1.10]  

