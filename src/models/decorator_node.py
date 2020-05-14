from models.control_flow_node import ControlFlowNode


class Decorator(ControlFlowNode):
    """
    Class that represents a decorator node. 
    """

    def __init__(self, name, children, reference=None):        
        super().__init__(name, children, reference)

    def __str__(self):
        text = "decorator: " + str(self.name) + " [\n"
        for child in self.children:
            text += "\t" + str(child).replace('\n', '\n\t') + "\n"
        text += "]"
        return text

    def to_latex_str(self, indent):
        text = indent * 4 * ' ' 
        text += "[\\decorator\n"
        for child in self.children:
            text += child.to_latex_str(indent=indent+1)
        text += indent * 4 * ' ' + "]\n"
        return text


class Inverter(Decorator):
    """
    Class that represents an inverter node.
    """

    def __init__(self, name, children, reference=None):
        super().__init__(name, children, reference)
    
    def __str__(self):
        text = "inverter: " + str(self.name) + " [\n"
        for child in self.children:
            text += "\t" + str(child).replace('\n', '\n\t') + "\n"
        text += "]"
        return text

    def to_latex_str(self, indent):
        text = indent * 4 * ' ' 
        text += "[\\inverter\n"
        for child in self.children:
            text += child.to_latex_str(indent=indent+1)
        text += indent * 4 * ' ' + "]\n"
        return text

    
    def to_python_string(self, indent):

        text = ""
        children_str = "[\n"

        child = self.children[0]
        text += child.to_python_string(indent)
        children_str += (indent + 2) * 4 * ' ' + "{}_NODE,\n".format(child.name.upper())

        children_str += ((indent + 1) * 4 * ' ') + "]\n"

        text += indent * 4 * ' ' 
        text += "%s_NODE = {\n" % (self.name.upper())
        indent += 1

        attrs = {
            "name": self.name,
            "type": "inverter",
        }

        for key,value in attrs.items():
            text += indent * 4 * ' ' + '"{}": "{}",\n'.format(key, value)

        text += indent * 4 * ' ' + '"children": {}'.format(children_str)

        indent -= 1
        text += indent * 4 * ' ' + '}\n'
        return text



class MaxTries(Decorator):
    """
    Class that represents a max-N-tries node.
    """

    def __init__(self, name, children, N):
        super().__init__(name, children)
        self.N = N
    
    def __str__(self):
        text = "decorator: " + str(self.name) + " " + str(self.N) + " [\n"
        for child in self.children:
            text += "\t" + str(child).replace('\n', '\n\t') + "\n"
        text += "]"
        return text

    def to_latex_str(self, indent):
        text = indent * 4 * ' ' 
        text += "[\\maxtries{" + str(self.N) + "}\n"
        for child in self.children:
            text += child.to_latex_str(indent=indent+1)
        text += indent * 4 * ' ' + "]\n"
        return text
    

    def to_python_string(self, indent):
        text = ""
        children_str = "[\n"

        child = self.children[0]
        text += child.to_python_string(indent)
        children_str += (indent + 2) * 4 * ' ' + "{}_NODE,\n".format(child.name.upper())

        children_str += ((indent + 1) * 4 * ' ') + "]\n"

        text += indent * 4 * ' ' 
        text += "%s_NODE = {\n" % (self.name.upper())
        indent += 1

        attrs = {
            "name": self.name,
            "type": "max_tries",
            "tries": self.N
        }

        for key,value in attrs.items():
            text += indent * 4 * ' ' + '"{}": "{}",\n'.format(key, value)

        text += indent * 4 * ' ' + '"children": {}'.format(children_str)

        indent -= 1
        text += indent * 4 * ' ' + '}\n'
        return text


class MaxSeconds(Decorator):
    """
    Class that representes a max-T-seconds node.
    """

    def __init__(self, name, children, T):
        super().__init__(name, children)
        self.T = T
    
    def __str__(self):
        text = "decorator: " + str(self.name) + " " + str(self.T) + " [\n"
        for child in self.children:
            text += "\t" + str(child).replace('\n', '\n\t') + "\n"
        text += "]"
        return text

    def to_latex_str(self, indent):
        text = indent * 4 * ' ' 
        text += "[\\maxseconds\n"
        for child in self.children:
            text += child.to_latex_str(indent=indent+1)
        text += indent * 4 * ' ' + "]\n"
        return text