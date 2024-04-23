.global maxSum
.text

maxSum:
    movq $0, %r8        # sum
    movq $0, %r10       # initial index
    movq $0, %r11
    movq %rsi, %r9  # endIndex
    decq %r9
    xorq %rax, %rax     # maxSum
    jmp .StartSum

.StartSum:
    movq (%rdi, %r10, 8), %rcx
    addq %rcx, %r8
    incq %r10
    cmpq %rdx, %r10
    jl .StartSum
    movq %r8, %rax
    decq %r10
    jmp .SumLast
    ret

.SumLast:
    movq (%rdi, %r10, 8), %rcx
    subq %rcx, %r8
    movq (%rdi, %r9, 8), %rcx
    addq %rcx, %r8
    decq %r10
    decq %r9
    call .max
    cmpq %r11, %r10
    jge .SumLast
    ret

.max:
    cmpq %rax, %r8
    cmovg %r8, %rax
    ret
