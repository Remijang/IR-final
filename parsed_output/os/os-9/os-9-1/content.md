# 9.1 Basic Concept: Tickets Represent Your Share  

Underlying lottery scheduling is one very basic concept: tickets, which are used to represent the share of a resource that a process (or user or whatever) should receive. The percent of tickets that a process has represents its share of the system resource in question.  

Let’s look at an example. Imagine two processes, A and B, and further that A has 75 tickets while B has only 25. Thus, what we would like is for A to receive $7 5 \%$ of the CPU and B the remaining $2 5 \%$ .  

Lottery scheduling achieves this probabilistically (but not deterministically) by holding a lottery every so often (say, every time slice). Holding a lottery is straightforward: the scheduler must know how many total tickets there are (in our example, there are 100). The scheduler then picks  

# TIP: USE RANDOMNESS  

One of the most beautiful aspects of lottery scheduling is its use of randomness. When you have to make a decision, using such a randomized approach is often a robust and simple way of doing so.  

Random approaches have at least three advantages over more traditional decisions. First, random often avoids strange corner-case behaviors that a more traditional algorithm may have trouble handling. For example, consider the LRU replacement policy (studied in more detail in a future chapter on virtual memory); while often a good replacement algorithm, LRU attains worst-case performance for some cyclic-sequential workloads. Random, on the other hand, has no such worst case.  

Second, random also is lightweight, requiring little state to track alternatives. In a traditional fair-share scheduling algorithm, tracking how much CPU each process has received requires per-process accounting, which must be updated after running each process. Doing so randomly necessitates only the most minimal of per-process state (e.g., the number of tickets each has).  

Finally, random can be quite fast. As long as generating a random number is quick, making the decision is also, and thus random can be used in a number of places where speed is required. Of course, the faster the need, the more random tends towards pseudo-random.  

a winning ticket, which is a number from 0 to $9 9 ^ { 1 }$ . Assuming A holds tickets 0 through 74 and B 75 through 99, the winning ticket simply determines whether A or B runs. The scheduler then loads the state of that winning process and runs it.  

Here is an example output of a lottery scheduler’s winning tickets:  

63 85 70 39 76 17 29 41 36 39 10 99 68 83 63 62 43 0 49 12  

Here is the resulting schedule:  

![](images/99cbe75b4871af0f6a74c0ecb22b721e26d4b4358cb72e0e0c32f8333653d2cc.jpg)  

As you can see from the example, the use of randomness in lottery scheduling leads to a probabilistic correctness in meeting the desired proportion, but no guarantee. In our example above, B only gets to run 4 out of 20 time slices $( 2 0 \% )$ , instead of the desired $2 5 \%$ allocation. However, the longer these two jobs compete, the more likely they are to achieve the desired percentages.  

TIP: USE TICKETS TO REPRESENT SHARES One of the most powerful (and basic) mechanisms in the design of lottery (and stride) scheduling is that of the ticket. The ticket is used to represent a process’s share of the CPU in these examples, but can be applied much more broadly. For example, in more recent work on virtual memory management for hypervisors, Waldspurger shows how tickets can be used to represent a guest operating system’s share of memory [W02]. Thus, if you are ever in need of a mechanism to represent a proportion of ownership, this concept just might be ... (wait for it) ... the ticket.  

