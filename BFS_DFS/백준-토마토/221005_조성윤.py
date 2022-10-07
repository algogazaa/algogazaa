#
import sys
from collections import deque
input = sys.stdin.readline

m,n,h = map(int, input().split())
graph = []
for _ in range(h):
    temp = []
    for _ in range(n):
        temp.append(list(map(int,input().split())))
    graph.append(temp)

start = []
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 1:
                start.append([z,x,y])

def bfs(start):
    q = deque(start)
    dx = [1,-1,0,0,0,0]
    dy = [0,0,1,-1,0,0]
    dz = [0,0,0,0,1,-1]
    while q:
        z,x,y = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                q.append([nz,nx,ny])
                
bfs(start)
result = 0
for i in graph:
    for j in i:
        if 0 in j:
            print(-1)
            result = -1
            break
        result = max(result, max(j))
    if result == -1:
        break
else:
    print(result-1)