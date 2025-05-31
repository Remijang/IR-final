# 31.4 The Producer/Consumer (Bounded Buffer) Problem  

The next problem we will confront in this chapter is known as the producer/consumer problem, or sometimes as the bounded buffer problem [D72]. This problem is described in detail in the previous chapter on condition variables; see there for details.  

OPERATINGSYSTEMS[VERSION 1.10]  

ASIDE: SETTING THE VALUE OF A SEMAPHORE  

We’ve now seen two examples of initializing a semaphore. In the first case, we set the value to 1 to use the semaphore as a lock; in the second, to 0, to use the semaphore for ordering. So what’s the general rule for semaphore initialization?  

One simple way to think about it, thanks to Perry Kivolowitz, is to consider the number of resources you are willing to give away immediately after initialization. With the lock, it was 1, because you are willing to have the lock locked (given away) immediately after initialization. With the ordering case, it was 0, because there is nothing to give away at the start; only when the child thread is done is the resource created, at which point, the value is incremented to 1. Try this line of thinking on future semaphore problems, and see if it helps.  

# First Attempt  

Our first attempt at solving the problem introduces two semaphores, empty and full, which the threads will use to indicate when a buffer entry has been emptied or filled, respectively. The code for the put and get routines is in Figure 31.9, and our attempt at solving the producer and consumer problem is in Figure 31.10 (page 8).  

In this example, the producer first waits for a buffer to become empty in order to put data into it, and the consumer similarly waits for a buffer to become filled before using it. Let us first imagine that $\mathrm { M A X = 1 }$ (there is only one buffer in the array), and see if this works.  

Imagine again there are two threads, a producer and a consumer. Let us examine a specific scenario on a single CPU. Assume the consumer gets to run first. Thus, the consumer will hit Line C1 in Figure 31.10, calling sem wait(&full). Because full was initialized to the value 0,  

1 int buffer[MAX];   
2 int $\pounds \mathrm { i } \ 1 1 \ = \ 0 .$ ;   
3 int use $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
4   
5 void put(int value) {   
6 buffer[fill] $\mathbf { \Sigma } = \mathbf { \Sigma }$ value; // Line F1   
7 fill $\mathbf { \Sigma } = \mathbf { \Sigma }$ (fill + 1) % MAX; // Line F2   
8 }   
9   
10 int get() {   
11 int tmp $\mathbf { \Sigma } = \mathbf { \Sigma }$ buffer[use]; // Line G1   
12 use $\mathbf { \Sigma } = \mathbf { \Sigma }$ (use + 1) % MAX; // Line G2   
13 return tmp;   
14 }   
1 sem_t empty;   
2 sem_t full;   
3   
4 void \*producer(void \*arg) {   
5 int i;   
6 for ( $\mathrm { ~ \\ ~ i ~ } = \mathrm { ~ \ ~ 0 ~ }$ ; i < loops; i++) {   
7 sem_wait(&empty); // Line P1   
8 put(i); // Line P2   
9 sem_post(&full); // Line P3   
10 }   
11 }   
12   
13 void $\star$ consumer(void \*arg) {   
14 int tmp $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
15 while (tmp ! $\ : \iota = \ : - 1 \ :$ ) {   
16 sem_wait(&full); // Line C1   
17 tmp $\mathbf { \Sigma } = \mathbf { \Sigma }$ get(); // Line C2   
18 sem_post(&empty); // Line C3   
19 printf("%d\n", tmp);   
20 }   
21 }   
22   
23 int main(int argc, char \*argv[]) {   
24 // ..   
25 sem_init(&empty, 0, MAX); // MAX are empt   
26 sem_init(&full, 0, 0); // 0 are full   
27 //   
28 }  

the call will decrement full (to -1), block the consumer, and wait for another thread to call sem post() on full, as desired.  

Assume the producer then runs. It will hit Line P1, thus calling the sem wait(&empty) routine. Unlike the consumer, the producer will continue through this line, because empty was initialized to the value MAX (in this case, 1). Thus, empty will be decremented to 0 and the producer will put a data value into the first entry of buffer (Line P2). The producer will then continue on to P3 and call sem post(&full), changing the value of the full semaphore from $^ { - 1 }$ to 0 and waking the consumer (e.g., move it from blocked to ready).  

In this case, one of two things could happen. If the producer continues to run, it will loop around and hit Line P1 again. This time, however, it would block, as the empty semaphore’s value is 0. If the producer instead was interrupted and the consumer began to run, it would return from sem wait(&full) (Line C1), find that the buffer was full, and consume it. In either case, we achieve the desired behavior.  

You can try this same example with more threads (e.g., multiple producers, and multiple consumers). It should still work.  

OPERATINGSYSTEMS[VERSION 1.10]  

