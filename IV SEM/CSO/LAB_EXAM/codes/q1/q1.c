#include<stdio.h>
typedef long long int ll;

ll compute(ll, ll, ll);

int main(){
    ll n,m,s;
    scanf("%lld %lld %lld", &n, &m, &s);
    printf("%lld\n",compute(n,m,s));
}
