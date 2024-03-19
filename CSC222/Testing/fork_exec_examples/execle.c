#include <stdio.h>
#include <unistd.h>

int main()
{
	int ret;
	char* env[] = { "HOME=/home/ibrahim", "LOGNAME=ibrahim", NULL};
	
	ret = execle("/bin/ls", "ls", "-a", "-l", "-h", NULL, env);
}
