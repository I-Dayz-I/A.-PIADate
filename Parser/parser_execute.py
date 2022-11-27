import sys
sys.path.append('.')
from Grammar.grammar_classes import GetGrammar
import Parser.lr1_parser as lr1


def get_result(List):
    gr = GetGrammar()
    pars = lr1.LR1Parser(gr)
    print('Tables were created')
    
    pars.parse(List)
    print('things were parrsed')