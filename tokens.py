import enum
from comp_globals import TokenType

class Token():
    def __init__(self,tokenType,line,column,value=None):
        self.value=value
        self.tokenType=tokenType
        self.line=line
        self.lexeme = value
        self.column=column
        if tokenType == TokenType.tokID:
            self.name = 'identifier'
            self.value = 'identifier'
        
        if tokenType == TokenType.tokNumber:
            self.name = 'numeric'
            self.value = 'numeric'
    
    def __str__(self) -> str:
        return str(self.tokenType)
    
    def __repr__(self):
        return self.__str__()
    
    
