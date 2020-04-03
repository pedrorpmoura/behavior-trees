import ply.lex as lex
import sys
import re




literals = "{[]},:->$%"
t_ignore = " \n\t"

tokens = (
    # keywords
    'BEHAVIOR',
    'SEQUENCE',
    'SELECTOR',
    'PROBSELECTOR',
    'PARALLEL',
    'DECORATOR',
    'CONDITION',
    'ACTION',
    'EXPRESSION',
    # 'INVERTER',
    # 'MAXTRIES',
    # 'MAXSECONDS',

     # variables
    'INT',
    # 'NODENAME',
    'CODE'
)


t_BEHAVIOR = 'behavior'
t_SEQUENCE = 'sequence'
t_SELECTOR = 'selector'
t_PROBSELECTOR = 'prob_selector'
t_PARALLEL = 'parallel'
t_DECORATOR = 'decorator'
t_CONDITION = 'condition'
t_ACTION = 'action'
t_EXPRESSION = 'expression'

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CODE(t):
    r'\$\$(.|\n)+?\$\$'
    print(t)
    return t

def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)


lexer = lex.lex()

lexer.input(
    """
    behavior : [ 
        sequence: [
            parallel : 10 [
                
            ]
        ]
    ]

    condition : $$
        ola
    $$

    action : $$
        ola
    $$
    """
)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)