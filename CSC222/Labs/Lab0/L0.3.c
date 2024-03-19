#include <stdio.h>

int main(){
    unsigned int input;
    printf("Give me a number: ");
    scanf("%u", &input);
    unsigned sum = 0;
    while(input != 0){
        sum += input % 10;
        input /= 10; //input = input /10
    }
    printf("Sum = %u\n", sum);
    return 0;
}