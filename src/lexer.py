import ply.lex as lex
import sys
import re


tokens = (
    # ponctuation
    'LBRACKET',
    'RBRACKET',
    'LCURLYBRACKET',
    'RCURLYBRACKET',
    'LSQUAREBRACKET',
    'RSQUAREBRACKET',
    'COLON',
    'COMMA',
    'DOLLAR',
    'DOUBLEPERCENTAGE',
    
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

    # variables
    'INT',
    'CODE',
    'NODENAME'
)


t_ignore = ' \n\t'


def t_LBRACKET(t):
    r'\('
    return t

def t_RBRACKET(t):
    r'\)'
    return t

def t_LCURLYBRACKET(t):
    r'\{'
    return t

def t_RCURLYBRACKET(t):
    r'\('
    return t

def t_LSQUAREBRACKET(t):
    r'\['
    return t

def t_RSQUAREBRACKET(t):
    r'\]'
    return t

def t_COLON(t):
    r'\:'
    return t

def t_COMMA(t):
    r'\,'
    return t

def t_DOLLAR(t):
    r'\$'
    return t

def t_DOUBLEPERCENTAGE(t):
    r'%%'
    return t



def t_BEHAVIOR(t):
    r'behavior'
    return t

def t_SEQUENCE(t):
    r'sequence'
    return t

def t_SELECTOR(t):
    r'selector'
    return t

def t_PROBSELECTOR(t):
    r'prob_selector'
    return t

def t_PARALLEL(t):
    r'parallel'
    return t

def t_DECORATOR(t):
    r'decorator'
    return t

def t_CONDITION(t):
    r'condition'
    return t

def t_ACTION(t):
    r'action'
    return t

def t_EXPRESSION(t):
    r'expression'
    return t



def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NODENAME(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = 'NODENAME'
    return t

def t_CODE(t):
     r'.+'
     t.type = 'CODE'
     return t

def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)



lexer = lex.lex()
lexer.input("""
    behavior: {

        sequence : [
            decorator: INVERTER [
                NODE
            ],
            condition: $CONDITION,
            parallel: N [
                sequence: [

                ]
            ]
        ]
    }

    condition CONDITION : {
        x == y
    }
""")

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)