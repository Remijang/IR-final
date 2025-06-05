# 10.2 Don’t Forget Synchronization  

Given that the caches do all of this work to provide coherence, do programs (or the OS itself) have to worry about anything when they access shared data? The answer, unfortunately, is yes, and is documented in great detail in the second piece of this book on the topic of concurrency. While we won’t get into the details here, we’ll sketch/review some of the basic ideas here (assuming you’re familiar with concurrency).  

When accessing (and in particular, updating) shared data items or structures across CPUs, mutual exclusion primitives (such as locks) should likely be used to guarantee correctness (other approaches, such as building lock-free data structures, are complex and only used on occasion; see the chapter on deadlock in the piece on concurrency for details). For example, assume we have a shared queue being accessed on multiple CPUs concurrently. Without locks, adding or removing elements from the queue concurrently will not work as expected, even with the underlying coherence protocols; one needs locks to atomically update the data structure to its new state.  

To make this more concrete, imagine this code sequence, which is used to remove an element from a shared linked list, as we see in Figure 10.3. Imagine if threads on two CPUs enter this routine at the same time. If  

OPERATINGSYSTEMS[VERSION 1.10]  

1 typedef struct __Node_t {   
2 int value;   
3 struct __Node_t \*next;   
4 } Node_t;   
5   
6 int List_Pop() {   
7 Node_t \*tmp $\mathbf { \Sigma } = \mathbf { \Sigma }$ head; // remember old head   
8 int value $\mathbf { \Sigma } = \mathbf { \Sigma }$ head->value; // ... and its value   
9 head $\mathbf { \Sigma } = \mathbf { \Sigma }$ head->next; // advance to next   
10 free(tmp); // free old head   
11 return value; // return value @head   
12 }  

Thread 1 executes the first line, it will have the current value of head stored in its tmp variable; if Thread 2 then executes the first line as well, it also will have the same value of head stored in its own private tmp variable (tmp is allocated on the stack, and thus each thread will have its own private storage for it). Thus, instead of each thread removing an element from the head of the list, each thread will try to remove the same head element, leading to all sorts of problems (such as an attempted double free of the head element at Line 10, as well as potentially returning the same data value twice).  

The solution, of course, is to make such routines correct via locking. In this case, allocating a simple mutex (e.g., pthread mutex t m;) and then adding a lock(&m) at the beginning of the routine and an unlock(&m) at the end will solve the problem, ensuring that the code will execute as desired. Unfortunately, as we will see, such an approach is not without problems, in particular with regards to performance. Specifically, as the number of CPUs grows, access to a synchronized shared data structure becomes quite slow.  

