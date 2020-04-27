READY   = 0
SUCCESS = 1
FAILURE = 2
RUNNING = 3




CONDITION1_NODE = {
    "name": "condition1",
    "type": "condition",
    "function": "condition1",
    "state": READY
}

ACTION1_NODE = {
    "name": "action1",
    "type": "action",
    "function": "action1",
    "state": READY
}

ACTION2_NODE = {
    "name": "action2",
    "type": "action",
    "function": "action2",
    "state": READY
}

SEL_NODE = {
    "name": "sel",
    "type": "selector",
    "children": [
        ACTION1_NODE,
        CONDITION1_NODE
    ],
    "state": READY
}

SEQ2_NODE = {
    "name": "seq2",
    "type": "sequence",
    "children": [
        CONDITION1_NODE,
        SEL_NODE
    ],
    "state": READY
}

ROOT_NODE = SEQ2_NODE

class Simulator:

    def __init__(self, tree, entity):
        self.tree = tree
        self.entity = entity
    
    def tick(self):
        self.tree['state'] = self.run(self.tree)


    def run(self, tree):
        if tree['type'] == 'sequence':
            return self.run_sequence_node(tree)

        if tree['type'] == 'selector':
            return self.run_selector_node(tree)

        if tree['type'] == 'action':
            return self.run_action_node(tree)

        if tree['type'] == 'condition':
            return self.run_condition_node(tree)

    def run_action_node(self, tree):
        return SUCCESS 

    def run_condition_node(self, tree):
        return FAILURE

    def run_sequence_node(self, tree):
        for c in tree['children']:
            returned_state = self.run(c)
            if returned_state != SUCCESS:
                return returned_state
        
        return SUCCESS


    def run_selector_node(self, tree):
        for c in tree['children']:
            returned_state = self.run(c)
            if returned_state != FAILURE:
                return returned_state
        
        return FAILURE

    def run_prob_selector_node(self):
        pass

    def run_parallel_node(self):
        pass

    def run_decorator_node(self):
        pass

    

S = Simulator(ROOT_NODE, {})
S.tick()
print(S.tree['state'])