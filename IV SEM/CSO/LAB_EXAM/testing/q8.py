def sort_to_wave(N, arr):
    # Step 1: Sort the array
    arr.sort()
    # print(arr)
    for i in range(0, N - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr
n = int(input())
data = input().split()
data = list(map(int, data[0:]))
data = sort_to_wave(n,data)
for i in data:
    print(i,end = ' ')
print()