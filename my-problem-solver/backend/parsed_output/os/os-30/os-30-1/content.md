# 30.1 Definition and Routines  

To wait for a condition to become true, a thread can make use of what is known as a condition variable. A condition variable is an explicit queue that threads can put themselves on when some state of execution (i.e., some condition) is not as desired (by waiting on the condition); some other thread, when it changes said state, can then wake one (or more) of those waiting threads and thus allow them to continue (by signaling on the condition). The idea goes back to Dijkstra’s use of “private semaphores” [D68]; a similar idea was later named a “condition variable” by Hoare in his work on monitors [H74].  

To declare such a condition variable, one simply writes something like this: pthread cond t c;, which declares $\mathrm { ~ \varsigma ~ } _ { \mathrm { ~ C ~ } }$ as a condition variable (note: proper initialization is also required). A condition variable has two operations associated with it: wait() and signal(). The wait() call is executed when a thread wishes to put itself to sleep; the signal() call  

OPERATINGSYSTEMS[VERSION 1.10]  

1 int done $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
2 pthread_mutex_t m $\mathbf { \tau } = \mathbf { \tau }$ PTHREAD_MUTEX_INITIALIZE   
3 pthread_cond_t c $\mathbf { \Sigma } = \mathbf { \Sigma }$ PTHREAD_COND_INITIALIZER   
4   
5 void thr_exit() {   
6 Pthread_mutex_lock(&m);   
7 done $\mathbf { \Sigma } = \mathbf { \Sigma } 1$ ;   
8 Pthread_cond_signal(&c);   
9 Pthread_mutex_unlock(&m);   
10 }   
11   
12 void \*child(void \*arg) {   
13 printf("child\n");   
14 thr_exit();   
15 return NULL;   
16 }   
17   
18 void thr_join() {   
19 Pthread_mutex_lock(&m);   
20 while (done $\scriptstyle = = 0$ )   
21 Pthread_cond_wait(&c, &m);   
22 Pthread_mutex_unlock(&m);   
23 }   
24   
25 int main(int argc, char \*argv[]) {   
26 printf("parent: begin\n");   
27 pthread_t p;   
28 Pthread_create(&p, NULL, child, NULL);   
29 thr_join();   
30 printf("parent: end\n");   
31 return 0;   
32 }  

# Figure 30.3: Parent Waiting For Child: Use A Condition Variable  

is executed when a thread has changed something in the program and thus wants to wake a sleeping thread waiting on this condition. Specifically, the POSIX calls look like this:  

pthread_cond_wait(pthread_cond_t \*c, pthread_mutex_t $\star \mathfrak { m }$ );   
pthread_cond_signal(pthread_cond_t $\star { \mathsf { C } }$ );  

We will often refer to these as wait() and signal() for simplicity. One thing you might notice about the wait() call is that it also takes a mutex as a parameter; it assumes that this mutex is locked when wait() is called. The responsibility of wait() is to release the lock and put the calling thread to sleep (atomically); when the thread wakes up (after some other thread has signaled it), it must re-acquire the lock before returning to the caller. This complexity stems from the desire to prevent certain race conditions from occurring when a thread is trying to put itself to sleep. Let’s take a look at the solution to the join problem (Figure 30.3) to understand this better.  

There are two cases to consider. In the first, the parent creates the child thread but continues running itself (assume we have only a single processor) and thus immediately calls into thr join() to wait for the child thread to complete. In this case, it will acquire the lock, check if the child is done (it is not), and put itself to sleep by calling wait() (hence releasing the lock). The child will eventually run, print the message “child”, and call thr exit() to wake the parent thread; this code just grabs the lock, sets the state variable done, and signals the parent thus waking it. Finally, the parent will run (returning from wait() with the lock held), unlock the lock, and print the final message “parent: end”.  

In the second case, the child runs immediately upon creation, sets done to 1, calls signal to wake a sleeping thread (but there is none, so it just returns), and is done. The parent then runs, calls thr join(), sees that done is 1, and thus does not wait and returns.  

