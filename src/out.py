# -*- encoding: utf8 -*-
READY   = 'READY'
SUCCESS = 'SUCCESS'
FAILURE = 'FAILURE'
RUNNING = 'RUNNING'

import json
import numpy as np




def sees_player(patroller):
    from math import sqrt
    player_x = patroller['player']['x']
    player_y = patroller['player']['y']

    patroller_x = patroller['x']
    patroller_y = patroller['y']

    if sqrt(patroller_x ** 2 - player_x** 2 + patroller_y**2 - player_y**2) <= patroller['vision_radius']:
        return SUCCESS

    return FAILURE


def activate_alarm(patroller):
    print("ALARM ACTIVATED!!")
    patroller['alarm_activated'] = True
    return SUCCESS


def player_dead(patroller):
    if patroller['player']['hp'] == 0:
        return SUCCESS
    return FAILURE


def fight_player(patroller):
    patroller['player']['hp'] -= 10
    return RUNNING


def run(patroller):
    patroller['x'] = patroller['x'] - 10
    patroller['y'] = patroller['y'] - 10

    print("Running away from player!")
    return RUNNING


def patrol(patroller):
    patroller['x'] = patroller['x'] + 10
    patroller['y'] = patroller['y'] + 10
    return RUNNING


def e1(patroller):
    return patroller['guts'] / 10

def e2(patroller):
    return 1 - patroller['guts'] / 10



class Simulator:

    CONDITION0_NODE = {
        "name": "condition0",
        "type": "condition",
        "function": "sees_player",
    }

    ACTION0_NODE = {
        "name": "action0",
        "type": "action",
        "function": "activate_alarm",
    }

    E1 = {
        "name": "e1",
        "type": "expression",
        "function": "e1",
    }

    CONDITION1_NODE = {
        "name": "condition1",
        "type": "condition",
        "function": "player_dead",
    }
    INVERTER0_NODE = {
        "name": "inverter0",
        "type": "inverter",
        "children": [
            CONDITION1_NODE,
        ]
    }

    ACTION1_NODE = {
        "name": "action1",
        "type": "action",
        "function": "fight_player",
    }

    SEQUENCE0_NODE = {
        "name": "sequence0",
        "type": "sequence",
        "memory": "False",
        "children": [
            INVERTER0_NODE,
            ACTION1_NODE,
        ]
    }

    E2 = {
        "name": "e2",
        "type": "expression",
        "function": "e2",
    }

    CONDITION2_NODE = {
        "name": "condition2",
        "type": "condition",
        "function": "sees_player",
    }

    ACTION2_NODE = {
        "name": "action2",
        "type": "action",
        "function": "run",
    }

    SEQUENCE1_NODE = {
        "name": "sequence1",
        "type": "sequence",
        "memory": "False",
        "children": [
            CONDITION2_NODE,
            ACTION2_NODE,
        ]
    }

    PROB_SELECTOR0_NODE = {
        "name": "prob_selector0",
        "type": "prob_selector",
        "memory": "True",
        "children": [
            SEQUENCE0_NODE,
            SEQUENCE1_NODE,
        ],
        "probs": [
            E1,
            E2,
        ]
    }

    SEQUENCE2_NODE = {
        "name": "sequence2",
        "type": "sequence",
        "memory": "True",
        "children": [
            CONDITION0_NODE,
            ACTION0_NODE,
            PROB_SELECTOR0_NODE,
        ]
    }

    ACTION3_NODE = {
        "name": "action3",
        "type": "action",
        "function": "patrol",
    }

    SELECTOR0_NODE = {
        "name": "selector0",
        "type": "selector",
        "memory": "False",
        "children": [
            SEQUENCE2_NODE,
            ACTION3_NODE,
        ]
    }

    ROOT_NODE = SELECTOR0_NODE

    def __init__(self, tree, entity):
        self.tree = tree
        self.introduce_states(self.tree)
        self.entity = entity

    def introduce_states(self, tree):
        if 'state' not in tree:
            tree['state'] = READY
        
        if tree['state'] != RUNNING:
            tree['state'] = READY

            if tree['type'] == 'action' or tree['type'] == 'condition':
                pass
            else:
                for c in tree['children']:
                    self.introduce_states(c)


    def tick(self):
        self.introduce_states(self.tree)
        self.tree['state'] = self.run(self.tree)
        


    def run(self, tree):
        index = None

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

            if tree['type'] == 'prob_selector':
                return self.run_prob_selector_node(tree, index)


    def run_action_node(self, tree):
        return globals()[tree['function']](self.entity)
        


    def run_condition_node(self, tree):
        result = globals()[tree['function']](self.entity)
        if result:
            return SUCCESS
        else:
            return FAILURE

    
    def run_sequence_node(self, tree, child_index):
        if child_index is None:
            child_index = 0
        
        if not tree['memory']:
            child_index = 0
        
        for c in tree['children'][child_index:]:
            c['state'] = self.run(c)
            if c['state'] != SUCCESS:
                return c['state']
        
        return SUCCESS


    def run_selector_node(self, tree, child_index):
        if child_index is None:
            child_index = 0

        if not tree['memory']:
            child_index = 0
        
        for c in tree['children'][child_index:]:
            c['state'] = self.run(c)
            if c['state'] != FAILURE:
                return c['state']
        
        return FAILURE


    def run_prob_selector_node(self, tree, child_index):
        if tree['memory']:
            if child_index is not None:
                c = tree['children'][child_index]
                c['state'] = self.run(c)
                if c['state'] != FAILURE:
                    return c['state']

        executed_probs = []
        for p in tree['probs']:
            executed_probs.append(globals()[p['function']](self.entity))
        
        children_indexes = list(range(len(tree['children'])))
        children_indexes = list(np.random.choice(children_indexes, len(children_indexes), 
            replace = False, p = executed_probs))
        
        for i in children_indexes:
            if tree['children'][i]['state'] != FAILURE:
                tree['children'][i]['state'] = self.run(tree['children'][i])
                if tree['children'][i]['state'] != FAILURE:
                    return tree['children'][i]['state']
        
        return FAILURE
          
            
            
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


    def run_inverter_node(self, tree):
        child = tree['children'][0]

        child['state'] = self.run(child)
        if child['state'] == SUCCESS:
            return FAILURE
        
        if child['state'] == FAILURE:
            return SUCCESS

        return RUNNING


    def run_max_tries_node(self, tree):
        
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



S = Simulator(ROOT_NODE, {'hp': 100})
i = 2
while i > 0:
    S.tick()
    #print(S.tree['state'])
    S.print_tree(S.tree)
    i -= 1

    print(S.entity)