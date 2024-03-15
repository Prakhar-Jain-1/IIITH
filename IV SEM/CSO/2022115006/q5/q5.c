#include<stdio.h>

void productWOele(long long int* ,int n ,long long int[]);


int main(int argc, char const *argv[])
{
    int n;
    
    scanf("%d",&n);
    
    long long int arr[n],arr1[n];
    
    for(int i = 0; i < n; i++){
        scanf("%lld",arr + i);
        arr1[i] = arr[i];
    }

    productWOele(arr,n,arr1);
    
    for (int i = 0; i < n; i++)
    {
        printf("%lld ",arr[i]);
    }
    
    printf("\n");
    return 0;
}
