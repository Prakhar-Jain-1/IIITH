#include<stdio.h>

int nCr(int n,int r);

int main(int argc, char const *argv[])
{
    int n,r;
    scanf("%d %d",&n,&r);
    printf("%d\n", nCr(n,r));
    return 0;
}

