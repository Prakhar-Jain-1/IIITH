def max_sum_from_ends(N, B, A):
    # Initialize prefix sums and suffix sums arrays
    prefix_sum = [0] * (N + 1)
    suffix_sum = [0] * (N + 1)

    # Calculate prefix sums
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]

    # Calculate suffix sums
    for i in range(1, N + 1):
        suffix_sum[i] = suffix_sum[i - 1] + A[N - i]

    # Initialize maximum sum
    max_sum = float('-inf')

    # Iterate over possible values of x (0 to B)
    for x in range(min(B + 1, N + 1)):
        y = B - x
        if y <= N:
            current_sum = prefix_sum[x] + suffix_sum[y]
            max_sum = max(max_sum, current_sum)

    return max_sum

# # Reading input
# import sys
# input = sys.stdin.read
i = input().split()
data = input().split()

# First line contains N and B
N = int(i[0])
B = int(i[1])

# Second line contains the array elements
A = list(map(int, data[0:]))

# Calculate and print the maximum possible sum
result = max_sum_from_ends(N, B, A)
print(result)
