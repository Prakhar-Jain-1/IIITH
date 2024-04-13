.global baseball
.text

baseball:
    xorq %r8, %r8       # array passer (i)
    xorq %r9, %r9       # count

    cmpq %rsi, %r8
    jl .looper
.looper:
    movsbq (%rdi, %r8, 1), %rdx
    incq %r8    
    cmpq $67, %rdx
    je .C
    cmpq $68, %rdx
    je .D
    cmpq $43, %rdx
    je .plus

    jmp .digit

.C:
    popq %r10
    decq %r9
    cmpq %rsi, %r8
    jl .looper
    jmp .exit

.D:
    popq %r10
    movq %r10, %r11
    addq %r10, %r11
    pushq %r10
    pushq %r11
    incq %r9
    cmpq %rsi, %r8
    jl .looper
    jmp .exit

.plus:
    popq %r10
    popq %r11
    movq %r10, %r12
    addq %r11, %r12
    pushq %r11
    pushq %r10
    pushq %r12
    incq %r9
    cmpq %rsi,%r8
    jl .looper
    jmp .exit

.digit:
    subq $48, %rdx
    pushq %rdx
    incq %r9
    cmpq %rsi,%r8
    jl .looper
    jmp .exit

.exit:
    xorq %rax,%rax
    cmpq $0, %r9
    jg .exit_loop

.exit_loop:
    popq %r10
    addq %r10,%rax
    decq %r9
    cmpq $0, %r9
    jg .exit_loop
    ret
