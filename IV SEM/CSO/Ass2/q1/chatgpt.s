.section .data
format_input:
    .ascii "Enter the value of N, L, R: \n"
format_array:
    .ascii "Enter the array elements: \n"
format_output:
    .ascii "Maximum subarray sum with length between %d and %d is: %d\n"

.section .bss
    .lcomm arr, 1000     # Define array to hold up to 1000 integers (adjust size as needed)

.section .text
.globl _start

# Function to find the maximum of two integers
max:
    cmp %rdi, %rsi
    jge .Lmax_end
    mov %rsi, %rax
    ret
.Lmax_end:
    mov %rdi, %rax
    ret

# Function to calculate the maximum subarray sum with length between L and R
maxSubarraySum:
    push %rbp
    mov %rsp, %rbp
    mov $0, %eax          # maxSum = 0

    mov %rdi, %r12        # arr
    mov %rsi, %r13        # n
    mov %rdx, %r14        # L
    mov %rcx, %r15        # R

    # Dynamic programming table to store maximum subarray sums
    lea (%r13, 1), %r13    # n + 1
    shl $2, %r13           # (n + 1) * 4
    push %r13
    call malloc
    pop %r13
    mov %rax, %rbx         # dp array pointer

    mov $0, %edx           # len = L
.Loop_len:
    cmp %r15, %edx         # while len <= R
    jg .Loop_end

    mov $0, %r8d           # currentMax = 0
    mov $0, %ecx           # maxEndingHere = 0

    # Calculate initial sum for the first subarray of length 'len'
    lea (%rbx, %rdx, 4), %rdi   # dp + len
    mov %edx, %esi         # len
    call sum_subarray

    mov (%rbx, %rdx, 4), %r8d   # currentMax = dp[len]
    mov %r8d, (%rbx, %rdx, 4)

    # Slide the window across the array to compute maximum subarray sums
    mov %edx, %esi         # len
    call sliding_window

    inc %edx               # len++
    jmp .Loop_len

.Loop_end:
    mov $0, %edi           # i = 0
    mov $0, %eax           # maxSum = 0
.Loop_maxSum:
    cmp %r13, %edi         # while i < n
    jge .Loop_maxSum_end

    mov (%rbx, %rdi, 4), %r8d   # dp[i]
    call max
    mov %eax, %r9d

    call max
    mov %eax, %r8d

    inc %edi               # i++
    jmp .Loop_maxSum

.Loop_maxSum_end:
    mov %eax, %edi         # result = maxSum

    pop %rbp
    ret

sum_subarray:
    push %rbp
    mov %rsp, %rbp

    mov $0, %eax           # sum = 0
    mov %rsi, %ecx         # len

.Loop_sum_subarray:
    cmp %rcx, %rsi         # while len > 0
    jle .Loop_sum_subarray_end

    add (%r12), %eax       # sum += arr[i]
    add $4, %r12           # arr++
    dec %ecx               # len--
    jmp .Loop_sum_subarray

.Loop_sum_subarray_end:
    mov %eax, %edi         # return sum

    pop %rbp
    ret

sliding_window:
    push %rbp
    mov %rsp, %rbp

    mov %rsi, %ecx         # len
    mov %rsi, %r10         # len

.Loop_sliding_window:
    cmp %r13, %ecx         # while i < n
    jge .Loop_sliding_window_end

    mov (%r12, %rcx, 4), %eax   # arr[i]
    add %eax, %r8d         # maxEndingHere += arr[i]

    sub (%r12, %rcx, 4), %eax   # arr[i - len]
    add %eax, %r8d         # maxEndingHere -= arr[i - len]

    call max
    mov %eax, %r9d         # currentMax = max(currentMax, maxEndingHere)
    mov %r9d, (%rbx, %rcx, 4)   # dp[i]

    inc %ecx               # i++
    jmp .Loop_sliding_window

.Loop_sliding_window_end:
    mov %r8d, %edi         # return currentMax

    pop %rbp
    ret

_start:
    # Prompt for input: N, L, R
    mov $format_input, %rdi
    call printf

    # Input: N, L, R
    lea arr, %rdi          # arr
    lea arr + 8, %rsi      # &L
    mov $3, %edx           # scanf("%d %d %d", &N, &L, &R)
    call scanf

    # Input: array elements
    mov $format_array, %rdi
    call printf

    lea arr, %rdi          # arr
    mov %rax, %rsi         # N
    shl $2, %rsi           # N * 4 (bytes per integer)
    mov $0, %rdx           # start from index 0

    # Read N integers into the array
.Loop_input:
    cmp %rax, %rdx         # while index < N
    jge .Loop_input_end

    lea (%rdi, %rdx, 4), %rsi   # &arr[index]
    mov $1, %edx           # %d (integer)
    call scanf

    inc %rdx               # index++
    jmp .Loop_input

.Loop_input_end:
    # Calculate the maximum subarray sum with length between L and R
    lea arr, %rdi          # arr
    mov %rax, %rsi         # N
    mov %r8, %rdx          # L
    mov %r9, %rcx          # R
    call maxSubarraySum

    # Output the result
    mov $format_output, %rdi
    mov %r8d, %esi         # L
    mov %r9d, %edx         # R
    mov %rax, %rcx         # result
    call printf

    # Exit the program
    mov $0, %rdi           # status = 0
    call exit
