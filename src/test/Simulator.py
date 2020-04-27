# -*- encoding: utf8 -*-
STATE_READY = 0
STATE_VISITING = 1
FAILURE = 2
RUNNING = 3
SUCCESS = 4


def action1(entity):
    entity['we'] -= 10
    return SUCCESS

def condition1(entity):
    if entity['hp'] == 100:
        return FAILURE
    return SUCCESS

def playerGoTo(coords):
    self.player_moving = True
    self.pathfinding = True
    self.destination = coords
    self.path_points = calculatePath()


def update():
    self.behavior_tree.update()
    if self.pathfinding:
        movimento = path_points/len(path.points) + self.current_point 
        self.move(movimento) # isto Ã© que realmente move o jogador

def update():
    physics()
    for entity in self.entities:
        entity.update()

def gameLoop():
    updateLoop()
    render()

def action2(entity):
    castle_coords = (80,80,80)
    if world.playerIsAt(castle_coords):
        return SUCCESS
    
    world.playerGoTo(castle_coords) # NAO BLOQUEIA
    return RUNNING


class Simulator:

    CONDITION1_NODE = {
        "name": "condition1", 
        "type" : "condition", 
        "function": "condition1", 
    }

    ACTION1_NODE = {
        "name": "action1",
        "type": "action", 
        "function": "action1", 
    }
    
    ACTION2_NODE = {
        "name": "action2",
        "type": "action", 
        "function": "action2", 
    }

    SELECTOR1_NODE = { 
        "name": "selector1",
        "type" : "selector", 
        "children": [
            ACTION2_NODE
        ], 
    }

    SEL_NODE = {
        "name": "sel",
        "type" : "selector", 
        "children" : [
            ACTION1_NODE,
            SELECTOR1_NODE,
        ], 
    }

    SEQ2_NODE = {
        "type": "sequence",
        "name": "seq2",
        "children": [
            CONDITION1_NODE,
            SEL_NODE,
        ]
    }

    ROOT_NODE = SEQ2_NODE

    def __init__(self, entity):
        self.nodes_state = {}
        self.fill_parents(self.ROOT_NODE)
        self.ROOT_NODE["parent"] = None
        self.parent_node = None
        self.current_node = None
        self.counter = 0
        self.current_state = STATE_READY
        self.verbose = True
        self.entity = entity


    def fill_parents(self, node): 
        if not "children" in node:
            return
        
        for child_node in node["children"]:
            self.fill_parents(child_node)
            child_node["parent"] = node
        

    def on_tick(self):
        if self.current_node != None:
            self.run_current_node()


    def run_node_selector(self):
        self.counter = 0
        self.current_node = self.current_node["children"][self.counter]
        self.print_verbose("[*]Going to Selector Children %s" % self.current_node["name"])
        return STATE_READY


    def run_node_executor(self):
        try:
            result = globals()[self.current_node["function"]](self.entity)
            self.print_verbose("[*] Executed %s result: %d" % (self.current_node["function"], result))
        except:
            self.print_verbose("Error executing %s" % self.current_node["name"])
        return result


    def run_node_sequence(self):
        self.parent_node = self.current_node
        self.current_node = self.current_node["children"][0]
        self.print_verbose("[*] Going to Sequence Children %s" % self.current_node["name"])
        return STATE_READY


    def get_success_next_node(self):
        parent = self.current_node["parent"]
        if parent == None:
            return None, SUCCESS
        if parent["type"] == "sequence":
            if len(parent["children"]) == parent["children"].index(self.current_node) + 1:
                # Done with sequence, lets go up
                return parent, SUCCESS
            self.counter = parent["children"].index(self.current_node) + 1
            return parent["children"][self.counter], STATE_READY
        elif parent["type"] == "selector":
            self.counter = 0
            return parent, SUCCESS


    def get_failed_next_node(self):
        parent = self.current_node["parent"]
        if parent == None:
            return None, FAILURE
        
        if parent["type"] == "sequence":
            self.counter = 0
            return parent, FAILURE
        elif parent["type"] == "selector":
            if len(parent["children"]) == parent["children"].index(self.current_node) + 1:
                # Done with sequence, lets go up
                return parent, FAILURE
            self.counter = parent["children"].index(self.current_node) + 1
            return parent["children"][self.counter], STATE_READY


    def run_current_node(self):
        node_type = self.current_node["type"]
        node_name = self.current_node["name"]
        self.print_verbose("Current node: [name: %s type: %s]" % (node_name, node_type))
        if self.current_state == STATE_READY:
            if node_type == "selector":
                self.current_state = self.run_node_selector()
            elif node_type == "sequence":
                self.current_state = self.run_node_sequence()
            elif node_type == "condition" or node_type == "action":
                self.current_state = self.run_node_executor()
        elif self.current_state == SUCCESS:
            # Done, lets go to the next one.
            self.current_node, self.current_state = self.get_success_next_node()
            if self.current_node == None:
                self.print_verbose("Done!")
            else:
                self.print_verbose("Completed last stuff, let's proceed to node %s" % self.current_node["name"])
        elif self.current_state == FAILURE:
            # Failed, lets go to the next one.
            self.current_node, self.current_state = self.get_failed_next_node()
            if self.current_node == None:
                self.print_verbose("Done!")
            else:
                self.print_verbose("Failed last stuff, let's proceed to node %s" % self.current_node["name"])


    def print_verbose(self, text):
        if self.verbose:
            print(text)


    def start(self):
        self.current_node = self.ROOT_NODE
        self.current_state = STATE_READY

if __name__ == "__main__":
    entity = {"hp": 100}
    sim = Simulator(entity)
    sim.start()
    for i in range(0, 100):
        sim.on_tick()

    print("Entity after behavior tree executing:")
    print(entity)

