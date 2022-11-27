from typing import List, Dict, Set, Callable
from abc import ABCMeta, abstractmethod
from comp_globals import TokenType

#from Language.Parser.ast import *


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


class Terminal(Symbol):
    def __init__(self, name: str, value: str = '') -> None:
        super().__init__(name)
        self.value = value if value != '' else name

    def copy(self):
        return Terminal(self.name, self.value)

    def __repr__(self) -> str:
        return f"{self.value}"


class Production:

    def __init__(self, symbols: List[Symbol], ast_node_builder=None):
        self.head: NonTerminal = None
        self.symbols: List[Symbol] = symbols
        #self.ast_node_builder = ast_node_builder
        self.pos: int = 0

    def get_terminals(self) -> Set[Terminal]:
        terminals: Set = set()
        for symbol in self.symbols:
            if (isinstance(symbol, Terminal)):
                terminals.add(symbol)
        return terminals

    def is_eps(self) -> bool:
        return len(self.symbols) == 1 and self.symbols[0] == "EPS"

    def set_builder(self, func: Callable):
        self.ast_node_builder = func

    # def get_ast_node_builder(self):
    #     if self.ast_node_builder is None:
    #         raise ValueError("Builder function not set.")
    #     return self.ast_node_builder

    def __repr__(self):
        prod_str = "-> " + " ".join(str(symbol) for symbol in self.symbols)
        return prod_str

    def copy(self):
        return Production(self.symbols, self.ast_node_builder)


class NonTerminal(Symbol):
    def __init__(self, name: str, prodList: List[Production] = None):
        super().__init__(name)
        self.name = name
        self.productions = prodList if prodList is not None else []
        self._terminals_set: Set = set()

    def __iadd__(self, prod: Production):
        self.productions.append(prod)
        self._terminals_set.update(prod.get_terminals())
        prod.head = self
        return self

    def set_ast(self, ast):
        self._ast = ast

    def copy(self):
        return NonTerminal(self.name, self.productions)


class Grammar:
    def __init__(self, non_terminal_list: List[NonTerminal], start: NonTerminal):
        self.non_terminal_list = non_terminal_list
        self.start = start

    def get_productions(self) -> List[Production]:
        prods = []
        for non_term in self.non_terminal_list:
            self.update_pos(non_term.productions, prods)
            prods.extend(non_term.productions)
        return prods

    def update_pos(self, productions, prods_l):
        pos = len(prods_l)
        for prod in productions:
            prod.pos = pos
            pos += 1

    def get_terminals(self) -> Set[Terminal]:
        terminals = set()
        for non_term in self.non_terminal_list:
            terminals.update(non_term._terminals_set)
        return terminals

    def set_builder(self, func: Callable):
        self.ast_node_builder = func




