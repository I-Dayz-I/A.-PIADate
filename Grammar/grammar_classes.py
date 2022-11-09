
class Terminal:
    def __init__(self, Name, Type):
        self.name = Name
        self.type = Type


class Production:

    def __init__(self, head ,Components):
        self.components = Components
        self.head = head


class NonTerminal:
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