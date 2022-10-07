from collections import deque
from typing import List
def solution(n: int, m: int, fires: List[List[int]], ices: List[List[int]]) -> List[List[int]]:
    answer = []
    graph = [[0] * n for _ in range(n)]

    for f in fires:
        temp = [f[0]-1, f[1]-1,m]
        visited = [[False] * n for _ in range(n)]
        bfs(n,temp, graph,visited, 1)
        
    for ic in ices:
        temp = [ic[0]-1, ic[1]-1,m]
        visited = [[False] * n for _ in range(n)]
        bfs(n,temp, graph,visited, -1)
    
    for g in graph:
        answer.append(g)
    return answer

def bfs(n,start, graph, visited, changeTemp):
    
    q = deque([start])
    visited[start[0]][start[1]] = True
    if changeTemp == 1:
        graph[start[0]][start[1]] += start[2]
    else:
        graph[start[0]][start[1]] -= start[2]
    fire_dx = [0,0,1,-1,1,-1,1,-1]
    fire_dy = [1,-1,0,0,-1,1,1,-1]
    ice_dx = [0,0,1,-1]
    ice_dy = [1,-1,0,0]
    while q:
        x,y,canMove = q.popleft()
        if changeTemp == 1:
            for i in range(len(fire_dx)):
                nx = fire_dx[i] + x
                ny = fire_dy[i] + y
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and canMove != 0:
                    graph[nx][ny] += canMove
                    visited[nx][ny] = True
                    q.append([nx,ny,canMove - 1])
        else:
            for i in range(len(ice_dx)):
                nx = ice_dx[i] + x
                ny = ice_dy[i] + y
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and canMove != 0:
                    graph[nx][ny] -= canMove
                    visited[nx][ny] = True
                    q.append([nx,ny,canMove - 1])

if __name__ == "__main__":
    n = [5,3]
    m = [3,2]
    fires  = [[[5,5],[1,3],[5,2]],[[1,1]]]
    ices = [[[1,5],[3,2]],[[3,3]]]
    for a,b,c,d in zip(n,m,fires,ices):
        print(solution(a,b,c,d))