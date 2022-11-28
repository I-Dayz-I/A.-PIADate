class Symbol(metaclass=ABCMeta):
    def __init__(self, name: str) -> None:
        self.name = name
        #self.ast = None

    def is_terminal(self) -> bool:
        return isinstance(self, Terminal)

    def __repr__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.name)

    # def ast(self):
    #     if self.is_terminal:
    #         return self
    #     return self.ast

    @abstractmethod
    def copy(self):
        pass
