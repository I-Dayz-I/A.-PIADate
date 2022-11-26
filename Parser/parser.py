from Grammar.grammar_classes import Grammar, Component, Production, Terminal, NonTerminal
from comp_globals import TokeTypes
from item import LR1Item
from typing import Dict, List, Tuple, Set
from automaton import Automata, LR1Table
from tokens import Token


class LR1Parser:
    def __init__(self, grammar: Grammar):
        self.grammar = grammar
        p = grammar.nonTList()

        self.table: LR1Table = LR1Table(grammar)
        self.action_table = self.table.action_table
        self.go_to_table = self.table.go_to_table
        
    def parse(self, tokens: List[Token]):
        tokens.append(Token('$', '$', TokenType.Symbol, 0))
        tokens_stack = []
        states_id_stack = [0]
        ast = []
        grammar_prod = self.grammar.get_productions()