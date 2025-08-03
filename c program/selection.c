#include <stdio.h>

int main()
{
    int n;
    printf("enter the length of the array");
    scanf("%d", &n);

    int a[n];
    int i;

    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }

    // for sorting
    int min;
    int temp;
    int p;
    int j;


    for (i = 0; i < n-1; i++)
    {                                                               //  1 5 8 4 9  i=0  n=3
        min = i;
        for (j = i+1; j < n; j++)
        {

            if (a[j] < a[min])
            {
               min=j;
               
            
            }
        }
        if (min != a[i])
        {
            p = a[min];
            a[min] = a[i];
            a[i] = p;
        }
    }
    
    for (i=0;i<n;i++){
printf("%d",a[i]);
    }
return 0;
}
