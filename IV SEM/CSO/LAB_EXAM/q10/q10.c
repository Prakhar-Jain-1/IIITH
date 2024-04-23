#include<stdio.h>
typedef long long int ll;

void WeirdRearrange(ll,ll*);

int main() {
    ll n;
    scanf("%lld",&n);
    ll arr[n];
    for (int  i = 0; i < n; i++)
    {
        scanf("%lld", arr + i);
    }
    WeirdRearrange(n,arr);
    for (int  i = 0; i < n; i++)
    {
        printf("%lld ", arr[i]);
    }
    printf("\n");
    return 0;
}
