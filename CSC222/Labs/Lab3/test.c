#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main( int argc, char *argv[] )  {
    char* ar[] = {"bash", "one.sh", NULL};
    execvp(ar[0], ar);
}