_Semicolon = Terminal(';',TokenType.tokSemicolon)  # ;     -------
_Point = Terminal('.',TokenType.tokPoint)  # .
_Arrow = Terminal(':',TokenType.tokArrow) # :
_Comennt =Terminal('#',TokenType.tokComennt)  # -------
_OpenParen =Terminal('(',TokenType.tokOpenParen)   # (     -------
_ClosedParen = Terminal(')',TokenType.tokClosedParen)  # )     -------
_OpenBracket = Terminal('{',TokenType.tokOpenBracket)   # {     -------
_ClosedBracket = Terminal('}',TokenType.tokClosedBracket)  # }     -------
_OpenSquareBracket = Terminal('[',TokenType.tokOpenSquareBracket)  # [     -------
_ClosedSquareBracket = Terminal(']',TokenType.tokClosedSquareBracket) # ]     -------
_Int =  Terminal('int',TokenType.tokInt)  # int     -------
_Double =  Terminal('double',TokenType.tokDouble) # double     -------
_String = Terminal('string',TokenType.tokString)  # string     -------
_Bool = Terminal('bool',TokenType.tokBool)   # bool     -------
_None = Terminal('none',TokenType.tokNone)  # None
_True =  Terminal('true',TokenType.tokTrue)  # True     -------
_False = Terminal('false',TokenType.tokFalse)  # False     -------
_Dicc =  Terminal('Dicc',TokenType.tokDicc)  # Dicc     -------
_Number = Terminal('Dicc',TokenType.tokDicc)   # numeros    -------
_Chain = Terminal(-1,TokenType.tokChain)   # Cadenas     -------
_List =  Terminal('list',TokenType.tokList)  # list (propio)     -------
_If = Terminal('if',TokenType.tokIf)  # if     -------
_Else = Terminal('else',TokenType.tokElse)  # else     -------
_Loop = Terminal('loop',TokenType.tokLoop)  # loop     -------
_Break = Terminal('break',TokenType.tokBreak)  # break     -------
_Continue = Terminal('continue',TokenType.tokContinue)  # continue     -------
_Let = Terminal('let',TokenType.tokLet) # let     -------
_Def = Terminal('def',TokenType.tokDef)  # TokeTypes.tokDef     -------
_Import = Terminal('import',TokenType.tokImport)  # continue
_Comma = Terminal(',',TokenType.tokComma)  # ,
_NextLine = Terminal(',',TokenType.tokComma)  # /n
_Not = Terminal('not',TokenType.tokNot)  # !
_Equal = Terminal('==',TokenType.tokEqual)  # ==     -------
_NotEqual = Terminal('!=',TokenType.tokNotEqual)  # !=     -------
_LessOrEqual = Terminal('<=',TokenType.tokLessOrEqual)  # <=     -------
_GreaterOrEqual = Terminal('>=',TokenType.tokGreaterOrEqual) # >=     -------
_Greater = Terminal('>',TokenType.tokGreater) # >     -------
_Less = Terminal('<',TokenType.tokLess) # <     -------
_SearchDicc = Terminal('searchDicc',TokenType.tokSearchDicc) 
_ReturnDicc = Terminal('returnDicc',TokenType.tokReturnDicc) 
_Sum = Terminal('+',TokenType.tokSum)  # +     -------
_Sub = Terminal('-',TokenType.tokSub)   # -     -------
_Mul = Terminal('*',TokenType.tokMul)  # *     -------
_Div = Terminal('/',TokenType.tokDiv)  # /     -------
_ModDiv = Terminal('%',TokenType.tokModDiv)  # %     -------
_Pow = Terminal('^',TokenType.tokPow)  # ^     -------
_And = Terminal('&&',TokenType.tokAnd)   # &&     -------
_Or = Terminal('||',TokenType.tokOr)  # ||     -------
_ID = Terminal('identifier',TokenType.tokID)   # -------
_Assign = Terminal('=',TokenType.tokAssign)   # Assign     -------
_Return = Terminal('return',TokenType.tokReturn)  # Return      -------
_Print = Terminal('print',TokenType.tokPrint)  # Print     -------
_Board = Terminal('board',TokenType.tokBoard) 
_CPiece = Terminal('ChessPiece',TokenType.tokCPiece) 
_Insert = Terminal('Insert',TokenType.tokInsert) 
_Delete = Terminal('Delete',TokenType.tokDelete)
_Move = Terminal('move',TokenType.tokMove)
_Override = Terminal('override',TokenType.tokOverride)
_Epsilon = Terminal('epsilon',None)
_Insert = Terminal('insertDicc',TokenType.tokInsert)
_EOF = Terminal('EOF',TokenType.EOF)

pow_nt = NonTerminal("pow")
disjunction = NonTerminal("disjunction")
conjunction = NonTerminal("conjunction")
negation = NonTerminal("negation")
bfs_start = NonTerminal('bfs_start')
statements = NonTerminal('statements')
statement = NonTerminal('statement')
comparison = NonTerminal('comparison')
expression = NonTerminal('expression')
expressions = NonTerminal('expressions')
fun_def = NonTerminal('fun_def')
if_def = NonTerminal('if_def')
elif_def = NonTerminal('elif_def')
else_def = NonTerminal('else_def')
while_def = NonTerminal('while_def')
#type_nt = NonTerminal('type')
atom = NonTerminal('atom')
params = NonTerminal('params')
sum_nt = NonTerminal("sum")
term = NonTerminal('term')
factor = NonTerminal('factor')
basic = NonTerminal('basic')
fun_type = NonTerminal('fun_type')
list_nt = NonTerminal('List')
assign_nt = NonTerminal('assign')
return_nt = NonTerminal('return')
delete = NonTerminal('delete')
program = NonTerminal('program')
stat_list =  NonTerminal('stat_list')
stat_list_fix = NonTerminal('stat_list_fix')
stat = NonTerminal('stat')
override_expr = NonTerminal('override_expr')
var_reasign = NonTerminal('var_reasign')
return_exp = NonTerminal('return_exp')
continue_exp = NonTerminal('continue_exp')
break_exp = NonTerminal('break_exp')
let_dec = NonTerminal('let_dec')
func_dec = NonTerminal('func_dec')
print_stat = NonTerminal('print_stat')
condictional_stat = NonTerminal('condictional_stat')
if_stat = NonTerminal('if_stat')
else_fix = NonTerminal('else_fix')
else_stat = NonTerminal('else_stat')
loop_stat = NonTerminal('loop_stat')
lenguage_funtion = NonTerminal('lenguage_funtion')
move = NonTerminal('move')
insert = NonTerminal('insert')
all_types = NonTerminal('all_types')
leng_type = NonTerminal('leng_type')
args_list = NonTerminal('args_list')
args_list_fix = NonTerminal('args_list_fix')
params_list = NonTerminal('params_list')
params_list_fix = NonTerminal('params_list_fix')
type = NonTerminal('type')
expr = NonTerminal('expr')
term = NonTerminal('term')
factor = NonTerminal('factor')
atom = NonTerminal('atom')
comparer = NonTerminal('comparer')
func_call = NonTerminal('func_call')
dic_func = NonTerminal('dic_func')
dic_dec = NonTerminal('dic_dec')
search_dic = NonTerminal('search_dic')
recieve_dic = NonTerminal('recieve_dic')
insert_dic = NonTerminal('insert_dic')



