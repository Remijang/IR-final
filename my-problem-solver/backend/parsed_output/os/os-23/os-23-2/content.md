# 23.2 The Linux Virtual Memory System  

We’ll now discuss some of the more interesting aspects of the Linux VM system. Linux development has been driven forward by real engineers solving real problems encountered in production, and thus a large number of features have slowly been incorporated into what is now a fully functional, feature-filled virtual memory system.  

While we won’t be able to discuss every aspect of Linux VM, we’ll touch on the most important ones, especially where it has gone beyond what is found in classic VM systems such as VAX/VMS. We’ll also try to highlight commonalities between Linux and older systems.  

For this discussion, we’ll focus on Linux for Intel $\dot { \times } 8 6$ . While Linux can and does run on many different processor architectures, Linux on $\times 8 6$ is its most dominant and important deployment, and thus the focus of our attention.  

# The Linux Address Space  

Much like other modern operating systems, and also like VAX/VMS, a Linux virtual address space1 consists of a user portion (where user program code, stack, heap, and other parts reside) and a kernel portion (where kernel code, stacks, heap, and other parts reside). Like those other systems, upon a context switch, the user portion of the currently-running address space changes; the kernel portion is the same across processes. Like those other systems, a program running in user mode cannot access kernel virtual pages; only by trapping into the kernel and transitioning to privileged mode can such memory be accessed.  

![](images/91865c6bcdb34f1d250fdc49b2dff291732f9fda85f77926156b1c2f6c5ab1f6.jpg)  
Figure 23.2: The Linux Address Space  

In classic 32-bit Linux (i.e., Linux with a 32-bit virtual address space), the split between user and kernel portions of the address space takes place at address $0 \mathbf { x } { \mathsf { C } } 0 0 0 0 0 0 0 0 ,$ or three-quarters of the way through the address space. Thus, virtual addresses 0 through 0xBFFFFFFF are user virtual addresses; the remaining virtual addresses ( $\operatorname { 0 } \mathrm { { x C } } 0 0 0 0 0 0 0$ through 0xFFFFFFFF) are in the kernel’s virtual address space. 64-bit Linux has a similar split but at slightly different points. Figure 23.2 shows a depiction of a typical (simplified) address space.  

One slightly interesting aspect of Linux is that it contains two types of kernel virtual addresses. The first are known as kernel logical addresses [O16]. This is what you would consider the normal virtual address space of the kernel; to get more memory of this type, kernel code merely needs to call kmalloc. Most kernel data structures live here, such as page tables, per-process kernel stacks, and so forth. Unlike most other memory in the system, kernel logical memory cannot be swapped to disk.  

The most interesting aspect of kernel logical addresses is their connection to physical memory. Specifically, there is a direct mapping between kernel logical addresses and the first portion of physical memory. Thus, kernel logical address $0 \times 0 0 0 0 0 0 0$ translates to physical address  

$0 \times 0 0 0 0 0 0 0 0$ , $0 \mathbf { x } \mathbf { C } 0 0 0 0 \mathbf { F } \mathbf { F } \mathbf { F }$ to $0 { \times } 0 0 0 0 0 0 \mathrm { { F F } , }$ and so forth. This direct mapping has two implications. The first is that it is simple to translate back and forth between kernel logical addresses and physical addresses; as a result, these addresses are often treated as if they are indeed physical. The second is that if a chunk of memory is contiguous in kernel logical address space, it is also contiguous in physical memory. This makes memory allocated in this part of the kernel’s address space suitable for operations which need contiguous physical memory to work correctly, such as I/O transfers to and from devices via direct memory access (DMA) (something we’ll learn about in the third part of this book).  

The other type of kernel address is a kernel virtual address. To get memory of this type, kernel code calls a different allocator, vmalloc, which returns a pointer to a virtually contiguous region of the desired size. Unlike kernel logical memory, kernel virtual memory is usually not contiguous; each kernel virtual page may map to non-contiguous physical pages (and is thus not suitable for DMA). However, such memory is easier to allocate as a result, and thus used for large buffers where finding a contiguous large chunk of physical memory would be challenging.  

