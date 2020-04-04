import ply.yacc as yacc
import sys
from lexer2 import *


def p_root1(p):
    '''
    root : behavior definitions
    '''
    print(p[1:])


def p_root2(p):
    '''
    root : definitions behavior
    '''
    print(p[1:])


def p_root3(p):
    '''
    root : behavior definitions DOUBLEPERCENTAGE CODE
    '''
    print(p[1:])


def p_root4(p):
    '''
    root : definitions behavior DOUBLEPERCENTAGE CODE
    '''


def p_behavior(p):
    '''
    behavior : BEHAVIOR '[' node ']'
    '''
    p[0] = p[1:]


def p_node_sequence(p):
    '''
    node : SEQUENCE ':' '[' nodes ']'
    '''
    p[0] = p[1:]


def p_node_selector(p):
    '''
    node : SELECTOR ':' '[' nodes ']'
    '''
    p[0] = p[1:]


def p_node_prob_selector(p):
    '''
    node : PROBSELECTOR ':' '[' prob_nodes ']'
    '''
    p[0] = p[1:]


def p_node_parallel(p):
    '''
    node : PARALLEL ':' INT '[' nodes ']'
    '''
    p[0] = p[1:]


def p_node_decorator1(p):
    '''
    node : DECORATOR ':' INVERTER '[' node ']'
    '''
    p[0] = p[1:]


def p_node_decorator2(p):
    '''
    node : DECORATOR ':' MAXTRIES '[' node ']'
    '''
    p[0] = p[1:]


def p_node_decorator3(p):
    '''
    node : DECORATOR ':' MAXSECONDS '[' node ']'
    '''
    p[0] = p[1:]


def p_node_condition(p):
    '''
    node : CONDITION ':' VAR
    '''
    p[0] = p[1:]


def p_node_action(p):
    '''
    node : ACTION ':' VAR
    '''
    p[0] = p[1:]


def p_nodes(p):
    '''
    nodes : nodes ',' node
          | node
    '''
    p[0] = p[1:]


def p_prob_nodes(p):
    '''
    prob_nodes : prob_nodes ',' prob_node
               | prob_node
    '''
    p[0] = p[1:]


def p_prob_node(p):
    '''
    prob_node : VAR RIGHTARROW node
    '''
    p[0] = p[1:]



# DEFINITIONS
def p_definitions(p):
    '''
    definitions : definitions definition
               | definition 
    '''
    p[0] = p[1:]


def p_definition_sequence(p):
    '''
    definitions : SEQUENCE VAR ':' '[' nodes ']'
    '''
    p[0] = p[1:]


def p_definition_selector(p):
    '''
    definitions : SELECTOR VAR ':' '[' nodes ']'
    '''
    p[0] = p[1:]


def p_definition_prob_selector(p):
    '''
    definitions : PROBSELECTOR VAR ':' '[' prob_nodes ']'
    '''
    p[0] = p[1:]


def p_definition_parallel(p):
    '''
    definitions : PARALLEL VAR ':' INT '[' nodes ']'
    '''
    p[0] = p[1:]


def p_definition_decorator1(p):
    '''
    definitions : DECORATOR VAR ':' INVERTER '[' node ']'
    '''
    p[0] = p[1:]


def p_definition_decorator2(p):
    '''
    definitions : DECORATOR VAR ':' MAXTRIES '[' node ']'
    '''
    p[0] = p[1:]


def p_definition_decorator3(p):
    '''
    definitions : DECORATOR VAR ':' MAXSECONDS '[' node ']'
    '''
    p[0] = p[1:]


def p_definition_condition(p):
    '''
    definition : CONDITION NODENAME ':' CODE
    '''
    p[0] = p[1:]


def p_definition_action(p):
    '''
    definition : ACTION NODENAME ':' CODE
    '''
    p[0] = p[1:]


def p_definition_expression(p):
    '''
    definition : EXPRESSION NODENAME ':' CODE
    '''
    p[0] = p[1:]


def p_error(p):
    print('Syntax error: ' + p.value + ', type: ' + p.type)

parser = yacc.yacc()

with open('test.txt', 'r') as f:
    s = f.read()
    parser.parse(s)