One last note: you might observe the parent uses a while loop instead of just an if statement when deciding whether to wait on the condition. While this does not seem strictly necessary per the logic of the program, it is always a good idea, as we will see below.  

To make sure you understand the importance of each piece of the thr exit() and thr join() code, let’s try a few alternate implementations. First, you might be wondering if we need the state variable done. What if the code looked like the example below? (Figure 30.4)  

Unfortunately this approach is broken. Imagine the case where the child runs immediately and calls thr exit() immediately; in this case, the child will signal, but there is no thread asleep on the condition. When the parent runs, it will simply call wait and be stuck; no thread will ever wake it. From this example, you should appreciate the importance of the state variable done; it records the value the threads are interested in knowing. The sleeping, waking, and locking all are built around it.  

1 void thr_exit() {   
2 Pthread_mutex_lock(&m);   
3 Pthread_cond_signal(&c);   
4 Pthread_mutex_unlock(&m);   
5 }   
6   
7 void thr_join() {   
8 Pthread_mutex_lock(&m);   
9 Pthread_cond_wait(&c, &m);   
10 Pthread_mutex_unlock(&m);   
11 }  

Figure 30.4: Parent Waiting: No State Variable  

OPERATINGSYSTEMS[VERSION 1.10]  

1 void thr_exit() {   
2 done $\mathbf { \Sigma } = \mathbf { \Sigma } 1$ ;   
3 Pthread_cond_signal(&c);   
4 }   
5   
6 void thr_join() {   
7 if (done $\scriptstyle \mathbf { \mu } = \mathbf { \mu } 0$ )   
8 Pthread_cond_wait(&c);   
9 }  

Here (Figure 30.5) is another poor implementation. In this example, we imagine that one does not need to hold a lock in order to signal and wait. What problem could occur here? Think about it1!  

The issue here is a subtle race condition. Specifically, if the parent calls thr join() and then checks the value of done, it will see that it is 0 and thus try to go to sleep. But just before it calls wait to go to sleep, the parent is interrupted, and the child runs. The child changes the state variable done to 1 and signals, but no thread is waiting and thus no thread is woken. When the parent runs again, it sleeps forever, which is sad.  

Hopefully, from this simple join example, you can see some of the basic requirements of using condition variables properly. To make sure you understand, we now go through a more complicated example: the producer/consumer or bounded-buffer problem.  

TIP: ALWAYS HOLD THE LOCK WHILE SIGNALING Although it is strictly not necessary in all cases, it is likely simplest and best to hold the lock while signaling when using condition variables. The example above shows a case where you must hold the lock for correctness; however, there are some other cases where it is likely OK not to, but probably is something you should avoid. Thus, for simplicity, hold the lock when calling signal.  

The converse of this tip, i.e., hold the lock when calling wait, is not just a tip, but rather mandated by the semantics of wait, because wait always (a) assumes the lock is held when you call it, (b) releases said lock when putting the caller to sleep, and (c) re-acquires the lock just before returning. Thus, the generalization of this tip is correct: hold the lock when calling signal or wait, and you will always be in good shape.  

1 int buffer;   
2 int count $\mathit { \Theta } = \mathit { \Theta } 0$ ; // initially, empty   
3   
4 void put(int value) {   
5 assert(count $\scriptstyle = = 0$ );   
6 count $\mathit { \Theta } = \mathit { \Theta } 1$ ;   
7 buffer $\mathbf { \Sigma } = \mathbf { \Sigma }$ value;   
8 }   
9   
10 int get() {   
11 assert(count $\scriptstyle \mathbf { \alpha = } \ 1$ );   
12 count $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
13 return buffer;   
14 }  

30.2 The Producer/Consumer (Bounded Buffer) Problem  

The next synchronization problem we will confront in this chapter is known as the producer/consumer problem, or sometimes as the bounded buffer problem, which was first posed by Dijkstra [D72]. Indeed, it was this very producer/consumer problem that led Dijkstra and his co-workers to invent the generalized semaphore (which can be used as either a lock or a condition variable) [D01]; we will learn more about semaphores later.  

