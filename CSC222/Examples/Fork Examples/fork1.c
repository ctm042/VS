#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

 int main() {
     
     int i;
     for (i = 0; i < 4; i++){
       fork();
     }
    printf("hello\n");
exit(0);

 }
