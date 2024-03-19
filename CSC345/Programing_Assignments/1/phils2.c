// Name: Caleb Matherne
// Date: 4/16/2023
// Description: Programming assignment #1 (Dinning Philosophers' problem)

#include <stdlib.h>
#include <stdio.h>
#include <semaphore.h>
#include <pthread.h>
#include <unistd.h>

#define DEBUG

int nump;           // declare number of philosophers variable
int nume;           // declare number of times to eat variable
sem_t* chopsticks;  // declare chopsticks array

void* Ph(void*);    // declare philosopher function

// Main function
int main(int argc, char* argv[]){

    nump = atoi(argv[1]);   // assign number of philosophers from arguments
    nume = atoi(argv[2]);   // assign number of times to eat from arguments

    // Create the chopsticks (Chopsticks)
    chopsticks = (sem_t*)malloc(nump * sizeof(sem_t));  // allocate space for the chopsticks array with the dynamic size
    for(int i = 0; i < nump; i++){                      // for each semaphore
        sem_init(&chopsticks[i], 0, 1);                     // create the shared semaphore with an initial value of 1
        #ifdef DEBUG
            printf("Created chopstick %d\n", i);
        #endif
    }

    // Create the threads (Philosophers)
    pthread_t philosophers[nump];                               // create the thread array
    int ids[nump];                                              // declare an id array 
    for(int i = 0; i < nump; i++){                              // for each thread
        ids[i] = i;                                                 // assign each index of the id array to a unique id
        pthread_create(&philosophers[i], NULL, Ph, &ids[i]);        // create the thread and start the Ph function with its unique id
        #ifdef DEBUG
            printf("Created philosopher %d\n", i);
        #endif
    }

    // Clean up
    for(int i = 0; i < nump; i++){              // for each thread
        pthread_join(philosophers[i], NULL);        // join the thread
    }
    free(chopsticks);                           // free the allocated semaphores
}

void* Ph(void* param){
    int id = *(int *)param;     // set id 
    int L = id;                 // chopstick id to the left
    int R = (id + 1) % nump;    // chopstick id to the right

    for (int i = 0; i < nume; i++){                             // for the number of times to eat
        printf("Philosopher %d is thinking... \n",id);              // print thinking
        usleep(100*1000);                                           // sleep

        if(id%2==0){                                                // if the id is even
            sem_wait(&chopsticks[L]);                                   // grab left chopstick first
            #ifdef DEBUG
                printf("P%d [%d|-]\n",id,L);
            #endif
            sem_wait(&chopsticks[R]);                                   // grab right chopstick second
            #ifdef DEBUG
                printf("P%d [%d|%d]\n",id,L,R);
            #endif
        }
        else{                                                       // if the id is odd
            sem_wait(&chopsticks[R]);                                   // grab right chopstick first
            #ifdef DEBUG
                printf("P%d [-|%d]\n",id,R);
            #endif
            sem_wait(&chopsticks[L]);                                   // grab left chopstick second
            #ifdef DEBUG
                printf("P%d [%d|%d]\n",id,L,R);
            #endif
        }
        printf("Philosopher %d is eating... [%d/%d]\n",id,i+1,nume);// print
        usleep(100*1000);                                           // sleep
        sem_post(&chopsticks[L]);                                   // release left chopstick 
        sem_post(&chopsticks[R]);                                   // release right chopstick 
        
    }
}

