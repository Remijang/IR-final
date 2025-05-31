# 32.2 Non-Deadlock Bugs  

Non-deadlock bugs make up a majority of concurrency bugs, according to Lu’s study. But what types of bugs are these? How do they arise? How can we fix them? We now discuss the two major types of nondeadlock bugs found by Lu et al.: atomicity violation bugs and order violation bugs.  

# Atomicity-Violation Bugs  

The first type of problem encountered is referred to as an atomicity violation. Here is a simple example, found in MySQL. Before reading the explanation, try figuring out what the bug is. Do it!  

1 Thread 1::   
2 if (thd->proc_info) {   
3 fputs(thd->proc_info, ...);   
4 }   
5   
6 Thread 2::   
7 thd->proc_info $\mathbf { \Sigma } = \mathbf { \Sigma }$ NULL;  

In the example, two different threads access the field proc info in the structure thd. The first thread checks if the value is non-NULL and then prints its value; the second thread sets it to NULL. Clearly, if the first thread performs the check but then is interrupted before the call to fputs, the second thread could run in-between, thus setting the pointer to NULL; when the first thread resumes, it will crash, as a NULL pointer will be dereferenced by fputs.  

OPERATINGSYSTEMS[VERSION 1.10]  

The more formal definition of an atomicity violation, according to Lu et al, is this: “The desired serializability among multiple memory accesses is violated (i.e. a code region is intended to be atomic, but the atomicity is not enforced during execution).” In our example above, the code has an atomicity assumption (in Lu’s words) about the check for non-NULL of proc info and the usage of proc info in the fputs() call; when the assumption is incorrect, the code will not work as desired.  

Finding a fix for this type of problem is often (but not always) straightforward. Can you think of how to fix the code above?  

In this solution (Figure 32.3), we simply add locks around the sharedvariable references, ensuring that when either thread accesses the proc info field, it has a lock held (proc info lock). Of course, any other code that accesses the structure should also acquire this lock before doing so.  

1 pthread_mutex_t proc_info_lock $\mathbf { \Sigma } = \mathbf { \Sigma }$ PTHREAD_MUTEX_INITIALIZER;   
2   
3 Thread 1::   
4 pthread_mutex_lock(&proc_info_lock);   
5 if (thd->proc_info) {   
6 fputs(thd->proc_info, ...);   
7 }   
8 pthread_mutex_unlock(&proc_info_lock);   
9   
10 Thread 2::   
11 pthread_mutex_lock(&proc_info_lock);   
12 thd->proc_info $\mathbf { \Sigma } = \mathbf { \Sigma }$ NULL;   
13 pthread_mutex_unlock(&proc_info_lock);  

# Order-Violation Bugs  

Another common type of non-deadlock bug found by Lu et al. is known as an order violation. Here is another simple example; once again, see if you can figure out why the code below has a bug in it.  

1 Thread 1::   
2 void init() {   
3 mThread $\mathbf { \Sigma } = \mathbf { \Sigma }$ PR_CreateThread(mMain, ...);   
4 }   
5   
6 Thread 2::   
7 void mMain(...) {   
8 mState $\mathbf { \tau } = \mathbf { \tau }$ mThread- $\cdot >$ State;   
9 }  

As you probably figured out, the code in Thread 2 seems to assume that the variable mThread has already been initialized (and is not NULL);  

1 pthread_mutex_t mtLock $\mathbf { \Sigma } = \mathbf { \Sigma }$ PTHREAD_MUTEX_INITIALIZ   
2 pthread_cond_t mtCond $\mathbf { \Sigma } = \mathbf { \Sigma }$ PTHREAD_COND_INITIALIZE   
3 int mtInit $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
4   
5 Thread 1::   
6 void init() {   
7   
8 mThread $\mathbf { \Sigma } = \mathbf { \Sigma }$ PR_CreateThread(mMain, ...);   
9   
10 // signal that the thread has been created..   
11 pthread_mutex_lock(&mtLock);   
12 mtInit $\mathbf { \Sigma } = \mathbf { \Sigma } \mathbf { 1 }$ ;   
13 pthread_cond_signal(&mtCond);   
14 pthread_mutex_unlock(&mtLock);   
15   
16 }   
17   
18 Thread 2::   
19 void mMain(...) {   
20   
21 // wait for the thread to be initialized..   
22 pthread_mutex_lock(&mtLock);   
23 while (mtInit $\scriptstyle \mathbf { \mu } = \mathbf { \mu } 0$ )   
24 pthread_cond_wait(&mtCond, &mtLock);   
25 pthread_mutex_unlock(&mtLock);   
26   
27 mState $\mathbf { \Sigma } = \mathbf { \Sigma }$ mThread->State;   
28   
29 }  

however, if Thread 2 runs immediately once created, the value of mThread will not be set when it is accessed within mMain() in Thread 2, and will likely crash with a NULL-pointer dereference. Note that we assume the value of mThread is initially NULL; if not, even stranger things could happen as arbitrary memory locations are accessed through the dereference in Thread 2.  

The more formal definition of an order violation is the following: “The desired order between two (groups of) memory accesses is flipped (i.e., $A$ should always be executed before $B$ , but the order is not enforced during execution)” $\left[ \mathrm { L } { + } 0 8 \right]$ .  

The fix to this type of bug is generally to enforce ordering. As discussed previously, using condition variables is an easy and robust way to add this style of synchronization into modern code bases. In the example above, we could thus rewrite the code as seen in Figure 32.5.  

In this fixed-up code sequence, we have added a condition variable (mtCond) and corresponding lock (mtLock), as well as a state variable  

OPERATINGSYSTEMS[VERSION 1.10]  

(mtInit). When the initialization code runs, it sets the state of mtInit to 1 and signals that it has done so. If Thread 2 had run before this point, it will be waiting for this signal and corresponding state change; if it runs later, it will check the state and see that the initialization has already occurred (i.e., mtInit is set to 1), and thus continue as is proper. Note that we could likely use mThread as the state variable itself, but do not do so for the sake of simplicity here. When ordering matters between threads, condition variables (or semaphores) can come to the rescue.  

# Non-Deadlock Bugs: Summary  

A large fraction $( 9 7 \% )$ of non-deadlock bugs studied by Lu et al. are either atomicity or order violations. Thus, by carefully thinking about these types of bug patterns, programmers can likely do a better job of avoiding them. Moreover, as more automated code-checking tools develop, they should likely focus on these two types of bugs as they constitute such a large fraction of non-deadlock bugs found in deployment.  

Unfortunately, not all bugs are as easily fixed as the examples we looked at above. Some require a deeper understanding of what the program is doing, or a larger amount of code or data structure reorganization to fix. Read Lu et al.’s excellent (and readable) paper for more details.  

