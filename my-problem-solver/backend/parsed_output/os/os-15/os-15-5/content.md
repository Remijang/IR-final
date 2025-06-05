# 15.5 Operating System Issues  

Just as the hardware provides new features to support dynamic relocation, the OS now has new issues it must handle; the combination of hardware support and OS management leads to the implementation of a simple virtual memory. Specifically, there are a few critical junctures where the OS must get involved to implement our base-and-bounds version of virtual memory.  

First, the OS must take action when a process is created, finding space for its address space in memory. Fortunately, given our assumptions that each address space is (a) smaller than the size of physical memory and (b) the same size, this is quite easy for the OS; it can simply view physical memory as an array of slots, and track whether each one is free or in use. When a new process is created, the OS will have to search a data structure (often called a free list) to find room for the new address space and then mark it used. With variable-sized address spaces, life is more complicated, but we will leave that concern for future chapters.  

Figure 15.4: Dynamic Relocation: Operating System Responsibilities   


<html><body><table><tr><td>OS Requirements</td><td>Notes</td></tr><tr><td>Memory management</td><td>Need to allocate memory for new processes;. Reclaim memory from terminated processes;.</td></tr><tr><td>Base/bounds management</td><td>Generally manage memory via free list. Must set base/bounds properly upon context switch</td></tr><tr><td>Exception handling</td><td>Code to run when exceptions arise; likely action is to terminate offending process.</td></tr></table></body></html>  

Let’s look at an example. In Figure 15.2 (page 5), you can see the OS using the first slot of physical memory for itself, and that it has relocated the process from the example above into the slot starting at physical memory address 32 KB. The other two slots are free (16 KB-32 KB and 48 KB64 KB); thus, the free list should consist of these two entries.  

Second, the OS must do some work when a process is terminated (i.e., when it exits gracefully, or is forcefully killed because it misbehaved), reclaiming all of its memory for use in other processes or the OS. Upon termination of a process, the OS thus puts its memory back on the free list, and cleans up any associated data structures as need be.  

Third, the OS must also perform a few additional steps when a context switch occurs. There is only one base and bounds register pair on each CPU, after all, and their values differ for each running program, as each program is loaded at a different physical address in memory. Thus, the OS must save and restore the base-and-bounds pair when it switches between processes. Specifically, when the OS decides to stop running a process, it must save the values of the base and bounds registers to memory, in some per-process structure such as the process structure or process control block (PCB). Similarly, when the OS resumes a running process (or runs it the first time), it must set the values of the base and bounds on the CPU to the correct values for this process.  

We should note that when a process is stopped (i.e., not running), it is possible for the OS to move an address space from one location in memory to another rather easily. To move a process’s address space, the OS first deschedules the process; then, the OS copies the address space from the current location to the new location; finally, the OS updates the saved base register (in the process structure) to point to the new location. When the process is resumed, its (new) base register is restored, and it begins running again, oblivious that its instructions and data are now in a completely new spot in memory.  

Fourth, the OS must provide exception handlers, or functions to be called, as discussed above; the OS installs these handlers at boot time (via privileged instructions). For example, if a process tries to access memory outside its bounds, the CPU will raise an exception; the OS must be prepared to take action when such an exception arises. The common reaction of the OS will be one of hostility: it will likely terminate the offending process. The OS should be highly protective of the machine it is running, and thus it does not take kindly to a process trying to access memory or  

OPERATINGSYSTEMS[VERSION 1.10]  

Figure 15.5: Limited Direct Execution (Dynamic Relocation) $@$ Boot   


<html><body><table><tr><td>OS @ boot (kernel mode)</td><td>Hardware</td><td>(No Program Yet)</td></tr><tr><td>initialize trap table</td><td>remember addresses of...</td><td></td></tr><tr><td></td><td>system call handler.</td><td></td></tr><tr><td></td><td>timer handler</td><td></td></tr><tr><td></td><td>illegal mem-access handler</td><td></td></tr><tr><td></td><td>illegal instruction handler.</td><td></td></tr><tr><td>start interrupt timer.</td><td></td><td></td></tr><tr><td></td><td>start timer; interrupt after X ms</td><td></td></tr><tr><td>initialize process table initialize free list.</td><td></td><td></td></tr></table></body></html>  

execute instructions that it shouldn’t. Bye bye, misbehaving process; it’s been nice knowing you.  

Figures 15.5 and 15.6 (page 12) illustrate much of the hardware/OS interaction in a timeline. The first figure shows what the OS does at boot time to ready the machine for use, and the second shows what happens when a process (Process A) starts running; note how its memory translations are handled by the hardware with no OS intervention. At some point (middle of second figure), a timer interrupt occurs, and the OS switches to Process B, which executes a “bad load” (to an illegal memory address); at that point, the OS must get involved, terminating the process and cleaning up by freeing B’s memory and removing its entry from the process table. As you can see from the figures, we are still following the basic approach of limited direct execution. In most cases, the OS just sets up the hardware appropriately and lets the process run directly on the CPU; only when the process misbehaves does the OS have to become involved.  

