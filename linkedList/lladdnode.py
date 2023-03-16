class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

class LinkedList:
  def __init__(self, nList):
    self.nList = nList

  def listToNodes(self):
    l = len(self.nList)
    for i in range(l):
      if i<l-1:
        n = Node(self.nList[i], self.nList[i+1])
        self.nList[i] = n
      else:
        n = Node(self.nList[i])
        self.nList[i] = n

  def insertNode(self, nNode: Node):
    self.nList.append(nNode)
    self.nList[-2].next = self.nList[-1]
  
  def printList(self):
    for i in range(len(self.nList)):
      print(self.nList[i].val, end="")
      if self.nList[i].next != None:
        print("->", end="")
    print("")
  
  def printFML(self):
    mid = int(len(self.nList)/2)
    print("first:", self.nList[0].val)
    if mid%2==0:
      print("mid", self.nList[mid-1].val, self.nList[mid].val)
    else:
      print("mid:", self.nList[mid].val)
    print("last:", self.nList[-1].val)
    print("")
      

print("insert the values like this: 1 2 3 ...")
lNodes = list(map(int, input().split()))

LL = LinkedList(lNodes)
LL.listToNodes()
LL.printList()
LL.printFML()

nVal = int(input("insert new node at the end: "))
n = Node(nVal)

LL.insertNode(n)
LL.printList()
LL.printFML()
