# 5.2 The wait() System Call  

So far, we haven’t done much: just created a child that prints out a message and exits. Sometimes, as it turns out, it is quite useful for a parent to wait for a child process to finish what it has been doing. This task is accomplished with the wait() system call (or its more complete sibling waitpid()); see Figure 5.2 for details.  

In this example (p2.c), the parent process calls wait() to delay its execution until the child finishes executing. When the child is done, wait() returns to the parent.  

Adding a wait() call to the code above makes the output deterministic. Can you see why? Go ahead, think about it.  

(waiting for you to think .... and done)  

Now that you have thought a bit, here is the output:  

prompt> ./p2   
hello (pid:29266)   
child (pid:29267)   
parent of 29267 (rc_wait:29267) (pid:29266)   
prompt>  

With this code, we now know that the child will always print first. Why do we know that? Well, it might simply run first, as before, and thus print before the parent. However, if the parent does happen to run first, it will immediately call wait(); this system call won’t return until the child has run and exited2. Thus, even when the parent runs first, it politely waits for the child to finish running, then wait() returns, and then the parent prints its message.  

