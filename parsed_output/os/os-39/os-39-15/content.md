# 39.15 Symbolic Links  

There is one other type of link that is really useful, and it is called a symbolic link or sometimes a soft link. Hard links are somewhat limited: you can’t create one to a directory (for fear that you will create a cycle in the directory tree); you can’t hard link to files in other disk partitions (because inode numbers are only unique within a particular file system, not across file systems); etc. Thus, a new type of link called the symbolic link was created [MJLF84].  

To create such a link, you can use the same program $\mathtt { l n }$ , but with the -s flag. Here is an example:  

prompt> echo hello $>$ file prompt> ln -s file file2 prompt> cat file2 hello  

OPERATINGSYSTEMS[VERSION 1.10]  

As you can see, creating a soft link looks much the same, and the original file can now be accessed through the file name file as well as the symbolic link name file2.  

However, beyond this surface similarity, symbolic links are actually quite different from hard links. The first difference is that a symbolic link is actually a file itself, of a different type. We’ve already talked about regular files and directories; symbolic links are a third type the file system knows about. A stat on the symlink reveals all:  

prompt> stat file regular file   
prompt> stat file2 .. symbolic link  

Running ls also reveals this fact. If you look closely at the first character of the long-form of the output from ls, you can see that the first character in the left-most column is a - for regular files, a d for directories, and an l for soft links. You can also see the size of the symbolic link (4 bytes in this case) and what the link points to (the file named file).  

prompt> ls -al drwxr-x--- 2 remzi remzi 29 May 3 19:10 ./ drwxr-x-- 27 remzi remzi 4096 May 3 15:14 ../ -rw-r- 1 remzi remzi 6 May 3 19:10 file lrwxrwxrwx 1 remzi remzi 4 May 3 19:10 file2 -> file  

The reason that file2 is 4 bytes is because the way a symbolic link is formed is by holding the pathname of the linked-to file as the data of the link file. Because we’ve linked to a file named file, our link file file2 is small (4 bytes). If we link to a longer pathname, our link file would be bigger:  

prompt> echo hello $>$ alongerfilename   
prompt> ln -s alongerfilename file3   
prompt> ls -al alongerfilename file3   
-rw-r- - 1 remzi remzi 6 May 3 19:17 alongerfilename   
lrwxrwxrwx 1 remzi remzi 15 May 3 19:17 file3 -> alongerfilename  

Finally, because of the way symbolic links are created, they leave the possibility for what is known as a dangling reference:  

prompt> echo hello $>$ file   
prompt> ln -s file file2   
prompt> cat file2   
hello   
prompt> rm file   
prompt> cat file2   
cat: file2: No such file or directory  

THREE EASY PIECES  

As you can see in this example, quite unlike hard links, removing the original file named file causes the link to point to a pathname that no longer exists.  

