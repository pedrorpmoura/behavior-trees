import ply.yacc as yacc
import sys
from lexer import *


from models.condition_node import Condition
from models.action_node import Action
from models.selector_node import Selector
from models.sequence_node import Sequence
from models.behavior_node import Behavior

current_index = 0

def p_root1(p):
    '''
    root : behavior CODE
    '''
    behavior = Behavior(p[1], p[2])
    print(str(behavior))


def p_root2(p):
    '''
    root : behavior definitions CODE
    '''
    behavior = Behavior(p[1], p[3])
    behavior.fill_definitions(p[2])
    print(str(behavior))


def p_root4(p):
    '''
    root : definitions behavior CODE
    '''
    behavior = Behavior(p[2], p[3])
    behavior.fill_definitions(p[1])
    print(str(behavior))

def p_behavior(p):
    '''
    behavior : BEHAVIOR ':' '[' node ']'
    '''
    p[0] = p[4]


def p_node_sequence1(p):
    '''
    node : SEQUENCE ':' '[' nodes ']'
    '''
    global current_index
    p[0] = Sequence("sequence" + str(current_index), p[4]) # list of nodes
    current_index += 1


def p_node_sequence2(p):
    '''
    node : SEQUENCE ':' VAR
    '''
    pass


def p_node_selector1(p):
    '''
    node : SELECTOR ':' '[' nodes ']'
    '''
    global current_index
    p[0] = Selector("selector" + str(current_index), p[4]) # list of nodes
    current_index += 1


def p_node_selector2(p):
    '''
    node : SELECTOR ':' VAR
    '''
    p[0] = Selector(p[3], [])

def p_node_prob_selector1(p):
    '''
    node : PROBSELECTOR ':' '[' prob_nodes ']'
    '''
    #p[0] = ProbSelector(p[4]) # list of nodes
    pass


def p_node_prob_selector2(p):
    '''
    node : PROBSELECTOR ':' VAR
    '''
    pass


def p_node_parallel1(p):
    '''
    node : PARALLEL ':' INT '[' nodes ']'
    '''
    p[0] = Parallel(p[4]) # list of nodes


def p_node_parallel2(p):
    '''
    node : PARALLEL ':' VAR
    '''
    pass


def p_node_decorator11(p):
    '''
    node : DECORATOR ':' INVERTER '[' node ']'
    '''
    #p[0] = Decorator(p[3],p[5])
    pass


def p_node_decorator12(p):
    '''
    node : DECORATOR ':' VAR
    '''


def p_node_decorator21(p):
    '''
    node : DECORATOR ':' MAXTRIES '[' node ']'
    '''
    p[0] = Decorator(p[3],p[5])


def p_node_decorator3(p):
    '''
    node : DECORATOR ':' MAXSECONDS '[' node ']'
    '''
    p[0] = Decorator(p[3],p[5])


def p_node_condition(p):
    '''
    node : CONDITION ':' VAR
    '''
    p[0] = Condition(p[3])


def p_node_action(p):
    '''
    node : ACTION ':' VAR
    '''
    p[0] = Action(p[3])


def p_nodes(p):
    '''
    nodes : nodes ',' node
          | node
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_prob_nodes(p):
    '''
    prob_nodes : prob_nodes ',' prob_node
               | prob_node
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_prob_node(p):
    '''
    prob_node : VAR RIGHTARROW node
    '''
    #p[0] = ProbNode(p[1], p[3])
    pass



# DEFINITIONS
def p_definitions(p):
    '''
    definitions : definitions definition
               | definition 
    '''
    p[0] = p[1:]


def p_definition_sequence(p):
    '''
    definition : SEQUENCE VAR ':' '[' nodes ']'
    '''
    p[0] = p[1:]


def p_definition_selector(p):
    '''
    definition : SELECTOR VAR ':' '[' nodes ']'
    '''
    p[0] = p[1:]


def p_definition_prob_selector(p):
    '''
    definition : PROBSELECTOR VAR ':' '[' prob_nodes ']'
    '''
    p[0] = p[1:]


def p_definition_parallel(p):
    '''
    definition : PARALLEL VAR ':' INT '[' nodes ']'
    '''
    p[0] = p[1:]


def p_definition_decorator1(p):
    '''
    definition : DECORATOR VAR ':' INVERTER '[' node ']'
    '''
    p[0] = p[1:]


def p_definition_decorator2(p):
    '''
    definition : DECORATOR VAR ':' MAXTRIES '[' node ']'
    '''
    p[0] = p[1:]


def p_definition_decorator3(p):
    '''
    definition : DECORATOR VAR ':' MAXSECONDS '[' node ']'
    '''
    p[0] = p[1:]



def p_error(p):
    print('Syntax error: ' + p.value + ', type: ' + p.type)

parser = yacc.yacc()

with open('test2.txt', 'r') as f:
    s = f.read()
    parser.parse(s)