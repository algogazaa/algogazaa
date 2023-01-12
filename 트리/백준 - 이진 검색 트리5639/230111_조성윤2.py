import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
class Tree:
    def __init__(self, id):
        self.id = id
        self.right = None
        self.left = None

nodeTree = []
while True:
    try:
        n = int(input())
        nodeTree.append(Tree(n))
    except:
        break

def addNode(root, child):
    if root.id > child.id:
        if root.left == None:
            root.left = child
        else:
            addNode(root.left,child)
    else:
        if root.right == None:
            root.right = child
        else:
            addNode(root.right, child)
            
def postOrder(root):
    if root == None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.id)
   
def makeTree():
    root = nodeTree[0]
    for i in range(1,len(nodeTree)):
        addNode(root,nodeTree[i])
    
    postOrder(root)

makeTree()