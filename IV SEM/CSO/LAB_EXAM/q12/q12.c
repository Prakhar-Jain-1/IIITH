#include<stdio.h>
#include<stdbool.h>
typedef long long int ll;
bool spNumber(ll);
int main() {
    ll n;
    scanf("%lld", &n);
    bool ret = spNumber(n);
    printf("%s\n", ret?"TRUE":"FALSE");
    return 0;
}
