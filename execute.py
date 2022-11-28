from Tokenizer.tokenizer import tokenizer
from Parser.parser_execute import get_result

a=tokenizer("{let int a = 4 * 2; loop(a < 10){ int b = 2 +3 ;}}")

p_list = get_result(a)
print(p_list)