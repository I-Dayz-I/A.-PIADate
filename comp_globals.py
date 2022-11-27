import enum



class TokenType(enum.Enum):
    tokSemicolon = enum.auto()  # ;     -------
    tokPoint = enum.auto()  # .
    tokArrow = enum.auto()  # :

    tokComennt = enum.auto()  # -------

    tokOpenParen = enum.auto()  # (     -------
    tokClosedParen = enum.auto()  # )     -------
    tokOpenBracket = enum.auto()  # {     -------
    tokClosedBracket = enum.auto()  # }     -------
    tokOpenSquareBracket = enum.auto()  # [     -------
    tokClosedSquareBracket = enum.auto()  # ]     -------

    tokInt = enum.auto()  # int     -------
    tokDouble = enum.auto()  # double     -------
    tokString = enum.auto()  # string     -------
    tokBool = enum.auto()  # bool     -------
    tokNone = enum.auto()  # None
    tokTrue = enum.auto()  # True     -------
    tokFalse = enum.auto()  # False     -------
    tokDicc = enum.auto()  # Dicc     -------
    tokNumber = enum.auto()  # numeros    -------
    tokChain = enum.auto()  # Cadenas     -------

    tokList = enum.auto()  # list (propio)     -------
    # tokMatrix=enum.auto() # matrix (propio)     -------
    # tokIndividual=enum.auto() #Individuo (propio)     -------
    # tokSpecies=enum.auto() #Especie (propio)     -------
    # tokMap=enum.auto() #mapa (propio)     -------
    # tokphenomenon=enum.auto() #fenomeno (propio)     -------

    tokIf = enum.auto()  # if     -------
    tokElif = enum.auto()  # elif     -------
    tokElse = enum.auto()  # else     -------
    tokLoop = enum.auto()  # loop     -------
    tokBreak = enum.auto()  # break     -------
    tokContinue = enum.auto()  # continue     -------
    tokLet = enum.auto()  # let     -------
    tokDef = enum.auto()  # TokeTypes.tokDef     -------

    tokImport = enum.auto()  # continue

    tokComma = enum.auto()  # ,
    tokNextLine = enum.auto()  # /n
    tokNot = enum.auto()  # !

    tokEqual = enum.auto()  # ==     -------
    tokNotEqual = enum.auto()  # !=     -------
    tokLessOrEqual = enum.auto()  # <=     -------
    tokGreaterOrEqual = enum.auto()  # >=     -------
    tokGreater = enum.auto()  # >     -------
    tokLess = enum.auto()  # <     -------

    tokSearchDicc = enum.auto()
    tokReturnDicc = enum.auto()
    tokInsertDicc = enum.auto()

    tokSum = enum.auto()  # +     -------
    tokSub = enum.auto()  # -     -------
    tokMul = enum.auto()  # *     -------
    tokDiv = enum.auto()  # /     -------
    tokModDiv = enum.auto()  # %     -------
    tokPow = enum.auto()  # ^     -------

    tokAnd = enum.auto()  # &&     -------
    tokOr = enum.auto()  # ||     -------

    tokID = enum.auto()  # -------

    
    tokModify = enum.auto()  # $Modify    -------
    tokCreate = enum.auto()  # $Create       --------
    tokDie = enum.auto()  # $Die     -------
    tokEvolve = enum.auto()  # $Evolve     -------
    tokAdd = enum.auto()  # $Add     -------
    tokMove = enum.auto()  # $Move     -------
    tokEat = enum.auto()   # $Eat     -------

    tokMSum = enum.auto()  # $MatrixSum
    tokMSub = enum.auto()  # $MatrixSub
    tokMMul = enum.auto()  # $MatrixMul
    tokMDiv = enum.auto()  # $MatrixDiv

    tokAssign = enum.auto()  # Assign     -------
    tokReturn = enum.auto()  # Return      -------
    tokPrint = enum.auto()  # Print     -------
    # tokOverride=enum.auto() #override

    # ---------Chess--------------------

    tokBoard = enum.auto()
    tokCPiece = enum.auto()

    tokInsert = enum.auto()
    tokDelete = enum.auto()
    tokOverride = enum.auto()
    EOF =enum.auto()
    Symbol =enum.auto()


