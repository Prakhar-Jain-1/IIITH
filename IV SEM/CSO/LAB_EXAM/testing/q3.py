n = int(input())
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(-3,end=" ")  # Replace with -3 for multiples of both 3 and 5
    elif i % 3 == 0:
        print(-1,end=" ")  # Replace with -1 for multiples of 3
    elif i % 5 == 0:
        print(-2,end=" ")  # Replace with -2 for multiples of 5
    else:
        print(i,end=" ")   # Otherwise, add the number itself
print()