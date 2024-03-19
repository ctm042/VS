#include<stdio.h>
#include<unistd.h>
#include<wait.h>

int main(){
    int x = 10, y = 3;
    pid_t r = fork();
    if(r == 0){
        execl("/bin/ls", "ls", "-la", "-h", NULL);
        printf("Done listing\n");
    }
    else{
        wait(NULL);
    }
    printf("x = %d, y = %d\n", x, y);
    return 0;
}