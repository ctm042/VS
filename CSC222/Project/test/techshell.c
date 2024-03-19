// Name: Ryan Texada
// Date: February 2023
// Description: Programming Project


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <fcntl.h>
#include <sys/wait.h>

#define MAX_ARGS 100
#define MAX_LEN 1024
#define DEBUG 0 // you can enable debugging when set to 1

int main() {
	char cwd[MAX_LEN];
	char *args[MAX_ARGS];
	char *in_file = NULL;
	char *out_file = NULL;
	int in_fd, out_fd;
	int num_args, status;
	pid_t pid;

	while(1) {
		// getting the current working directory
		if (getcwd(cwd, sizeof(cwd)) == NULL) {
			perror("getcwd() error");
			return 1;
		}

		// printing the shell prompt
		printf("%s$ ", cwd);
		fflush(stdout);

		// reading command line input
		char *line = NULL;
		size_t l_size = 0;
		ssize_t num_chars = getline(&line, &l_size, stdin);

		if (num_chars == -1) {
			perror("getline() error");
			return 1;
		}

		line[strlen(line)-1] = '\0'; // this removes the  newline character
		
		// getting command line arguments
		num_args = 0;
		char *token = strtok(line, " ");
		while (token != NULL) {
			if (strcmp(token, "<") == 0) {
				// redirection for input
				token = strtok(NULL, " ");
				in_file = token;
			}

			else if (strcmp(token, ">") == 0) {
				// redirection for output
				token = strtok(NULL, " ");
				out_file = token;
			}

			else {
				// if a regular argument
				args[num_args++] = token;
			}

			token = strtok(NULL, " ");
		}

		args[num_args] = NULL;


		// fork for child proccess
		pid = fork();
		if (pid < 0) {
			perror("fork() error");
			return 1;
		}

		else if (pid == 0) {
			// child
			if (in_file != NULL) {
				// open input file, read only
				in_fd = open (in_file, O_RDONLY);
				if (in_fd < 0) {
					fprintf(stderr, "open() error: %s\n", strerror(errno));
					return 1;
				}

				// redirecting input to input file 
				if (dup2(in_fd, STDIN_FILENO) < 0) {
					fprintf(stderr, "dup2() error: %s\n", strerror(errno));
					return 1;
				}

				close(in_fd);
			}

			if (out_file != NULL) {
				// open an output file to write to
				// if one doesnt exist create it
				// if it does exist then truncate it
				out_fd = open(out_file, O_WRONLY | O_CREAT | O_TRUNC, 0644);
				if (out_fd < 0) {
					fprintf(stderr, "open() error: %s\n", strerror(errno));
					return 1;
				}

				// redirecting output to output file
				if (dup2(out_fd, STDOUT_FILENO) < 0) {
					fprintf(stderr, "dup2() error: %s\n", strerror(errno));
					return 1;
				}

				close(out_fd);
			}

			// this is to execute the command
			if (execvp(args[0], args) < 0) {
				fprintf(stderr, "execvp() error: %s\n", strerror(errno));
				return 1;
			}

            // swap ^ with v
            
            execvp(args[0], args);
            perror("execvp";)
            exit(EXIT_FAILURE);


			else {
				// parent process
				waitpid(pid, &status, 0);
				if (WIFEXITED(status)) {
					if (DEBUG) printf("The child exited with status %d\n", WEXITSTATUS(status));
				}
			}


			// resets variables to prepare for the next command
			in_file = NULL;
			out_file = NULL;
			free(line);
		}

		return 0;
	}
}