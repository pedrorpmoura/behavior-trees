from models.node import Node

class ExecutionNode(Node):
    """
    Class that represents an execution node.
    """

    def __init__(self, name, reference=None):
        super(ExecutionNode, self).__init__(name, reference)
        self.name = self.name
        self.code_function = None

    def verify_definitions(self, definitions):
        pass

    def check_execution_nodes(self, function_list):
        if not self.reference in function_list:
            return self.reference
        
        self.code_function = function_list[self.reference]
        return True
