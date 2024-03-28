import platform

# generate assembly
class CodeGenerator:
    def __init__(self, parse_result):
        self.parse_result = parse_result
        self.generated_code = ""
        self.architecture = platform.architecture()[0]

    def generate(self):
            return self.generate_x64()



    def generate_arm(self):
        self.generated_code += ".text\n"
        for function_name, statement in self.parse_result:
            self.generated_code += f".globl {function_name}\n"
            self.generated_code += f"{function_name}:\n"
            self.generated_code += self.generate_statement_arm(statement)
        return self.generated_code

    def generate_x64(self):
        self.generated_code += ".text\n"
        for function_name, statement in self.parse_result:
            self.generated_code += f".globl {function_name}\n"
            self.generated_code += f"{function_name}:\n"
            self.generated_code += self.generate_statement_x64(statement)
        return self.generated_code

    def generate_statement_arm(self, statement):
        if isinstance(statement, int):
            return f"    mov r0, #{statement}\n    bx lr\n"
        else:
            return ""

    def generate_statement_x64(self, statement):
        if isinstance(statement, int):
            return f"    movl, {statement}, %eax\n    ret\n"
        else:
            return ""

parsed_result = [('main', 42)]
generator = CodeGenerator(parsed_result)
generated_code = generator.generate()
print(generated_code)