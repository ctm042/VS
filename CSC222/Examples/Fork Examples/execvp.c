#include <stdio.h>
#include <unistd.h>

int main()
{
     //searches for the location of the ls command among the directories specified by the PATH
    // environment variable, and passes arguments to the ls command in the cmd array.
	char* cmd[] = { "ls", "-a", "-l", "-h", NULL };

	execvp("ls", cmd);
}
