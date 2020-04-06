from models.execution_node import ExecutionNode

class Condition(ExecutionNode):
    """
    Class that represents a condition node.
    """

    def __init__(self, name):
        ExecutionNode.__init__(self, name)
    
    def __str__(self):
        return "Condition: " + self.name