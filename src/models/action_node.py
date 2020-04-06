from models.execution_node import ExecutionNode

class Action(ExecutionNode):
    """
    Class that represents an action node.
    """

    def __init__(self, name):
        ExecutionNode.__init__(self, name)

    def __str__(self):
        return "Action: " + self.name