# int min(int a, int b) {
#     return (a < b) ? a : b;
# }
# 
# // Helper function to find the maximum of two numbers
# int max(int a, int b) {
#     return (a > b) ? a : b;
# }
# 
# int nCr(int n,int r){
#     if(r == 0 || r == n) return 1;
#     int k = max(n-r, r);
#     k++;
#     int f = min(n-r, r);
#     int mul = 1;
#     while (k <= n)
#     {
#         mul*=k;
#         k++;
#     }
#     k = 2;
#     while(k <= f)
#     {
#         mul/=k;
#         k++;
#     }
#     return mul;
# }

.global nCr
.text


.max:
    movq %r8, %r9
    movq %rsi, %r8
    ret
.min:
    movq %rsi, %r9
    ret

.min_max:
    cmpq %rsi, %r8
    jl .max
    jmp .min
    ret

nCr:
    movq $1, %rax

    cmpq $0, %rsi
    je .exit1
    cmpq %rdi, %rsi
    je .exit1

    movq %rdi, %r8
    subq %rsi, %r8
    call .min_max
    movq %r8, %rdx
    incq %rdx
    call .numerator
    movq $2, %r10
    call .denominator
    ret

.numerator:
    imulq %rdx, %rax
    incq %rdx
    cmpq %rdi, %rdx
    jle .numerator    
    ret


.denominator:
    # movq %rdx, %r10
    cqto
    idivq %r10
    incq %r10
    cmpq %r9, %r10
    jle .denominator    
    ret



.exit1:
    ret
