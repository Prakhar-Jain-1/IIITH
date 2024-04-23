def is_special_number(n):
    # Precompute factorials of digits 0-9
    factorials = [1] * 10  # factorials[0] = 1, factorials[1] = 1, ..., factorials[9] = 1
    for i in range(2, 10):
        factorials[i] = factorials[i-1] * i
    
    # Calculate sum of factorial of digits of n
    digit_sum_factorials = 0
    original_n = n
    
    while n > 0:
        digit = n % 10
        digit_sum_factorials += factorials[digit]
        n //= 10
    
    # Check if the sum of factorial digits equals the original number
    return digit_sum_factorials == original_n

# Main function to test input/output
def main():
    n = int(input())
    if is_special_number(n):
        print("TRUE")
    else:
        print("FALSE")

if __name__ == "__main__":
    main()
