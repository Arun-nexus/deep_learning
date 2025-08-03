#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next;
};

void insert(struct node **start);
void insertend(struct node **start);
void insertspe(struct node **start);
 void delete(struct node **start);
void display(struct node *start);

int main()
{
    int value;
    struct node *start = NULL;

    while (1)
    {
        printf("enter your choice");
        scanf("%d", &value);

        switch (value)
        {
        case 1:
            insert(&start);

            break;

        case 2:
            insertend(&start);
            break;

        case 3:
            insertspe(&start);
            break;

        case 4:
            delete (&start);
            break;

        case 5:
            display(start);
            break;

        case 6:
            printf("exiting...");
            return 0;

        default:
            printf("wrong choice"
                   "\n");
            break;
        }
    }
}

void insert(struct node **start)
{
    int v;
    printf("enter the value ");
    scanf("%d", &v);
    struct node *newnode = (struct node *)malloc(sizeof(struct node));

    newnode->data = v;
    newnode->next = *start;
    *start = newnode;

    printf("inserted");
    printf("\n");
}

void insertend(struct node **start)
{
    int e;
    printf("enter the value ");
    scanf("%d", &e);

    struct node *newnode = (struct node *)malloc(sizeof(struct node));

    struct node *p = *start;
    if (*start == NULL)
    {
        printf("list is empty");
        printf("\n");
        printf("data is inserted to the begining");

        newnode->data = e;
        newnode->next = *start;
        *start = newnode;
    }
    else
    {
        while (p->next != NULL)
        {
            p = p->next;
        }
        newnode->data = e;
        newnode->next = NULL;
        p->next = newnode;
    }
    printf("\n");
}

void insertspe(struct node **start)
{
    int s;
    printf("enter the data");
    scanf("%d", &s);

    struct node *newnode = (struct node *)malloc(sizeof(struct node));

    if (*start == NULL)
    {
        printf("list is empty");
        printf("\n");
        printf("data is inserted to the begining");

        newnode->data = s;
        newnode->next = *start;
        *start = newnode;
    }
    else
    {
        int l;
        printf("enter the loc");
        scanf("%d", &l);
        struct node *p = *start;

        while (p!=NULL&&p->data != l)
        {
            p = p->next;
        }
        newnode->data = s;
        newnode->next = p->next;
        p->next = newnode;
    }
}

void delete(struct node **start)
{
    if (*start == NULL)
    {
        printf("list is empty");
        return;
    }

    struct node *p = *start;
    *start = (*start)->next;
    printf("%d", p->data);
    free(p);
    printf("\n");
}

void display(struct node *start)
{
    if (start == NULL)
    {
        printf("list is empty");
        return;
    }

    struct node *p = start;
    while (p != NULL)

    {
        printf("%d->", p->data);
        p = p->next;
    }
    printf("NULL"
           "\n");
}