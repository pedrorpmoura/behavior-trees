from models.control_flow_node import ControlFlowNode


class Decorator(ControlFlowNode):
    """
    Class that represents a decorator node. 
    """

    def __init__(self, name, children):        
        super().__init__(name, children)

    def __str__(self):
        text = "decorator: " + str(self.name) + " [\n"
        for child in self.children:
            text += "\t" + str(child).replace('\n', '\n\t') + "\n"
        text += "]"
        return text

    def to_latex_str(self, indent):
        text = indent * 4 * ' ' 
        text += "[\\decorator\n"
        for child in self.children:
            text += child.to_latex_str(indent=indent+1)
        text += indent * 4 * ' ' + "]\n"
        return text

class Inverter(Decorator):
    """
    Class that represents an inverter node.
    """

    def __init__(self, name, children):
        super().__init__(name, children)
    
    def __str__(self):
        text = "inverter: " + str(self.name) + " [\n"
        for child in self.children:
            text += "\t" + str(child).replace('\n', '\n\t') + "\n"
        text += "]"
        return text

    def to_latex_str(self, indent):
        text = indent * 4 * ' ' 
        text += "[\\inverter\n"
        for child in self.children:
            text += child.to_latex_str(indent=indent+1)
        text += indent * 4 * ' ' + "]\n"
        return text


class MaxTries(Decorator):
    """
    Class that represents a max-N-tries node.
    """

    def __init__(self, name, children, N):
        super().__init__(name, children)
        self.N = N
    
    def __str__(self):
        text = "decorator: " + str(self.name) + " " + str(self.N) + " [\n"
        for child in self.children:
            text += "\t" + str(child).replace('\n', '\n\t') + "\n"
        text += "]"
        return text

    def to_latex_str(self, indent):
        text = indent * 4 * ' ' 
        text += "[\\maxtries\n"
        for child in self.children:
            text += child.to_latex_str(indent=indent+1)
        text += indent * 4 * ' ' + "]\n"
        return text


class MaxSeconds(Decorator):
    """
    Class that representes a max-T-seconds node.
    """

    def __init__(self, name, children, T):
        super().__init__(name, children)
        self.T = T
    
    def __str__(self):
        text = "decorator: " + str(self.name) + " " + str(self.T) + " [\n"
        for child in self.children:
            text += "\t" + str(child).replace('\n', '\n\t') + "\n"
        text += "]"
        return text

    def to_latex_str(self, indent):
        text = indent * 4 * ' ' 
        text += "[\\maxseconds\n"
        for child in self.children:
            text += child.to_latex_str(indent=indent+1)
        text += indent * 4 * ' ' + "]\n"
        return text