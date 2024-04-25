.text
.globl main
main:
  movl $14, %eax
  movl $7, -4(%rbp)
  cdq
  idivl -4(%rbp)
  ret