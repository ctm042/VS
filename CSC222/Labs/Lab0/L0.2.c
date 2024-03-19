#include <stdio.h>

#define MPH 60

int main(){
    int mns = 0;
    //if(mns != 0) printf("%d", mns);
    while(1){
        printf("Ender the number of mns to convert (0 to quit): ");
        scanf("%i", &mns);
        if(mns == 0) break;
        printf("%d minutes = %d hour and %d minutes\n", mns, mns/MPH, mns%MPH);
    }
    printf("Done\n");
    return 0;
    }