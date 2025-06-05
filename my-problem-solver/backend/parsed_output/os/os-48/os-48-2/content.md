# 48.2 Unreliable Communication Layers  

One simple way is this: we don’t deal with it. Because some applications know how to deal with packet loss, it is sometimes useful to let them communicate with a basic unreliable messaging layer, an example of the end-to-end argument one often hears about (see the Aside at end of chapter). One excellent example of such an unreliable layer is found  

int UDP_Open(int port) { int sd; if ((sd $\mathbf { \Sigma } = \mathbf { \Sigma }$ socket(AF_INET, SOCK_DGRAM, 0)) == -1) return $^ { - 1 }$ ; struct sockaddr_in myaddr; bzero(&myaddr, sizeof(myaddr)); myaddr.sin_family $\mathbf { \Sigma } = \mathbf { \Sigma }$ AF_INET; myaddr.sin_port $\mathbf { \Sigma } = \mathbf { \Sigma }$ htons(port); myaddr.sin_addr.s_addr $\mathbf { \Sigma } = \mathbf { \Sigma }$ INADDR_ANY; if (bind(sd, (struct sockaddr $\star$ ) &myaddr, sizeof(myaddr)) $\scriptstyle \mathbf { \alpha = } \ - 1$ ) { close(sd); return -1; } return sd;   
}   
int UDP_FillSockAddr(struct sockaddr_in \*addr, char \*hostname, int port) { bzero(addr, sizeof(struct sockaddr_in)); addr->sin_family $\mathbf { \Sigma } = \mathbf { \Sigma }$ AF_INET; // host byte order addr->sin_port $\mathbf { \Sigma } = \mathbf { \Sigma }$ htons(port); // network byte order struct in_addr $\star$ in_addr; struct hostent \*host_entry; if ((host_entry $\mathbf { \tau } = \mathbf { \tau }$ gethostbyname(hostname)) $\scriptstyle = =$ NULL) return -1; in_addr $\mathbf { \Sigma } = \mathbf { \Sigma }$ (struct in_addr $\star$ ) host_entry->h_addr; addr->sin_addr $\mathbf { \Sigma } = \mathbf { \Sigma }$ \*in_addr; return 0;   
}   
int UDP_Write(int sd, struct sockaddr_in \*addr, char \*buffer, int n) { int addr_len $\mathbf { \Sigma } = \mathbf { \Sigma }$ sizeof(struct sockaddr_in); return sendto(sd, buffer, n, 0, (struct sockaddr $\star$ ) addr, addr_len);   
}   
int UDP_Read(int sd, struct sockaddr_in \*addr, char \*buffer, int n) { int len $\mathbf { \Sigma } = \mathbf { \Sigma }$ sizeof(struct sockaddr_in); return recvfrom(sd, buffer, n, 0, (struct sockaddr \*) addr, (socklen_t \*) &len);   
} Figure 48.2: A Simple UDP Library (udp.c)  

OPERATINGSYSTEMS[VERSION 1.10]  

# TIP: USE CHECKSUMS FOR INTEGRITY  

Checksums are a commonly-used method to detect corruption quickly and effectively in modern systems. A simple checksum is addition: just sum up the bytes of a chunk of data; of course, many other more sophisticated checksums have been created, including basic cyclic redundancy codes (CRCs), the Fletcher checksum, and many others [MK09].  

In networking, checksums are used as follows. Before sending a message from one machine to another, compute a checksum over the bytes of the message. Then send both the message and the checksum to the destination. At the destination, the receiver computes a checksum over the incoming message as well; if this computed checksum matches the sent checksum, the receiver can feel some assurance that the data likely did not get corrupted during transmission.  

Checksums can be evaluated along a number of different axes. Effectiveness is one primary consideration: does a change in the data lead to a change in the checksum? The stronger the checksum, the harder it is for changes in the data to go unnoticed. Performance is the other important criterion: how costly is the checksum to compute? Unfortunately, effectiveness and performance are often at odds, meaning that checksums of high quality are often expensive to compute. Life, again, isn’t perfect.  

in the UDP/IP networking stack available today on virtually all modern systems. To use UDP, a process uses the sockets API in order to create a communication endpoint; processes on other machines (or on the same machine) send UDP datagrams to the original process (a datagram is a fixed-sized message up to some max size).  

Figures 48.1 and 48.2 show a simple client and server built on top of UDP/IP. The client can send a message to the server, which then responds with a reply. With this small amount of code, you have all you need to begin building distributed systems!  

UDP is a great example of an unreliable communication layer. If you use it, you will encounter situations where packets get lost (dropped) and thus do not reach their destination; the sender is never thus informed of the loss. However, that does not mean that UDP does not guard against any failures at all. For example, UDP includes a checksum to detect some forms of packet corruption.  

However, because many applications simply want to send data to a destination and not worry about packet loss, we need more. Specifically, we need reliable communication on top of an unreliable network.  

