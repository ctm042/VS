#include<stdio.h>
#include<unistd.h>

int main(){
    pid_t p = getpid();
    pid_t pp = getppid();
    printf("my pid = %d\n", p);
    printf("parent pid = %d\n", pp);
    return 0;
}