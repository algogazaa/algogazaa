#런타임 에러

from collections import deque


num=int(input())
n=int(input())
dic={}
for i in range(num):
    dic[i+1]=set()

for _ in range(n):
    a,b=map(int,input().split())
    dic[a].add(b)
    dic[b].add(a)

#dic={1: {2, 5}, 2: {1, 3, 5}, 3: {2}, 4: {7}, 5: {1, 2, 6}, 6: {5}, 7: {4}}

visited=[False]*n

def bfs(start,visited):
    que=deque()
    que.append(start)
    visited[start]==True
    while que:
        node=que.popleft()
        for val in dic[node]:
            if visited[val-1]==False:
                que.append(val)
                visited[val-1]=True

bfs(1,visited)
cnt=0
for v in visited:
    if v==True:
        cnt+=1
print(cnt-1)
