#※노드의 개수가 최대 100,000개 (>>>>파이썬에서 기본 지원하는 최대 재귀 깊이 1000)
# sys모듈의 setrecursionlimit함수를 사용, 최대 재귀 깊이를 늘려준다.

import sys
sys.setrecursionlimit(10**9) #안하면 런타임 에러

n=int(input())
g=[[] for _ in range(n+1)] 
visited=[False for _ in range(n+1)]
answer=dict()

for i in range(n-1):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)

def dfs(v):
    visited[v]=True
    for i in g[v]: #[6,4]
        if visited[i]==False:
            answer[i]=v
            dfs(i)

dfs(1)

#answer={6: 1, 3: 6, 5: 3, 4: 1, 2: 4, 7: 4}

for i in range(2,n+1):
    print(answer[i])
