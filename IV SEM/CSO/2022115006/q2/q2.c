#include<stdio.h>
void* Rotate(int* arr, int n);

int main(int argc, char const *argv[])
{
    int n;
    scanf("%d",&n);
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d",arr + i);
    }
    Rotate(arr,n);
    // printf("%d",);
    for (int i = 0; i < n; i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n");
    return 0;
}
