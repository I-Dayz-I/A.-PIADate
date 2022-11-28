from comp_globals import TokenType 
import ajedrez.ajedrez.board
import ajedrez.ajedrez.piece


    
#-----------------------   
class ClassNode():
    

    def Eval(self,context):
        pass
    
    def validateNode(self,context):
        pass
    
    def transpilar(self):
        pass

    def checkTypes(self):
        pass

    def build_ast(productionList):
        pass
    


#-----------------------
class Context():
    def __init__(self,name,classNode=None,fatherContext=None,breakCheck=False):
        
        self.diccVarContext : dict(str,[str,type,ClassNode])= {}
        self.diccFuncContext : dict(str,[str,[type],ClassNode])={} 
        self.fatherContext= fatherContext
        self.name=name
        self.breakCheck=breakCheck
        self.classNode=classNode
    
        
    def checkVar(self,var,varType):
        #declarada
        if var in self.diccVarContext or (self.fatherContext!=None and self.fatherContext.checkVar()):
            varAtributes=self.retVar(var)
            if varAtributes==None:
                #error de tipo
                return False
            if varAtributes[1]==varType:
                return True
        #no declarada
        return False

    def checkFun(self,var,typeList):
        #declarada
        if var in self.diccFuncContext or (self.fatherContext!=None and self.fatherContext.checkFun()):
            varAtributes=self.retFun(var,typeList)
            if varAtributes==None:
                #error de tipo
                return False
            #i=1
            #while i<len(typeList):
            #    if varAtributes[i]!=typeList[i]:
            #        return False
            return True
        #no declarada
        return False
    
    def define_var(self,var,varType,varValue):
        if not self.checkVar(var,varType):
            self.diccVarContext[var]=[var,varType,varValue]
            return True
        return False
            
    def define_func(self,var,typeList:list,node):
        if not self.checkVar(var,typeList):
            typeList.insert(0,var)
            self.diccVarContext[var]=[var,typeList,node]
            return True
        return False
    
    #este metodo devuelve una lista con el formator [name,type]
    def retVar(self,var):
        current=self
        while current!=None:
            if self==None: return None
            if var in current.diccVarContext:
                return current.diccVarContext[var]
            current=self.fatherContext
    
    #este metodo devuelve una lista con el formator [name,arg1Type,arg2Type....,argNType]
    def retFun(self,var,argList):
        current=self
        while current!=None:
            if self==None: return None
            if (var,argList) in current.diccFuncContext:
                return current.diccFuncContext[var]
            current=self.fatherContext
    
    def redeclareVar(self,var,varType,varValue):
        current=self
        while current!=None:
            if self==None: return None
            if var in current.diccVarContext:
                oldVar= current.diccVarContext[var]
                if oldVar[1]==varType:
                    current[var]=(var,varType,varValue)
                    return True
                #error los tipos son diferentes
                return False
            current=self.fatherContext
            
        #error la variable no existe
        return False
        
    def create_hild(self,name,node):
        chilcontext=Context(name,self,node)
        return chilcontext



#--------------------------------------------------------------------------- #
#-------------------------- Nodos Operadores ------------------------------- #
#--------------------------------------------------------------------------- #


