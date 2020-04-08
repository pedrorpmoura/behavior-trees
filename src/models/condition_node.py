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