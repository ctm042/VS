#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main( int argc, char *argv[] )  {
    if ( argc == 1 ){
        printf("Usage: ./%s <executable>\n", __FILE__);
        printf(" e.g., ./%s ./one", __FILE__);
    }
    else{
        printf("running bash file");
        pid_t pid = fork();
        if (pid < 0){
            // fork failed
            printf("Fork failed\n");
            exit(-1);
        }
        else if (pid == 0){
            // child process
            srand(0);

            char* cmdarray[rand() % (10 + 1 - 1) + 4];
            cmdarray[0] = "bash";
            cmdarray[1] = argv[1];
            cmdarray[12] = NULL;
            for (int i = 2; i < 11; i++) {
                int num = rand() % (10 + 1 - 0) + 0;
                printf("%d", num);
                cmdarray[i] = num;
            }

            
            //[char* cmd[] = {"bash", argv[1]};
            execvp(cmdarray[0], cmdarray);
        }
        else{
            // parent process
            wait(NULL);
            printf("Child done.\n");
            exit(0);
        }

    }
    
    
}
