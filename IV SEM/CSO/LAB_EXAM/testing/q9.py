def firstMissing(arr):
    arr.sort()
    n = 1
    for i in arr:
        if i > n:
            return n
        if n == i: n+=1
    return n
n = int(input())
data = input().split()
data = list(map(int, data))
print(firstMissing(data))