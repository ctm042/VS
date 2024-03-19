#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
    if(argc < 2 || argc > 6) exit(1);

    for(int i = 0; i < argc; i++){
        if(i % 2 == 0){
            printf("%c ", argv[i][0]);
        }
        else{
            printf("%c ", argv[i][1]);
        }
    }
    return 0;
}