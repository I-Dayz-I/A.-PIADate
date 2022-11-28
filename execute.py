from Tokenizer.tokenizer import tokenizer
from Parser.parser_execute import get_result

import classnode

a=tokenizer("{let int a = 4 + 2; loop(a < 10){ let int b = 2 +3 ; };} ")

p_list = get_result(a)
p_list.reverse()

context= classnode.Context("Program")

newProgram= classnode.ProgramNode()
newProgram.build_ast(p_list,context)

# print()
# print('printeando la lista que devuelvo')
# print()
# print()

#for i in p_list:
#    print(i)