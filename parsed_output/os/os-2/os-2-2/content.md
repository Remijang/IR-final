# 2.2 Virtualizing Memory  

Now let’s consider memory. The model of physical memory presented by modern machines is very simple. Memory is just an array of bytes; to read memory, one must specify an address to be able to access the data stored there; to write (or update) memory, one must also specify the data to be written to the given address.  

Memory is accessed all the time when a program is running. A program keeps all of its data structures in memory, and accesses them through various instructions, like loads and stores or other explicit instructions that access memory in doing their work. Don’t forget that each instruction of the program is in memory too; thus memory is accessed on each instruction fetch.  

Let’s take a look at a program (in Figure 2.3) that allocates some memory by calling malloc(). The output of this program can be found here:  

prompt> ./mem   
(2134) address pointed to by p: 0x200000   
(2134) p: 1   
(2134) p: 2   
(2134) p: 3   
(2134) p: 4   
(2134) p: 5   
ˆC  

![](images/03380dcff89419c1b4544e5faa1194469280ccf8588fbb4980303f775fe61421.jpg)  
Figure 2.4: Running The Memory Program Multiple Times  

The program does a couple of things. First, it allocates some memory (line a1). Then, it prints out the address of the memory (a2), and then puts the number zero into the first slot of the newly allocated memory (a3). Finally, it loops, delaying for a second and incrementing the value stored at the address held in $\mathrm { ~ p ~ }$ . With every print statement, it also prints out what is called the process identifier (the PID) of the running program. This PID is unique per running process.  

Again, this first result is not too interesting. The newly allocated memory is at address $0 \times 2 0 0 0 0 0$ . As the program runs, it slowly updates the value and prints out the result.  

Now, we again run multiple instances of this same program to see what happens (Figure 2.4). We see from the example that each running program has allocated memory at the same address $( 0 \times 2 0 0 0 0 0 )$ , and yet each seems to be updating the value at $0 \times 2 0 0 0 0 0$ independently! It is as if each running program has its own private memory, instead of sharing the same physical memory with other running programs5.  

Indeed, that is exactly what is happening here as the OS is virtualizing memory. Each process accesses its own private virtual address space (sometimes just called its address space), which the OS somehow maps onto the physical memory of the machine. A memory reference within one running program does not affect the address space of other processes (or the OS itself); as far as the running program is concerned, it has physical memory all to itself. The reality, however, is that physical memory is a shared resource, managed by the operating system. Exactly how all of this is accomplished is also the subject of the first part of this book, on the topic of virtualization.  

