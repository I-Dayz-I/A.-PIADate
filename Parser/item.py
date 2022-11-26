from Grammar.grammar_classes import Production, Component,Terminal


class LR1Item:
    def __init__(self, production: Production, dot_index: int, lookahead: Terminal = None):
        self._repr = ''
        self.production = production
        self.dot_index = dot_index
        self.lookahead = lookahead
        self._repr = f"{self.production.head} -> "
        self._repr += " ".join(str(self.production.symbols[i]) for i in range(self.dot_index))
        self._repr += " . "
        self._repr += " ".join(str(self.production.symbols[i]) for i in range(self.dot_index,len(self.production.symbols)))
        self._repr += f", {self.lookahead}"

    def __repr__(self) -> str:
        return self._repr

    def getCurrentSymbol(self) -> Component:
        if self.dot_index < len(self.production.symbols):
            return self.production.symbols[self.dot_index]
        return None

    def __eq__(self, o):
        if isinstance(o, LR1Item):
            return self._repr == o._repr
        return False

    def __hash__(self):
        return hash(self.__repr__())
