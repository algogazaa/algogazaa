import sys
sys.setrecursionlimit(10**6)
class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.right = None
        self.left = None
    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x
        return self.y > other.y

def addNode(root, child):
    if root.x > child.x :
        if root.left == None:
            root.left = child
        else:
            addNode(root.left, child)
    else:
        if root.right == None:
            root.right = child
        else:
            addNode(root.right, child)

def preOrder(answer, root):
    if root == None:
        return
    
    # root 넣기
    answer[0].append(root.id)
    # 왼쪽 노드 순회
    preOrder(answer, root.left)
    # 오른쪽 노드 순회
    preOrder(answer, root.right)
    
    return

def postOrder(answer, root):
    if root == None:
        return
    # 왼쪽 노드 순회
    postOrder(answer, root.left)
    # 오른쪽 노드 순회
    postOrder(answer, root.right)
    # root 넣기
    answer[1].append(root.id)
    return

def solution(nodeinfo):
    nodeList = []
    for i in range(len(nodeinfo)):
        nodeList.append(Node(i + 1, nodeinfo[i][0], nodeinfo[i][1]))
    
    nodeList.sort()
    root = nodeList[0]
    for i in range(1, len(nodeList)):
        addNode(root, nodeList[i])
    
    answer = [[],[]]
    preOrder(answer, root)
    postOrder(answer, root)
    
    return answer


if __name__ == "__main__":
    nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
    print(solution(nodeinfo))