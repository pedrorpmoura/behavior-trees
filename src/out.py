


def cond1(entity):
    return True

def cond2(entity):
    return True

def cond3(entity):
    return True


def e1(entity):
    return 0.5

def e2(entity):
    return 0.5

def e3(entity):
    return 0.5

def e4(entity):
    return 0.5

def action1(entity):
    return RUNNING

def action2(entity):
    return RUNNING

def action3(entity):
    return RUNNING

    CONDITION0_NODE = {
        "name": "condition0",
        "type": "condition",
        "function": "cond1",
    }

    E1 = {
        "name": "e1",
        "type": "expression",
        "function": "e1",
    }

    ACTION0_NODE = {
        "name": "action0",
        "type": "action",
        "function": "action3",
    }

    E2 = {
        "name": "e2",
        "type": "expression",
        "function": "e2",
    }

    E3 = {
        "name": "e3",
        "type": "expression",
        "function": "e3",
    }

    CONDITION1_NODE = {
        "name": "condition1",
        "type": "condition",
        "function": "cond1",
    }

    CONDITION2_NODE = {
        "name": "condition2",
        "type": "condition",
        "function": "cond1",
    }

    SELECTOR0_NODE = {
        "name": "selector0",
        "type": "selector",
        "memory": "False",
        "children": [
            CONDITION1_NODE,
            CONDITION2_NODE,
        ]
    }

    E4 = {
        "name": "e4",
        "type": "expression",
        "function": "e4",
    }

    ACTION1_NODE = {
        "name": "action1",
        "type": "action",
        "function": "action2",
    }
    INVERTER0_NODE = {
        "name": "inverter0",
        "type": "inverter",
        "children": [
            ACTION1_NODE,
        ]
    }

    ACTION2_NODE = {
        "name": "action2",
        "type": "action",
        "function": "action3",
    }

    PARALLEL0_NODE = {
        "name": "parallel0",
        "type": "parallel",
        "success_rate": "1",
        "memory": "False",
        "children": [
            INVERTER0_NODE,
            ACTION2_NODE,
        ]
    }

    PROB_SELECTOR1_NODE = {
        "name": "prob_selector1",
        "type": "prob_selector",
        "memory": "True",
        "children": [
            SELECTOR0_NODE,
            PARALLEL0_NODE,
        ],
        "probs": [
            E3,
            E4,
        ]
    }

    PROB_SELECTOR0_NODE = {
        "name": "prob_selector0",
        "type": "prob_selector",
        "memory": "False",
        "children": [
            ACTION0_NODE,
            PROB_SELECTOR1_NODE,
        ],
        "probs": [
            E1,
            E2,
        ]
    }

    SEQUENCE0_NODE = {
        "name": "sequence0",
        "type": "sequence",
        "memory": "True",
        "children": [
            CONDITION0_NODE,
            PROB_SELECTOR0_NODE,
        ]
    }

    ROOT_NODE = SEQUENCE0_NODE