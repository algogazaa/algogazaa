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

# 노드 삭제 후 트리 재설정
tree = [[] for _ in range(N)]
for i in range(len(parents)):
    if parents[i] >= 0:
        tree[parents[i]].append(i)

answer = 0
for node in range(N):
    if len(tree[node]) == 0 and parents[node] >= 0:
        answer += 1

# 루트노드만 남을 경우 예외 처리
if answer == 0 and max(parents) == -1:
    answer = 1

print(answer)