Imagine one or more producer threads and one or more consumer threads. Producers generate data items and place them in a buffer; consumers grab said items from the buffer and consume them in some way.  

This arrangement occurs in many real systems. For example, in a multi-threaded web server, a producer puts HTTP requests into a work queue (i.e., the bounded buffer); consumer threads take requests out of this queue and process them.  

A bounded buffer is also used when you pipe the output of one program into another, e.g., grep foo file.txt | wc $- 1$ . This example runs two processes concurrently; grep writes lines from file.txt with the string foo in them to what it thinks is standard output; the UNIX shell redirects the output to what is called a UNIX pipe (created by the pipe system call). The other end of this pipe is connected to the standard input of the process wc, which simply counts the number of lines in the input stream and prints out the result. Thus, the grep process is the producer; the wc process is the consumer; between them is an in-kernel bounded buffer; you, in this example, are just the happy user.  

Because the bounded buffer is a shared resource, we must of course require synchronized access to it, lest2 a race condition arise. To begin to understand this problem better, let us examine some actual code.  

The first thing we need is a shared buffer, into which a producer puts data, and out of which a consumer takes data. Let’s just use a single  

1 void \*producer(void \*arg) {   
2 int i;   
3 int loops $\mathbf { \Sigma } = \mathbf { \Sigma }$ (int) arg;   
4 for ( $\textrm { \scriptsize ( i ) } = \textrm { \scriptsize 0 }$ ; i < loops; ${ \dot { \bf \underline { { 1 } } } } + +$ ) {   
5 put(i);   
6 }   
7 }   
8   
9 void \*consumer(void \*arg) {   
10 while (1) {   
11 int tmp $\mathbf { \tau } = \mathbf { \tau }$ get();   
12 printf("%d\n", tmp);   
13 }   
14 }  

integer for simplicity (you can certainly imagine placing a pointer to a data structure into this slot instead), and the two inner routines to put a value into the shared buffer, and to get a value out of the buffer. See Figure 30.6 (page 6) for details.  

Pretty simple, no? The put() routine assumes the buffer is empty (and checks this with an assertion), and then simply puts a value into the shared buffer and marks it full by setting count to 1. The get() routine does the opposite, setting the buffer to empty (i.e., setting count to 0) and returning the value. Don’t worry that this shared buffer has just a single entry; later, we’ll generalize it to a queue that can hold multiple entries, which will be even more fun than it sounds.  

Now we need to write some routines that know when it is OK to access the buffer to either put data into it or get data out of it. The conditions for this should be obvious: only put data into the buffer when count is zero (i.e., when the buffer is empty), and only get data from the buffer when count is one (i.e., when the buffer is full). If we write the synchronization code such that a producer puts data into a full buffer, or a consumer gets data from an empty one, we have done something wrong (and in this code, an assertion will fire).  

This work is going to be done by two types of threads, one set of which we’ll call the producer threads, and the other set which we’ll call consumer threads. Figure 30.7 shows the code for a producer that puts an integer into the shared buffer loops number of times, and a consumer that gets the data out of that shared buffer (forever), each time printing out the data item it pulled from the shared buffer.  

# A Broken Solution  

Now imagine that we have just a single producer and a single consumer. Obviously the put() and get() routines have critical sections within them, as put() updates the buffer, and get() reads from it. However, putting a lock around the code doesn’t work; we need something more.  

