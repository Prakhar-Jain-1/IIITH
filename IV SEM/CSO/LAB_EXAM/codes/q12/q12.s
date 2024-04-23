.global spNumber
.text

spNumber:
    movq %rdi, %rax
    movq $0,%r9
    movq $10, %r10
    jmp .compute

.compute:
    cqto
    divq %r10
    movq %rdx, %r8
    movq $1, %r11
    cmpq $0, %rdx
    jg .fact
    addq $1,%r9
    cmpq $0, %rax
    jg .compute
    
.fact:
    imulq %r8,%r11
    decq %r8
    cmpq $0, %r8
    jg .fact
    addq %r11, %r9
    cmpq %r9, %rdi
    jl .false
    cmpq $0, %rax
    jg .compute
    cmpq %r9, %rdi
    je .true
    jmp .false
.true:
    movq $1, %rax
    ret
.false:
    movq $0, %rax
    ret

