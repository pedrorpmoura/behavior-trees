from models.control_flow_node import ControlFlowNode

class Sequence(ControlFlowNode):
    """
    Class that represents a sequence node.
    """
    
    def __init__(self, name, children, memory = False, reference=None):
        super(Sequence, self).__init__(name, children, memory, reference)

    def __str__(self):
        text = "sequence: " + str(self.name) + " [\n"
        for child in self.children:
            text += "\t" + str(child).replace('\n', '\n\t') + "\n"
        text += "]"
        return text

    def to_latex_str(self, indent):
        text = indent * 4 * ' ' 
        if not self.memory:
            text += "[\\sequence\n"
        else:
            text += "[\\memorysequence\n"
        
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
            "type": "sequence",
            "memory": self.memory
        }

        for key,value in attrs.items():
            text += indent * 4 * ' ' + '"{}": "{}",\n'.format(key, value)

        text += indent * 4 * ' ' + '"children": {}'.format(children_str)

        indent -= 1
        text += indent * 4 * ' ' + '}\n'
        return text
