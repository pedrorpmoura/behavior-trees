from models.node import Node

class ControlFlowNode(Node):
    """
    Class that represents a control flow node.
    """

    def __init__(self, name, children):
        super().__init__(self)
        self.children = children