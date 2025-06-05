# 18.4 Paging: Also Too Slow  

With page tables in memory, we already know that they might be too big. As it turns out, they can slow things down too. For example, take our simple instruction:  

movl 21, %eax  

Again, let’s just examine the explicit reference to address 21 and not worry about the instruction fetch. In this example, we’ll assume the hardware performs the translation for us. To fetch the desired data, the system must first translate the virtual address (21) into the correct physical address (117). Thus, before fetching the data from address 117, the system must first fetch the proper page table entry from the process’s page table, perform the translation, and then load the data from physical memory.  

To do so, the hardware must know where the page table is for the currently-running process. Let’s assume for now that a single page-table base register contains the physical address of the starting location of the page table. To find the location of the desired PTE, the hardware will thus perform the following functions:  

VPN $\mathbf { \Sigma } = \mathbf { \Sigma }$ (VirtualAddress & VPN_MASK) $> >$ SHIFT PTEAddr $\mathbf { \Sigma } = \mathbf { \Sigma }$ PageTableBaseRegister $^ +$ (VPN $\star$ sizeof(PTE))  

In our example, VPN MASK would be set to $0 { \times } 3 0$ (hex 30, or binary 110000) which picks out the VPN bits from the full virtual address; SHIFT is set to 4 (the number of bits in the offset), such that we move the VPN bits down to form the correct integer virtual page number. For example, with virtual address 21 (010101), and masking turns this value into 010000; the shift turns it into 01, or virtual page 1, as desired. We then use this value as an index into the array of PTEs pointed to by the page table base register.  

Once this physical address is known, the hardware can fetch the PTE from memory, extract the PFN, and concatenate it with the offset from the virtual address to form the desired physical address. Specifically, you can think of the PFN being left-shifted by SHIFT, and then bitwise OR’d with the offset to form the final address as follows:  

offset $\mathbf { \Sigma } = \mathbf { \Sigma }$ VirtualAddress & OFFSET_MASK PhysAddr $\mathbf { \Sigma } = \mathbf { \Sigma }$ (PFN << SHIFT) | offset  

Finally, the hardware can fetch the desired data from memory and put it into register eax. The program has now succeeded at loading a value from memory!  

To summarize, we now describe the initial protocol for what happens on each memory reference. Figure 18.6 (page 9) shows the approach. For every memory reference (whether an instruction fetch or an explicit load or store), paging requires us to perform one extra memory reference in order to first fetch the translation from the page table. That is a lot of  

OPERATINGSYSTEMS[VERSION 1.10]  

![](images/3140db2ae2b5f9eac76b4f071264bc52acd71e5b11588238821273f51a63d896.jpg)  
Figure 18.6: Accessing Memory With Paging  

work! Extra memory references are costly, and in this case will likely slow down the process by a factor of two or more.  

And now you can hopefully see that there are two real problems that we must solve. Without careful design of both hardware and software, page tables will cause the system to run too slowly, as well as take up too much memory. While seemingly a great solution for our memory virtualization needs, these two crucial problems must first be overcome.  

