# 39.5 Reading And Writing, But Not Sequentially  

Thus far, we’ve discussed how to read and write files, but all access has been sequential; that is, we have either read a file from the beginning to the end, or written a file out from beginning to end.  

Sometimes, however, it is useful to be able to read or write to a specific offset within a file; for example, if you build an index over a text document, and use it to look up a specific word, you may end up reading from some random offsets within the document. To do so, we will use the lseek() system call. Here is the function prototype:  

off_t lseek(int fildes, off_t offset, int whence);  

The first argument is familiar (a file descriptor). The second argument is the offset, which positions the file offset to a particular location within the file. The third argument, called whence for historical reasons, determines exactly how the seek is performed. From the man page:  

If whence is SEEK_SET, the offset is set to offset bytes.   
If whence is SEEK_CUR, the offset is set to its current location plus offset bytes.   
If whence is SEEK_END, the offset is set to the size of the file plus offset bytes.  

As you can tell from this description, for each file a process opens, the OS tracks a “current” offset, which determines where the next read or write will begin reading from or writing to within the file. Thus, part of the abstraction of an open file is that it has a current offset, which is updated in one of two ways. The first is when a read or write of $N$ bytes takes place, $N$ is added to the current offset; thus each read or write implicitly updates the offset. The second is explicitly with lseek, which changes the offset as specified above.  

The offset, as you might have guessed, is kept in that struct file we saw earlier, as referenced from the struct proc. Here is a (simplified) xv6 definition of the structure:  

struct file { int ref; char readable; char writable; struct inode \*ip; uint off;   
};  

ASIDE: CALLING L S E E K() DOES NOT PERFORM A DISK SEEK The poorly-named system call lseek() confuses many a student trying to understand disks and how the file systems atop them work. Do not confuse the two! The lseek() call simply changes a variable in OS memory that tracks, for a particular process, at which offset its next read or write will start. A disk seek occurs when a read or write issued to the disk is not on the same track as the last read or write, and thus necessitates a head movement. Making this even more confusing is the fact that calling lseek() to read or write from/to random parts of a file, and then reading/writing to those random parts, will indeed lead to more disk seeks. Thus, calling lseek() can lead to a seek in an upcoming read or write, but absolutely does not cause any disk I/O to occur itself.  

As you can see in the structure, the OS can use this to determine whether the opened file is readable or writable (or both), which underlying file it refers to (as pointed to by the struct inode pointer ip), and the current offset (off). There is also a reference count (ref), which we will discuss further below.  

These file structures represent all of the currently opened files in the system; together, they are sometimes referred to as the open file table. The xv6 kernel just keeps these as an array, with one lock for the entire table:  

struct { struct spinlock lock; struct file file[NFILE];   
} ftable;  

Let’s make this a bit clearer with a few examples. First, let’s track a process that opens a file (of size 300 bytes) and reads it by calling the read() system call repeatedly, each time reading 100 bytes. Here is a trace of the relevant system calls, along with the values returned by each system call, and the value of the current offset in the open file table for this file access:  

<html><body><table><tr><td>System Calls</td><td></td><td>Return Code</td><td>Current Offset</td></tr><tr><td>fd = open("file", O_RDONLY);</td><td></td><td>3</td><td>0</td></tr><tr><td>read(fd, buffer, 100);</td><td></td><td>100</td><td>100</td></tr><tr><td>read(fd, buffer, 100);</td><td></td><td>100</td><td>200</td></tr><tr><td></td><td>read(fd, buffer, 100);</td><td>100</td><td>300</td></tr><tr><td></td><td>read(fd, buffer, 100);</td><td>0</td><td>300</td></tr><tr><td>close(fd) ;</td><td></td><td>0</td><td></td></tr></table></body></html>  

There are a couple of items of interest to note from the trace. First, you can see how the current offset gets initialized to zero when the file is  

OPERATINGSYSTEMS[VERSION 1.10]  

opened. Next, you can see how it is incremented with each read() by the process; this makes it easy for a process to just keep calling read() to get the next chunk of the file. Finally, you can see how at the end, an attempted read() past the end of the file returns zero, thus indicating to the process that it has read the file in its entirety.  

Second, let’s trace a process that opens the same file twice and issues a read to each of them.  

<html><body><table><tr><td></td><td></td><td>Return</td><td>OFT[10] Current</td><td>OFT[11] Current</td></tr><tr><td>System Calls</td><td></td><td>Code 3</td><td>Offset 0</td><td>Offset</td></tr><tr><td>fd1 = open("file",</td><td>O_RDONLY) ;</td><td>4</td><td>0</td><td>0</td></tr><tr><td>fd2 = open("file", O_RDONLY);</td><td></td><td>100</td><td>100</td><td>0</td></tr><tr><td>read(fdl, bufferl, 100); read(fd2, buffer2, 100);</td><td></td><td>100</td><td>100</td><td>100</td></tr><tr><td>close(fd1) ;</td><td></td><td>0</td><td></td><td>100</td></tr><tr><td>close(fd2);</td><td></td><td>0</td><td></td><td></td></tr></table></body></html>  

In this example, two file descriptors are allocated (3 and 4), and each refers to a different entry in the open file table (in this example, entries 10 and 11, as shown in the table heading; OFT stands for Open File Table). If you trace through what happens, you can see how each current offset is updated independently.  

In one final example, a process uses lseek() to reposition the current offset before reading; in this case, only a single open file table entry is needed (as with the first example).  

<html><body><table><tr><td>System Calls</td><td>Return Code</td><td>Current Offset</td></tr><tr><td>fd = open("file", O_RDONLY);</td><td>3</td><td>0</td></tr><tr><td>lseek(fd, 200, SEEK SET);</td><td>200</td><td>200</td></tr><tr><td>read(fd, buffer, 50);</td><td>50</td><td>250</td></tr><tr><td>close(fd);</td><td>0</td><td></td></tr></table></body></html>  

Here, the lseek() call first sets the current offset to 200. The subsequent read() then reads the next 50 bytes, and updates the current offset accordingly.  

