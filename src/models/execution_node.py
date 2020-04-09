from models.node import Node

class ExecutionNode(Node):
    """
    Class that represents an execution node.
    """

    # def __init__(self, name):
    #     Node.__init__(self, name)

    def __init__(self, name):
        super().__init__(name)


    def verify_definitions(self, definitions):
        pass