import tokens 




    
    
class Compenent:
    
    def __init__(self, Name) -> None:
        
        self.name = Name
        
        
        pass
    
    def isTerminal():
        
        return None
        
    
    
class Terminal(Compenent):
    
    def __init__(self, Name: str, TokenType : tokens.TokenType,value = None) -> None:
        
        self.type = TokenType
        self.name = Name
        self.vale  = value
        
        pass
    
        def isTerminal() -> bool:
            return True
        
        
        

class NonTerminal(Compenent):
    
    def __init__(self, Name: str,ProductionList: list) -> None:
        self.productionList = ProductionList
        self.name = Name
        
        
        
    def isTerminal() -> bool:
        return False
    


class Production:
    
    def __init__(self, Head:NonTerminal, ComponentsList: list ) -> None:
        
        self.head = Head
        self.components = ComponentsList
        pass
    
    


    
    

    
