#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <errno.h>
//#include <wait.h>
//#include <sys/wait.h>

#define N 10

int main() 
{
    int status, i;
    pid_t pid;

    /* Parent creates N children */
    for (i = 0; i < N; i++)             
	if ((pid = fork()) == 0)  /* Child */     
	    exit(100+i);                          

    /* Parent reaps N children in no particular order */
    while ((pid = waitpid(-1, &status, 0)) > 0) { 
	if (WIFEXITED(status))
        printf("child %d terminated normally with exit status=%d\n",pid, WEXITSTATUS(status));
	else
        printf("child %d terminated abnormally\n", pid);
    }

    if (errno != ECHILD)
      exit(0);
}