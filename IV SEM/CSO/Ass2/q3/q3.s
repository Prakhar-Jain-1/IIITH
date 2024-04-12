.global Postfix
.text

Postfix: 
	movq $0, %r8
	movsbq (%rdi, %r8, 1), %rax
	subq $48, %rax
	addq $2, %r8
	call .loop
	ret

.loop:
	movsbq (%rdi, %r8, 1), %r10
	addq $2, %r8
	movsbq (%rdi, %r8, 1), %rdx 

	cmpq $42, %rdx
	je .mult
	
	cmpq $43, %rdx
	je .add
	
	cmpq $47, %rdx
	je .divide
	
	cmpq $45, %rdx
	je .sub


	ret

.add:
	subq $48, %r10
	addq %r10, %rax
	# pushq %r10
	
	addq $2, %r8
	cmpq %rsi, %r8
	jl .loop

	ret

.sub:
	subq $48, %r10
	subq %r10, %rax
	
	addq $2, %r8
	cmpq %rsi, %r8
	jl .loop

	ret

.mult:

	subq $48, %r10

	imulq %r10, %rax
	
	addq $2, %r8
	cmpq %rsi, %r8
	jl .loop

	ret

.divide:
	subq $48, %r10
	cqto
	idivq %r10

	addq $2, %r8
	cmpq %rsi, %r8
	jl .loop

	ret
