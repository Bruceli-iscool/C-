import lexer


class Parser:
    """Parser for C-"""
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def parse(self):
        return self.parseFunc()
    
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
