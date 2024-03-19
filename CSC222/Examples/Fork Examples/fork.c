#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main()
{
	pid_t  pid;

	// fork another process
	pid = fork();
	if (pid < 0)
	{
		// error occurred
		printf("Fork failed\n");
		exit(-1);
	}
	else if (pid == 0)
	{
		// child process
		printf("Child PID=%d\n", getpid());
		fflush(stdout); //clear the output buffer and move the buffered data to console

		int i;

		for (i=0; i<3; i++)
		{
			printf("%d...", i);
			fflush(stdout);
			sleep(2);
		}
		printf("\n");
		fflush(stdout);
		execlp("/bin/ls", "ls", NULL);
		fflush(stdout);
	}
	else
	{
		// parent process
		// wait for the child to complete
		printf("Parent PID=%d\n", getpid());
		wait(NULL); //wait to terminate, only
		printf ("Child complete\n");
		exit(0);
	}
}
