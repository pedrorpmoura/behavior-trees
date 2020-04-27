import ply.yacc as yacc
import sys
from lexer import *


from models.condition_node import Condition
from models.action_node import Action
from models.selector_node import Selector
from models.sequence_node import Sequence
from models.decorator_node import Decorator, Inverter, MaxTries, MaxSeconds
from models.parallel_node import Parallel
from models.prob_selector_node import ProbSelector, ProbNode
from models.behavior_node import Behavior


current_indexes = {
    'sequence': 0,
    'selector': 0,
    'prob_selector': 0,
    'parallel': 0,
    'inverter': 0,
    'max_tries': 0,
    'max_seconds': 0,
    'action': 0,
    'condition': 0
}

def p_root1(p):
    '''
    root : behavior CODE
    '''
    behavior = Behavior(p[1])
    behavior.set_code(p[2])
    #print(str(behavior))
    #print(behavior.to_latex_str())
    p[0] = behavior

def p_root2(p):
    '''
    root : behavior definitions CODE
    '''
    behavior = Behavior(p[1])
    behavior.fill_definitions(p[2])
    behavior.set_code(p[3])
    #print(str(behavior))
    #print(behavior.to_latex_str())
    p[0] = behavior

def p_root3(p):
    '''
    root : definitions behavior CODE
    '''
    behavior = Behavior(p[2], p[3])
    behavior.fill_definitions(p[1])
    behavior.set_code(p[3])
    #print(str(behavior))
    #print(behavior.to_latex_str())
    p[0] = behavior


def p_behavior(p):
    '''
    behavior : BEHAVIOR ':' '[' node ']'
    '''
    p[0] = p[4]


def p_node_sequence1(p):
    '''
    node : SEQUENCE ':' '[' nodes ']'
    '''
    global current_indexes
    p[0] = Sequence("sequence" + str(current_indexes['sequence']), p[4]) # list of nodes
    current_indexes['sequence'] += 1


def p_node_sequence2(p):
    '''
    node : SEQUENCE ':' VAR
    '''
    p[0] = Sequence(p[3], [])


def p_node_selector1(p):
    '''
    node : SELECTOR ':' '[' nodes ']'
    '''
    global current_indexes
    p[0] = Selector("selector" + str(current_indexes['selector']), p[4]) # list of nodes
    current_indexes['selector'] += 1


def p_node_selector2(p):
    '''
    node : SELECTOR ':' VAR
    '''
    p[0] = Selector(p[3], [])


def p_node_prob_selector1(p):
    '''
    node : PROBSELECTOR ':' '[' prob_nodes ']'
    '''
    global current_indexes
    p[0] = ProbSelector("prob_selector" + str(current_indexes['prob_selector']), p[4]) # list of nodes
    current_indexes['prob_selector'] += 1


def p_node_prob_selector2(p):
    '''
    node : PROBSELECTOR ':' VAR
    '''
    p[0] = ProbSelector(p[3], [])


def p_node_parallel1(p):
    '''
    node : PARALLEL ':' INT '[' nodes ']'
    '''
    global current_indexes
    p[0] = Parallel("parallel" + str(current_indexes['parallel']), p[5], p[3])
    current_indexes['parallel'] += 1


def p_node_parallel2(p):
    '''
    node : PARALLEL ':' VAR
    '''
    p[0] = Parallel(p[3], [], None)


def p_node_decorator11(p):
    '''
    node : DECORATOR ':' INVERTER '[' node ']'
    '''
    global current_indexes
    p[0] = Inverter("inverter" + str(current_indexes['inverter']), [p[5]])
    current_indexes['inverter'] += 1


def p_node_decorator12(p):
    '''
    node : DECORATOR ':' MAXTRIES '(' INT ')' '[' node ']'
    '''
    global current_indexes
    p[0] = MaxTries("max_tries" + str(current_indexes['max_tries']), [p[8]], N = p[5])
    current_indexes['max_tries'] += 1


def p_node_decorator13(p):
    '''
    node : DECORATOR ':' MAXSECONDS '(' INT ')' '[' node ']'
    '''
    global current_indexes
    p[0] = MaxSeconds("max_seconds" + str(current_indexes['max_seconds']), [p[8]], T = p[5])
    current_indexes['max_seconds'] += 1


def p_node_decorator2(p):
    '''
    node : DECORATOR ':' VAR
    '''
    p[0] = Decorator(p[3], [])


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
    p[0] = ProbNode(p[1], p[3])



# DEFINITIONS
def p_definitions(p):
    '''
    definitions : definitions definition
               | definition 
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]


def p_definition_sequence(p):
    '''
    definition : SEQUENCE NODENAME ':' '[' nodes ']'
    '''
    p[0] = Sequence(p[2], p[5])


def p_definition_selector(p):
    '''
    definition : SELECTOR NODENAME ':' '[' nodes ']'
    '''
    p[0] = Selector(p[2], p[5])


def p_definition_prob_selector(p):
    '''
    definition : PROBSELECTOR NODENAME ':' '[' prob_nodes ']'
    '''
    p[0] = ProbSelector(p[2], p[5])


def p_definition_parallel(p):
    '''
    definition : PARALLEL NODENAME ':' INT '[' nodes ']'
    '''
    p[0] = Parallel(p[2], p[6], p[4])


def p_definition_decorator1(p):
    '''
    definition : DECORATOR NODENAME ':' INVERTER '[' node ']'
    '''
    p[0] = Inverter(p[2], [p[6]])


def p_definition_decorator2(p):
    '''
    definition : DECORATOR NODENAME ':' MAXTRIES '(' INT ')' '[' node ']'
    '''
    p[0] = MaxTries(p[2], [p[9]], p[6])


def p_definition_decorator3(p):
    '''
    definition : DECORATOR NODENAME ':' MAXSECONDS '(' INT ')' '[' node ']'
    '''
    p[0] = MaxSeconds(p[2], [p[9]], p[6])


def p_error(p):
    print('Syntax error: ' + p.value + ', type: ' + p.type)


if __name__ == '__main__':
    parser = yacc.yacc()
    import sys
    file = "test2.txt"
    with open(file, 'r') as f:
        s = f.read()
        behavior = parser.parse(s)
        if len(sys.argv) == 0:
            print("Usage: -l or -p")
            sys.exit(-1)

        if "-l" in sys.argv or "--latex" in sys.argv:
            print("Latex:")
            with open('behavior.tex', 'w') as latex_file:
                latex_file.write(behavior.to_latex_str())

        if "-p" in sys.argv or "--python" in sys.argv:
            import os
            filename = os.path.splitext(file)[0]
            py_output = behavior.to_python_string()
            with open(filename + ".generated.py", 'w') as python_file:
                python_file.write(py_output)