#
import sys
from collections import deque
input = sys.stdin.readline
k = int(input())
w,h = map(int, input().split())
graph = []

for _ in range(h):
    graph.append(list(map(int, input().split())))

visited = [[[False] * (k + 1) for _ in range(w)] for _ in range(h)]

def bfs(x, y, k):
    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
    hx, hy = [-2, -2, -1, 1, 2, 2, -1, 1], [-1, 1, -2, -2, -1, 1, 2, 2]
    q = deque([[x,y,k,0]])
    visited[x][y][k] = True
    
    while q:
        x,y,hmove,totalMove = q.popleft()
        if x == h-1 and y == w-1:
            return totalMove
        
        if hmove > 0 : # 말 움직임으로 움직이는 경우
            for i in range(8):
                nx = x + hx[i]
                ny = y + hy[i]
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny][hmove-1] and graph[nx][ny] == 0:
                    visited[nx][ny][hmove-1] = True
                    q.append([nx,ny,hmove - 1, totalMove + 1])
                    
 
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny][hmove] and graph[nx][ny] == 0:
                visited[nx][ny][hmove] = True
                q.append([nx,ny,hmove, totalMove + 1])
    
    return -1

print(bfs(0,0,k))