1 int loops; // must initialize somewhere..   
2 cond_t cond;   
3 mutex_t mutex;   
4   
5 void \*producer(void \*arg) {   
6 int i;   
7 for ( $\mathrm { ~ \\ ~ \underline { ~ } { ~ i ~ } ~ } = \mathrm { ~ \ 0 ~ }$ ; i < loops; $\dot { \bf \underline { { 1 } } } + +$ ) {   
8 Pthread_mutex_lock(&mutex); // p1   
9 if (count $\scriptstyle \mathbf { \alpha = } \ 1$ ) // p2   
10 Pthread_cond_wait(&cond, &mutex); // p3   
11 put(i); // p4   
12 Pthread_cond_signal(&cond); // p5   
13 Pthread_mutex_unlock(&mutex); // p6   
14 }   
15 }   
16   
17 void $\star$ consumer(void \*arg) {   
18 int i;   
19 for ( $\mathrm { ~ \\ ~ i ~ } = \mathrm { ~ \ ~ 0 ~ }$ ; i < loops; $\dot { 1 } + +$ ) {   
20 Pthread_mutex_lock(&mutex); // c1   
21 if (count $\scriptstyle \mathbf { \mu } = \mathbf { \mu } 0$ ) // c2   
22 Pthread_cond_wait(&cond, &mutex); // c3   
23 int tmp $\mathbf { \Sigma } = \mathbf { \Sigma }$ get(); // c4   
24 Pthread_cond_signal(&cond); // c5   
25 Pthread_mutex_unlock(&mutex); // c6   
26 printf("%d\n", tmp);   
27 }   
28 }  

Not surprisingly, that something more is some condition variables. In this (broken) first try (Figure 30.8), we have a single condition variable cond and associated lock mutex.  

Let’s examine the signaling logic between producers and consumers. When a producer wants to fill the buffer, it waits for it to be empty (p1– p3). The consumer has the exact same logic, but waits for a different condition: fullness (c1–c3).  

With just a single producer and a single consumer, the code in Figure 30.8 works. However, if we have more than one of these threads (e.g., two consumers), the solution has two critical problems. What are they?  

... (pause here to think) ...  

Let’s understand the first problem, which has to do with the if statement before the wait. Assume there are two consumers ( $\mathit { T } _ { c 1 }$ and ${ T _ { c 2 } }$ ) and one producer $( T _ { p } )$ . First, a consumer $( T _ { c 1 } )$ runs; it acquires the lock (c1), checks if any buffers are ready for consumption (c2), and finding that none are, waits (c3) (which releases the lock).  

Then the producer $( T _ { p } )$ runs. It acquires the lock (p1), checks if all  

OPERATINGSYSTEMS[VERSION 1.10]  

![](images/622e47783565633e7a09b7e390e12a60d6dfb96a61351be722a63907ed45d57d.jpg)  
Figure 30.9: Thread Trace: Broken Solution (v1)  

buffers are full (p2), and finding that not to be the case, goes ahead and fills the buffer (p4). The producer then signals that a buffer has been filled (p5). Critically, this moves the first consumer $( T _ { c 1 } )$ from sleeping on a condition variable to the ready queue; ${ T _ { c 1 } }$ is now able to run (but not yet running). The producer then continues until realizing the buffer is full, at which point it sleeps (p6, p1–p3).  

Here is where the problem occurs: another consumer $( T _ { c 2 } )$ sneaks in and consumes the one existing value in the buffer $( \mathrm { c 1 } , \mathrm { c 2 } , \mathrm { c 4 } , \mathrm { c 5 } , \mathrm { c }$ 6, skipping the wait at c3 because the buffer is full). Now assume ${ T _ { c 1 } }$ runs; just before returning from the wait, it re-acquires the lock and then returns. It then calls get() (c4), but there are no buffers to consume! An assertion triggers, and the code has not functioned as desired. Clearly, we should have somehow prevented $\textstyle T _ { c 1 }$ from trying to consume because ${ T _ { c 2 } }$ snuck in and consumed the one value in the buffer that had been produced. Figure 30.9 shows the action each thread takes, as well as its scheduler state (Ready, Running, or Sleeping) over time.  

The problem arises for a simple reason: after the producer woke $T _ { c 1 }$ , but before $T _ { c 1 }$ ever ran, the state of the bounded buffer changed (thanks to ${ T _ { c 2 } }$ ). Signaling a thread only wakes them up; it is thus a hint that the state of the world has changed (in this case, that a value has been placed in the buffer), but there is no guarantee that when the woken thread runs, the state will still be as desired. This interpretation of what a signal means is often referred to as Mesa semantics, after the first research that built a condition variable in such a manner [LR80]; the contrast, referred to as  

