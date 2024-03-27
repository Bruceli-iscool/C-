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
        if self.currentToken == "int":
            self.advance()  
            if self.currentToken.isidentifier():
                function_name = self.currentToken
                self.advance()  
                if self.currentToken == "(":
                    self.advance()  
                    if self.currentToken == "void":
                        self.advance() 
                        if self.currentToken == ")":
                            self.advance() 
                            if self.currentToken == "{":
                                self.advance()  
                                statement = self.statement()
                                if self.currentToken == "}":
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
        if self.currentToken == "return":
            self.advance()
            expression = self.exp()
            if self.currentToken == ";":
                self.advance()
                return expression
            else:
                print("C-: SyntaxError: Expected ';'")

    def exp(self):
        if self.currentToken.isdigit():
            exp_value = int(self.currentToken)
            self.advance() 
            return exp_value
        else:
            print("C-:SyntaxError: Expected value")

parse = Parser(['int', 'sum', '(', 'void', ')', '{', 'return', '10', ';', '}'])
parse.parse()