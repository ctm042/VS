#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
//What is possible?
//The atexit function takes a pointer to a function and adds it to a list of functions (initially empty) that will be called when the exit function is called.
//112002
//or
//211020
//102120
//122001
//100212
void end(void)
{
    printf("2");
}

 int main() {
     
     if (fork() == 0)
         atexit(end);
     if (fork() == 0)
         printf("0");
     else
         printf("1");
     exit(0);

 }


