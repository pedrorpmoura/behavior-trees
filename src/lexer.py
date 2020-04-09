import ply.lex as lex
import sys
import re




literals = "({[]}),:%"
t_ignore = " \n\t"

tokens = (
    'RIGHTARROW',
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
    'INVERTER',
    'MAXTRIES',
    'MAXSECONDS',

     # variables
    'INT',
    'VAR',
    'NODENAME',
    'CODE'
)

t_RIGHTARROW = r'->'
t_DOUBLEPERCENTAGE = r'%%'

t_BEHAVIOR      = r'\bbehavior\b'
t_SEQUENCE      = r'\bsequence\b'
t_SELECTOR      = r'\bselector\b'
t_PROBSELECTOR  = r'\bprob_selector\b'
t_PARALLEL      = r'\bparallel\b'
t_DECORATOR     = r'\bdecorator\b'
t_CONDITION     = r'\bcondition\b'
t_ACTION        = r'\baction\b'
t_INVERTER      = r'\bINVERTER\b'
t_MAXTRIES      = r'\bMAXTRIES\b'
t_MAXSECONDS    = r'\bMAXSECONDS\b'
t_VAR           = r'\$\w+'
t_NODENAME      = r'\b\w+\b'

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_CODE(t):
    r'%%(.|\n)+'
    t.value = t.value[2:]
    return t


def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)


lexer = lex.lex()

lexer.input(
    """
    behavior : [ 
        sequence: [
            condition : $CONDITION2,
            parallel : 10 [
                action : $ACTION1,
                action : $ACTION2
            ]
        ],
        prob_selector : [
            $EXPRESSION1 -> sequence : [
            condition : $CONDITION1
            ],
            $EXPRESSION2 -> sequence : [
                action: $action1
            ]
        ]
    ]s
    """
)

#while True:
#    tok = lexer.token()
#    if not tok:
#        break
#    print(tok)