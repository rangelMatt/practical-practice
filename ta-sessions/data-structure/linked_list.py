class LinkedList:
  
  def __init__(self, value=[], next=None):
    # initialize
    self.head = None
    self.value = value
    self.next = next
    
class Node:
  
  # create the box
  def __init__(self, value, next=None):
    #the box is holding the value
    self.value = value
    # the label
    self.next = next
    
class Queue:
  
  def __init__(self):
    self.rear = None
    self.front = None
    
class Stack:
  
  def __init__(self):
    self.top = None

class BinaryTree:
  def __init__(self):
    self.root = None
    
class BinarySearchTree(BinaryTree):
  def add(self, value):
    
    def climb(root,new_node):
      #base case
      if not root:
        return
      
      if new_node.value == root.value:
        # go left
        if root.left:
          
          climb(root.left, new_node)
        else:
          root.left = new_node
        
      else:
          # go right
        if root.right:
          climb(root.right, new_node)
        else:
          root.right = new_node
    
    add_node = Node(value)      
    
    if not self.root:
      self.root = add_node
      return
          
        