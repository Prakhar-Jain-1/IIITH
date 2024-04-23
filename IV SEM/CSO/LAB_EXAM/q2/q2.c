#include<stdio.h>
#include<stdbool.h>
typedef long long int ll;
bool oddBit(ll);
int main() {
    ll n;
    scanf("%lld",&n);
    printf("%s\n", oddBit(n)? "true": "false");
}
