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
                definitions.remove(definition)
        
        for child in self.children:
            child.verify_definitions(definitions)
