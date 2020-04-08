from models.control_flow_node import ControlFlowNode

class Selector(ControlFlowNode):
    """
    Class that represents a selector node.
    """

    def __init__(self, name, children):
        super().__init__(name, children)

    def __str__(self):
        text = "selector: " + str(self.name) + " [\n"
        for child in self.children:
            text += "\t" + str(child).replace('\n', '\n\t') + "\n"
        text += "]"
        return text
            
