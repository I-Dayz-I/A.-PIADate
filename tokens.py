import enum


class Token():
    def __init__(self,tokenType,line,column,value=None):
        self.value=value
        self.tokenType=tokenType
        self.line=line
        self.lexeme = value
        self.column=column
    
    def __str__(self) -> str:
        return str(self.tokenType)
    
    def __repr__(self):
        return self.__str__()
    
    
