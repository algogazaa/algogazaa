import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)



n = int(input())
tree = [[] for _ in range(n + 1)]
parent = [-1 for _ in range(n + 1)]
parent[1] = 0

for _ in range(n - 1):
    node1, node2 = map(int, input().split())
    tree[node1].append(node2)
    tree[node2].append(node1)


def dfs(tree, node):
    for connected in tree[node]:
        if parent[connected] == -1:
            parent[connected] = node
            dfs(tree, connected)


dfs(tree, 1)
for child in range(2, n+1):
    print(parent[child])
