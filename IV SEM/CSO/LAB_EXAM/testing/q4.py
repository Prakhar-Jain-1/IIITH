def is_palindrome(N):
    # Convert the number to a string
    str_N = str(N)
    
    # Check if the string is the same as its reverse
    return str_N == str_N[::-1]
n = int(input())
if is_palindrome(n):
    print("true")
else:
    print("false")