def generate_x64_assembly(ast):
    assembly_code = ""
    for function_name, expression in ast:
        assembly_code += f"{function_name}:\n"
        assembly_code += "  mov rax, 0\n"
        terms = expression.split()
        for term in terms:
            if term.isdigit():
                assembly_code += f"  push {term}\n"
            elif term == '+':
                assembly_code += "  pop rbx\n"
                assembly_code += "  pop rax\n"
                assembly_code += "  add rax, rbx\n"
                assembly_code += "  push rax\n"
            elif term == '-':
                assembly_code += "  pop rbx\n"
                assembly_code += "  pop rax\n"
                assembly_code += "  sub rax, rbx\n"
                assembly_code += "  push rax\n"
            elif term == '*':
                assembly_code += "  pop rbx\n"
                assembly_code += "  pop rax\n"
                assembly_code += "  imul rax, rbx\n"
                assembly_code += "  push rax\n"
            elif term == '/':
                assembly_code += "  pop rbx\n"
                assembly_code += "  pop rax\n"
                assembly_code += "  cqo\n"
                assembly_code += "  idiv rbx\n"
                assembly_code += "  push rax\n"
        assembly_code += "  pop rax\n"
        assembly_code += "  ret\n"
    return assembly_code

# Example AST
ast = [('main', '1 + 2 * 3 - 4 / 2')]

# Generate x64 assembly code
x64_assembly = generate_x64_assembly(ast)
print(x64_assembly)