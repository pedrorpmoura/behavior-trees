
STATE_READY = 0
STATE_VISITING = 1
STATE_FAILED = 2
STATE_RUNNING = 3
STATE_COMPLETE = 4


def action1(entity):
    entity['we'] -= 10
    return STATE_COMPLETE

def condition1(entity):
    if entity['hp'] == 100:
        return STATE_FAILED
    return STATE_COMPLETE

def action2(entity):
    pass

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

    ROOT_NODE = {
        "name": "root",
        "type" : "sequence", "children": [
            CONDITION1_NODE,
            SEL_NODE,
        ], 
        "parent": None
    }

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
            return None, STATE_COMPLETE
        if parent["type"] == "sequence":
            if len(parent["children"]) == parent["children"].index(self.current_node) + 1:
                # Done with sequence, lets go up
                return parent, STATE_COMPLETE
            self.counter = parent["children"].index(self.current_node) + 1
            return parent["children"][self.counter], STATE_READY
        elif parent["type"] == "selector":
            self.counter = 0
            return parent, STATE_COMPLETE


    def get_failed_next_node(self):
        parent = self.current_node["parent"]
        if parent == None:
            return None, STATE_FAILED
        
        if parent["type"] == "sequence":
            self.counter = 0
            return parent, STATE_FAILED
        elif parent["type"] == "selector":
            if len(parent["children"]) == parent["children"].index(self.current_node) + 1:
                # Done with sequence, lets go up
                return parent, STATE_FAILED
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
        elif self.current_state == STATE_COMPLETE:
            # Done, lets go to the next one.
            self.current_node, self.current_state = self.get_success_next_node()
            if self.current_node == None:
                self.print_verbose("Done!")
            else:
                self.print_verbose("Completed last stuff, let's proceed to node %s" % self.current_node["name"])
        elif self.current_state == STATE_FAILED:
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

