READY   = 'READY'
SUCCESS = 'SUCCESS'
FAILURE = 'FAILURE'
RUNNING = 'RUNNING'

import json


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
        ACTION2_NODE,
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

PARALLEL0_NODE = {
    "name": "parallel0",
    "type": "parallel",
    "success_rate": "2",
    "children": [
        ACTION1_NODE,
        ACTION2_NODE,
        CONDITION1_NODE
    ],
    "state": READY
}

ROOT_NODE = PARALLEL0_NODE

class Simulator:

    def __init__(self, tree, entity):
        self.tree = tree
        self.entity = entity
    
    def tick(self):
        self.tree['state'] = self.run(self.tree)


    def run(self, tree):
        index = 0

        if tree['type'] == 'action':
            return self.run_action_node(tree)

        elif tree['type'] == 'condition':
            return self.run_condition_node(tree)

        else:
            if tree['state'] == RUNNING:
                index = self.find_running_child_index(tree)

            if tree['type'] == 'sequence':
                return self.run_sequence_node(tree, index)

            if tree['type'] == 'selector':
                return self.run_selector_node(tree, index)

            if tree['type'] == 'parallel':
                return self.run_parallel_node(tree, int(tree['success_rate']))

        


    def run_action_node(self, tree):

        if tree['name'] == 'action1':
            tree['state'] = FAILURE
        else: 
            tree['state'] = FAILURE

        return tree['state'] 


    def run_condition_node(self, tree):
        tree['state'] = SUCCESS
        return tree['state']

    
    def run_sequence_node(self, tree, child_index):
        for c in tree['children'][child_index:]:
            c['state'] = self.run(c)
            if c['state'] != SUCCESS:
                return c['state']
        
        return SUCCESS


    def run_selector_node(self, tree, child_index):
        for c in tree['children'][child_index:]:
            c['state'] = self.run(c)
            if c['state'] != FAILURE:
                return c['state']
        
        return FAILURE


    def run_prob_selector_node(self):
        pass

    def run_parallel_node(self, tree, M):
        N = len(tree['children'])
        success = 0
        failure = 0
        for c in tree['children']:
            c['state'] = self.run(c)
            if c['state'] == SUCCESS:
                success += 1
            if c['state'] == FAILURE:
                failure += 1

        if success >= M:
            return SUCCESS
        if failure > N - M:
            return FAILURE
        
        return RUNNING

    def run_decorator_node(self):
        pass



    def find_running_child_index(self, tree):
        for i, c in enumerate(tree['children']):
            if c['state'] == RUNNING:
                return i


    def clear_children_state(self, tree):
        for c in tree['children']:
            c['state'] = READY


    def print_tree(self, tree):
        print(json.dumps(tree, indent = 2))

S = Simulator(ROOT_NODE, {})
S.tick()
S.print_tree(S.tree)