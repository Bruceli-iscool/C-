.text
.globl main
main:
        pushq   %rbp
movq    %rsp, %rbp
movl $15, %eax
popq    %rbp
retq