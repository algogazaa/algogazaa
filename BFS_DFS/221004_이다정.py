from collections import deque

M, N, H = map(int, input().split())

tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx = [0,1,0,-1,0,0]
dy = [1,0,-1,0,0,0]
dz = [0,0,0,0,1,-1]

done_idx = deque()
max_cnt = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                done_idx.append([i,j,k])

while done_idx:
    z,y,x = done_idx.popleft()
    for i in range(6):
        nz = z+dz[i]
        ny = y+dy[i]
        nx = x+dx[i]
        if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
            if tomato[nz][ny][nx] == 0:
                max_cnt = tomato[z][y][x]
                tomato[nz][ny][nx] = max_cnt + 1
                done_idx.append([nz, ny, nx])

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 0:
                print(-1)
                exit(0)

print(max_cnt)


### 시간 초과 .....PyPy3?
