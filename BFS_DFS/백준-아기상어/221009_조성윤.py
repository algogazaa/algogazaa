# bfs
import sys
from collections import deque

INF = sys.maxsize
input = sys.stdin.readline
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

total_time = 0
visited = [[0 for _ in range(n)] for _ in range(n)]
shark_size = 2

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(start):
    global shark_size
    q = deque([start])

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0<= ny <n and not visited[nx][ny] and shark_size >= graph[nx][ny] and graph[nx][ny] != 9:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx,ny])

                

# 초기 값 9인 곳 찾기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            start = [i,j]

eat_cnt = 0

while True:
    # 먹을 수 있는 물고기 있는지 체크
    eat_list = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0 and graph[i][j] < shark_size:
                eat_list.append([i,j])

    if not eat_list: # 먹을 수 있는 물고기가 없다면 종료
        print(total_time)
        break

    else: # 먹을 수 있는 물고기가 있다면
        bfs(start) # 먹을 수 있는 물고기 찾기 순회
        x, y = start
        graph[x][y] = 0 # 첫 start는 0로 초기화
        min_dist = INF # 먹을 수 있는 물고기 중 최소 거리
        for can_start in eat_list:
            x, y = can_start
            if visited[x][y] != 0 and visited[x][y] < min_dist:
                min_dist = visited[x][y]
                start = [x,y]
        
        if min_dist == INF: # 먹을 수 있는 물고기가 있는 곳에 도달할 수 없다면
            print(total_time)
            break

        else: # 먹을 수 있는 물고기에 도달 할 수 있다면
            x, y = start
            graph[x][y] = 9
            total_time += visited[x][y]  
            eat_cnt += 1
            visited = [[0 for _ in range(n)] for _ in range(n)]
            if eat_cnt == shark_size:
                eat_cnt = 0
                shark_size += 1

            

