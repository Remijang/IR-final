# 44.2 From Bits to Banks/Planes  

As they say in ancient Greece, storing a single bit (or a few) does not a storage system make. Hence, flash chips are organized into banks or planes which consist of a large number of cells.  

A bank is accessed in two different sized units: blocks (sometimes called erase blocks), which are typically of size 128 KB or 256 KB, and pages, which are a few KB in size (e.g., 4KB). Within each bank there are a large number of blocks; within each block, there are a large number of pages. When thinking about flash, you must remember this new terminology, which is different than the blocks we refer to in disks and RAIDs and the pages we refer to in virtual memory.  

Figure 44.1 shows an example of a flash plane with blocks and pages; there are three blocks, each containing four pages, in this simple example. We’ll see below why we distinguish between blocks and pages; it turns out this distinction is critical for flash operations such as reading and writing, and even more so for the overall performance of the device. The most important (and weird) thing you will learn is that to write to a page within a block, you first have to erase the entire block; this tricky detail makes building a flash-based SSD an interesting and worthwhile challenge, and the subject of the second-half of the chapter.  

![](images/e13c42669ed12d57b61a597dc872ee2d0d7fe5c0eee80bb2337607dc2c105e18.jpg)  
Figure 44.1: A Simple Flash Chip: Pages Within Blocks  

OPERATINGSYSTEMS[VERSION 1.10]  

