def gcd(M, N):
    # Ensure M >= N for the algorithm to work properly
    if N > M:
        M, N = N, M
    
    while N != 0:
        M, N = N, M % N
    
    return abs(M)

m, n = input().split()
m = int(m)
n = int(n)
print(gcd(n,m))