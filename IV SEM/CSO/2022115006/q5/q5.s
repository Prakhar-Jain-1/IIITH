.global productWOele
.text

productWOele:
    cmpq $1, %rsi
    je .exit
    movq %rsi, %r10
    movq $1, %r9
    movq (%rdx), %r11
    movq $1, (%rdx)
    call .floop
    decq %r10
    movq (%rcx,%r10,8), %r11
    movq $1, (%rcx,%r10,8)
    decq %r10
    call .rloop
    movq $0, %r9
    call .calc
    ret

.floop:
    movq -8(%rdx,%r9,8), %r8
    imulq %r11, %r8
    movq (%rdx,%r9,8),%r11
    movq %r8,(%rdx,%r9,8)
    incq %r9
    cmpq %rsi,%r9
    jl .floop
    ret

.rloop:
    movq 8(%rcx,%r10,8), %r8
    imulq %r11, %r8
    movq (%rcx,%r10,8),%r11
    movq %r8,(%rcx,%r10,8)
    decq %r10
    cmpq $0,%r10
    jnl .rloop
    ret

.calc:
    movq (%rdx,%r9,8), %r8
    movq (%rcx,%r9,8), %r10
    imulq %r10, %r8
    movq %r8,(%rdi,%r9,8)
    incq %r9
    cmpq %rsi,%r9
    jl .calc
    ret

.exit:
    movq $1, (%rdi)
    ret
