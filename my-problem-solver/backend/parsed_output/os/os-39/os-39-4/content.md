# 39.4 Reading And Writing Files  

Once we have some files, of course we might like to read or write them. Let’s start by reading an existing file. If we were typing at a command line, we might just use the program cat to dump the contents of the file to the screen.  

prompt> echo hello $>$ foo   
prompt> cat foo   
hello   
prompt>  

In this code snippet, we redirect the output of the program echo to the file foo, which then contains the word “hello” in it. We then use cat to see the contents of the file. But how does the cat program access the file foo?  

To find this out, we’ll use an incredibly useful tool to trace the system calls made by a program. On Linux, the tool is called strace; other systems have similar tools (see dtruss on a Mac, or truss on some older UNIX variants). What strace does is trace every system call made by a program while it runs, and dump the trace to the screen for you to see.  

Here is an example of using strace to figure out what cat is doing (some calls removed for readability):  

prompt> strace cat foo   
open("foo", O_RDONLY|O_LARGEFILE) ${ \begin{array} { r l } { = } & { 3 } \\ { = } & { 6 } \\ { = } & { 6 } \\ { = } & { 0 } \\ { = } & { 0 } \end{array} }$   
read(3, "hello\n", 4096)   
write(1, "hello\n", 6)   
hello   
read(3, "", 4096)   
close(3)   
prompt>  

THREE EASY PIECES  

The first thing that cat does is open the file for reading. A couple of things we should note about this; first, that the file is only opened for reading (not writing), as indicated by the O RDONLY flag; second, that the 64-bit offset is used (O LARGEFILE); third, that the call to open() succeeds and returns a file descriptor, which has the value of 3.  

Why does the first call to open() return 3, not 0 or perhaps 1 as you might expect? As it turns out, each running process already has three files open, standard input (which the process can read to receive input), standard output (which the process can write to in order to dump information to the screen), and standard error (which the process can write error messages to). These are represented by file descriptors 0, 1, and 2, respectively. Thus, when you first open another file (as cat does above), it will almost certainly be file descriptor 3.  

After the open succeeds, cat uses the read() system call to repeatedly read some bytes from a file. The first argument to read() is the file descriptor, thus telling the file system which file to read; a process can of course have multiple files open at once, and thus the descriptor enables the operating system to know which file a particular read refers to. The second argument points to a buffer where the result of the read() will be placed; in the system-call trace above, strace shows the results of the read in this spot (“hello”). The third argument is the size of the buffer, which in this case is $4 \mathrm { K B }$ . The call to read() returns successfully as well, here returning the number of bytes it read (6, which includes 5 for the letters in the word “hello” and one for an end-of-line marker).  

At this point, you see another interesting result of the strace: a single call to the write() system call, to the file descriptor 1. As we mentioned above, this descriptor is known as the standard output, and thus is used to write the word “hello” to the screen as the program cat is meant to do. But does it call write() directly? Maybe (if it is highly optimized). But if not, what cat might do is call the library routine printf(); internally, printf() figures out all the formatting details passed to it, and eventually writes to standard output to print the results to the screen.  

The cat program then tries to read more from the file, but since there are no bytes left in the file, the read() returns 0 and the program knows that this means it has read the entire file. Thus, the program calls close() to indicate that it is done with the file “foo”, passing in the corresponding file descriptor. The file is thus closed, and the reading of it thus complete.  

Writing a file is accomplished via a similar set of steps. First, a file is opened for writing, then the write() system call is called, perhaps repeatedly for larger files, and then close(). Use strace to trace writes to a file, perhaps of a program you wrote yourself, or by tracing the dd utility, e.g., dd if $\mathbf { \bar { \rho } } = \mathbf { \rho }$ foo of $\mathbf { \bar { \rho } } = \mathbf { \bar { \rho } }$ bar.  

OPERATINGSYSTEMS[VERSION 1.10]  

ASIDE: DATA STRUCTURE — THE OPEN FILE TABLE Each process maintains an array of file descriptors, each of which refers to an entry in the system-wide open file table. Each entry in this table tracks which underlying file the descriptor refers to, the current offset, and other relevant details such as whether the file is readable or writable.  

