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
            self.advance()  # consume "int"
            if self.currentToken[0] == "IDENTIFIER":
                function_name = self.currentToken[1]
                self.advance()  # consume identifier
                if self.currentToken[0] == "LPAREN":
                    self.advance()  # consume "("
                    if self.currentToken[0] == "VOID":
                        self.advance()  # consume "void"
                        if self.currentToken[0] == "RPAREN":
                            self.advance()  # consume ")"
                            if self.currentToken[0] == "LCURLY":
                                self.advance()  # consume "{"
                                statement = self.statement()
                                if self.currentToken[0] == "RCURLY":
                                    return (function_name, statement)
                                # error handling
                                else:
                                    print("C-: SyntaxError: Expected closing '}'")
                            else:
                                print("C-: SyntaxError: Expected '{'")
                        else:
                            print("C-: SyntaxError: Expected closing ')'")
                    # skip void
                    else:
                        self.advance()
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
            if self.currentToken == "SEMICOLON":
                self.advance()
                return expression
            else:
                print("C-: SyntaxError: Expected ';'")

    def exp(self):
        if self.currentToken[0] == "CONSTANT":
            exp_value = int(self.currentToken)
            self.advance() 
            return exp_value
        else:
            print("C-:SyntaxError: Expected value")

