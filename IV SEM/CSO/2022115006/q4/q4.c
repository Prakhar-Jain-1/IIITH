#include<stdio.h>
#include<math.h>

int sumMinMax(int arr[],int n);

int main(int argc, char const *argv[])
{
    int n;
    scanf("%d",&n);
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d",arr + i);
    }
    int k = sumMinMax(arr,n);
    printf("%d\n", k);
    return 0;
}
