# 2.3 Concurrency  

1 #include <stdio.h>   
2 #include <stdlib.h>   
3 #include "common.h"   
4 #include "common_threads.h"   
5   
6 volatile int counter $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
7 int loops;   
8   
9 void \*worker(void \*arg) {   
10 int i;   
11 for ( $\mathrm { ~ i ~ } = \mathrm { ~ 0 ~ }$ ; i < loops; ${ \dot { \bf \underline { { 1 } } } } + +$ ) {   
12 counter++;   
13 }   
14 return NULL;   
15 }   
16   
17 int main(int argc, char \*argv[]) {   
18 if (argc ! $\mathbf { \varepsilon } _ { : } = \mathbf { \varepsilon } _ { 2 }$ ) {   
19 fprintf(stderr, "usage: threads <value>\n");   
20 exit(1);   
21 }   
22 loops $\mathbf { \Sigma } =$ atoi(argv[1]);   
23 pthread_t p1, p2;   
24 printf("Initial value : %d\n", counter);   
25   
26 Pthread_create(&p1, NULL, worker, NULL);   
27 Pthread_create(&p2, NULL, worker, NULL);   
28 Pthread_join(p1, NULL);   
29 Pthread_join(p2, NULL);   
30 printf("Final value : %d\n", counter);   
31 return 0;  

Another main theme of this book is concurrency. We use this conceptual term to refer to a host of problems that arise, and must be addressed, when working on many things at once (i.e., concurrently) in the same program. The problems of concurrency arose first within the operating system itself; as you can see in the examples above on virtualization, the OS is juggling many things at once, first running one process, then another, and so forth. As it turns out, doing so leads to some deep and interesting problems.  

Unfortunately, the problems of concurrency are no longer limited just to the OS itself. Indeed, modern multi-threaded programs exhibit the same problems. Let us demonstrate with an example of a multi-threaded program (Figure 2.5).  

Although you might not understand this example fully at the moment (and we’ll learn a lot more about it in later chapters, in the section of the book on concurrency), the basic idea is simple. The main program creates two threads using Pthread create()6. You can think of a thread as a function running within the same memory space as other functions, with more than one of them active at a time. In this example, each thread starts running in a routine called worker(), in which it simply increments a counter in a loop for loops number of times.  

Below is a transcript of what happens when we run this program with the input value for the variable loops set to 1000. The value of loops determines how many times each of the two workers will increment the shared counter in a loop. When the program is run with the value of loops set to 1000, what do you expect the final value of counter to be?  

prompt> gcc -o threads threads.c -Wall -pthread   
prompt> ./threads 1000   
Initial value : 0   
Final value : 2000  

As you probably guessed, when the two threads are finished, the final value of the counter is 2000, as each thread incremented the counter 1000 times. Indeed, when the input value of loops is set to $N _ { \cdot }$ , we would expect the final output of the program to be $2 N$ . But life is not so simple, as it turns out. Let’s run the same program, but with higher values for loops, and see what happens:  

prompt> ./threads 100000   
Initial value : 0   
Final value : 143012 // huh??   
prompt> ./threads 100000   
Initial value : 0   
Final value : 137298 // what the??  

In this run, when we gave an input value of 100,000, instead of getting a final value of 200,000, we instead first get 143,012. Then, when we run the program a second time, we not only again get the wrong value, but also a different value than the last time. In fact, if you run the program over and over with high values of loops, you may find that sometimes you even get the right answer! So why is this happening?  

As it turns out, the reason for these odd and unusual outcomes relate to how instructions are executed, which is one at a time. Unfortunately, a key part of the program above, where the shared counter is incremented,  

THE CRUX OF THE PROBLEM: HOW TO BUILD CORRECT CONCURRENT PROGRAMS When there are many concurrently executing threads within the same memory space, how can we build a correctly working program? What primitives are needed from the OS? What mechanisms should be provided by the hardware? How can we use them to solve the problems of concurrency?  

takes three instructions: one to load the value of the counter from memory into a register, one to increment it, and one to store it back into memory. Because these three instructions do not execute atomically (all at once), strange things can happen. It is this problem of concurrency that we will address in great detail in the second part of this book.  

