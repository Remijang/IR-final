# 22.6 Workload Examples  

Let’s look at a few more examples in order to better understand how some of these policies behave. Here, we’ll examine more complex workloads instead of small traces. However, even these workloads are greatly simplified; a better study would include application traces.  

Our first workload has no locality, which means that each reference is to a random page within the set of accessed pages. In this simple example, the workload accesses 100 unique pages over time, choosing the next page to refer to at random; overall, 10,000 pages are accessed. In the experiment, we vary the cache size from very small (1 page) to enough to hold all the unique pages (100 pages), in order to see how each policy behaves over the range of cache sizes.  

![](images/77a3dc0e5727a3265b22a3216273b439d7d84fd54051a3319083628ed1da4f35.jpg)  
Figure 22.6: The No-Locality Workload  

Figure 22.6 plots the results of the experiment for optimal, LRU, Random, and FIFO. The y-axis of the figure shows the hit rate that each policy achieves; the $\mathbf { \boldsymbol { x } }$ -axis varies the cache size as described above.  

We can draw a number of conclusions from the graph. First, when there is no locality in the workload, it doesn’t matter much which realistic policy you are using; LRU, FIFO, and Random all perform the same, with the hit rate exactly determined by the size of the cache. Second, when the cache is large enough to fit the entire workload, it also doesn’t matter which policy you use; all policies (even Random) converge to a $1 0 0 \%$ hit rate when all the referenced blocks fit in cache. Finally, you can see that optimal performs noticeably better than the realistic policies; peeking into the future, if it were possible, does a much better job of replacement.  

The next workload we examine is called the $^ { \prime \prime } \mathrm { 8 0 - } 2 0 ^ { \prime \prime }$ workload, which exhibits locality: $8 0 \%$ of the references are made to $2 0 \%$ of the pages (the “hot” pages); the remaining $2 0 \%$ of the references are made to the remaining $\bar { 8 } 0 \%$ of the pages (the “cold” pages). In our workload, there are a total 100 unique pages again; thus, “hot” pages are referred to most of the time, and “cold” pages the remainder. Figure 22.7 (page 10) shows how the policies perform with this workload.  

As you can see from the figure, while both random and FIFO do reasonably well, LRU does better, as it is more likely to hold onto the hot pages; as those pages have been referred to frequently in the past, they are likely to be referred to again in the near future. Optimal once again does better, showing that LRU’s historical information is not perfect.  

![](images/359095c72ddcff85ffedb8b061cf7b4b638f35f97c30b4d9d8dbc52ccbcbd766.jpg)  
Figure 22.7: The 80-20 Workload  

You might now be wondering: is LRU’s improvement over Random and FIFO really that big of a deal? The answer, as usual, is “it depends.” If each miss is very costly (not uncommon), then even a small increase in hit rate (reduction in miss rate) can make a huge difference on performance. If misses are not so costly, then of course the benefits possible with LRU are not nearly as important.  

Let’s look at one final workload. We call this one the “looping sequential” workload, as in it, we refer to 50 pages in sequence, starting at 0, then 1, ..., up to page 49, and then we loop, repeating those accesses, for a total of 10,000 accesses to 50 unique pages. The last graph in Figure 22.8 shows the behavior of the policies under this workload.  

This workload, common in many applications (including important commercial applications such as databases [CD85]), represents a worstcase for both LRU and FIFO. These algorithms, under a looping-sequential workload, kick out older pages; unfortunately, due to the looping nature of the workload, these older pages are going to be accessed sooner than the pages that the policies prefer to keep in cache. Indeed, even with a cache of size 49, a looping-sequential workload of 50 pages results in a $0 \%$ hit rate. Interestingly, Random fares notably better, not quite approaching optimal, but at least achieving a non-zero hit rate. Turns out that random has some nice properties; one such property is not having weird corner-case behaviors.  

OPERATINGSYSTEMS[VERSION 1.10]  

![](images/5e11ba51d4570c3e3095a42d88a8aae16f3403430aa8bdf45a2f3ee2d123633b.jpg)  
Figure 22.8: The Looping Workload  

