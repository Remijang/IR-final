# 39.16 Permission Bits And Access Control Lists  

The abstraction of a process provided two central virtualizations: of the CPU and of memory. Each of these gave the illusion to a process that it had its own private CPU and its own private memory; in reality, the OS underneath used various techniques to share limited physical resources among competing entities in a safe and secure manner.  

The file system also presents a virtual view of a disk, transforming it from a bunch of raw blocks into much more user-friendly files and directories, as described within this chapter. However, the abstraction is notably different from that of the CPU and memory, in that files are commonly shared among different users and processes and are not (always) private. Thus, a more comprehensive set of mechanisms for enabling various degrees of sharing are usually present within file systems.  

The first form of such mechanisms is the classic UNIX permission bits. To see permissions for a file foo.txt, just type:  

prompt $>$ ls -l foo.txt -rw-r--r-- 1 remzi wheel 0 Aug 24 16:29 foo.txt  

We’ll just pay attention to the first part of this output, namely the $- \mathtt { r w - r -- r } \mathtt { w \mathrm { \mathtt { - - } } r } \mathtt { w \mathrm { - } }$ . The first character here just shows the type of the file: - for a regular file (which foo.txt is), d for a directory, l for a symbolic link, and so forth; this is (mostly) not related to permissions, so we’ll ignore it for now.  

We are interested in the permission bits, which are represented by the next nine characters $\big ( \mathtt { r w } - \mathtt { r } ^ { - } - \mathtt { r } \mathtt { \mathrm { - - } } \mathtt { - } \mathtt { - } \mathtt { \Gamma } \mathtt { \Lambda } \big )$ . These bits determine, for each regular file, directory, and other entities, exactly who can access it and how.  

The permissions consist of three groupings: what the owner of the file can do to it, what someone in a group can do to the file, and finally, what anyone (sometimes referred to as other) can do. The abilities the owner, group member, or others can have include the ability to read the file, write it, or execute it.  

In the example above, the first three characters of the output of $\mathsf { I s }$ show that the file is both readable and writable by the owner $( \underline { { { \Upsilon } } } \mathtt { w } - ) _ { \mathrm { . } }$ , and only readable by members of the group wheel and also by anyone else in the system $\mathrel { \mathop { \tt ~ \underbrace ~ { ~ \tt ~ { ~ r ~ \mathrm { ~  ~  ~  ~ \textmu ~ } } } } }$ followed by $\scriptstyle { \underline { { \boldsymbol { { r } } } } } - -$ ).  

The owner of the file can readily change these permissions, for example by using the chmod command (to change the file mode). To remove the ability for anyone except the owner to access the file, you could type:  

prompt> chmod 600 foo.txt  

OPERATINGSYSTEMS[VERSION 1.10]  

# ASIDE: SUPERUSER FOR FILE SYSTEMS  

Which user is allowed to do privileged operations to help administer the file system? For example, if an inactive user’s files need to be deleted to save space, who has the rights to do so?  

On local file systems, the common default is for there to be some kind of superuser (i.e., root) who can access all files regardless of privileges. In a distributed file system such as AFS (which has access control lists), a group called system:administrators contains users that are trusted to do so. In both cases, these trusted users represent an inherent security risk; if an attacker is able to somehow impersonate such a user, the attacker can access all the information in the system, thus violating expected privacy and protection guarantees.  

This command enables the readable bit (4) and writable bit (2) for the owner (OR’ing them together yields the 6 above), but set the group and other permission bits to 0 and 0, respectively, thus setting the permissions to ${ \texttt { Y w -- -- } }$  

The execute bit is particularly interesting. For regular files, its presence determines whether a program can be run or not. For example, if we have a simple shell script called hello.csh, we may wish to run it by typing:  

prompt> ./hello.csh hello, from shell world.  

However, if we don’t set the execute bit properly for this file, the following happens:  

prompt> chmod 600 hello.csh prompt> ./hello.csh ./hello.csh: Permission denied.  

For directories, the execute bit behaves a bit differently. Specifically, it enables a user (or group, or everyone) to do things like change directories (i.e., cd) into the given directory, and, in combination with the writable bit, create files therein. The best way to learn more about this: play around with it yourself! Don’t worry, you (probably) won’t mess anything up too badly.  

Beyond permissions bits, some file systems, such as the distributed file system known as AFS (discussed in a later chapter), include more sophisticated controls. AFS, for example, does this in the form of an access control list (ACL) per directory. Access control lists are a more general and powerful way to represent exactly who can access a given resource. In a file system, this enables a user to create a very specific list of who can and cannot read a set of files, in contrast to the somewhat limited owner/group/everyone model of permissions bits described above.  

For example, here are the access controls for a private directory in one author’s AFS account, as shown by the fs listacl command:  

prompt> fs listacl private   
Access list for private is   
Normal rights: system:administrators rlidwka remzi rlidwka  

The listing shows that both the system administrators and the use remzi can lookup, insert, delete, and administer files in this directory, a well as read, write, and lock those files.  

To allow someone (in this case, the other author) to access this directory, user remzi can just type the following command.  

prompt> fs setacl private/ andrea rl  

There goes remzi’s privacy! But now you have learned an even more important lesson: there can be no secrets in a good marriage, even within the file system3.  

