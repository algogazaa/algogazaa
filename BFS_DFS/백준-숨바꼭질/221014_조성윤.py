# 그래프 탐색, 이론, bfs
from collections import deque
n,k = map(int, input().split())
dist = [0] * (10**5 + 1)

def bfs():
    q = deque([n])

    while q:
        start = q.popleft()
        if start == k:
            print(dist[start])
            break
        for i in (start-1, start + 1, start *2):
            if 0<= i <= 100000 and dist[i] == 0:
                dist[i] = dist[start] + 1
                q.append(i)

bfs()