from models.node import ControlFlowNode

class Selector(ControlFlowNode):
    """
    Class that represents a selector node.
    """

    def __init__(self, name, children):
        super().__init__(self, name, children)