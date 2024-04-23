n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
# print(l)
l.sort()
for i in l:
    print(i,end=' ')
print()
