#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
#include <sys/wait.h>

//#define DEBUG
#define MAX_COMMAND_LENGTH 1024
#define MAX_ARGS 64

// Define the shell prompt format
#define SHELL_PROMPT_FORMAT "\033[1;32m%s$\033[0m "

// Declare functions
void print_prompt();
char* get_input();
void parse_input(char* input, char** args, char** input_file, char** output_file);
void execute_command(char** args, char* input_file, char* output_file);

int main() {
    #ifdef DEBUG
        printf("%s\n","[main]");
    #endif

    char* input; // Pointer to user input

    char** args = malloc(MAX_ARGS * sizeof(args)); // Array of pointers to command line arguments
    //char* args[MAX_ARGS]; 
    
    
    char* input_file; // Pointer to input file name
    //char* input_file = malloc(sizeof(input_file));


    char* output_file; // Pointer to output file name
    //char* output_file = malloc(sizeof(output_file));

    while (1) { // Main loop
        print_prompt(); // Print the shell prompt
        input = get_input(); // Get user input
        parse_input(input, args, &input_file, &output_file); // Parse the input
        
        // handle built-in commands
        if (strcmp(args[0], "cd") == 0) {
            if (chdir(args[1]) == -1) {
                perror("chdir() error");
            }
            continue;
        } 
        else if (strcmp(args[0], "exit") == 0) {
            break;
        }

        execute_command(args, input_file, output_file); // Execute the command

        free(input); // Free the memory used by input
        //free(input_file); // Free the memory used by input file
        input_file = NULL;
        //free(output_file); // Free the memory used by output file
        output_file = NULL;
    }
    return 0;
}

// Prints the shell prompt
void print_prompt() {

    #ifdef DEBUG
        printf("%s\n","[print_prompt]");
    #endif

    char cwd[MAX_COMMAND_LENGTH]; // Character array to store the current working directory
    if (getcwd(cwd, sizeof(cwd)) != NULL) { // If the current working directory is successfully obtained
        printf(SHELL_PROMPT_FORMAT, cwd); // Print the shell prompt with the current working directory
    } 
    else {
        perror("getcwd() error"); // Print an error message if there is an error in getting the current working directory
    }
}

// Gets user input
char* get_input() {

    #ifdef DEBUG
        printf("%s","[get_input]");
    #endif

    char* input = (char*) malloc(MAX_COMMAND_LENGTH); // Allocate memory for input
    if (input == NULL) { // If memory allocation fails
        perror("malloc() error"); // Print an error message
        exit(EXIT_FAILURE);
    }
    fgets(input, MAX_COMMAND_LENGTH, stdin); // Get user input
    input[strcspn(input, "\n")] = 0;//'\0'; // Replace the newline character at the end of input with a null terminator
    return input; // Return the pointer to input
}

// Takes the user input and separates it into individual arguments and input/output files
void parse_input(char* input, char** args, char** input_file, char** output_file) {
    
    #ifdef DEBUG
        printf("%s\n","[parse_input]");
    #endif

    int i = 0; // Initialize index variable
    char* token = strtok(input, " "); // Get first token

    #ifdef DEBUG
        printf("tokens = %s\n", token);
    #endif

    while (token != NULL) { // Loop untill each token has been tokenized
        if (strcmp(token, "<") == 0) { // Check for input redirection
            *input_file = strtok(NULL, " "); // Found redirection, set input file
        }
        else if (strcmp(token, ">") == 0) { // Check for output redirection
            *output_file = strtok(NULL, " "); // Found redirection, set output file
        }
        else { // Otherwise, add the token as an argument
            args[i] = strdup(token); // Add token to args array
            i++; // Increment index variable
        }
        token = strtok(NULL, " "); // Get next token

        #ifdef DEBUG
            printf("         %s\n", token);
        #endif
    }
    #ifdef DEBUG
        printf("input_file = %s\n", *input_file);
        printf("output_file = %s\n", *output_file);
    #endif
    
    args[i] = NULL; // Terminate the argument list with NULL
}

// Executes the command, redirecting stdin/stdout accordingly.
void execute_command(char** args, char* input_file, char* output_file) {

    #ifdef DEBUG
        printf("%s\n","[execute_command]");
    #endif

    pid_t pid = fork(); // Fork the process
    if (pid == -1) { // If fork fails
        perror("fork"); // Print an error message
        exit(EXIT_FAILURE);
    } 
    else if (pid == 0) { // Child process
        
        if (input_file != NULL) { // If output file is given
            
            FILE* infile = fopen(input_file, "r"); // Open file to read
            if (infile == NULL) { // If input file is invalid
                perror("fopen"); // Print an error message
                exit(EXIT_FAILURE);
            }
            dup2(fileno(infile), STDIN_FILENO); // Redirect input from file
            fclose(infile); // Close the file
        }
        if (output_file != NULL) {
            FILE* outfile = fopen(output_file, "w"); // Open file to write
            if (outfile == NULL) { // If output file is invalid
                perror("fopen"); // Print an error message
                exit(EXIT_FAILURE);
            }
            dup2(fileno(outfile), STDOUT_FILENO); // Redirect output to file
            fclose(outfile); // Close the file
        }

        execvp(args[0], args); // Execute command
        perror("execvp"); // If execvp returns, print an error message
        exit(EXIT_FAILURE);
    } 
    else { // Parent process
        int status;
        if (wait(&status) == -1) { // Wait for child to end
            perror("wait() error"); // Print an error message if parent returns -1
        }
    }
}