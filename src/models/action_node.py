from models.execution_node import ExecutionNode

class Action(ExecutionNode):
    """
    Class that represents an action node.
    """

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "action: " + self.name

    def to_latex_str(self, indent):
        text = indent * 4 * ' ' 
        text += "[\\action{"
        text += self.name.replace("_", " ")
        text += "}]\n"
        return text