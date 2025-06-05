# 4.4 Process States  

Now that we have some idea of what a process is (though we will continue to refine this notion), and (roughly) how it is created, let us talk about the different states a process can be in at a given time. The notion that a process can be in one of these states arose in early computer systems $\mathrm { [ D V 6 6 , V + 6 5 ] }$ . In a simplified view, a process can be in one of three states:  

• Running: In the running state, a process is running on a processor. This means it is executing instructions. • Ready: In the ready state, a process is ready to run but for some reason the OS has chosen not to run it at this given moment.  

![](images/d200deb276b6b014880c3f5aa08d8576ecad07e368a2ee5bb4c075c0a7a478da.jpg)  
Figure 4.2: Process: State Transitions  

• Blocked: In the blocked state, a process has performed some kind of operation that makes it not ready to run until some other event takes place. A common example: when a process initiates an I/O request to a disk, it becomes blocked and thus some other process can use the processor.  

If we were to map these states to a graph, we would arrive at the diagram in Figure 4.2. As you can see in the diagram, a process can be moved between the ready and running states at the discretion of the OS. Being moved from ready to running means the process has been scheduled; being moved from running to ready means the process has been descheduled. Once a process has become blocked (e.g., by initiating an I/O operation), the OS will keep it as such until some event occurs (e.g., I/O completion); at that point, the process moves to the ready state again (and potentially immediately to running again, if the OS so decides).  

Let’s look at an example of how two processes might transition through some of these states. First, imagine two processes running, each of which only use the CPU (they do no I/O). In this case, a trace of the state of each process might look like this (Figure 4.3).  

![](images/ee6647601c57c0bc7bbbb75616cd4263b02632dfaed99e3e116dfe67ca25dd4d.jpg)  
Figure 4.3: Tracing Process State: CPU Only  

OPERATINGSYSTEMS[VERSION 1.10]  

![](images/a61f04505254f24578faa680da75268f32db106332cb53dd97c9aa1b4337b36d.jpg)  
Figure 4.4: Tracing Process State: CPU and I/O  

In this next example, the first process issues an I/O after running for some time. At that point, the process is blocked, giving the other process a chance to run. Figure 4.4 shows a trace of this scenario.  

More specifically, Process0 initiates an I/O and becomes blocked waiting for it to complete; processes become blocked, for example, when reading from a disk or waiting for a packet from a network. The OS recognizes Process0 is not using the CPU and starts running Process1. While Process1 is running, the $\bar { 1 / \mathrm { O } }$ completes, moving Process0 back to ready. Finally, Process1 finishes, and Process0 runs and then is done.  

Note that there are many decisions the OS must make, even in this simple example. First, the system had to decide to run Process1 while Process0 issued an I/O; doing so improves resource utilization by keeping the CPU busy. Second, the system decided not to switch back to Process0 when its I/O completed; it is not clear if this is a good decision or not. What do you think? These types of decisions are made by the OS scheduler, a topic we will discuss a few chapters in the future.  

