class Node:
  def __init__(self, val: int):
    self.val = val
    self.left = None
    self.rigth = None

class BinTreeDps:
  def preDps(self, n: Node):
    if n == None:
      return
    print(n.val, end=" ")
    self.preDps(n.left)
    self.preDps(n.rigth)

  def inDps(self, n: Node):
    if n == None:
      return
    self.inDps(n.left)
    print(n.val, end=" ")
    self.inDps(n.rigth)

  def postDps(self, n: Node):
    if n == None:
      return
    self.postDps(n.left)
    self.postDps(n.rigth)
    print(n.val, end=" ")

traverse = BinTreeDps()

head = Node(1)
head.left = Node(2)
head.rigth = Node(3)
head.left.left = Node(4)

print("preorder traversal: ", end=" ")
traverse.preDps(head)
print()

print("inorder traversal: ", end=" ")
traverse.inDps(head)
print()

print("postorder traversal: ", end=" ")
traverse.postDps(head)