import copy
from collections import deque

n, m, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(m)] for _ in range(h)]
count = 0

def bfs(tomato2, queue):
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dh = [0, 0, 0, 0, 1, -1]

    count = 0

    k = queue.pop()
    c, b, a = k[0], k[1], k[2]

    for i in range(6):
        nx = a + dx[i]
        ny = b + dy[i]
        nh = c + dh[i]

        if 0<= nx < n and 0<= ny < m and 0<= nh < h:
            if tomato2[nh][ny][nx] == 0:
                count += 1
                tomato2[nh][ny][nx] = 1
    return count
day = 0
while True:
    num_tomato = 0
    tomato2 = []
    tomato2 = copy.deepcopy(tomato)
    for i in range(h):
        for j in range(m):
            for k in range(n):
                if tomato[i][j][k] == 1:
                    q = deque()
                    q.append([i, j, k])
                    count += bfs(tomato2, q)
                elif tomato[i][j][k] == 0:
                    num_tomato += 1
    if count == 0:
        if num_tomato != 0:
            day = -1
        elif day == 0 and num_tomato == 0:
            day = 0
        break
    tomato = tomato2
    day += 1
    count = 0

print(day)