In 32-bit Linux, one other reason for the existence of kernel virtual addresses is that they enable the kernel to address more than (roughly) 1 GB of memory. Years ago, machines had much less memory than this, and enabling access to more than 1 GB was not an issue. However, technology progressed, and soon there was a need to enable the kernel to use larger amounts of memory. Kernel virtual addresses, and their disconnection from a strict one-to-one mapping to physical memory, make this possible. However, with the move to 64-bit Linux, the need is less urgent, because the kernel is not confined to only the last 1 GB of the virtual address space.  

# Page Table Structure  

Because we are focused on Linux for $\times 8 6 ,$ our discussion will center on the type of page-table structure provided by $\mathbf { \boldsymbol { x } } 8 6 ,$ , as it determines what Linux can and cannot do. As mentioned before, $\times 8 6$ provides a hardwaremanaged, multi-level page table structure, with one page table per process; the OS simply sets up mappings in its memory, points a privileged register at the start of the page directory, and the hardware handles the rest. The OS gets involved, as expected, at process creation, deletion, and upon context switches, making sure in each case that the correct page table is being used by the hardware MMU to perform translations.  

Probably the biggest change in recent years is the move from 32-bit $\times 8 6$ to 64-bit $\times 8 6$ , as briefly mentioned above. As seen in the VAX/VMS system, 32-bit address spaces have been around for a long time, and as technology changed, they were finally starting to become a real limit for programs. Virtual memory makes it easy to program systems, but with modern systems containing many GB of memory, 32 bits were no longer enough to refer to each of them. Thus, the next leap became necessary.  

OPERATINGSYSTEMS[VERSION 1.10]  

Moving to a 64-bit address affects page table structure in $\times 8 6$ in the expected manner. Because $\times 8 6$ uses a multi-level page table, current 64- bit systems use a four-level table. The full 64-bit nature of the virtual address space is not yet in use, however, rather only the bottom 48 bits. Thus, a virtual address can be viewed as follows:  

![](images/1e2494b8cfa3eeaa849d42b769330bbf666d68d02870135e11d015c5861027f9.jpg)  

As you can see in the picture, the top 16 bits of a virtual address are unused (and thus play no role in translation), the bottom 12 bits (due to the 4-KB page size) are used as the offset (and hence just used directly, and not translated), leaving the middle 36 bits of virtual address to take part in the translation. The P1 portion of the address is used to index into the topmost page directory, and the translation proceeds from there, one level at a time, until the actual page of the page table is indexed by P4, yielding the desired page table entry.  

As system memories grow even larger, more parts of this voluminous address space will become enabled, leading to five-level and eventually six-level page-table tree structures. Imagine that: a simple page table lookup requiring six levels of translation, just to figure out where in memory a certain piece of data resides.  

# Large Page Support  

Intel $\times 8 6$ allows for the use of multiple page sizes, not just the standard 4- KB page. Specifically, recent designs support 2-MB and even 1-GB pages in hardware. Thus, over time, Linux has evolved to allow applications to utilize these huge pages (as they are called in the world of Linux).  

Using huge pages, as hinted at earlier, leads to numerous benefits. As seen in VAX/VMS, doing so reduces the number of mappings that are needed in the page table; the larger the pages, the fewer the mappings. However, fewer page-table entries is not the driving force behind huge pages; rather, it’s better TLB behavior and related performance gains.  

When a process actively uses a large amount of memory, it quickly fills up the TLB with translations. If those translations are for 4-KB pages, only a small amount of total memory can be accessed without inducing TLB misses. The result, for modern “big memory” workloads running on machines with many GBs of memory, is a noticeable performance cost; recent research shows that some applications spend $1 \mathrm { \bar { 0 } \% }$ of their cycles servicing TLB misses $\left[ \mathsf { B } { + } 1 3 \right]$ .  

Huge pages allow a process to access a large tract of memory without TLB misses, by using fewer slots in the TLB, and thus is the main advantage. However, there are other benefits to huge pages: there is a shorter TLB-miss path, meaning that when a TLB miss does occur, it is  

# TIP: CONSIDER INCREMENTALISM  

Many times in life, you are encouraged to be a revolutionary. “Think big!”, they say. “Change the world!”, they scream. And you can see why it is appealing; in some cases, big changes are needed, and thus pushing hard for them makes a lot of sense. And, if you try it this way, at least they might stop yelling at you.  

