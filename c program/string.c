#include<stdio.h>
#include<stdlib.h>
// #include<string.h>

// int main(){
//     char n[50];

//     printf("enter the string function");
//     fgets(n, sizeof(n),stdin);

//     printf(n);
    
//     return 0;
// }
int main()
{
    char *s;
    int size=5;

    s=(char*)malloc(sizeof(char));

    if (s==NULL){
        printf("memory allcoation failed");
        return 1;

    }

    printf("enter the snet");
    fgets(s,size,stdin);
    printf(s);
    free(s);

    return 0;

}