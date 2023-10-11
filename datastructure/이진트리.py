class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BST:
  def __init__(self, root):
    self.root = root
  
  def insert(self, value): # value가 입력값
    self.current_node = self.root # root값을 의미
    while True:
      if value < self.current_node: # root>self.current_node일 경우 
        if self.current_node != None:
          self.current_node = self.current_node.left
        else:
          self.current_node.left = Node(value)
          break
      
      else:
        if self.current_node.right != None:
          self.current_node = self.current_node.right
        else:
          self.current_node.right = Node(value)
          break

  def search(self, value): # key 값 자체는 value임
    self.current_node = self.root
    while self.current_node:
      if self.current_node.value == value :
        return True
      elif self.current_node.value > value:
        self.current_node = self.current_node.left
      else:
        self.current_node = self.current_node.right
    return False
  

