# 45.6 One Last Problem: Lost Writes  

Unfortunately, misdirected writes are not the last problem we will address. Specifically, some modern storage devices also have an issue known as a lost write, which occurs when the device informs the upper layer that a write has completed but in fact it never is persisted; thus, what remains is the old contents of the block rather than the updated new contents.  

The obvious question here is: do any of our checksumming strategies from above (e.g., basic checksums, or physical identity) help to detect lost writes? Unfortunately, the answer is no: the old block likely has a matching checksum, and the physical ID used above (disk number and block offset) will also be correct. Thus our final problem:  

CRUX: HOW TO HANDLE LOST WRITES How should a storage system or disk controller detect lost writes? What additional features are required from the checksum?  

There are a number of possible solutions that can help $\scriptstyle { \left[ { \mathrm { K } } + 0 8 \right] }$ . One classic approach [BS04] is to perform a write verify or read-after-write; by immediately reading back the data after a write, a system can ensure that the data indeed reached the disk surface. This approach, however, is quite slow, doubling the number of I/Os needed to complete a write.  

Some systems add a checksum elsewhere in the system to detect lost writes. For example, Sun’s Zettabyte File System (ZFS) includes a checksum in each file system inode and indirect block for every block included within a file. Thus, even if the write to a data block itself is lost, the checksum within the inode will not match the old data. Only if the writes to both the inode and the data are lost simultaneously will such a scheme fail, an unlikely (but unfortunately, possible!) situation.  

