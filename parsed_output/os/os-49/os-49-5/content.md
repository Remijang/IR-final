# 49.5 The NFSv2 Protocol  

We thus arrive at the NFSv2 protocol definition. Our problem statement is simple:  

THE CRUX: HOW TO DEFINE A STATELESS FILE PROTOCOL How can we define the network protocol to enable stateless operation? Clearly, stateful calls like open() can’t be a part of the discussion (as it would require the server to track open files); however, the client application will want to call open(), read(), write(), close() and other standard API calls to access files and directories. Thus, as a refined question, how do we define the protocol to both be stateless and support the POSIX file system API?  

One key to understanding the design of the NFS protocol is understanding the file handle. File handles are used to uniquely describe the file or directory a particular operation is going to operate upon; thus, many of the protocol requests include a file handle.  

You can think of a file handle as having three important components: a volume identifier, an inode number, and a generation number; together, these three items comprise a unique identifier for a file or directory that a client wishes to access. The volume identifier informs the server which file system the request refers to (an NFS server can export more than one file system); the inode number tells the server which file within that partition the request is accessing. Finally, the generation number is needed when reusing an inode number; by incrementing it whenever an inode number is reused, the server ensures that a client with an old file handle can’t accidentally access the newly-allocated file.  

Here is a summary of some of the important pieces of the protocol; the full protocol is available elsewhere (see Callaghan’s book for an excellent and detailed overview of NFS [C00]).  

NFSPROC GETATTR file handle returns: attributes   
NFSPROC SETATTR file handle, attributes returns: attributes   
NFSPROC LOOKUP directory file handle, name of file/dir to look up returns: file handle, attributes   
NFSPROC READ file handle, offset, count data, attributes   
NFSPROC WRITE file handle, offset, count, data attributes   
NFSPROC CREATE directory file handle, name of file, attributes file handle, attributes   
NFSPROC REMOVE directory file handle, name of file to be removed   
NFSPROC MKDIR directory file handle, name of directory, attributes file handle, attributes   
NFSPROC RMDIR directory file handle, name of directory to be removed   
NFSPROC READDIR directory handle, count of bytes to read, cookie returns: directory entries, cookie (to get more entries)  

# Figure 49.4: The NFS Protocol: Examples  

We briefly highlight the important components of the protocol. First, the LOOKUP protocol message is used to obtain a file handle, which is then subsequently used to access file data. The client passes a directory file handle and name of a file to look up, and the handle to that file (or directory) plus its attributes are passed back to the client from the server.  

For example, assume the client already has a directory file handle for the root directory of a file system (/) (indeed, this would be obtained through the NFS mount protocol, which is how clients and servers first are connected together; we do not discuss the mount protocol here for sake of brevity). If an application running on the client opens the file /foo.txt, the client-side file system sends a lookup request to the server, passing it the root file handle and the name foo.txt; if successful, the file handle (and attributes) for foo.txt will be returned.  

In case you are wondering, attributes are just the metadata that the file system tracks about each file, including fields such as file creation time, last modification time, size, ownership and permissions information, and so forth, i.e., the same type of information that you would get back if you called stat() on a file.  

Once a file handle is available, the client can issue READ and WRITE protocol messages on a file to read or write the file, respectively. The READ protocol message requires the protocol to pass along the file handle of the file along with the offset within the file and number of bytes to read. The server then will be able to issue the read (after all, the handle tells the server which volume and which inode to read from, and the offset and count tells it which bytes of the file to read) and return the data (and up  

OPERATINGSYSTEMS[VERSION 1.10]  

to-date attributes) to the client (or an error if there was a failure). WRITE is handled similarly, except the data is passed from the client to the server, and just a success code (and up-to-date attributes) is returned.  

One last interesting protocol message is the GETATTR request; given a file handle, it simply fetches the attributes for that file, including the last modified time of the file. We will see why this protocol request is important in NFSv2 below when we discuss caching (can you guess why?).  

