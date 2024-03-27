import re

class Lexer:
    def __init__(self, text):
        self.text = text
        self.tokens = []
        self.current_token = None
        self.token_index = -1
        self.tokenize()

    def tokenize(self):
        self.tokens = re.findall(r'\bint\b|\bvoid\b|\breturn\b|\b\d+\b|\w+|[()\{\};]', self.text)

    def advance(self):
        self.token_index += 1
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
        else:
            self.current_token = None

    def get_next_token(self):
        self.advance()
        return self.current_token
text = "int sum() { return 10; }"
lexer = Lexer(text)
tokens = lexer.tokens
print(tokens)