from models.control_flow_node import ControlFlowNode

class ProbSelector(ControlFlowNode):
    """
    Class that represents a prob_selector node.
    """

    def __init__(self, name, children):
        super().__init__(name, children)
    
    def __str__(self):
        text = "prob_selector: " + str(self.name) + " [\n"
        for child in self.children:
            text += "\t" + str(child).replace('\n', '\n\t') + "\n"
        text += "]"
        return text

    def to_latex_str(self, indent):
        text = indent * 4 * ' ' 
        text += "[\\probselector\n"
        for child in self.children:
            text += child.to_latex_str(indent=indent+1)
        text += indent * 4 * ' ' + "]\n"
        return text

    def to_python_string(self, indent):

        text = ""
        children_str = "[\n"
        probs = "[\n"
        for child in self.children:
            text += child.to_python_string(indent) + "\n"
            children_str += (indent + 2) * 4 * ' ' + '{}_NODE,\n'.format(child.node.name.upper())
            probs += (indent + 2) * 4 * ' ' + '{},\n'.format(child.expression.upper())

        children_str += ((indent + 1) * 4 * ' ') + "],\n"
        probs += ((indent + 1) * 4 * ' ') + "]\n"

        text += indent * 4 * ' ' 
        text += "%s_NODE = {\n" % (self.name.upper())
        indent += 1

        attrs = {
            "name": self.name,
            "type": "prob_selector",
        }

        for key,value in attrs.items():
            text += indent * 4 * ' ' + '"{}": "{}",\n'.format(key, value)

        text += indent * 4 * ' ' + '"children": {}'.format(children_str)
        text += indent * 4 * ' ' + '"probs": {}'.format(probs)

        indent -= 1
        text += indent * 4 * ' ' + '}\n'
        return text


class ProbNode():
    """
    Class that represents a prob_node.
    """

    def __init__(self, expression, node):
        self.expression = expression[1:]
        self.code_expression = None
        self.node = node
    
    def __str__(self):
        text =  str(self.expression) + " -> " + str(self.node)
        return text

    def check_execution_nodes(self, function_list):
        if self.expression not in function_list:
            return self.expression
        
        self.code_expression = function_list[self.expression]
        child_result = self.node.check_execution_nodes(function_list)
        if child_result != True:
            return child_result
        
        return True

    def to_latex_str(self, indent):
        text = indent * 4 * ' ' 
        text += "\\probnode{$" + str(self.expression) + "$}"
        text += self.to_latex_str(indent=indent)[(indent*4) + 1:-2]
        text += indent * 4 * ' ' + "]\n"
        return text

    def to_python_string(self, indent):
        text = indent * 4 * ' ' 
        text += "%s = {\n" % (self.expression.upper())
        indent += 1

        attrs = {
            "name": self.expression,
            "type": "expression",
            "function": self.expression,
        }

        for key,value in attrs.items():
            text += indent * 4 * ' ' + '"{}": "{}",\n'.format(key, value)

        indent -= 1
        text += indent * 4 * ' ' + '}\n\n'
        text += self.node.to_python_string(indent)
        return text