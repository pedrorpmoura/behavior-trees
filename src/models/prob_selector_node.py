from models.control_flow_node import ControlFlowNode
from models.action_node import Action
from models.condition_node import Condition
from models.sequence_node import Sequence
from models.selector_node import Selector
from models.parallel_node import Parallel
from models.decorator_node import Inverter

class ProbSelector(ControlFlowNode):
    """
    Class that represents a prob_selector node.
    """

    def __init__(self, name, children, memory = False, reference=None):
        super().__init__(name, children, memory, reference)
    
    def __str__(self):
        text = "prob_selector: " + str(self.name) + " [\n"
        for child in self.children:
            text += "\t" + str(child).replace('\n', '\n\t') + "\n"
        text += "]"
        return text

    def to_latex_str(self, indent):
        text = indent * 4 * ' ' 
        if not self.memory :
            text += "[\\probselector\n"
        else:
            text += "[\\memoryprobselector\n"

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
            "memory": self.memory
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

    def verify_definitions(self, definitions):
        self.node.verify_definitions(definitions)

    def to_latex_str(self, indent):
        text = indent * 4 * ' '
        #print(isinstance(self.node, Action))
        if isinstance(self.node, Action):
            print(self.node.reference.replace("_", " "))
            text += "[\\probnodeaction{$" + str(self.expression) + "$}{" + self.node.reference.replace("_", " ") + "}\n"

        elif isinstance(self.node, Condition):
            text += "[\\probnodecondition{$" + str(self.expression) + "$}{" + self.node.reference.replace("_", " ") + "}\n"

        elif isinstance(self.node, Sequence):
            if not self.node.memory:
                text += "[\\probnodesequence{$" + str(self.expression) + "$}\n"
            else:
                text += "[\\probnodememorysequence{$" + str(self.expression) + "$}\n"

            for child in self.node.children:
                text += child.to_latex_str(indent=indent+1)

        elif isinstance(self.node, Selector):
            if not self.node.memory:
                text += "[\\probnodeselector{$" + str(self.expression) + "$}\n"
            else:
                text += "[\\probnodememoryselector{$" + str(self.expression) + "$}\n"
            for child in self.node.children:
                text += child.to_latex_str(indent=indent+1)

        elif isinstance(self.node, ProbSelector):
            if not self.node.memory:
                text += "[\\probnodeprobselector{$" + str(self.expression) + "$}\n"
            else:
                text += "[\\probnodememoryprobselector{$" + str(self.expression) + "$}\n"
            
            for child in self.node.children:
                text += child.to_latex_str(indent=indent+1)


        elif isinstance(self.node, Parallel):
            text += "[\\probnodeparallel{$" + str(self.expression) + "$}{$" + str(self.node.success_rate) +"$}\n"
            for child in self.node.children:
                text += child.to_latex_str(indent=indent+1)
        
        elif isinstance(self.node, Inverter):
            text += "[\\probnodeinverter{$" + str(self.expression) + "$\n}"
            text += self.node.children[0].to_latex_str(indent=indent+1)
                
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