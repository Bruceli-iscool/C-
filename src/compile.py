import platform
from parse import *
# generate assembly
class CodeGenerator:
    def __init__(self, parse_result):
        self.parse_result = parse_result
        self.generated_code = ""

    def generate(self):
            # check for processor
            if platform.processor() == 'i386':
                return self.generate_x64()
            elif platform.processor() == 'arm':
                return self.generate_arm()
            else:
                pass



    def generate_arm(self):
        self.generated_code += ".text\n"
        for self.function_name, statement in self.parse_result:
            self.generated_code += f".globl _{self.self.function_name}\n"
            self.generated_code += f"_{self.self.function_name}:\n"
            if '-' in statement:
                self.generated_code += self.generate_statement_arm(statement, '-')
            else:
                self.generated_code += self.generate_statement_arm(statement)
        return self.generated_code

    def generate_x64(self):
        self.generated_code += ".text\n"
        for self.function_name, statement in self.parse_result:
            self.generated_code += f".globl _{self.function_name}\n"
            self.generated_code += f"_{self.function_name}:\n"
            self.generated_code += self.generate_statement_x64(statement)
        return self.generated_code

    def generate_statement_arm(self, statement):
        if isinstance(statement, int):
            return f"    	.cfi_startproc\n; %bb.0:\nmov	w0, #{statement}\nret\n.cfi_endproc"
        else:
            return ""

    def generate_statement_x64(self, statement):
        if isinstance(statement, int):
            return f"	pushq	%rbp\nmovq	%rsp, %rbp\nmovl ${statement}, %eax\npopq	%rbp\nretq"
        elif isinstance(statement, str):
            operator = statement[1]
            if operator == "+":
                return f"movl ${statement[0]}, %eax\nmovl ax, ${statement[2]}\nadd %eax, ax "
        else:
            return ""
