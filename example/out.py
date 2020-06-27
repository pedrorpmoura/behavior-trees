# -*- encoding: utf8 -*-
READY   = 'READY'
SUCCESS = 'SUCCESS'
FAILURE = 'FAILURE'
RUNNING = 'RUNNING'

import json
import numpy as np




def ball_found(player):
    print("SIMULATOR: Checking if ball is found")
    return player.ball_found


def ball_within_reach(player):
    print("SIMULATOR: Ball was found... checking if it's within reach")
    return player.ball_within_reach


def grab_ball(player):
    print("SIMULATOR: Ball is within reach... Grabbing ball")
    player.grab_ball()
    return SUCCESS


def approach_ball(player):
    print("SIMULATOR: Ball was found but not within reach, approaching")
    player.approach_ball()
    return RUNNING


def search_ball(player):
    print("SIMULATOR: ball is not found... searching")
    player.search_ball()
    return RUNNING


class Simulator:

    CONDITION0_NODE = {
        "name": "condition0",
        "type": "condition",
        "function": "ball_found",
    }

    CONDITION1_NODE = {
        "name": "condition1",
        "type": "condition",
        "function": "ball_within_reach",
    }

    ACTION1_NODE = {
        "name": "action1",
        "type": "action",
        "function": "grab_ball",
    }

    SEQUENCE1_NODE = {
        "name": "sequence1",
        "type": "sequence",
        "memory": "True",
        "children": [
            CONDITION1_NODE,
            ACTION1_NODE,
        ]
    }

    ACTION2_NODE = {
        "name": "action2",
        "type": "action",
        "function": "approach_ball",
    }

    SELECTOR1_NODE = {
        "name": "selector1",
        "type": "selector",
        "memory": "False",
        "children": [
            SEQUENCE1_NODE,
            ACTION2_NODE,
        ]
    }

    SEQUENCE0_NODE = {
        "name": "sequence0",
        "type": "sequence",
        "memory": "False",
        "children": [
            CONDITION0_NODE,
            SELECTOR1_NODE,
        ]
    }

    ACTION0_NODE = {
        "name": "action0",
        "type": "action",
        "function": "search_ball",
    }

    SELECTOR0_NODE = {
        "name": "selector0",
        "type": "selector",
        "memory": "False",
        "children": [
            SEQUENCE0_NODE,
            ACTION0_NODE,
        ]
    }

    ROOT_NODE = SELECTOR0_NODE

    def __init__(self, entity):
        self.tree = self.ROOT_NODE
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
        
        if tree['memory'] == "False":
            child_index = 0
        
        for c in tree['children'][child_index:]:
            c['state'] = self.run(c)
            if c['state'] != SUCCESS:
                return c['state']
        
        return SUCCESS


    def run_selector_node(self, tree, child_index):
        if child_index is None:
            child_index = 0

        if tree['memory'] == "False":
            child_index = 0
        
        for c in tree['children'][child_index:]:
            c['state'] = self.run(c)
            if c['state'] != FAILURE:
                return c['state']
        
        return FAILURE


    def run_prob_selector_node(self, tree, child_index):
        if tree['memory'] == "True":
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



#S = Simulator(ROOT_NODE, {'hp': 100})
#i = 2
#while i > 0:
#    S.tick()
#    #print(S.tree['state'])
#    S.print_tree(S.tree)
#    i -= 1
#
#    print(S.entity)