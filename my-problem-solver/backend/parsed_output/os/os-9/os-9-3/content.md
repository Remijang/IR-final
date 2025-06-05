# 9.3 Implementation  

Probably the most amazing thing about lottery scheduling is the simplicity of its implementation. All you need is a good random number generator to pick the winning ticket, a data structure to track the processes of the system (e.g., a list), and the total number of tickets.  

![](images/e7c0aba3aab5c6a14ad741ea8f74f9ce50d3f2d9e193748a53c89ac4f2649679.jpg)  
Figure 9.1: Lottery Scheduling Decision Code  

Let’s assume we keep the processes in a list. Here is an example comprised of three processes, A, B, and C, each with some number of tickets.  

To make a scheduling decision, we first have to pick a random number (the winner) from the total number of tickets $( 4 0 0 ) ^ { 2 }$ Let’s say we pick the number 300. Then, we simply traverse the list, with a simple counter used to help us find the winner (Figure 9.1).  

The code walks the process list, adding each ticket value to counter until the value exceeds winner. Once that is the case, the current list element is the winner. With our example of the winning ticket being 300, the following takes place. First, counter is incremented to 100 to account for A’s tickets; because 100 is less than 300, the loop continues. Then counter would be updated to 150 (B’s tickets), still less than 300 and thus again we continue. Finally, counter is updated to 400 (clearly greater than 300), and thus we break out of the loop with current pointing at C (the winner).  

![](images/ee95baf156d992a196a3b3ce4dbf4b47bb0ebb9c18cd2572c4ae5b5e1c916273.jpg)  
Figure 9.2: Lottery Fairness Study  

To make this process most efficient, it might generally be best to organize the list in sorted order, from the highest number of tickets to the lowest. The ordering does not affect the correctness of the algorithm; however, it does ensure in general that the fewest number of list iterations are taken, especially if there are a few processes that possess most of the tickets.  

