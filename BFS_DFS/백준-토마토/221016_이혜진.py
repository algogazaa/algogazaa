#런타임에러
#1 익은 토마토, 0 익지x 토마토, -1 토마토없음
import sys
from collections import deque

m,n,h=map(int,input().split())
g=[]
que=deque()
for k in range(h):
    tmp=[]
    for i in range(n):
        tmp.append(list(map(int,sys.stdin.readline().split)))
        for j in range(m):
            if tmp[i][j]==1: #익은 토마토만 que에 담기
                que.append((k,i,j))
    g.append(tmp)


dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]

def bfs(que):
    while que:
        z,y,x=que.popleft()
        #6방향 확인
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]
            #범위 벗어나면 무시
            if nx<0 or ny<0 or nz<0 or nx>=m or ny>=n or nz>=h:
                continue
            #토마토 없으면 무시
            if g[nz][ny][nx]==-1:
                continue
            #조건 해당
            if g[nz][ny][nx]==0:
                g[nz][ny][nx]==g[z][y][x]+1 
                que.append((nz,ny,nx))



bfs(que)

flag=False #토마토가 다 못익는가
for k in range(h):
    for i in range(n):
        for j in range(m):
            if g[k][i][j]==0: #안 익은 토마토가 있는경우
                flag==True
                break

g_max=[]
if flag==True:
    print(-1)
else:
    for k in range(h):
        g_max.append(max(map(max,g[k])))
    print(max(g_max))
