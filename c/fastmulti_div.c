#include <stdio.h>

int main()
{
    int x,y=0;
    x = 18;
    y = x << 3; //x will be multiplied with 6
    printf("%d",y);//144
    y = x >> 3;  //x will be divided by 6
    printf("\n%d",y);//2
    return 0;
}
