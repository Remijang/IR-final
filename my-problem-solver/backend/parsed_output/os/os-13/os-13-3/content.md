# 13.3 The Address Space  

However, we have to keep those pesky users in mind, and doing so requires the OS to create an easy to use abstraction of physical memory. We call this abstraction the address space, and it is the running program’s view of memory in the system. Understanding this fundamental OS abstraction of memory is key to understanding how memory is virtualized.  

The address space of a process contains all of the memory state of the running program. For example, the code of the program (the instructions) have to live in memory somewhere, and thus they are in the address space. The program, while it is running, uses a stack to keep track of where it is in the function call chain as well as to allocate local variables and pass parameters and return values to and from routines. Finally, the heap is used for dynamically-allocated, user-managed memory, such as that you might receive from a call to malloc() in C or new in an objectoriented language such as $C { + } { + }$ or Java. Of course, there are other things in there too (e.g., statically-initialized variables), but for now let us just assume those three components: code, stack, and heap.  

In the example in Figure 13.3 (page 4), we have a tiny address space (only 16KB)1. The program code lives at the top of the address space (starting at 0 in this example, and is packed into the first 1K of the address space). Code is static (and thus easy to place in memory), so we can place it at the top of the address space and know that it won’t need any more space as the program runs.  

![](images/5534266a392b5e64570a563abd6abaab22604b0274c9977d64ddd1ed1fc3d115.jpg)  
Figure 13.3: An Example Address Space  

Next, we have the two regions of the address space that may grow (and shrink) while the program runs. Those are the heap (at the top) and the stack (at the bottom). We place them like this because each wishes to be able to grow, and by putting them at opposite ends of the address space, we can allow such growth: they just have to grow in opposite directions. The heap thus starts just after the code (at 1KB) and grows downward (say when a user requests more memory via malloc()); the stack starts at 16KB and grows upward (say when a user makes a procedure call). However, this placement of stack and heap is just a convention; you could arrange the address space in a different way if you’d like (as we’ll see later, when multiple threads co-exist in an address space, no nice way to divide the address space like this works anymore, alas).  

Of course, when we describe the address space, what we are describing is the abstraction that the OS is providing to the running program. The program really isn’t in memory at physical addresses 0 through 16KB; rather it is loaded at some arbitrary physical address(es). Examine processes A, B, and C in Figure 13.2; there you can see how each process is loaded into memory at a different address. And hence the problem:  

OPERATINGSYSTEMS[VERSION 1.10]  

THE CRUX: HOW TO VIRTUALIZE MEMORY  

How can the OS build this abstraction of a private, potentially large address space for multiple running processes (all sharing memory) on top of a single, physical memory?  

When the OS does this, we say the OS is virtualizing memory, because the running program thinks it is loaded into memory at a particular address (say 0) and has a potentially very large address space (say 32-bits or 64-bits); the reality is quite different.  

When, for example, process A in Figure 13.2 tries to perform a load at address 0 (which we will call a virtual address), somehow the OS, in tandem with some hardware support, will have to make sure the load doesn’t actually go to physical address 0 but rather to physical address 320KB (where A is loaded into memory). This is the key to virtualization of memory, which underlies every modern computer system in the world.  

