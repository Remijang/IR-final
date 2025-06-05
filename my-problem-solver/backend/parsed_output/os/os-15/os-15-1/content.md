# 15.1 Assumptions  

Our first attempts at virtualizing memory will be very simple, almost laughably so. Go ahead, laugh all you want; pretty soon it will be the OS laughing at you, when you try to understand the ins and outs of TLBs, multi-level page tables, and other technical wonders. Don’t like the idea of the OS laughing at you? Well, you may be out of luck then; that’s just how the OS rolls.  

Specifically, we will assume for now that the user’s address space must be placed contiguously in physical memory. We will also assume, for simplicity, that the size of the address space is not too big; specifically, that it is less than the size of physical memory. Finally, we will also assume that each address space is exactly the same size. Don’t worry if these assumptions sound unrealistic; we will relax them as we go, thus achieving a realistic virtualization of memory.  

