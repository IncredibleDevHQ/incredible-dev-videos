#include <stdio.h>

int main()
{
    int a,b;
    a=9;b=8;
    a=a+b-(b=a);//17-9
    printf("After swapping: A= %d,B= %d",a,b);
    return 0;
}
//output:
//After swapping : A= 8, B= 9   
