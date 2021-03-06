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
        while ptr is not None:
            list_items.append(ptr.get_value())
            ptr = ptr.get_next_node()
        list_items.reverse()
        print("{} Stack: {}".format(self.get_name(), list_items))

#Introduction to the game
print("""The Tower of Hanoi (also called The problem of Benares Temple[1] or Tower of Brahma or Lucas' Tower[2] and sometimes pluralized as Towers, or simply pyramid puzzle[3]) is a mathematical game or puzzle consisting of three rods and a number of disks of various diameters, which can slide onto any rod. The puzzle begins with the disks stacked on one rod in order of decreasing size, the smallest at the top, thus approximating a conical shape. The objective of the puzzle is to move the entire stack to the last rod, obeying the following rules:
1.Only one disk may be moved at a time.
2.Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
3.No disk may be placed on top of a disk that is smaller than it.
With 3 disks, the puzzle can be solved in 7 moves. The minimal number of moves required to solve a Tower of Hanoi puzzle is 2^n ??? 1, where n is the number of disks.""")

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

#getting input from user for the number of disks to play the game with 
num_disks = int(input("Enter the number of disks you want to play the game with?"))

#checking if the num_disks is greater than 3, if not reasking the user
while num_disks < 3:
    print("\nEnter a number for disks which is greater than 3 for the game to be interesting.")
    num_disks = int(input("Enter the number of disks you want to play the game with?"))

#optimal no. of moves
optimal_moves = 2**num_disks - 1
print("The optimal no. of moves for {}: {}".format(num_disks, optimal_moves))

#pusing the disks into the left stack
for i in range(num_disks, 0, -1):
    left_stack.push(i)

#method for getting input from user
def get_input():
    choices = [stack.get_name()[0] for stack in stacks_list]
    while True:
        for i in range(0, len(stacks_list)):
            stack = stacks_list[i]
            letter = choices[i]
            print("Type {} for {}".format(letter, stack.get_name()))
        user_input = input("")
        if user_input in choices:
            for i in range(0, len(choices)):
                if user_input == choices[i]:
                    return stacks_list[i]
        else:
            print("Enter a valid option!!")

#setting up the game
user_moves = 0

while right_stack.size != num_disks:
    print("\n\nCurrent Stacks:")
    for stack in stacks_list:
        stack.print_items()

    while True:
        print("Which stack do you want to move from?")
        from_stack = get_input()
        print("Which stack do you want to move the disk to?")
        to_stack = get_input()

        if from_stack.is_empty():
            print("Invalid move!Try again:(")
        
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            value = from_stack.pop()
            to_stack.push(value)
            user_moves += 1
            break

        else:
            print("Invalid Move!Try Again:(")

#printing the result of the game
print("\n\nYou completed the game in {} moves, and the optimal number of moves is {}".format(user_moves, optimal_moves))

