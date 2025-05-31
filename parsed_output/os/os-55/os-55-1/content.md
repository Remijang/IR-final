# 55.1 Introduction  

So we know what our security goals are, we have at least a general sense of the security policies we’d like to enforce, and we have some evidence about who is requesting various system services that might (or might not) violate our policies. Now we need to take that information and turn it into something actionable, something that a piece of software can perform for us.  

There are two important steps here:  

1. Figure out if the request fits within our security policy.   
2. If it does, perform the operation. If not, make sure it isn’t done.  

The first step is generally referred to as access control. We will determine which system resources or services can be accessed by which parties in which ways under which circumstances. Basically, it boils down to another of those binary decisions that fit so well into our computing paradigms: yes or no. But how to make that decision? To make the problem more concrete, consider this case. User X wishes to read and write file /var/foo. Under the covers, this case probably implies that a process being run under the identity of User X issued a system call such as:  

open(”/var/foo”, O RDWR)  

Note here that we’re not talking about the Linux open() call, which is a specific implementation that handles access control a specific way. We’re talking about the general idea of how you might be able to control access to a file open system call. Hence the different font, to remind you.  

How should the system handle this request from the process, making sure that the file is not opened if the security policy to be enforced forbids it, but equally making sure that the file is opened if the policy allows it? We know that the system call will trap to the operating system, giving it the opportunity to do something to make this decision. Mechanically speaking, what should that “something” be?  

THE CRUX OF THE PROBLEM: HOW TO DETERMINE IF AN ACCESS REQUEST SHOULD BE GRANTED?  

How can the operating system decide if a particular request made by a particular process belonging to a particular user at some given moment should or should not be granted? What information will be used to make this decision? How can we set this information to encode the security policies we want to enforce for our system?  

