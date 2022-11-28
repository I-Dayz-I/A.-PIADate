#from class_node import classnode
from comp_globals import TokenType

terminales = ["epsilon", TokenType.tokComma, TokenType.tokOpenSquareBracket, TokenType.tokClosedSquareBracket, TokenType.tokList, TokenType.tokID,
              TokenType.tokMatrix, TokenType.tokIndividual, TokenType.tokMap, TokenType.tokphenomenon, TokenType.tokModify, TokenType.tokMSum,
              TokenType.tokMSub, TokenType.tokMMul, TokenType.tokMDiv, TokenType.tokDie, TokenType.tokEvolve, TokenType.tokAdd, TokenType.tokMove,
              TokenType.tokEat, TokenType.tokElse, TokenType.tokElif, TokenType.tokOpenParen, TokenType.tokClosedParen,
              TokenType.tokOpenBracket, TokenType.tokOr, TokenType.tokAnd, TokenType.tokGreaterOrEqual, TokenType.tokLessOrEqual, TokenType.tokNotEqual,
              TokenType.tokEqual, TokenType.tokGreater, TokenType.tokLess, TokenType.tokIf, TokenType.tokContinue,
              TokenType.tokBreak, TokenType.tokReturn, TokenType.tokLoop, TokenType.tokSum, TokenType.tokSub, TokenType.tokMul, TokenType.tokDiv, TokenType.tokModDiv,
              TokenType.tokPow, TokenType.tokString, TokenType.tokInt, TokenType.tokDouble, TokenType.tokTrue, TokenType.tokFalse, TokenType.tokBool, TokenType.tokAssign,
              TokenType.tokSemicolon, TokenType.tokClosedBracket, TokenType.EOF]


productions = {
    # program
    "program": [[TokenType.tokOpenBracket, "stat_list"]],

    # lista de statments
    "stat_list": [["stat", TokenType.tokSemicolon, "stat_list_fix"]],

    # si un statment se va en epsilon o sigue con una lista de statments
    # ["epsilon"] ?
    "stat_list_fix": [["stat_list"], [TokenType.tokClosedBracket]],

    # statment
    "stat": [["override_expr"], ["let_dec"], ["func_dec"], ["var_reasign"], ["print_stat"], ["condictional_stat"], ["loop_stat"], ["lenguage_funtion"], ["break_exp"], ["return_exp"], ["continue_exp"], ["epsilon"]],

    # statement cambia el la funcion de nombre el primer id por la del segundo id
    "override_expr": [TokenType.tokOverride, TokenType.tokOpenParen, "args_list",  TokenType.tokClosedParen],

    # reasignacion de variable
    "var_reasign": [TokenType.tokID, TokenType.tokAssign, "expr"],

    # return expresion
    "return_exp": [[TokenType.tokReturn, "expr"]],

    # expresion continue
    "continue_exp": [[TokenType.tokContinue]],

    # expresion break
    "break_exp": [[TokenType.tokBreak]],

    # let declarator
    "let_dec": [[TokenType.tokLet, "all_types", TokenType.tokID, TokenType.tokAssign, "expr"]],

    # declarador de funciones
    "func_dec": [[TokenType.tokDef, TokenType.tokID, TokenType.tokOpenParen, "params_list", TokenType.tokClosedParen, TokenType.tokArrow, "all_types", TokenType.tokOpenBracket, "stat_list"]],

    # print statment
    "print_stat": [TokenType.tokOpenParen, "expr", TokenType.tokClosedParen],

    # condicionales
    "condictional_stat": [["if_stat"]],

    # if statment   (aca regla semantica para q exp sea bool)
    "if_stat": [[TokenType.tokIf, TokenType.tokOpenParen, "expr", TokenType.tokClosedParen, TokenType.tokOpenBracket, "stat_list","else_fix"]],

    # elif statment   (aca regla semantica para q exp sea bool)
    #"elif_stat": [[TokeTypes.tokElif, TokeTypes.tokOpenParen, "expr", TokeTypes.tokClosedParen, TokeTypes.tokOpenBracket, "stat_list"], ["epsilon"]],
    
    #else_fix
    "else_fix":[["else_stat"],["epsilon"]],

    # else statment
    "else_stat": [[TokenType.tokElse, TokenType.tokOpenBracket, "stat_list"], ["epsilon"]],

    # loop statment   (aca regla semantica para q exp sea bool) y añadir a expr Tokbreak, como usar el break se hara mediante los contextos al ponerle el nombre de un loop si es un loop quien lo llama
    "loop_stat": [[TokenType.tokLoop, TokenType.tokOpenParen, "expr", TokenType.tokClosedParen, TokenType.tokOpenBracket, "stat_list"]],

    # funciones especiales del lenguaje
    # "lenguage_funtion":[["die"],["modify"],["evolve"],["add"],["move"],["eat"],["create"]],  # sacado para ponerlo en expresion
    "lenguage_funtion": [["insert"], ["delete"], ["move"]],

    # lenguage funtion move
    # "move":[[TokeTypes.tokMove,TokeTypes.tokOpenParen,"args_list",TokeTypes.tokClosedParen]],
    # chess version.... It takes a board identifier and 4 ints (initial and final positions)
    "move": [[TokenType.tokMove, TokenType.tokOpenParen,"args_list", TokenType.tokClosedParen]],

    # lenguage funtion insert (pensar en declarar la pieza en la misma linea)
    "insert": [[TokenType.tokInsert, TokenType.tokOpenParen, "args_list", TokenType.tokClosedParen]],

    # lenguage funtion die
    # "eat":[[TokeTypes.tokEat,TokeTypes.tokOpenParen,"args_list",TokeTypes.tokClosedParen]],

    # lenguage funtion create
    # "create":[[TokeTypes.tokCreate,TokeTypes.tokOpenParen,"args_list",TokeTypes.tokClosedParen]],

    # todos los tipos del lenguaje
    "all_types": [["leng_type"], ["type"]],

    # lenguaje types
    # "leng_type":[[TokeTypes.tokIndividual],[TokeTypes.tokSpecies],[TokeTypes.tokMap],[TokeTypes.tokphenomenon]],
    "leng_type": [[TokenType.tokBoard],  [TokenType.tokCPiece]],

    # args_list
    "args_list": [[ "expr", "args_list_fix"], ["epsilon"]],

    # si un arg se va en epsilon o sigue con una lista de statments
    "args_list_fix": [["epsilon"], [TokenType.tokComma, "args_list"]],

    #params_list
    "params_list": [["all_types","expr", "params_list_fix"], ["epsilon"]],

    # si un params se va en epsilon o sigue con una lista de expr
    "params_list_fix": [["epsilon"], [TokenType.tokComma, "params_list"]],

    # types
    "type": [[TokenType.tokInt], [TokenType.tokDouble], [TokenType.tokString], [TokenType.tokBool], [TokenType.tokNone]],

    # expresions
    "expr": [["term", TokenType.tokSum, "expr"], ["term", TokenType.tokSub, "expr"], ["term", "comparer", "expr"], ["term"]],

    # terminos
    "term": [["term", TokenType.tokMul, "factor"], ["term", TokenType.tokDiv, "factor"], ["factor"]],

    # factor
    "factor": [["atom"], [TokenType.tokOpenParen, "expr", TokenType.tokClosedParen]],

    # atomos
    "atom": [[TokenType.tokID], ["func_call"], [TokenType.tokNumber]  ,[TokenType.tokNone], [TokenType.tokChain], [TokenType.tokTrue], [TokenType.tokFalse], ["epsilon"]],

    # comparadores
    "comparer": [[TokenType.tokNot], [TokenType.tokNotEqual], [TokenType.tokGreaterOrEqual], [TokenType.tokGreater], [TokenType.tokLess], [TokenType.tokLessOrEqual], [TokenType.tokAnd], [TokenType.tokOr]],


    # llamados a funciones
    "func_call": [ ["dic_func"], [TokenType.tokID, TokenType.tokOpenParen, "args_list", TokenType.tokClosedParen]],

    # funciones de diccionario
    "dic_func": [["search_dic"], ["recieve_dic"], ["insert_dic"], ["dic_dec"]],

    # declaracion de diccionario
    "dic_dec": [[TokenType.tokDicc, TokenType.tokOpenSquareBracket, "args_list", TokenType.tokClosedSquareBracket]],

    # pregunta si una funcion
    "search_dic": [[TokenType.tokSearchDicc, TokenType.tokOpenParen, "args_list", TokenType.tokClosedParen]],

    # retorna el valor asociado a la llave
    "recieve_dic": [[TokenType.tokReturnDicc, TokenType.tokOpenParen, "args_list", TokenType.tokClosedParen]],

    # retorna el valor asociado a la llave
    "insert_dic": [[TokenType.tokInsertDicc, TokenType.tokOpenParen, "args_list", TokenType.tokClosedParen]],

    # vector type
 
    # lista de expresiones
    #"expr_list": [["expr"], ["expr_list_fix"]],

    # fix de expresion list
    #"expr_list_fix": [[TokeTypes.tokComma, "expr_list"], ["epsilon"]]
}

