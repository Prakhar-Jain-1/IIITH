#include<stdio.h>
typedef long long int ll;
ll array(ll,ll*);
int main() {
    ll n;
    scanf("%lld",&n);
    printf("%lld\n",n);
    ll arr[n];
    ll k = array(n,arr);
    printf("%lld\n",k);
    for (int i = 0; i < n; i++)
        printf("%lld ", arr[i]);
    printf("\n");
    return 0;
}
