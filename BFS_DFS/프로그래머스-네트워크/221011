from collections import deque


def solution(n, computers):
    visited=[False]*n
    cnt=0
    for i in range(n):
        if bfs(computers,i,visited)==True:
            cnt+=1
    return cnt

def bfs(g,start,visited):
    #이미 시작노드가 방문된 경우
    if visited[start]==True:
        return False
    
    que=deque()
    que.append(start)
    visited[start]=True
    while que:
        node=que.popleft()
        for i in range(len(g[node])): #g[node]=[1,1,0]..
            if g[node][i]==1 and visited[i]==False:
                que.append(i)
                visited[i]=True
    return True
