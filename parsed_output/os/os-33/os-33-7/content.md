# 33.7 Another Problem: State Management  

Another issue with the event-based approach is that such code is generally more complicated to write than traditional thread-based code. The reason is as follows: when an event handler issues an asynchronous I/O, it must package up some program state for the next event handler to use when the I/O finally completes; this additional work is not needed in thread-based programs, as the state the program needs is on the stack of the thread. Adya et al. call this work manual stack management, and it is fundamental to event-based programming $\left[ { \mathrm { A } } { + } 0 2 \right]$ .  

To make this point more concrete, let’s look at a simple example in which a thread-based server needs to read from a file descriptor $( \mathrm { f d } )$ and, once complete, write the data that it read from the file to a network socket descriptor $( { \mathrm { s d } } )$ . The code (ignoring error checking) looks like this:  

int rc $\mathbf { \Sigma } = \mathbf { \Sigma }$ read(fd, buffer, size);   
$\mathtt { r c } \ =$ write(sd, buffer, size);  

As you can see, in a multi-threaded program, doing this kind of work is trivial; when the read() finally returns, the code immediately knows which socket to write to because that information is on the stack of the thread (in the variable sd).  

In an event-based system, life is not so easy. To perform the same task, we’d first issue the read asynchronously, using the AIO calls described above. Let’s say we then periodically check for completion of the read using the aio error() call; when that call informs us that the read is complete, how does the event-based server know what to do?  

# ASIDE: UNIX SIGNALS  

A huge and fascinating infrastructure known as signals is present in all modern UNIX variants. At its simplest, signals provide a way to communicate with a process. Specifically, a signal can be delivered to an application; doing so stops the application from whatever it is doing to run a signal handler, i.e., some code in the application to handle that signal. When finished, the process just resumes its previous behavior.  

Each signal has a name, such as HUP (hang up), INT (interrupt), SEGV (segmentation violation), etc.; see the man page for details. Interestingly, sometimes it is the kernel itself that does the signaling. For example, when your program encounters a segmentation violation, the OS sends it a SIGSEGV (prepending SIG to signal names is common); if your program is configured to catch that signal, you can actually run some code in response to this erroneous program behavior (which is helpful for debugging). When a signal is sent to a process not configured to handle a signal, the default behavior is enacted; for SEGV, the process is killed.  

Here is a simple program that goes into an infinite loop, but has first set up a signal handler to catch SIGHUP:  

void handle(int arg) { printf("stop wakin’ me up...\n");   
}   
int main(int argc, char \*argv[]) { signal(SIGHUP, handle); while (1) ; // doin’ nothin’ except catchin’ some sigs return 0;   
}  

You can send signals to it with the kill command line tool (yes, this is an odd and aggressive name). Doing so will interrupt the main while loop in the program and run the handler code handle():  

prompt> ./main & [3] 36705 prompt> kill -HUP 36705 stop wakin’ me up.. prompt> kill -HUP 36705 stop wakin’ me up..  

There is a lot more to learn about signals, so much that a single chapter, much less a single page, does not nearly suffice. As always, there is one great source: Stevens and Rago [SR05]. Read more if interested.  

OPERATINGSYSTEMS[VERSION 1.10]  

The solution, as described by Adya et al. $[ \mathrm { A } { + } 0 2 ] .$ , is to use an old programming language construct known as a continuation [FHK84]. Though it sounds complicated, the idea is rather simple: basically, record the needed information to finish processing this event in some data structure; when the event happens (i.e., when the disk I/O completes), look up the needed information and process the event.  

In this specific case, the solution would be to record the socket descriptor $( { \mathrm { s d } } )$ in some kind of data structure (e.g., a hash table), indexed by the file descriptor (fd). When the disk I/O completes, the event handler would use the file descriptor to look up the continuation, which will return the value of the socket descriptor to the caller. At this point (finally), the server can then do the last bit of work to write the data to the socket.  

