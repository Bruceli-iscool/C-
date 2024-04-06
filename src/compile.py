# generate assembly
import platform


class CodeGenerator:
    def __init__(self, parse_result):
        self.parse_result = parse_result
        self.generated_code = ""

    def generate(self):
        # Check for processor architecture
        if platform.processor() == "arm":
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
        # add negation
        for function_name, expression in self.parse_result:
            self.generated_code += f".globl {function_name}\n"
            self.generated_code += f"{function_name}:\n"
            num = "0"
            expression = expression.replace(" ", "")
            for value in expression:
                if value.isdigit():
                    num += str(value)
                    expression = expression.lstrip(value)
                    continue
                else:
                    break
            num = int(num)
            self.generated_code += f"  movl ${num}, %eax\n"
            num = "0"
            # Parse and generate assembly for the expression
            while len(expression) > 0:
                current = expression[0]
                expression = expression[1:]
                if current == "+":
                    for value in expression:
                        if value.isdigit():
                            num += str(value)
                            expression = expression.lstrip(value)
                            continue
                        else:
                            break

                    self.generated_code += f"  addl ${int(num)}, %eax\n"
                    num = ""
                    continue
                elif current == "-":
                    for value in expression:
                        if value.isdigit():
                            num += str(value)
                            expression = expression.lstrip(value)
                            continue
                        else:
                            break
                    self.generated_code += f"  subl ${int(num)}, %eax\n"
                    num = ""
                    continue
                elif current == "*":
                    for value in expression:
                        if value.isdigit():
                            num += str(value)
                            expression = expression.lstrip(value)
                            continue
                        else:
                            break
                    self.generated_code += f"  imull ${int(num)}, %eax\n"
                    num = ""
                    continue
                # handling division takes multiple lines
                elif current == "/":
                    for value in expression:
                        if value.isdigit():
                            num += str(value)
                            expression = expression.lstrip(value)
                            continue
                        else:
                            break
                    self.generated_code += (
                        f"  movl ${int(num)}, -4(%rbp)\n  cdq\n  idivl -4(%rbp)\n"
                    )
        self.generated_code += "  ret\n"
        return self.generated_code


ast = [("main", "14/7")]

# Create code generator instance
#generator = CodeGenerator(ast)

# Generate assembly code
#assembly_code = generator.generate()
#print(assembly_code)
