#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void* message(void*);

int main()
{
	pthread_t t1, t2;
	char* msg1 = "Thread 1";
	char* msg2 = "Thread 2";
	int r1, r2;

	srand(time(NULL));

	r1 = pthread_create(&t1, NULL, message, (void*) msg1);
	r2 = pthread_create(&t2, NULL, message, (void*) msg2);

	pthread_join(t1, NULL);
	printf("Return from thread 1: exit code=%d\n", r1);
	fflush(stdout);
	pthread_join(t2, NULL);
	printf("Return from thread 2: exit code=%d\n", r2);
	fflush(stdout);

	exit(0);
}

void* message(void* msg)
{
	int r, i;

	r = rand() % 10;

	for (i=0; i<r; i++)
	{
		printf("%s: %d\n", (char*)msg, i);
		fflush(stdout);
		sleep(1);
	}

	pthread_exit(NULL);
}