1 int loops;   
2 cond_t cond;   
3 mutex_t mutex;   
4   
5 void \*producer(void \*arg) {   
6 int i;   
7 for ( $\mathrm { ~ \\ ~ \underline { ~ } { ~ i ~ } ~ } = \mathrm { ~ \ 0 ~ }$ ; i < loops; $\dot { \bf \underline { { 1 } } } + +$ ) {   
8 Pthread_mutex_lock(&mutex); // p1   
9 while (count $\scriptstyle \mathbf { \alpha = } \ 1$ ) // p2   
10 Pthread_cond_wait(&cond, &mutex); // p3   
11 put(i); // p4   
12 Pthread_cond_signal(&cond); // p5   
13 Pthread_mutex_unlock(&mutex); // p6   
14 }   
15 }   
16   
17 void \*consumer(void \*arg) {   
18 int i;   
19 for ( $\mathrm { ~ \\ ~ i ~ } = \mathrm { ~ \ ~ 0 ~ }$ ; i < loops; $\dot { 1 } + +$ ) {   
20 Pthread_mutex_lock(&mutex); // c1   
21 while (count $\scriptstyle \mathbf { \mu } = \mathbf { \mu } 0$ ) // c2   
22 Pthread_cond_wait(&cond, &mutex); // c3   
23 int tmp $\mathbf { \Sigma } = \mathbf { \Sigma }$ get(); // c4   
24 Pthread_cond_signal(&cond); // c5   
25 Pthread_mutex_unlock(&mutex); // c6   
26 printf("%d\n", tmp);   
27 }   
28 }  

# Figure 30.10: Producer/Consumer: Single CV And While  

Hoare semantics, is harder to build but provides a stronger guarantee that the woken thread will run immediately upon being woken [H74]. Virtually every system ever built employs Mesa semantics.  

# Better, But Still Broken: While, Not If  

Fortunately, this fix is easy (Figure 30.10): change the if to a while. Think about why this works; now consumer $T _ { c 1 }$ wakes up and (with the lock held) immediately re-checks the state of the shared variable (c2). If the buffer is empty at that point, the consumer simply goes back to sleep (c3). The corollary if is also changed to a while in the producer (p2).  

Thanks to Mesa semantics, a simple rule to remember with condition variables is to always use while loops. Sometimes you don’t have to recheck the condition, but it is always safe to do so; just do it and be happy.  

However, this code still has a bug, the second of two problems mentioned above. Can you see it? It has something to do with the fact that there is only one condition variable. Try to figure out what the problem is, before reading ahead. DO IT! (pause for you to think, or close your eyes...)  

OPERATINGSYSTEMS[VERSION 1.10]  

<html><body><table><tr><td>Te1 c1</td><td>State</td><td>Tc2</td><td>State</td><td>Tp State</td><td>connr 0</td><td>Comment</td></tr><tr><td>c2 c3 c2 c4 c5 c6 c1 c2 c3</td><td>Run Run Ready Ready Ready Ready Run Run Run Run Run Run Sleep Sleep Sleep Sleep Sleep Sleep Sleep Ready Sleep Sleep Sleep</td><td>c1 c2 c3 c2 c3</td><td>Ready Ready Ready Run Run p5 p3 Ready Ready Ready Ready Ready Run Sleep Sleep Sleep Sleep Sleep Sleep Sleep Sleep Sleep Sleep Sleep Sleep</td><td>Ready Ready Ready Ready Ready Ready p1 Run p2 Run Run Run p6 Run p1 Run p2 Run p4 Sleep Sleep Sleep Sleep Sleep Sleep Sleep Sleep Sleep Sleep</td><td>0 0 0 0 0 0 0 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0</td><td>Nothing to get Nothing to get Buffer now full Tc1 awoken Must sleep (full) Recheck condition Tc1 grabs data Oops! Woke Tc2 Nothing to get. Everyone aslep...</td></tr></table></body></html>  

