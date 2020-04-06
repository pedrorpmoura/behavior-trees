from models.node import Node

class ExecutionNode(Node):
    """
    Class that represents an execution node.
    """

    def __init__(self, name):
        Node.__init__(self, name)

