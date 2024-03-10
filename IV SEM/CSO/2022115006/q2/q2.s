.global Rotate
.text

Rotate:
	movq $1, %r8
	movq (%rdi), %rbx
	jmp .loop

.loop:
	call .swap
	cmpq %rsi, %r8
	jnge .loop
	movq %rbx, -4(%rdi,%r8,4)
	ret

.swap:
	movq (%rdi,%r8,4) ,%rdx
	movq %rdx ,-4(%rdi,%r8,4)
	incq %r8
	ret
