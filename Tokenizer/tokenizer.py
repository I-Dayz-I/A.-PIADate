
import sys
sys.path.append('.')
from logging import error
from unittest import result
import comp_globals
import tokens
import compErrors


def readSpecialKeyword(chain,currentPos,mytokens,line,column):
    currentToken=chain[currentPos]
    currentPos+=1
    while currentPos<len(chain):
        if chain[currentPos].isalpha() or chain[currentPos].isnumeric() or chain[currentPos]=="_":
            currentToken+=chain[currentPos]
            currentPos+=1
        else:
            break
    #if currentPos!=" ":
    #    compGlobals.errorsList.append(compErrors.CompError("Wrong special token declared",line,column))
    #    return -1
    if currentToken in comp_globals.specialKeywordsDicc:
        tempType=comp_globals.specialKeywordsDicc[currentToken]
        mytokens.append(tokens.Token(tempType,line,column,currentToken))
    else:    
        mytokens.append(tokens.Token(comp_globals.TokenType.tokID,line,column,currentToken))
    
    return currentPos
    
def readOperator(chain,currentPos,mytokens,line,column):
    currentToken=chain[currentPos]
    currentPos+=1
    tempOperator=currentToken
    while currentPos<len(chain):
        tempOperator+=chain[currentPos]
        if tempOperator in comp_globals.operatorsDicc:
            currentPos+=1
            currentToken=tempOperator
        else:
            break
    tempType=comp_globals.operatorsDicc[currentToken]
    mytokens.append(tokens.Token(tempType,line,column,currentToken))
    
    return currentPos

def readString(chain,currentPos,mytokens,line,column):
    print('reading String')
    currentToken=chain[currentPos]
    currentPos+=1
    while currentPos<len(chain):
        print(chain[currentPos])
        if chain[currentPos]=="\"":
            break
        currentToken+=str(chain[currentPos])
        currentPos+=1
    mytokens.append(tokens.Token(comp_globals.TokenType.tokChain,line,column,currentToken))
    print(currentToken)
    return currentPos

def readAlphaNumeric(chain,currentPos,mytokens,line,column):
    currenToken=chain[currentPos]
    currentPos+=1
    while currentPos<len(chain):
        if chain[currentPos].isalpha() or chain[currentPos].isnumeric() or chain[currentPos]=="_" :
            currenToken+=chain[currentPos]
            currentPos+=1
        else:
            break
    #if chain[currentPos]!=" " and not chain[currentPos] in compGlobals.operatorsDicc:
    #    compGlobals.errorsList.append(compErrors.CompError("Wrong alphanumeric token declared",line,column))
    #    return -1
    if currenToken in comp_globals.keywordsDicc:
        tempType=comp_globals.keywordsDicc[currenToken]
        mytokens.append(tokens.Token(tempType,line,column,currenToken))
    else:    
        mytokens.append(tokens.Token(comp_globals.TokenType.tokID,line,column,currenToken))
    
    return currentPos

def readNumeric(chain, currentPos,mytokens,line,column):
    point=0
    currentToken=chain[currentPos]
    currentPos+=1
    while currentPos<len(chain):
        if chain[currentPos]==".":
            if point==1:
                comp_globals.errorsList.append(compErrors.CompError("Wrong number token declared",line,column))
                return -1
            else:
                currentToken+=chain[currentPos]
                point=1
        elif chain[currentPos].isnumeric():
            currentToken+=chain[currentPos]
        else: 
            break
        currentPos+=1
    
    #if chain[currentPos]!=" " and not chain[currentPos] in compGlobals.operatorsDicc:
    #    compGlobals.errorsList.append(compErrors.CompError("Wrong numer token declared",line,column)) 
    #    return-1
    
    if point==0:
        mytokens.append(tokens.Token(comp_globals.TokenType.tokNumber,line,column,currentToken))
    else:
        mytokens.append(tokens.Token(comp_globals.TokenType.tokNumber,line,column,currentToken))
    return currentPos



def readComment(chain,currentPos):
    while currentPos<len(chain):
        currentPos+=1
        if chain[currentPos]=="\n":
            return currentPos
        currentPos+=1

def tokenizer(chain):
    line =1
    column=1
    currentPos=0
    initialPos=0
    currentToken=""
    mytokens=[]
    parenthesis=0
    squareBracket=0
    brackect=0
    
    
    while currentPos<len(chain):
        currentToken=chain[currentPos]
        if currentToken==" ":
            pass
        elif currentToken in comp_globals.bracketDicc:
            tempType=comp_globals.bracketDicc[currentToken]
            mytokens.append(tokens.Token(tempType,line,column,currentToken))
            
        
        elif currentToken=="$":
            specialKeyword=readSpecialKeyword(chain,currentPos,mytokens,line,column)-1
            if len(comp_globals.errorsList)>0:
                return None
            currentPos=specialKeyword
        
        elif currentToken=="\n":
            line+=1
            column=0
        elif currentToken=="#":
            currentPos=readComment(chain,currentPos)-1
        elif currentToken.isnumeric():
            numericResult=readNumeric(chain,currentPos,mytokens,line,column)-1
            if len(comp_globals.errorsList)>0:
                return None
            currentPos=numericResult
        elif currentToken=="\"":
            print('reading String')
            new_pos=readString(chain,currentPos,mytokens,line,column)
            currentPos = new_pos
        elif currentToken.isalpha():
            alphaResult=readAlphaNumeric(chain,currentPos,mytokens,line,column)-1
            if len(comp_globals.errorsList)>0:
                return None
            currentPos=alphaResult

        elif currentToken in comp_globals.operatorsDicc :
            currentPos=readOperator(chain,currentPos,mytokens,line,column)-1
        elif currentToken in comp_globals.puntuationDicc :
            tempType=comp_globals.puntuationDicc[currentToken]
            mytokens.append(tokens.Token(tempType,line,column,currentToken))
        else:
            comp_globals.errorsList.append(compErrors.CompError("Unexpected token",line,column)) 
            return None
                    
        currentPos+=1
        column+=currentPos-initialPos
        initialPos=currentPos
        
    #if balanceEverything(parenthesis,squareBracket,brackect):
    return mytokens
    #return None
        
        
        
def balanceEverything(parenthesis, squareBracket, brackect):
    if parenthesis!=0:
        comp_globals.errorsList.append(compErrors.CompError("Unbalance parenthesis",-1,-1)) 
        return False
    if squareBracket!=0:
        comp_globals.errorsList.append(compErrors.CompError("Unbalance squareBracket",-1,-1)) 
        return False
    if brackect!=0:
        comp_globals.errorsList.append(compErrors.CompError("Unbalance brackect",-1,-1)) 
        return False
    return True
    
    
a=tokenizer("int a=4*2; $Die p1; loop if(){}")
print("$Move $MatrixSum; a=(3+4)*7 ")