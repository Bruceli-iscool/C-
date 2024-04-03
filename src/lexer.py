import re
import sys

# Define token types using regular expressions
TOKEN_TYPES = [
    ('DOUBLE_HYPEN', r'--'),
    ('CONSTANT', r'\d+'),
    ('TIDLE', r'~'),
    ('ADD', r'\+'),
    ('TIMES', r'\*'),
    ('DIVIDE', r'/'),
    ('HYPEN', r'-'),
    ('AND', r'\&&'),
    ('OR', r'\|\|'),
    ('EQUAL', r'\=='),
    ('NOT EQUAL', r'\!='),
    ("LESS THAN", r'\<'),
    ("LESS THAN OR EQUAL", r'\<='),
    ("GREATER THAN", r'\>'),
    ("GREATER THAN OR EQUAL", r'\>='),
    ('INT', r'\bint\b(?![a-zA-Z0-9_])'),
    ('VOID', r'\bvoid\b(?![a-zA-Z0-9_])'),
    ('RETURN', r'\breturn\b(?![a-zA-Z0-9_])'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('OPEN_PAREN', r'\('),
    ('CLOSED_PAREN', r'\)'),
    ('OPEN_BRACE', r'\{'),
    ('CLOSED_BRACE', r'\}'),
    ('SEMICOLON', r';')
]


class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0

    def lex(self):
        while self.position < len(self.source_code):
            match = None
            for token_type in TOKEN_TYPES:
                token_name, pattern = token_type
                regex = re.compile(pattern)
                match = regex.match(self.source_code, self.position)
                if match:
                    value = match.group(0)
                    yield (token_name, value)
                    self.position = match.end()
                    break
            if not match:
                    # Skip whitespace characters
                    if self.source_code[self.position].isspace():
                        self.position += 1
                        continue
                    else:
                        print(f"C-:Invalid token: {self.source_code[self.position]}")
                        sys.exit()
