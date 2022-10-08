from collections import deque


def solution(n, m, fires, ices):
    frame = [[0 for _ in range(n)] for _ in range(n)]

    for i in fires:
        fire(n, i[0]-1, i[1]-1, m-1, frame)

    for j in ices:
        ice(n, j[0]-1, j[1]-1, m-1, frame)

    print(frame)


def fire(n, i, j, k, frames):
    dx = [1, 1, 1, -1, -1, -1, 0, 0]
    dy = [1, 0, -1, 0, 1, -1, 1, -1]

    isvisited = [[False for _ in range(n)]for _ in range(n)]

    queue = deque()
    queue.append([i, j, k+1])
    frames[i][j] += k+1

    while queue:
        a, b, c = queue.popleft()
        isvisited[a][b] = True

        for w in range(8):
            nx = a + dx[w]
            ny = b + dy[w]

            if 0<= nx < n and 0<= ny < n:
                if isvisited[nx][ny] == False:
                    isvisited[nx][ny] = True
                    frames[nx][ny] += c
                    queue.append([nx, ny, c-1])


def ice(n, i, j, k, frames):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    isvisited = [[False for _ in range(n)]for _ in range(n)]

    queue = deque()
    queue.append([i, j, k+1])
    frames[i][j] += -(k+1)

    while queue:
        a, b, c = queue.popleft()
        isvisited[a][b] = True

        for w in range(4):
            nx = a + dx[w]
            ny = b + dy[w]

            if 0<= nx < n and 0<= ny < n:
                if isvisited[nx][ny] == False:
                    isvisited[nx][ny] = True
                    frames[nx][ny] -= 1 * c
                    queue.append([nx, ny, c-1])

a = [[1, 1]]
b = [[3, 3]]
c = [[5, 5], [1, 3], [5, 2]]
d = [[1, 5], [3, 2]]

solution(5, 3, c, d)