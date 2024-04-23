.global WeirdRearrange
.text

WeirdRearrange:
    xorq %r8,%r8
    movq $2,%r10
    movq $1, %r9
    call .searcherOP
    addq %r14, %r15
    cmpq $2, %r15
    jne .exit
    xorq %r8,%r8
    movq %rdi, %r11
    decq %r11
    call .bubbleSort
    ret


.searcherOP:
    movq (%rsi, %r8, 8), %rax
    cqto
    idivq %r10
    call .fixer
    incq %r8
    cmpq %r8, %rdi
    jg .searcherOP
    ret

.fixer:
    cmpq $0,%rdx
    cmove %r9, %r14
    cmpq $1, %rdx
    cmove %r9, %r15
    ret

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
    cmpq %r10, %r8
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

.exit:
    ret

