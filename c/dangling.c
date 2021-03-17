#include <stdio.h>
int main()
{
   int* ptr = NULL ;
{ 
    int x = 10; 
    ptr = &x; 
} 
printf("%d", *ptr); //10
printf("%d", &x); //throws error
}

