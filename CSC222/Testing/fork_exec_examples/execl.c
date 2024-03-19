#include <stdio.h>
#include <unistd.h>

int main()
{
	int ret;
	
	ret = execl("/bin/ls", "ls", "-a", "-l", "-h", NULL);
    printf("What happen after?\n");
}