However, in many cases, a slower, more incremental approach might be the right thing to do. The Linux huge page example in this chapter is an example of engineering incrementalism; instead of taking the stance of a fundamentalist and insisting large pages were the way of the future, developers took the measured approach of first introducing specialized support for it, learning more about its upsides and downsides, and, only when there was real reason for it, adding more generic support for all applications.  

Incrementalism, while sometimes scorned, often leads to slow, thoughtful, and sensible progress. When building systems, such an approach might just be the thing you need. Indeed, this may be true in life as well.  

serviced more quickly. In addition, allocation can be quite fast (in certain scenarios), a small but sometimes important benefit.  

One interesting aspect of Linux support for huge pages is how it was done incrementally. At first, Linux developers knew such support was only important for a few applications, such as large databases with stringent performance demands. Thus, the decision was made to allow applications to explicitly request memory allocations with large pages (either through the mmap() or shmget() calls). In this way, most applications would be unaffected (and continue to use only 4-KB pages); a few demanding applications would have to be changed to use these interfaces, but for them it would be worth the pain.  

More recently, as the need for better TLB behavior is more common among many applications, Linux developers have added transparent huge page support. When this feature is enabled, the operating system automatically looks for opportunities to allocate huge pages (usually 2 MB, but on some systems, 1 GB) without requiring application modification.  

Huge pages are not without their costs. The biggest potential cost is internal fragmentation, i.e., a page that is large but sparsely used. This form of waste can fill memory with large but little used pages. Swapping, if enabled, also does not work well with huge pages, sometimes greatly amplifying the amount of I/O a system does. Overhead of allocation can also be bad (in some other cases). Overall, one thing is clear: the 4- KB page size which served systems so well for so many years is not the universal solution it once was; growing memory sizes demand that we consider large pages and other solutions as part of a necessary evolution of VM systems. Linux’s slow adoption of this hardware-based technology is evidence of the coming change.  

OPERATINGSYSTEMS[VERSION 1.10]  

# The Page Cache  

To reduce costs of accessing persistent storage (the focus of the third part of this book), most systems use aggressive caching subsystems to keep popular data items in memory. Linux, in this regard, is no different than traditional operating systems.  

The Linux page cache is unified, keeping pages in memory from three primary sources: memory-mapped files, file data and metadata from devices (usually accessed by directing read() and write() calls to the file system), and heap and stack pages that comprise each process (sometimes called anonymous memory, because there is no named file underneath of it, but rather swap space). These entities are kept in a page cache hash table, allowing for quick lookup when said data is needed.  

The page cache tracks if entries are clean (read but not updated) or dirty (a.k.a., modified). Dirty data is periodically written to the backing store (i.e., to a specific file for file data, or to swap space for anonymous regions) by background threads (called pdflush), thus ensuring that modified data eventually is written back to persistent storage. This background activity either takes place after a certain time period or if too many pages are considered dirty (both configurable parameters).  

In some cases, a system runs low on memory, and Linux has to decide which pages to kick out of memory to free up space. To do so, Linux uses a modified form of 2Q replacement [JS94], which we describe here.  

The basic idea is simple: standard LRU replacement is effective, but can be subverted by certain common access patterns. For example, if a process repeatedly accesses a large file (especially one that is nearly the size of memory, or larger), LRU will kick every other file out of memory. Even worse: retaining portions of this file in memory isn’t useful, as they are never re-referenced before getting kicked out of memory.  

The Linux version of the 2Q replacement algorithm solves this problem by keeping two lists, and dividing memory between them. When accessed for the first time, a page is placed on one queue (called A1 in the original paper, but the inactive list in Linux); when it is re-referenced, the page is promoted to the other queue (called Aq in the original, but the active list in Linux). When replacement needs to take place, the candidate for replacement is taken from the inactive list. Linux also periodically moves pages from the bottom of the active list to the inactive list, keeping the active list to about two-thirds of the total page cache size [G04].  

Linux would ideally manage these lists in perfect LRU order, but, as discussed in earlier chapters, doing so is costly. Thus, as with many OSes, an approximation of LRU (similar to clock replacement) is used.  

