from lexer import Lexer
from parse import Parser
from compile import CodeGenerator

# main file
def compile(file, out):
    with open(file, 'r') as files:
        rawInput = ""
        for line in files:
            rawInput = rawInput+line
        lexer = Lexer(rawInput)
        tokens = lexer.tokens
        parse = Parser(tokens)
        result = parse.parse()
        print(result)
        generator = CodeGenerator(result)
        generated_code = generator.generate()
        print(generated_code)
compile("/Users/keli/Documents/GitHub/gh/C-/.tests/return_2.c", 234)