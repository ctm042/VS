// Name Ryan Texada && Caleb Matherne
#include<stdio.h>
int main(){
    int num;
    int boolean; //0=false, 1=true
    while(1){
        printf("Please enter an integer >= 2; Enter 0 to quit.\n");
        scanf("%d", &num);
        if(num == 0) break;

        if(num >= 2){
            boolean = 1;
            for(int i = 2; i < num/2; i++){
                //printf("%d\n",i);
                if(num % i == 0){
                    printf("%d is divisible by %d", num, i);
                    if (i*i != num){
                        printf(" and %d",num/i);
                    }
                    printf(".\n");
                    boolean = 0;
                }
            }
            if (boolean == 1){
                printf("%d is prime.\n", num);
            }
        }
    }
    printf("Bye.\n");
    return 0;
}