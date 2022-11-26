from Grammar.grammar_classes import Grammar, Component, Production, Terminal, NonTerminal
from comp_globals import TokeTypes
from item import LR1Item
from typing import Dict, List, Tuple, Set
from json import load
import json
from os.path import exists


class Automata:
    
    def __init__(self,Grammar : Grammar) -> None:
        
        #Extending the grammar with the a initial Symbol
        self.grammar = Grammar
        self.grammar.start = None
        self.extendGrammar()
        
        start = self.grammar.start
        
        #Creating all initial Items with index in 0
        initial_items = {start: [LR1Item(start.productions[0], 0, Terminal('$', '$'))]}
        
        for non_term in self.grammar.nonTList:
            if (non_term.name == 'SProgram'):
                continue
            initial_items[non_term] = []
            for prod in non_term.productions:
                initial_items[non_term].append(LR1Item(prod, 0))
        
        initial_state = State(initial_items[start])
        initial_state.build(initial_items) 
        
        list_states = [initial_state]
        dict_states = {initial_state: initial_state}
        list_states_aux = list_states[:]
        
        while len(list_states_aux) > 0:
            state = list_states_aux[0]
            list_states_aux = list_states_aux[1:] if len(list_states_aux) >= 1 else []

            for sym in state.expectedComponet:
                state.set_go_to(sym, dict_states, list_states, list_states_aux, initial_items)

        self.list_states = list_states
    
    
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
        self.items = set(items)
        self.nexts: Dict[Component, State] = {}
        self.expectedComponet: Dict[Component, Set[LR1Item]] = {}
        self.number: int = 0


    def buildState(self, initialItems: Dict[NonTerminal, List[LR1Item]]):
        aux = self.itemList 
        
        while len(aux) > 0:
            item = aux[0]
            aux = aux[1:] if len(aux) >= 1 else []
            comp = item.getCurrentSymbol()
            b = {item}
            if item.dot_index == len(item.production.components):
                continue
            if comp in self.expectedComponet:
                self.expectedComponet[comp].add(item)
            else:
                self.expectedComponet[comp] = {item}

            if not comp.isTerminal():
                for i in initialItems[comp]:
                    if item.dot_index + 1 == len(item.production.components):
                        lookahead = item.lookahead
                    else:
                        lookahead = item.production.components[item.dot_index + 1]
                    new_item = LR1Item(i.production, i.dot_index, lookahead)
                    if new_item not in self.items:
                        self.items.add(new_item)
                        aux.append(new_item)
    
    
    def setGoTo(self,sym: Component, dict_states, list_states, aux: List, initial_items ):
        new_items = []
        
        for i in self.expectedComponet[sym]:
            new_item = LR1Item(i.production, i.dot_index + 1, i.lookahead)
            new_items.append(new_item)
        new_state = State(new_items)

        if new_state not in dict_states:
            new_state.number = len(dict_states)
            new_state.buildState(initial_items)
            dict_states[new_state] = new_state
            list_states.append(new_state)
            aux.append(new_state)
        else:
            new_state = dict_states[new_state]

        self.nexts[sym] = new_state
        

class LR1Table:
    def __init__(self, grammar: Grammar):
        self.grammar = grammar
        self.action_table = []
        self.go_to_table = []

        # If the action and go_to tables do not exist, they are built and then saved in a .json file.
        if not exists("lr1_table.json"):
            self.build_table()
        else:
            with open("lr1_table.json") as file:
                table = load(file)
                self.action_table = table[0]
                self.go_to_table = table[1]

    def build_table(self):
        aut = Automata(self.grammar)
        states = aut.list_states

        for state in states:
            state_action: Dict[str, Tuple[str, int]] = {}
            state_go_to: Dict[str, int] = {}

            for symbol in state.nexts:
                if symbol.isTerminal():
                    state_action[symbol.name] = ('SProgram', state.nexts[symbol].number)
                else:
                    state_go_to[symbol.name] = state.nexts[symbol].number

            dict_lookahead_item: Dict[Terminal, LR1Item] = {}

            for item in state.items:
                if item.dot_index == len(item.production.components):
                    dict_lookahead_item[item.lookahead] = item

##FIX THIS
            for lookahead in dict_lookahead_item:
                state_action[lookahead.name] = ('R', dict_lookahead_item[lookahead].production.pos)
                if lookahead.name == '$' and dict_lookahead_item[lookahead].production.head.name == 'SProgram':
                    state_action[lookahead.name] = ('OK', -1)

            self.action_table.append(state_action)
            self.go_to_table.append(state_go_to)

        # The tables are saved in a .json file
        with open('lr1_table.json', 'w') as file:
            json.dump([self.action_table, self.go_to_table], file)