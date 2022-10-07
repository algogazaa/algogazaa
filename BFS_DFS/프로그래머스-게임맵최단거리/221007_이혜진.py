from collections import deque

def solution(maps):
    return bfs(maps,0,0)

def bfs(g,sx,sy):
    n=len(g)
    m=len(g[0])
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    que=deque()
    que.append((sx,sy))
    visited=[[False]*m for n in range(5)]
    #큐가 빌 때까지 반복
    while que:
        x,y=que.popleft()
        #BFS소스코드 구현
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and g[nx][ny]==1:
                g[nx][ny]=g[x][y]+1
                que.append((nx,ny))
                visited[nx][ny]=True

    if visited[m-1][n-1]==False:
        return -1
    else:
        return g[m-1][n-1]


if __name__ == "__main__":
    #11,-1
    board=[[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]],[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]]
    for b in board:
        print(solution(b))
