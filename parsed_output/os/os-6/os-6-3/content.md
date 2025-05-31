# 6.3 Problem #2: Switching Between Processes  

The next problem with direct execution is achieving a switch between processes. Switching between processes should be simple, right? The OS should just decide to stop one process and start another. What’s the big deal? But it actually is a little bit tricky: specifically, if a process is running on the CPU, this by definition means the OS is not running. If the OS is not running, how can it do anything at all? (hint: it can’t) While this sounds almost philosophical, it is a real problem: there is clearly no way for the OS to take an action if it is not running on the CPU. Thus we arrive at the crux of the problem.  

THE CRUX: HOW TO REGAIN CONTROL OF THE CPU How can the operating system regain control of the CPU so that it can switch between processes?  

# A Cooperative Approach: Wait For System Calls  

One approach that some systems have taken in the past (for example, early versions of the Macintosh operating system [M11], or the old Xerox Alto system [A79]) is known as the cooperative approach. In this style, the OS trusts the processes of the system to behave reasonably. Processes that run for too long are assumed to periodically give up the CPU so that the OS can decide to run some other task.  

Thus, you might ask, how does a friendly process give up the CPU in this utopian world? Most processes, as it turns out, transfer control of the CPU to the OS quite frequently by making system calls, for example, to open a file and subsequently read it, or to send a message to another machine, or to create a new process. Systems like this often include an explicit yield system call, which does nothing except to transfer control to the OS so it can run other processes.  

Applications also transfer control to the OS when they do something illegal. For example, if an application divides by zero, or tries to access memory that it shouldn’t be able to access, it will generate a trap to the OS. The OS will then have control of the CPU again (and likely terminate the offending process).  

Thus, in a cooperative scheduling system, the OS regains control of the CPU by waiting for a system call or an illegal operation of some kind to take place. You might also be thinking: isn’t this passive approach less than ideal? What happens, for example, if a process (whether malicious, or just full of bugs) ends up in an infinite loop, and never makes a system call? What can the OS do then?  

# A Non-Cooperative Approach: The OS Takes Control  

Without some additional help from the hardware, it turns out the OS can’t do much at all when a process refuses to make system calls (or mistakes) and thus return control to the OS. In fact, in the cooperative approach, your only recourse when a process gets stuck in an infinite loop is to resort to the age-old solution to all problems in computer systems: reboot the machine. Thus, we again arrive at a subproblem of our general quest to gain control of the CPU.  

THE CRUX: HOW TO GAIN CONTROL WITHOUT COOPERATION How can the OS gain control of the CPU even if processes are not being cooperative? What can the OS do to ensure a rogue process does not take over the machine?  

The answer turns out to be simple and was discovered by a number of people building computer systems many years ago: a timer interrupt $\left[ \mathrm { M } \mathrm { + } 6 3 \right]$ . A timer device can be programmed to raise an interrupt every so many milliseconds; when the interrupt is raised, the currently running process is halted, and a pre-configured interrupt handler in the OS runs. At this point, the OS has regained control of the CPU, and thus can do what it pleases: stop the current process, and start a different one.  

As we discussed before with system calls, the OS must inform the hardware of which code to run when the timer interrupt occurs; thus, at boot time, the OS does exactly that. Second, also during the boot  

TIP: DEALING WITH APPLICATION MISBEHAVIOR Operating systems often have to deal with misbehaving processes, those that either through design (maliciousness) or accident (bugs) attempt to do something that they shouldn’t. In modern systems, the way the OS tries to handle such malfeasance is to simply terminate the offender. One strike and you’re out! Perhaps brutal, but what else should the OS do when you try to access memory illegally or execute an illegal instruction?  

OPERATINGSYSTEMS[VERSION 1.10]  

sequence, the OS must start the timer, which is of course a privileged operation. Once the timer has begun, the OS can thus feel safe in that control will eventually be returned to it, and thus the OS is free to run user programs. The timer can also be turned off (also a privileged operation), something we will discuss later when we understand concurrency in more detail.  

Note that the hardware has some responsibility when an interrupt occurs, in particular to save enough of the state of the program that was running when the interrupt occurred such that a subsequent return-fromtrap instruction will be able to resume the running program correctly. This set of actions is quite similar to the behavior of the hardware during an explicit system-call trap into the kernel, with various registers thus getting saved (e.g., onto a kernel stack) and thus easily restored by the return-from-trap instruction.  

# Saving and Restoring Context  

