# 33.2 An Important API: select() (or poll())  

With that basic event loop in mind, we next must address the question of how to receive events. In most systems, a basic API is available, via either the select() or poll() system calls.  

What these interfaces enable a program to do is simple: check whether there is any incoming I/O that should be attended to. For example, imagine that a network application (such as a web server) wishes to check whether any network packets have arrived, in order to service them. These system calls let you do exactly that.  

Take select() for example. The manual page (on a Mac) describes the API in this manner:  

int select(int nfds, fd_set $\star$ restrict readfds, fd_set $\star$ restrict writefds, fd_set \*restrict errorfds, struct timeval \*restrict timeout);  

The actual description from the man page: select() examines the I/O descriptor sets whose addresses are passed in readfds, writefds, and errorfds to see  

OPERATINGSYSTEMS[VERSION 1.10]  

ASIDE: BLOCKING VS. NON-BLOCKING INTERFACES Blocking (or synchronous) interfaces do all of their work before returning to the caller; non-blocking (or asynchronous) interfaces begin some work but return immediately, thus letting whatever work that needs to be done get done in the background.  

The usual culprit in blocking calls is I/O of some kind. For example, if a call must read from disk in order to complete, it might block, waiting for the I/O request that has been sent to the disk to return.  

Non-blocking interfaces can be used in any style of programming (e.g., with threads), but are essential in the event-based approach, as a call that blocks will halt all progress.  

if some of their descriptors are ready for reading, are ready for writing, or have an exceptional condition pending, respectively. The first nfds descriptors are checked in each set, i.e., the descriptors from 0 through nfds-1 in the descriptor sets are examined. On return, select() replaces the given descriptor sets with subsets consisting of those descriptors that are ready for the requested operation. select() returns the total number of ready descriptors in all the sets.  

A couple of points about select(). First, note that it lets you check whether descriptors can be read from as well as written to; the former lets a server determine that a new packet has arrived and is in need of processing, whereas the latter lets the service know when it is OK to reply (i.e., the outbound queue is not full).  

Second, note the timeout argument. One common usage here is to set the timeout to NULL, which causes select() to block indefinitely, until some descriptor is ready. However, more robust servers will usually specify some kind of timeout; one common technique is to set the timeout to zero, and thus use the call to select() to return immediately.  

The poll() system call is quite similar. See its manual page, or Stevens and Rago [SR05], for details.  

Either way, these basic primitives give us a way to build a non-blocking event loop, which simply checks for incoming packets, reads from sockets with messages upon them, and replies as needed.  

