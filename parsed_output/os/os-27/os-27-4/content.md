# 27.4 Condition Variables  

The other major component of any threads library, and certainly the case with POSIX threads, is the presence of a condition variable. Condition variables are useful when some kind of signaling must take place between threads, if one thread is waiting for another to do something before it can continue. Two primary routines are used by programs wishing to interact in this way:  

int pthread_cond_wait(pthread_cond_t \*cond, pthread_mutex_t \*mutex); int pthread_cond_signal(pthread_cond_t \*cond);  

To use a condition variable, one has to in addition have a lock that is associated with this condition. When calling either of the above routines, this lock should be held.  

The first routine, pthread cond wait(), puts the calling thread to sleep, and thus waits for some other thread to signal it, usually when something in the program has changed that the now-sleeping thread might care about. A typical usage looks like this:  

pthread_mutex_t lock $\mathbf { \Sigma } = \mathbf { \Sigma }$ PTHREAD_MUTEX_INITIALIZER;   
pthread_cond_t cond $\mathbf { \Sigma } = \mathbf { \Sigma }$ PTHREAD_COND_INITIALIZER;   
Pthread_mutex_lock(&lock);   
while (ready $\scriptstyle \mathbf { \mu } = \mathbf { \mu } 0$ ) Pthread_cond_wait(&cond, &lock);   
Pthread_mutex_unlock(&lock);  

In this code, after initialization of the relevant lock and condition3, a thread checks to see if the variable ready has yet been set to something other than zero. If not, the thread simply calls the wait routine in order to sleep until some other thread wakes it.  

The code to wake a thread, which would run in some other thread, looks like this:  

Pthread_mutex_lock(&lock);   
ready $\mathbf { \Sigma } = \mathbf { \Sigma } 1$ ;   
Pthread_cond_signal(&cond);   
Pthread_mutex_unlock(&lock);  

A few things to note about this code sequence. First, when signaling (as well as when modifying the global variable ready), we always make sure to have the lock held. This ensures that we don’t accidentally introduce a race condition into our code.  

Second, you might notice that the wait call takes a lock as its second parameter, whereas the signal call only takes a condition. The reason for this difference is that the wait call, in addition to putting the calling thread to sleep, releases the lock when putting said caller to sleep. Imagine if it did not: how could the other thread acquire the lock and signal it to wake up? However, before returning after being woken, the pthread cond wait() re-acquires the lock, thus ensuring that any time the waiting thread is running between the lock acquire at the beginning of the wait sequence, and the lock release at the end, it holds the lock.  

One last oddity: the waiting thread re-checks the condition in a while loop, instead of a simple if statement. We’ll discuss this issue in detail when we study condition variables in a future chapter, but in general, using a while loop is the simple and safe thing to do. Although it rechecks the condition (perhaps adding a little overhead), there are some pthread implementations that could spuriously wake up a waiting thread; in such a case, without rechecking, the waiting thread will continue thinking that the condition has changed even though it has not. It is safer thus to view waking up as a hint that something might have changed, rather than an absolute fact.  

Note that sometimes it is tempting to use a simple flag to signal between two threads, instead of a condition variable and associated lock. For example, we could rewrite the waiting code above to look more like this in the waiting code:  

while (ready $\scriptstyle \mathbf { \mu } = \mathbf { \mu } 0$ ) ; // spin  

The associated signaling code would look like this: ready $\mathbf { \Sigma } = \mathbf { \Sigma } 1$ ;  

Don’t ever do this, for the following reasons. First, it performs poorly in many cases (spinning for a long time just wastes CPU cycles). Second, it is error prone. As recent research shows $\left[ \mathsf { X } { + } 1 0 \right]$ , it is surprisingly easy to make mistakes when using flags (as above) to synchronize between threads; in that study, roughly half the uses of these ad hoc synchronizations were buggy! Don’t be lazy; use condition variables even when you think you can get away without doing so.  

If condition variables sound confusing, don’t worry too much (yet) – we’ll be covering them in great detail in a subsequent chapter. Until then, it should suffice to know that they exist and to have some idea how and why they are used.  

