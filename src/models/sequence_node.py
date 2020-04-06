from models.control_flow_node import ControlFlowNode

class Sequence(ControlFlowNode):
    """
    Class that represents a sequence node.
    """

    def __init__(self, name, children):
        ControlFlowNode.__init__(self, name, children)
    
    
    def __str__(self):
        text = "sequence: " + str(self.name) + "\n" + "[\n"
        for child in self.children:
            text += "\t" + str(child) + "\n"
        text += "]\n"
        return text
        
        
        
        
        
        
        
        
        