# 39.12 Reading Directories  

Now that we’ve created a directory, we might wish to read one too. Indeed, that is exactly what the program ls does. Let’s write our own little tool like ls and see how it is done.  

Instead of just opening a directory as if it were a file, we instead use a new set of calls. Below is an example program that prints the contents of a directory. The program uses three calls, opendir(), readdir(), and closedir(), to get the job done, and you can see how simple the interface is; we just use a simple loop to read one directory entry at a time, and print out the name and inode number of each file in the directory.  

int main(int argc, char \*argv[]) { DIR $\star \mathrm { d } \mathrm { p } \ =$ opendir("."); assert(dp $\vdots = \mathrm { ~ N ~ }$ ULL); struct dirent $\star \mathrm { d }$ ; while (( ${ \mathrm { ~ \ : ~ d ~ } } =$ readdir(dp)) ! $\mathbf { \Sigma } = \mathbf { \Sigma }$ NULL) { printf("%lu %s\n", (unsigned long) d->d_ino, d->d_name); } closedir(dp); return 0;   
}  

The declaration below shows the information available within each directory entry in the struct dirent data structure:  

struct dirent { char d_name[256]; // filename ino_t d_ino; // inode number off_t d_off; // offset to the next dirent unsigned short d_reclen; // length of this record unsigned char d_type; // type of file   
};  

Because directories are light on information (basically, just mapping the name to the inode number, along with a few other details), a program may want to call stat() on each file to get more information on each, such as its length or other detailed information. Indeed, this is exactly what ls does when you pass it the $- 1$ flag; try strace on ls with and without that flag to see for yourself.  