Now that the OS has regained control, whether cooperatively via a system call, or more forcefully via a timer interrupt, a decision has to be made: whether to continue running the currently-running process, or switch to a different one. This decision is made by a part of the operating system known as the scheduler; we will discuss scheduling policies in great detail in the next few chapters.  

If the decision is made to switch, the OS then executes a low-level piece of code which we refer to as a context switch. A context switch is conceptually simple: all the OS has to do is save a few register values for the currently-executing process (onto its kernel stack, for example) and restore a few for the soon-to-be-executing process (from its kernel stack). By doing so, the OS thus ensures that when the return-from-trap instruction is finally executed, instead of returning to the process that was running, the system resumes execution of another process.  

To save the context of the currently-running process, the OS will execute some low-level assembly code to save the general purpose registers, PC, and the kernel stack pointer of the currently-running process, and then restore said registers, PC, and switch to the kernel stack for the soon-to-be-executing process. By switching stacks, the kernel enters the call to the switch code in the context of one process (the one that was interrupted) and returns in the context of another (the soon-to-be-executing  

TIP: USE THE TIMER INTERRUPT TO REGAIN CONTROL The addition of a timer interrupt gives the OS the ability to run again on a CPU even if processes act in a non-cooperative fashion. Thus, this hardware feature is essential in helping the OS maintain control of the machine.  

TIP: REBOOT IS USEFUL  

Earlier on, we noted that the only solution to infinite loops (and similar behaviors) under cooperative preemption is to reboot the machine. While you may scoff at this hack, researchers have shown that reboot (or in general, starting over some piece of software) can be a hugely useful tool in building robust systems $\scriptstyle { \mathrm { [ C + 0 4 ] } }$ .  

Specifically, reboot is useful because it moves software back to a known and likely more tested state. Reboots also reclaim stale or leaked resources (e.g., memory) which may otherwise be hard to handle. Finally, reboots are easy to automate. For all of these reasons, it is not uncommon in large-scale cluster Internet services for system management software to periodically reboot sets of machines in order to reset them and thus obtain the advantages listed above.  

Thus, next time you reboot, you are not just enacting some ugly hack. Rather, you are using a time-tested approach to improving the behavior of a computer system. Well done!  

one). When the OS then finally executes a return-from-trap instruction, the soon-to-be-executing process becomes the currently-running process. And thus the context switch is complete.  

A timeline of the entire process is shown in Figure 6.3. In this example, Process A is running and then is interrupted by the timer interrupt. The hardware saves its registers (onto its kernel stack) and enters the kernel (switching to kernel mode). In the timer interrupt handler, the OS decides to switch from running Process A to Process B. At that point, it calls the switch() routine, which carefully saves current register values (into the process structure of A), restores the registers of Process B (from its process structure entry), and then switches contexts, specifically by changing the stack pointer to use B’s kernel stack (and not A’s). Finally, the OS returnsfrom-trap, which restores B’s registers and starts running it.  

Note that there are two types of register saves/restores that happen during this protocol. The first is when the timer interrupt occurs; in this case, the user registers of the running process are implicitly saved by the hardware, using the kernel stack of that process. The second is when the OS decides to switch from A to B; in this case, the kernel registers are explicitly saved by the software (i.e., the OS), but this time into memory in the process structure of the process. The latter action moves the system from running as if it just trapped into the kernel from A to as if it just trapped into the kernel from B.  

To give you a better sense of how such a switch is enacted, Figure 6.4 shows the context switch code for xv6. See if you can make sense of it (you’ll have to know a bit of $\times 8 6$ , as well as some xv6, to do so). The context structures old and new are found in the old and new process’s process structures, respectively.  

OPERATINGSYSTEMS[VERSION 1.10]  

<html><body><table><tr><td>OS @ boot (kernel mode)</td><td>Hardware</td><td></td></tr><tr><td>initialize trap table</td><td>remember addresses of... syscall handler timer handler</td><td></td></tr><tr><td>start interrupt timer</td><td>start timer interrupt CPU in X ms</td><td></td></tr><tr><td>OS @ run (kernel mode)</td><td>Hardware</td><td>Program (user mode) Process A</td></tr><tr><td>Handle the trap</td><td>timer interrupt save regs(A) -> k-stack(A) move to kernel mode jump to trap handler</td><td></td></tr><tr><td>Call switch() routine save regs(A) > proc_t(A) restore regs(B)  proc_t(B) switch to k-stack(B)</td><td></td><td></td></tr><tr><td>return-from-trap (into B)</td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>restore regs(B)  k-stack(B)</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>move to user mode</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>jump to B's PC</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td>Process B</td></tr><tr><td></td><td></td><td></td></tr></table></body></html>  

