import ply.yacc as yacc
import sys
from lexer import *


def p_root(p):
    '''
    root : behavior definitions 
         | definitions behavior
    '''
    print(p[1])


def p_behavior(p):
    '''
    behavior : BEHAVIOR LCURLYBRACKET node RCURLYBRACKET
    '''
    p[0] = ' '.join(p[1:])


def p_node(p):
    '''
    node : sequence
         | selector
         | prob_selector
         | parallel
         | decorator
         | action
         | condition
    '''
    p[0] = p[1]


def p_sequence(p):
    '''
    sequence : SEQUENCE COLON LSQUAREBRACKET nodes RSQUAREBRACKET
    '''
    p[0] = ' '.join(p[1:])


def p_selector(p):
    '''
    selector : SELECTOR COLON LSQUAREBRACKET nodes RSQUAREBRACKET
    '''
    p[0] = ' '.join(p[1:])


def p_prob_selector(p):
    '''
    prob_selector : PROBSELECTOR COLON LSQUAREBRACKET prob_nodes RSQUAREBRACKET
    '''
    p[0] = ' '.join(p[1:])


def p_parallel(p):
    '''
    parallel : PARALLEL COLON INT LSQUAREBRACKET nodes RSQUAREBRACKET
    '''
    p[0] = ' '.join(p[1:])


def p_decorator(p):
    '''
    decorator : DECORATOR COLON policy LSQUAREBRACKET node RSQUAREBRACKET
    '''
    p[0] = ' '.join(p[1:])


def p_nodes(p):
    '''
    nodes : nodes COMMA node
          | node
    '''
    p[0] = ' '.join(p[1:])


def p_prob_nodes(p):
    '''
    prob_nodes : prob_nodes COMMA prob_node
               | prob_node
    '''
    p[0] = ' '.join(p[1:])


def p_prob_node(p):
    '''
    prob_node : var RIGHTARROW node
    '''
    p[0] = ' '.join(p[1:])


def p_policy(p):
    '''
    policy : INVERTER
           | MAXTRIES
           | MAXSECONDS
    '''
    p[0] = ' '.join(p[1:])

def p_condition(p):
    '''
    condition : CONDITION COLON var
    '''
    p[0] = ' '.join(p[1:])



def p_action(p):
    '''
    action : ACTION COLON var
    '''
    p[0] = ' '.join(p[1:])


def p_var(p):
    '''
    var : DOLLAR NODENAME
    '''
    p[0] = ' '.join(p[1:])



# DEFINITIONS
def p_definitions(p):
    '''
    definitions : definitions definition
               | definition
    '''
    p[0] = ' '.join(p[1:])


def p_definition(p):
    '''
    definition : sequence_def
              | selector_def
              | prob_selector_def
              | parallel_def
              | decorator_def
              | action_def
              | condition_def
              | expression_def
    '''
    p[0] = ' '.join(p[1:])


def p_sequence_def(p):
    '''
    sequence_def : SEQUENCE NODENAME COLON LSQUAREBRACKET nodes RSQUAREBRACKET
    '''
    p[0] = ' '.join(p[1:])


def p_selector_def(p):
    '''
    selector_def : SELECTOR NODENAME COLON LSQUAREBRACKET nodes RSQUAREBRACKET
    '''
    p[0] = ' '.join(p[1:])


def p_prob_selector_def(p):
    '''
    prob_selector_def : PROBSELECTOR NODENAME COLON LSQUAREBRACKET nodes RSQUAREBRACKET
    '''
    p[0] = ' '.join(p[1:])


def p_parallel_def(p):
    '''
    parallel_def : PARALLEL NODENAME COLON INT LSQUAREBRACKET nodes RSQUAREBRACKET
    '''
    p[0] = ' '.join(p[1:])


def p_decorator_def(p):
    '''
    decorator_def : DECORATOR NODENAME COLON policy LSQUAREBRACKET nodes RSQUAREBRACKET
    '''
    p[0] = ' '.join(p[1:])


def p_condition_def(p):
    '''
    condition_def : CONDITION NODENAME COLON LCURLYBRACKET CODE RCURLYBRACKET
    '''
    p[0] = ' '.join(p[1:])


def p_action_def(p):
    '''
    action_def : ACTION NODENAME COLON LCURLYBRACKET CODE RCURLYBRACKET
    '''
    p[0] = ' '.join(p[1:])


def p_expression_def(p):
    '''
    expression_def : EXPRESSION NODENAME COLON LCURLYBRACKET CODE RCURLYBRACKET
    '''
    p[0] = ' '.join(p[1:])


def p_error(p):
    print('Syntax error: ' + p.value + ', type: ' + p.type)


parser = yacc.yacc()

with open('test.txt', 'r') as f:
    s = f.read()
    parser.parse(s)

# while True:
#     s = input()
#     parser.parse(s)