#LISTO
class SumNode(ClassNode):
    def __init__(self,context): 
        self.Left=None
        self.Right=None
        self.context=context

        self.RT = None
        self.ET = None
    
    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)

        if value1.isnumeric() and value2.isnumeric():
            return  value1+value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla

    def transpilar(self):
        return str(self.Left) + " + " +  str(self.Right)

    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)
        
    def build_ast(self,productionList,indeProduc,context):
        self.Left=eatTerm(productionList,indeProduc,context)
        self.Right=eatExpression(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET
        
#listo
class SubNode(ClassNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context

        self.RT = None
        self.ET = None
    
    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)
        if value1.isnumeric() and value2.isnumeric():
            return  value1-value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
        
    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)

    def transpilar(self):
        return str(self.Left) + " - " +  str(self.Right)

    def build_ast(self,productionList,indeProduc,context):
        self.Left=eatTerm(productionList,indeProduc,context)
        self.Right=eatExpression(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET
    
#listo
class MulNode(ClassNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context
    
    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)
        if value1.isnumeric() and value2.isnumeric():
            return  value1*value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
        
    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)
    
    def transpilar(self):
        return str(self.Left) + " * " +  str(self.Right)

    def build_ast(self,productionList,indeProduc,context):
        self.Left=eatFactor(productionList,indeProduc,context)
        self.Right=eatTerm(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET

#listo    
class DivNode(ClassNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context

        self.RT = None
        self.ET = None
    
    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)
        if value1.isnumeric() and value2.isnumeric()and value2!=0:
            return  value1/value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
        
    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)

    def transpilar(self):
        return str(self.Left) + " / " +  str(self.Right)
    
    def build_ast(self,productionList,indeProduc,context):
        self.Left=eatFactor(productionList,indeProduc,context)
        self.Right=eatTerm(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET
#listo
class ModNode(ClassNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context
    
    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)
        if value1.isnumeric() and value2.isnumeric()and value2!=0:
            return  value1%value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
        
    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)

    def transpilar(self):
        return str(self.Left) + " % " +  str(self.Right)

    def build_ast(self,productionList,indeProduc,context):
        self.Left=eatFactor(productionList,indeProduc,context)
        self.Right=eatTerm(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET
        
#listo
class PowNode(ClassNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context

        self.RT = None
        self.ET = None
    
    def Eval(self):
        value1=self.Left.Eval()
        value2=self.Right.Eval()
        if int==type(value1)  and int==type(value2):
            return  value1**value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
        
    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)
    
    def transpilar(self):
        return str(self.Left) + " ^ " +  str(self.Right)

    def build_ast(self,productionList):
        pass

#--------------------------------------------------------------------------- #
#-----------------------Comparer Oper -------------------------------------- #
#--------------------------------------------------------------------------- #

#listo
class EqualNode(ClassNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None

        self.RT = None
        self.ET = None
    
    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)
        type1 = type(value1)
        type2 = type(value2)
        if type1 == type2:
            return  value1==value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
        
    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)

    def transpilar(self):
        return str(self.Left) + " == " +  str(self.Right)

    def build_ast(self,productionList,indeProduc,context):
        self.Left=eatTerm(productionList,indeProduc,context)
        self.Right=eatExpression(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET
    
#listo    
class NotEqualNode(ClassNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None

        self.RT = None
        self.ET = None
    
    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)
        if int==type(value1)  and int==type(value2):
            return  value1!=value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
        
    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)
    
    def transpilar(self):
        return str(self.Left) + " != " +  str(self.Right)


    def build_ast(self,productionList,indeProduc,context):
        self.Left=eatTerm(productionList,indeProduc,context)
        self.Right=eatExpression(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET

#listo    
class LoENode(ClassNode):
    def __init__(self):
        self.Left=None
        self.Right=None
    
        self.RT = None
        self.ET = None

    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)
        type1 = type(value1)
        type2 = type(value2)
        if type1 == type2:
            return  value1<=value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
        
    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)
    
    def transpilar(self):
        return str(self.Left) + " <= " +  str(self.Right)

    def build_ast(self,productionList,indeProduc,context):
        self.Left=eatTerm(productionList,indeProduc,context)
        self.Right=eatExpression(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET

#listo
class GoENode(ClassNode):
    def __init__(self):
        self.Left=None
        self.Right=None

        self.RT = None
        self.ET = None

    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)
        type1 = type(value1)
        type2 = type(value2)
        if type1 == type2:
            return  value1>=value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
        
    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)
        
    def transpilar(self):
        return str(self.Left) + " >= " +  str(self.Right)

    def build_ast(self,productionList,indeProduc,context):
        self.Left=eatTerm(productionList,indeProduc,context)
        self.Right=eatExpression(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET

#listo
class GreaterNode(ClassNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
    
        self.RT = None
        self.ET = None

    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)
        type1 = type(value1)
        type2 = type(value2)
        if type1 == type2:
            return  value1>value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
        
    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)
    
    def transpilar(self):
        return str(self.Left) + " > " +  str(self.Right)

    def build_ast(self,productionList,indeProduc,context):
        self.Left=eatTerm(productionList,indeProduc,context)
        self.Right=eatExpression(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET

#listo
class LessNode(ClassNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context
    
        self.RT = None
        self.ET = None

    def Eval(self,context):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)
        type1 = type(value1)
        type2 = type(value2)
        if type1 == type2:
            return  value1<value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
        
    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)
        
    def transpilar(self):
        return str(self.Left) + " < " +  str(self.Right)

    def build_ast(self,productionList,indeProduc,context):
        self.Left=eatTerm(productionList,indeProduc,context)
        self.Right=eatExpression(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET

    
#--------------------------------------------------------------------------- #
#--------------------------Condicional ------------------------------------- #
#--------------------------------------------------------------------------- #

#listo    
class AndNode(ClassNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context
    
        self.RT = None
        self.ET = None

    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)
        type1 = type(value1)
        type2 = type(value2)
        if type1 == type2:
            return  value1 and value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
        
    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)
    
    def transpilar(self):
        return str(self.Left) + " and " +  str(self.Right)

    def build_ast(self,productionList,indeProduc,context):
        self.Left=eatTerm(productionList,indeProduc,context)
        self.Right=eatExpression(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET

#listo
class OrNode(ClassNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context
    
        self.RT = None
        self.ET = None

    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)
        if bool==type(value1)  and bool==type(value2):
            return  value1 and value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
    
    def transpilar(self):
        return str(self.Left) + " or " +  str(self.Right)

    def validateNode(self,context):
        valid= self.Left.validateNode(context) or self.Right.validateNode(context)
        
    def build_ast(self,productionList,indeProduc,context):
        self.Left=eatTerm(productionList,indeProduc,context)
        self.Right=eatExpression(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET


# -------------------------------------------------------------------------
# Ciclos ------------------------------------------------------------------
# -------------------------------------------------------------------------
#listo
class LoopNode(ClassNode):
    def init(self,context:Context):
        self.Conditional=None
        self.Body=None
        self.breakref=None
        self.context=context
        self.newContext=None
    
        self.RT = None
        self.ET = None

    #hijo del break
    def breakValue(self):
        return self
    
    def Eval(self):
        while (self.Left.Eval()):
            
            self.Body.Eval(self.newContext)
            
    def transpilar(self):
        textcode = ""
        textcode += "while " + self.Conditional.transpilar() + ":"
        textcode += "\n \t"
        textcode += self.transpilar()

        return textcode
        
    def validateNode(self,context):
        valid= self.Conditional.validateNode(context) and self.Body.validateNode(context)
        
    def build_ast(self,productionList,indexProduc):
        indexProduc[0]+=1
        node=eatExpression(productionList,indexProduc,self.context)
        
        
        node.build_ast(productionList,indexProduc)
        self.Conditional=node
        
        self.newcontext=self.context.create_hild("loop",self)
        node=ProgramNode()
        node.build_ast(productionList,self.newcontext,indexProduc)
        self.Body=node
#listo
class BreakNode(ClassNode):
    def init(self, context):
        self.context = context
        self.RT = None
        self.ET = None


    def Eval(self, context):
        return

    def transpilar(self):
        return "break"
    
    def validateNode(self):
        contexttemp = self.context
        while True:
            name = contexttemp.name
            breakCheck = contexttemp.breakCheck
            classNode = contexttemp.classNode

            if name == "loop":
                if breakCheck == False:
                    self.context.breakCheck = True
                    classNode.breakref = self
                    return True
                elif classNode.breakref == self:
                    return True

            if contexttemp.fatherContext == None:
                break

            contexttemp = contexttemp.fatherContext

        return False

    def build_ast(self,productionList,indexProduc,context):
        indexProduc[0]+=1
        #esto hay que implementarlo ya que el el break al crease solo guarda a su hijo como el nodo loop mas cercano
        #esto seria buscar en el contexto
        self.context = context
        contexttemp = self.context
        
        while True:
            name = contexttemp.name
            breakCheck = contexttemp.breakCheck
            classNode = contexttemp.classNode

            if name == "loop":
                if breakCheck == False:
                    contexttemp.breakCheck = True
                    classNode.breakref = self
                    break
                elif classNode.breakref == self:
                    break

            if contexttemp.fatherContext == None:
                break

            contexttemp = contexttemp.fatherContext


#-------------------------- Modificar----------------------------------
#listo
class ProgramNode(ClassNode):
    def __init__(self):
        self.ListStatement = None
        
        self.RT = None
        self.ET = None

    def Eval(self):
        for statement in self.ListStatement:
            value = statement.Eval(self.context)
    
    def transpilar(self):
        textcode = ""
        for statement in self.ListStatement:
            textcode += statement.transpilar()
            textcode += "\n"

    def validateNode(self, context):
        for statement in self.ListStatement:
            if statement.validateNode(context):
                return False
            
    #["override_expr"],["let_dec"],["func_dec"],["var_reasign"],["print_stat"],["condictional_stat"],["loop_stat"],["lenguage_funtion"],["break_exp"],["return_exp"],["continue_exp"],["epsilon"]
    def build_ast(self,productionList,context,indexProduc=[0]):
        self.context = context

        #indexProduc[0]=0
        self.ListStatement=[]
        self.buildPosible()
        head=None
        while indexProduc[0]<len(productionList) :
            head=productionList[indexProduc[0]].head
            if productionList[indexProduc[0]].symbols[0]==TokenType.tokClosedBracket:
                break
            indexProduc[0]+=1
            #esto se come ciertas producciones
            if head in self.posibleProductions:
                
                #arreglar esto
                node=self.posibleProductions[head]()
                #resolver el nodo
                node.build_ast(productionList,indexProduc,self.contex)
                #agregarlo a los hijos
                self.ListStatement.append(node)
                
    
    def buildPosible(self):
        #arreglar esto
        self.posibleProductions={}
        
        self.posibleProductions["override_expr"]=OverrideNode
        self.posibleProductions["let_dec"]=LetNode
        self.posibleProductions["func_dec"]=FucNode
        self.posibleProductions["var_reasign"]=ReasignNode
        self.posibleProductions["print_stat"]=PrintNode
        self.posibleProductions["if_stat"]=IfNode
        self.posibleProductions["loop_stat"]=LoopNode
        #["die"],["modify"],["evolve"],["add"],["move"],["eat"],["create"]
        
        self.posibleProductions["break_exp"]=BreakNode
        self.posibleProductions["return_exp"]=ReturnNode
        self.posibleProductions["continue_exp"]=ContinueNode
    
    
#listo
class ContinueNode(ClassNode):
    def init(self):
        self.context = None
        self.loop = None
        self.loop_validate = False

        self.RT = None
        self.ET = None

    def Eval(self):
        self.loop.eval()

    def transpilar(self):
        return "continue"

    def validateNode(self):
        return self.loop_validate

    def build_ast(self,productionList, context,indexProduc=[0]):
        self.contex = context

        contexttemp = context
        while contexttemp == None:
            name = contexttemp.name
            classNode = contexttemp.classNode

            if name == "loop":
                self.loop_validate = True
                self.loop = classNode
                break

            contexttemp = contexttemp.fatherContext


class ReturnNode(ClassNode):
    def init(self):
        self.fun = None
        self.salida = None
        self.validatefun = False

        self.RT = None
        self.ET = None

    def Eval(self):
        val_salida = []

        count = 0
        for node_salida in self.salida:
            val_salida.append(node_salida.Eval())
            if type(val_salida[count]) != self.fun.argstypes[count]:
                raise Exception("La salida " + count + " de la función " + self.fun.name + " no coincide con el tipo esperado")

        return val_salida
    
    def validateNode(self):
        if not self.validatefun:
            return False

        for node_salida in self.salida:
            if not node_salida.validateNode():
                return False

        return True


    def transpilar(self):
        return  "return " + self.salida.transpilar()

    def build_ast(self,productionList,indexProduc,context):
        self.context = context

        indexProduc[0]+=1
        self.salida= eatExpression(productionList,indexProduc,context)

        contexttemp = self.context
        
        while contexttemp == None:
            classnode = contexttemp.classNode

            if type(classnode) == FucNode:
                self.validatefun = True
                self.fun = classnode
                break

            contexttemp = contexttemp.fatherContext


#listo
class BreakNode(ClassNode):
    def init(self, context):
        self.context = context
        self.RT = None
        self.ET = None


    def Eval(self, context):
        return

    def transpilar(self):
        return "break"
    
    def validateNode(self, context):
        contexttemp = context
        while True:
            name = contexttemp.name
            breakCheck = contexttemp.breakCheck
            classNode = contexttemp.classNode

            if name == "loop":
                if breakCheck == False:
                    context.breakCheck = True
                    classNode.breakref = self
                    return True
                elif classNode.breakref == self:
                    return True

            if contexttemp.fatherContext == None:
                break

            contexttemp = contexttemp.fatherContext

        return False

    def build_ast(self,productionList,indexProduc):
        indexProduc[0]+=1
        #esto hay que implementarlo ya que el el break al crease solo guarda a su hijo como el nodo loop mas cercano
        #esto seria buscar en el contexto

        contexttemp = self.context
        
        while True:
            name = contexttemp.name
            breakCheck = contexttemp.breakCheck
            classNode = contexttemp.classNode

            if name == "loop":
                if breakCheck == False:
                    self.context.breakCheck = True
                    classNode.breakref = self
                    break
                elif classNode.breakref == self:
                    break

            if contexttemp.fatherContext == None:
                break

            contexttemp = contexttemp.fatherContext

#listo
class LetNode(ClassNode):
    def __init__(self):
        self.type = None
        self.idnode = None
        self.val = None
        

        self.RT = None
        self.ET = None

    def Eval(self,context):
        return
    
    def validateNode(self, context):
        if not (self.idnode is IdNode) :
            return False

        validate = self.idnode.validateNode(context) and self.val.validateNode(context)
        return validate

    def transpilar(self):
        return "Let " + str(self.type) + " " + str(self.idnode) + " = " + self.val.transpilar()
    
    def build_ast(self,productionList,indexProduc,context):
        self.context = context
        #agregado el tipo "sale como token todavia no es grave"
        value=productionList[indexProduc[0]].components[1].value
        indexProduc[0]+=2
        self.type =eatType(productionList,indexProduc,context)
        #creando id
        idn=IdNode()
        #self,id,funcOrVar,defineOrCall,valType=None
        idn.build_ast(self.context,value,"var","define",self.type)
        
        self.idnode = idn
        #self.ET=self.idnode.RT
        indexProduc[0]+=1
        self.val=eatExpression(productionList,indexProduc,context)
        #self.RT=self.val.RT
        #guardar el el contexto el par como variable-valor/ varibale-funcion 
        self.context.define_var(idn, self.type, self.val)

#listo
class OverrideNode(ClassNode):
    def __init__(self):
        self.id1 = None
        self.id2 = None
        self.dont_exist=False


    def Eval(self):
        pass
    
    def validateNode(self, context):
        if self.dont_exist:
            return False

        return True

    def transpilar(self):
        return "Let " + str(self.type) + " " + str(self.idnode) + " = " + self.val
    
    def build_ast(self,productionList,indexProduc,context):
        self.context = context
        #agregado el tipo "sale como token todavia no es grave"
        args =eatArgList(productionList,indexProduc,context)
        #creando id
        self.id1=args[0]
        self.id2=args[1]
        try :
            self.context.diccFuncContext[self.id1.id]=self.context.diccFuncContext[self.id2.id]
        except:
            self.dont_exist=True

#listo
class ReasignNode(ClassNode):
    def init(self):
        self.idnode = None
        self.val = None
        self.dont_exit = True

        self.RT = None
        self.ET = None

    def Eval(self):
        self.context.redeclareVar(self.idnode, type(self.val) , self.val)
    
    def validateNode(self):
        if not self.idnode is IdNode:
            return False

        validate = self.idnode.validateNode(self.context) and self.val.validateNode(self.context)
        if not validate:
            return False

        return not self.dont_exit

    def transpilar(self):
        return str(self.idnode) + " = " + self.val.transpilar()
    
    def build_ast(self,productionList, context ,indexProduc):
        
        self.context = context

        #creando id
        idn=IdNode(self.context)
        #self,id,funcOrVar,defineOrCall,valType=None
        idn.build_ast(productionList[indexProduc[0]].components[1].head,"var","define",self.type)
        self.idnode = idn

        #self.ET=self.idnode.RT
        indexProduc[0]+=1
        self.val=eatExpression(productionList,indexProduc,context)
        #self.RT=self.val.RT

        ref = self.context.retVar(idn.name)

        if ref != None:
            self.dont_exit = False

            

    
expresionDicc={}
def fillExpresion():
    expresionDicc[TokenType.tokSub]=SumNode
    expresionDicc[TokenType.tokSum]=SubNode
    
termDicc={}
def fillTerm():
    termDicc[TokenType.tokMul]=MulNode
    termDicc[TokenType.tokDiv]=DivNode
    termDicc[TokenType.tokDiv]=DivNode

def eatType(productionList,indexProduc,context):
    return productionList[indexProduc[0]].components[0]

def eatExpression(productionList,indexProduc,context):
    if len(productionList[indexProduc[0]].components)==3:
        component=productionList[indexProduc[0]][1]
        if component in expresionDicc:
            #creamos el node
            node =expresionDicc[component]()
            
            indexProduc[0]+=1
            node.build_ast(productionList,indexProduc,context)
            return node
        elif component=="comparer":
            indexProduc[0]+=1
            return eatComparer(productionList,indexProduc,context)
    else:
        indexProduc[0]+=1
        return eatTerm(productionList,indexProduc,context)

def eatComparer(productionList,indexProduc,context):
    component=productionList[indexProduc][0][0]
    #buscando cual comparador es
    node =expresionDicc[component](context)
    
    indexProduc[0]+=1
    node.build_ast(productionList,indexProduc)
    return node

def eatFactor(productionList,indexProduc,context):
    component=productionList[indexProduc[0]][1]
    if component==productionList[indexProduc][0][0]==TokenType.tokOpenParen:
            indexProduc[0]+=1
            return eatExpression(productionList,indexProduc,context)
    else:
        indexProduc[0]+=1
        return eatAtom(productionList,indexProduc,context)
        
    
def eatTerm(productionList,indexProduc,context):
    if len(productionList[indexProduc][0].components)==3:
        component=productionList[indexProduc[0]][1]    
        if component in termDicc:
            #creamos el node
            node =expresionDicc[component]()
            
            indexProduc[0]+=1
            node.build_ast(productionList,indexProduc,context)
            return node
        else:
            indexProduc[0]+=1
            return eatFactor
        
    

def eatAtom(productionList,indexProduc,context):
    component=productionList[indexProduc][0][0]
    if component in termDicc:
        #buscando cual atomo es
        node =expresionDicc[component]()

        indexProduc[0]+=1
        node.build_ast(productionList,indexProduc)
        return node
    elif component=="func_call":
        indexProduc[0]+=1
        if len(productionList[indexProduc][0].component)==4:
            node=func_callNode()
            node.build_ast(productionList,indexProduc,context)
            return node
        elif productionList[indexProduc][0].component=="dic_func":
            indexProduc[0]+=2
            return eatDiccFunc(productionList,indexProduc,context)
        #elif productionList[indexProduc][0].component=="matrix_func":
        #    indexProduc[0]+=2
        #    eatMatrixFunc(productionList,indexProduc,context)



def eatDiccFunc():
    print("llegamos")
    pass
#def eatMatrixFunc(productionList,indexProduc,context):
#    component=productionList[indexProduc][0][0]
#    node =diccMatrixFunc[component](context)
#    
#    indexProduc[0]+=1
#    node.build_ast(productionList,indexProduc)
#    return node

# def eatDiccFunc(productionList,indexProduc,context):
    # component=productionList[indexProduc][0][0]
    # node =diccFunDicc[component](context)
    
    # indexProduc[0]+=1
    # node.build_ast(productionList,indexProduc,context)
    # return node
    

#listo
class IfNode(ClassNode):
    def init(self):
        self.condition = None
        self.body = None
        self.elsenode = None


        self.RT = None
        self.ET = None

    def Eval(self):
        if self.condition.Eval(self.context):
            self.body.Eval()

        else:
            self.elsenode.Eval()
    
    def transpilar(self):
        textcode = ""
        textcode += "if "
        textcode += self.condition.transpilar()
        textcode += ":"
        
        textcode += "\n\t"

        self.body.transpilar()

        textcode += "\n"
        textcode += self.elsenode.transpilar()

        return textcode


    def validateNode(self):
        validate1 = self.condition.validateNode()
        if not validate1:
            return False
        
        validate2 = self.body.validateNode()
        if not validate2:
            return False

        validate3 = self.elsenode.validateNode(self.context)
        if not validate3:
            return False

        return True
    
    def build_ast(self,productionList, context,indexProduc=[0]):
        self.context = context

        indexProduc[0]+=1
        self.condition = eatExpression(productionList,indexProduc,self.context)
        
        indexProduc[0]+=1 #? esto va aqui?
        self.newcontext=self.context.create_hild("if",self)
        self.body = ProgramNode()
        self.body.build_ast(productionList,indexProduc,self.newcontext)

        #indexProduc[0]+=1
        head = productionList[indexProduc[0]+1].head
        
        
        
        if head.name == "else":
            indexProduc[0]+=1
            self.elsenode = elseNode()

            self.elsenode.build_ast(productionList, self.context.fatherContext ,indexProduc)

#listo
class elseNode(ClassNode):
    def init(self):
        #self.ifnode = None
        self.body = None
        
        self.RT = None
        self.ET = None


    def Eval(self):
        self.ProgramNode.Eval()

    def transpilar(self):
        textcode = ""
        textcode += "else:"
        textcode += "\n"
        
        self.body.transpilar()

        return textcode


    def validateNode(self):
        if not self.context.name == "if":
            return False

        return self.body.validateNode()

    def build_ast(self, productionList, context, indexProduc=[0]):
        self.context = context

        self.newcontext=self.context.create_hild("else",self)
        indexProduc[0]+=1
        self.body = ProgramNode()
        self.body.build_ast(productionList, self.newcontext, indexProduc)

        
#ffffffff       
#listo
class IdNode(ClassNode):
    def init(self):
        self.id = None

        self.RT = None
        self.ET = None

    def Eval(self):
        if self.defineOrCall == "call":
            return self.context.retVar(self.id)

    def transpilar(self):
        return str(self.id)

    def validateNode(self):
        if self.defineOrCall == "call":
            if self.funcOrVar == "var":
                return self.context.retVar(self.id) != None

        
    
    #primer termino                                              "valor"
    def build_ast(self,context,id,funcOrVar,defineOrCall,valType="referencia"):
        self.id=id
        self.context = context
        self.RT=valType
        self.funcOrVar=funcOrVar
        self.defineOrCall=defineOrCall
        


class FucNode(ClassNode):
    def init(self,context):
        self.argstypes = None
        self.argsid = None
        self.name = None
        self.node_statements = None
        self.context = context
        
        self.ReturnType = None
        self.EspecterType = None

    def Eval(self,context):
        return self.Left + self.Right
    
    
    def build_ast(self,productionList,indexProduc,context):
        self.context=context

        #creando id
        idn=IdNode(self.context)
        #self,id,funcOrVar,defineOrCall,valType=None
        idn.build_ast(productionList[indexProduc][0].components[1],"func","define",None)
        
        self.idnode = idn
        #esta parte busca los parametros 
        indexProduc[0]+=1
        argsss=eatArgList(productionList,indexProduc,self.context)
        self.argsid=argsss[1]
        self.argstypes=argsss[0]
        
        indexProduc[0]+=2
        self.RT= eatType(productionList,indexProduc,context)
        indexProduc[0]+=1
        newcontext=self.context.create_hild("func",self)
        node=ProgramNode(newcontext)
        node.build_ast(productionList,indexProduc)
        self.node_statements=node
        
        
def eatArgList(productionList,indexProduc,context):
    
    resultId=[]
    while 1:
        if productionList[indexProduc][1].head=="args_list":
            indexProduc[0]+=1
            resultId.append(eatExpression(productionList,indexProduc,context))
        elif  productionList[indexProduc][1].head=="args_list_fix":
            indexProduc[0]+=1
            continue
        else:
            return resultId

def eatType(productionList,indexProduc):
    return productionList[indexProduc][0].components[0]

class func_callNode(ClassNode):
    def __init__(self,value = None,hijos = None):
        super().__init__(value,hijos)
        
        self.RT = None
        self.ET = None

        try:
            self.Left = hijos[0]
        except:
            Exception("No fue mandado el primer hijo")
            
        try:
            self.Right = hijos[1]
        except:
            Exception("No fue mandado el primer hijo")
            
    def Eval(self):
        return self.Left + self.Right
    
    def build_ast(self,productionList,indexProduc):
        indexProduc[0]+=1
        self.condition = eatExpression(productionList,indexProduc,self.context)
        
        #indexProduc[0]+=1 #? esto va aqui?
        self.ListStatements = ProgramNode(productionList,indexProduc,self.context)

#listo
class PrintNode(ClassNode):
    def __init__(self):
        self.name = "print"
        self.args = None
        

        self.RT = None
        self.ET = None

    def Eval(self,context):
        val = self.args[0].Eval(self.context)
        print(val)
        return
    
    def build_ast(self,context,productionList,indexProduc):
        self.context = context
        indexProduc[0]+=1
        self.args = eatExpression(productionList,indexProduc,self.context)


        

#------------------ Nodes of Chess---------------------------------------------------



#"move": [[TokeTypes.tokMove, TokeTypes.tokOpenParen,"args_list", TokeTypes.tokClosedParen]],
class MoveNode(ClassNode):
    def init(self):
        self.pos1x = None
        self.pos1y = None

        self.pos2x = None
        self.pos2y = None

        self.board = None

        self.RT = None
        self.ET = None

    def Eval(self,context):
        x1 = self.pos1x.Eval() 
        y1 = self.pos1y.Eval()

        x2 = self.pos2x.Eval()
        y2 = self.pos2y.Eval()
        
        return self.board.move_pos(x1,y1,x2,y2)
    
    def validateNode(self):
        if not self.posx.ValidateNode() or not self.posy.ValidateNode():
            return False
        
        if not self.pieza.ValidateNode() or self.board.ValidateNode():
            return False

        return True


    def transpilar(self):
        s = "move(" + self.board.transpilar() + "," + self.pos1x.transpilar()
        s += "," + self.pos1y.transpilar() + "," + self.pos2x.transpilar() + "," + self.pos2y.transpilar() + ")"
        return s

    def build_ast(self,productionList,indexProduc,context):
        self.context = context

        indexProduc[0]+=1
        args = eatArgList(productionList,indexProduc,context)

        self.board = args[0]
        self.pos1x = args[1]
        self.pos1y = args[2] 
        self.pos2x = args[3]
        self.pos2y = args[4]

class PieceNode(ClassNode):
    def init(self):
        self.fmov=None
        self.color=None
        self.tipo=None


    def Eval(self):
        return
    
    def validateNode(self):
        return self.fmov.ValidateNode()


    def transpilar(self):
        return  "Piece("+str(self.fmov.id.name)+","+str(self.color)+","+ self.tipo+ ")" 

    def build_ast(self,fmov,color, tipo,context):
        self.context = context
        self.fmov = fmov
        self.color = color
        self.tipo = tipo
 
class BoardNode(ClassNode):
    def init(self):
        self.id=None
        self.x=None
        self.y=None
        self.table = None


    def Eval(self,context):
        return BoardNode(self.x,self.y)
    
    def validateNode(self):
        if not self.x.validateNode() or not self.y.validateNode():
            return False
        if self.context.checkFunc(self.id,["board"]):
            return False
        return True


    def transpilar(self):
        return  "board("+str(self.x)+str(self.y)+ ")" 

    def build_ast(self,x,y,context):
        self.context = context
        self.x = x
        self.y = y

        self.table = []
        for i in range(self.x):
            self.table.append([])
            for j in range(self.y):
                self.table[j] = None




#"createdBoard": [[TokeTypes.tokMove, TokeTypes.tokOpenParen,"args_list", TokeTypes.tokClosedParen]],
class CreatedBoardNode(ClassNode):
    def init(self):
        self.id=None
        self.board = None


    def Eval(self):
        return BoardNode(self.board.x,self.board.y)
    
    def validateNode(self):
        if self.context.checkFunc(self.id,[BoardNode]):
            return False
        return self.board.validateNode()


    def transpilar(self):
        return  self.id + " = " + self.board.transpilar() 

    def build_ast(self,productionList,indexProduc,context):
        self.context = context

        #creando id
        idn=IdNode()
        #self,id,funcOrVar,defineOrCall,valType=None
        idn.build_ast(productionList[indexProduc][0].components[1],"func","define",None)

        indexProduc[0]+=1
        salida= eatArgList(productionList,indexProduc,context)

        x=salida[0]
        y=salida[1]
        self.board = BoardNode()
        self.board.build_ast(x,y,self.context)

        if self.context.retVar(self.id.name) != None:
            self.context.define_var(self.id.name, BoardNode, self.board)


class InsertNode(ClassNode):
    def init(self):
        self.posx = None
        self.posy = None
        self.pieza = None
        self.board = None

        self.RT = None
        self.ET = None

    def Eval(self):
        posx = self.posx.Eval()
        posy = self.posy.Eval()
        
        self.board.table[posx][posy] = self.pieza
    
    def validateNode(self):
        if not self.posx.ValidateNode() or not self.posy.ValidateNode():
            return False
        
        if not self.pieza.ValidateNode() or self.board.ValidateNode():
            return False

        return True

    def transpilar(self):
        return  "insert(" + self.pieza.transpilar() + "," + self.posx.transpilar() + "," + self.posy.transpilar() + ")"

    def build_ast(self,productionList,indexProduc,context):
        self.context = context

        indexProduc[0]+=1
        args = eatArgList(productionList,indexProduc,context)

        self.pieza = args[0]
        self.posx = args[1]
        self.posy = args[2]


class DeleteNode(ClassNode):
    def init(self):
        self.posx = None
        self.posy = None
        self.pieza = None
        self.board = None

        self.RT = None
        self.ET = None

    def Eval(self):
        posx = self.posx.Eval()
        posy = self.posy.Eval()

        self.board.table[posx][posy] = None

    
    def validateNode(self):
        if not self.posx.ValidateNode() or not self.posy.ValidateNode():
            return False
        
        if not self.pieza.ValidateNode() or self.board.ValidateNode():
            return False

        return True

    def transpilar(self):
        return  "delete(" + self.pieza.transpilar() + "," + self.posx.transpilar() + "," + self.posy.transpilar() + ")"


    def build_ast(self,productionList,indexProduc,context):
        self.context = context

        indexProduc[0]+=1
        args = eatArgList(productionList,indexProduc,context)

        self.pieza = args[0]
        self.posx = args[1]
        self.posy = args[2]
            
class CreatePieceNode(ClassNode):
    def init(self):
        self.id=None
        self.piece = None


    def Eval(self):
        return
    
    def validateNode(self):
        if self.context.checkFunc(self.id,[PieceNode]):
            return False
        if not self.piece.validateNode():
            return False
        return True

    def transpilar(self):
        return  self.id + " = " + self.piece.transpilar() 

    def build_ast(self,productionList,indexProduc,context):
        self.context = context

        #creando id
        idn=IdNode()
        #self,id,funcOrVar,defineOrCall,valType=None
        idn.build_ast(productionList[indexProduc][0].components[1],"func","define",None)

        indexProduc[0]+=1
        args= eatArgList(productionList,indexProduc,context)

        fmov=args[0]
        color=args[1]
        tipo=args[2]
        self.piece = PieceNode()
        self.piece.build_ast(fmov,color,tipo,self.context)

        if self.context.retVar(self.id.name) != None:
            self.context.define_var(self.id.name, BoardNode, self.board)