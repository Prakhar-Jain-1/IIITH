.global isPalindrome
.text

isPalindrome:
    movq $-1, %r8
    call .len
    movq $1, %rax
    movq $-1, %r9
    call .pCheck
    ret

.len:
    incq %r8
    cmpq $0, (%rdi,%r8,1)
    jne .len
    ret
    
.pCheck:
    decq %r8
    incq %r9

    cmpq %r8, %r9
    jl .k
    ret
    

.k:
    movzbq (%rdi, %r8,1), %r10
    movzbq (%rdi, %r9,1), %r11
    
    cmpq %r10, %r11
    je .pCheck

    cmpq %r10, %r11
    jne .exit

.exit:
    movq $0, %rax
    ret
