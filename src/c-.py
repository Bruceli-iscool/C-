import sys
from lexer import *
from parse import Parser
from compile import CodeGenerator

# main file
def compile(file, out):
    with open(file, 'r') as files:
        rawInput = ""
        for line in files:
            rawInput = rawInput+line
        lexer = Lexer(rawInput)
        token = lexer.lex()
        tokens = list(token)
        print(tokens)
        parse = Parser(tokens)
        result = parse.parse()
        generator = CodeGenerator(result)
        generated_code = generator.generate()
        print(generated_code)
        sys.exit()
    