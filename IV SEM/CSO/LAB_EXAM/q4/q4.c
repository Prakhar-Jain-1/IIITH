#include<stdio.h>
#include<stdbool.h>
typedef long long int ll;
bool isPalindrome(ll);
int main() {
    ll n;
    scanf("%lld", &n);
    printf("%s\n",isPalindrome(n)? "true": "false");
}
