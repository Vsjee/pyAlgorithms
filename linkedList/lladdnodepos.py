class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

class LinkedList:
  def __init__(self, nList):
    self.nList = nList
  
  def listToNode(self):
    l = len(self.nList)
    for i in range(l):
      if i<l-1:
        n = Node(self.nList[i], self.nList[i+1])
        self.nList[i] = n
      else:
        n = Node(self.nList[i])
        self.nList[i] = n
      
  def printList(self):
    for i in range(len(self.nList)):
      print(self.nList[i].val, end="")
      if self.nList[i].next != None:
        print("->", end="")
    print("")

  def insertNode(self, n: Node, pos: int):
    if len(self.nList) == pos:
      self.nList.append(n)
      self.nList[-2].next = self.nList[-1]
    elif pos == 0:
      self.nList.insert(pos, n)
      self.nList[pos].next = self.nList[pos+1]
    else:
      self.nList.insert(pos, n)
      self.nList[pos-1].next = self.nList[pos]
      self.nList[pos].next = self.nList[pos+1]

  def listLen(self):
    return len(self.nList)

print("insert the values like this: 1 2 3 ...")
nList = list(map(int, input().split()))

LL = LinkedList(nList)
LL.listToNode()
LL.printList()

currListLen = LL.listLen()
print("availables index: 0", currListLen)
print("insert a new node: 1[val] 2[pos]")

nNode = list(map(int, input().split()))
n = Node(nNode[0])

LL.insertNode(n, nNode[-1])
LL.printList()