from models.node import Node


class ControlFlowNode(Node):
    """
    Class that represents a control flow node.
    """

    def __init__(self, name, children):
        super().__init__(name)
        self.children = children
    

    def verify_definitions(self, definitions):

        for definition in definitions:
            if self.name == '$' + definition.name:
                self.children = definition.children
                self.name = definition.name
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