Let’s confirm you figured it out correctly, or perhaps let’s confirm that you are now awake and reading this part of the book. The problem occurs when two consumers run first $\mathit { T } _ { c 1 }$ and ${ T _ { c 2 } }$ ) and both go to sleep (c3). Then, the producer runs, puts a value in the buffer, and wakes one of the consumers (say $T _ { c 1 }$ ). The producer then loops back (releasing and reacquiring the lock along the way) and tries to put more data in the buffer; because the buffer is full, the producer instead waits on the condition (thus sleeping). Now, one consumer is ready to run $( T _ { c 1 } )$ , and two threads are sleeping on a condition $\mathit { T } _ { c 2 }$ and $T _ { p }$ ). We are about to cause a problem: things are getting exciting!  

The consumer $T _ { c 1 }$ then wakes by returning from wait() (c3), re-checks the condition (c2), and finding the buffer full, consumes the value (c4). This consumer then, critically, signals on the condition (c5), waking only one thread that is sleeping. However, which thread should it wake?  

Because the consumer has emptied the buffer, it clearly should wake the producer. However, if it wakes the consumer ${ T _ { c 2 } }$ (which is definitely possible, depending on how the wait queue is managed), we have a problem. Specifically, the consumer ${ T _ { c 2 } }$ will wake up and find the buffer empty (c2), and go back to sleep (c3). The producer $T _ { p } ,$ which has a value  

1 cond_t empty, fill;   
2 mutex_t mutex;   
3   
4 void \*producer(void \*arg) {   
5 int i;   
6 for ( $\mathrm { ~ \\ ~ i ~ } = \mathrm { ~ \ ~ 0 ~ }$ ; i < loops; ${ \dot { \bf \underline { { 1 } } } } + + { \bf \underline { { 1 } } }$ ) {   
7 Pthread_mutex_lock(&mutex);   
8 while (count $\scriptstyle \mathbf { \alpha = { \begin{array} { l } { 1 } \end{array} } }$ )   
9 Pthread_cond_wait(&empty, &mutex);   
10 put(i);   
11 Pthread_cond_signal(&fill);   
12 Pthread_mutex_unlock(&mutex);   
13 }   
14 }   
15   
16 void \*consumer(void \*arg) {   
17 int i;   
18 for ( $\mathrm { ~ \\ ~ i ~ } = \mathrm { ~ \ ~ 0 ~ }$ ; i < loops; ${ \dot { \bf \underline { { 1 } } } } + + { \bf \underline { { 1 } } }$ ) {   
19 Pthread_mutex_lock(&mutex);   
20 while (count $\scriptstyle \mathbf { \mu } = \mathbf { \mu } 0$ )   
21 Pthread_cond_wait(&fill, &mutex);   
22 int tmp $\mathbf { \Sigma } = \mathbf { \Sigma }$ get();   
23 Pthread_cond_signal(&empty);   
24 Pthread_mutex_unlock(&mutex);   
25 printf("%d\n", tmp);   
26 }   
27 }  

to put into the buffer, is left sleeping. The other consumer thread, $T _ { c 1 }$ , also goes back to sleep. All three threads are left sleeping, a clear bug; see Figure 30.11 for the brutal step-by-step of this terrible calamity.  

Signaling is clearly needed, but must be more directed. A consumer should not wake other consumers, only producers, and vice-versa.  

# The Single Buffer Producer/Consumer Solution  

The solution here is once again a small one: use two condition variables, instead of one, in order to properly signal which type of thread should wake up when the state of the system changes. Figure 30.12 shows the resulting code.  

In the code, producer threads wait on the condition empty, and signals fill. Conversely, consumer threads wait on fill and signal empty. By doing so, the second problem above is avoided by design: a consumer can never accidentally wake a consumer, and a producer can never accidentally wake a producer.  

OPERATINGSYSTEMS[VERSION 1.10]  

