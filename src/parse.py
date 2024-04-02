# Parser for C-
class Parser:
    def __init__(self, tokens):
        # make tokens an object
        self.tokens = tokens
        self.currentToken = None
        self.index = -1
        self.advance()

    def advance(self):
        self.index += 1
        if self.index < len(self.tokens):
            # find current token
            self.currentToken = self.tokens[self.index]
        else:
            self.currentToken = None

    def parse(self):
        return self.program()
    
    def program(self):
        return self.function()
    
    # Handle functions (for now the main function)
    def function(self):
        if self.currentToken[0] == "INT":
            self.advance()  
            if self.currentToken[0] == "IDENTIFIER":
                function_name = self.currentToken[1]
                self.advance()  
                if self.currentToken[0] == "OPEN_PAREN":
                    self.advance()  
                    if self.currentToken[0] == "VOID":
                        self.advance()  # skip void
                        if self.currentToken[0] == "CLOSED_PAREN":
                                self.advance()  
                                if self.currentToken[0] == "OPEN_BRACE":
                                    self.advance()  
                                    statement = self.statement()
                                    if self.currentToken[0] == "CLOSED_BRACE":
                                        return [(function_name, statement)]
                                    # error handling
                                    else:
                                        print("C-: SyntaxError: Expected closing '}'")
                                else:
                                    print("C-: SyntaxError: Expected '{'")
                        else:
                            print("C-: SyntaxError: Expected closing ')'")
                    

                else:
                    print("C-: SyntaxError: Expected '('")
            else:
                print("C-: SyntaxError: Expected Identifier after int")
        else:
            print("C-: SyntaxError: Expected 'int'")
    def statement(self):
        if self.currentToken[0] == "RETURN":
            self.advance()
            expression = self.exp()
            if self.currentToken[0] == "SEMICOLON":
                self.advance()
                return expression
            else:
                print("C-: SyntaxError: Expected ';'")

    def exp(self):
        if self.currentToken[0] == "CONSTANT":
            exp_value = int(self.currentToken[1])
            self.advance()
            if self.currentToken[0] in ["ADD", "HYPEN", "TIMES", "DIVIDE"]:
                    operator = self.currentToken[1]
                    self.advance()
                    operand = exp_value
                    try:
                        equation = eval(str(operand) + str(operator) + str(self.exp()))
                    except ZeroDivisionError:
                        print("C-: DivisionError: Cannot divide by 0.")
                    return equation
            else:
                return exp_value
            
        elif self.currentToken[0] in ["HYPEN", "TIDLE"]:
            self.operator = self.currentToken[1]
            self.advance()
            if self.currentToken[0] == "OPEN_PAREN":
                self.advance()
                statement =  eval(str(self.operator) + str(self.exp()))
                if self.currentToken[0] == "CLOSED_PAREN":
                    self.advance()
                    return statement
                else:
                    print("C-: SyntaxError: Expected ')'")
            else:
                operand = self.exp()
                num = str(self.operator) + str(operand)
                num = eval(num)
                return num
        elif self.currentToken[0] == "OPEN_PAREN":
            self.advance()
            expression = self.exp()
            if self.currentToken[0] == "CLOSED_PAREN":
                self.advance()
                return expression
            else:
                print("C-: SyntaxError: Expected ')'")
        else:
            print("C-: Expected value.")

#tokens = [('INT', 'int'), ('IDENTIFIER', 'main'), ('OPEN_PAREN', '('), ('VOID', 'void'), ('CLOSED_PAREN', ')'), ('OPEN_BRACE', '{'), ('RETURN', 'return'), ('TIDLE', '~'), ('OPEN_PAREN', '('), ('HYPEN', '-'), ('CONSTANT', '2'), ('CLOSED_PAREN', ')'), ('SEMICOLON', ';'), ('CLOSED_BRACE', '}')]

# test code
#parser = Parser(tokens);result = parser.parse();print(result)
tokens2 = [
    ("INT", "int"),
    ("IDENTIFIER", "main"),
    ("OPEN_PAREN", "("),
    ("VOID", "void"),
    ("CLOSED_PAREN", ")"),
    ("OPEN_BRACE", "{"),
    ("RETURN", "return"),
    ("CONSTANT", "4"),
    ("ADD", "+"),
    ("CONSTANT", "3"),
    ("DIVIDE", "/"),
    ("CONSTANT", "3"),
    ("SEMICOLON", ";"),
    ("CLOSED_BRACE", "}")
]

parser = Parser(tokens2);result = parser.parse();print(result)