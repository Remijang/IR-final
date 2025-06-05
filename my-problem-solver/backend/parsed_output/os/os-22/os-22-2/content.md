# 22.2 The Optimal Replacement Policy  

To better understand how a particular replacement policy works, it would be nice to compare it to the best possible replacement policy. As it turns out, such an optimal policy was developed by Belady many years ago [B66] (he originally called it MIN). The optimal replacement policy leads to the fewest number of misses overall. Belady showed that a simple (but, unfortunately, difficult to implement!) approach that replaces the page that will be accessed furthest in the future is the optimal policy, resulting in the fewest-possible cache misses.  

OPERATINGSYSTEMS[VERSION 1.10]  

TIP: COMPARING AGAINST OPTIMAL IS USEFUL Although optimal is not very practical as a real policy, it is incredibly useful as a comparison point in simulation or other studies. Saying that your fancy new algorithm has a $8 0 \%$ hit rate isn’t meaningful in isolation; saying that optimal achieves an $8 2 \%$ hit rate (and thus your new approach is quite close to optimal) makes the result more meaningful and gives it context. Thus, in any study you perform, knowing what the optimal is lets you perform a better comparison, showing how much improvement is still possible, and also when you can stop making your policy better, because it is close enough to the ideal [AD03].  

Hopefully, the intuition behind the optimal policy makes sense. Think about it like this: if you have to throw out some page, why not throw out the one that is needed the furthest from now? By doing so, you are essentially saying that all the other pages in the cache are more important than the one furthest out. The reason this is true is simple: you will refer to the other pages before you refer to the one furthest out.  

Let’s trace through a simple example to understand the decisions the optimal policy makes. Assume a program accesses the following stream of virtual pages: $0 , 1 , 2 , 0 , 1 , 3 , 0 , 3 , 1 , \breve { 2 } , 1$ . Figure 22.1 shows the behavior of optimal, assuming a cache that fits three pages.  

In the figure, you can see the following actions. Not surprisingly, the first three accesses are misses, as the cache begins in an empty state; such a miss is sometimes referred to as a cold-start miss (or compulsory miss). Then we refer again to pages 0 and 1, which both hit in the cache. Finally, we reach another miss (to page 3), but this time the cache is full; a replacement must take place! Which begs the question: which page should we replace? With the optimal policy, we examine the future for each page currently in the cache $( { \bar { 0 } } , 1 ,$ and 2), and see that 0 is accessed almost immediately, 1 is accessed a little later, and 2 is accessed furthest in the future. Thus the optimal policy has an easy choice: evict page 2, resulting in  

![](images/71132f2f22ffbdbbe242602ffcb24dfc89a16a03d5adc4d42562fb84f86d887e.jpg)  
Figure 22.1: Tracing The Optimal Policy  

THREE EASY PIECES  

# ASIDE: TYPES OF CACHE MISSES  

In the computer architecture world, architects sometimes find it useful to characterize misses by type, into one of three categories: compulsory, capacity, and conflict misses, sometimes called the Three C’s [H87]. A compulsory miss (or cold-start miss [EF78]) occurs because the cache is empty to begin with and this is the first reference to the item; in contrast, a capacity miss occurs because the cache ran out of space and had to evict an item to bring a new item into the cache. The third type of miss (a conflict miss) arises in hardware because of limits on where an item can be placed in a hardware cache, due to something known as setassociativity; it does not arise in the OS page cache because such caches are always fully-associative, i.e., there are no restrictions on where in memory a page can be placed. See H&P for details [HP06].  

pages 0, 1, and 3 in the cache. The next three references are hits, but then we get to page 2, which we evicted long ago, and suffer another miss. Here the optimal policy again examines the future for each page in the cache $( 0 , 1 , \cdots$ and 3), and sees that as long as it doesn’t evict page 1 (which is about to be accessed), we’ll be OK. The example shows page 3 getting evicted, although 0 would have been a fine choice too. Finally, we hit on page 1 and the trace completes.  

We can also calculate the hit rate for the cache: with 6 hits and 5 misses, the hit rate is Hits+Misses which is $\frac { 6 } { 6 { + } 5 }$ or $5 4 . 5 \%$ . You can also compute the hit rate modulo compulsory misses (i.e., ignore the first miss to a given page), resulting in a $8 5 . 7 \%$ hit rate.  

Unfortunately, as we saw before in the development of scheduling policies, the future is not generally known; you can’t build the optimal policy for a general-purpose operating system1. Thus, in developing a real, deployable policy, we will focus on approaches that find some other way to decide which page to evict. The optimal policy will thus serve only as a comparison point, to know how close we are to “perfect”.  

