#include<stdio.h>

int isPalindrome(char* str);


int main(int argc, char const *argv[])
{
    char str[200] = {0};
    scanf("%s",str);
    int isP = isPalindrome(str);

    printf("%d\n",isP);
    return 0;
}
