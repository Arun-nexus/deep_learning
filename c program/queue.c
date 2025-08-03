#include <stdio.h>

int q[5];

int f = -1, r = -1;

void enqueue();
void dequeue();
void traverse();

int main()
{
    int ch;

    while (1)
    {
        printf("enter the operation");
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
            traverse();
            break;

        case 4:
            printf("exiting");
            break;

        default:
            printf("invalid choice");

            break;
        }
    }
    return 0;
}

void enqueue()
{
    int v;
    printf("enter the value of for inserting");
    scanf("%d", &v);
    if (f == 4)
    {
        printf("queue is full");
    }
    else
    {
        q[f] = v;
        f++;
    }
}

void dequeue()
{
    if (f == -1)
    {
        printf("queue is empty");
    }
    else
    {
       
        printf("%d", q[r]);
         r++;
    }
}

void traverse()
{
    if (f == -1)
    {
        printf("queue is empty");
    }
    else
    {
        for (int i = r; i <= f; i++)
        {
            printf("%d", q[i]);
        }
    }
}