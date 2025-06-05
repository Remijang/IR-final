# 44.10 Wear Leveling  

Finally, a related background activity that modern FTLs must implement is wear leveling, as introduced above. The basic idea is simple: because multiple erase/program cycles will wear out a flash block, the FTL should try its best to spread that work across all the blocks of the device evenly. In this manner, all blocks will wear out at roughly the same time, instead of a few “popular” blocks quickly becoming unusable.  

The basic log-structuring approach does a good initial job of spreading out write load, and garbage collection helps as well. However, sometimes a block will be filled with long-lived data that does not get over-written; in this case, garbage collection will never reclaim the block, and thus it does not receive its fair share of the write load.  

To remedy this problem, the FTL must periodically read all the live data out of such blocks and re-write it elsewhere, thus making the block available for writing again. This process of wear leveling increases the write amplification of the SSD, and thus decreases performance as extra $\mathrm { I } / \mathrm { O }$ is required to ensure that all blocks wear at roughly the same rate. Many different algorithms exist in the literature $[ \mathrm { A } { + } 0 \bar { 8 } _ { , }$ , $\dot { \mathrm { M } } { + } 1 \dot { 4 }$ ]; read more if you are interested.  

