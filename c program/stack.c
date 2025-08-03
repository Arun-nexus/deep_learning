#include <stdio.h>
int s[5];

void enqueue();
void dequeue();
void transverse();

int top = 0;

int main()
{
    int ch;
 printf("enter the operation:");
    while (1)
    {
       
        scanf("%d", &ch);

        switch (ch)
        {
        case 1:
            enqueue();

            break;
        case 2:
            dequeue();
            break;

        case 3:
            transverse();
            break;

        case 4:
            printf("exiting...");
            return 0;
            break;

        default:
            printf("invalid operation");

            break;
        }
    }

    return 0;
}
void enqueue()
{
    int v;
    printf("enter the value which you want to add");
    scanf("%d", &v);
    if (top >= 5)
    {
        printf("stack is full");
    }
    else
    {
        s[top] = v;
        top ++;
    }
}

void dequeue()
{
    int d;

    if (top == 0)
    {
        printf("stack is empty");
    }
    else
    {
      
        top --;

        printf("%d",s[top]);
    }
}

void transverse()
{
    int i;
    int d;

    if (top == 0)
    {
        printf("stack is empty");
    }
    else
    {
        for (i = top-1; i >=0; i--)
        {
            
            printf("%d", s[i]);
        }
    }
}