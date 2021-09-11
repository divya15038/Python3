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
    #initialized stack
    def __init__(self, name):
        self.name = name
        self.limit = 1000
        self.size = 0
        self.top_item = None

    #method to check if stack is empty
    def is_empty(self):
        return self.size == 0

    #method to check if the stack has more space to accomodate more items in it
    def has_space(self):
        return self.limit > self.size
        
    #method to push an element into stack 
    def push(self, value):
        if self.has_space():
            new_node = Node(value)
            new_node.set_next_node(self.top_item)
            self.top_item = new_node
            self.size += 1
        else:
            print("No more space in the stack!")

    #method to remove an item from stack
    def pop(self):
        if not self.is_empty():
            removed_item = self.top_item
            self.top_item = removed_item.get_next_node()
            self.size -= 1
            return removed_item.get_value()
        print("No item to pop in stack!")

    #method to see the top element without removing it
    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        print("No item in stack to peek!")

    #returning the name of top item
    def get_name(self):
        return self.name

    #printing the items in a stack
    def print_items(self):
        ptr = self.top_item
        list_items = []
        while ptr:
            list_items.append(ptr)
            ptr = self.top_item.get_next_node()
        list_items.reverse()
        print("{} Stack: {}".format(self.get_name, list_items))

#Introduction to the game
print("""The Tower of Hanoi (also called The problem of Benares Temple[1] or Tower of Brahma or Lucas' Tower[2] and sometimes pluralized as Towers, or simply pyramid puzzle[3]) is a mathematical game or puzzle consisting of three rods and a number of disks of various diameters, which can slide onto any rod. The puzzle begins with the disks stacked on one rod in order of decreasing size, the smallest at the top, thus approximating a conical shape. The objective of the puzzle is to move the entire stack to the last rod, obeying the following rules:
1.Only one disk may be moved at a time.
2.Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
3.No disk may be placed on top of a disk that is smaller than it.
With 3 disks, the puzzle can be solved in 7 moves. The minimal number of moves required to solve a Tower of Hanoi puzzle is 2^n − 1, where n is the number of disks.""")

print("Let's play the game 'Towers of Hanoi!!All the best:))")

#Create the stacks
left_stack = Stacks("Left")
middle_stack = Stacks("Middle")
right_stack = Stacks("Right")

#Create a list containing stacks created
stacks_list = []
stacks_list.append(left_stack)
stacks_list.append(middle_stack)
stacks_list.append(right_stack)