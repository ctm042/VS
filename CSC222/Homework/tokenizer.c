// Name: Caleb Matherne
// Date: 1/12/23
// Desc: Homework 2

// include libraries
#include<stdio.h>
#include<string.h>

int main(){
    // declare input
    char input[256];

    // initialize prompt header
    char prompt[3] = "$ ";

    // initialize delimiter
    char delim[1] = " ";

    // declare token count
    int tokcount;

    // enter loop
    while(1){
        // begin to prompt
        printf("%s", prompt);

        // define input
        fgets(input, 257, stdin);

        // catch exit case to break loop
        if(strcmp(input, "exit\n") == 0) break;

        // print input
        printf("Line read: %s",input);

        // reset(define) token count
        tokcount = 0;

        // print header for tokens
        printf("Token(s):");

        // tokenize
        for (char *token = strtok(input,delim); token != NULL; token = strtok(NULL, delim)){
            // print out each token
            printf("\n %s",token);

            // increment token count
            tokcount++;
        }

        // print token count
        printf("%d token(s) read\n\n", tokcount);
    }
    return 0;
}