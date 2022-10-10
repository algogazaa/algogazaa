from collections import deque

def bfs(q):

    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    while q:
        x, y, weight, eat, dis, sum_eat, space, isvisited = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0<= ny < n:
                if space[nx][ny] == 0:
                    if isvisited[nx][ny] == False:
                        isvisited[nx][ny] = True
                        q.append([nx, ny, weight, eat, dis+1, sum_eat, space, isvisited])
                elif space[nx][ny] < weight:
                    isvisited = [[False for _ in range(n)] for _ in range(n)]
                    isvisited[nx][ny] = True
                    eat += 1
                    space[nx][ny] = 0
                    if eat == weight:
                        eat = 0
                        weight += 1
                        q.append([nx, ny, weight, eat, dis+1, sum_eat+1, space, isvisited])
                    else:
                        q.append([nx, ny, weight, eat+1, dis+1, sum_eat+1, space, isvisited])

    return 0

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
shark_location_x = 0
shark_location_y = 0
for i in range(n):
    for j in range(n):
        if space[i][j] != 9 and space[i][j] != 0:
            cnt += 1
        if space[i][j] == 9:
            shark_location_x = i
            shark_location_y = j

queue = deque()
isvisited = [[False for _ in range(n)]for _ in range(n)]
isvisited[shark_location_x][shark_location_y] = True
# 상어 현재 위치 x, y, 현재 상어 크기, 현재 먹은 물고기 수, 현재 거리, 총 먹은 물고기 수
queue.append([shark_location_x, shark_location_y, 2, 0, 0, 0, space, isvisited])
answer = bfs(queue)