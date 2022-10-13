
from collections import deque


num=int(input())
n=int(input())
dic={}
for i in range(num):
    dic[i]=set()

for _ in range(n):
    a,b=map(int,input().split())
    dic[a-1].add(b-1)
    dic[b-1].add(a-1)


#노드 0번부터 시작으로 계산
#dic={0: {1, 4}, 1: {0, 2, 4}, 2: {1}, 3: {6}, 4: {0, 1, 5}, 5: {4}, 6: {3}}
visited=[False]*num #해결!! n,num 변수명 헷갈림

def bfs(start,visited):
    que=deque()
    que.append(start)
    visited[start]=True

    while que:
        node=que.popleft()
        for val in dic[node]: 
            if visited[val]==False:
                que.append(val)
                visited[val]=True

bfs(0,visited)
#visited=[True, True, True, False, True, True, False]
cnt=0
for v in visited:
    if v==True:
        cnt+=1
print(cnt-1)

