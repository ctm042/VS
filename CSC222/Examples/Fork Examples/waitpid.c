#include<stdio.h>
#include<stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

#define N 2
int main()
{
    int status, i;
    pid_t pid;
    /* Parent creates N children */
    for(i=0;i<N;i++)
        if ((pid = fork()) == 0) /* Child */
            exit(100+i);
    
    /* Parent reaps N children in order */
    
    while ((pid = waitpid(-1, &status, 0)) > 0) {
          if(status)
              printf("child %d terminated normally with exit status=%d\n",
                     pid, status);
                
            else
              printf("child %d terminated abnormally\n", pid);
                
    }
    
    return 0;
}
