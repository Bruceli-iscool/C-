.text
.globl main
main:
  mov $0, %eax
  mov $1, %ebx
  mov $2, %ebx
  add %ebx, %eax
  mov $5, %ebx
  sub %ebx, %eax
  ret