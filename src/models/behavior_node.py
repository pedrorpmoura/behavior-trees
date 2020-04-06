
class Behavior:
    def __init__(self, node, code):
        self.root_node = node
        self.code_str = code

    def __str__(self): 
        return str(self.root_node)

    