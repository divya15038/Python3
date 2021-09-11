class Node:
    #intializing node with value and link node
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
    
    #returning value of node
    def get_value(self):
        return self.value

    #returning linked node of a node
    def get_next_node(self):
        return self.next_node

    #setting next node for a node
    def set_next_node(self, next_node):
        self.next_node = next_node