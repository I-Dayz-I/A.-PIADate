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
    Symbol = enum.auto()


class Token:
    def __init__(self, value, lexeme, type, location):
        self.type = type
        self.value = value
        self.lexeme = lexeme
        self.name = lexeme
        self.location = location

    def __str__(self):
        return f"({self.value}, {self.type})"

    def __repr__(self):
        return self.__str__()


class TokenValues:
    # Keywords
    Def = "def"
    Return = "return"
    If = "if"
    Else = "else"
    Elif = "elif"
    While = "while"

    # Types
    Number = "Number"
    String = "String"
    Bool = "Bool"
    Void = "Void"
    List = "List"

    _True = "true"
    _False = "false"
    _None = "none"

    number = "number"

    # Arithmetic Operators
    Add = "+"  # +
    Sub = "-"  # -
    Mul = "*"  # *
    Div = "/"  # /
    Mod = "%"  # %
    Pow = "^"  # ^

    # Comparative Operators
    Less = "<"  # <
    LessOrEquals = "<="  # <=
    Greater = ">"  # >
    GreaterOrEquals = ">="  # >=
    Equals = "=="  # ==
    NotEquals = "!="  # !=

    # Logical Operators
    And = "and"  # and
    Or = "or"  # or
    Not = "not"  # !
    dot = "dot"  # .

    # Assignment
    Assign = "="  # =

    # Separators
    ValueSeparator = ","  # ,
    StatementSeparator = ";"  # ;

    # Text
    QuotationMarks = '"'  # "
    QuotationMarksS = "'"  # '

    # Others
    TwoPoints = ":"  #:
    Dot = "."  # .
    #
    OpenBracket = "("  # (
    ClosedBracket = ")"  # )
    OpenCurlyBraces = "{"  # {
    ClosedCurlyBraces = "}"  # }
    OpenStraightBracket = "["  # [
    ClosedStraightBracket = "]"  # ]

    #
    Print = "print"  # print

    #
    List = "list"  # list

    def __init__(self):
        pass
