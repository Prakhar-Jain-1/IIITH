#include<stdio.h>
#include <stdio.h>

int binarySearch(int arr[], int* idx, int target);


int main(int argc, char const *argv[]){
    int arr[32];
    for (int i = 0; i < 32; i++)
    {
        scanf("%d", arr + i);
    }
    int idx = -1;
    int target;
    scanf("%d",&target);
    int i = binarySearch(arr,&idx,target);
    printf("%d %d\n", idx,i);
    
    return 0;
}
