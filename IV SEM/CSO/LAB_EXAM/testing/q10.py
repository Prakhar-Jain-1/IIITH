def lexicographically_smallest_array(N, arr):
    # Separate even and odd numbers
    even_nums = False
    odd_nums = False
    
    for num in arr:
        if num % 2 == 0:
            even_nums = True
        else:
            odd_nums = True
    if odd_nums and even_nums:
        arr.sort()
    
    # Merge even and odd arrays to form the final lexicographically smallest array
    # result = even_nums + odd_nums
    
    return arr
n = int(input())
data = input().split()
data = list(map(int, data[0:]))
# print(data)
data = lexicographically_smallest_array(n,data)
for i in data:
    print(i,end = ' ')
print()