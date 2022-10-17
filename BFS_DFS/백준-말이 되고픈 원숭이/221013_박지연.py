import copy
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
        x, y, count, dis, visitedd = q.popleft()

        if x == n-1 and y == m-1:
            return dis

        if count != 0:
            for i in range(8):
                nx = mx[i] + x
                ny = my[i] + y
                n_count = count - 1
                n_dis = dis + 1

                if 0 <= nx < n and 0 <= ny < m:
                    if map[nx][ny] != 1 and visitedd[nx][ny] == False:
                        # real_vis = copy.deepcopy(visitedd)
                        real_vis = [item[:] for item in visitedd]
                        real_vis[nx][ny] = True
                        q.append([nx, ny, n_count, n_dis, real_vis])

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            n_dis = dis + 1

            if 0 <= nx < n and 0 <= ny < m and visitedd[nx][ny] == False:
                if map[nx][ny] != 1:
                    # real_vis = copy.deepcopy(visitedd)
                    real_vis = [item[:] for item in visitedd]
                    real_vis[nx][ny] = True
                    q.append([nx, ny, count, n_dis, real_vis])

    return result


isvisited = [[False for _ in range(m)]for _ in range(n)]
queue = deque()
queue.append([0, 0, cnt, 0, isvisited])
isvisited[0][0] = True
result = bfs(queue)
print(result)

# 이차원 배열의 경우 slicing으로 복사시
# a = [[1,2],[3,4]]
# temp = [i[:] for i in a]
# 이렇게 복사해야 deepcopy와 같은 효과가 난다.
# temp = a[:]인 경우 temp = a와 같다.


#반례
# 1
# 4 4
# 0 0 0 0
# 0 0 0 0
# 0 0 1 1
# 0 0 1 0


