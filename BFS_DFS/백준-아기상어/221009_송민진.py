from collections import deque

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]


# 기본 설정
baby_size = [2, 0]
now_x, now_y = 0, 0
result = 0

for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            now_x, now_y = i, j
            space[now_x][now_y] = 0
            break


# 함수 1 : 모든 위치까지의 최단거리 죄다 계산
def bfs():
    distance = [[-1] * n for _ in range(n)]
    distance[now_x][now_y] = 0

    queue = deque()
    queue.append((now_x, now_y))

    dx = [0, -1, 1, 0]
    dy = [1, 0, 0, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if space[nx][ny] <= baby_size[0] and distance[nx][ny] == -1:
                    queue.append((nx, ny))
                    distance[nx][ny] = distance[x][y] + 1
    return distance


# 함수 2 : 목적지 (먹을 물고기) 찾기
def find_fish(distance):
    target_x, target_y = 0, 0
    min_distance = 1e9

    # 먹을 물고기가 있는지 찾기
    for i in range(n):
        for j in range(n):
            if distance[i][j] != -1 and 1 <= space[i][j] < baby_size[0]:
                if distance[i][j] < min_distance:
                    target_x, target_y = i, j
                    min_distance = distance[i][j]

    # 더이상 먹을 물고기가 존재하지 않을 때,
    if min_distance == 1e9:
        return None

    # 먹을 물고기가 존재할 때,
    else:
        # 목적지의 x, y좌표 및 목적지까지의 거리 리턴
        return target_x, target_y, min_distance


# 계산하기
while True:
    # 먹을 물고기가 있는지 + 그 물고기까지의 최단거리 한 번에 계산
    value = find_fish(bfs())

    # 더이상 먹을 물고기가 존재하지 않으면,
    if value is None:
        print(result)
        break

    # 먹을 물고기가 존재함 -> 계속 반복문 돌림
    else:
        now_x, now_y = value[0], value[1]
        result += value[2]
        space[now_x][now_y] = 0
        baby_size[1] += 1
        # 아기상어 성장
        if baby_size[1] == baby_size[0]:
            baby_size[0] += 1
            baby_size[1] = 0
