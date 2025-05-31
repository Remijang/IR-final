# 28.12 Too Much Spinning: What Now?  

Our hardware-based locks are simple (only a few lines of code) and they work (you could even prove that if you’d like to, by writing some code), which are two excellent properties of any system or code. However, in some cases, these solutions can be quite inefficient. Imagine you are running two threads on a single processor. Now imagine that one thread (thread 0) is in a critical section and thus has a lock held, and unfortunately gets interrupted. The second thread (thread 1) now tries to acquire the lock, but finds that it is held. Thus, it begins to spin. And spin. Then it spins some more. And finally, a timer interrupt goes off, thread 0 is run again, which releases the lock, and finally (the next time  

1 typedef struct __lock_t {   
2 int ticket;   
3 int turn;   
4 } lock_t;   
5   
6 void lock_init(lock_t \*lock) {   
7 lock->ticket $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
8 lock->turn = 0;   
9 }   
10   
11 void lock(lock_t \*lock) {   
12 int myturn $\mathbf { \tau } = \mathbf { \tau }$ FetchAndAdd(&lock->ticket);   
13 while (lock->turn ! $\mathbf { \Sigma } = \mathbf { \Sigma }$ myturn)   
14 ; // spin   
15 }   
16   
17 void unlock(lock_t \*lock) {   
18 lock->turn $\mathbf { \Sigma } = \mathbf { \Sigma }$ lock->turn + 1;   
19 }  

it runs, say), thread 1 won’t have to spin so much and will be able to acquire the lock. Thus, any time a thread gets caught spinning in a situation like this, it wastes an entire time slice doing nothing but checking a value that isn’t going to change! The problem gets worse with $N$ threads contending for a lock; $N - \bar { 1 }$ time slices may be wasted in a similar manner, simply spinning and waiting for a single thread to release the lock. And thus, our next problem:  

THE CRUX: HOW TO AVOID SPINNING  

How can we develop a lock that doesn’t needlessly waste time spinning on the CPU?  

Hardware support alone cannot solve the problem. We’ll need OS support too! Let’s now figure out just how that might work.  

