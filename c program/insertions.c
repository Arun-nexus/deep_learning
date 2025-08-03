#include <stdio.h>

int main()
{
    int n;  int a[n];int i;

    printf("enter the element of the array");
    scanf("%d", &n);
  

    printf("enter the value of tha array");
    

    for (i = 0; i < n; i++)
    {
        scanf("%d", a[i]);
    }
    int p;
    int j, c;

    for (i = 1; i < n; i++)
    {
        p = a[i];
        for (j = i - 1; j < n; j++)
        {
            while (p > a[j])
            {
                c=a[j];
                a[j]=p;
                p=c;

            }
        }
        p=a[j]+1;


    }


    // 6 1 4 7 8
    return 0;
}