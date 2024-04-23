.global gcd
.text

gcd:
    movq %rdi,%rax
    movq $0, %r8
    jmp .looper

.looper:
    cqto
    idivq %rsi
    movq %rsi, %rax
    movq %rdx, %rsi
    cmpq %rsi, %r8
    jl .looper
    ret
    
