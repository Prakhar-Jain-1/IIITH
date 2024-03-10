.global	onlyOnce
.text

onlyOnce:
	movq (%rdi), %rax
	leaq 4(%rdi), %rdi
	imulq $2, %rsi
	jmp .loop
	ret


.loop:
	xorq (%rdi), %rax
	leaq 4(%rdi), %rdi
	decq %rsi
	cmpq $0, %rsi
	jg .loop
