#include<stdio.h>
typedef long long int ll;
void waveSort(ll,ll*);
int main() {
    ll n;
    scanf("%lld", &n);
    ll arr[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%lld", arr+i);
    }
    waveSort(n, arr);
    for (int i = 0; i < n; i++)
    {
        printf("%lld ", arr[i]);
    }
    printf("\n");
    return 0 ;
}
