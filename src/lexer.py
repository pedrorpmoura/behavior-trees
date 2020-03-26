import ply.lex as lex
import sys
import re

tokens_generated = (
    'DOLLAR',
    'CODE',
    'COMMA',
    'LSQBRACKET',
    'DECORATOR',
    'ACTION',
    'NODENAME',
    'PROB_SELECTOR',
    'SEQUENCE',
    'KEYWORD',
    'DOUBLEPERCENTAGE',
    'RSQRBRACKET',
    'LEFTBRACKET',
    'RIGHTBRACKET',
    'CONDITION',
    'COLON',
    'BEHAVIOUR',
    'PARALLEL',
    'SELECTOR',
    'LSQRBRACKET'
)

tokens = (
    'BEHAVIOUR',
    'SEQUENCE',
    'SELECTOR',
    'PROB_SELECTOR',
    'PARALLEL',
    'DECORATOR',
    'ACTION',
    'CONDITION',
    'NODENAME',
    'CODE',
    'KEYWORD',
    'DOUBLEPERCENTAGE',
    'COMMA',
)


t_BEHAVIOUR = r'behaviour'
t_SEQUENCE = r'sequence'
t_SELECTOR = r'selector'
t_PROB_SELECTOR = r'prob_selector'
t_PARALLEL = r'parallel'
t_DECORATOR = r'decorator'
t_ACTION = r'action'
t_CONDITION = r'condition'
t_NODENAME = r'[a-zA-Z][a-zA-Z0-9]*'
t_KEYWORD = r'[\[\{\]\}]'
t_CODE = r'.*'
t_DOUBLEPERCENTAGE = r'%%'
t_COMMA = r'\,'


