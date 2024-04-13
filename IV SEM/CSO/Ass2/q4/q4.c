#include<stdio.h>
int baseball(char[], int);

int main(int argc, char const *argv[]){
    int n;
    scanf("%d",&n);
    char arr[n];
    scanf("%s",arr);
    int  k = baseball(arr, n);
    printf("%d\n",k);
    return 0;
}
