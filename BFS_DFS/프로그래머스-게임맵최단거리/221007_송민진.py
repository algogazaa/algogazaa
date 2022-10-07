from collections import deque

def solution(maps):
    x, y = 0, 0
    n = len(maps)
    m = len(maps[0])
    queue = deque()
    queue.append((x, y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for di in range(4):
            nx = x + dx[di]
            ny = y + dy[di]
            if nx >= len(maps) or ny >= len(maps[0]) or nx < 0 or ny < 0:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                
    if maps[n-1][m-1] in [0, 1]:
        return -1
    else:
        return maps[n-1][m-1]
