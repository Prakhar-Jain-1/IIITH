.global compute
.text

compute:
    cmpq $1,%rdx
    je .sum
    cmpq $2,%rdx
    je .diff
    cmpq $3,%rdx
    je .divide
    cmpq $4,%rdx
    je .expo
    cmpq $5,%rdx
    je .mod


.sum:
    movq %rsi, %rax
    addq %rdi, %rax
    ret

.diff:
    movq %rdi, %rax
    subq %rsi, %rax
    ret

.divide:
    movq %rdi, %rax
    cqto
    idivq %rsi
    ret

.mod:
    movq %rdi, %rdx
    cqto
    idivq %rsi
    movq %rdx, %rax
    ret

.expo:
    movq $1,%rax
    xorq %r9, %r9
    cmpq %rsi, %r9
    jl .mul
    ret

.mul:
    imulq %rdi, %rax
    incq %r9
    cmpq %rsi, %r9
    jl .mul
    ret
