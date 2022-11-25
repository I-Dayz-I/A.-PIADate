from typing import Dict, List, Tuple, Set

class Component:
    def __init__(self,Name) -> None:
        self.name =Name
        
    def isTerminal(self) -> bool:
        return isinstance(self, Terminal)

class Terminal(Component):
    def __init__(self, Name, Type):
        self.name = Name
        self.type = Type


class Production:

    def __init__(self, head ,Components:list):
        self.components = Components
        self.head = head
        self.pos = 0


class NonTerminal(Component):
    def __init__(self, Name, Productions):
        self.name = Name
        self.productions = Productions

    def __iadd__(self, prod: Production):
        self.add(prod)
        return self


class Grammar:
    def __init__(self, nonTList, Head):
        self.nonTList = nonTList
        self.head = Head 
        
    def get_productions(self) -> List[Production]:
        prods = []
        for non_term in self.nonTList:
            self.update_pos(non_term.productions, prods)
            prods.extend(non_term.productions)
        return prods
    
    def update_pos(self, productions, prods_l):
        pos = len(prods_l)
        for prod in productions:
            prod.pos = pos
            pos += 1
        
