# 4.1 The Abstraction: A Process  

The abstraction provided by the OS of a running program is something we will call a process. As we said above, a process is simply a running program; at any instant in time, we can summarize a process by taking an inventory of the different pieces of the system it accesses or affects during the course of its execution.  

To understand what constitutes a process, we thus have to understand its machine state: what a program can read or update when it is running. At any given time, what parts of the machine are important to the execution of this program?  

One obvious component of machine state that comprises a process is its memory. Instructions lie in memory; the data that the running program reads and writes sits in memory as well. Thus the memory that the process can address (called its address space) is part of the process.  

Also part of the process’s machine state are registers; many instructions explicitly read or update registers and thus clearly they are important to the execution of the process.  

Note that there are some particularly special registers that form part of this machine state. For example, the program counter (PC) (sometimes called the instruction pointer or IP) tells us which instruction of the program will execute next; similarly a stack pointer and associated frame  

OPERATINGSYSTEMS[VERSION 1.10]  

# TIP: SEPARATE POLICY AND MECHANISM  

In many operating systems, a common design paradigm is to separate high-level policies from their low-level mechanisms $\bar { [ \mathrm { L } + 7 5 ] }$ . You can think of the mechanism as providing the answer to a how question about a system; for example, how does an operating system perform a context switch? The policy provides the answer to a which question; for example, which process should the operating system run right now? Separating the two allows one easily to change policies without having to rethink the mechanism and is thus a form of modularity, a general software design principle.  

pointer are used to manage the stack for function parameters, local variables, and return addresses.  

Finally, programs often access persistent storage devices too. Such I/O information might include a list of the files the process currently has open.  

