import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

position = [0 for _ in range(n + 1)]
for i in range(n):
	position[inorder[i]] = i

def preOrder(inStart, pStart, size):
	if size <= 0:
		return
	root = postorder[pStart + size - 1]
	rootIdx = position[root]
	leftSize = rootIdx - inStart
	rightSize = size - leftSize - 1
	print(root, end = " ")
	preOrder(inStart, pStart, leftSize)
	preOrder(rootIdx + 1, pStart + leftSize, rightSize)

preOrder(0,0,n)