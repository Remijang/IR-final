# 43.2 Writing Sequentially And Effectively  

Unfortunately, writing to disk sequentially is not (alone) enough to guarantee efficient writes. For example, imagine if we wrote a single block to address $A ,$ at time $T$ . We then wait a little while, and write to the disk at address $A + 1$ (the next block address in sequential order), but at time $T + \delta$ . In-between the first and second writes, unfortunately, the disk has rotated; when you issue the second write, it will thus wait for most of a rotation before being committed (specifically, if the rotation takes time $T _ { r o t a t i o n . }$ , the disk will wait $T _ { r o t a t i o n } \bar { - } \delta$ before it can commit the second write to the disk surface). And thus you can hopefully see that simply writing to disk in sequential order is not enough to achieve peak performance; rather, you must issue a large number of contiguous writes (or one large write) to the drive in order to achieve good write performance.  

To achieve this end, LFS uses an ancient technique known as write buffering1. Before writing to the disk, LFS keeps track of updates in memory; when it has received a sufficient number of updates, it writes them to disk all at once, thus ensuring efficient use of the disk.  

The large chunk of updates LFS writes at one time is referred to by the name of a segment. Although this term is over-used in computer systems, here it just means a large-ish chunk which LFS uses to group writes. Thus, when writing to disk, LFS buffers updates in an in-memory segment, and then writes the segment all at once to the disk. As long as the segment is large enough, these writes will be efficient.  

Here is an example, in which LFS buffers two sets of updates into a small segment; actual segments are larger (a few MB). The first update is of four block writes to file $j$ ; the second is one block being added to file $k$ . LFS then commits the entire segment of seven blocks to disk at once. The resulting on-disk layout of these blocks is as follows:  

![](images/7cb3e9c139e17c0f539ed3b48f92338e66c59afd23fe678a5e8b83efb03c9c7c.jpg)  

