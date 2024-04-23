#include<stdio.h>
typedef long long int ll;

ll gcd(ll,ll);

int main() {
    ll n,m;
    scanf("%lld %lld", &n, &m);
    printf("%lld\n",gcd(n,m));
}
