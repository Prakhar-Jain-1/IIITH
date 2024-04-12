#include<stdio.h>

int Postfix(char[], int);



int main(int argc, char const *argv[]){
    int n = 0;
    scanf("%d\n", &n);
    char arr[n];
    for(int i = 0; i < n; i++){
        scanf("%c", arr + i);
    }
    // for(int i = 0; i < n; i++){
    //     printf("%c", arr[i]);
    // }
    int k = Postfix(arr,n);
    printf("ANSWER = %d\n", k);
}
