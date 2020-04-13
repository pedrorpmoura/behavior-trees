from models.execution_node import ExecutionNode

class Condition(ExecutionNode):
    """
    Class that represents a condition node.
    """

    #def __init__(self, name):
    #    ExecutionNode.__init__(self, name)
    
    def __init__(self, name):
        super().__init__(name)
    
    def __str__(self):
        return "condition: " + self.name

    def to_latex_str(self, indent):
        text = indent * 4 * ' ' 
        text += "[\\condition{"
        text += self.name.replace("_", " ")
        text += "}]\n"
        return text