.global sumMinMax
.text

sumMinMax:
    movq $0, %r10
    movslq (%rdi,%r10,4), %r8 # min
    movslq (%rdi,%r10,4), %r9 # max
    jmp .loop

.loop:
    movslq (%rdi,%r10,4), %r11
    cmpq %r11, %r8
    jg .min
    
    cmpq %r11, %r9
    jl .max

    incq %r10
    
    cmpq %rsi, %r10
    jnge .loop
    movq %r8, %rax
    addq %r9, %rax
    ret

.max:
    movq %r11, %r9
    jmp .loop
 
.min:
    movq %r11, %r8
    jmp .loop
