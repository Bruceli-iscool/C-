import re

# Define token types using regular expressions
TOKEN_TYPES = [
    ('INT', r'int'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('VOID', r'void'),
    ('LCURLY', r'\{'),
    ('RCURLY', r'\}'),
    ('RETURN', r'return'),
    ('SEMICOLON', r';'),
    ('CONSTANT', r'\d+')
]

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.tokens = []

    def lex(self):
        while self.position < len(self.source_code):
            match = None
            for token_type in TOKEN_TYPES:
                pattern = token_type[1]
                regex = re.compile(pattern)
                match = regex.match(self.source_code, self.position)
                if match:
                    value = match.group(0)
                    self.tokens.append((token_type[0], value))
                    self.position = match.end()
                    break
            if not match:
                raise SyntaxError(f"Invalid token: {self.source_code[self.position]}")
        return ([self.tokens])

