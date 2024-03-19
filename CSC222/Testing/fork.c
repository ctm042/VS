#include<stdio.h>
#include<unistd.h>

int main(){
    int x = 10, y = 3;
    pid_t r = fork();
    if(r == 0){ //only the child does this
        x = x*y;
        y = x%y;
    }
    printf("x = %d, y = %d", x, y);
    return 0;
}