from collections import deque

m, n, h = map(int, input().split())
box = []
tomato = deque([])
day = 0

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, input().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                tomato.append([i, j, k])
    box.append(tmp)

# 3차원 방향 설정
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while tomato:
    x, y, z = tomato.popleft()
    for i in range(5):
        nx = x + dx[i]
        ny = y - dy[i]
        nz = z + dz[i]
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and box[nx][ny][nz] == 0:
            # 비교한 토마토에 기존 토마토 + 1 (하루 지나는 것 구현)
            box[nx][ny][nz] = box[x][y][z] + 1
            tomato.append([nx, ny, nz])

    for i in box:
        for j in i:
            for k in j:
                if k == 0:
                    print(-1)
                    exit()
            day = max(day, max(j))

# 처음부터 익은 토마토가 존재하고, 따라서 시작점이 1이기 때문에 day - 1
print(day - 1)
