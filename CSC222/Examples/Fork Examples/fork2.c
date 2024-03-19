#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main()
{
	pid_t pid, child;
	int c_status;

	// fork another process
	child = fork();
	if (child < 0)
	{
		// error occurred
		printf("Fork failed\n");
		exit(-1);
	}
	else if (child == 0)
	{
		// child process
		printf("Child PID=%d\n", getpid());
		fflush(stdout);

		char* args[] = { "ls", "-alh", NULL };
//		char* args[] = { "ls", "-z", NULL };
		execvp(args[0], args);
		fprintf(stderr, "Error with execvp\n");
		exit(1);
	}
	else
	{
		// parent process
		// wait for the child to complete
		printf("Parent PID=%d\n", getpid());
		//pid = wait(&c_status);
        pid = waitpid(-1, &c_status, 0);
		printf ("Child %ld complete; exited with status %d\n", (long)pid, c_status);
		exit(0);
	}
}
