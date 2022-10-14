#
import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
m = int(input())
visited = [False] * (n + 1)
connection = defaultdict(list)
result = 0
for _ in range(m):
    a,b = map(int, input().split())
    connection[a].append(b)
    connection[b].append(a)
    
def dfs(start, result):
    visited[start] = True
    for i in connection[start]:
        if not visited[i]:
            result += 1
            result = dfs(i, result)
    
    return result        
print(dfs(1,result))