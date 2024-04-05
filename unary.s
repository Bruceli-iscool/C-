.text
.globl _main
_main:
  movl $1, %eax
  addl $1, %eax
  addl $6, %eax
  movl $4, -4(%rbp)
  cdq
  idivl -4(%rbp)
  ret