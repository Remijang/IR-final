# 16.3 What About The Stack?  

Thus far, we’ve left out one important component of the address space: the stack. The stack has been relocated to physical address 28KB in the diagram above, but with one critical difference: it grows backwards (i.e., towards lower addresses). In physical memory, it “starts” at $2 8 \mathrm { K B } ^ { 1 }$ and grows back to 26KB, corresponding to virtual addresses 16KB to 14KB; translation must proceed differently.  

The first thing we need is a little extra hardware support. Instead of just base and bounds values, the hardware also needs to know which way the segment grows (a bit, for example, that is set to 1 when the segment grows in the positive direction, and 0 for negative). Our updated view of what the hardware tracks is seen in Figure 16.4:  

Figure 16.4: Segment Registers (With Negative-Growth Support)   


<html><body><table><tr><td>Segment</td><td>Base</td><td>Size (max 4K)</td><td>Grows Positive?</td></tr><tr><td>Codeoo</td><td>32K</td><td>2K</td><td>1</td></tr><tr><td>Heapo1</td><td>34K</td><td>3K</td><td>1</td></tr><tr><td>Stack11</td><td>28K</td><td>2K</td><td>0</td></tr></table></body></html>  

With the hardware understanding that segments can grow in the negative direction, the hardware must now translate such virtual addresses slightly differently. Let’s take an example stack virtual address and translate it to understand the process.  

In this example, assume we wish to access virtual address 15KB, which should map to physical address 27KB. Our virtual address, in binary form, thus looks like this: 11 1100 0000 0000 (hex $0 { \times } 3 { \mathrm { C } } 0 0 \$ ). The hardware uses the top two bits (11) to designate the segment, but then we are left with an offset of 3KB. To obtain the correct negative offset, we must subtract the maximum segment size from 3KB: in this example, a segment can be 4KB, and thus the correct negative offset is 3KB minus 4KB which equals -1KB. We simply add the negative offset (-1KB) to the base (28KB) to arrive at the correct physical address: 27KB. The bounds check can be calculated by ensuring the absolute value of the negative offset is less than or equal to the segment’s current size (in this case, 2KB).  

