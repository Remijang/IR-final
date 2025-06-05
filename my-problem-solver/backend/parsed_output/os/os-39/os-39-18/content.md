# 39.18 Summary  

The file system interface in UNIX systems (and indeed, in any system) is seemingly quite rudimentary, but there is a lot to understand if you wish to master it. Nothing is better, of course, than simply using it (a lot). So please do so! Of course, read more; as always, Stevens [SR05] is the place to begin.  

ASIDE: KEY FILE SYSTEM TERMS  

• A file is an array of bytes which can be created, read, written, and deleted. It has a low-level name (i.e., a number) that refers to it uniquely. The low-level name is often called an i-number.   
• A directory is a collection of tuples, each of which contains a human-readable name and low-level name to which it maps. Each entry refers either to another directory or to a file. Each directory also has a low-level name (i-number) itself. A directory always has two special entries: the . entry, which refers to itself, and the .. entry, which refers to its parent.   
• A directory tree or directory hierarchy organizes all files and directories into a large tree, starting at the root.   
To access a file, a process must use a system call (usually, open()) to request permission from the operating system. If permission is granted, the OS returns a file descriptor, which can then be used for read or write access, as permissions and intent allow.   
• Each file descriptor is a private, per-process entity, which refers to an entry in the open file table. The entry therein tracks which file this access refers to, the current offset of the file (i.e., which part of the file the next read or write will access), and other relevant information.   
• Calls to read() and write() naturally update the current offset; otherwise, processes can use lseek() to change its value, enabling random access to different parts of the file.   
• To force updates to persistent media, a process must use fsync() or related calls. However, doing so correctly while maintaining high performance is challenging $\scriptstyle { [ { \mathrm { P } } + 1 4 ] }$ , so think carefully when doing so.   
• To have multiple human-readable names in the file system refer to the same underlying file, use hard links or symbolic links. Each is useful in different circumstances, so consider their strengths and weaknesses before usage. And remember, deleting a file is just performing that one last unlink() of it from the directory hierarchy.   
• Most file systems have mechanisms to enable and disable sharing. A rudimentary form of such controls are provided by permissions bits; more sophisticated access control lists allow for more precise control over exactly who can access and manipulate information.  

