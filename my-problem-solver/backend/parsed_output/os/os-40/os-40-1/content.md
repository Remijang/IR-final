# 40.1 The Way To Think  

To think about file systems, we usually suggest thinking about two different aspects of them; if you understand both of these aspects, you probably understand how the file system basically works.  

The first is the data structures of the file system. In other words, what types of on-disk structures are utilized by the file system to organize its data and metadata? The first file systems we’ll see (including vsfs below) employ simple structures, like arrays of blocks or other objects, whereas  

# ASIDE: MENTAL MODELS OF FILE SYSTEMS  

As we’ve discussed before, mental models are what you are really trying to develop when learning about systems. For file systems, your mental model should eventually include answers to questions like: what on-disk structures store the file system’s data and metadata? What happens when a process opens a file? Which on-disk structures are accessed during a read or write? By working on and improving your mental model, you develop an abstract understanding of what is going on, instead of just trying to understand the specifics of some file-system code (though that is also useful, of course!).  

more sophisticated file systems, like SGI’s XFS, use more complicated tree-based structures $\left[ { \mathsf { S } } { + } { 9 6 } \right]$ .  

The second aspect of a file system is its access methods. How does it map the calls made by a process, such as open(), read(), write(), etc., onto its structures? Which structures are read during the execution of a particular system call? Which are written? How efficiently are all of these steps performed?  

If you understand the data structures and access methods of a file system, you have developed a good mental model of how it truly works, a key part of the systems mindset. Try to work on developing your mental model as we delve into our first implementation.  

