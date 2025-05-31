# 44.1 Storing a Single Bit  

Flash chips are designed to store one or more bits in a single transistor; the level of charge trapped within the transistor is mapped to a binary value. In a single-level cell (SLC) flash, only a single bit is stored within a transistor (i.e., 1 or 0); with a multi-level cell (MLC) flash, two bits are encoded into different levels of charge, e.g., 00, 01, 10, and 11 are represented by low, somewhat low, somewhat high, and high levels. There is even triple-level cell (TLC) flash, which encodes 3 bits per cell. Overall, SLC chips achieve higher performance and are more expensive.  

# TIP: BE CAREFUL WITH TERMINOLOGY  

You may have noticed that some terms we have used many times before (blocks, pages) are being used within the context of a flash, but in slightly different ways than before. New terms are not created to make your life harder (although they may be doing just that), but arise because there is no central authority where terminology decisions are made. What is a block to you may be a page to someone else, and vice versa, depending on the context. Your job is simple: to know the appropriate terms within each domain, and use them such that people well-versed in the discipline can understand what you are talking about. It’s one of those times where the only solution is simple but sometimes painful: use your memory.  

Of course, there are many details as to exactly how such bit-level storage operates, down at the level of device physics. While beyond the scope of this book, you can read more about it on your own [J10].  

