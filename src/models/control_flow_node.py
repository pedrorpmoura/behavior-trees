from models.node import Node

class ControlFlowNode(Node):
    """
    Class that represents a control flow node.
    """

    # def __init__(self, name, children):
    #     Node.__init__(self, name)
    #     self.children = children

    
    def __init__(self, name, children):
        super().__init__(name)
        self.children = children
    
    