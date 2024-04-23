.global array
.text

array:
    movq $1, %r8
    movq $3, %r10
    movq $5, %r11
    cmpq %r8, %rdi
    jge .check
    ret

.check:
    xorq %r9, %r9
    call .3mul
    call .5mul
    call .setval
    movq %r9, -8(%rsi, %r8, 8)
    incq %r8
    cmpq %r8, %rdi
    jge .check
    ret

.3mul:
    movq  %r8, %rdx
    movq  %r8, %rax
    cqto
    idivq %r10
    cmpq $0, %rdx
    je .subtract3
    ret
.5mul:
    movq  %r8, %rdx
    movq  %r8, %rax
    cqto
    idivq %r11
    cmpq $0, %rdx
    je .subtract5
    ret

.subtract3:
    subq $1, %r9
    ret
.subtract5:
    subq $2, %r9
    ret
.setval:
    cmpq $0, %r9
    je .s
    ret
.s:
    movq %r8, %r9
    ret
