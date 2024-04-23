# Read input
input_str = input()
M, N, S = input_str.split()

# Convert M and N to integers
M = int(M)
N = int(N)

# Perform operation based on S
if S == '1':
    result = M + N
elif S == '2':
    result = M - N
elif S == '3':
    result = M / N
elif S == '4':
    result = M ** N
elif S == '5':
    result = M % N

print(int(result))
