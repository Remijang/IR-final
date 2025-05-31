# 22.3 A Simple Policy: FIFO  

Many early systems avoided the complexity of trying to approach optimal and employed very simple replacement policies. For example, some systems used FIFO (first-in, first-out) replacement, where pages were simply placed in a queue when they enter the system; when a replacement occurs, the page on the tail of the queue (the “first-in” page) is evicted. FIFO has one great strength: it is quite simple to implement.  

Let’s examine how FIFO does on our example reference stream (Figure 22.2, page 5). We again begin our trace with three compulsory misses to pages 0, 1, and 2, and then hit on both 0 and 1. Next, page 3 is referenced, causing a miss; the replacement decision is easy with FIFO: pick the page that was the “first one” in (the cache state in the figure is kept in FIFO order, with the first-in page on the left), which is page 0. Unfortunately, our next access is to page 0, causing another miss and replacement (of page 1). We then hit on page 3, but miss on 1 and 2, and finally hit on 1.  

![](images/e9a1895d9dffd87f035c747172fa919c4cfc63dfc26d60d7dabb738fa1c55930.jpg)  
Figure 22.2: Tracing The FIFO Policy  

Comparing FIFO to optimal, FIFO does notably worse: a $3 6 . 4 \%$ hit rate (or $\mathbf { \widetilde { 5 7 . 1 \% } }$ excluding compulsory misses). FIFO simply can’t determine the importance of blocks: even though page 0 had been accessed a number of times, FIFO still kicks it out, simply because it was the first one brought into memory.  

ASIDE: BELADY’S ANOMALY  

Belady (of the optimal policy) and colleagues found an interesting reference stream that behaved a little unexpectedly [BNS69]. The memoryreference stream: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5. The replacement policy they were studying was FIFO. The interesting part: how the cache hit rate changed when moving from a cache size of 3 to 4 pages.  

In general, you would expect the cache hit rate to increase (get better) when the cache gets larger. But in this case, with FIFO, it gets worse! Calculate the hits and misses yourself and see. This odd behavior is generally referred to as Belady’s Anomaly (to the chagrin of his co-authors).  

Some other policies, such as LRU, don’t suffer from this problem. Can you guess why? As it turns out, LRU has what is known as a stack property $\mathrm { \bar { [ M + 7 0 ] } }$ . For algorithms with this property, a cache of size $N + 1$ naturally includes the contents of a cache of size $N$ . Thus, when increasing the cache size, hit rate will either stay the same or improve. FIFO and Random (among others) clearly do not obey the stack property, and thus are susceptible to anomalous behavior.  

![](images/9b0fbbc38953d29ca5bd19adcf16793a667c3b57e5f991403081147d01d8713d.jpg)  
Figure 22.3: Tracing The Random Policy  

