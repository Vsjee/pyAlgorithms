class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.rigth = None

class BinTreeTraverse:
  def printTree(self, head):
    queue = []
    queue.append(head)
    while(len(queue)!= 0):
      l = len(queue)
      if l == 0:
        break

      for i in range(l):
        print(queue[i].val, end=" ")

        if(queue[i].left != None):
          queue.append(queue[i].left)
        
        if(queue[i].rigth != None):
          queue.append(queue[i].rigth)

        queue.reverse()
        queue.pop()
        queue.reverse()
      
      print()

traverse = BinTreeTraverse()

head = Node(1)
head.left = Node(2)
head.rigth = Node(3)
head.left.left = Node(4)

traverse.printTree(head)
