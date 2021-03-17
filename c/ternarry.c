#include <stdio.h>
int main()
{
  int a = 10, b = 20;
    //using if else
    if (a > b)
    {
        printf("%d is bigger.",a);
    }
    else
    {
        printf("%d is bigger.",b);
    }
    //using ternary conditional operator
    printf("\n%d is bigger",(a>b)?a:b);
    return 0;
}
//Output:
//20 is bigger
//20 is bigger
