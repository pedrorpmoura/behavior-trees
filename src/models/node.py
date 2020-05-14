class Node(object):
    """
    Class that represents a node in a behavior tree.
    """

    def __init__(self, name, reference=None):
        self.name = name
        self.reference = reference
        if reference:
            self.reference = reference.replace("$", "")
    
    def get_name(self):
        return self.name

    def get_reference(self):
        return self.reference