from collections import deque


n,k=map(int,input().split())
visited=[0 for _ in range(100001)] 

def bfs(start):
    que=deque()
    que.append(start)
    while que:
        x=que.popleft()
        if x==k: #동생있는 곳 도착
            return visited[k]

        #갈 수 있는 방향
        nx_list=[x+1,x-1,x*2]
        for nx in nx_list:
            if 0<=nx<=100000: #x*2일때 visited범위를 넘어갈 수 있음
                if visited[nx]==0: #처음 방문
                    visited[nx]=visited[x]+1
                    que.append(nx)

print(bfs(n))
