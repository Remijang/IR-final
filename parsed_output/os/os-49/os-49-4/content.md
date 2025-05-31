# 49.4 Key To Fast Crash Recovery: Statelessness  

This simple goal is realized in NFSv2 by designing what we refer to as a stateless protocol. The server, by design, does not keep track of anything about what is happening at each client. For example, the server does not know which clients are caching which blocks, or which files are currently open at each client, or the current file pointer position for a file, etc. Simply put, the server does not track anything about what clients are doing; rather, the protocol is designed to deliver in each protocol request all the information that is needed in order to complete the request. If it doesn’t now, this stateless approach will make more sense as we discuss the protocol in more detail below.  

For an example of a stateful (not stateless) protocol, consider the open() system call. Given a pathname, open() returns a file descriptor (an integer). This descriptor is used on subsequent read() or write() requests to access various file blocks, as in this application code (note that proper error checking of the system calls is omitted for space reasons):  

char buffer[MAX];   
int fd $\mathbf { \Sigma } = \mathbf { \Sigma }$ open("foo", O_RDONLY); // get descriptor "fd" read(fd, buffer, MAX); // read MAX from foo via "fd" read(fd, buffer, MAX); // read MAX again   
read(fd, buffer, MAX); // read MAX again   
close(fd); // close file  

# Figure 49.3: Client Code: Reading From A File  

Now imagine that the client-side file system opens the file by sending a protocol message to the server saying “open the file ’foo’ and give me back a descriptor”. The file server then opens the file locally on its side and sends the descriptor back to the client. On subsequent reads, the client application uses that descriptor to call the read() system call; the client-side file system then passes the descriptor in a message to the file server, saying “read some bytes from the file that is referred to by the descriptor I am passing you here”.  

In this example, the file descriptor is a piece of shared state between the client and the server (Ousterhout calls this distributed state [O91]). Shared state, as we hinted above, complicates crash recovery. Imagine the server crashes after the first read completes, but before the client has issued the second one. After the server is up and running again, the client then issues the second read. Unfortunately, the server has no idea to which file fd is referring; that information was ephemeral (i.e., in memory) and thus lost when the server crashed. To handle this situation, the client and server would have to engage in some kind of recovery protocol, where the client would make sure to keep enough information around in its memory to be able to tell the server what it needs to know (in this case, that file descriptor fd refers to file foo).  

OPERATINGSYSTEMS[VERSION 1.10]  

It gets even worse when you consider the fact that a stateful server has to deal with client crashes. Imagine, for example, a client that opens a file and then crashes. The open() uses up a file descriptor on the server; how can the server know it is OK to close a given file? In normal operation, a client would eventually call close() and thus inform the server that the file should be closed. However, when a client crashes, the server never receives a close(), and thus has to notice the client has crashed in order to close the file.  

For these reasons, the designers of NFS decided to pursue a stateless approach: each client operation contains all the information needed to complete the request. No fancy crash recovery is needed; the server just starts running again, and a client, at worst, might have to retry a request.  

