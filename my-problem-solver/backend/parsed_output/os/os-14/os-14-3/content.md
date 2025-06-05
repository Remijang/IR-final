# 14.3 The free() Call  

As it turns out, allocating memory is the easy part of the equation; knowing when, how, and even if to free memory is the hard part. To free heap memory that is no longer in use, programmers simply call free():  

int $\begin{array} { r l } { \mathbf { \nabla } \times \mathbf { x } } & { { } = } \end{array}$ malloc(10 $\star$ sizeof(int));   
free(x);  

The routine takes one argument, a pointer returned by malloc(). Thus, you might notice, the size of the allocated region is not passed in by the user, and must be tracked by the memory-allocation library itself.  

