.global mundi
.text

mundi:
    movq $0, %r8
    movq $0, %r9
    movq %rdi, %rax
    decq %rax
    call .totalCalc
    movq $0, %r8
    pushq %r9
    call .bubbleSort
    movq $0, %r8
    popq %r9
    call .summer
    ret

.bubbleSort:
    xorq %r9, %r9
    movq %rax, %r10
    subq %r8,%r10
    cmpq %r10, %r9
    jl .looper
    ret

.looper:
    call .mini
    cmpq %r10, %r9
    jl .looper    
    incq %r8
    cmpq %rax, %r8
    jl .bubbleSort
    ret

.mini:
    movq (%rsi, %r9, 8), %r12
    movq 8(%rsi, %r9, 8), %r13
    movq %r12, %r15
    movq %r13, %r14
    cmpq %r13, %r12
    cmovg %r12, %r14
    cmpq %r13, %r12
    cmovg %r13, %r15
    movq %r14, (%rsi,%r9,8)
    movq %r15, 8(%rsi,%r9,8)
    incq %r9
    ret


.totalCalc:
    movsbq (%rdx, %r8, 1), %r10
    cmpq $48, %r10
    je .zero
    jmp .one
.zero:
    addq %r8, %r9
    movq $0, %r12
    movq %rax, %r11
    subq %r8, %r11
    subq %r8, %r11
    cmpq $0, %r11
    cmovg %r11, %r12
    movq %r12, (%rsi, %r8, 8)
    incq %r8
    cmpq %r8, %rdi
    jg .totalCalc
    ret
.one:
    addq %rax, %r9
    subq %r8, %r9
    movq $0, %r12
    movq %r8, %r11
    subq %rax, %r11
    addq %r8, %r11
    cmpq $0, %r11
    cmovg %r11, %r12
    movq %r12, (%rsi, %r8, 8)
    incq %r8
    cmpq %r8, %rdi
    jg .totalCalc
    ret

.summer:
    movq (%rsi, %r8, 8), %r12
    addq %r12, %r9
    movq %r9, (%rsi, %r8, 8)
    incq %r8
    cmpq %r8, %rdi
    jg .summer
    ret
