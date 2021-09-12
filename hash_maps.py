from indianStatesCapitals_lib import Indian_states

class Node:
  def __init__(self, value):
    self.value = value
    self.next_node = None
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, head_node=None):
    self.head_node = head_node
  
  def insert(self, new_node):
    current_node = self.head_node

    if not current_node:
      self.head_node = new_node

    while(current_node):
      next_node = current_node.get_next_node()
      if not next_node:
        current_node.set_next_node(new_node)
      current_node = next_node

  def __iter__(self):
    current_node = self.head_node
    while(current_node):
      yield current_node.get_value()

class HashMap:  
  def __init__(self, array_size = 0):
    self.array_size = array_size
    self.array = [LinkedList() for i in range(self.array_size)]

  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code

  def compress(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for element in list_at_array:   
      if key == element[0]:
        element = [key, value]    
      return
    list_at_array.insert(payload)


  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    for item in list_at_index:
      if item[0] == key:
        return item[1]
      return None

india = HashMap(28)
for state in Indian_states:
  india.assign(state[0], state[1])

#taking input from user
user_input = (input("Enter an Indian state?:")).capitalize()

#Checking for a valid input
flag = True
for state in Indian_states:
  if user_input == state[0]:
    flag = False
if flag:    
  print("Enter valid state name!")
else:
  print("The capital of {} is {}".format(user_input, india.retrieve(user_input)))

