import platform
from parse import *
# generate assembly
import platform

class CodeGenerator:
    def __init__(self, parse_result):
        self.parse_result = parse_result
        self.generated_code = ""

    def generate(self):
        # Check for processor architecture
        if platform.processor() == 'arm':
            return self.generate_arm()
        else:
            return self.generate_x64()

    def generate_arm(self):
        self.generated_code += ".text\n"
        for function_name, statement in self.parse_result:
            self.generated_code += f".globl _{function_name}\n"
            self.generated_code += f"_{function_name}:\n"
            if isinstance(statement, int):
                self.generated_code += f"mov w0, #{statement}\nret\n"
        return self.generated_code

    def generate_x64(self):
        self.generated_code += ".text\n"
        for function_name, expression in self.parse_result:
            self.generated_code += f".globl _{function_name}\n"
            self.generated_code += f"_{function_name}:\n"
            self.generated_code += "  movq $0, %eax\n"
        

# Example AST
ast = [('main', '1 + 2 * 3 - 4 / 2')]

# Create code generator instance
generator = CodeGenerator(ast)

# Generate assembly code
assembly_code = generator.generate()
print(assembly_code)