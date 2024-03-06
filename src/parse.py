import lexer


class Parser:
    """Parser for C-"""
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def parse(self):
        return self.parseFunc()
    # change error handling
    def parseFunc(self):
        """Parse functions"""
        if self.matchToken("INT_KEYWORD"):
            self.index += 1
            identifier = self.parseIdentifier()
            if self.matchToken("OPEN_PAREN") and self.matchToken("CLOSED_PAREN") and self.matchToken("VOID_KEYWORD") or self.matchToken("OPEN_PAREN") and self.matchToken("CLOSED_PAREN"):
                self.index += 3
                if self.matchToken("OPEN_BRACE"):
                    self.index += 1
                    statement = self.parseStatement()
                    if self.matchToken("CLOSE_BRACE"):
                        return f"int {identifier}(void)" + "{" + f"\n{statement}" +"}"       
                    else:
                        raise ValueError("c-: Expexted closing '}'")
                else:
                    raise ValueError("c-: Unexpected '}'")
            else:
                raise ValueError("c-: Expected '()'")
        else:
            raise ValueError("c-: Expected function type")
    
    def parseStatement(self):
        """Parse Statements"""
        if self.matchToken("RETURN_KEYWORD"):
            self.index += 1
            exp = self.parseExpression()
            if self.matchToken("SEMICOLON"):
                return f"return {exp};"
            else:
                raise ValueError("c-: Expected ';'")
        
    def parseExpression(self):
        return self.parseInt()
    
    def parseIdentifier(self):
        if self.matchToken("IDENTIFIER"):
            return self.tokens[self.index][1]
        else:
            raise ValueError("c-: Expected an identifier")
        
    def parseInt(self):
        if self.match_token("INT_CONSTANT"):
            return self.tokens[self.index][1]
        else:
            raise ValueError("c-: Expected an integer constant")
        
    def matchToken(self, expected_type):
        return self.index < len(self.tokens) and self.tokens[self.index][0] == expected_type