# 13.5 Summary  

We have seen the introduction of a major OS subsystem: virtual memory. The VM system is responsible for providing the illusion of a large, sparse, private address space to each running program; each virtual address space contains all of a program’s instructions and data, which can be referenced by the program via virtual addresses. The OS, with some serious hardware help, will take each of these virtual memory references and turn them into physical addresses, which can be presented to the physical memory in order to fetch or update the desired information. The OS will provide this service for many processes at once, making sure to protect programs from one another, as well as protect the OS. The entire approach requires a great deal of mechanism (i.e., lots of low-level machinery) as well as some critical policies to work; we’ll start from the bottom up, describing the critical mechanisms first. And thus we proceed!  

# ASIDE: EVERY ADDRESS YOU SEE IS VIRTUAL  

Ever write a C program that prints out a pointer? The value you see (some large number, often printed in hexadecimal), is a virtual address. Ever wonder where the code of your program is found? You can print that out too, and yes, if you can print it, it also is a virtual address. In fact, any address you can see as a programmer of a user-level program is a virtual address. It’s only the OS, through its tricky techniques of virtualizing memory, that knows where in the physical memory of the machine these instructions and data values lie. So never forget: if you print out an address in a program, it’s a virtual one, an illusion of how things are laid out in memory; only the OS (and the hardware) knows the real truth.  

Here’s a little program (va.c) that prints out the locations of the main() routine (where code lives), the value of a heap-allocated value returned from malloc(), and the location of an integer on the stack:  

1 #include <stdio.h>   
2 #include <stdlib.h>   
3 int main(int argc, char \*argv[]) {   
4 printf("location of code : %p\n", main);   
5 printf("location of heap : %p\n", malloc(100e6));   
6 int $\mathrm { ~  ~ x ~ } = \mathrm { ~  ~ 3 ~ }$ ;   
7 printf("location of stack: %p\n", &x);   
8 return x;   
9 }  

When run on a 64-bit Mac, we get the following output:  

location of code : 0x1095afe50   
location of heap : 0x1096008c0   
location of stack: 0x7fff691aea64  

From this, you can see that code comes first in the address space, then the heap, and the stack is all the way at the other end of this large virtual space. All of these addresses are virtual, and will be translated by the OS and hardware in order to fetch values from their true physical locations.  

