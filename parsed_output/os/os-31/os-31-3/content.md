# 31.3 Semaphores For Ordering  

Semaphores are also useful to order events in a concurrent program. For example, a thread may wish to wait for a list to become non-empty,  

OPERATINGSYSTEMS[VERSION 1.10]  

1 sem_t s;   
2   
3 void \*child(void \*arg) {   
4 printf("child\n");   
5 sem_post(&s); // signal here: child is done   
6 return NULL;   
7 }   
8   
9 int main(int argc, char \*argv[]) {   
10 sem_init(&s, 0, X); // what should X be?   
11 printf("parent: begin\n");   
12 pthread_t c;   
13 Pthread_create(&c, NULL, child, NULL);   
14 sem_wait(&s); // wait here for child   
15 printf("parent: end\n");   
16 return 0;   
17 }  

so it can delete an element from it. In this pattern of usage, we often find one thread waiting for something to happen, and another thread making that something happen and then signaling that it has happened, thus waking the waiting thread. We are thus using the semaphore as an ordering primitive (similar to our use of condition variables earlier).  

A simple example is as follows. Imagine a thread creates another thread and then wants to wait for it to complete its execution (Figure 31.6). When this program runs, we would like to see the following:  

parent: begin child parent: end  

The question, then, is how to use a semaphore to achieve this effect; as it turns out, the answer is relatively easy to understand. As you can see in the code, the parent simply calls sem wait() and the child sem post() to wait for the condition of the child finishing its execution to become true. However, this raises the question: what should the initial value of this semaphore be?  

(Again, think about it here, instead of reading ahead)  

The answer, of course, is that the value of the semaphore should be set to is 0. There are two cases to consider. First, let us assume that the parent creates the child but the child has not run yet (i.e., it is sitting in a ready queue but not running). In this case (Figure 31.7, page 6), the parent will call sem wait() before the child has called sem post(); we’d like the parent to wait for the child to run. The only way this will happen is if the value of the semaphore is not greater than 0; hence, 0 is the initial value. The parent runs, decrements the semaphore (to -1), then waits (sleeping). When the child finally runs, it will call sem post(), increment the value of the semaphore to 0, and wake the parent, which will then return from sem wait() and finish the program.  

Figure 31.7: Thread Trace: Parent Waiting For Child (Case 1)   


<html><body><table><tr><td>Val</td><td>Parent</td><td>State</td><td>Child</td><td>State</td></tr><tr><td>0 0 -1</td><td>create(Child) call sem.wait () decr sem</td><td>Run Run Run</td><td>(Child exists, can run)</td><td>Ready Ready Ready</td></tr><tr><td>-1 -1</td><td>(sem<0)->sleep Switch->Child</td><td>Sleep Sleep</td><td>child runs</td><td>Ready Run</td></tr><tr><td>-1 0</td><td></td><td>Sleep</td><td>call sem post () inc sem</td><td>Run</td></tr><tr><td>0</td><td></td><td>Sleep</td><td></td><td>Run</td></tr><tr><td>0</td><td></td><td>Ready</td><td>wake(Parent)</td><td>Run</td></tr><tr><td></td><td></td><td>Ready</td><td>sem_post () returns</td><td>Run</td></tr><tr><td>0</td><td></td><td>Ready</td><td>Interrupt->Parent</td><td>Ready</td></tr><tr><td>0</td><td>sem_wait() returns</td><td>Run</td><td></td><td>Ready</td></tr></table></body></html>  

Figure 31.8: Thread Trace: Parent Waiting For Child (Case 2)   


<html><body><table><tr><td>Val</td><td>Parent</td><td>State</td><td>Child</td><td>State</td></tr><tr><td>0</td><td>create(Child) Interrupt->Child</td><td>Run Ready</td><td>(Child exists; can run)</td><td>Ready</td></tr><tr><td>0</td><td rowspan="4"></td><td rowspan="4">Ready Ready</td><td>child runs</td><td>Run</td></tr><tr><td>0</td><td>call sem_post ()</td><td>Run</td></tr><tr><td>1</td><td>inc sem</td><td>Run</td></tr><tr><td>1</td><td>wake(nobody)</td><td>Run</td></tr><tr><td>1</td><td></td><td>Ready Ready</td><td>sem_post () returns</td><td>Run</td></tr><tr><td>1</td><td>parent runs</td><td>Run</td><td>Interrupt->Parent</td><td>Ready</td></tr><tr><td>1</td><td>call sem_wait ()</td><td>Run</td><td></td><td>Ready</td></tr><tr><td>0</td><td>decrement sem</td><td>Run</td><td></td><td> Ready</td></tr><tr><td>0</td><td>(sem>0)->awake</td><td>Run</td><td></td><td>Ready</td></tr><tr><td>0</td><td>sem wait () returns</td><td>Run</td><td></td><td>Ready</td></tr></table></body></html>  

The second case (Figure 31.8) occurs when the child runs to completion before the parent gets a chance to call sem wait(). In this case, the child will first call sem post(), thus incrementing the value of the semaphore from 0 to 1. When the parent then gets a chance to run, it will call sem wait() and find the value of the semaphore to be 1; the parent will thus decrement the value (to 0) and return from sem wait() without waiting, also achieving the desired effect.  

