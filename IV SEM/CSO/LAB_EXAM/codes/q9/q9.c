#include<stdio.h>
typedef long long int ll;

ll firstNonNeg(ll,ll*);

int main() {
    ll n;
    scanf("%lld",&n);
    ll arr[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%lld", arr + i);
    }
    printf("%lld\n", firstNonNeg(n, arr));
    
}
