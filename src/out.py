

def expression1():
    return 1

def expression2():
    return 1
    
def action1(x):
    if x == 2:
        return True
    
    return False

    EXPRESSION1 = {
        "name": "expression1",
        "type": "expression",
        "function": "expression1",
    }

    ACTION1_NODE = {
        "name": "action1",
        "type": "action",
        "function": "action1",
    }

    EXPRESSION2 = {
        "name": "expression2",
        "type": "expression",
        "function": "expression2",
    }

    ACTION1_NODE = {
        "name": "action1",
        "type": "action",
        "function": "action1",
    }

    PROB_SELECTOR0_NODE = {
        "name": "prob_selector0",
        "type": "prob_selector",
        "children": [
            ACTION1_NODE,
            ACTION1_NODE,
        ],
        "probs": [
            EXPRESSION1,
            EXPRESSION2,
        ]
    }

    ROOT_NODE = PROB_SELECTOR0_NODE