#------------------------------------------------------------------------------------------------------#
#------------------------------------- DicNode --------------------------------------------------------#
#------------------------------------------------------------------------------------------------------#

# dicNode = {
#     "program": classnode.ProgramNode(),
#     "stat": classnode.StatementNode(),
#     "break": classnode.BreakNode(),
#     "let_dec": classnode.LetNode(),
#     "func_dec": classnode.FucNode(),
#     "print_stat": classnode.PrintNode(),
#     "condictional_stat": classnode.Condictional_statNode(),
#     "if_stat": classnode.IfNode(),
#     "elif_stat": classnode.ElifNode(),
#     "else_stat": classnode.elseNode(),
#     "loop_stat": classnode.loopNode(),
#     "die": classnode.dieNode(),
#     "modify": classnode.modifyNode(),
#     "evolve": classnode.evolveNode(),
#     "add": classnode.AddNode(),
#     "move": classnode.moveNode(),
#     "eat": classnode.eatNode(),
#     "create": classnode.createNode(),
#     "func_call": classnode.func_callNode(),
#     "vectorial": classnode.vectorialNode(),
#     "dic_dec": classnode.DicNode(),
#     "search_dic": classnode.SearchDicNode(),
#     "recieve_dic": classnode.RecieveDicNode(),
#     "var_reasign": classnode.RedeclareVar(),
#     "return_exp": classnode.ReturnNode(),

#     #------------------------------------- TokTerminales -----------------------------------------------#

#     TokenType.tokBreak: classnode.TookBreakNode(),
#     TokenType.tokID: classnode.IdNode(),
#     TokenType.tokEqual: classnode.EqualNode(),
#     TokenType.tokSum: classnode.SumNode(),
#     TokenType.tokSub: classnode.SubNode(),
#     TokenType.tokMul: classnode.MulNode(),
#     TokenType.tokDiv: classnode.DivNode(),
#     TokenType.tokNumber: classnode.NumberNode(),
#     TokenType.tokChain: classnode.ChainNode(),
#     TokenType.tokTrue: classnode.TrueNode(),
#     TokenType.tokFalse: classnode.FalseNode(),
#     TokenType.tokNone: classnode.NoneNode()
# }

