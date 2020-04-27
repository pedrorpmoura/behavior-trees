from models.node import Node

class ExecutionNode(Node):
    """
    Class that represents an execution node.
    """

    def __init__(self, name):
        super(ExecutionNode, self).__init__(name)
        self.code_function = None

    def verify_definitions(self, definitions):
        self.name = self.name[1:]

    def check_execution_nodes(self, function_list):
        if not self.name in function_list:
            return self.name
        
        self.code_function = function_list[self.name]
        return True
