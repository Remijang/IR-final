# 7.3 First In, First Out (FIFO)  

The most basic algorithm we can implement is known as First In, First Out (FIFO) scheduling or sometimes First Come, First Served (FCFS).  

FIFO has a number of positive properties: it is clearly simple and thus easy to implement. And, given our assumptions, it works pretty well.  

Let’s do a quick example together. Imagine three jobs arrive in the system, A, B, and $C ,$ at roughly the same time $( T _ { a r r i v a l } = 0 )$ ). Because FIFO has to put some job first, let’s assume that while they all arrived simultaneously, A arrived just a hair before B which arrived just a hair before C. Assume also that each job runs for 10 seconds. What will the average turnaround time be for these jobs?  

![](images/8779138f2ec77e5e61e2d60ee7d3a92eafb1b3d123c00869817cd0b9422ae35e.jpg)  
Figure 7.1: FIFO Simple Example  

From Figure 7.1, you can see that A finished at 10, B at 20, and C at 30. Thus, the average turnaround time for the three jobs is simply $\textstyle { \frac { 1 0 + 2 0 + 3 0 } { 3 } } =$ 20. Computing turnaround time is as easy as that.  

Now let’s relax one of our assumptions. In particular, let’s relax assumption 1, and thus no longer assume that each job runs for the same amount of time. How does FIFO perform now? What kind of workload could you construct to make FIFO perform poorly?  

(think about this before reading on ... keep thinking ... got it?!)  

Presumably you’ve figured this out by now, but just in case, let’s do an example to show how jobs of different lengths can lead to trouble for FIFO scheduling. In particular, let’s again assume three jobs (A, B, and C), but this time A runs for 100 seconds while B and C run for 10 each.  

![](images/5c00a2257b0cfe0e05dfd467025ca1a1da42b854ccded1faec391602bb0c9dda.jpg)  
Figure 7.2: Why FIFO Is Not That Great  

As you can see in Figure 7.2, Job A runs first for the full 100 seconds before B or C even get a chance to run. Thus, the average turnaround time for the system is high: a painful 110 seconds $\begin{array} { r } { \frac { \prime } { 3 } \frac { 1 0 0 + 1 1 0 + 1 2 0 } { 3 } = 1 1 0 , } \end{array}$ ).  

This problem is generally referred to as the convoy effect $\scriptstyle { [ { \mathrm { B } } + 7 9 ] }$ , where a number of relatively-short potential consumers of a resource get queued  

# TIP: THE PRINCIPLE OF SJF  

Shortest Job First represents a general scheduling principle that can be applied to any system where the perceived turnaround time per customer (or, in our case, a job) matters. Think of any line you have waited in: if the establishment in question cares about customer satisfaction, it is likely they have taken SJF into account. For example, grocery stores commonly have a “ten-items-or-less” line to ensure that shoppers with only a few things to purchase don’t get stuck behind the family preparing for some upcoming nuclear winter.  

behind a heavyweight resource consumer. This scheduling scenario might remind you of a single line at a grocery store and what you feel like when you see the person in front of you with three carts full of provisions and a checkbook out; it’s going to be a while2.  

So what should we do? How can we develop a better algorithm to deal with our new reality of jobs that run for different amounts of time? Think about it first; then read on.  

