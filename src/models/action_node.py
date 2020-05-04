from models.execution_node import ExecutionNode

class Action(ExecutionNode):
    """
    Class that represents an action node.
    """

    def __init__(self, name):
        super(Action, self).__init__(name)

    def __str__(self):
        return "action: " + self.name

    def to_latex_str(self, indent):
        text = indent * 4 * ' ' 
        text += "[\\action{"
        text += self.name.replace("_", " ")
        text += "}]\n"
        return text

    def to_python_string(self, indent):
        text = indent * 4 * ' ' 
        text += "%s_NODE = {\n" % (self.name.upper())
        indent += 1

        attrs = {
            "name": self.name,
            "type": "action",
            "function": self.name,
        }

        for key,value in attrs.items():
            text += indent * 4 * ' ' + '"{}": "{}",\n'.format(key, value)

        indent -= 1
        text += indent * 4 * ' ' + '}\n'
        return text