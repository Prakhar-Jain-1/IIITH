#include<stdio.h>
typedef long long int ll;

void mundi(ll,ll*,char*);

int main() {
    ll n;
    scanf("%lld\n", &n);
    char arr[n];
    ll ret[n];
    for (int i = 0; i < n; i++){
        scanf("%c", arr + i);
        if(arr[i] != 48 && arr[i] != 49) i--;
    }
    mundi(n, ret, arr);
    for (int  i = 0; i < n; i++)
    {
        printf("%lld ", ret[i]);
    }
    printf("\n");
    return 0;
}
