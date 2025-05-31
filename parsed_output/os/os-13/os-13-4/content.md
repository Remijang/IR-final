# 13.4 Goals  

Thus we arrive at the job of the OS in this set of notes: to virtualize memory. The OS will not only virtualize memory, though; it will do so with style. To make sure the OS does so, we need some goals to guide us. We have seen these goals before (think of the Introduction), and we’ll see them again, but they are certainly worth repeating.  

One major goal of a virtual memory (VM) system is transparency2. The OS should implement virtual memory in a way that is invisible to the running program. Thus, the program shouldn’t be aware of the fact that memory is virtualized; rather, the program behaves as if it has its own private physical memory. Behind the scenes, the OS (and hardware) does all the work to multiplex memory among many different jobs, and hence implements the illusion.  

Another goal of VM is efficiency. The OS should strive to make the virtualization as efficient as possible, both in terms of time (i.e., not making programs run much more slowly) and space (i.e., not using too much memory for structures needed to support virtualization). In implementing time-efficient virtualization, the OS will have to rely on hardware support, including hardware features such as TLBs (which we will learn about in due course).  

Finally, a third VM goal is protection. The OS should make sure to protect processes from one another as well as the OS itself from pro  

# TIP: THE PRINCIPLE OF ISOLATION  

Isolation is a key principle in building reliable systems. If two entities are properly isolated from one another, this implies that one can fail without affecting the other. Operating systems strive to isolate processes from each other and in this way prevent one from harming the other. By using memory isolation, the OS further ensures that running programs cannot affect the operation of the underlying OS. Some modern OS’s take isolation even further, by walling off pieces of the OS from other pieces of the OS. Such microkernels [BH70, $\bar { \mathrm { R } } { + } 8 9$ , $S { + } 0 3 { \dot { \mathrm { \Omega } } }$ ] thus may provide greater reliability than typical monolithic kernel designs.  

cesses. When one process performs a load, a store, or an instruction fetch, it should not be able to access or affect in any way the memory contents of any other process or the OS itself (that is, anything outside its address space). Protection thus enables us to deliver the property of isolation among processes; each process should be running in its own isolated cocoon, safe from the ravages of other faulty or even malicious processes.  

In the next chapters, we’ll focus our exploration on the basic mechanisms needed to virtualize memory, including hardware and operating systems support. We’ll also investigate some of the more relevant policies that you’ll encounter in operating systems, including how to manage free space and which pages to kick out of memory when you run low on space. In doing so, we’ll build up your understanding of how a modern virtual memory system really works3.  

