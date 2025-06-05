# 44.8 Garbage Collection  

The first cost of any log-structured approach such as this one is that garbage is created, and therefore garbage collection (i.e., dead-block reclamation) must be performed. Let’s use our continued example to make sense of this. Recall that logical blocks 100, 101, 2000, and 2001 have been written to the device.  

Now, let’s assume that blocks 100 and 101 are written to again, with contents $\mathsf { c l }$ and $_ { \mathtt { C 2 } }$ . The writes are written to the next free pages (in this case, physical pages 4 and 5), and the mapping table is updated accordingly. Note that the device must have first erased block 1 to make such programming possible:  

<html><body><table><tr><td>Table:</td><td colspan="4">100 >4</td><td colspan="2">101 >5</td><td colspan="2">2000->2</td><td colspan="4">2001-3</td><td>Memory</td></tr><tr><td>Block:</td><td colspan="4">0 2</td><td></td><td colspan="2">1</td><td></td><td colspan="4"></td><td rowspan="3">Flash Chip</td></tr><tr><td>Page:</td><td>00 01</td><td></td><td>02</td><td>03</td><td></td><td></td><td>04 05 06 07</td><td></td><td>08091011</td><td></td><td></td></tr><tr><td>Content:</td><td>a1</td><td>a2</td><td>b1</td><td>b2</td><td>c1</td><td>c2</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>State:</td><td></td><td>v</td><td>v</td><td>v</td><td>v</td><td>v</td><td>E</td><td>E</td><td>i</td><td>i</td><td>i</td></tr></table></body></html>  

OPERATINGSYSTEMS[VERSION 1.10]  

The problem we have now should be obvious: physical pages 0 and 1, although marked VALID, have garbage in them, i.e., the old versions of blocks 100 and 101. Because of the log-structured nature of the device, overwrites create garbage blocks, which the device must reclaim to provide free space for new writes to take place.  

The process of finding garbage blocks (also called dead blocks) and reclaiming them for future use is called garbage collection, and it is an important component of any modern SSD. The basic process is simple: find a block that contains one or more garbage pages, read in the live (non-garbage) pages from that block, write out those live pages to the log, and (finally) reclaim the entire block for use in writing.  

Let’s now illustrate with an example. The device decides it wants to reclaim any dead pages within block 0 above. Block 0 has two dead blocks (pages 0 and 1) and two live blocks (pages 2 and 3, which contain blocks 2000 and 2001, respectively). To do so, the device will:  

• Read live data (pages 2 and 3) from block 0 • Write live data to end of the log • Erase block 0 (freeing it for later usage)  

For the garbage collector to function, there must be enough information within each block to enable the SSD to determine whether each page is live or dead. One natural way to achieve this end is to store, at some location within each block, information about which logical blocks are stored within each page. The device can then use the mapping table to determine whether each page within the block holds live data or not.  

From our example above (before the garbage collection has taken place), block 0 held logical blocks 100, 101, 2000, 2001. By checking the mapping table (which, before garbage collection, contained $1 0 0 - > 4$ , $1 0 1 - > 5$ , $2 0 0 0 \mathrm { - } { > } 2$ , $2 0 0 1 \mathrm { - } > 3 )$ , the device can readily determine whether each of the pages within the SSD block holds live information. For example, pages 2 and 3 are clearly still pointed to by the map; pages 0 and 1 are not and therefore are candidates for garbage collection.  

When this garbage collection process is complete in our example, the state of the device is:  

<html><body><table><tr><td>Table:</td><td>100</td><td>>4</td><td></td><td>101</td><td>+5</td><td></td><td>2000-6</td><td></td><td></td><td>2001->7</td><td></td><td></td></tr><tr><td>Block:</td><td colspan="4">0</td><td colspan="4">1</td><td colspan="4">2</td><td rowspan="3">Flash Chip</td></tr><tr><td>Page:</td><td>00 01 02 03</td><td></td><td></td><td></td><td></td><td></td><td>04 05 06 07</td><td></td><td></td><td>08 09 10 11</td><td></td><td></td></tr><tr><td>Content:</td><td></td><td></td><td></td><td></td><td>c1</td><td>c2</td><td>b1</td><td>b2</td><td></td><td></td><td></td><td></td></tr><tr><td>State:</td><td>E</td><td>E</td><td>E</td><td>E</td><td>v</td><td>v</td><td></td><td>v</td><td>i</td><td>i</td><td></td><td>i i</td><td></td></tr></table></body></html>  

As you can see, garbage collection can be expensive, requiring reading and rewriting of live data. The ideal candidate for reclamation is a block that consists of only dead pages; in this case, the block can immediately be erased and used for new data, without expensive data migration.  

# ASIDE: A NEW STORAGE API KNOWN AS TRIM  

When we think of hard drives, we usually just think of the most basic interface to read and write them: read and write (there is also usually some kind of cache flush command, ensuring that writes have actually been persisted, but sometimes we omit that for simplicity). With log-structured SSDs, and indeed, any device that keeps a flexible and changing mapping of logical-to-physical blocks, a new interface is useful, known as the trim operation.  

The trim operation takes an address (and possibly a length) and simply informs the device that the block(s) specified by the address (and length) have been deleted; the device thus no longer has to track any information about the given address range. For a standard hard drive, trim isn’t particularly useful, because the drive has a static mapping of block addresses to specific platter, track, and sector(s). For a log-structured SSD, however, it is highly useful to know that a block is no longer needed, as the SSD can then remove this information from the FTL and later reclaim the physical space during garbage collection.  

Although we sometimes think of interface and implementation as separate entities, in this case, we see that the implementation shapes the interface. With complex mappings, knowledge of which blocks are no longer needed makes for a more effective implementation.  

To reduce GC costs, some SSDs overprovision the device $\left[ { \mathrm { A } } { + } 0 8 \right]$ ; by adding extra flash capacity, cleaning can be delayed and pushed to the background, perhaps done at a time when the device is less busy. Adding more capacity also increases internal bandwidth, which can be used for cleaning and thus not harm perceived bandwidth to the client. Many modern drives overprovision in this manner, one key to achieving excellent overall performance.  

