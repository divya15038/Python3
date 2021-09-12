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

class LinkedList:
    #initialized a linkedlist with head node
    def __init__(self, value = None):
        self.head_node = Node(value)
    #returns value stored in head node
    def get_head_node(self):
        return self.head_node.get_value()
    #inserts new nodes into the linked list
    def insert(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.get_head_node())
        self.head_node = new_node
    #returns the elements in a linked list
    def stringify_list(self):
        string_list = []
        ptr = self.get_head_node()
        while ptr:
            if ptr.get_value() != None:
                string_list.append(ptr.get_value())
            ptr = ptr.get_next_node()
        return string_list
    #removes nodes of the linked list with a given value
    def removeNode(self, value_to_remove):
        current_node = self.get_head_node()
        #if the value is in the head node
        while current_node.get_value() == value_to_remove and current_node is not None:
            self.head_node = current_node.get_next_node()
            current_node = self.get_head_node()
        
        while current_node is not None and current_node.get_next_node() is not None:
            next_node = current_node.get_next_node()
            if next_node.get_value() == value_to_remove:
                current_node.set_next_node(next_node.get_next_node())
            else:
                current_node = next_node

class HashMap:
    #initializing a HashMap
    def __init__(self, array_size = None):
        self.array_size = array_size
        self.array = [LinkedList for i in range(array_size)]
    #returns hash code for a key
    def hash(self, key):
        return sum(key.encode())
    #returns array inex from hash code
    def compress(self, hash_code):
        return hash_code % self.array_size
    #assigns key to an array index
    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        new_node = Node([key, value])
        list_at_index = self.array[array_index]
        for item in list_at_index:
            if item[0] == key:
                item = [key, value]
                return
            list_at_index.append(new_node)
    #returns value for a given key
    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]
        for element in list_at_index:
            if element[0] == key:
                return element[1]
            return None