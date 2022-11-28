from Tokenizer.tokenizer import tokenizer
from Parser.parser_execute import get_result

a=tokenizer("{let int a = 4 + 2; loop(a < 10){ let int b = 2 +3 ; };} ")

p_list = get_result(a)

# print()
# print('printeando la lista que devuelvo')
# print()
# print()

for i in p_list:
    print(i)