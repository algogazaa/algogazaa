from collections import defaultdict

n = int(input())
m = int(input())
visited = [False for _ in range(n)]
connection = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    connection[a].append(b)
    connection[b].append(a)

def dfs(index, result):
    visited[index-1] = True
    for i in connection[index]:
        if not visited[i]:
            result += 1
            result = dfs(i, result)

    return result

print(dfs(1, 0))