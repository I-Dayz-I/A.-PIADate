import sys
sys.path.append('.')
import json
from os.path import exists

from comp_globals import  TokenType
from tokens import Token
from Grammar.grammar_classes import Grammar
from Parser.lr1_aux import LR1Table
from typing import List


class LR1Parser:
    def __init__(self, grammar: Grammar):
        self.grammar = grammar
        p = grammar.get_productions()

        self.table: LR1Table = LR1Table(grammar)
        self.action_table = self.table.action_table
        self.go_to_table = self.table.go_to_table

        self.final = Token(TokenType.Symbol,0,0,'$')

    def parse(self, tokens: List[Token]):
        print('here')
        tokens.append(Token(TokenType.Symbol,0,0,'$'))
        tokens_stack = []
        states_id_stack = [0]
        ast = []
        grammar_prod = self.grammar.get_productions()
        result_list = []

        while len(tokens) > 0:
            
            
            token = tokens[0]
            current_state_actions = self.action_table[states_id_stack[-1]]
#            print(token,current_state_actions)
#           print(tokens_stack)
            #TESTING
            if(token == TokenType.tokLoop):
                print('')
            #TESTING
            
            if token.value not in current_state_actions:
                raise Exception(
                    f'Unexpected token {token.value} with value {token.lexeme}, line {token.line +1}')

            action = current_state_actions[token.value]
          #  print(action)
            if action[0] == 'OK':
                return result_list

            # Apply a SHIFT Action
            elif action[0] == 'S':
                states_id_stack.append(action[1])
                tokens_stack.append(token.lexeme)
                tokens = tokens[1:] if len(tokens) >= 1 else []

            # Apply a REDUCE Action
            else:
                prod = grammar_prod[action[1]]
                print(prod)
                # if prod.ast_node_builder is not None:
                #     prod.ast_node_builder(tokens_stack, ast)

                self.remove_prod(len(prod.symbols), states_id_stack, tokens_stack)

                state_go_to = self.go_to_table[states_id_stack[-1]]
                if prod.head.name not in state_go_to:
                    raise Exception(
                        f"Non recognized tokens sequence starting with {prod.head.name}")
                
                result_list.append(prod)
                tokens_stack.append(prod.head.name)
                states_id_stack.append(state_go_to[prod.head.name])

    # method to remove production tokens and associated states from their respective stacks
    @staticmethod
    def remove_prod(counter, states, tokens):
        for i in range(counter):
            tokens.pop()
            states.pop()
