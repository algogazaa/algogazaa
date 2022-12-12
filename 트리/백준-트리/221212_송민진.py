import sys
input = sys.stdin.readline

N = int(input())
parents = list(map(int, input().split()))
to_erase = int(input())
tree = [[] for _ in range(N)]

for i in range(len(parents)):
    if parents[i] != -1:
        tree[parents[i]].append(i)


def dfs(node):
    if len(tree[node]) > 0:
        for child in tree[node]:
            dfs(child)
    tree[node] = []
    parents[node] = -2


dfs(to_erase)

answer = 0
for node in range(N):
    if len(tree[node]) == 0 and parents[node] >= 0:
        answer += 1

print(answer)
