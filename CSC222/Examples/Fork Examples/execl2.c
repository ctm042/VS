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
		int ret;

		printf("Child PID=%d\n", getpid());
		fflush(stdout);
		ret = execl("/bin/ls", "ls", "-a", "-l", "-h", NULL);
		printf(" returned ret....%d\n", ret);	// why isn't this printed out?
	}
	else
	{
		// parent process
		// wait for the child to complete
		printf("Parent PID=%d\n", getpid());
		wait(NULL);
		printf("Child done.\n");
		exit(0);
	}
}
