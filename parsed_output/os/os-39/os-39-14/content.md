# 39.14 Hard Links  

We now come back to the mystery of why removing a file is performed via unlink(), by understanding a new way to make an entry in the file system tree, through a system call known as link(). The link() system call takes two arguments, an old pathname and a new one; when you “link” a new file name to an old one, you essentially create another way to refer to the same file. The command-line program ln is used to do this, as we see in this example:  

prompt> echo hello $>$ file   
prompt> cat file   
hello   
prompt> ln file file2   
prompt> cat file2   
hello  

OPERATINGSYSTEMS[VERSION 1.10]  

Here we created a file with the word “hello” in it, and called the file $\mathtt { f i l e } ^ { 2 }$ . We then create a hard link to that file using the ln program. After this, we can examine the file by either opening file or file2.  

The way link() works is that it simply creates another name in the directory you are creating the link to, and refers it to the same inode number (i.e., low-level name) of the original file. The file is not copied in any way; rather, you now just have two human-readable names (file and file2) that both refer to the same file. We can even see this in the directory itself, by printing out the inode number of each file:  

prompt> ls -i file file2   
67158084 file   
67158084 file2   
prompt>  

By passing the -i flag to ls, it prints out the inode number of each file (as well as the file name). And thus you can see what link really has done: just make a new reference to the same exact inode number (67158084 in this example).  

By now you might be starting to see why unlink() is called unlink() When you create a file, you are really doing two things. First, you are making a structure (the inode) that will track virtually all relevant information about the file, including its size, where its blocks are on disk, and so forth. Second, you are linking a human-readable name to that file, and putting that link into a directory.  

After creating a hard link to a file, the file system perceives no difference between the original file name (file) and the newly created file name (file2); indeed, they are both just links to the underlying metadata about the file, which is found in inode number 67158084.  

Thus, to remove a file from the file system, we call unlink(). In the example above, we could for example remove the file named file, and still access the file without difficulty:  

prompt> rm file removed ‘file’ prompt> cat file2 hello  

The reason this works is because when the file system unlinks file, it checks a reference count within the inode number. This reference count (sometimes called the link count) allows the file system to track how many different file names have been linked to this particular inode. When unlink() is called, it removes the “link” between the human-readable name (the file that is being deleted) to the given inode number, and decrements the reference count; only when the reference count reaches zero does the file system also free the inode and related data blocks, and thus truly “delete” the file.  

You can see the reference count of a file using stat() of course. Let’s see what it is when we create and delete hard links to a file. In this example, we’ll create three links to the same file, and then delete them. Watch the link count!  

prompt> echo hello > file   
prompt> stat file Inode: 67158084 Links: 1   
prompt> ln file file2   
prompt> stat file Inode: 67158084 Links: 2 .   
prompt> stat file2 Inode: 67158084 Links: 2 .   
prompt> ln file2 file3   
prompt> stat file Inode: 67158084 Links: 3   
prompt> rm file   
prompt> stat file2 Inode: 67158084 Links: 2 .   
prompt> rm file2   
prompt> stat file3 Inode: 67158084 Links: 1   
prompt> rm file3  

