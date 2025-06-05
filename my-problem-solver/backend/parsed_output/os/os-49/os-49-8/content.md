# 49.8 Improving Performance: Client-side Caching  

Distributed file systems are good for a number of reasons, but sending all read and write requests across the network can lead to a big performance problem: the network generally isn’t that fast, especially as compared to local memory or disk. Thus, another problem: how can we improve the performance of a distributed file system?  

The answer, as you might guess from reading the big bold words in the sub-heading above, is client-side caching. The NFS client-side file system caches file data (and metadata) that it has read from the server in client memory. Thus, while the first access is expensive (i.e., it requires network communication), subsequent accesses are serviced quite quickly out of client memory.  

The cache also serves as a temporary buffer for writes. When a client application first writes to a file, the client buffers the data in client memory (in the same cache as the data it read from the file server) before writing the data out to the server. Such write buffering is useful because it decouples application write() latency from actual write performance, i.e., the application’s call to write() succeeds immediately (and just puts the data in the client-side file system’s cache); only later does the data get written out to the file server.  

Thus, NFS clients cache data and performance is usually great and we are done, right? Unfortunately, not quite. Adding caching into any sort of system with multiple client caches introduces a big and interesting challenge which we will refer to as the cache consistency problem.  

