# 7.4 Shortest Job First (SJF)  

It turns out that a very simple approach solves this problem; in fact it is an idea stolen from operations research [C54,PV56] and applied to scheduling of jobs in computer systems. This new scheduling discipline is known as Shortest Job First (SJF), and the name should be easy to remember because it describes the policy quite completely: it runs the shortest job first, then the next shortest, and so on.  

![](images/4f92f0bb19e7ead28329234160fb2f785f6e130a871ed8933577e219200e12cf.jpg)  
Figure 7.3: SJF Simple Example  

Let’s take our example above but with SJF as our scheduling policy. Figure 7.3 shows the results of running A, $\mathsf { B } ,$ and C. Hopefully the diagram makes it clear why SJF performs much better with regards to average turnaround time. Simply by running B and C before A, SJF reduces average turnaround from 110 seconds to 50 ( $\frac { 1 0 + 2 0 + 1 2 0 } { 3 } = 5 0$ ), more than a factor of two improvement.  

# ASIDE: PREEMPTIVE SCHEDULERS  

In the old days of batch computing, a number of non-preemptive schedulers were developed; such systems would run each job to completion before considering whether to run a new job. Virtually all modern schedulers are preemptive, and quite willing to stop one process from running in order to run another. This implies that the scheduler employs the mechanisms we learned about previously; in particular, the scheduler can perform a context switch, stopping one running process temporarily and resuming (or starting) another.  

In fact, given our assumptions about jobs all arriving at the same time, we could prove that SJF is indeed an optimal scheduling algorithm. However, you are in a systems class, not theory or operations research; no proofs are allowed.  

Thus we arrive upon a good approach to scheduling with SJF, but our assumptions are still fairly unrealistic. Let’s relax another. In particular, we can target assumption 2, and now assume that jobs can arrive at any time instead of all at once. What problems does this lead to?  

(Another pause to think ... are you thinking? Come on, you can do it)  

Here we can illustrate the problem again with an example. This time, assume A arrives at $t = 0$ and needs to run for 100 seconds, whereas B and C arrive at $t = 1 0$ and each need to run for 10 seconds. With pure SJF, we’d get the schedule seen in Figure 7.4.  

![](images/58713f79e27a618792852b6378d5632493d235bef2cb0c6344769c61007e50ed.jpg)  
Figure 7.4: SJF With Late Arrivals From B and C  

As you can see from the figure, even though B and C arrived shortly after A, they still are forced to wait until A has completed, and thus suffer the same convoy problem. Average turnaround time for these three jobs is 103.33 seconds $\mathrm { \langle \frac { 1 0 0 + ( 1 1 0 - 1 0 ) + ( 1 \bar { 2 } 0 - 1 0 ) } { 3 } \frac { \partial } { \partial \phantom { | } } , }$ ). What can a scheduler do?  

