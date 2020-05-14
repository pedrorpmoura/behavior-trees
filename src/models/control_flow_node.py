from models.node import Node


class ControlFlowNode(Node):
    """
    Class that represents a control flow node.
    """

    def __init__(self, name, children, memory = False, reference=None):
        super(ControlFlowNode, self).__init__(name, reference)
        self.children = children
        self.memory = memory
    

    def verify_definitions(self, definitions):

        for definition in definitions:
            if not self.reference:
                continue
            if self.reference == definition.name:
                self.children = definition.children
                definitions.remove(definition)
        
        for child in self.children:
            child.verify_definitions(definitions)


    def check_execution_nodes(self, function_list):
        for child in self.children:
            child_result = child.check_execution_nodes(function_list)
            if child_result != True:
                return child_result

        return True
    
    def get_children(self):
        return self.children

    def to_latex_str(self):
        text = ""