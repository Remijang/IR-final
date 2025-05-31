# 9.2 Ticket Mechanisms  

Lottery scheduling also provides a number of mechanisms to manipulate tickets in different and sometimes useful ways. One way is with the concept of ticket currency. Currency allows a user with a set of tickets to allocate tickets among their own jobs in whatever currency they would like; the system then automatically converts said currency into the correct global value.  

For example, assume users A and B have each been given 100 tickets. User A is running two jobs, A1 and A2, and gives them each 500 tickets (out of 1000 total) in A’s currency. User B is running only 1 job and gives it 10 tickets (out of 10 total). The system converts A1’s and A2’s allocation from 500 each in A’s currency to 50 each in the global currency; similarly, B1’s 10 tickets is converted to 100 tickets. The lottery is then held over the global ticket currency (200 total) to determine which job runs.  

User A $ 5 0 0$ ( $\mathbb { A } ^ { \prime } \mathbb { s }$ currency) to A1 $- >$ 50 (global currency) $- > 5 0 0$ ( $\mathbb { A } ^ { \prime } \mathbb { s }$ currency) to A2 $\mathrel { - } >$ 50 (global currency) User $3 \  \quad 1 0$ ( $\mathbf { \mathrm { B ^ { \prime } } } \mathbf { \varepsilon } _ { S }$ currency) to B1 $- > \ 1 0 0$ (global currency)  

Another useful mechanism is ticket transfer. With transfers, a process can temporarily hand off its tickets to another process. This ability is especially useful in a client/server setting, where a client process sends a message to a server asking it to do some work on the client’s behalf. To speed up the work, the client can pass the tickets to the server and thus try to maximize the performance of the server while the server is handling the client’s request. When finished, the server then transfers the tickets back to the client and all is as before.  

Finally, ticket inflation can sometimes be a useful technique. With inflation, a process can temporarily raise or lower the number of tickets it owns. Of course, in a competitive scenario with processes that do not trust one another, this makes little sense; one greedy process could give itself a vast number of tickets and take over the machine. Rather, inflation can be applied in an environment where a group of processes trust one another; in such a case, if any one process knows it needs more CPU time, it can boost its ticket value as a way to reflect that need to the system, all without communicating with any other processes.  

1 // counter: used to track if we’ve found the winner ye   
2 int counter $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
3   
4 // winner: call some random number generator to   
5 // get a value $> = ~ 0$ and $< =$ (totaltickets - 1)   
6 int winner $\mathbf { \Sigma } = \mathbf { \Sigma }$ getrandom(0, totaltickets);   
7   
8 // current: use this to walk through the list of jobs   
9 node_t \*current $\mathbf { \Sigma } = \mathbf { \Sigma }$ head;   
10 while (current) {   
11 counter $\mathbf { \tau } = \mathbf { \tau }$ counter $^ +$ current->tickets;   
12 if (counter $>$ winner)   
13 break; // found the winner   
14 current $\mathbf { \tau } = \mathbf { \tau }$ current->next;   
15 }   
16 // ’current’ is the winner: schedule it..  