This 2Q approach generally behaves quite a bit like LRU, but notably handles the case where a cyclic large-file access occurs by confining the pages of that cyclic access to the inactive list. Because said pages are never re-referenced before getting kicked out of memory, they do not flush out other useful pages found in the active list.  

# ASIDE: THE UBIQUITY OF MEMORY-MAPPING  

Memory mapping predates Linux by some years, and is used in many places within Linux and other modern systems. The idea is simple: by calling mmap() on an already opened file descriptor, a process is returned a pointer to the beginning of a region of virtual memory where the contents of the file seem to be located. By then using that pointer, a process can access any part of the file with a simple pointer dereference.  

Accesses to parts of a memory-mapped file that have not yet been brought into memory trigger page faults, at which point the OS will page in the relevant data and make it accessible by updating the page table of the process accordingly (i.e., demand paging).  

Every regular Linux process uses memory-mapped files, even though the code in main() does not call mmap() directly, because of how Linux loads code from the executable and shared library code into memory. Below is the (highly abbreviated) output of the pmap command line tool, which shows what different mapping comprise the virtual address space of a running program (the shell, in this example, tcsh). The output shows four columns: the virtual address of the mapping, its size, the protection bits of the region, and the source of the mapping:  

0000000000400000 372K r-x-- tcsh  
00000000019d5000 1780K rw--- [anon ]  
00007f4e7cf06000 1792K r-x-- libc-2.23.so  
00007f4e7d2d0000 36K r-x-- libcrypt-2.23.so  
00007f4e7d508000 148K r-x-- libtinfo.so.5.9  
00007f4e7d731000 152K r-x-- ld-2.23.so  
00007f4e7d932000 16K rw-- [stack ]  

As you can see from this output, the code from the tcsh binary, as well as code from libc, libcrypt, libtinfo, and code from the dynamic linker itself (ld.so) are all mapped into the address space. Also present are two anonymous regions, the heap (the second entry, labeled anon) and the stack (labeled stack). Memory-mapped files provide a straightforward and efficient way for the OS to construct a modern address space.  

# Security And Buffer Overflows  

Probably the biggest difference between modern VM systems (Linux, Solaris, or one of the BSD variants) and ancient ones (VAX/VMS) is the emphasis on security in the modern era. Protection has always been a serious concern for operating systems, but with machines more interconnected than ever, it is no surprise that developers have implemented a variety of defensive countermeasures to halt those wily hackers from gaining control of systems.  

OPERATINGSYSTEMS[VERSION 1.10]  

One major threat is found in buffer overflow attacks2, which can be used against normal user programs and even the kernel itself. The idea of these attacks is to find a bug in the target system which lets the attacker inject arbitrary data into the target’s address space. Such vulnerabilities sometime arise because the developer assumes (erroneously) that an input will not be overly long, and thus (trustingly) copies the input into a buffer; because the input is in fact too long, it overflows the buffer, thus overwriting memory of the target. Code as innocent as the below can be the source of the problem:  

int some_function(char \*input) {char dest_buffer[100];strcpy(dest_buffer, input); // oops, unbounded copy!  
}  

In many cases, such an overflow is not catastrophic, e.g., bad input innocently given to a user program or even the OS will probably cause it to crash, but no worse. However, malicious programmers can carefully craft the input that overflows the buffer so as to inject their own code into the targeted system, essentially allowing them to take it over and do their own bidding. If successful upon a network-connected user program, attackers can run arbitrary computations or even rent out cycles on the compromised system; if successful upon the operating system itself, the attack can access even more resources, and is a form of what is called privilege escalation (i.e., user code gaining kernel access rights). If you can’t guess, these are all Bad Things.  

The first and most simple defense against buffer overflow is to prevent execution of any code found within certain regions of an address space (e.g., within the stack). The NX bit (for No-eXecute), introduced by AMD into their version of $\times 8 6$ (a similar XD bit is now available on Intel’s), is one such defense; it just prevents execution from any page which has this bit set in its corresponding page table entry. The approach prevents code, injected by an attacker into the target’s stack, from being executed, and thus mitigates the problem.  

