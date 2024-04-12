#include <stdio.h>

// Function to calculate the maximum subarray sum with length between L and R
long long int maxSubarraySum(long long int arr[], int n, int L, int R);
int main() {
    int N, L, R;

    scanf("%d %d %d", &N, &L, &R);

    long long int arr[N];

    for (int i = 0; i < N; i++) {
        scanf("%lld", &arr[i]);
    }

    // Call the assembly function maxSubarraySum
    long long int result = maxSubarraySum(arr, N, L, R);

    // Output the result
    printf("%lld\n", result);

    return 0;
}
