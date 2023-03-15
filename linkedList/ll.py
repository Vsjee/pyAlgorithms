class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def insert(self, val):
    n_node = Node(val)
    if (self.head):
      curr = self.head
      while (curr.next):
        curr = curr.next
      curr.next = n_node
    else:
      self.head = n_node

  def printLL(self):
    curr = self.head

    while(curr):
      print(curr.val, end="")
      if curr.next != None:
        print("->", end="")
      curr = curr.next

LL = LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
LL.printLL()