# 18.1 A Simple Example And Overview  

To help make this approach more clear, let’s illustrate it with a simple example. Figure 18.1 (page 2) presents an example of a tiny address space, only 64 bytes total in size, with four 16-byte pages (virtual pages 0, 1, 2, and 3). Real address spaces are much bigger, of course, commonly 32 bits and thus 4-GB of address space, or even $\bar { 6 4 } \mathrm { b i t s } ^ { 1 }$ ; in the book, we’ll often use tiny examples to make them easier to digest.  

![](images/e565e78535184ec80ea25ba5b84bbeb13613811dafc023e49cf44e790879852a.jpg)  
Figure 18.1: A Simple 64-byte Address Space  

Physical memory, as shown in Figure 18.2, also consists of a number of fixed-sized slots, in this case eight page frames (making for a 128-byte physical memory, also ridiculously small). As you can see in the diagram, the pages of the virtual address space have been placed at different locations throughout physical memory; the diagram also shows the OS using some of physical memory for itself.  

Paging, as we will see, has a number of advantages over our previous approaches. Probably the most important improvement will be flexibility: with a fully-developed paging approach, the system will be able to support the abstraction of an address space effectively, regardless of how a process uses the address space; we won’t, for example, make assumptions about the direction the heap and stack grow and how they are used.  

![](images/728af40db9c1ebfdb57d788252dc847c5da4cf5a06bb090ec49a91aac0b3d441.jpg)  
Figure 18.2: A 64-Byte Address Space In A 128-Byte Physical Memory  

OPERATINGSYSTEMS[VERSION 1.10]  

Another advantage is the simplicity of free-space management that paging affords. For example, when the OS wishes to place our tiny 64-byte address space into our eight-page physical memory, it simply finds four free pages; perhaps the OS keeps a free list of all free pages for this, and just grabs the first four free pages off of this list. In the example, the OS has placed virtual page 0 of the address space (AS) in physical frame 3, virtual page 1 of the AS in physical frame 7, page 2 in frame 5, and page 3 in frame 2. Page frames 1, 4, and 6 are currently free.  

To record where each virtual page of the address space is placed in physical memory, the operating system usually keeps a per-process data structure known as a page table. The major role of the page table is to store address translations for each of the virtual pages of the address space, thus letting us know where in physical memory each page resides. For our simple example (Figure 18.2, page 2), the page table would thus have the following four entries: (Virtual Page $0 \stackrel { - } {  }$ Physical Frame 3), ( $\mathrm { V P } \ 1  \mathrm { P F } \ 7$ ), $( \mathrm { V P } 2  \mathrm { P F } 5 ,$ ), and $( \mathrm { V P } 3  \mathrm { P } \bar { \mathrm { F } } 2 ,$ ).  

It is important to remember that this page table is a per-process data structure (most page table structures we discuss are per-process structures; an exception we’ll touch on is the inverted page table). If another process were to run in our example above, the OS would have to manage a different page table for it, as its virtual pages obviously map to different physical pages (modulo any sharing going on).  

Now, we know enough to perform an address-translation example. Let’s imagine the process with that tiny address space (64 bytes) is performing a memory access:  

movl <virtual address>, %eax  

Specifically, let’s pay attention to the explicit load of the data from address <virtual address $>$ into the register eax (and thus ignore the instruction fetch that must have happened prior).  

To translate this virtual address that the process generated, we have to first split it into two components: the virtual page number (VPN), and the offset within the page. For this example, because the virtual address space of the process is 64 bytes, we need 6 bits total for our virtual address $( 2 ^ { 6 } ~ = ~ 6 4 )$ ). Thus, our virtual address can be conceptualized as follows:  

<html><body><table><tr><td>Va5</td><td>Va4</td><td>Va3</td><td>Va2</td><td>Va1</td><td>Va0</td></tr></table></body></html>  

In this diagram, Va5 is the highest-order bit of the virtual address, and Va0 the lowest-order bit. Because we know the page size (16 bytes), we can further divide the virtual address as follows:  

![](images/e9a10421971b2a000cb0d838c670a1e993b23a295841c95f767ad40099b4b29f.jpg)  

THREE EASY PIECES  

The page size is 16 bytes in a 64-byte address space; thus we need to be able to select 4 pages, and the top 2 bits of the address do just that. Thus, we have a 2-bit virtual page number (VPN). The remaining bits tell us which byte of the page we are interested in, 4 bits in this case; we call this the offset.  

When a process generates a virtual address, the OS and hardware must combine to translate it into a meaningful physical address. For example, let us assume the load above was to virtual address 21:  

movl 21, %eax  

Turning $^ { \prime \prime } 2 1 ^ { \prime \prime }$ into binary form, we get $^ { \prime \prime } 0 1 0 1 0 1 ^ { \prime \prime }$ , and thus we can examine this virtual address and see how it breaks down into a virtual page number (VPN) and offset:  

![](images/86eccba66243a4a2e335a30973a584f8a6c4aac1b586b401d74b6151a38be5bf.jpg)  

Thus, the virtual address $^ { \prime \prime } 2 1 ^ { \prime \prime }$ is on the 5th $( ^ { \prime \prime } 0 1 0 1 ^ { \prime \prime } \mathrm { t h } )$ byte of virtual page $^ { \prime \prime } 0 1 ^ { \prime \prime }$ (or 1). With our virtual page number, we can now index our page table and find which physical frame virtual page 1 resides within. In the page table above the physical frame number (PFN) (also sometimes called the physical page number or PPN) is 7 (binary 111). Thus, we can translate this virtual address by replacing the VPN with the PFN and then issue the load to physical memory (Figure 18.3).  

![](images/71d0e873deb07c75524839985ca13b09b4a21cb1b2bdfdf7052b71c298f3c357.jpg)  
Figure 18.3: The Address Translation Process  

OPERATINGSYSTEMS[VERSION 1.10]  

![](images/094c236f2afe41eec9e1ae3e46d2a7fdb0475a9e8658dc203f6a45b51844e456.jpg)  
Figure 18.4: Example: Page Table in Kernel Physical Memory  

Note the offset stays the same (i.e., it is not translated), because the offset just tells us which byte within the page we want. Our final physical address is 1110101 (117 in decimal), and is exactly where we want our load to fetch data from (Figure 18.2, page 2).  

With this basic overview in mind, we can now ask (and hopefully, answer) a few basic questions you may have about paging. For example, where are these page tables stored? What are the typical contents of the page table, and how big are the tables? Does paging make the system (too) slow? These and other beguiling questions are answered, at least in part, in the text below. Read on!  

