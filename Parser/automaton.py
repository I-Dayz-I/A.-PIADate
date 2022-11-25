from Grammar.grammar_classes import Grammar, Component, Production, Terminal, NonTerminal
from comp_globals import TokeTypes
from item import LR1Item
from typing import Dict, List, Tuple, Set


class Automata:
    
    def __init__(self,Grammar : Grammar) -> None:
        
        #Extending the grammar with the a initial Symbol
        self.grammar = Grammar
        self.grammar.start = None
        self.extendGrammar()
        
        start = self.grammar.start
        
        #Creating all initial Items with index in 0
        initial_items = {start: [LR1Item(start.productions[0], 0, Terminal('$', '$'))]}
        for non_term in self.grammar.non_terminal_list:
            if (non_term.name == 'S'):
                continue
            initial_items[non_term] = []
            for prod in non_term.productions:
                initial_items[non_term].append(LR1Item(prod, 0))

        
        
        pass
    
    
    
    def extendGrammar(self):
        #Getting the first production of the Grammar
        newProduction = Production(None,[self.grammar.head])
        #Creating the new NonTerminal
        newNonTerminal = NonTerminal('SProgram', [newProduction])
        #Adding the Nonterminal to the production and the Production to the NonTerminal
        newProduction.head = newNonTerminal
        self.grammar.start = newNonTerminal
        self.grammar.nonTList.append(newNonTerminal)



class State:
    def __init__(self, items:List[LR1Item]) -> None:
        self.itemList: List[LR1Item] = items
        pass