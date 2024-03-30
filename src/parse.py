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
    
    # Handle fucntions (for now the main function)
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
            return exp_value
        elif self.currentToken[0] in ["HYPEN", "TIDLE"]:
            operator = self.currentToken[0]
            self.advance()
            operand = self.exp()
            return (operator, operand)
        elif self.currentToken[0] == "OPEN_PAREN":
            self.advance()
            expression = self.exp()
            if self.currentToken[0] == "CLOSED_PAREN":
                self.advance()
                return expression
            else:
                print("C-: SyntaxError: Expected ')'")
        else:
            print("C-:SyntaxError: Expected value")
tokens = [
    ("INT", "int"),
    ("IDENTIFIER", "main"),
    ("OPEN_PAREN", "("),
    ("VOID", "void"),
    ("CLOSED_PAREN", ")"),
    ("OPEN_BRACE", "{"),
    ("RETURN", "return"),
    ("HYPEN", "-"),
    ("CONSTANT", "5"),
    ("SEMICOLON", ";"),
    ("CLOSED_BRACE", "}"),
]

parser = Parser(tokens)
result = parser.parse()
print(result)
