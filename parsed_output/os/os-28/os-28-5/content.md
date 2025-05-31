# 28.5 Controlling Interrupts  

One of the earliest solutions used to provide mutual exclusion was to disable interrupts for critical sections; this solution was invented for single-processor systems. The code would look like this:  

1 void lock() {   
2 DisableInterrupts();   
3 }   
4 void unlock() {   
5 EnableInterrupts();   
6 }  

Assume we are running on such a single-processor system. By turning off interrupts (using some kind of special hardware instruction) before entering a critical section, we ensure that the code inside the critical section will not be interrupted, and thus will execute as if it were atomic. When we are finished, we re-enable interrupts (again, via a hardware instruction) and thus the program proceeds as usual.  

The main positive of this approach is its simplicity. You certainly don’t have to scratch your head too hard to figure out why this works. Without interruption, a thread can be sure that the code it executes will execute and that no other thread will interfere with it.  

The negatives, unfortunately, are many. First, this approach requires us to allow any calling thread to perform a privileged operation (turning interrupts on and off), and thus trust that this facility is not abused. As you already know, any time we are required to trust an arbitrary program, we are probably in trouble. Here, the trouble manifests in numerous ways: a greedy program could call lock() at the beginning of its execution and thus monopolize the processor; worse, an errant or malicious program could call lock() and go into an endless loop. In this latter case, the OS never regains control of the system, and there is only one recourse: restart the system. Using interrupt disabling as a generalpurpose synchronization solution requires too much trust in applications.  

Second, the approach does not work on multiprocessors. If multiple threads are running on different CPUs, and each try to enter the same critical section, it does not matter whether interrupts are disabled; threads will be able to run on other processors, and thus could enter the critical section. As multiprocessors are now commonplace, our general solution will have to do better than this.  

Third, turning off interrupts for extended periods of time can lead to interrupts becoming lost, which can lead to serious systems problems. Imagine, for example, if the CPU missed the fact that a disk device has finished a read request. How will the OS know to wake the process waiting for said read?  

OPERATINGSYSTEMS[VERSION 1.10]  

1 typedef struct __lock_t { int flag; } lock_t;   
2   
3 void init(lock_t \*mutex) {   
4 // 0 -> lock is available, 1 -> held   
5 mutex->flag $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
6 }   
7   
8 void lock(lock_t $\star$ mutex) {   
9 while (mutex->flag $\scriptstyle \mathbf { \alpha = } \ \mathbf { 1 }$ ) // TEST the flag   
10 ; // spin-wait (do nothing)   
11 mutex->flag $\mathit { \Theta } = \mathit { \Theta } 1$ ; // now SET it!   
12 }   
13   
14 void unlock(lock_t $\star$ mutex) {   
15 mutex->flag $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
16 }  

For these reasons, turning off interrupts is only used in limited contexts as a mutual-exclusion primitive. For example, in some cases an operating system itself will use interrupt masking to guarantee atomicity when accessing its own data structures, or at least to prevent certain messy interrupt handling situations from arising. This usage makes sense, as the trust issue disappears inside the OS, which always trusts itself to perform privileged operations anyhow.  

