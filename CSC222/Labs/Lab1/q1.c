#include <stdio.h>
#include <string.h>
int main(){
    char text[20];
    printf("Enter an input string: ");
    scanf("%[^\n]s", text);
    printf("\"%s\"\n", text);

    int i, len, temp;
    len = strlen(text);
    for (i = 0; i < len/2; i++){
        temp = text[i];
        text[i] = text[len - i - 1];
        text[len - i - 1] = temp;
    }

    printf("\"%s\"\n", text);    
    
    return 0;
}