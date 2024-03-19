#include <stdlib.h>
#include <stdio.h>
#include <semaphore.h>
#include <pthread.h>
#include <unistd.h> //wait

struct sbuf_t {
char *buffer; /* Buffer array */
int n;     /* Maximum number of slots */
int front; /*  first item */
int rear;  /* last item */
sem_t mutex; /* sempahore to protect accesses to buf */
sem_t slots; /* sempaphore to count available slots */
sem_t items; /* semaphore to count available items */
};

void init(struct sbuf_t *sp, int maxitems);  /* Initialize the data structure sbuf_t members...*/
void clean(struct sbuf_t *sp);        /* Free memory allocated for the buffer */
char produceNextLetter(int i);      /*produce the next letter, starting with 'a'*/
void *producer(void *); /* called by producer thread */
void *consumer(void *); /* called by consumer thread */


int main(int argc, char* argv[]){

    if(argc != 2){
        printf("Usage: %s n where n is the buffer size\n", argv[0]);
        exit(1);
    }
    int n = atoi(argv[1]);

    struct sbuf_t sb;
    init(&sb, n);
    pthread_t tprod;
    pthread_t tcons;
    pthread_create(&tprod, NULL, producer, &sb);
    pthread_create(&tcons, NULL, consumer, &sb);

    pthread_join(tprod, NULL);
    pthread_join(tcons, NULL);
    clean(&sb);
    return 0;
}

/*Initialize all the struct members here*/
void init(struct sbuf_t *sb, int maxsize){
    sb->buffer = (char*)malloc(maxsize*sizeof(char));
    sb->n = maxsize;
    sb->front = sb->rear = 0;
    sem_init(&sb->mutex, 0, 1); //buffer
    sem_init(&sb->slots, 0, maxsize); //slots
    sem_init(&sb->items, 0, 0); //items
}

/*This function will produce the next char. loop back to a when you reach z.*/
char produceNextLetter(int i){
    return (char)(65 + i%26);
}

/*This function will produce and insert the char. at the rear of the buffer */
void* producer(void* param){ //producer() is called with &sb as param
    struct sbuf_t *s = (struct sbuf_t*)param;
    int a = 0;
    while(1){
        char c = produceNextLetter(a++);
        sem_wait(&s->slots);
        sem_wait(&s->mutex);
        s->buffer[s->rear++ %s->n] = c;
        printf("+%c\n", c);
        sem_post(s->mutex);
        sem_post(s->items);
    }
}

/*This function will consume the item at the front of the buffer*/
void* consumer(void* param){
    struct sbuf_t *p = (struct sbuf_t *)param;
    char c;
    while(1){
        sleep(1);
        sem_wait(&p->items);
        sem_wait(&p->mutex);
        c = p->buffer[p->front++ %p->n];
        printf("-%c\n", c);
        sem_post(&p->mutex);
        sem_post(&p->slots);
    }
}


/*Nothig more to be done here*/
void clean(struct sbuf_t *sb){
    free(sb->buffer);
}