#include<stdio.h>
typedef long long int ll;
ll maxSum(ll[],ll,ll);

int main() {
    ll n,b;
    scanf("%lld %lld", &n, &b);
    ll arr[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%lld",arr+i);
    }
    printf("%lld\n", maxSum(arr,n,b));
    return 0;
}