1 void \*producer(void \*arg) {   
2 int i;   
3 for ( $\mathrm { ~ \ : ~ i ~ } = \mathrm { ~ 0 ~ }$ ; i < loops; i++) {   
4 sem_wait(&mutex); // Line P0 (NEW LINE)   
5 sem_wait(&empty); // Line P1   
6 put(i); // Line P2   
7 sem_post(&full); // Line P3   
8 sem_post(&mutex); // Line P4 (NEW LINE)   
9 }   
10 }   
11   
12 void \*consumer(void \*arg) {   
13 int i;   
14 for ( $\mathrm { ~ \textit ~ { ~ i ~ } ~ } = \mathrm { ~ \textit ~ { ~ 0 ~ } ~ }$ ; i < loops; i++) {   
15 sem_wait(&mutex); // Line C0 (NEW LINE)   
16 sem_wait(&full); // Line C1   
17 int tmp $\mathbf { \Sigma } = \mathbf { \Sigma }$ get(); // Line C2   
18 sem_post(&empty); // Line C3   
19 sem_post(&mutex); // Line C4 (NEW LINE)   
20 printf("%d\n", tmp);   
21 }   
}  

Let us now imagine that MAX is greater than 1 (say $\mathtt { M A X = 1 0 }$ ). For this example, let us assume that there are multiple producers and multiple consumers. We now have a problem: a race condition. Do you see where it occurs? (take some time and look for it) If you can’t see it, here’s a hint: look more closely at the put() and get() code.  

OK, let’s understand the issue. Imagine two producers (Pa and $\mathrm { P b }$ ) both calling into put() at roughly the same time. Assume producer Pa gets to run first, and just starts to fill the first buffer entry $( \pm \mathrm { i } 1 1 = 0$ at Line F1). Before Pa gets a chance to increment the fill counter to 1, it is interrupted. Producer Pb starts to run, and at Line F1 it also puts its data into the 0th element of buffer, which means that the old data there is overwritten! This action is a no-no; we don’t want any data from the producer to be lost.  

# A Solution: Adding Mutual Exclusion  

As you can see, what we’ve forgotten here is mutual exclusion. The filling of a buffer and incrementing of the index into the buffer is a critical section, and thus must be guarded carefully. So let’s use our friend the binary semaphore and add some locks. Figure 31.11 shows our attempt.  

Now we’ve added some locks around the entire $\mathrm { { p u t } ( ) / \mathrm { { g e t } ( ) } }$ parts of the code, as indicated by the NEW LINE comments. That seems like the right idea, but it also doesn’t work. Why? Deadlock. Why does deadlock occur? Take a moment to consider it; try to find a case where deadlock arises. What sequence of steps must happen for the program to deadlock?  

1 void \*producer(void \*arg) {   
2 int i;   
3 for ( $\mathbf { \partial } _ { \cdot } \dot { \mathbf { 1 } } \ = \ 0$ ; i < loops; i++) {   
4 sem_wait(&empty); // Line P1   
5 sem_wait(&mutex); // Line P1.5 (lock)   
6 put(i); // Line P2   
7 sem_post(&mutex); // Line P2.5 (unlock)   
8 sem_post(&full); // Line P3   
9 }   
10 }   
11   
12 void \*consumer(void \*arg) {   
13 int i;   
14 for ( $\mathbf { \partial } \cdot \dot { \bf 1 } \ = \ 0$ ; i < loops; i++) {   
15 sem_wait(&full); // Line C1   
16 sem_wait(&mutex); // Line C1.5 (lock)   
17 int tmp $\mathbf { \Sigma } = \mathbf { \Sigma }$ get(); // Line C2   
18 sem_post(&mutex); // Line C2.5 (unlock)   
19 sem_post(&empty); // Line C3   
20 printf("%d\n", tmp);   
21 }   
22 }  

# Avoiding Deadlock  

OK, now that you figured it out, here is the answer. Imagine two threads, one producer and one consumer. The consumer gets to run first. It acquires the mutex (Line C0), and then calls sem wait() on the full semaphore (Line C1); because there is no data yet, this call causes the consumer to block and thus yield the CPU; importantly, though, the consumer still holds the lock.  

A producer then runs. It has data to produce and if it were able to run, it would be able to wake the consumer thread and all would be good. Unfortunately, the first thing it does is call sem wait() on the binary mutex semaphore (Line P0). The lock is already held. Hence, the producer is now stuck waiting too.  

There is a simple cycle here. The consumer holds the mutex and is waiting for the someone to signal full. The producer could signal full but is waiting for the mutex. Thus, the producer and consumer are each stuck waiting for each other: a classic deadlock.  

# At Last, A Working Solution  

To solve this problem, we simply must reduce the scope of the lock. Figure 31.12 (page 10) shows the correct solution. As you can see, we simply move the mutex acquire and release to be just around the critical section;  

OPERATINGSYSTEMS[VERSION 1.10]  

the full and empty wait and signal code is left outside2. The result is a simple and working bounded buffer, a commonly-used pattern in multithreaded programs. Understand it now; use it later. You will thank us for years to come. Or at least, you will thank us when the same question is asked on the final exam, or during a job interview.  

