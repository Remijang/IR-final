# 5.4 Why? Motivating The API  

Of course, one big question you might have: why would we build such an odd interface to what should be the simple act of creating a new process? Well, as it turns out, the separation of fork() and exec() is essential in building a UNIX shell, because it lets the shell run code after the call to fork() but before the call to exec(); this code can alter the environment of the about-to-be-run program, and thus enables a variety of interesting features to be readily built.  

The shell is just a user program4. It shows you a prompt and then waits for you to type something into it. You then type a command (i.e., the name of an executable program, plus any arguments) into it; in most cases, the shell then figures out where in the file system the executable resides, calls fork() to create a new child process to run the command, calls some variant of exec() to run the command, and then waits for the command to complete by calling wait(). When the child completes, the shell returns from wait() and prints out a prompt again, ready for your next command.  

The separation of fork() and exec() allows the shell to do a whole bunch of useful things rather easily. For example:  

prompt> wc p3.c $>$ newfile.txt  

In the example above, the output of the program wc is redirected into the output file newfile.txt (the greater-than sign is how said redirection is indicated). The way the shell accomplishes this task is quite simple: when the child is created, before calling exec(), the shell (specifically, the code executed in the child process) closes standard output and opens the file newfile.txt. By doing so, any output from the soonto-be-running program wc is sent to the file instead of the screen (open file descriptors are kept open across the exec() call, thus enabling this behavior [SR05]).  

Figure 5.4 (page 8) shows a program that does exactly this. The reason this redirection works is due to an assumption about how the operating system manages file descriptors. Specifically, UNIX systems start looking for free file descriptors at zero. In this case, STDOUT FILENO will be the first available one and thus get assigned when open() is called. Subsequent writes by the child process to the standard output file descriptor, for example by routines such as printf(), will then be routed transparently to the newly-opened file instead of the screen.  

Here is the output of running the p4.c program:  

prompt> ./p4   
prompt> cat p4.output 32 109 846 p4.c   
prompt>  

You’ll notice (at least) two interesting tidbits about this output. First, when $\mathtt { p 4 }$ is run, it looks as if nothing has happened; the shell just prints the command prompt and is immediately ready for your next command. However, that is not the case; the program $\mathtt { p 4 }$ did indeed call fork() to create a new child, and then run the wc program via a call to execvp(). You don’t see any output printed to the screen because it has been redirected to the file $\mathtt { p 4 }$ .output. Second, you can see that when we cat the output file, all the expected output from running wc is found. Cool, right?  

UNIX pipes are implemented in a similar way, but with the pipe() system call. In this case, the output of one process is connected to an inkernel pipe (i.e., queue), and the input of another process is connected to that same pipe; thus, the output of one process seamlessly is used as input to the next, and long and useful chains of commands can be strung together. As a simple example, consider looking for a word in a file, and then counting how many times said word occurs; with pipes and the utilities grep and wc, it is easy; just type grep -o foo file | wc -l into the command prompt and marvel at the result.  

Finally, while we just have sketched out the process API at a high level, there is a lot more detail about these calls out there to be learned and digested; we’ll learn more, for example, about file descriptors when we talk about file systems in the third part of the book. For now, suffice it to say that the fork()/exec() combination is a powerful way to create and manipulate processes.  

1 #include <stdio.h>   
2 #include <stdlib.h>   
3 #include <unistd.h>   
4 #include <string.h>   
5 #include <fcntl.h>   
6 #include <sys/wait.h>   
7   
8 int main(int argc, char \*argv[]) {   
9 int rc $\mathbf { \Sigma } = \mathbf { \Sigma }$ fork();   
10 if (rc < 0) {   
11 // fork failed   
12 fprintf(stderr, "fork failed\n");   
13 exit(1);   
14 } else if $\mathrm { ~ \ : ~ \ : ~ } . \mathrm { ~ \ : ~ \ : ~ c ~ \ : ~ } = = \mathrm { ~ \ : ~ 0 ~ }$ ) {   
15 // child: redirect standard output to a file   
16 close(STDOUT_FILENO);   
17 open("./p4.output", O_CREAT|O_WRONLY|O_TRUNC,   
18 S_IRWXU);   
19 // now exec "wc".   
20 char \*myargs[3];   
21 myargs[0] $\mathbf { \Sigma } = \mathbf { \Sigma }$ strdup("wc"); // program: wc   
22 myargs[1] $\mathbf { \Sigma } = \mathbf { \Sigma }$ strdup("p4.c"); // arg: file to count   
23 myargs[2] $\mathbf { \Sigma } = \mathbf { \Sigma }$ NULL; // mark end of array   
24 execvp(myargs[0], myargs); // runs word count   
25 } else {   
26 // parent goes down this path (main)   
27 int rc_wait $\mathbf { \Sigma } = \mathbf { \Sigma }$ wait(NULL);   
28 }   
29 return 0;   
30 }  

