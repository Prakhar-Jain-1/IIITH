.global oddBit
.text

oddBit:
    movq %rdi, %rax
    movq %rdi, %rdx
    movq $2, %r9
    xorq %r8, %r8
    cmpq $0, %rax
    jne .calc

.calc:
    cqto
    idivq %r9
    addq %rdx, %r8
    movq %rax, %rdx
    cmpq $0, %rax
    jne .calc
    jmp .exit
    ret

.exit:
    # ret
    movq %r8, %rdx
    movq %r8, %rax
    cqto
    idivq %r9
    movq %rdx, %rax
    ret
