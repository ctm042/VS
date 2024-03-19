#include <stdio.h>
int main(){
    char name[20];
    printf("Enter your first name: ");
    scanf("%s", name);
    printf("\"%s\"\n", name);
    printf("\"%25s\"\n", name);
    printf("\"%-25s\"\n", name);
    return 0;
}