import grammar as gr
import lr1_parser as lr1

gr = gr.GetGrammar()

pars = lr1.LR1Parser(gr)

print('it worked sort off')