However, clever attackers are ... clever, and even when injected code cannot be added explicitly by the attacker, arbitrary code sequences can be executed by malicious code. The idea is known, in its most general form, as return-oriented programming (ROP) [S07], and really it is quite brilliant. The observation behind ROP is that there are lots of bits of code (gadgets, in ROP terminology) within any program’s address space, especially C programs that link with the voluminous C library. Thus, an attacker can overwrite the stack such that the return address in the currently executing function points to a desired malicious instruction (or series of instructions), followed by a return instruction. By stringing together a large number of gadgets (i.e., ensuring each return jumps to the next gadget), the attacker can execute arbitrary code. Amazing!  

To defend against ROP (including its earlier form, the return-to-libc attack $\left[ { \mathsf { S } } { + } { 0 4 } \right] .$ ), Linux (and other systems) add another defense, known as address space layout randomization (ASLR). Instead of placing code, stack, and the heap at fixed locations within the virtual address space, the OS randomizes their placement, thus making it quite challenging to craft the intricate code sequence required to implement this class of attacks. Most attacks on vulnerable user programs will thus cause crashes, but not be able to gain control of the running program.  

Interestingly, you can observe this randomness in practice rather easily. Here’s a piece of code that demonstrates it on a modern Linux system:  

int main(int argc, char \*argv[]) { int stack $\mathit { \Theta } = \mathit { \Theta } 0$ ; printf("%p\n", &stack); return 0;   
}  

This code just prints out the (virtual) address of a variable on the stack. In older non-ASLR systems, this value would be the same each time. But, as you can see below, the value changes with each run:  

prompt> ./random 0x7ffd3e55d2b4 prompt> ./random 0x7ffe1033b8f4 prompt> ./random 0x7ffe45522e94  

ASLR is such a useful defense for user-level programs that it has also been incorporated into the kernel, in a feature unimaginatively called kernel address space layout randomization (KASLR). However, it turns out the kernel may have even bigger problems to handle, as we discuss next.  

# Other Security Problems: Meltdown And Spectre  

As we write these words (August, 2018), the world of systems security has been turned upside down by two new and related attacks. The first is called Meltdown, and the second Spectre. They were discovered at about the same time by four different groups of researchers/engineers, and have led to deep questioning of the fundamental protections offered by computer hardware and the OS above. See spectreattack.com for papers describing each attack in detail; Spectre is considered the more problematic of the two.  

OPERATINGSYSTEMS[VERSION 1.10]  

The general weakness exploited in each of these attacks is that the CPUs found in modern systems perform all sorts of crazy behind-thescenes tricks to improve performance. One class of technique that lies at the core of the problem is called speculative execution, in which the CPU guesses which instructions will soon be executed in the future, and starts executing them ahead of time. If the guesses are correct, the program runs faster; if not, the CPU undoes their effects on architectural state (e.g., registers) and tries again, this time going down the right path.  

The problem with speculation is that it tends to leave traces of its execution in various parts of the system, such as processor caches, branch predictors, etc. And thus the problem: as the authors of the attacks show, such state can make vulnerable the contents of memory, even memory that we thought was protected by the MMU.  

One avenue to increasing kernel protection was thus to remove as much of the kernel address space from each user process and instead have a separate kernel page table for most kernel data (called kernel pagetable isolation, or KPTI) $\left[ \mathrm { G } { + } 1 7 \right]$ . Thus, instead of mapping the kernel’s code and data structures into each process, only the barest minimum is kept therein; when switching into the kernel, then, a switch to the kernel page table is now needed. Doing so improves security and avoids some attack vectors, but at a cost: performance. Switching page tables is costly. Ah, the costs of security: convenience and performance.  

Unfortunately, KPTI doesn’t solve all of the security problems laid out above, just some of them. And simple solutions, such as turning off speculation, would make little sense, because systems would run thousands of times slower. Thus, it is an interesting time to be alive, if systems security is your thing.  

To truly understand these attacks, you’ll (likely) have to learn a lot more first. Begin by understanding modern computer architecture, as found in advanced books on the topic, focusing on speculation and all the mechanisms needed to implement it. Definitely read about the Meltdown and Spectre attacks, at the websites mentioned above; they actually also include a useful primer on speculation, so perhaps are not a bad place to start. And study the operating system for further vulnerabilities. Who knows what problems remain?  

