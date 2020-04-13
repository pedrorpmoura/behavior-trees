class Node:
    """
    Class that represents a node in a behavior tree.
    """

    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name