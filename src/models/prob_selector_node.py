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

    def to_latex_str(self, indent):
        text = indent * 4 * ' ' 
        text += "[\\probselector\n"
        for child in self.children:
            text += child.to_latex_str(indent=indent+1)
        text += indent * 4 * ' ' + "]\n"
        return text

class ProbNode():
    """
    Class that represents a prob_node.
    """

    def __init__(self, expression, node):
        self.expression = expression
        self.node = node
    
    def __str__(self):
        text =  str(self.expression) + " -> " + str(self.node)
        return text

    def to_latex_str(self, indent):
        text = indent * 4 * ' ' 
        text += "\\probnode{$" + str(self.expression) + "$}"
        text += child.to_latex_str(indent=indent)[(indent*4) + 1:-2]
        text += indent * 4 * ' ' + "]\n"
        return text