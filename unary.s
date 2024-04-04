.text
.globl _main
_main:
  mov $14, %eax
  addl $2, %eax
  imul $5, %eax
  ret