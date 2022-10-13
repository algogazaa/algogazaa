import sys
from collections import deque

cnt = int(input())
m, n = map(int, input().split())
map = [list(map(int, input().split()))for _ in range(n)]
answer = sys.maxsize


def bfs(q):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    mx = [-2, -2, -1, -1, 1, 1, 2, 2]
    my = [1, -1, 2, -2, 2, -2, 1, -1]

    result = -1

    while q:
        x, y, count, dis, visited = q.popleft()

        if x == n and y == m:
            if result == -1:
                result = dis
            else:
                result = min(result, dis)

        if count != 0:
            for i in range(8):
                nx = mx[i] + x
                ny = my[i] + y
                n_count = cnt - 1
                n_dis = dis + 1

                if 0 <= nx < n and 0 <= ny < m:
                    if map[nx][ny] != 1 and visited[nx][ny] == False:
                        visited[nx][ny] = True
                        q.append([nx, ny, n_count, n_dis, visited])

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            n_dis = dis + 1

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if map[nx][ny] != 1:
                    visited[nx][ny] = True
                    q.append([nx, ny, count, n_dis, visited])

    return dis


isvisited = [[False for _ in range(m)]for _ in range(n)]
queue = deque()
queue.append([0, 0, cnt, 0, isvisited])
isvisited[0][0] = True
result = bfs(queue)
print(result)



