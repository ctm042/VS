#include <stdio.h>
#include <unistd.h>

int main()
{
    //searches for the location of the ls command among the directories
    //specified by the PATH environment variable.
	execlp("ls", "ls", "-a", "-l", "-h", NULL);
}
