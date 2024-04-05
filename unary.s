.text
.globl _main
_main:
  mov $14, %eax
  movl $7, -4(%rbp)
  idivl -4(%rbp)
  ret