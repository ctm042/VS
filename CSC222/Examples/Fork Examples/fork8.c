#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

//How many lines of output does the following function print? Give your answer as a function of n. Assume n ≥ 1.
void end(void)
{
    printf("2");
}

 int main() {
     
     int i;
     int n;
     printf("Enter number of n: \n");
     scanf("%d", &n);
     for (i=0;i<n;i++)
         fork();
     printf("hello\n");
     exit(0);

 }


