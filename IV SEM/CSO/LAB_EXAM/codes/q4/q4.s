.global isPalindrome
.text

isPalindrome:
    movq %rdi, %rax
    movq $10, %r8
    jmp .stack

.stack:
    cqto
    idivq %r8
    pushq %rdx
    cmpq $0, %rax
    jne .stack
    movq %rdi, %rax
    jmp .poper
.poper:
    cqto
    idivq %r8
    popq %r9
    cmpq %r9, %rdx
    jne .exitFalse
    cmpq $0, %rax
    jne .poper
    movq $1, %rax
    ret
.exitFalse:
    cqto
    idivq %r8
    popq %r9
    cmpq $0, %rax
    jne .exitFalse
    movq $0, %rax
    ret
