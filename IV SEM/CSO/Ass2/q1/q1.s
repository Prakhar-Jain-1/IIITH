# int maxSubarraySum(long long int arr[], int n, int L, int R) {
#     int maxSum = -1e9;
#     int sumL = 0, sumR = 0, maxTill = 0, maxInd = L-1, i = 0;
#     
#     while (i < L){
#         sumL+=arr[i++];
#     }
#     
#     sumR = sumL, maxTill = sumL;
# 
#     for (int j = i; j < R; j++){
#         sumR += arr[j];
#         if(sumR > maxSum){
#             maxSum = sumR, maxInd = j;
#         }
#     }
#     
#     maxSum = maxTill;
#     
#     for (; i < n; i++) {
#         sumL += (arr[i] - arr[i - L]);
#         sumR-=arr[i - L];
#         maxTill -= arr[i - L];
# 
#         if(i + R - 1 < n) sumR += arr[i + R - 1];
#         
#         if(maxInd < i){ 
#             maxTill += arr[i];
#             maxInd = i;
#         }
#         
#         if(maxTill < sumR){
#             maxTill = sumR;
#             maxInd = min(i + R - 1,n-1);
#         }
#         
#         maxSum = max(maxTill, maxSum);
#         printf("%d\n",maxTill);
#     }
#     return maxSum;
# }


.global maxSubarraySum
.text

maxSubarraySum:
    movq $0, %r8        # i
    movq $0, %r9        # sumL
    movq %rdx, %r12     # maxInd
    decq %r12           # maxInd
    
    call .set_upLoop1

    movq %r9, %r10       # sumR
    movq %r9, %r11       # maxTill
    movq %r8, %r14       # j

    call .bachhao
    movq %r11, %rax
    cmpq %rsi, %r8 
    jl .compute_loop
    ret

.bachhao:
    cmpq %rcx, %r14
    jl .set_upLoop2
    ret

.set_upLoop2:
    movq (%rdi, %r14, 8), %r13
    addq %r13, %r10      # arr[j] + sumR
    call .setUpMax
    incq %r14
    cmpq %rcx, %r14
    jl .set_upLoop2

    ret

.setUpMax:
    cmpq %r10, %r11
    jl .sMax
    ret

.sMax:
    movq %r10, %r11
    movq %r14, %r12
    ret


.set_upLoop1:
    movq (%rdi, %r8, 8), %r13
    addq %r13, %r9      # arr[i] + sumL
    incq %r8
    cmpq %rdx, %r8
    jl .set_upLoop1
    ret


.compute_loop:
    movq %r8, %r15
    subq %rdx, %r15
    movq (%rdi, %r15, 8), %r13
    subq %r13, %r9
    subq %r13, %r10
    subq %r13, %r11
    movq (%rdi, %r8, 8), %r13
    addq %r13, %r9

    call .ifR
    call .ifMaxInd
    call .TR
    call .retSet
    incq %r8
    cmpq %rsi, %r8 
    jl .compute_loop
    ret

.ifR:
    movq %r8, %r15
    addq %rcx, %r15
    decq %r15
    cmpq %rsi, %r15
    jl .setR
    jmp .setMinInd

    ret

.setR:
    movq (%rdi, %r15, 8), %r13
    addq %r13, %r10
    ret
.setMinInd:
    movq %rsi, %r15
    decq %r15
    ret

.ifMaxInd:
    cmpq %r8, %r12
    jl .mi
    ret

.mi:

    addq %r13, %r11
    incq %r12
    ret

.TR:
    cmpq %r10, %r11
    jl .curMaxSet
    ret

.curMaxSet:
    movq %r10, %r11
    movq %r15, %r12
    ret

.retSet:
    cmpq %r11, %rax
    jl .setMax
    ret

.setMax:
    movq %r11, %rax
    ret
