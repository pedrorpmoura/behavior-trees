from models.control_flow_node import ControlFlowNode

class Parallel(ControlFlowNode):
    """
    Class that represents a parallel node.
    """

    def __init__(self, name, children):
        super().__init__(self, name, children)