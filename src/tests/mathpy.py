import re

# Define operator precedence for arithmetic expressions
precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
}

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.currentToken = None
        self.index = -1
        self.advance()

    def advance(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.currentToken = self.tokens[self.index]
        else:
            self.currentToken = None

    def parse(self):
        return self.program()

    def program(self):
        return self.function()

    def function(self):
        if self.currentToken[0] == "INT":
            self.advance()
            if self.currentToken[0] == "IDENTIFIER":
                function_name = self.currentToken[1]
                self.advance()
                if self.currentToken[0] == "OPEN_PAREN":
                    self.advance()
                    if self.currentToken[0] == "VOID":
                        self.advance()
                        if self.currentToken[0] == "CLOSED_PAREN":
                            self.advance()
                            if self.currentToken[0] == "OPEN_BRACE":
                                self.advance()
                                statement = self.statement()
                                if self.currentToken[0] == "CLOSED_BRACE":
                                    self.advance()
                                    return [(function_name, statement)]
                                else:
                                    print("C-: SyntaxError: Expected closing '}' after function body")
                            else:
                                print("C-: SyntaxError: Expected '{' after function parameters")
                        else:
                            print("C-: SyntaxError: Expected closing ')' after function parameters")
                    else:
                        print("C-: SyntaxError: Expected 'void' as function return type")
                else:
                    print("C-: SyntaxError: Expected '(' after function name")
            else:
                print("C-: SyntaxError: Expected Identifier after int")
        else:
            print("C-: SyntaxError: Expected 'int' for function declaration")

    def statement(self):
        if self.currentToken[0] == "RETURN":
            self.advance()
            expression = self.exp()
            if self.currentToken[0] == "SEMICOLON":
                self.advance()
                return expression
            else:
                print("C-: SyntaxError: Expected ';' after return statement")

    def exp(self):
        if self.currentToken[0] == "CONSTANT":
            return int(self.currentToken[1])
        elif self.currentToken[0] == "OPEN_PAREN":
            self.advance()
            expression_value = self.exp()
            if self.currentToken[0] == "CLOSED_PAREN":
                self.advance()
                return expression_value
            else:
                print("C-: SyntaxError: Expected ')'")
        else:
            return self.parse_arithmetic_expression()

    def parse_arithmetic_expression(self):
        expression = ""
        while self.currentToken and self.currentToken[0] not in ["SEMICOLON", "CLOSED_PAREN"]:
            expression += self.currentToken[1]
            self.advance()
        tokens = tokenize(expression)
        result = evaluate_arithmetic_expression(tokens)
        return result

def tokenize(expression):
    tokens = re.findall(r'\d+|\S', expression)
    return tokens

def evaluate_arithmetic_expression(tokens):
    output_queue = []
    operator_stack = []

    for token in tokens:
        if token.isdigit():
            output_queue.append(token)
        elif token in precedence:
            while (operator_stack and
                   operator_stack[-1] != '(' and
                   precedence[operator_stack[-1]] >= precedence[token]):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            operator_stack.pop()

    while operator_stack:
        output_queue.append(operator_stack.pop())

    stack = []
    for token in output_queue:
        if token.isdigit():
            stack.append(int(token))
        elif token in precedence:
            op2 = stack.pop()
            op1 = stack.pop()
            if token == '+':
                stack.append(op1 + op2)
            elif token == '-':
                stack.append(op1 - op2)
            elif token == '*':
                stack.append(op1 * op2)
            elif token == '/':
                stack.append(op1 / op2)

    return stack[0] if stack else None

# Test tokens
tokens = [('INT', 'int'), ('IDENTIFIER', 'main'), ('OPEN_PAREN', '('), ('VOID', 'void'), ('CLOSED_PAREN', ')'), ('OPEN_BRACE', '{'), ('RETURN', 'return'), ('TIDLE', '~'), ('OPEN_PAREN', '('), ('HYPEN', '-'), ('CONSTANT', '2'), ('CLOSED_PAREN', ')'), ('SEMICOLON', ';'), ('CLOSED_BRACE', '}')]

# Test code
parser = Parser(tokens)
result = parser.parse()
print(result)

