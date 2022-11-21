from collections import deque

n, m = list(map(int, input().split()))
count = n*m
visited = [[1 for _ in range(m)] for _ in range(n)]

q = list(map(int, input().split()))
k = list(map(int, input().split()))
p = list(map(int, input().split()))


def bfs(x, y, type, cnt):
    queue = deque()
    queue.append([x, y, 0, type])
    queue.append([x, y, 1, type])
    queue.append([x, y, 2, type])
    queue.append([x, y, 3, type])
    queue.append([x, y, 4, type])
    queue.append([x, y, 5, type])
    queue.append([x, y, 6, type])
    queue.append([x, y, 7, type])

    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]
    kx = [1, 1, -1, -1, 2, 2, -2, -2]
    ky = [2, -2, 2, -2, 1, -1, 1, -1]

    while queue:
        a, b, i, t = queue.popleft()
        if t == 'q':
            nx = a + dx[i]
            ny = b + dy[i]
        else:
            nx = a + kx[i]
            ny = b + ky[i]

        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 1:
            visited[nx][ny] = -1
            queue.append([nx, ny, i, t])
            cnt -= 1

    return cnt

pp = 1
for _ in range(len(p)//2):
    visited[p[pp]-1][p[pp+1]-1] = 0
    pp += 2
    count -= 1

qq = 1
for _ in range(len(q)//2):
    visited[q[qq]-1][q[qq+1]-1] = -2
    qq += 2
    count -= 1
kk = 1
for _ in range(len(k)//2):
    visited[k[kk]-1][k[kk+1]-1] = -2
    kk += 2
    count -= 1

qq = 1
for _ in range(len(q)//2):
    x = q[qq]-1
    y = q[qq+1]-1
    count = bfs(x, y, 'q', count)
    qq += 2

kk = 1
for _ in range(len(k)//2):
    count = bfs(k[kk]-1, k[kk+1]-1, 'k', count)
    kk += 2

print(count)
print(visited)