import sys
n = int(input())
k = 0
while n:
    if n%2 == 1: k+=1
    n=n//2
print(k%2 == 1)