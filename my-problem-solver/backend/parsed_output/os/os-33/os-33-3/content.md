# 33.3 Using select()  

To make this more concrete, let’s examine how to use select() to see which network descriptors have incoming messages upon them. Figure 33.1 shows a simple example.  

This code is actually fairly simple to understand. After some initialization, the server enters an infinite loop. Inside the loop, it uses the FD ZERO() macro to first clear the set of file descriptors, and then uses FD SET() to include all of the file descriptors from minFD to maxFD in  

1 #include <stdio.h>   
2 #include <stdlib.h>   
3 #include <sys/time.h>   
4 #include <sys/types.h>   
5 #include <unistd.h>   
6   
7 int main(void) {   
8 // open and set up a bunch of sockets (not shown)   
9 // main loop   
10 while (1) {   
11 // initialize the fd_set to all zero   
12 fd_set readFDs;   
13 FD_ZERO(&readFDs);   
14   
15 // now set the bits for the descriptors   
16 // this server is interested in   
17 // (for simplicity, all of them from min to max)   
18 int fd;   
19 for (fd $\mathbf { \Sigma } = \mathbf { \Sigma }$ minFD; fd $\prec$ maxFD; $\operatorname { f d } + +$ )   
20 FD_SET(fd, &readFDs);   
21   
22 // do the select   
23 int rc $\mathbf { \Sigma } = \mathbf { \Sigma }$ select(maxFD $+ 1$ , &readFDs, NULL, NULL, NULL);   
24   
25 // check which actually have data using FD_ISSET()   
26 int fd;   
27 for (fd $\mathbf { \Sigma } = \mathbf { \Sigma }$ minFD; fd $\prec$ maxFD; $\operatorname { f d } + +$ )   
28 if (FD_ISSET(fd, &readFDs))   
29 processFD(fd);   
30 }   
31 }  

the set. This set of descriptors might represent, for example, all of the network sockets to which the server is paying attention. Finally, the server calls select() to see which of the connections have data available upon them. By then using FD ISSET() in a loop, the event server can see which of the descriptors have data ready and process the incoming data.  

Of course, a real server would be more complicated than this, and require logic to use when sending messages, issuing disk I/O, and many other details. For further information, see Stevens and Rago [SR05] for API information, or Pai et. al or Welsh et al. for a good overview of the general flow of event-based servers [PDZ99, WCB01].  

OPERATINGSYSTEMS[VERSION 1.10]  

TIP: DON’T BLOCK IN EVENT-BASED SERVERS Event-based servers enable fine-grained control over scheduling of tasks. However, to maintain such control, no call that blocks the execution of the caller can ever be made; failing to obey this design tip will result in a blocked event-based server, frustrated clients, and serious questions as to whether you ever read this part of the book.  