keywordsDicc = {
    # Keywords Condicionales
    "if": TokenType.tokIf,
    "elif": TokenType.tokElif,
    "else": TokenType.tokElse,
    
    "override":TokenType.tokOverride,

    # declaracion
    "let": TokenType.tokLet,
    "def": TokenType.tokDef,

    # Keywords de Ciclos
    "loop": TokenType.tokLoop,

    "break": TokenType.tokBreak,
    "continue": TokenType.tokContinue,

    # Keywords de tipos
    "int": TokenType.tokInt,
    "double": TokenType.tokDouble,
    "string": TokenType.tokString,
    "dict": TokenType.tokDicc,

    # Keywords de valor
    "bool": TokenType.tokBool,
    "None": TokenType.tokNone,
    # "True"     : TokeTypes.tokTrue,
    # "False "   : TokeTypes.tokFalse,

    # Kewords del trabajo
    # "Individuo": TokeTypes.tokIndividual,
    # "Especie"  : TokeTypes.tokSpecies,
    # "mapa"     : TokeTypes.tokMap,
    # "fenomeno" : TokeTypes.tokphenomenon,

    # Keywords de ajedrez
    "Board": TokenType.tokBoard,
    "CPiece": TokenType.tokCPiece,


    # especiales
    "print": TokenType.tokPrint
}

operatorsDicc = {
    # Operadores de calculo
    "+": TokenType.tokSum,
    "-": TokenType.tokSub,
    "*": TokenType.tokMul,
    ":": TokenType.tokDiv,
    "%": TokenType.tokModDiv,
    "^": TokenType.tokPow,

    # operador de asignacion
    "=": TokenType.tokAssign,

    # Operadores condicionales
    "&&": TokenType.tokAnd,
    "||": TokenType.tokOr,
    "!":    TokenType.tokNot,
    # Operadores de comparacion
    "==": TokenType.tokEqual,
    "!=": TokenType.tokNotEqual,
    "<=": TokenType.tokLessOrEqual,
    ">=": TokenType.tokGreaterOrEqual,
    ">": TokenType.tokGreater,
    "<": TokenType.tokLess,



    # solo para la tokenizacion
    "&": None,
    "|": None,




}

bracketDicc = {
    "(": TokenType.tokOpenParen,
    ")": TokenType.tokClosedParen,
    "[": TokenType.tokOpenSquareBracket,
    "]": TokenType.tokClosedSquareBracket,
    "{": TokenType.tokOpenBracket,
    "}": TokenType.tokClosedBracket,
}

puntuationDicc = {
    # Signos de comentario
    "#": TokenType.tokComennt,

    # Signos de puntuacion
    ";":  TokenType.tokSemicolon,
    # "." :  TokeTypes.tokPoint,

    # Signos de Separacion
    ",": TokenType.tokComma,
    # "."  : TokeTypes.tokColom,

    # simbolo para especificar tipos de retorno
    "->": TokenType.tokArrow,
    # Signos Especiales
    # "\n" : TokeTypes.tokNextLine
}

specialKeywordsDicc = {

    # "$Modify": TokeTypes.tokModify,
    # "$Create" :TokeTypes.tokCreate,
    # "$Die": TokeTypes.tokDie,
    # "$Evolve":TokeTypes.tokEvolve,
    # "$Add":TokeTypes.tokAdd,
    # "$Move":TokeTypes.tokMove,
    # "$Eat":TokeTypes.tokEat,
    # "$Override":TokeTypes.tokOverride,

    # "$MatrixSum":TokeTypes.tokMSum,
    # "$MatrixSub":TokeTypes.tokMSub,
    # "$MatrixMul":TokeTypes.tokMMul,
    # "$MatrixDiv":TokeTypes.tokMDiv

    # Chess

    "insert": TokenType.tokInsert,
    "delete": TokenType.tokDelete,
    "move":TokenType.tokMove,


}

errorsList = []
