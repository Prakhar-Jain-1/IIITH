.bubbleSort:
    xorq %r9, %r9
    movq %r11, %r10
    subq %r8,%r10
    cmpq %r10, %r9
    jl .looper
    ret

.looper:
    call .maxi
    cmpq %r10, %r9
    jl .looper    
    incq %r8
    cmpq %rax, %r8
    jl .bubbleSort
    ret

.maxi:
    movq (%rsi, %r9, 8), %r12
    movq 8(%rsi, %r9, 8), %r13
    movq %r12, %r15
    movq %r13, %r14
    cmpq %r13, %r12
    cmovl %r12, %r14
    cmpq %r13, %r12
    cmovl %r13, %r15
    movq %r14, (%rsi,%r9,8)
    movq %r15, 8(%rsi,%r9,8)
    incq %r9
    ret
