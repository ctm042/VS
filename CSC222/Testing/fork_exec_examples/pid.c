#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>



int main()
{
    pid_t me = getpid();
    pid_t parent = getppid();
    printf("my pid =%d; parent pid =%d\n", me, parent);
    return 0;
    
}
