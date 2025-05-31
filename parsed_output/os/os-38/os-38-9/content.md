# 38.9 Other Interesting RAID Issues  

There are a number of other interesting ideas that one could (and perhaps should) discuss when thinking about RAID. Here are some things we might eventually write about.  

For example, there are many other RAID designs, including Levels 2 and 3 from the original taxonomy, and Level 6 to tolerate multiple disk faults $\scriptstyle { [ C + 0 4 ] }$ . There is also what the RAID does when a disk fails; sometimes it has a hot spare sitting around to fill in for the failed disk. What happens to performance under failure, and performance during reconstruction of the failed disk? There are also more realistic fault models, to take into account latent sector errors or block corruption $\scriptstyle { \left[ { \mathrm { B } } + 0 8 \right] } ,$ , and lots of techniques to handle such faults (see the data integrity chapter for details). Finally, you can even build RAID as a software layer: such software RAID systems are cheaper but have other problems, including the consistent-update problem [DAA05].  

