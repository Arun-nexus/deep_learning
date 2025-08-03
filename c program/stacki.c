#include<stdio.h>
#define n 5
int a[n];
int top =-1;

void insert()
{
if (top==n-1){
    printf("stack is full");

}
else{
    int j;

    printf("enter the number for inserting in the stack");
    scanf("%d",&j);
    top++;

    a[top]=j;

}
}
void delete(){
    if (top==-1){
        printf("stack is empty");

    }
    else{
        printf("the deleted element is  %d  ",  a[top]);
        top--;

    }
}
void display(){
    if (top==-1){
        printf("stack is empty");

    }
    else{
        int i;

        for(i=0;i<=top;i++){
            printf("stack elements are %d",a[i]);

        }
    }
}

int main(){
    while (1){int m;
    printf("enter your choice");
    scanf("%d",&m);
    switch(m){
        case 1:
        insert();
        break;

        case 2:
        display();
        break;

        case 3:
        delete();
        break;
        case 4:
        printf("exiting from thh efunction");
        return 0;
        default :
        printf("error");

    }
    }
}