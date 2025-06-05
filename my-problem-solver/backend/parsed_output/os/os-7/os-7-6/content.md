# 7.6 A New Metric: Response Time  

Thus, if we knew job lengths, and that jobs only used the CPU, and our only metric was turnaround time, STCF would be a great policy. In fact, for a number of early batch computing systems, these types of scheduling algorithms made some sense. However, the introduction of time-shared machines changed all that. Now users would sit at a terminal and demand interactive performance from the system as well. And thus, a new metric was born: response time.  

We define response time as the time from when the job arrives in a system to the first time it is scheduled3. More formally:  

$$
T _ { r e s p o n s e } = T _ { f i r s t r u n } - T _ { a r r i v a l }
$$  

![](images/9f687d3a708e1201a38c2e722eb8444127b32719851bf3db2c06fc98800fde21.jpg)  
Figure 7.6: SJF Again (Bad for Response Time)  

![](images/c50b696cd01f5d28cd5118d4ab355713816724d8c9b82643665e5bc5426605d7.jpg)  
Figure 7.7: Round Robin (Good For Response Time)  

For example, if we had the schedule from Figure 7.5 (with A arriving at time 0, and B and C at time 10), the response time of each job is as follows: 0 for job A, 0 for B, and 10 for C (average: 3.33).  

As you might be thinking, STCF and related disciplines are not particularly good for response time. If three jobs arrive at the same time, for example, the third job has to wait for the previous two jobs to run in their entirety before being scheduled just once. While great for turnaround time, this approach is quite bad for response time and interactivity. Indeed, imagine sitting at a terminal, typing, and having to wait 10 seconds to see a response from the system just because some other job got scheduled in front of yours: not too pleasant.  

Thus, we are left with another problem: how can we build a scheduler that is sensitive to response time?  

