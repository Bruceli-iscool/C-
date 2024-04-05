.text
.globl _main
_main:
  movl $1, %eax
  addl $1, %eax
  subl $2, %eax
  movl $2, -4(%rbp)
  cdq
  idivl -4(%rbp)
  ret
