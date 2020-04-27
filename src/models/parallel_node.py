from models.control_flow_node import ControlFlowNode

class Parallel(ControlFlowNode):
    """
    Class that represents a parallel node.
    """

    def __init__(self, name, children, success_rate):
        super().__init__(name, children)
        self.success_rate = success_rate
    

    def __str__(self):
        text = "sequence: " + str(self.name) + " " + str(self.success_rate) + " [\n"
        for child in self.children:
            text += "\t" + str(child).replace('\n', '\n\t') + "\n"
        text += "]"
        return text

    def to_latex_str(self, indent):
        text = indent * 4 * ' ' 
        text += "[\\parallel\n"
        for child in self.children:
            text += child.to_latex_str(indent=indent+1)
        text += indent * 4 * ' ' + "]\n"
        return text

    def to_python_string(self, indent):

        text = ""
        children_str = "[\n"
        for child in self.children:
            text += child.to_python_string(indent) + "\n"
            children_str += (indent + 2) * 4 * ' ' + "{}_NODE,\n".format(child.name.upper())

        children_str += ((indent + 1) * 4 * ' ') + "]\n"

        text += indent * 4 * ' ' 
        text += "%s_NODE = {\n" % (self.name.upper())
        indent += 1

        attrs = {
            "name": self.name,
            "type": "parallel",
        }

        for key,value in attrs.items():
            text += indent * 4 * ' ' + '"{}": "{}",\n'.format(key, value)

        text += indent * 4 * ' ' + '"children": {}'.format(children_str)

        indent -= 1
        text += indent * 4 * ' ' + '}\n'
        return text