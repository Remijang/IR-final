# 26.3 Why It Gets Worse: Shared Data  

The simple thread example we showed above was useful in showing how threads are created and how they can run in different orders depending on how the scheduler decides to run them. What it doesn’t show you, though, is how threads interact when they access shared data.  

Let us imagine a simple example where two threads wish to update a global shared variable. The code we’ll study is in Figure 26.6 (page 7).  

Here are a few notes about the code. First, as Stevens suggests [SR05], we wrap the thread creation and join routines to simply exit on failure; for a program as simple as this one, we want to at least notice an error occurred (if it did), but not do anything very smart about it (e.g., just exit). Thus, Pthread create() simply calls pthread create() and makes sure the return code is 0; if it isn’t, Pthread create() just prints a message and exits.  

Second, instead of using two separate function bodies for the worker threads, we just use a single piece of code, and pass the thread an argument (in this case, a string) so we can have each thread print a different letter before its messages.  

Finally, and most importantly, we can now look at what each worker is trying to do: add a number to the shared variable counter, and do so 10 million times (1e7) in a loop. Thus, the desired final result is: 20,000,000.  

We now compile and run the program, to see how it behaves. Sometimes, everything works how we might expect:  

prompt> gcc -o main main.c -Wall -pthread; ./main   
main: begin (counter $\mathit { \Theta } = \mathit { \Theta } 0$ )   
A: begin   
B: begin   
A: done   
B: done   
main: done with both (counter $\mathbf { \Sigma } = \mathbf { \Sigma }$ 20000000)  

OPERATINGSYSTEMS[VERSION 1.10]  

1 #include <stdio.h>   
2 #include <pthread.h>   
3 #include "common.h"   
4 #include "common_threads.h"   
5   
6 static volatile int counter $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
7   
8 // mythread()   
9 //   
10 // Simply adds 1 to counter repeatedly, in a loop   
11 // No, this is not how you would add 10,000,000 to   
12 // a counter, but it shows the problem nicely.   
13 //   
14 void \*mythread(void \*arg) {   
15 printf("%s: begin\n", (char $\star$ ) arg);   
16 int i;   
17 for ( $\mathrm { ~ \bf ~ \underline { ~ } { ~ i ~ } ~ } = \mathrm { ~ \bf ~ 0 ~ }$ ; i < 1e7; $\dot { \bf \underline { { 1 } } } + +$ ) {   
18 counter $\mathbf { \Sigma } =$ counter $\mathbf { \Sigma } + \mathbf { \Sigma } \mathbf { \Sigma } 1$ ;   
19 }   
20 printf("%s: done\n", (char $\star$ ) arg);   
21 return NULL;   
22 }   
23   
24 // main()   
25 //   
26 // Just launches two threads (pthread_create)   
27 // and then waits for them (pthread_join)   
28 //   
29 int main(int argc, char \*argv[]) {   
30 pthread_t p1, p2;   
31 printf("main: begin (counter $\begin{array} { r l } { = } & { { } \frac { 0 } { 0 } \mathrm { d } } \end{array}$ )\n", counter)   
32 Pthread_create(&p1, NULL, mythread, "A");   
33 Pthread_create(&p2, NULL, mythread, "B");   
34   
35 // join waits for the threads to finish   
36 Pthread_join(p1, NULL);   
37 Pthread_join(p2, NULL);   
38 printf("main: done with both (counter $\mathbf { \Sigma } = \mathbf { \Sigma }$ %d)\n",   
39 counter);   
40 return 0;   
41 }  

Unfortunately, when we run this code, even on a single processor, we don’t necessarily get the desired result. Sometimes, we get:  

prompt> ./main   
main: begin (counter $\mathit { \Theta } = \mathit { \Theta } 0$ )   
A: begin   
B: begin   
A: done   
B: done   
main: done with both (counter $\mathbf { \Sigma } = \mathbf { \Sigma }$ 19345221)  

Let’s try it one more time, just to see if we’ve gone crazy. After all, aren’t computers supposed to produce deterministic results, as you have been taught?! Perhaps your professors have been lying to you? (gasp)  

prompt> ./main   
main: begin (counter $\mathit { \Theta } = \mathit { \Theta } 0$ )   
A: begin   
B: begin   
A: done   
B: done   
main: done with both (counter $\mathbf { \Sigma } = \mathbf { \Sigma }$ 19221041)  

Not only is each run wrong, but also yields a different result! A big question remains: why does this happen?  

TIP: KNOW AND USE YOUR TOOLS You should always learn new tools that help you write, debug, and understand computer systems. Here, we use a neat tool called a disassembler. When you run a disassembler on an executable, it shows you what assembly instructions make up the program. For example, if we wish to understand the low-level code to update a counter (as in our example), we run objdump (Linux) to see the assembly code: prompt> objdump -d main Doing so produces a long listing of all the instructions in the program, neatly labeled (particularly if you compiled with the $- \mathfrak { g }$ flag), which includes symbol information in the program. The objdump program is just one of many tools you should learn how to use; a debugger like gdb, memory profilers like valgrind or purify, and of course the compiler itself are others that you should spend time to learn more about; the better you are at using your tools, the better systems you’ll be able to build.  

OPERATINGSYSTEMS[VERSION 1.10]  