program +=Production([_OpenBracket,stat_list])

stat_list += Production([stat,_Semicolon,stat_list_fix ])

stat_list_fix += Production([stat_list])
stat_list_fix += Production([_ClosedBracket])

stat += Production([override_expr])
stat += Production([let_dec])
stat += Production([func_dec])
stat += Production([var_reasign])
stat += Production([print_stat])
stat += Production([condictional_stat])
stat += Production([loop_stat])
stat += Production([lenguage_funtion])
stat += Production([break_exp])
stat += Production([return_exp])
stat += Production([continue_exp])
stat += Production([_Epsilon])

delete += Production([_Override, _OpenParen, args_list, _ClosedParen])
print(delete)

override_expr += Production([_Override,_OpenParen,args_list,_ClosedParen])

var_reasign += Production([_ID,_Assign,expr])

return_exp += Production([_Return,expr,expr])

continue_exp += Production([_Continue])

break_exp+= Production([_Break])

let_dec += Production([_Let,all_types,_ID,_Assign,expr])
print(delete)

func_dec += Production([_Def,_ID,_OpenParen,params_list,_ClosedParen,_Arrow,all_types,_OpenBracket,stat_list])

print_stat += Production([_OpenParen,expr,_ClosedParen])

condictional_stat += Production([if_stat])

if_stat += Production([_If,_OpenParen,expr,_ClosedParen,_OpenBracket,stat_list,else_fix])

else_fix += Production([else_stat])

else_fix += Production([_Epsilon])

else_stat += Production([_Else,_OpenBracket,stat_list])

else_stat += Production([_Epsilon])
print(delete)

loop_stat += Production([_Loop,_OpenParen, expr,_ClosedParen,_OpenBracket,stat_list])

lenguage_funtion += Production([insert])

lenguage_funtion += Production([delete])

move += Production([_Move,_OpenParen,args_list,_ClosedParen])
print(delete)

insert += Production([_Insert,_OpenParen,args_list,_ClosedParen])

all_types += Production([leng_type])

all_types += Production([type])

leng_type += Production([_Board])

leng_type += Production([_CPiece])

args_list += Production([expr,args_list_fix])

args_list += Production([_Epsilon])

args_list_fix += Production([_Epsilon])

args_list_fix += Production([_Comma,args_list])

params_list += Production([all_types,expr,params_list_fix])

params_list += Production([_Epsilon])

params_list_fix += Production([_Epsilon])

params_list_fix += Production([_Comma,params_list])

type += Production([_Int])

type += Production([_Double])

type += Production([_String])

type += Production([_Bool])

type += Production([_None])

expr += Production([term,_Sum,expr])

expr += Production([term,_Sub,expr])

expr += Production([term,comparer,expr])

expr += Production([term])

term += Production([term,_Mul,factor])

term += Production([term,_Div,factor])

term += Production([factor])

factor += Production([atom])

factor += Production([_OpenParen,expr,_ClosedParen])

atom += Production([_ID])

atom += Production([func_call])

atom+= Production([_Number])

atom+= Production([_None])

atom +=Production([_Chain])

atom += Production([_True])

atom += Production([_False])

atom += Production([_Epsilon])

comparer += Production([_Equal])

comparer += Production([_Not])

comparer += Production([_GreaterOrEqual])

comparer += Production([_Greater])

comparer += Production([_Less])

comparer += Production([_LessOrEqual])

comparer += Production([_And])

comparer += Production([_Or])

func_call += Production([dic_func])

func_call += Production([_ID,_OpenParen,args_list,_ClosedParen])

dic_func +=Production([search_dic])

dic_func +=Production([recieve_dic])

dic_func +=Production([insert_dic])

dic_func +=Production([dic_dec])

dic_dec += Production([_Dicc,_ID,_Assign,_OpenSquareBracket,args_list,_Comma,args_list,_ClosedSquareBracket])

search_dic += Production([_SearchDicc, _OpenParen,args_list, _ClosedParen])

recieve_dic += Production([_ReturnDicc, _OpenParen,args_list, _ClosedParen])

insert_dic += Production([_Insert, _OpenParen,args_list, _ClosedParen])

nonTermList = [delete,program,stat_list,stat_list_fix,stat,override_expr,var_reasign,return_exp,continue_exp,break_exp,let_dec,func_dec,print_stat,condictional_stat
            ,if_stat,else_fix,else_stat,loop_stat,lenguage_funtion,move,insert,all_types,leng_type,args_list,args_list_fix,params_list,params_list_fix,type,expr,term,
            factor,atom,comparer,func_call,dic_func,dic_dec,search_dic,recieve_dic,insert_dic,pow_nt,disjunction,conjunction,negation,bfs_start,statements,statement,comparison,expression,expressions
            ,fun_def,if_def,elif_def,else_def,while_def,atom,params,sum_nt,term,factor,basic,fun_type,list_nt,assign_nt,return_nt]

def GetGrammar() ->Grammar :
    fullGrammar = Grammar(nonTermList,program)
    
    return fullGrammar
