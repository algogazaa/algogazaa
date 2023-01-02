#
import sys
input = sys.stdin.readline
n = int(input())
tree = list(map(int, input().split()))
k = int(input())
result = 0
def dfs(deleteNode, tree):
    tree[deleteNode] = -2
    for i in range(n):
        if tree[i] == deleteNode:
            dfs(i, tree)

dfs(k, tree)

for i in range(n):
    if tree[i] != -2 and i not in tree:
        result += 1
        
print(result)