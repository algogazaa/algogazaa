from collections import deque


def solution(n, m, fires, ices):
    frame = [[0 for _ in range(n)] for _ in range(n)]
    for k in range(m):
        for i in range(n):
            for j in range(n):
                if [i+1, j+1] in fires:
                    fire(n, i, j, k+1, frame)
                if [i+1, j+1] in ices:
                    ice(n, i, j, k+1, frame)
    print(frame)


def fire(n, i, j, k, frames):
    dx = [1, 1, 1, -1, -1, -1, 0, 0]
    dy = [1, 0, -1, 0, 1, -1, 1, -1]

    isvisited = [[False for _ in range(n)]for _ in range(n)]

    queue = deque()
    queue.append([i, j, 0])
    frames[i][j] += 1

    while queue:
        a, b, c = queue.popleft()
        isvisited[a][b] = True

        for w in range(8):
            nx = a + dx[w]
            ny = b + dy[w]
            nc = c + 1

            if 0<= nx < n and 0<= ny < n and nc <= k:
                if isvisited[nx][ny] == False:
                    isvisited[nx][ny] = True
                    frames[nx][ny] += 1
                    queue.append([nx, ny, nc])


def ice(n, i, j, k, frames):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    isvisited = [[False for _ in range(n)]for _ in range(n)]

    queue = deque()
    queue.append([i, j, 0])
    frames[i][j] -= 1

    while queue:
        a, b, c = queue.popleft()
        isvisited[a][b] = True

        for w in range(4):
            nx = a + dx[w]
            ny = b + dy[w]
            nc = c + 1

            if 0<= nx < n and 0<= ny < n and nc <= k:
                if isvisited[nx][ny] == False:
                    isvisited[nx][ny] = True
                    frames[nx][ny] -= 1
                    queue.append([nx, ny, nc])

a = [[1, 1]]
b = [[3, 3]]
c = [[5, 5], [1, 3], [5, 2]]
d = [[1, 5], [3, 2]]

solution(5, 3, c, d)