import copy
from collections import deque

a, b = map(int,input().split())

def bfs(a):
    q = deque()
    isvisited = [False for _ in range(100001)]
    isvisited[a] = True
    q.append([a, 0, isvisited])

    dx = [1, -1, 2]

    while q:
        location, dis, visited = q.popleft()
        if location == b:
            return dis
        for i in range(3):
            if i == 2:
                n_location = location * dx[i]
            else:
                n_location = location + dx[i]
            if 0<= n_location < 100001:
                if not visited[n_location]:
                    real_vis = copy.deepcopy(visited)
                    real_vis[n_location] = True
                    n_dis = dis + 1
                    q.append([n_location, n_dis, real_vis])



print(bfs(a))