# 53.2 What Are We Protecting?  

We aren’t likely to achieve good protection unless we have a fairly comprehensive view of what we’re trying to protect when we say our operating system should be secure. Fortunately, that question is easy to answer for an operating system, at least at the high level: everything. That answer isn’t very comforting, but it is best to have a realistic understanding of the broad implications of operating system security.  

A typical commodity operating system has complete control of all (or almost all) hardware on the machine and is able to do literally anything the hardware permits. That means it can control the processor, read and write all registers, examine any main memory location, and perform any operation one of its peripherals supports. As a result, among the things the OS can do are:  

• examine or alter any process’s memory   
• read, write, delete or corrupt any file on any writeable persistent storage medium, including hard disks and flash drives   
• change the scheduling or even halt execution of any process   
• send any message to anywhere, including altered versions of those a process wished to send   
• enable or disable any peripheral device  

# ASIDE: SECURITY ENCLAVES  

A little bit back, we said the operating system controls “almost all” the hardware on the machine. That kind of caveat should have gotten you asking, “well, what parts of the hardware doesn’t it control?” Originally, it really was all the hardware. But starting in the 1990s, hardware developer began to see a need to keep some hardware isolated, to a degree, from the operating system. The first such hardware was primarily intended to protect the boot process of the operating system. TPM, or Trusted Platform Module, provided assurance that you were booting the version of the operating system you intended to, protecting you from attacks that tried to boot compromised versions of the system. More recently, more general hardware elements have tried to control what can be done on the machine, typically with some particularly important data, often data that is related to cryptography. Such hardware elements are called security enclaves, since they are meant to allow only safe use of this data, even by the most powerful, trusted code in the system – the operating system itself. They are often used to support operations in a cloud computing environment, where multiple operating systems might be running under virtual machines sharing the same physical hardware. This turns out to be a harder trick than anyone expected. Security tricks usually are. Security enclaves often prove not to provide quite as much isolation as their designers hoped. But the attacks on them tend to be sophisticated and difficult, and usually require the ability to run privileged code on the system already. So even if they don’t achieve their full goals, they do put an extra protective barrier against compromised operating system code.  

• give any process access to any other process’s resources • arbitrarily take away any resource a process controls • respond to any system call with a maximally harmful lie  

In essence, processes are at the mercy of the operating system. It is nearly impossible for a process to ’protect’ any part of itself from a malicious operating system. We typically assume our operating system is not actually malicious2, but a flaw that allows a malicious process to cause the operating system to misbehave is nearly as bad, since it could potentially allow that process to gain any of the powers of the operating system itself. This point should make you think very seriously about the importance of designing secure operating systems and, more commonly, applying security patches to any operating system you are running. Security flaws in your operating system can completely compromise everything about the machine the system runs on, so preventing them and patching any that are found is vitally important.  

