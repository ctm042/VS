#include <stdio.h>
#include <errno.h>
#include <string.h>

extern int errno;

int main()
{
	FILE *fh;
	fh = fopen("test.txt", "r");
	if (fh == NULL)
		printf("errno=%d; error=%s\n", errno, strerror(errno));
	else
		fclose(fh);
}
