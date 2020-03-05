from models.control_flow_node import ControlFlowNode

class Sequence(ControlFlowNode):
    """
    Class that represents a sequence node.
    """

    def __init__(self, name, children):
        super().__init__(self, name, children)