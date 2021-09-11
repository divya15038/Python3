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

class Stacks:
    def __init__(self, name):
        self.name = name
        self.limit = 1000
        self.size = 0
        self.top_item = None

    def is_empty(self):
        return self.size == 0

    def has_space(self):
        if self.limit > self.size:
            return True
        return False

    def push(self, value):
        if self.has_space():
            new_node = Node(value)
            new_node.set_next_node(self.top_item)
            self.top_item = new_node
            self.size += 1
        else:
            print("No more space in the stack!")

    def pop(self):
        if not self.is_empty():
            removed_item = self.top_item
            self.top_item = removed_item.get_next_node()
            self.size -= 1
            return removed_item.get_value()
        print("No item to pop in stack!")

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        print("No item in stack to peek!")

    def get_name(self):
        return self.name

    def print_items(self):
        ptr = self.top_item
        list_items = []
        while ptr:
            list_items.append(ptr)
            ptr = self.top_item.get_next_node()
        list_items.reverse()
        print("{} Stack: {}".format(self.get_name, list_items))