
class Behavior:

    def __init__(self, node):
        self.root_node = node
    

    def __str__(self): 
        return str(self.root_node)

    def set_code(self, code):
        self.code_str = code
        self.functions = {}
        globals_generated = {}
        exec(code, globals_generated)
        #print("Code: ")
        for global_f, content in globals_generated.items():
            if global_f[0:2] == '__':
                continue
            
            if not callable(content):
                # Its not a function
                continue

            #print("Found a function: " + global_f)
            self.functions[global_f] = content
        
        self.check_execution_nodes()

    
    def check_execution_nodes(self):
        """ This functions checks if all conditions/actions have a code function """
        result = self.root_node.check_execution_nodes(self.functions)
        if result != True:
            print("Missing a code definition for action/condition: " + result)
            return
    
    def fill_definitions(self, definitions):
        self.root_node.verify_definitions(definitions)

    def __get_template(self):
        with open('Simulator.template.py', 'r') as f:
            return f.read()

    def to_python_string_test(self, indent = 1):
        behavior_tree_str = self.code_str + "\n\n"
        behavior_tree_str += self.root_node.to_python_string(indent)
        behavior_tree_str += "\n" + indent * 4 * ' ' + "ROOT_NODE = {}_NODE".format(self.root_node.name.upper())
        return behavior_tree_str

    def to_python_string(self, indent = 1):
        template_str = self.__get_template()
        behavior_tree_str = self.root_node.to_python_string(indent)

        behavior_tree_str += "\n" + indent * 4 * ' ' + "ROOT_NODE = {}_NODE".format(self.root_node.name.upper())
        final_str = template_str.replace("{CODE}", self.code_str)
        final_str = final_str.replace("{TREE}", behavior_tree_str)
        return final_str


    def to_latex_str(self):
        return "\\documentclass{article}\n" + \
            "\\usepackage{amsmath}\n" + \
            "\\usepackage{amssymb}\n" + \
            "\\usepackage{tikz}\n" + \
            "\\usepackage{forest}\n" + \
            "\\usepackage{../report/behaviortrees}\n" + \
            "\\begin{document}\n" + \
            "\\begin{behavior}\n" + (" " * 4) + \
            "[\\rootnode\n" + self.root_node.to_latex_str(indent=2) + \
            (" " * 4) + "]\n\\end{behavior}\n" + \
            "\\end{document}\n"