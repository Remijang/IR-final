# 14.6 Other Calls  

There are a few other calls that the memory-allocation library supports. For example, calloc() allocates memory and also zeroes it before returning; this prevents some errors where you assume that memory is zeroed and forget to initialize it yourself (see the paragraph on “uninitialized reads” above). The routine realloc() can also be useful, when you’ve allocated space for something (say, an array), and then need to add something to it: realloc() makes a new larger region of memory, copies the old region into it, and returns the pointer to the new region.  

OPERATINGSYSTEMS[VERSION 1.10]  

