.global binarySearch
.text


binarySearch:
    movq $0, %r8        # i
    movq $0, %r9        # l
    movq $31, %r10      # r
    # movq (%rsi), %r11   # *idx
    movq %rdx, %rcx     # target
    
    jmp .loop

.loop:
    incq %r8
    movq %r9, %rax
    addq %r10, %rax
    movq $2, %r14
    cqto
    idivq %r14
    movslq (%rdi, %rax, 4), %r12
    cmpq %rcx, %r12
    je .exit
    cmpq %rcx, %r12
    jl .less
    cmpq %rcx, %r12
    jg .great
    
.exit:
    movq %rax, (%rsi)
    movq %r8, %rax
    ret
.less:
    incq %rax
    movq %rax, %r9
    cmpq %r9, %r10
    jge .loop
    movq %r8,%rax
    ret
.great:
    decq %rax
    movq %rax, %r10
    cmpq %r9, %r10
    jge .loop
    movq %r8,%rax
    ret