1 int buffer[MAX];   
2 int fill_ptr $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
3 int use_ptr $\mathbf { \xi } = \mathbf { \xi } 0 ; \mathbf { \zeta }$   
4 int count $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
5   
6 void put(int value) {   
7 buffer[fill_ptr] $\mathbf { \Sigma } = \mathbf { \Sigma }$ value;   
8 fill_ptr $\mathbf { \Sigma } = \mathbf { \Sigma }$ (fill_ptr $\mathbf { \Sigma } + \mathbf { \Sigma } \ b { \mathrm { 1 } }$ ) % MAX;   
9 count $^ { + + }$ ;   
10 }   
11   
12 int get() {   
13 int tmp $\mathbf { \Sigma } = \mathbf { \Sigma }$ buffer[use_ptr];   
14 use_ptr $\mathbf { \Sigma } = \mathbf { \Sigma }$ (use_ptr + 1) % MAX;   
15 count--;   
16 return tmp;   
17 }   
1 cond_t empty, fill;   
2 mutex_t mutex;   
3   
4 void \*producer(void \*arg) {   
5 int i;   
6 for ( $\mathrm { ~ \\ ~ i ~ } = \mathrm { ~ \ r ~ 0 ~ }$ ; i < loops; ${ \dot { \bf \underline { { 1 } } } } + +$ ) {   
7 Pthread_mutex_lock(&mutex); // p1   
8 while (count $\scriptstyle = =$ MAX) // p2   
9 Pthread_cond_wait(&empty, &mutex); // p3   
10 put(i); // p4   
11 Pthread_cond_signal(&fill); // p5   
12 Pthread_mutex_unlock(&mutex); // p6   
13 }   
14 }   
15   
16 void \*consumer(void \*arg) {   
17 int i;   
18 for ( $\mathrm { ~ \\ ~ i ~ } = \mathrm { ~ \ ~ 0 ~ }$ ; i < loops; ${ \dot { \bf \underline { { 1 } } } } + +$ ) {   
19 Pthread_mutex_lock(&mutex); // c1   
20 while (count $\scriptstyle \mathbf { \mu } = \mathbf { \mu } 0$ ) // c2   
21 Pthread_cond_wait(&fill, &mutex); // c3   
22 int tmp $\mathbf { \Sigma } = \mathbf { \Sigma }$ get(); // c4   
23 Pthread_cond_signal(&empty); // c5   
24 Pthread_mutex_unlock(&mutex); // c6   
25 printf("%d\n", tmp);   
26 }   
27 1  

# TIP: USE WHILE (NOT IF) FOR CONDITIONS  

When checking for a condition in a multi-threaded program, using a while loop is always correct; using an if statement only might be, depending on the semantics of signaling. Thus, always use while and your code will behave as expected.  

Using while loops around conditional checks also handles the case where spurious wakeups occur. In some thread packages, due to details of the implementation, it is possible that two threads get woken up though just a single signal has taken place [L11]. Spurious wakeups are further reason to re-check the condition a thread is waiting on.  

# The Correct Producer/Consumer Solution  

We now have a working producer/consumer solution, albeit not a fully general one. The last change we make is to enable more concurrency and efficiency; specifically, we add more buffer slots, so that multiple values can be produced before sleeping, and similarly multiple values can be consumed before sleeping. With just a single producer and consumer, this approach is more efficient as it reduces context switches; with multiple producers or consumers (or both), it even allows concurrent producing or consuming to take place, thus increasing concurrency. Fortunately, it is a small change from our current solution.  

The first change for this correct solution is within the buffer structure itself and the corresponding put() and get() (Figure 30.13). We also slightly change the conditions that producers and consumers check in order to determine whether to sleep or not. We also show the correct waiting and signaling logic (Figure 30.14). A producer only sleeps if all buffers are currently filled (p2); similarly, a consumer only sleeps if all buffers are currently empty (c2). And thus we solve the producer/consumer problem; time to sit back and drink a cold one.  

