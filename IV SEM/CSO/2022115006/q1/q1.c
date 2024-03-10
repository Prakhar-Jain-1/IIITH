#include<stdio.h>

int onlyOnce(int arr[], int size);

int main(){
    int n ;
    scanf("%d", &n);
    int arr[2*n + 1];
    for(int i = 0; i < 2*n + 1; i++){
        scanf("%d",arr + i);
    }
    int once = onlyOnce(arr,n);
    printf("%d\n", once);
}