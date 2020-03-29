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
    'RIGHTARROW',
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
    'INVERTER',
    'MAXTRIES',
    'MAXSECONDS',

    # variables
    'INT',
    'NODENAME',
    'CODE'
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
    r'\}'
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

def t_RIGHTARROW(t):
    r'\-\>'
    return t

def t_DOLLAR(t):
    r'\$'
    return t

def t_DOUBLEPERCENTAGE(t):
    r'%%'
    return t



def t_BEHAVIOR(t):
    r'\b(behavior)\b'
    return t

def t_SEQUENCE(t):
    r'\b(sequence)\b'
    return t

def t_SELECTOR(t):
    r'\b(selector)\b'
    return t

def t_PROBSELECTOR(t):
    r'\b(prob_selector)\b'
    return t

def t_PARALLEL(t):
    r'\b(parallel)\b'
    return t

def t_DECORATOR(t):
    r'\b(decorator)\b'
    return t

def t_CONDITION(t):
    r'\b(condition)\b'
    return t

def t_ACTION(t):
    r'\b(action)\b'
    return t

def t_EXPRESSION(t):
    r'\b(expression)\b'
    return t

def t_INVERTER(t):
    r'\b(INVERTER)\b'
    return t

def t_MAXTRIES(t):
    r'\b(MAXTRIES)\b'
    return t

def t_MAXSECONDS(t):
    r'\b(MAXSECONDS)\b'
    return t



def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NODENAME(t):
    r'\w[\w\d]*'
    t.type = 'NODENAME'
    return t

def t_CODE(t):
    r'    (.|\n)+'
    t.type = 'CODE'
    return t


def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)



lexer = lex.lex()

lexer.input(
    """
    condition CONDITION : {
        x == y
    }
    """
)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
'''
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
'''
