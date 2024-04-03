import platform
import sys
# generate assembly
class CodeGenerator:
    def __init__(self, parse_result):
        self.parse_result = parse_result
        self.generated_code = ""

    def generate(self):
            # check for processor
            if platform.processor() == 'i386' or platform.processor() == 'Intel64 Family 6 Model 126 Stepping 5, GenuineIntel':
                return self.generate_x64()
            elif platform.processor() == 'arm':
                return self.generate_arm()
            else:
                pass



    def generate_arm(self):
        self.generated_code += ".text\n"
        for function_name, expression in self.parse_result:
            self.generated_code += f".globl _{function_name}\n"
            self.generated_code += f"_{function_name}:\n"
            self.generated_code += self.generate_statement_arm(expression)
        return self.generated_code

    def generate_x64(self):
        self.generated_code += ".text\n"
        for function_name, expression in self.parse_result:
            self.generated_code += f".globl _{function_name}\n"
            self.generated_code += f"_{function_name}:\n"
            self.generated_code += self.generate_statement_x64(expression)
        return self.generated_code
    # handle operators along with statements
    def generate_statement_arm(self, expression):
        if isinstance(expression, int):
            return f"    mov r0, #{expression}\n    bx lr\n"
        elif isinstance(expression, tuple):
            operator = expression[0]
            if operator == '+':
                left_operand_code = self.generate_statement_arm(expression[1])
                right_operand_code = self.generate_statement_arm(expression[2])
                return left_operand_code + right_operand_code + "    add r0, r0, r1\n    bx lr\n"
            elif operator == '-':
                left_operand_code = self.generate_statement_arm(expression[1])
                right_operand_code = self.generate_statement_arm(expression[2])
                return left_operand_code + right_operand_code + "    sub r0, r0, r1\n    bx lr\n"
            elif operator == '*':
                left_operand_code = self.generate_statement_arm(expression[1])
                right_operand_code = self.generate_statement_arm(expression[2])
                return left_operand_code + right_operand_code + "    mul r0, r0, r1\n    bx lr\n"
            elif operator == '/':
                left_operand_code = self.generate_statement_arm(expression[1])
                right_operand_code = self.generate_statement_arm(expression[2])
                return left_operand_code + right_operand_code + "    sdiv r0, r0, r1\n    bx lr\n"
            else:
               print(f"C-: Unsupported operator: {operator}")
               sys.exit()
        else:
            print("C-: Invalid expression format")
            sys.exit()

    def generate_statement_x64(self, expression):
        if isinstance(expression, int):
            return f"    mov eax, {expression}\n    ret\n"
        elif isinstance(expression, str):
            operator = expression[1]
            if operator == '+':
                left_operand_code = self.generate_statement_x64(expression[0])
                right_operand_code = self.generate_statement_x64(expression[2])
                return left_operand_code + right_operand_code + "    add eax, ebx\n    ret\n"
            elif operator == '-':
                left_operand_code = self.generate_statement_x64(expression[0])
                right_operand_code = self.generate_statement_x64(expression[2])
                return left_operand_code + right_operand_code + "    sub eax, ebx\n    ret\n"
            elif operator == '*':
                left_operand_code = self.generate_statement_x64(expression[0])
                right_operand_code = self.generate_statement_x64(expression[2])
                return left_operand_code + right_operand_code + "    imul ebx\n    ret\n"
            elif operator == '/':
                left_operand_code = self.generate_statement_x64(expression[0])
                right_operand_code = self.generate_statement_x64(expression[2])
                return left_operand_code + right_operand_code + "    cdq\n    idiv ebx\n    ret\n"
            else:
                print(f"C-: Unsupported operator: {operator}")
                sys.exit()
        else:
            print("C-: Invalid expression format")
            sys.exit()
# Test case
parse_result = [('main', '5+6')]

# Instantiate the code generator
code_generator = CodeGenerator(parse_result)

# Generate assembly code
assembly_code = code_generator.generate()

# Print the assembly code
print(assembly_code)
