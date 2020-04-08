from models.control_flow_node import ControlFlowNode

class ProbSelector(ControlFlowNode):
    """
    Class that represents a prob_selector node.
    """

    def __init__(self, name, children):
        super().__init__(name, children)
    
    def __str__(self):
        text = "prob_selector: " + str(self.name) + " [\n"
        for child in self.children:
            text += "\t" + str(child).replace('\n', '\n\t') + "\n"
        text += "]"
        return text

class ProbNode():
    """
    Class that represents a prob_node.
    """

    def __init__(self, expression, child):
        self.expression = expression
        self.child = child

    
    def __str__(self):
        text =  str(self.expression) + " -> " + str(self.child)
        return text