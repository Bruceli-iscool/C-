import re

"""Lexer for C-"""

# tokens
TOKENS = [
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),  
    ('CONSTANT', r'\d+(\.\d+)?'),
    ('KEYWORD', r'(int|float|char|void)'),
    ('VOID', r'void'), 
    ('RETURN', r'return'),  
    ('OPEN_PAREN', r'\('),  
    ('CLOSE_PAREN', r'\)'),  
    ('OPEN_BRACE', r'\{'),  
    ('CLOSE_BRACE', r'\}'),  
    ('SEMICOLON', r';')
]

def tokenize(userinput):
    tokens = []
    if userinput == '\s':
        pass
    else:
        for token_type, pattern in TOKENS:
            matches = re.findall(pattern, userinput)
            for match in matches:
                tokens.append((token_type, match))
        return tokens

filename = input('>')
with open(filename) as file:
    for line in file:
        print(tokenize(line))