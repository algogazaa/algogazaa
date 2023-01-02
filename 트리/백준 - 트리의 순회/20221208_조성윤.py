#
import sys
input = sys.stdin.readline
n = int(input())
inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))

class Tree:
    def __init__(self, node, left, right):
        self.value = node
        self.left = left
        self.right = right
def findIdx(arr, start, root):
    for i in range(start, len(arr)):
        if arr[i] == root:
            return i
    
def makeTree(inOrder, postOrder, inStart, pStart, size):
    if size <= 0:
        return None
    
    root = postOrder[pStart + size - 1]
    rootIdx = findIdx(inOrder, inStart, root)
    leftTreeSize = rootIdx - inStart
    rightTreeSize = size - rootIdx - 1
    leftTree = makeTree(inOrder, postOrder, inStart, pStart, leftTreeSize)
    rightTree = makeTree(inOrder, postOrder, rootIdx + 1, pStart + leftTreeSize, rightTreeSize)
    return Tree(root, leftTree, rightTree)

tree = makeTree(inOrder, postOrder, 0, 0, n)
