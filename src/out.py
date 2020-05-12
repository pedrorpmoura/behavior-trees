
def full_hp(entity):
    return entity['hp'] == 100

def sub_hp(entity):
    entity['hp'] -= 10

def add_hp(entity):
    entity['hp'] += 10

    FULL_HP_NODE = {
        "name": "full_hp",
        "type": "condition",
        "function": "full_hp",
    }

    SUB_HP_NODE = {
        "name": "sub_hp",
        "type": "action",
        "function": "sub_hp",
    }

    SEQUENCE0_NODE = {
        "name": "sequence0",
        "type": "sequence",
        "children": [
            FULL_HP_NODE,
            SUB_HP_NODE,
        ]
    }

    ADD_HP_NODE = {
        "name": "add_hp",
        "type": "action",
        "function": "add_hp",
    }
    MAX_TRIES0_NODE = {
        "name": "max_tries0",
        "type": "max_tries",
        "tries": "20",
        "children": [
            ADD_HP_NODE,
        ]
    }

    SELECTOR0_NODE = {
        "name": "selector0",
        "type": "selector",
        "children": [
            SEQUENCE0_NODE,
            MAX_TRIES0_NODE,
        ]
    }

    ROOT_NODE = SELECTOR0_NODE