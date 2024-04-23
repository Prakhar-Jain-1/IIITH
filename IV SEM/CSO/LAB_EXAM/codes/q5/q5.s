.global rearrange
.text

rearrange:
    xorq %r9, %r9       # one count
    xorq %rdx, %rdx     # i
    movq $0, %r8
    movq $1, %r11
    jmp .loop

.loop:
    movq (%rsi, %rdx, 8), %rax
    addq %rax, %r9
    incq %rdx
    cmpq %rdi,%rdx
    jl .loop
    subq %r9, %rdx
    xorq %r10, %r10
    cmpq %rdx, %r8
    jne .zeroAdder
    ret

.zeroAdder:
    movq $0, (%rsi, %r10, 8)
    decq %rdx
    incq %r10
    cmpq %rdx, %r8
    jne .zeroAdder
    cmpq %r9, %r8
    jne .oneAdder
    ret

.oneAdder:
    movq $1, (%rsi, %r10, 8)
    decq %r9
    incq %r10
    cmpq %r9, %r8
    jne .oneAdder
    ret


