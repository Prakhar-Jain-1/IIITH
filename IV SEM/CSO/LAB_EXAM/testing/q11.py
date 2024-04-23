
def solve(s):
    tot = 0
    v = []
    
    for i in range(n):
        if s[i] == 0:  # 'L' is represented as 0
            v.append((n - 1 - i) - i)
            tot += i
        else:  # 'R' is represented as 1
            v.append(i - (n - 1 - i))
            tot += n - 1 - i
    
    v.sort(reverse=True)
    
    for i in range(n):
        if v[i] > 0:
            tot += v[i]
        print(tot, end=' ')
    
    print()



n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
solve(l)
