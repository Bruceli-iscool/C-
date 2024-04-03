.text
.globl main
main:
  movq $1, %rax
  pushq $1
  popq %rbx
  popq %rax
  addq %rbx, %rax
  pushq %rax
  pushq $2
  popq %rbx
  popq %rax
  imulq %rbx, %rax
  pushq %rax
  pushq $3
  popq %rbx
  popq %rax
  subq %rbx, %rax
  pushq %rax
  pushq $4
  popq %rbx
  popq %rax
  cqo
  idivq %rbx
  pushq %rax
  pushq $2
  popq %rax
  ret