class Node:
    #initializes the node with a value and link for next node
    def __init__(self, value, link_node = None):
        self.value = value
        self.link_node = link_node
    #returns value for a given node
    def get_value(self):
        return self.value
    #sets the next node for a given node
    def set_next_node(self, next_node):
        self.link_node = next_node
    #returns the next node for a given node
    def get_next_node(self):
        return self.link_node